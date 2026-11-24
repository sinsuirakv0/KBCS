# v16.0.2 → v16.0.3 · 最優先の変更候補 (78)

[一覧の目次](README.md)

<a id="compare-b1e057c712b9745a9272ded39a933f2c"></a>

### [`00b691cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b691cc.md) → [`00b6a1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a1c0.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9d0.md) · 呼出先 8件 [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c5c9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9a0.md) · 呼出先 8件 [`006398ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/006398ac.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.14% / 新版 96.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6a2d8",
      "incomplete_value": true,
      "site": "00b6a2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
      "definition_site": "00b692e4",
      "incomplete_value": true,
      "site": "00b69304",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6a888",
      "incomplete_value": true,
      "site": "00b6a888",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:a43:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69894",
      "incomplete_value": true,
      "site": "00b69894",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:9f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 214,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6a950",
      "incomplete_value": true,
      "site": "00b6a950",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:651:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6995c",
      "incomplete_value": true,
      "site": "00b6995c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:4f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 234,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6a1f4",
      "READ",
      [
        "storage",
        "002c3170",
        null,
        null
      ]
    ],
    [
      "00b6a2d8",
      "READ",
      [
        "storage",
        "002c4320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6a3e0",
      "READ",
      [
        "storage",
        "002af3da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a1f4",
      "READ",
      [
        "storage",
        "002c31c0",
        null,
        null
      ]
    ],
    [
      "00b6a2d8",
      "READ",
      [
        "storage",
        "002c4370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6a3e0",
      "READ",
      [
        "storage",
        "002af4b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b691cc.md#insn-00b69200) · [`00b692c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b691cc.md#insn-00b692c0) · [`00b692dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b691cc.md#insn-00b692dc)
- 新版 [`00b6a1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a1c0.md#insn-00b6a1f4) · [`00b6a2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a1c0.md#insn-00b6a2b4) · [`00b6a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6a/00b6a1c0.md#insn-00b6a2d0)

~~~diff
- 00b69200 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:170:8"]]
- 00b69200 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00b69200 ["COPY", "register:5010:8", ["const:0:8"]]
- 00b69200 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00b6a1f4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1c0:8"]]
+ 00b6a1f4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00b6a1f4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00b6a1f4 ["COPY", "register:5018:8", ["const:0:8"]]
- 00b69200 bytes 405dc03d
+ 00b6a1f4 bytes 4071c03d
- 00b692c0 ["INT_ADD", "register:40f0:8", ["const:b692c0:8", "const:4:8"]]
- 00b692c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b6a2b4 ["INT_ADD", "register:40f0:8", ["const:b6a2b4:8", "const:4:8"]]
+ 00b6a2b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b692c0 bytes 28bb0394
+ 00b6a2b4 bytes 1fbb0394
- 00b692dc ["INT_ADD", "register:40f0:8", ["const:b692dc:8", "const:4:8"]]
- 00b692dc ["CALL", null, ["callee:00c59130:8"]]
+ 00b6a2d0 ["INT_ADD", "register:40f0:8", ["const:b6a2d0:8", "const:4:8"]]
+ 00b6a2d0 ["CALL", null, ["callee:00c59130:8"]]
- 00b692dc bytes a1bb0394
+ 00b6a2d0 bytes 98bb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a974da0f4de7deefb5c5ca723aefa7d"></a>

### [`00b6ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md) → [`00b6be4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6be4c.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba00.md) · 呼出先 5件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5bf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf90.md)
- 新版 呼出元 1件 [`00c5c9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9d0.md) · 呼出先 5件 [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5cf60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.60% / 新版 98.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6bf48",
      "incomplete_value": false,
      "site": "00b6bf4c",
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
            "const:761:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6af54",
      "incomplete_value": false,
      "site": "00b6af58",
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
            "const:694:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6c054",
      "incomplete_value": false,
      "site": "00b6c058",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b060",
      "incomplete_value": false,
      "site": "00b6b064",
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
            "const:d6d:8"
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
      "00b6bf48",
      "PARAM",
      [
        "storage",
        "002a9694",
        null,
        "string"
      ]
    ],
    [
      "00b6c054",
      "PARAM",
      [
        "storage",
        "002a4d6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6bf48",
      "PARAM",
      [
        "storage",
        "002a9761",
        null,
        "string"
      ]
    ],
    [
      "00b6c054",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md#insn-00b6af58) · [`00b6b064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md#insn-00b6b064) · [`00b6af34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md#insn-00b6af34)
- 新版 [`00b6bf4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6be4c.md#insn-00b6bf4c) · [`00b6c058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6be4c.md#insn-00b6c058) · [`00b6bf28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6be4c.md#insn-00b6bf28)

~~~diff
- 00b6af58 ["INT_ADD", "register:40f0:8", ["const:b6af58:8", "const:4:8"]]
- 00b6af58 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b6bf4c ["INT_ADD", "register:40f0:8", ["const:b6bf4c:8", "const:4:8"]]
+ 00b6bf4c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b6af58 bytes 86bf0394
+ 00b6bf4c bytes 7dbf0394
- 00b6b064 ["INT_ADD", "register:40f0:8", ["const:b6b064:8", "const:4:8"]]
- 00b6b064 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b6c058 ["INT_ADD", "register:40f0:8", ["const:b6c058:8", "const:4:8"]]
+ 00b6c058 ["CALL", null, ["callee:00c5bd40:8"]]
- 00b6b064 bytes 43bf0394
+ 00b6c058 bytes 3abf0394
- 00b6af34 ["INT_ADD", "register:40f0:8", ["const:b6af34:8", "const:4:8"]]
- 00b6af34 ["CALL", null, ["callee:00c5cf60:8"]]
+ 00b6bf28 ["INT_ADD", "register:40f0:8", ["const:b6bf28:8", "const:4:8"]]
+ 00b6bf28 ["CALL", null, ["callee:00c5cf60:8"]]
- 00b6af34 bytes 17c40394
+ 00b6bf28 bytes 0ec40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43920f0711cc7386c3f5b5178aeb968"></a>

### [`00b6df7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df7c.md) → [`00b6ef70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef70.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md) · 呼出先 17件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)
- 新版 呼出元 1件 [`00c5cda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cda0.md) · 呼出先 17件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 84.56% / 新版 84.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 14件, `store_condition` 5件, `store_destination` 11件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6efb0",
      "incomplete_value": false,
      "site": "00b6efb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfbc",
      "incomplete_value": false,
      "site": "00b6dfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "00b6f000",
      "incomplete_value": true,
      "site": "00b6f000",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e00c",
      "incomplete_value": true,
      "site": "00b6e00c",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6f148",
      "incomplete_value": true,
      "site": "00b6f148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e154",
      "incomplete_value": true,
      "site": "00b6e154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6efa4",
      "READ",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6efa8",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6efb0",
      "WRITE",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b6efa4",
      "READ",
      [
        "storage",
        "01127250",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6efa8",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6efb0",
      "WRITE",
      [
        "storage",
        "01127250",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df7c.md#insn-00b6dfbc) · [`00b6e00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df7c.md#insn-00b6e00c) · [`00b6e024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df7c.md#insn-00b6e024)
- 新版 [`00b6efb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef70.md#insn-00b6efb0) · [`00b6f000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef70.md#insn-00b6f000) · [`00b6f018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6ef70.md#insn-00b6f018)

~~~diff
- 00b6dfbc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:290:8"]]
- 00b6dfbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b6efb0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:250:8"]]
+ 00b6efb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b6dfbc bytes 089302b9
+ 00b6efb0 bytes 085302b9
- 00b6e00c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:298:8"]]
- 00b6e00c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b6f000 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:258:8"]]
+ 00b6f000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b6e00c bytes 354f01f9
+ 00b6f000 bytes 352f01f9
- 00b6e024 ["INT_ADD", "register:40f0:8", ["const:b6e024:8", "const:4:8"]]
- 00b6e024 ["CALL", null, ["callee:00c5c610:8"]]
+ 00b6f018 ["INT_ADD", "register:40f0:8", ["const:b6f018:8", "const:4:8"]]
+ 00b6f018 ["CALL", null, ["callee:00c5c610:8"]]
- 00b6e024 bytes 87b50394
+ 00b6f018 bytes 7eb50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6c2aeeb49ac5d59f03e33e2311814a"></a>

### [`00b6e388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e388.md) → [`00b6f37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f37c.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdf0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cdc0.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcf0.md) [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 80.82% / 新版 80.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6f39c",
      "incomplete_value": true,
      "site": "00b6f39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6f400",
      "incomplete_value": true,
      "site": "00b6f400",
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
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e40c",
      "incomplete_value": true,
      "site": "00b6e40c",
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
            "const:2b0:8"
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
      "definition_site": "00b6f428",
      "incomplete_value": true,
      "site": "00b6f428",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e434",
      "incomplete_value": true,
      "site": "00b6e434",
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
            "const:2d0:8"
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
      "00b6f390",
      "READ",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6f39c",
      "WRITE",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6f3a8",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6f390",
      "READ",
      [
        "storage",
        "01127250",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6f39c",
      "WRITE",
      [
        "storage",
        "01127250",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6f3a8",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e388.md#insn-00b6e3a8) · [`00b6e3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e388.md#insn-00b6e3d8) · [`00b6e408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e388.md#insn-00b6e408)
- 新版 [`00b6f39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f37c.md#insn-00b6f39c) · [`00b6f3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f37c.md#insn-00b6f3cc) · [`00b6f3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f37c.md#insn-00b6f3fc)

~~~diff
- 00b6e3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 00b6e3a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6f39c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:250:8"]]
+ 00b6f39c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b6e3a8 bytes 099102b9
+ 00b6f39c bytes 095102b9
- 00b6e3d8 ["INT_ADD", "register:40f0:8", ["const:b6e3d8:8", "const:4:8"]]
- 00b6e3d8 ["CALL", null, ["callee:00c5c2e0:8"]]
+ 00b6f3cc ["INT_ADD", "register:40f0:8", ["const:b6f3cc:8", "const:4:8"]]
+ 00b6f3cc ["CALL", null, ["callee:00c5c2e0:8"]]
- 00b6e3d8 bytes ceb30394
+ 00b6f3cc bytes c5b30394
- 00b6e408 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e408 ["INT_ADD", "register:40f0:8", ["const:b6e408:8", "const:4:8"]]
- 00b6e408 ["CALLIND", null, ["register:0:8"]]
+ 00b6f3fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6f3fc ["INT_ADD", "register:40f0:8", ["const:b6f3fc:8", "const:4:8"]]
+ 00b6f3fc ["CALLIND", null, ["register:0:8"]]
- 00b6e408 bytes 00013fd6
+ 00b6f3fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758d16bb6f1ca7cedc4ea54206263602"></a>

### [`00b6e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e4ac.md) → [`00b6f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f4a0.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bff0.md) · 呼出先 4件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md)
- 新版 呼出元 1件 [`00c5cfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cfc0.md) · 呼出先 4件 [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00c5bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5cda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cda0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.72% / 新版 80.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6f5d4",
      "incomplete_value": true,
      "site": "00b6f5d4",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e5e0",
      "incomplete_value": true,
      "site": "00b6e5e0",
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
            "const:141:8"
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
      "definition_site": "00b6f5d8",
      "incomplete_value": true,
      "site": "00b6f5d8",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e5e4",
      "incomplete_value": true,
      "site": "00b6e5e4",
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
            "const:144:8"
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
      "definition_site": "00b6f4c0",
      "incomplete_value": true,
      "site": "00b6f4c0",
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
      "definition_site": "00b6e4cc",
      "incomplete_value": true,
      "site": "00b6e4cc",
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
      "00b6f4b4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f4c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e4fc"
      ]
    ],
    [
      "00b6f4e4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6f4b4",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f4c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6f4f0"
      ]
    ],
    [
      "00b6f4e4",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e4ac.md#insn-00b6e510) · [`00b6e544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e4ac.md#insn-00b6e544) · [`00b6e4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e4ac.md#insn-00b6e4bc)
- 新版 [`00b6f504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f4a0.md#insn-00b6f504) · [`00b6f538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f4a0.md#insn-00b6f538) · [`00b6f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f4a0.md#insn-00b6f4b0)

~~~diff
- 00b6e510 ["INT_ADD", "register:40f0:8", ["const:b6e510:8", "const:4:8"]]
- 00b6e510 ["CALL", null, ["callee:00c5bc40:8"]]
+ 00b6f504 ["INT_ADD", "register:40f0:8", ["const:b6f504:8", "const:4:8"]]
+ 00b6f504 ["CALL", null, ["callee:00c5bc40:8"]]
- 00b6e510 bytes d8b10394
+ 00b6f504 bytes cfb10394
- 00b6e544 ["INT_ADD", "register:40f0:8", ["const:b6e544:8", "const:4:8"]]
- 00b6e544 ["CALL", null, ["callee:00576618:8"]]
+ 00b6f538 ["INT_ADD", "register:40f0:8", ["const:b6f538:8", "const:4:8"]]
+ 00b6f538 ["CALL", null, ["callee:00576618:8"]]
- 00b6e544 bytes 6d1fe897
+ 00b6f538 bytes 381ce897
- 00b6e4bc ["COPY", "register:40b0:8", ["const:1126000:8"]]
+ 00b6f4b0 ["COPY", "register:40b0:8", ["const:1127000:8"]]
- 00b6e4bc bytes d62d0090
+ 00b6f4b0 bytes d62d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c023cdc344aca66a09aa2fefb515ece"></a>

### [`00b6e5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md) → [`00b6f5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f5ec.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b6e76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 1件 [`00b6f760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f760.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "00b6f624",
      "incomplete_value": true,
      "site": "00b6f634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
      "definition_site": "00b6e630",
      "incomplete_value": true,
      "site": "00b6e640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b8:8"
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
      "definition_site": "00b6f628",
      "incomplete_value": true,
      "site": "00b6f634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
      "definition_site": "00b6e634",
      "incomplete_value": true,
      "site": "00b6e640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c8:8"
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
      "definition_site": "00b6f668",
      "incomplete_value": true,
      "site": "00b6f66c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e674",
      "incomplete_value": true,
      "site": "00b6e678",
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
            "const:130:8"
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
      "00b6f624",
      "READ",
      [
        "storage",
        "011262b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f628",
      "READ",
      [
        "storage",
        "011262c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f660",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6f624",
      "READ",
      [
        "storage",
        "01127278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f628",
      "READ",
      [
        "storage",
        "01127288",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f660",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md#insn-00b6e640) · [`00b6e678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md#insn-00b6e678) · [`00b6e694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md#insn-00b6e694)
- 新版 [`00b6f634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f5ec.md#insn-00b6f634) · [`00b6f66c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f5ec.md#insn-00b6f66c) · [`00b6f688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f5ec.md#insn-00b6f688)

~~~diff
- 00b6e640 ["INT_ADD", "register:40f0:8", ["const:b6e640:8", "const:4:8"]]
- 00b6e640 ["CALL", null, ["callee:00c5cfe0:8"]]
+ 00b6f634 ["INT_ADD", "register:40f0:8", ["const:b6f634:8", "const:4:8"]]
+ 00b6f634 ["CALL", null, ["callee:00c5cfe0:8"]]
- 00b6e640 bytes 74b60394
+ 00b6f634 bytes 6bb60394
- 00b6e678 ["INT_ADD", "register:40f0:8", ["const:b6e678:8", "const:4:8"]]
- 00b6e678 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00b6f66c ["INT_ADD", "register:40f0:8", ["const:b6f66c:8", "const:4:8"]]
+ 00b6f66c ["CALL", null, ["callee:00c5bea0:8"]]
- 00b6e678 bytes 16b20394
+ 00b6f66c bytes 0db20394
- 00b6e694 ["INT_ADD", "register:40f0:8", ["const:b6e694:8", "const:4:8"]]
- 00b6e694 ["CALL", null, ["callee:00c5be40:8"]]
+ 00b6f688 ["INT_ADD", "register:40f0:8", ["const:b6f688:8", "const:4:8"]]
+ 00b6f688 ["CALL", null, ["callee:00c5be40:8"]]
- 00b6e694 bytes f7b10394
+ 00b6f688 bytes eeb10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22a46f84f86bf526a2ce630b895bddf1"></a>

### [`00b6e76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md) → [`00b6f760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f760.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bde0.md) · 呼出先 14件 [`00b6e5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md)
- 新版 呼出元 1件 [`00c5cdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cdb0.md) · 呼出先 14件 [`00b6f5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f5ec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6f79c",
      "incomplete_value": true,
      "site": "00b6f79c",
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
      "definition_site": "00b6e7a8",
      "incomplete_value": true,
      "site": "00b6e7a8",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6f7b8",
      "incomplete_value": true,
      "site": "00b6f7b8",
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
      "definition_site": "00b6e7c4",
      "incomplete_value": true,
      "site": "00b6e7c4",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6f84c",
      "incomplete_value": true,
      "site": "00b6f84c",
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
      "definition_site": "00b6e858",
      "incomplete_value": true,
      "site": "00b6e858",
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
      "00b6f794",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f7b4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f7e8",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6f794",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f7b4",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6f7e8",
      "READ",
      [
        "storage",
        "01127258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md#insn-00b6e808) · [`00b6e82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md#insn-00b6e82c) · [`00b6e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md#insn-00b6e868)
- 新版 [`00b6f7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f760.md#insn-00b6f7fc) · [`00b6f820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f760.md#insn-00b6f820) · [`00b6f85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6f760.md#insn-00b6f85c)

~~~diff
- 00b6e808 ["INT_ADD", "register:40f0:8", ["const:b6e808:8", "const:4:8"]]
- 00b6e808 ["CALL", null, ["callee:00c5bee0:8"]]
+ 00b6f7fc ["INT_ADD", "register:40f0:8", ["const:b6f7fc:8", "const:4:8"]]
+ 00b6f7fc ["CALL", null, ["callee:00c5bee0:8"]]
- 00b6e808 bytes c2b10394
+ 00b6f7fc bytes b9b10394
- 00b6e82c ["INT_ADD", "register:40f0:8", ["const:b6e82c:8", "const:4:8"]]
- 00b6e82c ["CALL", null, ["callee:00c5cd10:8"]]
+ 00b6f820 ["INT_ADD", "register:40f0:8", ["const:b6f820:8", "const:4:8"]]
+ 00b6f820 ["CALL", null, ["callee:00c5cd10:8"]]
- 00b6e82c bytes 45b50394
+ 00b6f820 bytes 3cb50394
- 00b6e868 ["INT_ADD", "register:40f0:8", ["const:b6e868:8", "const:4:8"]]
- 00b6e868 ["CALL", null, ["callee:00c5bc40:8"]]
+ 00b6f85c ["INT_ADD", "register:40f0:8", ["const:b6f85c:8", "const:4:8"]]
+ 00b6f85c ["CALL", null, ["callee:00c5bc40:8"]]
- 00b6e868 bytes 02b10394
+ 00b6f85c bytes f9b00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-749ed4ffe6dd503710f0926a950eba7a"></a>

### [`00b6eafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eafc.md) → [`00b6faf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6faf0.md) _ZN11flatbuffers19FLATBUFFERS_VERSIONEv

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
      "definition_site": "00b6faf4",
      "incomplete_value": false,
      "site": "00b6faf8",
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
            "const:efe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eb00",
      "incomplete_value": false,
      "site": "00b6eb04",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6faf4",
      "DATA",
      [
        "storage",
        "002bbe20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6faf4",
      "DATA",
      [
        "storage",
        "002bbefe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eafc.md#insn-00b6eb00)
- 新版 [`00b6faf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6faf0.md#insn-00b6faf4)

~~~diff
- 00b6eb00 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00b6eb00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6eb00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6eb00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6faf4 ["COPY", "tmp:0:8", ["const:efe:8"]]
+ 00b6faf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6faf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6faf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6eb00 bytes 00803891
+ 00b6faf4 bytes 00f83b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f72a945342ff3e7c6eb80cf52df220e"></a>

### [`00b6eb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md) → [`00b6fafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fafc.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md)
- 新版 呼出元 1件 [`00c5d810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d810.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6fb4c",
      "incomplete_value": false,
      "site": "00b6fb58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:cef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eb58",
      "incomplete_value": false,
      "site": "00b6eb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:c11:8"
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
      "definition_site": "00b6fbf4",
      "incomplete_value": false,
      "site": "00b6fc00",
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
            "const:a42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ec00",
      "incomplete_value": false,
      "site": "00b6ec0c",
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
            "const:96b:8"
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
      "definition_site": "00b6fc14",
      "incomplete_value": false,
      "site": "00b6fc20",
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
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ec20",
      "incomplete_value": false,
      "site": "00b6ec2c",
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
            "const:71a:8"
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
      "00b6fb4c",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ],
    [
      "00b6fbf4",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ],
    [
      "00b6fc14",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6fb4c",
      "PARAM",
      [
        "storage",
        "002b4cef",
        null,
        null
      ]
    ],
    [
      "00b6fbf4",
      "PARAM",
      [
        "storage",
        "002b0a42",
        null,
        null
      ]
    ],
    [
      "00b6fc14",
      "PARAM",
      [
        "storage",
        "002bd7f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md#insn-00b6eb64) · [`00b6ec0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md#insn-00b6ec0c) · [`00b6ec2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md#insn-00b6ec2c)
- 新版 [`00b6fb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fafc.md#insn-00b6fb58) · [`00b6fc00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fafc.md#insn-00b6fc00) · [`00b6fc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fafc.md#insn-00b6fc20)

~~~diff
- 00b6eb64 ["INT_ADD", "register:40f0:8", ["const:b6eb64:8", "const:4:8"]]
- 00b6eb64 ["CALL", null, ["callee:00c59020:8"]]
+ 00b6fb58 ["INT_ADD", "register:40f0:8", ["const:b6fb58:8", "const:4:8"]]
+ 00b6fb58 ["CALL", null, ["callee:00c59020:8"]]
- 00b6eb64 bytes 3ba50394
+ 00b6fb58 bytes 32a50394
- 00b6ec0c ["INT_ADD", "register:40f0:8", ["const:b6ec0c:8", "const:4:8"]]
- 00b6ec0c ["CALL", null, ["callee:00c59020:8"]]
+ 00b6fc00 ["INT_ADD", "register:40f0:8", ["const:b6fc00:8", "const:4:8"]]
+ 00b6fc00 ["CALL", null, ["callee:00c59020:8"]]
- 00b6ec0c bytes 11a50394
+ 00b6fc00 bytes 08a50394
- 00b6ec2c ["INT_ADD", "register:40f0:8", ["const:b6ec2c:8", "const:4:8"]]
- 00b6ec2c ["CALL", null, ["callee:00c59020:8"]]
+ 00b6fc20 ["INT_ADD", "register:40f0:8", ["const:b6fc20:8", "const:4:8"]]
+ 00b6fc20 ["CALL", null, ["callee:00c59020:8"]]
- 00b6ec2c bytes 09a50394
+ 00b6fc20 bytes 00a50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d2dc6fac557f77dcbf6e7343e6bd5d1"></a>

### [`00b6ed94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ed94.md) → [`00b6fd88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fd88.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6fde4",
      "incomplete_value": true,
      "site": "00b6fdf8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6edf0",
      "incomplete_value": true,
      "site": "00b6ee04",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6fddc",
      "incomplete_value": true,
      "site": "00b6fdfc",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ede8",
      "incomplete_value": true,
      "site": "00b6ee08",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6fe6c",
      "incomplete_value": true,
      "site": "00b6fe78",
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
      "definition_site": "00b6ee78",
      "incomplete_value": true,
      "site": "00b6ee84",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6fdbc",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fdc0",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fdf8",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6fdbc",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fdc0",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fdf8",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6edb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ed94.md#insn-00b6edb8) · [`00b6edbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ed94.md#insn-00b6edbc) · [`00b6edc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ed94.md#insn-00b6edc8)
- 新版 [`00b6fdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fd88.md#insn-00b6fdac) · [`00b6fdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fd88.md#insn-00b6fdb0) · [`00b6fdbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fd88.md#insn-00b6fdbc)

~~~diff
- 00b6edb8 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b6fdac ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b6edb8 bytes 7a090090
+ 00b6fdac bytes 7a090090
- 00b6edbc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b6fdb0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b6edbc bytes 680900b0
+ 00b6fdb0 bytes 680900b0
- 00b6edc8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b6edc8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6fdbc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b6fdbc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6edc8 bytes 5a7746f9
+ 00b6fdbc bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e287fa4f42161e13b788b57adf4afb0"></a>

### [`00b6ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ef00.md) → [`00b6fef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fef4.md) _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0d0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`00c5d0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0a0.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c592c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ff4c",
      "incomplete_value": true,
      "site": "00b6ff60",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ef58",
      "incomplete_value": true,
      "site": "00b6ef6c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ff44",
      "incomplete_value": true,
      "site": "00b6ff64",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ef50",
      "incomplete_value": true,
      "site": "00b6ef70",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ffd4",
      "incomplete_value": true,
      "site": "00b6ffe0",
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
      "definition_site": "00b6efe0",
      "incomplete_value": true,
      "site": "00b6efec",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6ff24",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ff28",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ff60",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6ff24",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ff28",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ff60",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ef00.md#insn-00b6ef24) · [`00b6ef28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ef00.md#insn-00b6ef28) · [`00b6ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ef00.md#insn-00b6ef30)
- 新版 [`00b6ff18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fef4.md#insn-00b6ff18) · [`00b6ff1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fef4.md#insn-00b6ff1c) · [`00b6ff24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6f/00b6fef4.md#insn-00b6ff24)

~~~diff
- 00b6ef24 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b6ff18 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b6ef24 bytes 7a090090
+ 00b6ff18 bytes 7a090090
- 00b6ef28 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b6ff1c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b6ef28 bytes 680900b0
+ 00b6ff1c bytes 680900b0
- 00b6ef30 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b6ef30 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ff24 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b6ff24 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ef30 bytes 5a7746f9
+ 00b6ff24 bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9b4b6e22785dfacf2a057956608d74"></a>

### [`00b6f148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f148.md) → [`00b7013c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7013c.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d810.md)

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
      "definition_site": "00b70168",
      "incomplete_value": false,
      "site": "00b70170",
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
            "const:b9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f174",
      "incomplete_value": false,
      "site": "00b6f17c",
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
            "const:b5f:8"
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
      "00b70168",
      "PARAM",
      [
        "storage",
        "002a0b5f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b70168",
      "PARAM",
      [
        "storage",
        "002a0b9f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f148.md#insn-00b6f17c) · [`00b6f174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f148.md#insn-00b6f174) · [`00b6f188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f148.md#insn-00b6f188)
- 新版 [`00b70170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7013c.md#insn-00b70170) · [`00b70168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7013c.md#insn-00b70168) · [`00b7017c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7013c.md#insn-00b7017c)

~~~diff
- 00b6f17c ["INT_ADD", "register:40f0:8", ["const:b6f17c:8", "const:4:8"]]
- 00b6f17c ["CALL", null, ["callee:00c59150:8"]]
+ 00b70170 ["INT_ADD", "register:40f0:8", ["const:b70170:8", "const:4:8"]]
+ 00b70170 ["CALL", null, ["callee:00c59150:8"]]
- 00b6f17c bytes 01a40394
+ 00b70170 bytes f8a30394
- 00b6f174 ["COPY", "tmp:0:8", ["const:b5f:8"]]
- 00b6f174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b70168 ["COPY", "tmp:0:8", ["const:b9f:8"]]
+ 00b70168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b70168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b70168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6f174 bytes 007c2d91
+ 00b70168 bytes 007c2e91
- 00b6f188 ["INT_ADD", "register:40f0:8", ["const:b6f188:8", "const:4:8"]]
- 00b6f188 ["CALL", null, ["callee:00c5d810:8"]]
+ 00b7017c ["INT_ADD", "register:40f0:8", ["const:b7017c:8", "const:4:8"]]
+ 00b7017c ["CALL", null, ["callee:00c5d810:8"]]
- 00b6f188 bytes aeb50394
+ 00b7017c bytes a5b50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ea68054e1d6d11a04d6e03003406034"></a>

### [`00b6f1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f1c8.md) → [`00b701bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b701bc.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b701e4",
      "incomplete_value": false,
      "site": "00b701f0",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f1f0",
      "incomplete_value": false,
      "site": "00b6f1fc",
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
            "const:b69:8"
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
      "00b701e4",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b701e4",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f1c8.md#insn-00b6f1fc) · [`00b6f1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f1c8.md#insn-00b6f1f0) · [`00b6f208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f1c8.md#insn-00b6f208)
- 新版 [`00b701f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b701bc.md#insn-00b701f0) · [`00b701e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b701bc.md#insn-00b701e4) · [`00b701fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b701bc.md#insn-00b701fc)

~~~diff
- 00b6f1fc ["INT_ADD", "register:40f0:8", ["const:b6f1fc:8", "const:4:8"]]
- 00b6f1fc ["CALL", null, ["callee:00c59150:8"]]
+ 00b701f0 ["INT_ADD", "register:40f0:8", ["const:b701f0:8", "const:4:8"]]
+ 00b701f0 ["CALL", null, ["callee:00c59150:8"]]
- 00b6f1fc bytes e1a30394
+ 00b701f0 bytes d8a30394
- 00b6f1f0 ["COPY", "tmp:0:8", ["const:b69:8"]]
- 00b6f1f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f1f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f1f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b701e4 ["COPY", "tmp:0:8", ["const:ba9:8"]]
+ 00b701e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b701e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b701e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6f1f0 bytes 00a42d91
+ 00b701e4 bytes 00a42e91
- 00b6f208 ["INT_ADD", "register:40f0:8", ["const:b6f208:8", "const:4:8"]]
- 00b6f208 ["CALL", null, ["callee:00c5d810:8"]]
+ 00b701fc ["INT_ADD", "register:40f0:8", ["const:b701fc:8", "const:4:8"]]
+ 00b701fc ["CALL", null, ["callee:00c5d810:8"]]
- 00b6f208 bytes 8eb50394
+ 00b701fc bytes 85b50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620167f233b782bf9f4ae3bfc1bd3559"></a>

### [`00b6f24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f24c.md) → [`00b70240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70240.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5f0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)
- 新版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5c0.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b70278",
      "incomplete_value": false,
      "site": "00b70288",
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
            "const:c82:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f284",
      "incomplete_value": false,
      "site": "00b6f294",
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
            "const:c38:8"
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
      "definition_site": "00b70298",
      "incomplete_value": false,
      "site": "00b702b4",
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
            "const:666:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f2a4",
      "incomplete_value": false,
      "site": "00b6f2c0",
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
            "const:50e:8"
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
      "definition_site": "00b702d8",
      "incomplete_value": false,
      "site": "00b702e0",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f2e4",
      "incomplete_value": false,
      "site": "00b6f2ec",
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
            "const:b69:8"
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
      "00b70278",
      "PARAM",
      [
        "storage",
        "002c1c38",
        null,
        "string"
      ]
    ],
    [
      "00b70298",
      "PARAM",
      [
        "storage",
        "002a850e",
        null,
        "string"
      ]
    ],
    [
      "00b702d8",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b70278",
      "PARAM",
      [
        "storage",
        "002c1c82",
        null,
        "string"
      ]
    ],
    [
      "00b70298",
      "PARAM",
      [
        "storage",
        "002a8666",
        null,
        "string"
      ]
    ],
    [
      "00b702d8",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f24c.md#insn-00b6f294) · [`00b6f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f24c.md#insn-00b6f2c0) · [`00b6f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f24c.md#insn-00b6f2ec)
- 新版 [`00b70288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70240.md#insn-00b70288) · [`00b702b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70240.md#insn-00b702b4) · [`00b702e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70240.md#insn-00b702e0)

~~~diff
- 00b6f294 ["INT_ADD", "register:40f0:8", ["const:b6f294:8", "const:4:8"]]
- 00b6f294 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b70288 ["INT_ADD", "register:40f0:8", ["const:b70288:8", "const:4:8"]]
+ 00b70288 ["CALL", null, ["callee:00c5a070:8"]]
- 00b6f294 bytes 83a70394
+ 00b70288 bytes 7aa70394
- 00b6f2c0 ["INT_ADD", "register:40f0:8", ["const:b6f2c0:8", "const:4:8"]]
- 00b6f2c0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b702b4 ["INT_ADD", "register:40f0:8", ["const:b702b4:8", "const:4:8"]]
+ 00b702b4 ["CALL", null, ["callee:00c59020:8"]]
- 00b6f2c0 bytes 64a30394
+ 00b702b4 bytes 5ba30394
- 00b6f2ec ["INT_ADD", "register:40f0:8", ["const:b6f2ec:8", "const:4:8"]]
- 00b6f2ec ["CALL", null, ["callee:00c59150:8"]]
+ 00b702e0 ["INT_ADD", "register:40f0:8", ["const:b702e0:8", "const:4:8"]]
+ 00b702e0 ["CALL", null, ["callee:00c59150:8"]]
- 00b6f2ec bytes a5a30394
+ 00b702e0 bytes 9ca30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e504d3ac05575b7bff2389c3fd55eb01"></a>

### [`00b6f758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f758.md) → [`00b7074c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7074c.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c590.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d560.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

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
      "definition_site": "00b707f8",
      "incomplete_value": false,
      "site": "00b70814",
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
            "const:b7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f804",
      "incomplete_value": false,
      "site": "00b6f820",
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
            "const:ab3:8"
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
      "definition_site": "00b70838",
      "incomplete_value": false,
      "site": "00b70840",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f844",
      "incomplete_value": false,
      "site": "00b6f84c",
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
            "const:b69:8"
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
      "definition_site": "00b70944",
      "incomplete_value": true,
      "site": "00b70950",
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
      "definition_site": "00b6f950",
      "incomplete_value": true,
      "site": "00b6f95c",
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
      "00b707d8",
      "PARAM",
      [
        "storage",
        "002be638",
        null,
        "string"
      ]
    ],
    [
      "00b707f8",
      "PARAM",
      [
        "storage",
        "002a2ab3",
        null,
        "string"
      ]
    ],
    [
      "00b70838",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b707d8",
      "PARAM",
      [
        "storage",
        "002be716",
        null,
        "string"
      ]
    ],
    [
      "00b707f8",
      "PARAM",
      [
        "storage",
        "002a2b7e",
        null,
        "string"
      ]
    ],
    [
      "00b70838",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f758.md#insn-00b6f820) · [`00b6f84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f758.md#insn-00b6f84c) · [`00b6f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f758.md#insn-00b6f95c)
- 新版 [`00b70814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7074c.md#insn-00b70814) · [`00b70840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7074c.md#insn-00b70840) · [`00b70950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b7074c.md#insn-00b70950)

~~~diff
- 00b6f820 ["INT_ADD", "register:40f0:8", ["const:b6f820:8", "const:4:8"]]
- 00b6f820 ["CALL", null, ["callee:00c59020:8"]]
+ 00b70814 ["INT_ADD", "register:40f0:8", ["const:b70814:8", "const:4:8"]]
+ 00b70814 ["CALL", null, ["callee:00c59020:8"]]
- 00b6f820 bytes 0ca20394
+ 00b70814 bytes 03a20394
- 00b6f84c ["INT_ADD", "register:40f0:8", ["const:b6f84c:8", "const:4:8"]]
- 00b6f84c ["CALL", null, ["callee:00c59150:8"]]
+ 00b70840 ["INT_ADD", "register:40f0:8", ["const:b70840:8", "const:4:8"]]
+ 00b70840 ["CALL", null, ["callee:00c59150:8"]]
- 00b6f84c bytes 4da20394
+ 00b70840 bytes 44a20394
- 00b6f95c ["INT_ADD", "register:40f0:8", ["const:b6f95c:8", "const:4:8"]]
- 00b6f95c ["CALL", null, ["callee:00c5e200:8"]]
+ 00b70950 ["INT_ADD", "register:40f0:8", ["const:b70950:8", "const:4:8"]]
+ 00b70950 ["CALL", null, ["callee:00c5e200:8"]]
- 00b6f95c bytes 35b60394
+ 00b70950 bytes 2cb60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e32dd1bdc99eeee96c635b1b6c0a8d"></a>

### [`00b6fa40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fa40.md) → [`00b70a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70a34.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c720.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)
- 新版 呼出元 1件 [`00c5d6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d6f0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b70ab4",
      "incomplete_value": true,
      "site": "00b70ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fac0",
      "incomplete_value": true,
      "site": "00b6fad4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b70ab8",
      "incomplete_value": true,
      "site": "00b70acc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:6c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fac4",
      "incomplete_value": true,
      "site": "00b6fad8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:67e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b70ac0",
      "incomplete_value": true,
      "site": "00b70ae4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6facc",
      "incomplete_value": true,
      "site": "00b6faf0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b70ab4",
      "READ",
      [
        "storage",
        "002b268b",
        null,
        "string"
      ]
    ],
    [
      "00b70ab8",
      "READ",
      [
        "storage",
        "002b267e",
        null,
        "string"
      ]
    ],
    [
      "00b70ac0",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b70ab4",
      "READ",
      [
        "storage",
        "002b26d5",
        null,
        "string"
      ]
    ],
    [
      "00b70ab8",
      "READ",
      [
        "storage",
        "002b26c8",
        null,
        "string"
      ]
    ],
    [
      "00b70ac0",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6faf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fa40.md#insn-00b6faf4) · [`00b6fab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fa40.md#insn-00b6fab4) · [`00b6fabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fa40.md#insn-00b6fabc)
- 新版 [`00b70ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70a34.md#insn-00b70ae8) · [`00b70aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70a34.md#insn-00b70aa8) · [`00b70ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70a34.md#insn-00b70ab0)

~~~diff
- 00b6faf4 ["INT_ADD", "register:40f0:8", ["const:b6faf4:8", "const:4:8"]]
- 00b6faf4 ["CALL", null, ["callee:00c59150:8"]]
+ 00b70ae8 ["INT_ADD", "register:40f0:8", ["const:b70ae8:8", "const:4:8"]]
+ 00b70ae8 ["CALL", null, ["callee:00c59150:8"]]
- 00b6faf4 bytes a3a10394
+ 00b70ae8 bytes 9aa10394
- 00b6fab4 ["INT_ADD", "register:40f0:8", ["const:b6fab4:8", "const:4:8"]]
- 00b6fab4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b70aa8 ["INT_ADD", "register:40f0:8", ["const:b70aa8:8", "const:4:8"]]
+ 00b70aa8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b6fab4 bytes 2ba10394
+ 00b70aa8 bytes 22a10394
- 00b6fabc ["COPY", "tmp:0:8", ["const:67e:8"]]
- 00b6fabc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b6fabc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b6fabc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b70ab0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00b70ab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b70ab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b70ab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b6fabc bytes 29f91991
+ 00b70ab0 bytes 29211b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ad8b3809bd633e526e340d577f5898"></a>

### [`00b6fb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fb54.md) → [`00b70b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70b48.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) · 呼出先 14件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)
- 新版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d790.md) · 呼出先 14件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 20件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b71bb4",
      "incomplete_value": true,
      "site": "00b71bcc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "old": {
      "definition_site": "00b70bc0",
      "incomplete_value": true,
      "site": "00b70bd8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 132,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b71bb8",
      "incomplete_value": true,
      "site": "00b71bd0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:bb1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70bc4",
      "incomplete_value": true,
      "site": "00b70bdc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:b71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 133,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b71bb8",
      "incomplete_value": true,
      "site": "00b71bd0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70bc4",
      "incomplete_value": true,
      "site": "00b70bdc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 134,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b70c38",
      "DATA",
      [
        "storage",
        "0030deee",
        "switchD_00b6fc4c::switchdataD_0030deee",
        "ushort"
      ]
    ],
    [
      "00b70e5c",
      "READ",
      [
        "storage",
        "002a71c8",
        null,
        "string"
      ]
    ],
    [
      "00b70e5c",
      "READ",
      [
        "storage",
        "002b471e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b70c38",
      "DATA",
      [
        "storage",
        "0030df2e",
        "switchD_00b70c40::switchdataD_0030df2e",
        "ushort"
      ]
    ],
    [
      "00b70e5c",
      "READ",
      [
        "storage",
        "002a7320",
        null,
        "string"
      ]
    ],
    [
      "00b70e5c",
      "READ",
      [
        "storage",
        "002b47fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fb54.md#insn-00b6fe94) · [`00b6ff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fb54.md#insn-00b6ff44) · [`00b70160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fb54.md#insn-00b70160)
- 新版 [`00b70e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70b48.md#insn-00b70e88) · [`00b70f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70b48.md#insn-00b70f38) · [`00b71154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b70/00b70b48.md#insn-00b71154)

~~~diff
- 00b6fe94 ["INT_ADD", "register:40f0:8", ["const:b6fe94:8", "const:4:8"]]
- 00b6fe94 ["CALL", null, ["callee:00c59150:8"]]
+ 00b70e88 ["INT_ADD", "register:40f0:8", ["const:b70e88:8", "const:4:8"]]
+ 00b70e88 ["CALL", null, ["callee:00c59150:8"]]
- 00b6fe94 bytes bba00394
+ 00b70e88 bytes b2a00394
- 00b6ff44 ["INT_ADD", "register:40f0:8", ["const:b6ff44:8", "const:4:8"]]
- 00b6ff44 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00b70f38 ["INT_ADD", "register:40f0:8", ["const:b70f38:8", "const:4:8"]]
+ 00b70f38 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b6ff44 bytes afb40394
+ 00b70f38 bytes a6b40394
- 00b70160 ["INT_ADD", "register:40f0:8", ["const:b70160:8", "const:4:8"]]
- 00b70160 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b71154 ["INT_ADD", "register:40f0:8", ["const:b71154:8", "const:4:8"]]
+ 00b71154 ["CALL", null, ["callee:00c5a070:8"]]
- 00b70160 bytes d0a30394
+ 00b71154 bytes c7a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a1efba4b695fec3832438847172dbc"></a>

### [`00b71238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71238.md) → [`00b7222c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b7222c.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md) · 呼出先 12件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7f0.md) · 呼出先 12件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72338",
      "incomplete_value": false,
      "site": "00b72348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:a82:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71344",
      "incomplete_value": false,
      "site": "00b71354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "definition_site": "00b72358",
      "incomplete_value": false,
      "site": "00b72374",
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
            "const:965:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71364",
      "incomplete_value": false,
      "site": "00b71380",
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
            "const:887:8"
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
      "definition_site": "00b7250c",
      "incomplete_value": false,
      "site": "00b72514",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71518",
      "incomplete_value": false,
      "site": "00b71520",
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
            "const:b69:8"
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
      "00b722c0",
      "DATA",
      [
        "storage",
        "00c90228",
        null,
        null
      ]
    ],
    [
      "00b72338",
      "PARAM",
      [
        "storage",
        "002c0a38",
        null,
        "string"
      ]
    ],
    [
      "00b72358",
      "PARAM",
      [
        "storage",
        "002bf887",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b722c0",
      "DATA",
      [
        "storage",
        "00c911f8",
        null,
        null
      ]
    ],
    [
      "00b72338",
      "PARAM",
      [
        "storage",
        "002c0a82",
        null,
        "string"
      ]
    ],
    [
      "00b72358",
      "PARAM",
      [
        "storage",
        "002bf965",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71238.md#insn-00b71354) · [`00b71380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71238.md#insn-00b71380) · [`00b71520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71238.md#insn-00b71520)
- 新版 [`00b72348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b7222c.md#insn-00b72348) · [`00b72374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b7222c.md#insn-00b72374) · [`00b72514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b7222c.md#insn-00b72514)

~~~diff
- 00b71354 ["INT_ADD", "register:40f0:8", ["const:b71354:8", "const:4:8"]]
- 00b71354 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b72348 ["INT_ADD", "register:40f0:8", ["const:b72348:8", "const:4:8"]]
+ 00b72348 ["CALL", null, ["callee:00c5a070:8"]]
- 00b71354 bytes 539f0394
+ 00b72348 bytes 4a9f0394
- 00b71380 ["INT_ADD", "register:40f0:8", ["const:b71380:8", "const:4:8"]]
- 00b71380 ["CALL", null, ["callee:00c59020:8"]]
+ 00b72374 ["INT_ADD", "register:40f0:8", ["const:b72374:8", "const:4:8"]]
+ 00b72374 ["CALL", null, ["callee:00c59020:8"]]
- 00b71380 bytes 349b0394
+ 00b72374 bytes 2b9b0394
- 00b71520 ["INT_ADD", "register:40f0:8", ["const:b71520:8", "const:4:8"]]
- 00b71520 ["CALL", null, ["callee:00c59150:8"]]
+ 00b72514 ["INT_ADD", "register:40f0:8", ["const:b72514:8", "const:4:8"]]
+ 00b72514 ["CALL", null, ["callee:00c59150:8"]]
- 00b71520 bytes 189b0394
+ 00b72514 bytes 0f9b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06af5605e491e3f8f28106d622b2773d"></a>

### [`00b71e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md) → [`00b72e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72e44.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c730.md) · 呼出先 17件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5d700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d700.md) · 呼出先 17件 [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.66% / 新版 99.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b72f60",
      "incomplete_value": true,
      "site": "00b72f98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71f6c",
      "incomplete_value": true,
      "site": "00b71fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73084",
      "incomplete_value": false,
      "site": "00b7308c",
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
            "const:a42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b72090",
      "incomplete_value": false,
      "site": "00b72098",
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
            "const:96b:8"
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
      "00b72f60",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b73084",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b72f60",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b73084",
      "PARAM",
      [
        "storage",
        "002b0a42",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md#insn-00b72098) · [`00b71e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md#insn-00b71e98) · [`00b71ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md#insn-00b71ea8)
- 新版 [`00b7308c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72e44.md#insn-00b7308c) · [`00b72e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72e44.md#insn-00b72e8c) · [`00b72e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72e44.md#insn-00b72e9c)

~~~diff
- 00b72098 ["INT_ADD", "register:40f0:8", ["const:b72098:8", "const:4:8"]]
- 00b72098 ["CALL", null, ["callee:00b5bc44:8"]]
+ 00b7308c ["INT_ADD", "register:40f0:8", ["const:b7308c:8", "const:4:8"]]
+ 00b7308c ["CALL", null, ["callee:00b5bc44:8"]]
- 00b72098 bytes eea2ff97
+ 00b7308c bytes eea2ff97
- 00b71e98 ["INT_ADD", "register:40f0:8", ["const:b71e98:8", "const:4:8"]]
- 00b71e98 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00b72e8c ["INT_ADD", "register:40f0:8", ["const:b72e8c:8", "const:4:8"]]
+ 00b72e8c ["CALL", null, ["callee:00c5dae0:8"]]
- 00b71e98 bytes 1eab0394
+ 00b72e8c bytes 15ab0394
- 00b71ea8 ["INT_ADD", "register:40f0:8", ["const:b71ea8:8", "const:4:8"]]
- 00b71ea8 ["CALL", null, ["callee:00c5db50:8"]]
+ 00b72e9c ["INT_ADD", "register:40f0:8", ["const:b72e9c:8", "const:4:8"]]
+ 00b72e9c ["CALL", null, ["callee:00c5db50:8"]]
- 00b71ea8 bytes 36ab0394
+ 00b72e9c bytes 2dab0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-106c8ed7bfd594de748f71015e3dd25e"></a>

### [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) → [`00b732dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b732dc.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) [`00c5c8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8a0.md) · 呼出先 12件 [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00b732dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b732dc.md) [`00c5d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d870.md) · 呼出先 12件 [`00b732dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b732dc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.49% / 新版 89.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 16件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b737a4",
      "incomplete_value": true,
      "site": "00b737b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b727b0",
      "incomplete_value": true,
      "site": "00b727c4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b737c4",
      "incomplete_value": true,
      "site": "00b737c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b727d0",
      "incomplete_value": true,
      "site": "00b727d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b737b0",
      "incomplete_value": true,
      "site": "00b737c8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b727bc",
      "incomplete_value": true,
      "site": "00b727d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b73354",
      "DATA",
      [
        "storage",
        "0030e098",
        "switchD_00b72368::switchdataD_0030e098",
        "byte"
      ]
    ],
    [
      "00b7336c",
      "PARAM",
      [
        "storage",
        "002b15b7",
        null,
        null
      ]
    ],
    [
      "00b733c4",
      "READ",
      [
        "storage",
        "002b26b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b73354",
      "DATA",
      [
        "storage",
        "0030e0d8",
        "switchD_00b7335c::switchdataD_0030e0d8",
        "byte"
      ]
    ],
    [
      "00b7336c",
      "PARAM",
      [
        "storage",
        "002b168e",
        null,
        null
      ]
    ],
    [
      "00b733c4",
      "READ",
      [
        "storage",
        "002b26fa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md#insn-00b72358) · [`00b7235c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md#insn-00b7235c) · [`00b72378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md#insn-00b72378)
- 新版 [`00b7334c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b732dc.md#insn-00b7334c) · [`00b7336c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b732dc.md#insn-00b7336c)

~~~diff
- 00b72358 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00b72358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b72358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b72358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b7334c ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00b7334c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b7334c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b7334c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b72358 bytes 29610291
+ 00b7334c bytes 29610391
- 00b7235c ["COPY", "register:4050:8", ["const:b7236c:8"]]
- 00b7235c bytes 8a000010
- 00b72378 ["COPY", "tmp:0:8", ["const:5b7:8"]]
- 00b72378 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b72378 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b72378 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b7336c ["COPY", "tmp:0:8", ["const:68e:8"]]
+ 00b7336c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7336c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b7336c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b72378 bytes 21dc1691
+ 00b7336c bytes 21381a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de20bc1096dd2b14b330da2785f29558"></a>

### [`00b72aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72aa4.md) → [`00b73a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73a98.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c850.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d820.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.82% / 新版 93.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b73b0c",
      "incomplete_value": false,
      "site": "00b73b38",
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
            "const:18a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b72b18",
      "incomplete_value": false,
      "site": "00b72b44",
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
            "const:bb:8"
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
      "definition_site": "00b73cdc",
      "incomplete_value": false,
      "site": "00b73ce8",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b72ce8",
      "incomplete_value": false,
      "site": "00b72cf4",
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
            "const:b69:8"
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
      "00b73ae8",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b73b0c",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ],
    [
      "00b73c04",
      "DATA",
      [
        "storage",
        "0030e09d",
        "switchD_00b72c1c::switchdataD_0030e09d",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b73ae8",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b73b0c",
      "PARAM",
      [
        "storage",
        "002b818a",
        null,
        null
      ]
    ],
    [
      "00b73c04",
      "DATA",
      [
        "storage",
        "0030e0dd",
        "switchD_00b73c10::switchdataD_0030e0dd",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72aa4.md#insn-00b72b44) · [`00b72cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72aa4.md#insn-00b72cf4) · [`00b72aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72aa4.md#insn-00b72aec)
- 新版 [`00b73b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73a98.md#insn-00b73b38) · [`00b73ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73a98.md#insn-00b73ce8) · [`00b73ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73a98.md#insn-00b73ae0)

~~~diff
- 00b72b44 ["INT_ADD", "register:40f0:8", ["const:b72b44:8", "const:4:8"]]
- 00b72b44 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b73b38 ["INT_ADD", "register:40f0:8", ["const:b73b38:8", "const:4:8"]]
+ 00b73b38 ["CALL", null, ["callee:00c5c660:8"]]
- 00b72b44 bytes d3a20394
+ 00b73b38 bytes caa20394
- 00b72cf4 ["INT_ADD", "register:40f0:8", ["const:b72cf4:8", "const:4:8"]]
- 00b72cf4 ["CALL", null, ["callee:00c59150:8"]]
+ 00b73ce8 ["INT_ADD", "register:40f0:8", ["const:b73ce8:8", "const:4:8"]]
+ 00b73ce8 ["CALL", null, ["callee:00c59150:8"]]
- 00b72cf4 bytes 23950394
+ 00b73ce8 bytes 1a950394
- 00b72aec ["INT_ADD", "register:40f0:8", ["const:b72aec:8", "const:4:8"]]
- 00b72aec ["CALL", null, ["callee:00c58f30:8"]]
+ 00b73ae0 ["INT_ADD", "register:40f0:8", ["const:b73ae0:8", "const:4:8"]]
+ 00b73ae0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b72aec bytes 1d950394
+ 00b73ae0 bytes 14950394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f563c03906610452a27bc0d7b2e3f4"></a>

### [`00b72ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md) → [`00b73fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md) _ZN11flatbuffers6Parser10ParseFieldERNS_9StructDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c540.md) · 呼出先 27件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5d510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d510.md) · 呼出先 27件 [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.26% / 新版 90.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `store_value` 88件

アドレスに依存する影響 `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b740d4",
      "incomplete_value": true,
      "site": "00b740e4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
      "definition_site": "00b730e0",
      "incomplete_value": true,
      "site": "00b730f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b740e0",
      "incomplete_value": true,
      "site": "00b740f8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b730ec",
      "incomplete_value": true,
      "site": "00b73104",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b740e8",
      "incomplete_value": true,
      "site": "00b740f8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b730f4",
      "incomplete_value": true,
      "site": "00b73104",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b740d4",
      "READ",
      [
        "storage",
        "002c2ab0",
        null,
        null
      ]
    ],
    [
      "00b740e0",
      "READ",
      [
        "storage",
        "002a71e4",
        null,
        "string"
      ]
    ],
    [
      "00b740e0",
      "READ",
      [
        "storage",
        "002a71f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b740d4",
      "READ",
      [
        "storage",
        "002c2b00",
        null,
        null
      ]
    ],
    [
      "00b740e0",
      "READ",
      [
        "storage",
        "002a733c",
        null,
        "string"
      ]
    ],
    [
      "00b740e0",
      "READ",
      [
        "storage",
        "002a734c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b74570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md#insn-00b74570) · [`00b746f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md#insn-00b746f8) · [`00b74aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md#insn-00b74aa0)
- 新版 [`00b75564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md#insn-00b75564) · [`00b756ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md#insn-00b756ec) · [`00b75a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md#insn-00b75a94)

~~~diff
- 00b74570 ["INT_ADD", "register:40f0:8", ["const:b74570:8", "const:4:8"]]
- 00b74570 ["CALL", null, ["callee:00c59150:8"]]
+ 00b75564 ["INT_ADD", "register:40f0:8", ["const:b75564:8", "const:4:8"]]
+ 00b75564 ["CALL", null, ["callee:00c59150:8"]]
- 00b74570 bytes 048f0394
+ 00b75564 bytes fb8e0394
- 00b746f8 ["COPY", "tmp:0:8", ["const:4f9:8"]]
- 00b746f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b746f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b746f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b756ec ["COPY", "tmp:0:8", ["const:651:8"]]
+ 00b756ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b756ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b756ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b746f8 bytes 29e51391
+ 00b756ec bytes 29451991
- 00b74aa0 ["INT_ADD", "register:40f0:8", ["const:b74aa0:8", "const:4:8"]]
- 00b74aa0 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b75a94 ["INT_ADD", "register:40f0:8", ["const:b75a94:8", "const:4:8"]]
+ 00b75a94 ["CALL", null, ["callee:00c5c150:8"]]
- 00b74aa0 bytes b8990394
+ 00b75a94 bytes af990394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89aa8ac66f6a9efc2b5deddfa2beff1"></a>

### [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) → [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) _ZN11flatbuffers6Parser16ParseSingleValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c700.md) · 呼出先 35件 [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00b7d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md) [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md)
- 新版 呼出元 1件 [`00c5d6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d6d0.md) · 呼出先 35件 [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00b7e1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md) [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.81% / 新版 95.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b76648",
      "incomplete_value": true,
      "site": "00b7665c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:3a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b75654",
      "incomplete_value": true,
      "site": "00b75668",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:2ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b76660",
      "incomplete_value": true,
      "site": "00b76660",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7566c",
      "incomplete_value": true,
      "site": "00b7566c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b76820",
      "incomplete_value": true,
      "site": "00b76830",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:c60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7582c",
      "incomplete_value": true,
      "site": "00b7583c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b76648",
      "READ",
      [
        "storage",
        "002bd2ca",
        null,
        "string"
      ]
    ],
    [
      "00b7664c",
      "READ",
      [
        "storage",
        "002bd2d8",
        null,
        "string"
      ]
    ],
    [
      "00b7666c",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b76648",
      "READ",
      [
        "storage",
        "002bd3a8",
        null,
        "string"
      ]
    ],
    [
      "00b7664c",
      "READ",
      [
        "storage",
        "002bd3b6",
        null,
        "string"
      ]
    ],
    [
      "00b7666c",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md#insn-00b75684) · [`00b75984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md#insn-00b75984) · [`00b759f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md#insn-00b759f0)
- 新版 [`00b76678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md#insn-00b76678) · [`00b76978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md#insn-00b76978) · [`00b769e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md#insn-00b769e4)

~~~diff
- 00b75684 ["INT_ADD", "register:40f0:8", ["const:b75684:8", "const:4:8"]]
- 00b75684 ["CALL", null, ["callee:00c59150:8"]]
+ 00b76678 ["INT_ADD", "register:40f0:8", ["const:b76678:8", "const:4:8"]]
+ 00b76678 ["CALL", null, ["callee:00c59150:8"]]
- 00b75684 bytes bf8a0394
+ 00b76678 bytes b68a0394
- 00b75984 ["INT_ADD", "register:40f0:8", ["const:b75984:8", "const:4:8"]]
- 00b75984 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b76978 ["INT_ADD", "register:40f0:8", ["const:b76978:8", "const:4:8"]]
+ 00b76978 ["CALL", null, ["callee:00c5c150:8"]]
- 00b75984 bytes ff950394
+ 00b76978 bytes f6950394
- 00b759f0 ["INT_ADD", "register:40f0:8", ["const:b759f0:8", "const:4:8"]]
- 00b759f0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b769e4 ["INT_ADD", "register:40f0:8", ["const:b769e4:8", "const:4:8"]]
+ 00b769e4 ["CALL", null, ["callee:00c59020:8"]]
- 00b759f0 bytes 98890394
+ 00b769e4 bytes 8f890394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9505df1ba5f8e8b92c7cb1333fc3df15"></a>

### [`00b766d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b766d8.md) → [`00b776cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b776cc.md) _ZN11flatbuffers6Parser13ParseMetaDataEPNS_11SymbolTableINS_5ValueEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c620.md) · 呼出先 13件 [`00639b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5f0.md) · 呼出先 13件 [`00639ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639ee4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b77870",
      "incomplete_value": false,
      "site": "00b77874",
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
            "const:89d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7687c",
      "incomplete_value": false,
      "site": "00b76880",
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
            "const:7bf:8"
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
      "definition_site": "00b7788c",
      "incomplete_value": false,
      "site": "00b77890",
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
            "const:b9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76898",
      "incomplete_value": false,
      "site": "00b7689c",
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
            "const:b5f:8"
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
      "definition_site": "00b77954",
      "incomplete_value": false,
      "site": "00b77958",
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
            "const:9a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76960",
      "incomplete_value": false,
      "site": "00b76964",
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
            "const:8cb:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b77834",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ],
    [
      "00b77870",
      "PARAM",
      [
        "storage",
        "002be7bf",
        null,
        "string"
      ]
    ],
    [
      "00b7788c",
      "PARAM",
      [
        "storage",
        "002a0b5f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b77834",
      "PARAM",
      [
        "storage",
        "002b818a",
        null,
        null
      ]
    ],
    [
      "00b77870",
      "PARAM",
      [
        "storage",
        "002be89d",
        null,
        "string"
      ]
    ],
    [
      "00b7788c",
      "PARAM",
      [
        "storage",
        "002a0b9f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b766d8.md#insn-00b76880) · [`00b7689c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b766d8.md#insn-00b7689c) · [`00b76964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b766d8.md#insn-00b76964)
- 新版 [`00b77874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b776cc.md#insn-00b77874) · [`00b77890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b776cc.md#insn-00b77890) · [`00b77958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b776cc.md#insn-00b77958)

~~~diff
- 00b76880 ["INT_ADD", "register:40f0:8", ["const:b76880:8", "const:4:8"]]
- 00b76880 ["CALL", null, ["callee:00c59150:8"]]
+ 00b77874 ["INT_ADD", "register:40f0:8", ["const:b77874:8", "const:4:8"]]
+ 00b77874 ["CALL", null, ["callee:00c59150:8"]]
- 00b76880 bytes 40860394
+ 00b77874 bytes 37860394
- 00b7689c ["INT_ADD", "register:40f0:8", ["const:b7689c:8", "const:4:8"]]
- 00b7689c ["CALL", null, ["callee:00c59150:8"]]
+ 00b77890 ["INT_ADD", "register:40f0:8", ["const:b77890:8", "const:4:8"]]
+ 00b77890 ["CALL", null, ["callee:00c59150:8"]]
- 00b7689c bytes 39860394
+ 00b77890 bytes 30860394
- 00b76964 ["INT_ADD", "register:40f0:8", ["const:b76964:8", "const:4:8"]]
- 00b76964 ["CALL", null, ["callee:00c59150:8"]]
+ 00b77958 ["INT_ADD", "register:40f0:8", ["const:b77958:8", "const:4:8"]]
+ 00b77958 ["CALL", null, ["callee:00c59150:8"]]
- 00b76964 bytes 07860394
+ 00b77958 bytes fe850394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf51d0d7b79e5f2346f3daa4e102885f"></a>

### [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) → [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) FUN_00b77dbc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00b72ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md) [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b9847c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 6件 [`00b73fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md) [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b99470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b77f4c",
      "incomplete_value": false,
      "site": "00b77f60",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76f58",
      "incomplete_value": false,
      "site": "00b76f6c",
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
            "const:dfc:8"
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
      "definition_site": "00b77f70",
      "incomplete_value": false,
      "site": "00b77f90",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76f7c",
      "incomplete_value": false,
      "site": "00b76f9c",
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
            "const:ecd:8"
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
      "definition_site": "00b77fb4",
      "incomplete_value": false,
      "site": "00b77fbc",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b76fc0",
      "incomplete_value": false,
      "site": "00b76fc8",
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
            "const:b69:8"
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
      "00b77dfc",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b77e40",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b77e54",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b77dfc",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b77e40",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b77e54",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md#insn-00b76f6c) · [`00b76f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md#insn-00b76f9c) · [`00b76fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md#insn-00b76fc8)
- 新版 [`00b77f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md#insn-00b77f60) · [`00b77f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md#insn-00b77f90) · [`00b77fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md#insn-00b77fbc)

~~~diff
- 00b76f6c ["INT_ADD", "register:40f0:8", ["const:b76f6c:8", "const:4:8"]]
- 00b76f6c ["CALL", null, ["callee:00c5a070:8"]]
+ 00b77f60 ["INT_ADD", "register:40f0:8", ["const:b77f60:8", "const:4:8"]]
+ 00b77f60 ["CALL", null, ["callee:00c5a070:8"]]
- 00b76f6c bytes 4d880394
+ 00b77f60 bytes 44880394
- 00b76f9c ["INT_ADD", "register:40f0:8", ["const:b76f9c:8", "const:4:8"]]
- 00b76f9c ["CALL", null, ["callee:00c59020:8"]]
+ 00b77f90 ["INT_ADD", "register:40f0:8", ["const:b77f90:8", "const:4:8"]]
+ 00b77f90 ["CALL", null, ["callee:00c59020:8"]]
- 00b76f9c bytes 2d840394
+ 00b77f90 bytes 24840394
- 00b76fc8 ["INT_ADD", "register:40f0:8", ["const:b76fc8:8", "const:4:8"]]
- 00b76fc8 ["CALL", null, ["callee:00c59150:8"]]
+ 00b77fbc ["INT_ADD", "register:40f0:8", ["const:b77fbc:8", "const:4:8"]]
+ 00b77fbc ["CALL", null, ["callee:00c59150:8"]]
- 00b76fc8 bytes 6e840394
+ 00b77fbc bytes 65840394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20f6245a394d6d78aa7b97d3d1e46b7b"></a>

### [`00b77418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77418.md) → [`00b7840c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b7840c.md) _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0c0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`00c5d090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d090.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b78468",
      "incomplete_value": true,
      "site": "00b7847c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77474",
      "incomplete_value": true,
      "site": "00b77488",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b784f0",
      "incomplete_value": true,
      "site": "00b784fc",
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
      "definition_site": "00b774fc",
      "incomplete_value": true,
      "site": "00b77508",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78440",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b78444",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b7847c",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b78440",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b78444",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7847c",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77418.md#insn-00b7743c) · [`00b77440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77418.md#insn-00b77440) · [`00b7744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b77418.md#insn-00b7744c)
- 新版 [`00b78430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b7840c.md#insn-00b78430) · [`00b78434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b7840c.md#insn-00b78434) · [`00b78440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b7840c.md#insn-00b78440)

~~~diff
- 00b7743c ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b78430 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b7743c bytes 1a0900f0
+ 00b78430 bytes 1a0900f0
- 00b77440 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b78434 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b77440 bytes 28090090
+ 00b78434 bytes 28090090
- 00b7744c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b7744c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b78440 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b78440 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7744c bytes 5a7746f9
+ 00b78440 bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b50186df9839268932cdc25b7efbab2b"></a>

### [`00b775c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md) → [`00b785bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md) _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b775c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md) [`00c5c600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c600.md) · 呼出先 29件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00b775c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md) [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00b785bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md) [`00c5d5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5d0.md) · 呼出先 29件 [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00b785bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md) [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b788e4",
      "incomplete_value": false,
      "site": "00b788f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:93e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b778f0",
      "incomplete_value": false,
      "site": "00b778fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:871:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b78d20",
      "incomplete_value": false,
      "site": "00b78d2c",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b77d2c",
      "incomplete_value": false,
      "site": "00b77d38",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b78614",
      "DATA",
      [
        "storage",
        "0030e0e7",
        "switchD_00b77630::switchdataD_0030e0e7",
        "byte"
      ]
    ],
    [
      "00b788e4",
      "PARAM",
      [
        "storage",
        "002aa871",
        null,
        "string"
      ]
    ],
    [
      "00b78b58",
      "PARAM",
      [
        "storage",
        "002bbf42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b78614",
      "DATA",
      [
        "storage",
        "0030e127",
        "switchD_00b78624::switchdataD_0030e127",
        "byte"
      ]
    ],
    [
      "00b788e4",
      "PARAM",
      [
        "storage",
        "002aa93e",
        null,
        "string"
      ]
    ],
    [
      "00b78b58",
      "PARAM",
      [
        "storage",
        "002bc020",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b778fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md#insn-00b778fc) · [`00b77d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md#insn-00b77d38) · [`00b77618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md#insn-00b77618)
- 新版 [`00b788f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md#insn-00b788f0) · [`00b78d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md#insn-00b78d2c) · [`00b7860c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md#insn-00b7860c)

~~~diff
- 00b778fc ["INT_ADD", "register:40f0:8", ["const:b778fc:8", "const:4:8"]]
- 00b778fc ["CALL", null, ["callee:00b5bc44:8"]]
+ 00b788f0 ["INT_ADD", "register:40f0:8", ["const:b788f0:8", "const:4:8"]]
+ 00b788f0 ["CALL", null, ["callee:00b5bc44:8"]]
- 00b778fc bytes d58cff97
+ 00b788f0 bytes d58cff97
- 00b77d38 ["INT_ADD", "register:40f0:8", ["const:b77d38:8", "const:4:8"]]
- 00b77d38 ["CALL", null, ["callee:00c59150:8"]]
+ 00b78d2c ["INT_ADD", "register:40f0:8", ["const:b78d2c:8", "const:4:8"]]
+ 00b78d2c ["CALL", null, ["callee:00c59150:8"]]
- 00b77d38 bytes 12810394
+ 00b78d2c bytes 09810394
- 00b77618 ["COPY", "tmp:0:8", ["const:e7:8"]]
- 00b77618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b77618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b77618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b7860c ["COPY", "tmp:0:8", ["const:127:8"]]
+ 00b7860c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7860c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b7860c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b77618 bytes 089d0391
+ 00b7860c bytes 089d0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-115e7f09c63575c1f55e38fa4a63035a"></a>

### [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) → [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) FUN_00b7914c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b775c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b987bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 5件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b785bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b997b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b792dc",
      "incomplete_value": false,
      "site": "00b792f0",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b782e8",
      "incomplete_value": false,
      "site": "00b782fc",
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
            "const:dfc:8"
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
      "definition_site": "00b79300",
      "incomplete_value": false,
      "site": "00b79320",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7830c",
      "incomplete_value": false,
      "site": "00b7832c",
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
            "const:ecd:8"
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
      "definition_site": "00b79344",
      "incomplete_value": false,
      "site": "00b7934c",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78350",
      "incomplete_value": false,
      "site": "00b78358",
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
            "const:b69:8"
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
      "00b7918c",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b791d0",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b791e4",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7918c",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b791d0",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b791e4",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b782fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md#insn-00b782fc) · [`00b7832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md#insn-00b7832c) · [`00b78358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md#insn-00b78358)
- 新版 [`00b792f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md#insn-00b792f0) · [`00b79320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md#insn-00b79320) · [`00b7934c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md#insn-00b7934c)

~~~diff
- 00b782fc ["INT_ADD", "register:40f0:8", ["const:b782fc:8", "const:4:8"]]
- 00b782fc ["CALL", null, ["callee:00c5a070:8"]]
+ 00b792f0 ["INT_ADD", "register:40f0:8", ["const:b792f0:8", "const:4:8"]]
+ 00b792f0 ["CALL", null, ["callee:00c5a070:8"]]
- 00b782fc bytes 69830394
+ 00b792f0 bytes 60830394
- 00b7832c ["INT_ADD", "register:40f0:8", ["const:b7832c:8", "const:4:8"]]
- 00b7832c ["CALL", null, ["callee:00c59020:8"]]
+ 00b79320 ["INT_ADD", "register:40f0:8", ["const:b79320:8", "const:4:8"]]
+ 00b79320 ["CALL", null, ["callee:00c59020:8"]]
- 00b7832c bytes 497f0394
+ 00b79320 bytes 407f0394
- 00b78358 ["INT_ADD", "register:40f0:8", ["const:b78358:8", "const:4:8"]]
- 00b78358 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7934c ["INT_ADD", "register:40f0:8", ["const:b7934c:8", "const:4:8"]]
+ 00b7934c ["CALL", null, ["callee:00c59150:8"]]
- 00b78358 bytes 8a7f0394
+ 00b7934c bytes 817f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ca5839f4c3e50dd791b43256e0c09e"></a>

### [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) → [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) FUN_00b799f0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b775c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b77/00b775c8.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b97f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 5件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b785bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b78/00b785bc.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b98f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b79b80",
      "incomplete_value": false,
      "site": "00b79b94",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78b8c",
      "incomplete_value": false,
      "site": "00b78ba0",
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
            "const:dfc:8"
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
      "definition_site": "00b79ba4",
      "incomplete_value": false,
      "site": "00b79bc4",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78bb0",
      "incomplete_value": false,
      "site": "00b78bd0",
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
            "const:ecd:8"
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
      "definition_site": "00b79be8",
      "incomplete_value": false,
      "site": "00b79bf0",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78bf4",
      "incomplete_value": false,
      "site": "00b78bfc",
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
            "const:b69:8"
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
      "00b79a30",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b79a74",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b79a88",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b79a30",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b79a74",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b79a88",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b78ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md#insn-00b78ba0) · [`00b78bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md#insn-00b78bd0) · [`00b78bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md#insn-00b78bfc)
- 新版 [`00b79b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md#insn-00b79b94) · [`00b79bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md#insn-00b79bc4) · [`00b79bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md#insn-00b79bf0)

~~~diff
- 00b78ba0 ["INT_ADD", "register:40f0:8", ["const:b78ba0:8", "const:4:8"]]
- 00b78ba0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b79b94 ["INT_ADD", "register:40f0:8", ["const:b79b94:8", "const:4:8"]]
+ 00b79b94 ["CALL", null, ["callee:00c5a070:8"]]
- 00b78ba0 bytes 40810394
+ 00b79b94 bytes 37810394
- 00b78bd0 ["INT_ADD", "register:40f0:8", ["const:b78bd0:8", "const:4:8"]]
- 00b78bd0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b79bc4 ["INT_ADD", "register:40f0:8", ["const:b79bc4:8", "const:4:8"]]
+ 00b79bc4 ["CALL", null, ["callee:00c59020:8"]]
- 00b78bd0 bytes 207d0394
+ 00b79bc4 bytes 177d0394
- 00b78bfc ["INT_ADD", "register:40f0:8", ["const:b78bfc:8", "const:4:8"]]
- 00b78bfc ["CALL", null, ["callee:00c59150:8"]]
+ 00b79bf0 ["INT_ADD", "register:40f0:8", ["const:b79bf0:8", "const:4:8"]]
+ 00b79bf0 ["CALL", null, ["callee:00c59150:8"]]
- 00b78bfc bytes 617d0394
+ 00b79bf0 bytes 587d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d578efcd50321e2c2010576de65d7e0f"></a>

### [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) → [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) _ZN11flatbuffers6Parser10ParseTableERKNS_9StructDefEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEPj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c550.md) · 呼出先 41件 [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00b7d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md) [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md)
- 新版 呼出元 1件 [`00c5d520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d520.md) · 呼出先 41件 [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00b7e1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md) [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b79f7c",
      "incomplete_value": true,
      "site": "00b79f9c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b78f88",
      "incomplete_value": true,
      "site": "00b78fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7a244",
      "incomplete_value": true,
      "site": "00b7a258",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
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
    "old": {
      "definition_site": "00b79250",
      "incomplete_value": true,
      "site": "00b79264",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:77a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7a244",
      "incomplete_value": true,
      "site": "00b7a258",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b79250",
      "incomplete_value": true,
      "site": "00b79264",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b79f7c",
      "READ",
      [
        "storage",
        "002c2810",
        null,
        null
      ]
    ],
    [
      "00b7a054",
      "READ",
      [
        "storage",
        "002a97c5",
        null,
        "string"
      ]
    ],
    [
      "00b7a054",
      "READ",
      [
        "storage",
        "002a97d5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b79f7c",
      "READ",
      [
        "storage",
        "002c2860",
        null,
        null
      ]
    ],
    [
      "00b7a054",
      "READ",
      [
        "storage",
        "002a9892",
        null,
        "string"
      ]
    ],
    [
      "00b7a054",
      "READ",
      [
        "storage",
        "002a98a2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md#insn-00b79090) · [`00b79284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md#insn-00b79284) · [`00b7a084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md#insn-00b7a084)
- 新版 [`00b7a084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md#insn-00b7a084) · [`00b7a278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md#insn-00b7a278) · [`00b7b078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md#insn-00b7b078)

~~~diff
- 00b79090 ["INT_ADD", "register:40f0:8", ["const:b79090:8", "const:4:8"]]
- 00b79090 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7a084 ["INT_ADD", "register:40f0:8", ["const:b7a084:8", "const:4:8"]]
+ 00b7a084 ["CALL", null, ["callee:00c59150:8"]]
- 00b79090 bytes 3c7c0394
+ 00b7a084 bytes 337c0394
- 00b79284 ["INT_ADD", "register:40f0:8", ["const:b79284:8", "const:4:8"]]
- 00b79284 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7a278 ["INT_ADD", "register:40f0:8", ["const:b7a278:8", "const:4:8"]]
+ 00b7a278 ["CALL", null, ["callee:00c59150:8"]]
- 00b79284 bytes bf7b0394
+ 00b7a278 bytes b67b0394
- 00b7a084 ["INT_ADD", "register:40f0:8", ["const:b7a084:8", "const:4:8"]]
- 00b7a084 ["CALL", null, ["callee:00c5d050:8"]]
+ 00b7b078 ["INT_ADD", "register:40f0:8", ["const:b7b078:8", "const:4:8"]]
+ 00b7b078 ["CALL", null, ["callee:00c5d050:8"]]
- 00b7a084 bytes ff870394
+ 00b7b078 bytes f6870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4acf191c9388e99340028cea964a9182"></a>

### [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) → [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) _ZN11flatbuffers6Parser11ParseVectorERKNS_4TypeEPjPNS_8FieldDefEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5b0.md) · 呼出先 31件 [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00b7d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md) [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md)
- 新版 呼出元 1件 [`00c5d580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d580.md) · 呼出先 31件 [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00b7e1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md) [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7c6bc",
      "incomplete_value": true,
      "site": "00b7c6bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:a43:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7b6c8",
      "incomplete_value": true,
      "site": "00b7b6c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:9f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7d034",
      "value": [
        "leaf",
        "ram:b80ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c040",
      "value": [
        "leaf",
        "ram:b7fed8:8"
      ]
    },
    "ordinal": 46,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7c3c8",
      "DATA",
      [
        "storage",
        "0030e11a",
        "switchD_00b7b3e0::switchdataD_0030e11a",
        "byte"
      ]
    ],
    [
      "00b7c4b4",
      "DATA",
      [
        "storage",
        "0030e12d",
        "switchD_00b7b4cc::switchdataD_0030e12d",
        "byte"
      ]
    ],
    [
      "00b7c514",
      "DATA",
      [
        "storage",
        "0030e140",
        "switchD_00b7b538::switchdataD_0030e140",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b7c3c8",
      "DATA",
      [
        "storage",
        "0030e15a",
        "switchD_00b7c3d4::switchdataD_0030e15a",
        "byte"
      ]
    ],
    [
      "00b7c4b4",
      "DATA",
      [
        "storage",
        "0030e16d",
        "switchD_00b7c4c0::switchdataD_0030e16d",
        "byte"
      ]
    ],
    [
      "00b7c514",
      "DATA",
      [
        "storage",
        "0030e180",
        "switchD_00b7c52c::switchdataD_0030e180",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md#insn-00b7c040) · [`00b7b394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md#insn-00b7b394) · [`00b7b3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md#insn-00b7b3cc)
- 新版 [`00b7d034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md#insn-00b7d034) · [`00b7c388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md#insn-00b7c388) · [`00b7c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md#insn-00b7c3c0)

~~~diff
- 00b7c040 ["INT_ADD", "register:40f0:8", ["const:b7c040:8", "const:4:8"]]
- 00b7c040 ["CALL", null, ["ram:b7fed8:8"]]
+ 00b7d034 ["INT_ADD", "register:40f0:8", ["const:b7d034:8", "const:4:8"]]
+ 00b7d034 ["CALL", null, ["ram:b80ecc:8"]]
- 00b7c040 bytes a60f0094
+ 00b7d034 bytes a60f0094
- 00b7b394 ["INT_ADD", "register:40f0:8", ["const:b7b394:8", "const:4:8"]]
- 00b7b394 ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b7c388 ["INT_ADD", "register:40f0:8", ["const:b7c388:8", "const:4:8"]]
+ 00b7c388 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b7b394 bytes 23850394
+ 00b7c388 bytes 1a850394
- 00b7b3cc ["COPY", "tmp:0:8", ["const:11a:8"]]
- 00b7b3cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b7b3cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b7b3cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b7c3c0 ["COPY", "tmp:0:8", ["const:15a:8"]]
+ 00b7c3c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b7c3c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b7c3c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b7b3cc bytes 29690491
+ 00b7c3c0 bytes 29690591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c464b3996fc93df1028e355a6cfe8b1"></a>

### [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) → [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) _ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5c530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c530.md) · 呼出先 31件 [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00b7d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md) [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md)
- 新版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d500.md) · 呼出先 31件 [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00b7e1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md) [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7d0b8",
      "incomplete_value": true,
      "site": "00b7d0f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c0c4",
      "incomplete_value": true,
      "site": "00b7c0fc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:170:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7da08",
      "incomplete_value": true,
      "site": "00b7da18",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:c7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ca14",
      "incomplete_value": true,
      "site": "00b7ca24",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:c3a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 99,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b7da08",
      "incomplete_value": true,
      "site": "00b7da18",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ca14",
      "incomplete_value": true,
      "site": "00b7ca24",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 100,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7d0b8",
      "READ",
      [
        "storage",
        "002c3170",
        null,
        null
      ]
    ],
    [
      "00b7d298",
      "DATA",
      [
        "storage",
        "0030e1b3",
        "switchD_00b7c2ac::switchdataD_0030e1b3",
        "byte"
      ]
    ],
    [
      "00b7da04",
      "READ",
      [
        "storage",
        "002c2650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7d0b8",
      "READ",
      [
        "storage",
        "002c31c0",
        null,
        null
      ]
    ],
    [
      "00b7d298",
      "DATA",
      [
        "storage",
        "0030e1f3",
        "switchD_00b7d2a0::switchdataD_0030e1f3",
        "byte"
      ]
    ],
    [
      "00b7da04",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md#insn-00b7ca40) · [`00b7c0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md#insn-00b7c0c4) · [`00b7c15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md#insn-00b7c15c)
- 新版 [`00b7da34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md#insn-00b7da34) · [`00b7d0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md#insn-00b7d0b8) · [`00b7d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md#insn-00b7d150)

~~~diff
- 00b7ca40 ["INT_ADD", "register:40f0:8", ["const:b7ca40:8", "const:4:8"]]
- 00b7ca40 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7da34 ["INT_ADD", "register:40f0:8", ["const:b7da34:8", "const:4:8"]]
+ 00b7da34 ["CALL", null, ["callee:00c59150:8"]]
- 00b7ca40 bytes d06d0394
+ 00b7da34 bytes c76d0394
- 00b7c0c4 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:170:8"]]
- 00b7c0c4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00b7c0c4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00b7c0c4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00b7d0b8 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:1c0:8"]]
+ 00b7d0b8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00b7d0b8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00b7d0b8 ["COPY", "register:5018:8", ["const:0:8"]]
- 00b7c0c4 bytes 605dc03d
+ 00b7d0b8 bytes 6071c03d
- 00b7c15c ["INT_ADD", "register:40f0:8", ["const:b7c15c:8", "const:4:8"]]
- 00b7c15c ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b7d150 ["INT_ADD", "register:40f0:8", ["const:b7d150:8", "const:4:8"]]
+ 00b7d150 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b7c15c bytes b1810394
+ 00b7d150 bytes a8810394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83cd74d988fd99fe2b2787ac1dd356fc"></a>

### [`00b7cae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cae4.md) → [`00b7dad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7dad8.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c880.md) · 呼出先 11件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md) [`00c5c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0c0.md)
- 新版 呼出元 1件 [`00c5d850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d850.md) · 呼出先 11件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md) [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md) [`00c5d090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.00% / 新版 89.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7dc10",
      "incomplete_value": false,
      "site": "00b7dc18",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cc1c",
      "incomplete_value": false,
      "site": "00b7cc24",
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
            "const:b28:8"
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
      "definition_site": "00b7dc24",
      "incomplete_value": false,
      "site": "00b7dc2c",
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
            "const:7bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cc30",
      "incomplete_value": false,
      "site": "00b7cc38",
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
            "const:6e8:8"
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
      "definition_site": "00b7dc44",
      "incomplete_value": false,
      "site": "00b7dc4c",
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
            "const:a76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cc50",
      "incomplete_value": false,
      "site": "00b7cc58",
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
            "const:998:8"
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
      "00b7db74",
      "DATA",
      [
        "storage",
        "0030e1c6",
        "switchD_00b7cb88::switchdataD_0030e1c6",
        "byte"
      ]
    ],
    [
      "00b7dc10",
      "PARAM",
      [
        "storage",
        "0029fb28",
        null,
        "string"
      ]
    ],
    [
      "00b7dc24",
      "PARAM",
      [
        "storage",
        "002b06e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7db74",
      "DATA",
      [
        "storage",
        "0030e206",
        "switchD_00b7db7c::switchdataD_0030e206",
        "byte"
      ]
    ],
    [
      "00b7dc10",
      "PARAM",
      [
        "storage",
        "0029fb68",
        null,
        "string"
      ]
    ],
    [
      "00b7dc24",
      "PARAM",
      [
        "storage",
        "002b07bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cae4.md#insn-00b7cc24) · [`00b7cc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cae4.md#insn-00b7cc38) · [`00b7cc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cae4.md#insn-00b7cc58)
- 新版 [`00b7dc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7dad8.md#insn-00b7dc18) · [`00b7dc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7dad8.md#insn-00b7dc2c) · [`00b7dc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7dad8.md#insn-00b7dc4c)

~~~diff
- 00b7cc24 ["INT_ADD", "register:40f0:8", ["const:b7cc24:8", "const:4:8"]]
- 00b7cc24 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b7dc18 ["INT_ADD", "register:40f0:8", ["const:b7dc18:8", "const:4:8"]]
+ 00b7dc18 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b7cc24 bytes 3f7b0394
+ 00b7dc18 bytes 367b0394
- 00b7cc38 ["INT_ADD", "register:40f0:8", ["const:b7cc38:8", "const:4:8"]]
- 00b7cc38 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b7dc2c ["INT_ADD", "register:40f0:8", ["const:b7dc2c:8", "const:4:8"]]
+ 00b7dc2c ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b7cc38 bytes 3a7b0394
+ 00b7dc2c bytes 317b0394
- 00b7cc58 ["INT_ADD", "register:40f0:8", ["const:b7cc58:8", "const:4:8"]]
- 00b7cc58 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00b7dc4c ["INT_ADD", "register:40f0:8", ["const:b7dc4c:8", "const:4:8"]]
+ 00b7dc4c ["CALL", null, ["callee:00c5c8f0:8"]]
- 00b7cc58 bytes 327b0394
+ 00b7dc4c bytes 297b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d59e232d1066f7f1935d267ab010253"></a>

### [`00b7d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md) → [`00b7e1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md) FUN_00b7e1c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b9813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9813c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b99130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99130.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e3bc",
      "incomplete_value": false,
      "site": "00b7e3c4",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d3c8",
      "incomplete_value": false,
      "site": "00b7d3d0",
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
            "const:b69:8"
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
      "definition_site": "00b7e460",
      "incomplete_value": false,
      "site": "00b7e474",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d46c",
      "incomplete_value": false,
      "site": "00b7d480",
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
            "const:dfc:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e484",
      "incomplete_value": false,
      "site": "00b7e4a4",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d490",
      "incomplete_value": false,
      "site": "00b7d4b0",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b7e200",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e244",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7e258",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7e200",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e244",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7e258",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md#insn-00b7d3d0) · [`00b7d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md#insn-00b7d480) · [`00b7d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d1cc.md#insn-00b7d4b0)
- 新版 [`00b7e3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md#insn-00b7e3c4) · [`00b7e474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md#insn-00b7e474) · [`00b7e4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e1c0.md#insn-00b7e4a4)

~~~diff
- 00b7d3d0 ["INT_ADD", "register:40f0:8", ["const:b7d3d0:8", "const:4:8"]]
- 00b7d3d0 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7e3c4 ["INT_ADD", "register:40f0:8", ["const:b7e3c4:8", "const:4:8"]]
+ 00b7e3c4 ["CALL", null, ["callee:00c59150:8"]]
- 00b7d3d0 bytes 6c6b0394
+ 00b7e3c4 bytes 636b0394
- 00b7d480 ["INT_ADD", "register:40f0:8", ["const:b7d480:8", "const:4:8"]]
- 00b7d480 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7e474 ["INT_ADD", "register:40f0:8", ["const:b7e474:8", "const:4:8"]]
+ 00b7e474 ["CALL", null, ["callee:00c5a070:8"]]
- 00b7d480 bytes 086f0394
+ 00b7e474 bytes ff6e0394
- 00b7d4b0 ["INT_ADD", "register:40f0:8", ["const:b7d4b0:8", "const:4:8"]]
- 00b7d4b0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7e4a4 ["INT_ADD", "register:40f0:8", ["const:b7e4a4:8", "const:4:8"]]
+ 00b7e4a4 ["CALL", null, ["callee:00c59020:8"]]
- 00b7d4b0 bytes e86a0394
+ 00b7e4a4 bytes df6a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eca5948d476236b4aa38191b899029b"></a>

### [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md) → [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md) FUN_00b7e718

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b982dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b992d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7e8ac",
      "incomplete_value": false,
      "site": "00b7e8c0",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d8b8",
      "incomplete_value": false,
      "site": "00b7d8cc",
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
            "const:dfc:8"
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
      "definition_site": "00b7e8d0",
      "incomplete_value": false,
      "site": "00b7e8f0",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d8dc",
      "incomplete_value": false,
      "site": "00b7d8fc",
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
            "const:ecd:8"
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
      "definition_site": "00b7e914",
      "incomplete_value": false,
      "site": "00b7e91c",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d920",
      "incomplete_value": false,
      "site": "00b7d928",
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
            "const:b69:8"
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
      "00b7e758",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e79c",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7e7b0",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7e758",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7e79c",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7e7b0",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md#insn-00b7d8cc) · [`00b7d8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md#insn-00b7d8fc) · [`00b7d928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md#insn-00b7d928)
- 新版 [`00b7e8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md#insn-00b7e8c0) · [`00b7e8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md#insn-00b7e8f0) · [`00b7e91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md#insn-00b7e91c)

~~~diff
- 00b7d8cc ["INT_ADD", "register:40f0:8", ["const:b7d8cc:8", "const:4:8"]]
- 00b7d8cc ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7e8c0 ["INT_ADD", "register:40f0:8", ["const:b7e8c0:8", "const:4:8"]]
+ 00b7e8c0 ["CALL", null, ["callee:00c5a070:8"]]
- 00b7d8cc bytes f56d0394
+ 00b7e8c0 bytes ec6d0394
- 00b7d8fc ["INT_ADD", "register:40f0:8", ["const:b7d8fc:8", "const:4:8"]]
- 00b7d8fc ["CALL", null, ["callee:00c59020:8"]]
+ 00b7e8f0 ["INT_ADD", "register:40f0:8", ["const:b7e8f0:8", "const:4:8"]]
+ 00b7e8f0 ["CALL", null, ["callee:00c59020:8"]]
- 00b7d8fc bytes d5690394
+ 00b7e8f0 bytes cc690394
- 00b7d928 ["INT_ADD", "register:40f0:8", ["const:b7d928:8", "const:4:8"]]
- 00b7d928 ["CALL", null, ["callee:00c59150:8"]]
+ 00b7e91c ["INT_ADD", "register:40f0:8", ["const:b7e91c:8", "const:4:8"]]
+ 00b7e91c ["CALL", null, ["callee:00c59150:8"]]
- 00b7d928 bytes 166a0394
+ 00b7e91c bytes 0d6a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9dfc39fc39787ebc66b9c73c50966d8"></a>

### [`00b7dee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md) → [`00b7eedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eedc.md) FUN_00b7eedc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b9861c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b99610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f094",
      "incomplete_value": false,
      "site": "00b7f0b4",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e0a0",
      "incomplete_value": false,
      "site": "00b7e0c0",
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
            "const:ecd:8"
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
      "definition_site": "00b7f0d8",
      "incomplete_value": false,
      "site": "00b7f0e0",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e0e4",
      "incomplete_value": false,
      "site": "00b7e0ec",
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
            "const:b69:8"
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
      "definition_site": "00b7f17c",
      "incomplete_value": false,
      "site": "00b7f190",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e188",
      "incomplete_value": false,
      "site": "00b7e19c",
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
            "const:dfc:8"
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
      "00b7ef1c",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ef60",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7ef74",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7ef1c",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b7ef60",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ],
    [
      "00b7ef74",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md#insn-00b7e0c0) · [`00b7e0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md#insn-00b7e0ec) · [`00b7e19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md#insn-00b7e19c)
- 新版 [`00b7f0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eedc.md#insn-00b7f0b4) · [`00b7f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eedc.md#insn-00b7f0e0) · [`00b7f190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eedc.md#insn-00b7f190)

~~~diff
- 00b7e0c0 ["INT_ADD", "register:40f0:8", ["const:b7e0c0:8", "const:4:8"]]
- 00b7e0c0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7f0b4 ["INT_ADD", "register:40f0:8", ["const:b7f0b4:8", "const:4:8"]]
+ 00b7f0b4 ["CALL", null, ["callee:00c59020:8"]]
- 00b7e0c0 bytes e4670394
+ 00b7f0b4 bytes db670394
- 00b7e0ec ["INT_ADD", "register:40f0:8", ["const:b7e0ec:8", "const:4:8"]]
- 00b7e0ec ["CALL", null, ["callee:00c59150:8"]]
+ 00b7f0e0 ["INT_ADD", "register:40f0:8", ["const:b7f0e0:8", "const:4:8"]]
+ 00b7f0e0 ["CALL", null, ["callee:00c59150:8"]]
- 00b7e0ec bytes 25680394
+ 00b7f0e0 bytes 1c680394
- 00b7e19c ["INT_ADD", "register:40f0:8", ["const:b7e19c:8", "const:4:8"]]
- 00b7e19c ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7f190 ["INT_ADD", "register:40f0:8", ["const:b7f190:8", "const:4:8"]]
+ 00b7f190 ["CALL", null, ["callee:00c5a070:8"]]
- 00b7e19c bytes c16b0394
+ 00b7f190 bytes b86b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67463cd3195c88cc9b4022921e160587"></a>

### [`00b7e52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e52c.md) → [`00b7f520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f520.md) FUN_00b7f520

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b9895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b99950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7f62c",
      "incomplete_value": false,
      "site": "00b7f640",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e638",
      "incomplete_value": false,
      "site": "00b7e64c",
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
            "const:dfc:8"
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
      "definition_site": "00b7f650",
      "incomplete_value": false,
      "site": "00b7f670",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e65c",
      "incomplete_value": false,
      "site": "00b7e67c",
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
            "const:ecd:8"
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
      "definition_site": "00b7f680",
      "incomplete_value": false,
      "site": "00b7f69c",
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
            "const:bae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e68c",
      "incomplete_value": false,
      "site": "00b7e6a8",
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
            "const:b6e:8"
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
      "00b7f62c",
      "PARAM",
      [
        "storage",
        "002b6dfc",
        null,
        "string"
      ]
    ],
    [
      "00b7f650",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00b7f680",
      "PARAM",
      [
        "storage",
        "002a1b6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7f62c",
      "PARAM",
      [
        "storage",
        "002b6ecb",
        null,
        "string"
      ]
    ],
    [
      "00b7f650",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ],
    [
      "00b7f680",
      "PARAM",
      [
        "storage",
        "002a1bae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e52c.md#insn-00b7e64c) · [`00b7e67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e52c.md#insn-00b7e67c) · [`00b7e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e52c.md#insn-00b7e6a8)
- 新版 [`00b7f640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f520.md#insn-00b7f640) · [`00b7f670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f520.md#insn-00b7f670) · [`00b7f69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f520.md#insn-00b7f69c)

~~~diff
- 00b7e64c ["INT_ADD", "register:40f0:8", ["const:b7e64c:8", "const:4:8"]]
- 00b7e64c ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7f640 ["INT_ADD", "register:40f0:8", ["const:b7f640:8", "const:4:8"]]
+ 00b7f640 ["CALL", null, ["callee:00c5a070:8"]]
- 00b7e64c bytes 956a0394
+ 00b7f640 bytes 8c6a0394
- 00b7e67c ["INT_ADD", "register:40f0:8", ["const:b7e67c:8", "const:4:8"]]
- 00b7e67c ["CALL", null, ["callee:00c59020:8"]]
+ 00b7f670 ["INT_ADD", "register:40f0:8", ["const:b7f670:8", "const:4:8"]]
+ 00b7f670 ["CALL", null, ["callee:00c59020:8"]]
- 00b7e67c bytes 75660394
+ 00b7f670 bytes 6c660394
- 00b7e6a8 ["INT_ADD", "register:40f0:8", ["const:b7e6a8:8", "const:4:8"]]
- 00b7e6a8 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7f69c ["INT_ADD", "register:40f0:8", ["const:b7f69c:8", "const:4:8"]]
+ 00b7f69c ["CALL", null, ["callee:00c59020:8"]]
- 00b7e6a8 bytes 6a660394
+ 00b7f69c bytes 61660394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f01bdbdb1613c733af614e2cc1d62e3"></a>

### [`00b7e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e9f0.md) → [`00b7f9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f9e4.md) FUN_00b7f9e4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 12件 [`00b98afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 12件 [`00b99af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7fb04",
      "incomplete_value": false,
      "site": "00b7fb18",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb10",
      "incomplete_value": false,
      "site": "00b7eb24",
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
            "const:dfc:8"
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
      "definition_site": "00b7fb28",
      "incomplete_value": false,
      "site": "00b7fb48",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb34",
      "incomplete_value": false,
      "site": "00b7eb54",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7fb58",
      "incomplete_value": false,
      "site": "00b7fb74",
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
            "const:bae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eb64",
      "incomplete_value": false,
      "site": "00b7eb80",
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
            "const:b6e:8"
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
      "00b7fb04",
      "PARAM",
      [
        "storage",
        "002b6dfc",
        null,
        "string"
      ]
    ],
    [
      "00b7fb28",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00b7fb58",
      "PARAM",
      [
        "storage",
        "002a1b6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7fb04",
      "PARAM",
      [
        "storage",
        "002b6ecb",
        null,
        "string"
      ]
    ],
    [
      "00b7fb28",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ],
    [
      "00b7fb58",
      "PARAM",
      [
        "storage",
        "002a1bae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7eb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e9f0.md#insn-00b7eb24) · [`00b7eb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e9f0.md#insn-00b7eb54) · [`00b7eb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e9f0.md#insn-00b7eb80)
- 新版 [`00b7fb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f9e4.md#insn-00b7fb18) · [`00b7fb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f9e4.md#insn-00b7fb48) · [`00b7fb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f9e4.md#insn-00b7fb74)

~~~diff
- 00b7eb24 ["INT_ADD", "register:40f0:8", ["const:b7eb24:8", "const:4:8"]]
- 00b7eb24 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7fb18 ["INT_ADD", "register:40f0:8", ["const:b7fb18:8", "const:4:8"]]
+ 00b7fb18 ["CALL", null, ["callee:00c5a070:8"]]
- 00b7eb24 bytes 5f690394
+ 00b7fb18 bytes 56690394
- 00b7eb54 ["INT_ADD", "register:40f0:8", ["const:b7eb54:8", "const:4:8"]]
- 00b7eb54 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7fb48 ["INT_ADD", "register:40f0:8", ["const:b7fb48:8", "const:4:8"]]
+ 00b7fb48 ["CALL", null, ["callee:00c59020:8"]]
- 00b7eb54 bytes 3f650394
+ 00b7fb48 bytes 36650394
- 00b7eb80 ["INT_ADD", "register:40f0:8", ["const:b7eb80:8", "const:4:8"]]
- 00b7eb80 ["CALL", null, ["callee:00c59020:8"]]
+ 00b7fb74 ["INT_ADD", "register:40f0:8", ["const:b7fb74:8", "const:4:8"]]
+ 00b7fb74 ["CALL", null, ["callee:00c59020:8"]]
- 00b7eb80 bytes 34650394
+ 00b7fb74 bytes 2b650394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29255ac74f05d2e3883150c1bc7e7f3e"></a>

### [`00b7ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ef04.md) → [`00b7fef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fef8.md) FUN_00b7fef8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 4件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.64% / 新版 97.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b7ffc8",
      "incomplete_value": false,
      "site": "00b7ffdc",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7efd4",
      "incomplete_value": false,
      "site": "00b7efe8",
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
            "const:dfc:8"
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
      "definition_site": "00b7ffec",
      "incomplete_value": false,
      "site": "00b8000c",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eff8",
      "incomplete_value": false,
      "site": "00b7f018",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80030",
      "incomplete_value": false,
      "site": "00b80038",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f03c",
      "incomplete_value": false,
      "site": "00b7f044",
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
            "const:b69:8"
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
      "00b7ffc8",
      "PARAM",
      [
        "storage",
        "002b6dfc",
        null,
        "string"
      ]
    ],
    [
      "00b7ffec",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00b80030",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7ffc8",
      "PARAM",
      [
        "storage",
        "002b6ecb",
        null,
        "string"
      ]
    ],
    [
      "00b7ffec",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ],
    [
      "00b80030",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7efe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ef04.md#insn-00b7efe8) · [`00b7f018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ef04.md#insn-00b7f018) · [`00b7f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7ef04.md#insn-00b7f044)
- 新版 [`00b7ffdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fef8.md#insn-00b7ffdc) · [`00b8000c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fef8.md#insn-00b8000c) · [`00b80038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7fef8.md#insn-00b80038)

~~~diff
- 00b7efe8 ["INT_ADD", "register:40f0:8", ["const:b7efe8:8", "const:4:8"]]
- 00b7efe8 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b7ffdc ["INT_ADD", "register:40f0:8", ["const:b7ffdc:8", "const:4:8"]]
+ 00b7ffdc ["CALL", null, ["callee:00c5a070:8"]]
- 00b7efe8 bytes 2e680394
+ 00b7ffdc bytes 25680394
- 00b7f018 ["INT_ADD", "register:40f0:8", ["const:b7f018:8", "const:4:8"]]
- 00b7f018 ["CALL", null, ["callee:00c59020:8"]]
+ 00b8000c ["INT_ADD", "register:40f0:8", ["const:b8000c:8", "const:4:8"]]
+ 00b8000c ["CALL", null, ["callee:00c59020:8"]]
- 00b7f018 bytes 0e640394
+ 00b8000c bytes 05640394
- 00b7f044 ["INT_ADD", "register:40f0:8", ["const:b7f044:8", "const:4:8"]]
- 00b7f044 ["CALL", null, ["callee:00c59150:8"]]
+ 00b80038 ["INT_ADD", "register:40f0:8", ["const:b80038:8", "const:4:8"]]
+ 00b80038 ["CALL", null, ["callee:00c59150:8"]]
- 00b7f044 bytes 4f640394
+ 00b80038 bytes 46640394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a870839d761700c07a53789b7078a2cd"></a>

### [`00b7f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f1e4.md) → [`00b801d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b801d8.md) FUN_00b801d8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00b754dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b75/00b754dc.md) [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) [`00b7b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7b/00b7b314.md) [`00b7c098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7c098.md) [`00b81808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81808.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 5件 [`00b764d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b76/00b764d0.md) [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) [`00b7c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7c/00b7c308.md) [`00b7d08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7d/00b7d08c.md) [`00b827fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b827fc.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b802a8",
      "incomplete_value": false,
      "site": "00b802bc",
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
            "const:ecb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f2b4",
      "incomplete_value": false,
      "site": "00b7f2c8",
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
            "const:dfc:8"
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
      "definition_site": "00b802cc",
      "incomplete_value": false,
      "site": "00b802ec",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f2d8",
      "incomplete_value": false,
      "site": "00b7f2f8",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80310",
      "incomplete_value": false,
      "site": "00b80318",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f31c",
      "incomplete_value": false,
      "site": "00b7f324",
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
            "const:b69:8"
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
      "00b802a8",
      "PARAM",
      [
        "storage",
        "002b6dfc",
        null,
        "string"
      ]
    ],
    [
      "00b802cc",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00b80310",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b802a8",
      "PARAM",
      [
        "storage",
        "002b6ecb",
        null,
        "string"
      ]
    ],
    [
      "00b802cc",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ],
    [
      "00b80310",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f1e4.md#insn-00b7f2c8) · [`00b7f2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f1e4.md#insn-00b7f2f8) · [`00b7f324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f1e4.md#insn-00b7f324)
- 新版 [`00b802bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b801d8.md#insn-00b802bc) · [`00b802ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b801d8.md#insn-00b802ec) · [`00b80318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b801d8.md#insn-00b80318)

~~~diff
- 00b7f2c8 ["INT_ADD", "register:40f0:8", ["const:b7f2c8:8", "const:4:8"]]
- 00b7f2c8 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b802bc ["INT_ADD", "register:40f0:8", ["const:b802bc:8", "const:4:8"]]
+ 00b802bc ["CALL", null, ["callee:00c5a070:8"]]
- 00b7f2c8 bytes 76670394
+ 00b802bc bytes 6d670394
- 00b7f2f8 ["INT_ADD", "register:40f0:8", ["const:b7f2f8:8", "const:4:8"]]
- 00b7f2f8 ["CALL", null, ["callee:00c59020:8"]]
+ 00b802ec ["INT_ADD", "register:40f0:8", ["const:b802ec:8", "const:4:8"]]
+ 00b802ec ["CALL", null, ["callee:00c59020:8"]]
- 00b7f2f8 bytes 56630394
+ 00b802ec bytes 4d630394
- 00b7f324 ["INT_ADD", "register:40f0:8", ["const:b7f324:8", "const:4:8"]]
- 00b7f324 ["CALL", null, ["callee:00c59150:8"]]
+ 00b80318 ["INT_ADD", "register:40f0:8", ["const:b80318:8", "const:4:8"]]
+ 00b80318 ["CALL", null, ["callee:00c59150:8"]]
- 00b7f324 bytes 97630394
+ 00b80318 bytes 8e630394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebff810685951d1ba7dee1c189939b0c"></a>

### [`00b7f900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f900.md) → [`00b808f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b808f4.md) _ZN11flatbuffers6Parser19ParseAlignAttributeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEmPm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c750.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md)
- 新版 呼出元 1件 [`00c5d720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d720.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80a14",
      "incomplete_value": false,
      "site": "00b80a24",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fa20",
      "incomplete_value": false,
      "site": "00b7fa30",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b80a2c",
      "incomplete_value": false,
      "site": "00b80a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fa38",
      "incomplete_value": false,
      "site": "00b7fa44",
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
            "const:f6c:8"
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
      "definition_site": "00b80a94",
      "incomplete_value": false,
      "site": "00b80ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:bf4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7faa0",
      "incomplete_value": false,
      "site": "00b7fabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:baa:8"
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
      "00b80988",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b809a0",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00b809b0",
      "READ",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b80988",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b809a0",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b809b0",
      "READ",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f900.md#insn-00b7fa30) · [`00b7fa44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f900.md#insn-00b7fa44) · [`00b7fabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f900.md#insn-00b7fabc)
- 新版 [`00b80a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b808f4.md#insn-00b80a24) · [`00b80a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b808f4.md#insn-00b80a38) · [`00b80ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b808f4.md#insn-00b80ab0)

~~~diff
- 00b7fa30 ["INT_ADD", "register:40f0:8", ["const:b7fa30:8", "const:4:8"]]
- 00b7fa30 ["CALL", null, ["callee:00c59150:8"]]
+ 00b80a24 ["INT_ADD", "register:40f0:8", ["const:b80a24:8", "const:4:8"]]
+ 00b80a24 ["CALL", null, ["callee:00c59150:8"]]
- 00b7fa30 bytes d4610394
+ 00b80a24 bytes cb610394
- 00b7fa44 ["INT_ADD", "register:40f0:8", ["const:b7fa44:8", "const:4:8"]]
- 00b7fa44 ["CALL", null, ["callee:00c59020:8"]]
+ 00b80a38 ["INT_ADD", "register:40f0:8", ["const:b80a38:8", "const:4:8"]]
+ 00b80a38 ["CALL", null, ["callee:00c59020:8"]]
- 00b7fa44 bytes 83610394
+ 00b80a38 bytes 7a610394
- 00b7fabc ["INT_ADD", "register:40f0:8", ["const:b7fabc:8", "const:4:8"]]
- 00b7fabc ["CALL", null, ["callee:00c59020:8"]]
+ 00b80ab0 ["INT_ADD", "register:40f0:8", ["const:b80ab0:8", "const:4:8"]]
+ 00b80ab0 ["CALL", null, ["callee:00c59020:8"]]
- 00b7fabc bytes 65610394
+ 00b80ab0 bytes 5c610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1da63f6ca431330c3fcdd19302f0826e"></a>

### [`00b7fc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fc30.md) → [`00b80c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80c24.md) _ZN11flatbuffers11NumToStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0e0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582d0.md)
- 新版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0b0.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c592a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80c7c",
      "incomplete_value": true,
      "site": "00b80c90",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fc88",
      "incomplete_value": true,
      "site": "00b7fc9c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80c74",
      "incomplete_value": true,
      "site": "00b80c94",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fc80",
      "incomplete_value": true,
      "site": "00b7fca0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b80d04",
      "incomplete_value": true,
      "site": "00b80d10",
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
      "definition_site": "00b7fd10",
      "incomplete_value": true,
      "site": "00b7fd1c",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b80c54",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b80c58",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b80c90",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b80c54",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b80c58",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b80c90",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fc30.md#insn-00b7fc54) · [`00b7fc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fc30.md#insn-00b7fc58) · [`00b7fc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7fc30.md#insn-00b7fc60)
- 新版 [`00b80c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80c24.md#insn-00b80c48) · [`00b80c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80c24.md#insn-00b80c4c) · [`00b80c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b80c24.md#insn-00b80c54)

~~~diff
- 00b7fc54 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b80c48 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b7fc54 bytes da0800f0
+ 00b80c48 bytes da0800f0
- 00b7fc58 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b80c4c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b7fc58 bytes e8080090
+ 00b80c4c bytes e8080090
- 00b7fc60 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b7fc60 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b80c54 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b80c54 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7fc60 bytes 5a7746f9
+ 00b80c54 bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d246d2391b505b8b55257fbce2fea2"></a>

### [`00b8040c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b8040c.md) → [`00b81400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81400.md) _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c780.md) · 呼出先 20件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d750.md) · 呼出先 20件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b814f4",
      "incomplete_value": true,
      "site": "00b81504",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b80500",
      "incomplete_value": true,
      "site": "00b80510",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:210:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81500",
      "incomplete_value": true,
      "site": "00b81510",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:b4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8050c",
      "incomplete_value": true,
      "site": "00b8051c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:b0e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81500",
      "incomplete_value": true,
      "site": "00b81510",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8050c",
      "incomplete_value": true,
      "site": "00b8051c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b814f4",
      "READ",
      [
        "storage",
        "002c3210",
        null,
        null
      ]
    ],
    [
      "00b81500",
      "READ",
      [
        "storage",
        "002a1b0e",
        null,
        "string"
      ]
    ],
    [
      "00b81500",
      "READ",
      [
        "storage",
        "002a1b1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b814f4",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "00b81500",
      "READ",
      [
        "storage",
        "002a1b4e",
        null,
        "string"
      ]
    ],
    [
      "00b81500",
      "READ",
      [
        "storage",
        "002a1b5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b8040c.md#insn-00b80540) · [`00b807a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b8040c.md#insn-00b807a4) · [`00b80474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b8040c.md#insn-00b80474)
- 新版 [`00b81534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81400.md#insn-00b81534) · [`00b81798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81400.md#insn-00b81798) · [`00b81468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81400.md#insn-00b81468)

~~~diff
- 00b80540 ["INT_ADD", "register:40f0:8", ["const:b80540:8", "const:4:8"]]
- 00b80540 ["CALL", null, ["callee:00c59150:8"]]
+ 00b81534 ["INT_ADD", "register:40f0:8", ["const:b81534:8", "const:4:8"]]
+ 00b81534 ["CALL", null, ["callee:00c59150:8"]]
- 00b80540 bytes 105f0394
+ 00b81534 bytes 075f0394
- 00b807a4 ["INT_ADD", "register:40f0:8", ["const:b807a4:8", "const:4:8"]]
- 00b807a4 ["CALL", null, ["callee:00c59150:8"]]
+ 00b81798 ["INT_ADD", "register:40f0:8", ["const:b81798:8", "const:4:8"]]
+ 00b81798 ["CALL", null, ["callee:00c59150:8"]]
- 00b807a4 bytes 775e0394
+ 00b81798 bytes 6e5e0394
- 00b80474 ["INT_ADD", "register:40f0:8", ["const:b80474:8", "const:4:8"]]
- 00b80474 ["CALL", null, ["callee:00c5d5d0:8"]]
+ 00b81468 ["INT_ADD", "register:40f0:8", ["const:b81468:8", "const:4:8"]]
+ 00b81468 ["CALL", null, ["callee:00c5d5d0:8"]]
- 00b80474 bytes 63700394
+ 00b81468 bytes 5a700394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53c6a1d586ced266f5d0ecf753383da7"></a>

### [`00b80e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80e68.md) → [`00b81e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81e5c.md) _ZN11flatbuffers6Parser19ParseEnumFromStringERKNS_4TypeEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c760.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d730.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 5件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b81eb8",
      "incomplete_value": true,
      "site": "00b81ee4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
      "definition_site": "00b80ec4",
      "incomplete_value": true,
      "site": "00b80ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b820c0",
      "incomplete_value": true,
      "site": "00b820d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:696:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b810cc",
      "incomplete_value": true,
      "site": "00b810dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:64c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b820c0",
      "incomplete_value": true,
      "site": "00b820d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b810cc",
      "incomplete_value": true,
      "site": "00b810dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b81eb8",
      "READ",
      [
        "storage",
        "002c3240",
        null,
        null
      ]
    ],
    [
      "00b81fcc",
      "PARAM",
      [
        "storage",
        "002ae24e",
        null,
        "string"
      ]
    ],
    [
      "00b81fe0",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b81eb8",
      "READ",
      [
        "storage",
        "002c3290",
        null,
        null
      ]
    ],
    [
      "00b81fcc",
      "PARAM",
      [
        "storage",
        "002ae31b",
        null,
        "string"
      ]
    ],
    [
      "00b81fe0",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80e68.md#insn-00b80fdc) · [`00b81154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80e68.md#insn-00b81154) · [`00b81168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b80/00b80e68.md#insn-00b81168)
- 新版 [`00b81fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81e5c.md#insn-00b81fd0) · [`00b82148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81e5c.md#insn-00b82148) · [`00b8215c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b81/00b81e5c.md#insn-00b8215c)

~~~diff
- 00b80fdc ["INT_ADD", "register:40f0:8", ["const:b80fdc:8", "const:4:8"]]
- 00b80fdc ["CALL", null, ["callee:00c59150:8"]]
+ 00b81fd0 ["INT_ADD", "register:40f0:8", ["const:b81fd0:8", "const:4:8"]]
+ 00b81fd0 ["CALL", null, ["callee:00c59150:8"]]
- 00b80fdc bytes 695c0394
+ 00b81fd0 bytes 605c0394
- 00b81154 ["INT_ADD", "register:40f0:8", ["const:b81154:8", "const:4:8"]]
- 00b81154 ["CALL", null, ["callee:00c59150:8"]]
+ 00b82148 ["INT_ADD", "register:40f0:8", ["const:b82148:8", "const:4:8"]]
+ 00b82148 ["CALL", null, ["callee:00c59150:8"]]
- 00b81154 bytes 0b5c0394
+ 00b82148 bytes 025c0394
- 00b81168 ["INT_ADD", "register:40f0:8", ["const:b81168:8", "const:4:8"]]
- 00b81168 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8215c ["INT_ADD", "register:40f0:8", ["const:b8215c:8", "const:4:8"]]
+ 00b8215c ["CALL", null, ["callee:00c59150:8"]]
- 00b81168 bytes 065c0394
+ 00b8215c bytes fd5b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2226b00774e4df91b1e290ac009cb43"></a>

### [`00b81308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81308.md) → [`00b822fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b822fc.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0f0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0c0.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.91% / 新版 87.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82358",
      "incomplete_value": true,
      "site": "00b8236c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81364",
      "incomplete_value": true,
      "site": "00b81378",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82350",
      "incomplete_value": true,
      "site": "00b82370",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8135c",
      "incomplete_value": true,
      "site": "00b8137c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b823e0",
      "incomplete_value": true,
      "site": "00b823ec",
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
      "definition_site": "00b813ec",
      "incomplete_value": true,
      "site": "00b813f8",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b82330",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b82334",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b8236c",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b82330",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b82334",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b8236c",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81308.md#insn-00b8132c) · [`00b81330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81308.md#insn-00b81330) · [`00b8133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81308.md#insn-00b8133c)
- 新版 [`00b82320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b822fc.md#insn-00b82320) · [`00b82324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b822fc.md#insn-00b82324) · [`00b82330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b822fc.md#insn-00b82330)

~~~diff
- 00b8132c ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b82320 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b8132c bytes da0800b0
+ 00b82320 bytes da0800b0
- 00b81330 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b82324 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b81330 bytes c80800d0
+ 00b82324 bytes c80800d0
- 00b8133c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b8133c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b82330 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b82330 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8133c bytes 5a7746f9
+ 00b82330 bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf76e9eb74641d23719222aafb3f1b9"></a>

### [`00b81474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81474.md) → [`00b82468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b82468.md) _ZN11flatbuffers11NumToStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c100.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`00c5d0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0d0.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59250.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.91% / 新版 87.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b824c4",
      "incomplete_value": true,
      "site": "00b824d8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b814d0",
      "incomplete_value": true,
      "site": "00b814e4",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b824bc",
      "incomplete_value": true,
      "site": "00b824dc",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b814c8",
      "incomplete_value": true,
      "site": "00b814e8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8254c",
      "incomplete_value": true,
      "site": "00b82558",
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
      "definition_site": "00b81558",
      "incomplete_value": true,
      "site": "00b81564",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8249c",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b824a0",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b824d8",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8249c",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b824a0",
      "READ",
      [
        "storage",
        "00c9c8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b824d8",
      "DATA",
      [
        "storage",
        "00c91c70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81474.md#insn-00b81498) · [`00b8149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81474.md#insn-00b8149c) · [`00b814a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81474.md#insn-00b814a8)
- 新版 [`00b8248c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b82468.md#insn-00b8248c) · [`00b82490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b82468.md#insn-00b82490) · [`00b8249c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b82468.md#insn-00b8249c)

~~~diff
- 00b81498 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00b8248c ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00b81498 bytes da0800b0
+ 00b8248c bytes da0800b0
- 00b8149c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00b82490 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00b8149c bytes c80800d0
+ 00b82490 bytes c80800d0
- 00b814a8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
- 00b814a8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b8249c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cb8:8"]]
+ 00b8249c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b814a8 bytes 5a7746f9
+ 00b8249c bytes 5a5f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d52b0b0ffb4cdf343837a68185772b9"></a>

### [`00b815e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b815e0.md) → [`00b825d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b825d4.md) _ZN11flatbuffers6Parser10TokenErrorEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c560.md) · 呼出先 10件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d530.md) · 呼出先 10件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b826a0",
      "incomplete_value": true,
      "site": "00b826a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b816ac",
      "incomplete_value": true,
      "site": "00b816b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b82744",
      "incomplete_value": false,
      "site": "00b82754",
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
            "const:6dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81750",
      "incomplete_value": false,
      "site": "00b81760",
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
            "const:605:8"
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
      "definition_site": "00b82778",
      "incomplete_value": false,
      "site": "00b82780",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81784",
      "incomplete_value": false,
      "site": "00b8178c",
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
            "const:b69:8"
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
      "00b82694",
      "DATA",
      [
        "storage",
        "00c90a28",
        null,
        "undefined *"
      ]
    ],
    [
      "00b82744",
      "PARAM",
      [
        "storage",
        "002b0605",
        null,
        "string"
      ]
    ],
    [
      "00b82778",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b82694",
      "DATA",
      [
        "storage",
        "00c919f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b82744",
      "PARAM",
      [
        "storage",
        "002b06dc",
        null,
        "string"
      ]
    ],
    [
      "00b82778",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b816b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b815e0.md#insn-00b816b0) · [`00b81760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b815e0.md#insn-00b81760) · [`00b8178c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b815e0.md#insn-00b8178c)
- 新版 [`00b826a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b825d4.md#insn-00b826a4) · [`00b82754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b825d4.md#insn-00b82754) · [`00b82780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b825d4.md#insn-00b82780)

~~~diff
- 00b816b0 ["INT_ADD", "register:40f0:8", ["const:b816b0:8", "const:4:8"]]
- 00b816b0 ["CALL", null, ["callee:00c59080:8"]]
+ 00b826a4 ["INT_ADD", "register:40f0:8", ["const:b826a4:8", "const:4:8"]]
+ 00b826a4 ["CALL", null, ["callee:00c59080:8"]]
- 00b816b0 bytes 805a0394
+ 00b826a4 bytes 775a0394
- 00b81760 ["INT_ADD", "register:40f0:8", ["const:b81760:8", "const:4:8"]]
- 00b81760 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b82754 ["INT_ADD", "register:40f0:8", ["const:b82754:8", "const:4:8"]]
+ 00b82754 ["CALL", null, ["callee:00c5a070:8"]]
- 00b81760 bytes 505e0394
+ 00b82754 bytes 475e0394
- 00b8178c ["INT_ADD", "register:40f0:8", ["const:b8178c:8", "const:4:8"]]
- 00b8178c ["CALL", null, ["callee:00c59150:8"]]
+ 00b82780 ["INT_ADD", "register:40f0:8", ["const:b82780:8", "const:4:8"]]
+ 00b82780 ["CALL", null, ["callee:00c59150:8"]]
- 00b8178c bytes 7d5a0394
+ 00b82780 bytes 745a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4664edc3534b98ac7e08114c8e941fdd"></a>

### [`00b81808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81808.md) → [`00b827fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b827fc.md) _ZN11flatbuffers6Parser13ParseFunctionEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c610.md) · 呼出先 23件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00b7f1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7f/00b7f1e4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5d5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5e0.md) · 呼出先 23件 [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00b801d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b80/00b801d8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82e54",
      "incomplete_value": true,
      "site": "00b82e68",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81e60",
      "incomplete_value": true,
      "site": "00b81e74",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 79,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82e64",
      "incomplete_value": true,
      "site": "00b82e84",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81e70",
      "incomplete_value": true,
      "site": "00b81e90",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 82,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b82e6c",
      "incomplete_value": true,
      "site": "00b82e88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:6ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81e78",
      "incomplete_value": true,
      "site": "00b81e94",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:628:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b829a4",
      "PARAM",
      [
        "storage",
        "002b15ec",
        null,
        "string"
      ]
    ],
    [
      "00b829b8",
      "PARAM",
      [
        "storage",
        "002ae217",
        null,
        "string"
      ]
    ],
    [
      "00b829d4",
      "PARAM",
      [
        "storage",
        "002a72de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b829a4",
      "PARAM",
      [
        "storage",
        "002b16c3",
        null,
        "string"
      ]
    ],
    [
      "00b829b8",
      "PARAM",
      [
        "storage",
        "002ae2e4",
        null,
        "string"
      ]
    ],
    [
      "00b829d4",
      "PARAM",
      [
        "storage",
        "002a7436",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b819bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81808.md#insn-00b819bc) · [`00b819d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81808.md#insn-00b819d0) · [`00b819fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81808.md#insn-00b819fc)
- 新版 [`00b829b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b827fc.md#insn-00b829b0) · [`00b829c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b827fc.md#insn-00b829c4) · [`00b829f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b82/00b827fc.md#insn-00b829f0)

~~~diff
- 00b819bc ["INT_ADD", "register:40f0:8", ["const:b819bc:8", "const:4:8"]]
- 00b819bc ["CALL", null, ["callee:00b5bc44:8"]]
+ 00b829b0 ["INT_ADD", "register:40f0:8", ["const:b829b0:8", "const:4:8"]]
+ 00b829b0 ["CALL", null, ["callee:00b5bc44:8"]]
- 00b819bc bytes a564ff97
+ 00b829b0 bytes a564ff97
- 00b819d0 ["INT_ADD", "register:40f0:8", ["const:b819d0:8", "const:4:8"]]
- 00b819d0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b829c4 ["INT_ADD", "register:40f0:8", ["const:b829c4:8", "const:4:8"]]
+ 00b829c4 ["CALL", null, ["callee:00c59020:8"]]
- 00b819d0 bytes a0590394
+ 00b829c4 bytes 97590394
- 00b819fc ["INT_ADD", "register:40f0:8", ["const:b819fc:8", "const:4:8"]]
- 00b819fc ["CALL", null, ["callee:00c59020:8"]]
+ 00b829f0 ["INT_ADD", "register:40f0:8", ["const:b829f0:8", "const:4:8"]]
+ 00b829f0 ["CALL", null, ["callee:00c59020:8"]]
- 00b819fc bytes 95590394
+ 00b829f0 bytes 8c590394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4db519abb3a690f55f70f3b21854fe7e"></a>

### [`00b821f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b821f0.md) → [`00b831e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b831e4.md) _ZN11flatbuffers6Parser13TryTypedValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEibRNS_5ValueENS_8BaseTypeEPb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c640.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5d610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d610.md) · 呼出先 11件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b83284",
      "incomplete_value": true,
      "site": "00b8329c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82290",
      "incomplete_value": true,
      "site": "00b822a8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b83288",
      "incomplete_value": true,
      "site": "00b832a0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82294",
      "incomplete_value": true,
      "site": "00b822ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8328c",
      "incomplete_value": true,
      "site": "00b832a4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:818:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b82298",
      "incomplete_value": true,
      "site": "00b822b0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:73a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b83284",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ],
    [
      "00b83288",
      "READ",
      [
        "storage",
        "002b4744",
        null,
        "string"
      ]
    ],
    [
      "00b8328c",
      "READ",
      [
        "storage",
        "002b473a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b83284",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ],
    [
      "00b83288",
      "READ",
      [
        "storage",
        "002b4822",
        null,
        "string"
      ]
    ],
    [
      "00b8328c",
      "READ",
      [
        "storage",
        "002b4818",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b821f0.md#insn-00b82344) · [`00b823b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b821f0.md#insn-00b823b8) · [`00b82578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b821f0.md#insn-00b82578)
- 新版 [`00b83338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b831e4.md#insn-00b83338) · [`00b833ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b831e4.md#insn-00b833ac) · [`00b8356c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b831e4.md#insn-00b8356c)

~~~diff
- 00b82344 ["INT_ADD", "register:40f0:8", ["const:b82344:8", "const:4:8"]]
- 00b82344 ["CALL", null, ["callee:00c59020:8"]]
+ 00b83338 ["INT_ADD", "register:40f0:8", ["const:b83338:8", "const:4:8"]]
+ 00b83338 ["CALL", null, ["callee:00c59020:8"]]
- 00b82344 bytes 43570394
+ 00b83338 bytes 3a570394
- 00b823b8 ["INT_ADD", "register:40f0:8", ["const:b823b8:8", "const:4:8"]]
- 00b823b8 ["CALL", null, ["callee:00c59020:8"]]
+ 00b833ac ["INT_ADD", "register:40f0:8", ["const:b833ac:8", "const:4:8"]]
+ 00b833ac ["CALL", null, ["callee:00c59020:8"]]
- 00b823b8 bytes 26570394
+ 00b833ac bytes 1d570394
- 00b82578 ["INT_ADD", "register:40f0:8", ["const:b82578:8", "const:4:8"]]
- 00b82578 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8356c ["INT_ADD", "register:40f0:8", ["const:b8356c:8", "const:4:8"]]
+ 00b8356c ["CALL", null, ["callee:00c59150:8"]]
- 00b82578 bytes 02570394
+ 00b8356c bytes f9560394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82947ceba0e3534969128086c8157ce8"></a>

### [`00b82d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82d54.md) → [`00b83d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83d48.md) _ZN11flatbuffers6Parser9ParseEnumEbPPNS_7EnumDefEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c870.md) · 呼出先 36件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00bac038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac038.md) [`00bad494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad494.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d840.md) · 呼出先 36件 [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00bad02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad02c.md) [`00bae488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae488.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 33件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b842bc",
      "incomplete_value": true,
      "site": "00b842d0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:800:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b832c8",
      "incomplete_value": true,
      "site": "00b832dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b842cc",
      "incomplete_value": true,
      "site": "00b842dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b832d8",
      "incomplete_value": true,
      "site": "00b832e8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 85,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b842cc",
      "incomplete_value": true,
      "site": "00b842e4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b832d8",
      "incomplete_value": true,
      "site": "00b832f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 87,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b84190",
      "READ",
      [
        "storage",
        "002a84f9",
        null,
        "string"
      ]
    ],
    [
      "00b84218",
      "READ",
      [
        "storage",
        "002c2a00",
        null,
        null
      ]
    ],
    [
      "00b8421c",
      "READ",
      [
        "storage",
        "002bd2e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b84190",
      "READ",
      [
        "storage",
        "002a8651",
        null,
        "string"
      ]
    ],
    [
      "00b84218",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ],
    [
      "00b8421c",
      "READ",
      [
        "storage",
        "002bd3bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82d54.md#insn-00b84334) · [`00b82ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82d54.md#insn-00b82ddc) · [`00b82e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82d54.md#insn-00b82e08)
- 新版 [`00b85328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83d48.md#insn-00b85328) · [`00b83dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83d48.md#insn-00b83dd0) · [`00b83dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b83/00b83d48.md#insn-00b83dfc)

~~~diff
- 00b84334 ["INT_ADD", "register:40f0:8", ["const:b84334:8", "const:4:8"]]
- 00b84334 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b85328 ["INT_ADD", "register:40f0:8", ["const:b85328:8", "const:4:8"]]
+ 00b85328 ["CALL", null, ["callee:00c58f50:8"]]
- 00b84334 bytes 134f0394
+ 00b85328 bytes 0a4f0394
- 00b82ddc ["INT_ADD", "register:40f0:8", ["const:b82ddc:8", "const:4:8"]]
- 00b82ddc ["CALL", null, ["callee:00c58f30:8"]]
+ 00b83dd0 ["INT_ADD", "register:40f0:8", ["const:b83dd0:8", "const:4:8"]]
+ 00b83dd0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b82ddc bytes 61540394
+ 00b83dd0 bytes 58540394
- 00b82e08 ["INT_ADD", "register:40f0:8", ["const:b82e08:8", "const:4:8"]]
- 00b82e08 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b83dfc ["INT_ADD", "register:40f0:8", ["const:b83dfc:8", "const:4:8"]]
+ 00b83dfc ["CALL", null, ["callee:00c5c650:8"]]
- 00b82e08 bytes 1e620394
+ 00b83dfc bytes 15620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02590e85a703cee47f1b789ec578ccab"></a>

### [`00b843b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b843b0.md) → [`00b853a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b853a4.md) _ZN11flatbuffers6Parser9StartEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbPPNS_7EnumDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8b0.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d880.md) · 呼出先 9件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b85400",
      "incomplete_value": true,
      "site": "00b85434",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8440c",
      "incomplete_value": true,
      "site": "00b84440",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b854f4",
      "incomplete_value": false,
      "site": "00b85500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:342:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84500",
      "incomplete_value": false,
      "site": "00b8450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:275:8"
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
      "definition_site": "00b85508",
      "incomplete_value": false,
      "site": "00b85514",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84514",
      "incomplete_value": false,
      "site": "00b84520",
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
            "const:b69:8"
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
      "00b85400",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b854f4",
      "PARAM",
      [
        "storage",
        "002ad275",
        null,
        "string"
      ]
    ],
    [
      "00b85508",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b85400",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b854f4",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ],
    [
      "00b85508",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b843b0.md#insn-00b8450c) · [`00b84520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b843b0.md#insn-00b84520) · [`00b843f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b843b0.md#insn-00b843f0)
- 新版 [`00b85500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b853a4.md#insn-00b85500) · [`00b85514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b853a4.md#insn-00b85514) · [`00b853e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b853a4.md#insn-00b853e4)

~~~diff
- 00b8450c ["INT_ADD", "register:40f0:8", ["const:b8450c:8", "const:4:8"]]
- 00b8450c ["CALL", null, ["callee:00c59150:8"]]
+ 00b85500 ["INT_ADD", "register:40f0:8", ["const:b85500:8", "const:4:8"]]
+ 00b85500 ["CALL", null, ["callee:00c59150:8"]]
- 00b8450c bytes 1d4f0394
+ 00b85500 bytes 144f0394
- 00b84520 ["INT_ADD", "register:40f0:8", ["const:b84520:8", "const:4:8"]]
- 00b84520 ["CALL", null, ["callee:00c59150:8"]]
+ 00b85514 ["INT_ADD", "register:40f0:8", ["const:b85514:8", "const:4:8"]]
+ 00b85514 ["CALL", null, ["callee:00c59150:8"]]
- 00b84520 bytes 184f0394
+ 00b85514 bytes 0f4f0394
- 00b843f0 ["INT_ADD", "register:40f0:8", ["const:b843f0:8", "const:4:8"]]
- 00b843f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b853e4 ["INT_ADD", "register:40f0:8", ["const:b853e4:8", "const:4:8"]]
+ 00b853e4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b843f0 bytes dc4e0394
+ 00b853e4 bytes d34e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d08941359599c782a88e20c9e275e5f"></a>

### [`00b846d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b846d0.md) → [`00b856c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b856c4.md) _ZN11flatbuffers14EnumValBuilder21AssignEnumeratorValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c260.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c280.md)
- 新版 呼出元 1件 [`00c5d230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d230.md) · 呼出先 7件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b857c8",
      "incomplete_value": false,
      "site": "00b857d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b847d4",
      "incomplete_value": false,
      "site": "00b847e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b857dc",
      "incomplete_value": false,
      "site": "00b857ec",
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
            "const:f9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b847e8",
      "incomplete_value": false,
      "site": "00b847f8",
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
            "const:ecd:8"
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
      "definition_site": "00b85810",
      "incomplete_value": false,
      "site": "00b85818",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8481c",
      "incomplete_value": false,
      "site": "00b84824",
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
            "const:b69:8"
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
      "00b857c8",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b857dc",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00b85810",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b857c8",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b857dc",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ],
    [
      "00b85810",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b847e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b846d0.md#insn-00b847e0) · [`00b847f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b846d0.md#insn-00b847f8) · [`00b84824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b846d0.md#insn-00b84824)
- 新版 [`00b857d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b856c4.md#insn-00b857d4) · [`00b857ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b856c4.md#insn-00b857ec) · [`00b85818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b856c4.md#insn-00b85818)

~~~diff
- 00b847e0 ["INT_ADD", "register:40f0:8", ["const:b847e0:8", "const:4:8"]]
- 00b847e0 ["CALL", null, ["callee:00c59150:8"]]
+ 00b857d4 ["INT_ADD", "register:40f0:8", ["const:b857d4:8", "const:4:8"]]
+ 00b857d4 ["CALL", null, ["callee:00c59150:8"]]
- 00b847e0 bytes 684e0394
+ 00b857d4 bytes 5f4e0394
- 00b847f8 ["INT_ADD", "register:40f0:8", ["const:b847f8:8", "const:4:8"]]
- 00b847f8 ["CALL", null, ["callee:00c59020:8"]]
+ 00b857ec ["INT_ADD", "register:40f0:8", ["const:b857ec:8", "const:4:8"]]
+ 00b857ec ["CALL", null, ["callee:00c59020:8"]]
- 00b847f8 bytes 164e0394
+ 00b857ec bytes 0d4e0394
- 00b84824 ["INT_ADD", "register:40f0:8", ["const:b84824:8", "const:4:8"]]
- 00b84824 ["CALL", null, ["callee:00c59150:8"]]
+ 00b85818 ["INT_ADD", "register:40f0:8", ["const:b85818:8", "const:4:8"]]
+ 00b85818 ["CALL", null, ["callee:00c59150:8"]]
- 00b84824 bytes 574e0394
+ 00b85818 bytes 4e4e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d432106d044845c7686bc0c8dc6f35"></a>

### [`00b84a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84a5c.md) → [`00b85a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85a50.md) _ZN11flatbuffers6Parser11StartStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPPNS_9StructDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5d0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5a0.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b85b84",
      "incomplete_value": true,
      "site": "00b85b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:afb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84b90",
      "incomplete_value": true,
      "site": "00b84ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:abb:8"
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
      "definition_site": "00b85bb8",
      "incomplete_value": false,
      "site": "00b85bc0",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84bc4",
      "incomplete_value": false,
      "site": "00b84bcc",
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
            "const:b69:8"
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
      "00b85b84",
      "PARAM",
      [
        "storage",
        "0029fabb",
        null,
        "string"
      ]
    ],
    [
      "00b85bb8",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b85b84",
      "PARAM",
      [
        "storage",
        "0029fafb",
        null,
        "string"
      ]
    ],
    [
      "00b85bb8",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84a5c.md#insn-00b84ba0) · [`00b84bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84a5c.md#insn-00b84bcc) · [`00b84a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84a5c.md#insn-00b84a98)
- 新版 [`00b85b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85a50.md#insn-00b85b94) · [`00b85bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85a50.md#insn-00b85bc0) · [`00b85a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85a50.md#insn-00b85a8c)

~~~diff
- 00b84ba0 ["INT_ADD", "register:40f0:8", ["const:b84ba0:8", "const:4:8"]]
- 00b84ba0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b85b94 ["INT_ADD", "register:40f0:8", ["const:b85b94:8", "const:4:8"]]
+ 00b85b94 ["CALL", null, ["callee:00c5a070:8"]]
- 00b84ba0 bytes 40510394
+ 00b85b94 bytes 37510394
- 00b84bcc ["INT_ADD", "register:40f0:8", ["const:b84bcc:8", "const:4:8"]]
- 00b84bcc ["CALL", null, ["callee:00c59150:8"]]
+ 00b85bc0 ["INT_ADD", "register:40f0:8", ["const:b85bc0:8", "const:4:8"]]
+ 00b85bc0 ["CALL", null, ["callee:00c59150:8"]]
- 00b84bcc bytes 6d4d0394
+ 00b85bc0 bytes 644d0394
- 00b84a98 ["INT_ADD", "register:40f0:8", ["const:b84a98:8", "const:4:8"]]
- 00b84a98 ["CALL", null, ["callee:00c5d700:8"]]
+ 00b85a8c ["INT_ADD", "register:40f0:8", ["const:b85a8c:8", "const:4:8"]]
+ 00b85a8c ["CALL", null, ["callee:00c5d700:8"]]
- 00b84a98 bytes 265f0394
+ 00b85a8c bytes 1d5f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f087eb75573fbdb7a97ceebae7cf154e"></a>

### [`00b84c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84c54.md) → [`00b85c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85c48.md) _ZN11flatbuffers6Parser10CheckClashERNSt6__ndk16vectorIPNS_8FieldDefENS1_9allocatorIS4_EEEEPNS_9StructDefEPKcNS_8BaseTypeE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c510.md) · 呼出先 10件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5d4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d4e0.md) · 呼出先 10件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b85e14",
      "incomplete_value": false,
      "site": "00b85e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ba2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84e20",
      "incomplete_value": false,
      "site": "00b84e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b58:8"
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
      "definition_site": "00b85e28",
      "incomplete_value": false,
      "site": "00b85e34",
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
            "const:a45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84e34",
      "incomplete_value": false,
      "site": "00b84e40",
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
            "const:967:8"
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
      "definition_site": "00b85e90",
      "incomplete_value": false,
      "site": "00b85e98",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b84e9c",
      "incomplete_value": false,
      "site": "00b84ea4",
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
            "const:b69:8"
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
      "00b85e14",
      "PARAM",
      [
        "storage",
        "002c0b58",
        null,
        "string"
      ]
    ],
    [
      "00b85e28",
      "PARAM",
      [
        "storage",
        "002bf967",
        null,
        "string"
      ]
    ],
    [
      "00b85e90",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b85e14",
      "PARAM",
      [
        "storage",
        "002c0ba2",
        null,
        "string"
      ]
    ],
    [
      "00b85e28",
      "PARAM",
      [
        "storage",
        "002bfa45",
        null,
        "string"
      ]
    ],
    [
      "00b85e90",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84c54.md#insn-00b84e2c) · [`00b84e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84c54.md#insn-00b84e40) · [`00b84ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b84c54.md#insn-00b84ea4)
- 新版 [`00b85e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85c48.md#insn-00b85e20) · [`00b85e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85c48.md#insn-00b85e34) · [`00b85e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b85/00b85c48.md#insn-00b85e98)

~~~diff
- 00b84e2c ["INT_ADD", "register:40f0:8", ["const:b84e2c:8", "const:4:8"]]
- 00b84e2c ["CALL", null, ["callee:00c59150:8"]]
+ 00b85e20 ["INT_ADD", "register:40f0:8", ["const:b85e20:8", "const:4:8"]]
+ 00b85e20 ["CALL", null, ["callee:00c59150:8"]]
- 00b84e2c bytes d54c0394
+ 00b85e20 bytes cc4c0394
- 00b84e40 ["INT_ADD", "register:40f0:8", ["const:b84e40:8", "const:4:8"]]
- 00b84e40 ["CALL", null, ["callee:00c59020:8"]]
+ 00b85e34 ["INT_ADD", "register:40f0:8", ["const:b85e34:8", "const:4:8"]]
+ 00b85e34 ["CALL", null, ["callee:00c59020:8"]]
- 00b84e40 bytes 844c0394
+ 00b85e34 bytes 7b4c0394
- 00b84ea4 ["INT_ADD", "register:40f0:8", ["const:b84ea4:8", "const:4:8"]]
- 00b84ea4 ["CALL", null, ["callee:00c59150:8"]]
+ 00b85e98 ["INT_ADD", "register:40f0:8", ["const:b85e98:8", "const:4:8"]]
+ 00b85e98 ["CALL", null, ["callee:00c59150:8"]]
- 00b84ea4 bytes b74c0394
+ 00b85e98 bytes ae4c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df7100c2e871f2e9133bd68aa39054e4"></a>

### [`00b854d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md) → [`00b864cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b864cc.md) _ZN11flatbuffers6Parser9ParseDeclEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c860.md) · 呼出先 30件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b86348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86348.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d830.md) · 呼出先 30件 [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b8733c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b8733c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.48% / 新版 94.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 16件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b865f8",
      "incomplete_value": true,
      "site": "00b86628",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:724:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85604",
      "incomplete_value": true,
      "site": "00b85634",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:6da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b86a0c",
      "incomplete_value": true,
      "site": "00b86a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:66f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85a18",
      "incomplete_value": true,
      "site": "00b85a18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:598:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b86a10",
      "incomplete_value": true,
      "site": "00b86a10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b85a1c",
      "incomplete_value": true,
      "site": "00b85a1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b865b4",
      "PARAM",
      [
        "storage",
        "002c1c5e",
        null,
        "string"
      ]
    ],
    [
      "00b865dc",
      "PARAM",
      [
        "storage",
        "002b6def",
        null,
        "string"
      ]
    ],
    [
      "00b865f8",
      "READ",
      [
        "storage",
        "002b26da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b865b4",
      "PARAM",
      [
        "storage",
        "002c1ca8",
        null,
        "string"
      ]
    ],
    [
      "00b865dc",
      "PARAM",
      [
        "storage",
        "002b6ebe",
        null,
        "string"
      ]
    ],
    [
      "00b865f8",
      "READ",
      [
        "storage",
        "002b2724",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8563c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md#insn-00b8563c) · [`00b85bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md#insn-00b85bd4) · [`00b85c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b854d8.md#insn-00b85c04)
- 新版 [`00b86630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b864cc.md#insn-00b86630) · [`00b86bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b864cc.md#insn-00b86bc8) · [`00b86bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b86/00b864cc.md#insn-00b86bf8)

~~~diff
- 00b8563c ["INT_ADD", "register:40f0:8", ["const:b8563c:8", "const:4:8"]]
- 00b8563c ["CALL", null, ["callee:00c59150:8"]]
+ 00b86630 ["INT_ADD", "register:40f0:8", ["const:b86630:8", "const:4:8"]]
+ 00b86630 ["CALL", null, ["callee:00c59150:8"]]
- 00b8563c bytes d14a0394
+ 00b86630 bytes c84a0394
- 00b85bd4 ["INT_ADD", "register:40f0:8", ["const:b85bd4:8", "const:4:8"]]
- 00b85bd4 ["CALL", null, ["callee:00c5d4e0:8"]]
+ 00b86bc8 ["INT_ADD", "register:40f0:8", ["const:b86bc8:8", "const:4:8"]]
+ 00b86bc8 ["CALL", null, ["callee:00c5d4e0:8"]]
- 00b85bd4 bytes 4f5a0394
+ 00b86bc8 bytes 465a0394
- 00b85c04 ["INT_ADD", "register:40f0:8", ["const:b85c04:8", "const:4:8"]]
- 00b85c04 ["CALL", null, ["callee:00c5d4e0:8"]]
+ 00b86bf8 ["INT_ADD", "register:40f0:8", ["const:b86bf8:8", "const:4:8"]]
+ 00b86bf8 ["CALL", null, ["callee:00c5d4e0:8"]]
- 00b85c04 bytes 435a0394
+ 00b86bf8 bytes 3a5a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d43af324b68996b2cb95dd0a20b31eea"></a>

### [`00b86480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86480.md) → [`00b87474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87474.md) _ZN11flatbuffers6Parser12ParseServiceEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5e0.md) · 呼出先 21件 [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5d5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d5b0.md) · 呼出先 21件 [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b87a34",
      "incomplete_value": true,
      "site": "00b87a44",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c3000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86a40",
      "incomplete_value": true,
      "site": "00b86a50",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b87c6c",
      "incomplete_value": true,
      "site": "00b87c7c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86c78",
      "incomplete_value": true,
      "site": "00b86c88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 119,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b87c6c",
      "incomplete_value": true,
      "site": "00b87c7c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b86c78",
      "incomplete_value": true,
      "site": "00b86c88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 120,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b876b0",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b87990",
      "PARAM",
      [
        "storage",
        "002af45c",
        null,
        "string"
      ]
    ],
    [
      "00b879a4",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b876b0",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b87990",
      "PARAM",
      [
        "storage",
        "002af533",
        null,
        "string"
      ]
    ],
    [
      "00b879a4",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b869bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86480.md#insn-00b869bc) · [`00b86ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86480.md#insn-00b86ca8) · [`00b86e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b86/00b86480.md#insn-00b86e08)
- 新版 [`00b879b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87474.md#insn-00b879b0) · [`00b87c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87474.md#insn-00b87c9c) · [`00b87dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b87/00b87474.md#insn-00b87dfc)

~~~diff
- 00b869bc ["INT_ADD", "register:40f0:8", ["const:b869bc:8", "const:4:8"]]
- 00b869bc ["CALL", null, ["callee:00c59150:8"]]
+ 00b879b0 ["INT_ADD", "register:40f0:8", ["const:b879b0:8", "const:4:8"]]
+ 00b879b0 ["CALL", null, ["callee:00c59150:8"]]
- 00b869bc bytes f1450394
+ 00b879b0 bytes e8450394
- 00b86ca8 ["INT_ADD", "register:40f0:8", ["const:b86ca8:8", "const:4:8"]]
- 00b86ca8 ["CALL", null, ["callee:00c59150:8"]]
+ 00b87c9c ["INT_ADD", "register:40f0:8", ["const:b87c9c:8", "const:4:8"]]
+ 00b87c9c ["CALL", null, ["callee:00c59150:8"]]
- 00b86ca8 bytes 36450394
+ 00b87c9c bytes 2d450394
- 00b86e08 ["INT_ADD", "register:40f0:8", ["const:b86e08:8", "const:4:8"]]
- 00b86e08 ["CALL", null, ["callee:00c59150:8"]]
+ 00b87dfc ["INT_ADD", "register:40f0:8", ["const:b87dfc:8", "const:4:8"]]
+ 00b87dfc ["CALL", null, ["callee:00c59150:8"]]
- 00b86e08 bytes de440394
+ 00b87dfc bytes d5440394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48601e128e8f20cd0a35c34f54aa1df5"></a>

### [`00b87760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87760.md) → [`00b88754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88754.md) _ZN11flatbuffers6Parser14ParseProtoDeclEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c660.md) · 呼出先 25件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d630.md) · 呼出先 25件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.07% / 新版 98.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b88a94",
      "incomplete_value": true,
      "site": "00b88a98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b87aa0",
      "incomplete_value": true,
      "site": "00b87aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b88c54",
      "incomplete_value": false,
      "site": "00b88c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87c60",
      "incomplete_value": false,
      "site": "00b87c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:23b:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b88c88",
      "incomplete_value": false,
      "site": "00b88c90",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b87c94",
      "incomplete_value": false,
      "site": "00b87c9c",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b887c8",
      "PARAM",
      [
        "storage",
        "002b26ef",
        null,
        "string"
      ]
    ],
    [
      "00b887e8",
      "PARAM",
      [
        "storage",
        "002b3689",
        null,
        "string"
      ]
    ],
    [
      "00b88904",
      "PARAM",
      [
        "storage",
        "002b06d2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b887c8",
      "PARAM",
      [
        "storage",
        "002b2739",
        null,
        "string"
      ]
    ],
    [
      "00b887e8",
      "PARAM",
      [
        "storage",
        "002b36d3",
        null,
        "string"
      ]
    ],
    [
      "00b88904",
      "PARAM",
      [
        "storage",
        "002b07a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87760.md#insn-00b87aa4) · [`00b87c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87760.md#insn-00b87c70) · [`00b87c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87760.md#insn-00b87c9c)
- 新版 [`00b88a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88754.md#insn-00b88a98) · [`00b88c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88754.md#insn-00b88c64) · [`00b88c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b88/00b88754.md#insn-00b88c90)

~~~diff
- 00b87aa4 ["INT_ADD", "register:40f0:8", ["const:b87aa4:8", "const:4:8"]]
- 00b87aa4 ["CALL", null, ["callee:00c59080:8"]]
+ 00b88a98 ["INT_ADD", "register:40f0:8", ["const:b88a98:8", "const:4:8"]]
+ 00b88a98 ["CALL", null, ["callee:00c59080:8"]]
- 00b87aa4 bytes 83410394
+ 00b88a98 bytes 7a410394
- 00b87c70 ["INT_ADD", "register:40f0:8", ["const:b87c70:8", "const:4:8"]]
- 00b87c70 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b88c64 ["INT_ADD", "register:40f0:8", ["const:b88c64:8", "const:4:8"]]
+ 00b88c64 ["CALL", null, ["callee:00c5a070:8"]]
- 00b87c70 bytes 0c450394
+ 00b88c64 bytes 03450394
- 00b87c9c ["INT_ADD", "register:40f0:8", ["const:b87c9c:8", "const:4:8"]]
- 00b87c9c ["CALL", null, ["callee:00c59150:8"]]
+ 00b88c90 ["INT_ADD", "register:40f0:8", ["const:b88c90:8", "const:4:8"]]
+ 00b88c90 ["CALL", null, ["callee:00c59150:8"]]
- 00b87c9c bytes 39410394
+ 00b88c90 bytes 30410394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43337b6a23305484d5f08376cd19e6b6"></a>

### [`00b881e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md) → [`00b891d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md) _ZN11flatbuffers6Parser16ParseProtoFieldsEPNS_9StructDefEbb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b881e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md) [`00c5c6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6e0.md) · 呼出先 35件 [`00b881e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00b891d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md) [`00c5d6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d6b0.md) · 呼出先 35件 [`00b891d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8a988",
      "incomplete_value": true,
      "site": "00b8a99c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:8be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89994",
      "incomplete_value": true,
      "site": "00b899a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:7f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 260,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8a988",
      "incomplete_value": true,
      "site": "00b8a99c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89994",
      "incomplete_value": true,
      "site": "00b899a8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 261,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8a98c",
      "incomplete_value": true,
      "site": "00b8a9a0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b89998",
      "incomplete_value": true,
      "site": "00b899ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 262,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b892d4",
      "READ",
      [
        "storage",
        "002c43b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b892e4",
      "READ",
      [
        "storage",
        "002c3d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b892e8",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b892d4",
      "READ",
      [
        "storage",
        "002c4408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b892e4",
      "READ",
      [
        "storage",
        "002c3d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b892e8",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8840c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md#insn-00b8840c) · [`00b88524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md#insn-00b88524) · [`00b88544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b88/00b881e4.md#insn-00b88544)
- 新版 [`00b89400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md#insn-00b89400) · [`00b89518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md#insn-00b89518) · [`00b89538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b89/00b891d8.md#insn-00b89538)

~~~diff
- 00b8840c ["INT_ADD", "register:40f0:8", ["const:b8840c:8", "const:4:8"]]
- 00b8840c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b89400 ["INT_ADD", "register:40f0:8", ["const:b89400:8", "const:4:8"]]
+ 00b89400 ["CALL", null, ["callee:00c590f0:8"]]
- 00b8840c bytes 453f0394
+ 00b89400 bytes 3c3f0394
- 00b88524 ["INT_ADD", "register:40f0:8", ["const:b88524:8", "const:4:8"]]
- 00b88524 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b89518 ["INT_ADD", "register:40f0:8", ["const:b89518:8", "const:4:8"]]
+ 00b89518 ["CALL", null, ["callee:00c590f0:8"]]
- 00b88524 bytes ff3e0394
+ 00b89518 bytes f63e0394
- 00b88544 ["INT_ADD", "register:40f0:8", ["const:b88544:8", "const:4:8"]]
- 00b88544 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b89538 ["INT_ADD", "register:40f0:8", ["const:b89538:8", "const:4:8"]]
+ 00b89538 ["CALL", null, ["callee:00c590f0:8"]]
- 00b88544 bytes f73e0394
+ 00b89538 bytes ee3e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63a2b94536380ed0a732edac76303bc3"></a>

### [`00b89c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89c60.md) → [`00b8ac54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8ac54.md) _ZN11flatbuffers6Parser18ParseProtoMapFieldEPNS_9StructDefE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c740.md) · 呼出先 15件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d710.md) · 呼出先 15件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.39% / 新版 99.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8b01c",
      "incomplete_value": true,
      "site": "00b8b03c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a028",
      "incomplete_value": true,
      "site": "00b8a048",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
    "ordinal": 73,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8b090",
      "incomplete_value": true,
      "site": "00b8b098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:18a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a09c",
      "incomplete_value": true,
      "site": "00b8a0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:bb:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8aef4",
      "PARAM",
      [
        "storage",
        "002ac110",
        null,
        "string"
      ]
    ],
    [
      "00b8b01c",
      "READ",
      [
        "storage",
        "002c40a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8b090",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8aef4",
      "PARAM",
      [
        "storage",
        "002ac1dd",
        null,
        "string"
      ]
    ],
    [
      "00b8b01c",
      "READ",
      [
        "storage",
        "002c40f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b8b090",
      "PARAM",
      [
        "storage",
        "002b818a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89c60.md#insn-00b8a0a4) · [`00b89c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89c60.md#insn-00b89c9c) · [`00b89cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89c60.md#insn-00b89cbc)
- 新版 [`00b8b098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8ac54.md#insn-00b8b098) · [`00b8ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8ac54.md#insn-00b8ac90) · [`00b8acb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8a/00b8ac54.md#insn-00b8acb0)

~~~diff
- 00b8a0a4 ["INT_ADD", "register:40f0:8", ["const:b8a0a4:8", "const:4:8"]]
- 00b8a0a4 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b8b098 ["INT_ADD", "register:40f0:8", ["const:b8b098:8", "const:4:8"]]
+ 00b8b098 ["CALL", null, ["callee:00c5c660:8"]]
- 00b8a0a4 bytes 7b450394
+ 00b8b098 bytes 72450394
- 00b89c9c ["INT_ADD", "register:40f0:8", ["const:b89c9c:8", "const:4:8"]]
- 00b89c9c ["CALL", null, ["callee:00c5d790:8"]]
+ 00b8ac90 ["INT_ADD", "register:40f0:8", ["const:b8ac90:8", "const:4:8"]]
+ 00b8ac90 ["CALL", null, ["callee:00c5d790:8"]]
- 00b89c9c bytes c94a0394
+ 00b8ac90 bytes c04a0394
- 00b89cbc ["INT_ADD", "register:40f0:8", ["const:b89cbc:8", "const:4:8"]]
- 00b89cbc ["CALL", null, ["callee:00c5d7f0:8"]]
+ 00b8acb0 ["INT_ADD", "register:40f0:8", ["const:b8acb0:8", "const:4:8"]]
+ 00b8acb0 ["CALL", null, ["callee:00c5d7f0:8"]]
- 00b89cbc bytes d94a0394
+ 00b8acb0 bytes d04a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d652330b4d5a1408c43545660ceb4e14"></a>

### [`00b8a39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a39c.md) → [`00b8b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b390.md) _ZN11flatbuffers14EnumValBuilder16AcceptEnumeratorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c250.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c150.md) [`00c5c240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c240.md)
- 新版 呼出元 1件 [`00c5d220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d220.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d120.md) [`00c5d210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d210.md)

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
      "definition_site": "00b8b41c",
      "incomplete_value": false,
      "site": "00b8b428",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a428",
      "incomplete_value": false,
      "site": "00b8a434",
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
            "const:b69:8"
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
      "00b8b408",
      "PARAM",
      [
        "storage",
        "002aa87f",
        null,
        "string"
      ]
    ],
    [
      "00b8b41c",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8b408",
      "PARAM",
      [
        "storage",
        "002aa94c",
        null,
        "string"
      ]
    ],
    [
      "00b8b41c",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a39c.md#insn-00b8a434) · [`00b8a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a39c.md#insn-00b8a3e0) · [`00b8a400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a39c.md#insn-00b8a400)
- 新版 [`00b8b428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b390.md#insn-00b8b428) · [`00b8b3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b390.md#insn-00b8b3d4) · [`00b8b3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b390.md#insn-00b8b3f4)

~~~diff
- 00b8a434 ["INT_ADD", "register:40f0:8", ["const:b8a434:8", "const:4:8"]]
- 00b8a434 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8b428 ["INT_ADD", "register:40f0:8", ["const:b8b428:8", "const:4:8"]]
+ 00b8b428 ["CALL", null, ["callee:00c59150:8"]]
- 00b8a434 bytes 53370394
+ 00b8b428 bytes 4a370394
- 00b8a3e0 ["INT_ADD", "register:40f0:8", ["const:b8a3e0:8", "const:4:8"]]
- 00b8a3e0 ["CALL", null, ["callee:00c5d210:8"]]
+ 00b8b3d4 ["INT_ADD", "register:40f0:8", ["const:b8b3d4:8", "const:4:8"]]
+ 00b8b3d4 ["CALL", null, ["callee:00c5d210:8"]]
- 00b8a3e0 bytes 98470394
+ 00b8b3d4 bytes 8f470394
- 00b8a400 ["INT_ADD", "register:40f0:8", ["const:b8a400:8", "const:4:8"]]
- 00b8a400 ["CALL", null, ["callee:00c5d120:8"]]
+ 00b8b3f4 ["INT_ADD", "register:40f0:8", ["const:b8b3f4:8", "const:4:8"]]
+ 00b8b3f4 ["CALL", null, ["callee:00c5d120:8"]]
- 00b8a400 bytes 54470394
+ 00b8b3f4 bytes 4b470394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe51560666671b047563a1eeeabf2b6"></a>

### [`00b8a49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a49c.md) → [`00b8b490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b490.md) _ZN11flatbuffers6Parser30ParseFlexBufferNumericConstantEPN11flexbuffers7BuilderE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7b0.md) · 呼出先 6件 [`00b99988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00c5d780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d780.md) · 呼出先 6件 [`00b9a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c59660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59660.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8b500",
      "incomplete_value": false,
      "site": "00b8b50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:833:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a50c",
      "incomplete_value": false,
      "site": "00b8a518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:755:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8b514",
      "incomplete_value": false,
      "site": "00b8b520",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8a520",
      "incomplete_value": false,
      "site": "00b8a52c",
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
            "const:b69:8"
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
      "00b8b500",
      "PARAM",
      [
        "storage",
        "002b4755",
        null,
        "string"
      ]
    ],
    [
      "00b8b514",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8b500",
      "PARAM",
      [
        "storage",
        "002b4833",
        null,
        "string"
      ]
    ],
    [
      "00b8b514",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a49c.md#insn-00b8a518) · [`00b8a52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a49c.md#insn-00b8a52c) · [`00b8a4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a49c.md#insn-00b8a4f0)
- 新版 [`00b8b50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b490.md#insn-00b8b50c) · [`00b8b520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b490.md#insn-00b8b520) · [`00b8b4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b490.md#insn-00b8b4e4)

~~~diff
- 00b8a518 ["INT_ADD", "register:40f0:8", ["const:b8a518:8", "const:4:8"]]
- 00b8a518 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8b50c ["INT_ADD", "register:40f0:8", ["const:b8b50c:8", "const:4:8"]]
+ 00b8b50c ["CALL", null, ["callee:00c59150:8"]]
- 00b8a518 bytes 1a370394
+ 00b8b50c bytes 11370394
- 00b8a52c ["INT_ADD", "register:40f0:8", ["const:b8a52c:8", "const:4:8"]]
- 00b8a52c ["CALL", null, ["callee:00c59150:8"]]
+ 00b8b520 ["INT_ADD", "register:40f0:8", ["const:b8b520:8", "const:4:8"]]
+ 00b8b520 ["CALL", null, ["callee:00c59150:8"]]
- 00b8a52c bytes 15370394
+ 00b8b520 bytes 0c370394
- 00b8a4f0 ["INT_ADD", "register:40f0:8", ["const:b8a4f0:8", "const:4:8"]]
- 00b8a4f0 ["CALL", null, ["callee:00c59660:8"]]
+ 00b8b4e4 ["INT_ADD", "register:40f0:8", ["const:b8b4e4:8", "const:4:8"]]
+ 00b8b4e4 ["CALL", null, ["callee:00c59660:8"]]
- 00b8a4f0 bytes 68380394
+ 00b8b4e4 bytes 5f380394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2234795627902355abec15b2f9ec623b"></a>

### [`00b8a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md) → [`00b8b5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md) _ZN11flatbuffers6Parser20ParseFlexBufferValueEPN11flexbuffers7BuilderE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md) [`00c5c770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c770.md) · 呼出先 22件 [`00b8a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md) [`00b99988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99988.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00b8b5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md) [`00c5d740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d740.md) · 呼出先 22件 [`00b8b5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md) [`00b9a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b9a/00b9a97c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.17% / 新版 96.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8baa8",
      "incomplete_value": true,
      "site": "00b8bab8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:6b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8aab4",
      "incomplete_value": true,
      "site": "00b8aac4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8baac",
      "incomplete_value": true,
      "site": "00b8babc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
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
    "old": {
      "definition_site": "00b8aab8",
      "incomplete_value": true,
      "site": "00b8aac8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8baac",
      "incomplete_value": true,
      "site": "00b8babc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8aab8",
      "incomplete_value": true,
      "site": "00b8aac8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8b6ac",
      "DATA",
      [
        "storage",
        "0030e1d4",
        "switchD_00b8a6c0::switchdataD_0030e1d4",
        "byte"
      ]
    ],
    [
      "00b8b9b0",
      "DATA",
      [
        "storage",
        "0030e1d8",
        "switchD_00b8a9c4::switchdataD_0030e1d8",
        "byte"
      ]
    ],
    [
      "00b8b9c8",
      "PARAM",
      [
        "storage",
        "002ad18d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8b6ac",
      "DATA",
      [
        "storage",
        "0030e214",
        "switchD_00b8b6b4::switchdataD_0030e214",
        "byte"
      ]
    ],
    [
      "00b8b9b0",
      "DATA",
      [
        "storage",
        "0030e218",
        "switchD_00b8b9b8::switchdataD_0030e218",
        "byte"
      ]
    ],
    [
      "00b8b9c8",
      "PARAM",
      [
        "storage",
        "002ad25a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8aadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md#insn-00b8aadc) · [`00b8abd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md#insn-00b8abd4) · [`00b8a628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a5d4.md#insn-00b8a628)
- 新版 [`00b8bad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md#insn-00b8bad0) · [`00b8bbc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md#insn-00b8bbc8) · [`00b8b61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8b/00b8b5c8.md#insn-00b8b61c)

~~~diff
- 00b8aadc ["INT_ADD", "register:40f0:8", ["const:b8aadc:8", "const:4:8"]]
- 00b8aadc ["CALL", null, ["callee:00c59150:8"]]
+ 00b8bad0 ["INT_ADD", "register:40f0:8", ["const:b8bad0:8", "const:4:8"]]
+ 00b8bad0 ["CALL", null, ["callee:00c59150:8"]]
- 00b8aadc bytes a9350394
+ 00b8bad0 bytes a0350394
- 00b8abd4 ["INT_ADD", "register:40f0:8", ["const:b8abd4:8", "const:4:8"]]
- 00b8abd4 ["CALL", null, ["callee:00c5e1f0:8"]]
+ 00b8bbc8 ["INT_ADD", "register:40f0:8", ["const:b8bbc8:8", "const:4:8"]]
+ 00b8bbc8 ["CALL", null, ["callee:00c5e1f0:8"]]
- 00b8abd4 bytes 93490394
+ 00b8bbc8 bytes 8a490394
- 00b8a628 ["INT_ADD", "register:40f0:8", ["const:b8a628:8", "const:4:8"]]
- 00b8a628 ["CALL", null, ["callee:00c5d5c0:8"]]
+ 00b8b61c ["INT_ADD", "register:40f0:8", ["const:b8b61c:8", "const:4:8"]]
+ 00b8b61c ["CALL", null, ["callee:00c5d5c0:8"]]
- 00b8a628 bytes f2470394
+ 00b8b61c bytes e9470394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-173b77d6cab7db263ee37d76a0d51cb8"></a>

### [`00b8b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b29c.md) → [`00b8c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c290.md) _ZN11flatbuffers6Parser14StartParseFileEPKcS2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d650.md) · 呼出先 8件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8c380",
      "incomplete_value": false,
      "site": "00b8c39c",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8b38c",
      "incomplete_value": false,
      "site": "00b8b3a8",
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
            "const:b69:8"
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
      "00b8c2cc",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8c364",
      "READ",
      [
        "storage",
        "002a60c1",
        null,
        "string"
      ]
    ],
    [
      "00b8c380",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8c2cc",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00b8c364",
      "READ",
      [
        "storage",
        "002a6219",
        null,
        "string"
      ]
    ],
    [
      "00b8c380",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b29c.md#insn-00b8b3a8) · [`00b8b2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b29c.md#insn-00b8b2c4) · [`00b8b2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b29c.md#insn-00b8b2e4)
- 新版 [`00b8c39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c290.md#insn-00b8c39c) · [`00b8c2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c290.md#insn-00b8c2b8) · [`00b8c2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c290.md#insn-00b8c2d8)

~~~diff
- 00b8b3a8 ["INT_ADD", "register:40f0:8", ["const:b8b3a8:8", "const:4:8"]]
- 00b8b3a8 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8c39c ["INT_ADD", "register:40f0:8", ["const:b8c39c:8", "const:4:8"]]
+ 00b8c39c ["CALL", null, ["callee:00c59150:8"]]
- 00b8b3a8 bytes 76330394
+ 00b8c39c bytes 6d330394
- 00b8b2c4 ["COPY", "tmp:0:8", ["const:38e:8"]]
- 00b8b2c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b8b2c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b8b2c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b8c2b8 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00b8c2b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b8c2b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b8c2b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b8b2c4 bytes 29390e91
+ 00b8c2b8 bytes 29991391
- 00b8b2e4 ["INT_ADD", "register:40f0:8", ["const:b8b2e4:8", "const:4:8"]]
- 00b8b2e4 ["CALL", null, ["callee:00c59080:8"]]
+ 00b8c2d8 ["INT_ADD", "register:40f0:8", ["const:b8c2d8:8", "const:4:8"]]
+ 00b8c2d8 ["CALL", null, ["callee:00c59080:8"]]
- 00b8b2e4 bytes 73330394
+ 00b8c2d8 bytes 6a330394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5154122370eedcaf909e1dad6d29db5c"></a>

### [`00b8b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b594.md) → [`00b8c588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c588.md) _ZN11flatbuffers6Parser9ParseRootEPKcPS2_S2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c890.md) · 呼出先 17件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d860.md) · 呼出先 17件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8c8e8",
      "incomplete_value": false,
      "site": "00b8c8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8b8f4",
      "incomplete_value": false,
      "site": "00b8b8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b5f:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8c8fc",
      "incomplete_value": false,
      "site": "00b8c908",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8b908",
      "incomplete_value": false,
      "site": "00b8b914",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8c918",
      "incomplete_value": false,
      "site": "00b8c924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8b924",
      "incomplete_value": false,
      "site": "00b8b930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8c8e8",
      "PARAM",
      [
        "storage",
        "002c0b5f",
        null,
        "string"
      ]
    ],
    [
      "00b8c8fc",
      "PARAM",
      [
        "storage",
        "002a85c8",
        null,
        "string"
      ]
    ],
    [
      "00b8c918",
      "PARAM",
      [
        "storage",
        "002bc001",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8c8e8",
      "PARAM",
      [
        "storage",
        "002c0ba9",
        null,
        "string"
      ]
    ],
    [
      "00b8c8fc",
      "PARAM",
      [
        "storage",
        "002a8720",
        null,
        "string"
      ]
    ],
    [
      "00b8c918",
      "PARAM",
      [
        "storage",
        "002bc0df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b594.md#insn-00b8b8fc) · [`00b8b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b594.md#insn-00b8b914) · [`00b8b930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b594.md#insn-00b8b930)
- 新版 [`00b8c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c588.md#insn-00b8c8f0) · [`00b8c908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c588.md#insn-00b8c908) · [`00b8c924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8c588.md#insn-00b8c924)

~~~diff
- 00b8b8fc ["INT_ADD", "register:40f0:8", ["const:b8b8fc:8", "const:4:8"]]
- 00b8b8fc ["CALL", null, ["callee:00c59150:8"]]
+ 00b8c8f0 ["INT_ADD", "register:40f0:8", ["const:b8c8f0:8", "const:4:8"]]
+ 00b8c8f0 ["CALL", null, ["callee:00c59150:8"]]
- 00b8b8fc bytes 21320394
+ 00b8c8f0 bytes 18320394
- 00b8b914 ["INT_ADD", "register:40f0:8", ["const:b8b914:8", "const:4:8"]]
- 00b8b914 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8c908 ["INT_ADD", "register:40f0:8", ["const:b8c908:8", "const:4:8"]]
+ 00b8c908 ["CALL", null, ["callee:00c59150:8"]]
- 00b8b914 bytes 1b320394
+ 00b8c908 bytes 12320394
- 00b8b930 ["INT_ADD", "register:40f0:8", ["const:b8b930:8", "const:4:8"]]
- 00b8b930 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8c924 ["INT_ADD", "register:40f0:8", ["const:b8c924:8", "const:4:8"]]
+ 00b8c924 ["CALL", null, ["callee:00c59150:8"]]
- 00b8b930 bytes 14320394
+ 00b8c924 bytes 0b320394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbad05e278a2be0971b9ff8669afd53f"></a>

### [`00b8bd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bd1c.md) → [`00b8cd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cd10.md) _ZN11flatbuffers6Parser11DoParseJsonEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c580.md) · 呼出先 8件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c400.md)
- 新版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d550.md) · 呼出先 8件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d3d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d3d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.78% / 新版 90.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8cd68",
      "incomplete_value": true,
      "site": "00b8cd78",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
      "definition_site": "00b8bd74",
      "incomplete_value": true,
      "site": "00b8bd84",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8cd6c",
      "incomplete_value": true,
      "site": "00b8cd7c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:37c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8bd78",
      "incomplete_value": true,
      "site": "00b8bd88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:2af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8cd6c",
      "incomplete_value": true,
      "site": "00b8cd7c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8bd78",
      "incomplete_value": true,
      "site": "00b8bd88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8cd68",
      "READ",
      [
        "storage",
        "002c2280",
        null,
        null
      ]
    ],
    [
      "00b8cd6c",
      "READ",
      [
        "storage",
        "002ad2af",
        null,
        "string"
      ]
    ],
    [
      "00b8cd6c",
      "READ",
      [
        "storage",
        "002ad2bf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8cd68",
      "READ",
      [
        "storage",
        "002c22d0",
        null,
        null
      ]
    ],
    [
      "00b8cd6c",
      "READ",
      [
        "storage",
        "002ad37c",
        null,
        "string"
      ]
    ],
    [
      "00b8cd6c",
      "READ",
      [
        "storage",
        "002ad38c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8be2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bd1c.md#insn-00b8be2c) · [`00b8bd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bd1c.md#insn-00b8bd64) · [`00b8bd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bd1c.md#insn-00b8bd70)
- 新版 [`00b8ce20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cd10.md#insn-00b8ce20) · [`00b8cd58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cd10.md#insn-00b8cd58) · [`00b8cd64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cd10.md#insn-00b8cd64)

~~~diff
- 00b8be2c ["INT_ADD", "register:40f0:8", ["const:b8be2c:8", "const:4:8"]]
- 00b8be2c ["CALL", null, ["callee:00c59150:8"]]
+ 00b8ce20 ["INT_ADD", "register:40f0:8", ["const:b8ce20:8", "const:4:8"]]
+ 00b8ce20 ["CALL", null, ["callee:00c59150:8"]]
- 00b8be2c bytes d5300394
+ 00b8ce20 bytes cc300394
- 00b8bd64 ["INT_ADD", "register:40f0:8", ["const:b8bd64:8", "const:4:8"]]
- 00b8bd64 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8cd58 ["INT_ADD", "register:40f0:8", ["const:b8cd58:8", "const:4:8"]]
+ 00b8cd58 ["CALL", null, ["callee:00c58f30:8"]]
- 00b8bd64 bytes 7f300394
+ 00b8cd58 bytes 76300394
- 00b8bd70 ["COPY", "tmp:0:8", ["const:2af:8"]]
- 00b8bd70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b8bd70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b8bd70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b8cd64 ["COPY", "tmp:0:8", ["const:37c:8"]]
+ 00b8cd64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b8cd64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b8cd64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b8bd70 bytes 29bd0a91
+ 00b8cd64 bytes 29f10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772a9ac60f3fb0a145101e42f8c9ca88"></a>

### [`00b8bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md) → [`00b8cf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md) _ZN11flatbuffers6Parser7DoParseEPKcPS2_S2_S2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b8bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md) [`00c5c830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c830.md) · 呼出先 39件 [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00b8bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md) [`00b8db54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8db54.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00b8cf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md) [`00c5d800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d800.md) · 呼出先 39件 [`006398ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/006398ac.md) [`00b8cf54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md) [`00b8eb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8eb48.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_value` 10件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8de24",
      "incomplete_value": true,
      "site": "00b8de58",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:820:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8ce30",
      "incomplete_value": true,
      "site": "00b8ce64",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 179,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8e464",
      "incomplete_value": true,
      "site": "00b8e474",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8d470",
      "incomplete_value": true,
      "site": "00b8d480",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 219,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8e468",
      "incomplete_value": true,
      "site": "00b8e478",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:b4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8d474",
      "incomplete_value": true,
      "site": "00b8d484",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:b0e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 220,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8d28c",
      "DATA",
      [
        "storage",
        "00ca4768",
        null,
        "pointer"
      ]
    ],
    [
      "00b8d420",
      "PARAM",
      [
        "storage",
        "002b3682",
        null,
        "string"
      ]
    ],
    [
      "00b8d440",
      "PARAM",
      [
        "storage",
        "002b6df5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8d28c",
      "DATA",
      [
        "storage",
        "00ca5738",
        null,
        "pointer"
      ]
    ],
    [
      "00b8d420",
      "PARAM",
      [
        "storage",
        "002b36cc",
        null,
        "string"
      ]
    ],
    [
      "00b8d440",
      "PARAM",
      [
        "storage",
        "002b6ec4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8c0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md#insn-00b8c0dc) · [`00b8c450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md#insn-00b8c450) · [`00b8c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bf60.md#insn-00b8c760)
- 新版 [`00b8d0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md#insn-00b8d0d0) · [`00b8d444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md#insn-00b8d444) · [`00b8d754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8c/00b8cf54.md#insn-00b8d754)

~~~diff
- 00b8c0dc ["INT_ADD", "register:40f0:8", ["const:b8c0dc:8", "const:4:8"]]
- 00b8c0dc ["CALL", null, ["callee:00c5c680:8"]]
+ 00b8d0d0 ["INT_ADD", "register:40f0:8", ["const:b8d0d0:8", "const:4:8"]]
+ 00b8d0d0 ["CALL", null, ["callee:00c5c680:8"]]
- 00b8c0dc bytes 753d0394
+ 00b8d0d0 bytes 6c3d0394
- 00b8c450 ["INT_ADD", "register:40f0:8", ["const:b8c450:8", "const:4:8"]]
- 00b8c450 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b8d444 ["INT_ADD", "register:40f0:8", ["const:b8d444:8", "const:4:8"]]
+ 00b8d444 ["CALL", null, ["callee:00c590f0:8"]]
- 00b8c450 bytes 342f0394
+ 00b8d444 bytes 2b2f0394
- 00b8c760 ["INT_ADD", "register:40f0:8", ["const:b8c760:8", "const:4:8"]]
- 00b8c760 ["CALL", null, ["callee:00c5d7a0:8"]]
+ 00b8d754 ["INT_ADD", "register:40f0:8", ["const:b8d754:8", "const:4:8"]]
+ 00b8d754 ["CALL", null, ["callee:00c5d7a0:8"]]
- 00b8c760 bytes 1c400394
+ 00b8d754 bytes 13400394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06daaf28a14919a187b03c8945d6dacd"></a>

### [`00b8d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d990.md) → [`00b8e984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e984.md) _ZN11flatbuffers6Parser26CheckPrivatelyLeakedFieldsERKNS_10DefinitionES3_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7a0.md) · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)
- 新版 呼出元 1件 [`00c5d770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d770.md) · 呼出先 6件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d810.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8ea7c",
      "incomplete_value": true,
      "site": "00b8ea8c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8da88",
      "incomplete_value": true,
      "site": "00b8da98",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8eab4",
      "incomplete_value": false,
      "site": "00b8eabc",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8dac0",
      "incomplete_value": false,
      "site": "00b8dac8",
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
            "const:b69:8"
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
      "00b8ea7c",
      "READ",
      [
        "storage",
        "002c2db0",
        null,
        null
      ]
    ],
    [
      "00b8ea88",
      "READ",
      [
        "storage",
        "002a2b62",
        null,
        "string"
      ]
    ],
    [
      "00b8ea88",
      "READ",
      [
        "storage",
        "002a2b72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b8ea7c",
      "READ",
      [
        "storage",
        "002c2e00",
        null,
        null
      ]
    ],
    [
      "00b8ea88",
      "READ",
      [
        "storage",
        "002a2c2d",
        null,
        "string"
      ]
    ],
    [
      "00b8ea88",
      "READ",
      [
        "storage",
        "002a2c3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8dac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d990.md#insn-00b8dac8) · [`00b8d9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d990.md#insn-00b8d9fc) · [`00b8da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d990.md#insn-00b8da1c)
- 新版 [`00b8eabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e984.md#insn-00b8eabc) · [`00b8e9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e984.md#insn-00b8e9f0) · [`00b8ea10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8e/00b8e984.md#insn-00b8ea10)

~~~diff
- 00b8dac8 ["INT_ADD", "register:40f0:8", ["const:b8dac8:8", "const:4:8"]]
- 00b8dac8 ["CALL", null, ["callee:00c59150:8"]]
+ 00b8eabc ["INT_ADD", "register:40f0:8", ["const:b8eabc:8", "const:4:8"]]
+ 00b8eabc ["CALL", null, ["callee:00c59150:8"]]
- 00b8dac8 bytes ae290394
+ 00b8eabc bytes a5290394
- 00b8d9fc ["INT_ADD", "register:40f0:8", ["const:b8d9fc:8", "const:4:8"]]
- 00b8d9fc ["CALL", null, ["callee:00c5db10:8"]]
+ 00b8e9f0 ["INT_ADD", "register:40f0:8", ["const:b8e9f0:8", "const:4:8"]]
+ 00b8e9f0 ["CALL", null, ["callee:00c5db10:8"]]
- 00b8d9fc bytes 513c0394
+ 00b8e9f0 bytes 483c0394
- 00b8da1c ["INT_ADD", "register:40f0:8", ["const:b8da1c:8", "const:4:8"]]
- 00b8da1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b8ea10 ["INT_ADD", "register:40f0:8", ["const:b8ea10:8", "const:4:8"]]
+ 00b8ea10 ["CALL", null, ["callee:00c58f50:8"]]
- 00b8da1c bytes 59290394
+ 00b8ea10 bytes 50290394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-825cef8e8651be09028cdb5a81afa8cb"></a>

### [`00b8e178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md) → [`00b8f16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md) _ZN11flatbuffers6Parser9SerializeEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 32件 [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md) [`0054a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a654.md) [`00bb09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb09f8.md) [`00bb16dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb16dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 32件 [`00540c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c30.md) [`0054a974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054a974.md) [`00bb19ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb19ec.md) [`00bb26d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb26d0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.88% / 新版 99.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8f274",
      "incomplete_value": false,
      "site": "00b8f274",
      "value": [
        "leaf",
        "const:bb19ec:8"
      ]
    },
    "old": {
      "definition_site": "00b8e280",
      "incomplete_value": false,
      "site": "00b8e280",
      "value": [
        "leaf",
        "const:bb09f8:8"
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b8f354",
      "incomplete_value": false,
      "site": "00b8f354",
      "value": [
        "leaf",
        "const:bb26d0:8"
      ]
    },
    "old": {
      "definition_site": "00b8e360",
      "incomplete_value": false,
      "site": "00b8e360",
      "value": [
        "leaf",
        "const:bb16dc:8"
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b8fd60",
      "incomplete_value": false,
      "site": "00b8fd68",
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
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8ed6c",
      "incomplete_value": false,
      "site": "00b8ed74",
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
            "const:eaf:8"
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8f274",
      "DATA",
      [
        "storage",
        "00bb09f8",
        null,
        null
      ]
    ],
    [
      "00b8f354",
      "DATA",
      [
        "storage",
        "00bb16dc",
        null,
        null
      ]
    ],
    [
      "00b8fa3c",
      "READ",
      [
        "storage",
        "00c9b960",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8f274",
      "DATA",
      [
        "storage",
        "00bb19ec",
        null,
        null
      ]
    ],
    [
      "00b8f354",
      "DATA",
      [
        "storage",
        "00bb26d0",
        null,
        null
      ]
    ],
    [
      "00b8fa3c",
      "READ",
      [
        "storage",
        "00c9c930",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ed74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md#insn-00b8ed74) · [`00b8e20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md#insn-00b8e20c) · [`00b8e238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8e/00b8e178.md#insn-00b8e238)
- 新版 [`00b8fd68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md#insn-00b8fd68) · [`00b8f200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md#insn-00b8f200) · [`00b8f22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b8f/00b8f16c.md#insn-00b8f22c)

~~~diff
- 00b8ed74 ["INT_ADD", "register:40f0:8", ["const:b8ed74:8", "const:4:8"]]
- 00b8ed74 ["CALL", null, ["callee:00c5d3d0:8"]]
+ 00b8fd68 ["INT_ADD", "register:40f0:8", ["const:b8fd68:8", "const:4:8"]]
+ 00b8fd68 ["CALL", null, ["callee:00c5d3d0:8"]]
- 00b8ed74 bytes a3350394
+ 00b8fd68 bytes 9a350394
- 00b8e20c ["INT_ADD", "register:40f0:8", ["const:b8e20c:8", "const:4:8"]]
- 00b8e20c ["CALL", null, ["callee:00c5cab0:8"]]
+ 00b8f200 ["INT_ADD", "register:40f0:8", ["const:b8f200:8", "const:4:8"]]
+ 00b8f200 ["CALL", null, ["callee:00c5cab0:8"]]
- 00b8e20c bytes 35360394
+ 00b8f200 bytes 2c360394
- 00b8e238 ["INT_ADD", "register:40f0:8", ["const:b8e238:8", "const:4:8"]]
- 00b8e238 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b8f22c ["INT_ADD", "register:40f0:8", ["const:b8f22c:8", "const:4:8"]]
+ 00b8f22c ["CALL", null, ["callee:00c58f30:8"]]
- 00b8e238 bytes 4a270394
+ 00b8f22c bytes 41270394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ee051e12ae320eb3386e3190ebf53c"></a>

### [`00b908ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b908ac.md) → [`00b918a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b918a0.md) _ZN11flatbuffers9StructDef11DeserializeERNS_6ParserEPKN10reflection6ObjectE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c960.md) · 呼出先 14件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d930.md) · 呼出先 14件 [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b91d10",
      "incomplete_value": true,
      "site": "00b91d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:18a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b90d1c",
      "incomplete_value": true,
      "site": "00b90d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:bb:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b91b40",
      "READ",
      [
        "storage",
        "002b0598",
        null,
        "string"
      ]
    ],
    [
      "00b91b44",
      "READ",
      [
        "storage",
        "002b059e",
        null,
        "string"
      ]
    ],
    [
      "00b91c88",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b91b40",
      "READ",
      [
        "storage",
        "002b066f",
        null,
        "string"
      ]
    ],
    [
      "00b91b44",
      "READ",
      [
        "storage",
        "002b0675",
        null,
        "string"
      ]
    ],
    [
      "00b91c88",
      "READ",
      [
        "storage",
        "002c3f68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b908ac.md#insn-00b90d20) · [`00b90920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b908ac.md#insn-00b90920) · [`00b90a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b908ac.md#insn-00b90a00)
- 新版 [`00b91d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b918a0.md#insn-00b91d14) · [`00b91914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b918a0.md#insn-00b91914) · [`00b919f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b918a0.md#insn-00b919f4)

~~~diff
- 00b90d20 ["INT_ADD", "register:40f0:8", ["const:b90d20:8", "const:4:8"]]
- 00b90d20 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b91d14 ["INT_ADD", "register:40f0:8", ["const:b91d14:8", "const:4:8"]]
+ 00b91d14 ["CALL", null, ["callee:00c5c660:8"]]
- 00b90d20 bytes 5c2a0394
+ 00b91d14 bytes 532a0394
- 00b90920 ["INT_ADD", "register:40f0:8", ["const:b90920:8", "const:4:8"]]
- 00b90920 ["CALL", null, ["callee:00b941e0:8"]]
+ 00b91914 ["INT_ADD", "register:40f0:8", ["const:b91914:8", "const:4:8"]]
+ 00b91914 ["CALL", null, ["callee:00b941e0:8"]]
- 00b90920 bytes 330a0094
+ 00b91914 bytes 330a0094
- 00b90a00 ["INT_ADD", "register:40f0:8", ["const:b90a00:8", "const:4:8"]]
- 00b90a00 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b919f4 ["INT_ADD", "register:40f0:8", ["const:b919f4:8", "const:4:8"]]
+ 00b919f4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b90a00 bytes 581d0394
+ 00b919f4 bytes 4f1d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8878eb20c6a9416ca1addf03bb60ec0b"></a>

### [`00b90ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec8.md) → [`00b91ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91ebc.md) _ZN11flatbuffers8FieldDef11DeserializeERNS_6ParserEPKN10reflection5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c910.md) · 呼出先 12件 [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d8e0.md) · 呼出先 12件 [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9223c",
      "incomplete_value": true,
      "site": "00b9223c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:65b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91248",
      "incomplete_value": true,
      "site": "00b91248",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:503:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9227c",
      "incomplete_value": true,
      "site": "00b9229c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:944:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b91288",
      "incomplete_value": true,
      "site": "00b912a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:866:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b92218",
      "READ",
      [
        "storage",
        "002a8503",
        null,
        "string"
      ]
    ],
    [
      "00b9227c",
      "READ",
      [
        "storage",
        "002bf866",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b92218",
      "READ",
      [
        "storage",
        "002a865b",
        null,
        "string"
      ]
    ],
    [
      "00b9227c",
      "READ",
      [
        "storage",
        "002bf944",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec8.md#insn-00b90f50) · [`00b90f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec8.md#insn-00b90f70) · [`00b90fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec8.md#insn-00b90fa0)
- 新版 [`00b91f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91ebc.md#insn-00b91f44) · [`00b91f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91ebc.md#insn-00b91f64) · [`00b91f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91ebc.md#insn-00b91f94)

~~~diff
- 00b90f50 ["INT_ADD", "register:40f0:8", ["const:b90f50:8", "const:4:8"]]
- 00b90f50 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b91f44 ["INT_ADD", "register:40f0:8", ["const:b91f44:8", "const:4:8"]]
+ 00b91f44 ["CALL", null, ["callee:00c58f30:8"]]
- 00b90f50 bytes 041c0394
+ 00b91f44 bytes fb1b0394
- 00b90f70 ["INT_ADD", "register:40f0:8", ["const:b90f70:8", "const:4:8"]]
- 00b90f70 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b91f64 ["INT_ADD", "register:40f0:8", ["const:b91f64:8", "const:4:8"]]
+ 00b91f64 ["CALL", null, ["callee:00c590a0:8"]]
- 00b90f70 bytes 581c0394
+ 00b91f64 bytes 4f1c0394
- 00b90fa0 ["INT_ADD", "register:40f0:8", ["const:b90fa0:8", "const:4:8"]]
- 00b90fa0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b91f94 ["INT_ADD", "register:40f0:8", ["const:b91f94:8", "const:4:8"]]
+ 00b91f94 ["CALL", null, ["callee:00c58f50:8"]]
- 00b90fa0 bytes f81b0394
+ 00b91f94 bytes ef1b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e328c7a80c927d77cd779a7cf3d4397"></a>

### [`00b931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md) → [`00b941e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md) FUN_00b941e0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00b908ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b908ac.md) [`00b90ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec0.md) [`00b90ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b90ec8.md) [`00b91d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91d24.md) [`00b92178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92178.md) · 呼出先 8件 [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 8件 [`00b918a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b918a0.md) [`00b91eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91eb4.md) [`00b91ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b91/00b91ebc.md) [`00b92d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b92/00b92d18.md) [`00b9316c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b93/00b9316c.md) · 呼出先 8件 [`006398ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/006398ac.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.58% / 新版 99.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b94298",
      "incomplete_value": false,
      "site": "00b9429c",
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
            "const:18a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b932a4",
      "incomplete_value": false,
      "site": "00b932a8",
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
            "const:bb:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b94298",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b94298",
      "PARAM",
      [
        "storage",
        "002b818a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b932a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md#insn-00b932a8) · [`00b93284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md#insn-00b93284) · [`00b932a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b931ec.md#insn-00b932a4)
- 新版 [`00b9429c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md#insn-00b9429c) · [`00b94278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md#insn-00b94278) · [`00b94298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b941e0.md#insn-00b94298)

~~~diff
- 00b932a8 ["INT_ADD", "register:40f0:8", ["const:b932a8:8", "const:4:8"]]
- 00b932a8 ["CALL", null, ["callee:00c5c660:8"]]
+ 00b9429c ["INT_ADD", "register:40f0:8", ["const:b9429c:8", "const:4:8"]]
+ 00b9429c ["CALL", null, ["callee:00c5c660:8"]]
- 00b932a8 bytes fa200394
+ 00b9429c bytes f1200394
- 00b93284 ["INT_ADD", "register:40f0:8", ["const:b93284:8", "const:4:8"]]
- 00b93284 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b94278 ["INT_ADD", "register:40f0:8", ["const:b94278:8", "const:4:8"]]
+ 00b94278 ["CALL", null, ["callee:00c58f30:8"]]
- 00b93284 bytes 37130394
+ 00b94278 bytes 2e130394
- 00b932a4 ["COPY", "tmp:0:8", ["const:bb:8"]]
- 00b932a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b932a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b932a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b94298 ["COPY", "tmp:0:8", ["const:18a:8"]]
+ 00b94298 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94298 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94298 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b932a4 bytes 21ec0291
+ 00b94298 bytes 21280691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd34e384a697d3e3a5aac1114b42d9a"></a>

### [`00b938d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md) → [`00b948c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md) _ZN11flatbuffers6Parser11DeserializeEPKhm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b939e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b939e4.md) [`00b93a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93a80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c570.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b949d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b949d8.md) [`00b94a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94a74.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5d540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d540.md) [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b948ec",
      "incomplete_value": true,
      "site": "00b9491c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b938f8",
      "incomplete_value": true,
      "site": "00b93928",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:db0:8"
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
      "definition_site": "00b94910",
      "incomplete_value": false,
      "site": "00b94934",
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
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9391c",
      "incomplete_value": false,
      "site": "00b93940",
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
            "const:eaf:8"
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
      "definition_site": "00b94944",
      "incomplete_value": false,
      "site": "00b9494c",
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
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93950",
      "incomplete_value": false,
      "site": "00b93958",
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
            "const:eaf:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b948ec",
      "READ",
      [
        "storage",
        "002c3db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94910",
      "PARAM",
      [
        "storage",
        "002a4eaf",
        null,
        null
      ]
    ],
    [
      "00b94944",
      "PARAM",
      [
        "storage",
        "002a4eaf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b948ec",
      "READ",
      [
        "storage",
        "002c3e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b94910",
      "PARAM",
      [
        "storage",
        "002a4f7a",
        null,
        null
      ]
    ],
    [
      "00b94944",
      "PARAM",
      [
        "storage",
        "002a4f7a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md#insn-00b93940) · [`00b93958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md#insn-00b93958) · [`00b938f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md#insn-00b938f8)
- 新版 [`00b94934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md#insn-00b94934) · [`00b9494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md#insn-00b9494c) · [`00b948ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md#insn-00b948ec)

~~~diff
- 00b93940 ["INT_ADD", "register:40f0:8", ["const:b93940:8", "const:4:8"]]
- 00b93940 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00b94934 ["INT_ADD", "register:40f0:8", ["const:b94934:8", "const:4:8"]]
+ 00b94934 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b93940 bytes 30260394
+ 00b94934 bytes 27260394
- 00b93958 ["INT_ADD", "register:40f0:8", ["const:b93958:8", "const:4:8"]]
- 00b93958 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00b9494c ["INT_ADD", "register:40f0:8", ["const:b9494c:8", "const:4:8"]]
+ 00b9494c ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b93958 bytes 2a260394
+ 00b9494c bytes 21260394
- 00b938f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db0:8"]]
- 00b938f8 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b938f8 ["COPY", "register:5008:8", ["const:0:8"]]
- 00b938f8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00b948ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
+ 00b948ec ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b948ec ["COPY", "register:5008:8", ["const:0:8"]]
+ 00b948ec ["COPY", "register:5010:8", ["const:0:8"]]
- 00b938f8 bytes 20d946fd
+ 00b948ec bytes 200147fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eaed448483a9d0318c8585a09af1d4d"></a>

### [`00b939e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b939e4.md) → [`00b949d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b949d8.md) _ZN10reflection30VerifySizePrefixedSchemaBufferERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b938d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md) · 呼出先 2件 [`00c5ca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca40.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md)
- 新版 呼出元 1件 [`00b948c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md) · 呼出先 2件 [`00c5da10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da10.md) [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md)

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
      "definition_site": "00b94a1c",
      "incomplete_value": false,
      "site": "00b94a24",
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
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93a28",
      "incomplete_value": false,
      "site": "00b93a30",
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
            "const:eaf:8"
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
      "00b94a1c",
      "PARAM",
      [
        "storage",
        "002a4eaf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b94a1c",
      "PARAM",
      [
        "storage",
        "002a4f7a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b939e4.md#insn-00b93a30) · [`00b93a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b939e4.md#insn-00b93a28)
- 新版 [`00b94a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b949d8.md#insn-00b94a24) · [`00b94a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b949d8.md#insn-00b94a1c)

~~~diff
- 00b93a30 ["INT_ADD", "register:40f0:8", ["const:b93a30:8", "const:4:8"]]
- 00b93a30 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00b94a24 ["INT_ADD", "register:40f0:8", ["const:b94a24:8", "const:4:8"]]
+ 00b94a24 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b93a30 bytes f4250394
+ 00b94a24 bytes eb250394
- 00b93a28 ["COPY", "tmp:0:8", ["const:eaf:8"]]
- 00b93a28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b93a28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b93a28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b94a1c ["COPY", "tmp:0:8", ["const:f7a:8"]]
+ 00b94a1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94a1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94a1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b93a28 bytes 21bc3a91
+ 00b94a1c bytes 21e83d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd41c7aaa311c4e9301b8689893020ed"></a>

### [`00b93a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93a80.md) → [`00b94a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94a74.md) _ZN10reflection18VerifySchemaBufferERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b938d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b938d4.md) · 呼出先 2件 [`00c5ca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ca40.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md)
- 新版 呼出元 1件 [`00b948c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b948c8.md) · 呼出先 2件 [`00c5da10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5da10.md) [`00c5e1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1d0.md)

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
      "definition_site": "00b94a9c",
      "incomplete_value": false,
      "site": "00b94aa8",
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
            "const:f7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b93aa8",
      "incomplete_value": false,
      "site": "00b93ab4",
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
            "const:eaf:8"
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
      "00b94a9c",
      "PARAM",
      [
        "storage",
        "002a4eaf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b94a9c",
      "PARAM",
      [
        "storage",
        "002a4f7a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b93ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93a80.md#insn-00b93ab4) · [`00b93aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b93/00b93a80.md#insn-00b93aa8)
- 新版 [`00b94aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94a74.md#insn-00b94aa8) · [`00b94a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b94/00b94a74.md#insn-00b94a9c)

~~~diff
- 00b93ab4 ["INT_ADD", "register:40f0:8", ["const:b93ab4:8", "const:4:8"]]
- 00b93ab4 ["CALL", null, ["callee:00c5e1d0:8"]]
+ 00b94aa8 ["INT_ADD", "register:40f0:8", ["const:b94aa8:8", "const:4:8"]]
+ 00b94aa8 ["CALL", null, ["callee:00c5e1d0:8"]]
- 00b93ab4 bytes d3250394
+ 00b94aa8 bytes ca250394
- 00b93aa8 ["COPY", "tmp:0:8", ["const:eaf:8"]]
- 00b93aa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b93aa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b93aa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b94a9c ["COPY", "tmp:0:8", ["const:f7a:8"]]
+ 00b94a9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94a9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b94a9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b93aa8 bytes 21bc3a91
+ 00b94a9c bytes 21e83d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bd7274c17469394401893b0324985cb"></a>

### [`00b9514c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b9514c.md) → [`00b96140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96140.md) _ZN11flatbuffers6Parser9ConformToERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b964f0",
      "incomplete_value": false,
      "site": "00b964f4",
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
            "const:4e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b954fc",
      "incomplete_value": false,
      "site": "00b95500",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9654c",
      "incomplete_value": false,
      "site": "00b96550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:713:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b95558",
      "incomplete_value": false,
      "site": "00b9555c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:6c9:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b96560",
      "incomplete_value": false,
      "site": "00b96564",
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
            "const:882:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9556c",
      "incomplete_value": false,
      "site": "00b95570",
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
            "const:7b5:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b96244",
      "PARAM",
      [
        "storage",
        "002a638f",
        null,
        null
      ]
    ],
    [
      "00b9636c",
      "PARAM",
      [
        "storage",
        "002a2bae",
        null,
        "string"
      ]
    ],
    [
      "00b963d4",
      "PARAM",
      [
        "storage",
        "002a60d5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b96244",
      "PARAM",
      [
        "storage",
        "002a64e7",
        null,
        null
      ]
    ],
    [
      "00b9636c",
      "PARAM",
      [
        "storage",
        "002a2c79",
        null,
        "string"
      ]
    ],
    [
      "00b963d4",
      "PARAM",
      [
        "storage",
        "002a622d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b9514c.md#insn-00b95500) · [`00b9555c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b9514c.md#insn-00b9555c) · [`00b95570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b9514c.md#insn-00b95570)
- 新版 [`00b964f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96140.md#insn-00b964f4) · [`00b96550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96140.md#insn-00b96550) · [`00b96564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b96/00b96140.md#insn-00b96564)

~~~diff
- 00b95500 ["INT_ADD", "register:40f0:8", ["const:b95500:8", "const:4:8"]]
- 00b95500 ["CALL", null, ["callee:00b5bc44:8"]]
+ 00b964f4 ["INT_ADD", "register:40f0:8", ["const:b964f4:8", "const:4:8"]]
+ 00b964f4 ["CALL", null, ["callee:00b5bc44:8"]]
- 00b95500 bytes d415ff97
+ 00b964f4 bytes d415ff97
- 00b9555c ["INT_ADD", "register:40f0:8", ["const:b9555c:8", "const:4:8"]]
- 00b9555c ["CALL", null, ["callee:00c59150:8"]]
+ 00b96550 ["INT_ADD", "register:40f0:8", ["const:b96550:8", "const:4:8"]]
+ 00b96550 ["CALL", null, ["callee:00c59150:8"]]
- 00b9555c bytes 090b0394
+ 00b96550 bytes 000b0394
- 00b95570 ["INT_ADD", "register:40f0:8", ["const:b95570:8", "const:4:8"]]
- 00b95570 ["CALL", null, ["callee:00c59020:8"]]
+ 00b96564 ["INT_ADD", "register:40f0:8", ["const:b96564:8", "const:4:8"]]
+ 00b96564 ["CALL", null, ["callee:00c59020:8"]]
- 00b95570 bytes b80a0394
+ 00b96564 bytes af0a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3233318622bc71f379888682861bc110"></a>

### [`00b967f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b967f4.md) → [`00b977e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b977e8.md) _ZN11flatbuffers14EnumValBuilder13ValidateValueEPlb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c240.md) · 呼出先 15件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5d210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d210.md) · 呼出先 15件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5d170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.23% / 新版 92.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b978bc",
      "incomplete_value": true,
      "site": "00b978d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b968c8",
      "incomplete_value": true,
      "site": "00b968e0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:6f1:8"
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
      "definition_site": "00b978bc",
      "incomplete_value": true,
      "site": "00b978d4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b968c8",
      "incomplete_value": true,
      "site": "00b968e0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b978e4",
      "incomplete_value": false,
      "site": "00b978f4",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b968f0",
      "incomplete_value": false,
      "site": "00b96900",
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
            "const:b69:8"
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
      "00b9782c",
      "DATA",
      [
        "storage",
        "0030e1fd",
        "switchD_00b96840::switchdataD_0030e1fd",
        "byte"
      ]
    ],
    [
      "00b978bc",
      "READ",
      [
        "storage",
        "002b06f1",
        null,
        "string"
      ]
    ],
    [
      "00b978bc",
      "READ",
      [
        "storage",
        "002b0701",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b9782c",
      "DATA",
      [
        "storage",
        "0030e23d",
        "switchD_00b97834::switchdataD_0030e23d",
        "byte"
      ]
    ],
    [
      "00b978bc",
      "READ",
      [
        "storage",
        "002b07c8",
        null,
        "string"
      ]
    ],
    [
      "00b978bc",
      "READ",
      [
        "storage",
        "002b07d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b967f4.md#insn-00b96900) · [`00b96830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b967f4.md#insn-00b96830) · [`00b96834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b967f4.md#insn-00b96834)
- 新版 [`00b978f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b977e8.md#insn-00b978f4) · [`00b97824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b977e8.md#insn-00b97824)

~~~diff
- 00b96900 ["INT_ADD", "register:40f0:8", ["const:b96900:8", "const:4:8"]]
- 00b96900 ["CALL", null, ["callee:00c59150:8"]]
+ 00b978f4 ["INT_ADD", "register:40f0:8", ["const:b978f4:8", "const:4:8"]]
+ 00b978f4 ["CALL", null, ["callee:00c59150:8"]]
- 00b96900 bytes 20060394
+ 00b978f4 bytes 17060394
- 00b96830 ["COPY", "tmp:0:8", ["const:1fd:8"]]
- 00b96830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b96830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b96830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b97824 ["COPY", "tmp:0:8", ["const:23d:8"]]
+ 00b97824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b97824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b97824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b96830 bytes 08f50791
+ 00b97824 bytes 08f50891
- 00b96834 ["COPY", "register:4050:8", ["const:b96844:8"]]
- 00b96834 bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0edfe3893f2c20323382d960f1a3c02c"></a>

### [`00b96990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96990.md) → [`00b97984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97984.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE1EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1b0.md) · 呼出先 8件 [`00b97f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d180.md) · 呼出先 8件 [`00b98f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b979dc",
      "incomplete_value": false,
      "site": "00b979ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b969e8",
      "incomplete_value": false,
      "site": "00b969f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
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
      "definition_site": "00b97ac4",
      "incomplete_value": false,
      "site": "00b97acc",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96ad0",
      "incomplete_value": false,
      "site": "00b96ad8",
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
            "const:b69:8"
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
      "00b979dc",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b97a10",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b97a10",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b979dc",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b97a10",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b97a10",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b969f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96990.md#insn-00b969f8) · [`00b96ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96990.md#insn-00b96ad8) · [`00b969e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96990.md#insn-00b969e0)
- 新版 [`00b979ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97984.md#insn-00b979ec) · [`00b97acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97984.md#insn-00b97acc) · [`00b979d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97984.md#insn-00b979d4)

~~~diff
- 00b969f8 ["INT_ADD", "register:40f0:8", ["const:b969f8:8", "const:4:8"]]
- 00b969f8 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b979ec ["INT_ADD", "register:40f0:8", ["const:b979ec:8", "const:4:8"]]
+ 00b979ec ["CALL", null, ["callee:00c5a070:8"]]
- 00b969f8 bytes aa090394
+ 00b979ec bytes a1090394
- 00b96ad8 ["INT_ADD", "register:40f0:8", ["const:b96ad8:8", "const:4:8"]]
- 00b96ad8 ["CALL", null, ["callee:00c59150:8"]]
+ 00b97acc ["INT_ADD", "register:40f0:8", ["const:b97acc:8", "const:4:8"]]
+ 00b97acc ["CALL", null, ["callee:00c59150:8"]]
- 00b96ad8 bytes aa050394
+ 00b97acc bytes a1050394
- 00b969e0 ["INT_ADD", "register:40f0:8", ["const:b969e0:8", "const:4:8"]]
- 00b969e0 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b979d4 ["INT_ADD", "register:40f0:8", ["const:b979d4:8", "const:4:8"]]
+ 00b979d4 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b969e0 bytes bc150394
+ 00b979d4 bytes b3150394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a4c4140e0574d72ea6bf24fc4b86f2"></a>

### [`00b96bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96bc4.md) → [`00b97bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97bb8.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE2EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1c0.md) · 呼出先 8件 [`00b97f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d190.md) · 呼出先 8件 [`00b98f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97c70",
      "incomplete_value": false,
      "site": "00b97c8c",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96c7c",
      "incomplete_value": false,
      "site": "00b96c98",
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
            "const:b9f:8"
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
      "definition_site": "00b97cf8",
      "incomplete_value": false,
      "site": "00b97d00",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96d04",
      "incomplete_value": false,
      "site": "00b96d0c",
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
            "const:b69:8"
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
      "00b97c10",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b97c44",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b97c44",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97c10",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b97c44",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b97c44",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96bc4.md#insn-00b96c98) · [`00b96d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96bc4.md#insn-00b96d0c) · [`00b96c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96bc4.md#insn-00b96c14)
- 新版 [`00b97c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97bb8.md#insn-00b97c8c) · [`00b97d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97bb8.md#insn-00b97d00) · [`00b97c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97bb8.md#insn-00b97c08)

~~~diff
- 00b96c98 ["INT_ADD", "register:40f0:8", ["const:b96c98:8", "const:4:8"]]
- 00b96c98 ["CALL", null, ["callee:00c59020:8"]]
+ 00b97c8c ["INT_ADD", "register:40f0:8", ["const:b97c8c:8", "const:4:8"]]
+ 00b97c8c ["CALL", null, ["callee:00c59020:8"]]
- 00b96c98 bytes ee040394
+ 00b97c8c bytes e5040394
- 00b96d0c ["INT_ADD", "register:40f0:8", ["const:b96d0c:8", "const:4:8"]]
- 00b96d0c ["CALL", null, ["callee:00c59150:8"]]
+ 00b97d00 ["INT_ADD", "register:40f0:8", ["const:b97d00:8", "const:4:8"]]
+ 00b97d00 ["CALL", null, ["callee:00c59150:8"]]
- 00b96d0c bytes 1d050394
+ 00b97d00 bytes 14050394
- 00b96c14 ["INT_ADD", "register:40f0:8", ["const:b96c14:8", "const:4:8"]]
- 00b96c14 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b97c08 ["INT_ADD", "register:40f0:8", ["const:b97c08:8", "const:4:8"]]
+ 00b97c08 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b96c14 bytes 2f150394
+ 00b97c08 bytes 26150394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91fc107f0e2bdd1d1f2392d6f524d997"></a>

### [`00b96df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96df8.md) → [`00b97dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97dec.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE3EaEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1d0.md) · 呼出先 8件 [`00b9813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9813c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1a0.md) · 呼出先 8件 [`00b99130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99130.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b97ea8",
      "incomplete_value": false,
      "site": "00b97ec4",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96eb4",
      "incomplete_value": false,
      "site": "00b96ed0",
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
            "const:b9f:8"
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
      "definition_site": "00b97f30",
      "incomplete_value": false,
      "site": "00b97f38",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96f3c",
      "incomplete_value": false,
      "site": "00b96f44",
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
            "const:b69:8"
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
      "00b97e48",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b97e7c",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b97e7c",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b97e48",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b97e7c",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b97e7c",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96df8.md#insn-00b96ed0) · [`00b96f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96df8.md#insn-00b96f44) · [`00b96e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96df8.md#insn-00b96e4c)
- 新版 [`00b97ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97dec.md#insn-00b97ec4) · [`00b97f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97dec.md#insn-00b97f38) · [`00b97e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97dec.md#insn-00b97e40)

~~~diff
- 00b96ed0 ["INT_ADD", "register:40f0:8", ["const:b96ed0:8", "const:4:8"]]
- 00b96ed0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b97ec4 ["INT_ADD", "register:40f0:8", ["const:b97ec4:8", "const:4:8"]]
+ 00b97ec4 ["CALL", null, ["callee:00c59020:8"]]
- 00b96ed0 bytes 60040394
+ 00b97ec4 bytes 57040394
- 00b96f44 ["INT_ADD", "register:40f0:8", ["const:b96f44:8", "const:4:8"]]
- 00b96f44 ["CALL", null, ["callee:00c59150:8"]]
+ 00b97f38 ["INT_ADD", "register:40f0:8", ["const:b97f38:8", "const:4:8"]]
+ 00b97f38 ["CALL", null, ["callee:00c59150:8"]]
- 00b96f44 bytes 8f040394
+ 00b97f38 bytes 86040394
- 00b96e4c ["INT_ADD", "register:40f0:8", ["const:b96e4c:8", "const:4:8"]]
- 00b96e4c ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b97e40 ["INT_ADD", "register:40f0:8", ["const:b97e40:8", "const:4:8"]]
+ 00b97e40 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b96e4c bytes a1140394
+ 00b97e40 bytes 98140394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35981b912e868f410bf5f9b08f5d3549"></a>

### [`00b97030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97030.md) → [`00b98024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98024.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE4EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1e0.md) · 呼出先 8件 [`00b97f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1b0.md) · 呼出先 8件 [`00b98f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b980dc",
      "incomplete_value": false,
      "site": "00b980f8",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b970e8",
      "incomplete_value": false,
      "site": "00b97104",
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
            "const:b9f:8"
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
      "definition_site": "00b98164",
      "incomplete_value": false,
      "site": "00b9816c",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97170",
      "incomplete_value": false,
      "site": "00b97178",
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
            "const:b69:8"
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
      "00b9807c",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b980b0",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b980b0",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b9807c",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b980b0",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b980b0",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97030.md#insn-00b97104) · [`00b97178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97030.md#insn-00b97178) · [`00b97080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97030.md#insn-00b97080)
- 新版 [`00b980f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98024.md#insn-00b980f8) · [`00b9816c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98024.md#insn-00b9816c) · [`00b98074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98024.md#insn-00b98074)

~~~diff
- 00b97104 ["INT_ADD", "register:40f0:8", ["const:b97104:8", "const:4:8"]]
- 00b97104 ["CALL", null, ["callee:00c59020:8"]]
+ 00b980f8 ["INT_ADD", "register:40f0:8", ["const:b980f8:8", "const:4:8"]]
+ 00b980f8 ["CALL", null, ["callee:00c59020:8"]]
- 00b97104 bytes d3030394
+ 00b980f8 bytes ca030394
- 00b97178 ["INT_ADD", "register:40f0:8", ["const:b97178:8", "const:4:8"]]
- 00b97178 ["CALL", null, ["callee:00c59150:8"]]
+ 00b9816c ["INT_ADD", "register:40f0:8", ["const:b9816c:8", "const:4:8"]]
+ 00b9816c ["CALL", null, ["callee:00c59150:8"]]
- 00b97178 bytes 02040394
+ 00b9816c bytes f9030394
- 00b97080 ["INT_ADD", "register:40f0:8", ["const:b97080:8", "const:4:8"]]
- 00b97080 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b98074 ["INT_ADD", "register:40f0:8", ["const:b98074:8", "const:4:8"]]
+ 00b98074 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b97080 bytes 14140394
+ 00b98074 bytes 0b140394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-922cf9a31b013950c0bc45b1bf7f4aea"></a>

### [`00b97264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97264.md) → [`00b98258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98258.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE5EsEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1f0.md) · 呼出先 8件 [`00b982dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1c0.md) · 呼出先 8件 [`00b992d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98314",
      "incomplete_value": false,
      "site": "00b98330",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97320",
      "incomplete_value": false,
      "site": "00b9733c",
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
            "const:b9f:8"
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
      "definition_site": "00b9839c",
      "incomplete_value": false,
      "site": "00b983a4",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b973a8",
      "incomplete_value": false,
      "site": "00b973b0",
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
            "const:b69:8"
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
      "00b982b4",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b982e8",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b982e8",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b982b4",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b982e8",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b982e8",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9733c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97264.md#insn-00b9733c) · [`00b973b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97264.md#insn-00b973b0) · [`00b972b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97264.md#insn-00b972b8)
- 新版 [`00b98330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98258.md#insn-00b98330) · [`00b983a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98258.md#insn-00b983a4) · [`00b982ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98258.md#insn-00b982ac)

~~~diff
- 00b9733c ["INT_ADD", "register:40f0:8", ["const:b9733c:8", "const:4:8"]]
- 00b9733c ["CALL", null, ["callee:00c59020:8"]]
+ 00b98330 ["INT_ADD", "register:40f0:8", ["const:b98330:8", "const:4:8"]]
+ 00b98330 ["CALL", null, ["callee:00c59020:8"]]
- 00b9733c bytes 45030394
+ 00b98330 bytes 3c030394
- 00b973b0 ["INT_ADD", "register:40f0:8", ["const:b973b0:8", "const:4:8"]]
- 00b973b0 ["CALL", null, ["callee:00c59150:8"]]
+ 00b983a4 ["INT_ADD", "register:40f0:8", ["const:b983a4:8", "const:4:8"]]
+ 00b983a4 ["CALL", null, ["callee:00c59150:8"]]
- 00b973b0 bytes 74030394
+ 00b983a4 bytes 6b030394
- 00b972b8 ["INT_ADD", "register:40f0:8", ["const:b972b8:8", "const:4:8"]]
- 00b972b8 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b982ac ["INT_ADD", "register:40f0:8", ["const:b982ac:8", "const:4:8"]]
+ 00b982ac ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b972b8 bytes 86130394
+ 00b982ac bytes 7d130394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c85ef0ed20affb60537e22757246e50e"></a>

### [`00b9749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9749c.md) → [`00b98490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98490.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE6EtEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c200.md) · 呼出先 8件 [`00b9847c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1d0.md) · 呼出先 8件 [`00b99470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.45% / 新版 96.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98548",
      "incomplete_value": false,
      "site": "00b98564",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97554",
      "incomplete_value": false,
      "site": "00b97570",
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
            "const:b9f:8"
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
      "definition_site": "00b985d0",
      "incomplete_value": false,
      "site": "00b985d8",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b975dc",
      "incomplete_value": false,
      "site": "00b975e4",
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
            "const:b69:8"
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
      "00b984e8",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b9851c",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b9851c",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b984e8",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b9851c",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b9851c",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9749c.md#insn-00b97570) · [`00b975e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9749c.md#insn-00b975e4) · [`00b974ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9749c.md#insn-00b974ec)
- 新版 [`00b98564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98490.md#insn-00b98564) · [`00b985d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98490.md#insn-00b985d8) · [`00b984e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98490.md#insn-00b984e0)

~~~diff
- 00b97570 ["INT_ADD", "register:40f0:8", ["const:b97570:8", "const:4:8"]]
- 00b97570 ["CALL", null, ["callee:00c59020:8"]]
+ 00b98564 ["INT_ADD", "register:40f0:8", ["const:b98564:8", "const:4:8"]]
+ 00b98564 ["CALL", null, ["callee:00c59020:8"]]
- 00b97570 bytes b8020394
+ 00b98564 bytes af020394
- 00b975e4 ["INT_ADD", "register:40f0:8", ["const:b975e4:8", "const:4:8"]]
- 00b975e4 ["CALL", null, ["callee:00c59150:8"]]
+ 00b985d8 ["INT_ADD", "register:40f0:8", ["const:b985d8:8", "const:4:8"]]
+ 00b985d8 ["CALL", null, ["callee:00c59150:8"]]
- 00b975e4 bytes e7020394
+ 00b985d8 bytes de020394
- 00b974ec ["INT_ADD", "register:40f0:8", ["const:b974ec:8", "const:4:8"]]
- 00b974ec ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b984e0 ["INT_ADD", "register:40f0:8", ["const:b984e0:8", "const:4:8"]]
+ 00b984e0 ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b974ec bytes f9120394
+ 00b984e0 bytes f0120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-774166869137d8469f4a886c9d341415"></a>

### [`00b976d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b976d0.md) → [`00b986c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b986c4.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE7EiEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c210.md) · 呼出先 8件 [`00b9861c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1e0.md) · 呼出先 8件 [`00b99610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98724",
      "incomplete_value": false,
      "site": "00b98734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97730",
      "incomplete_value": false,
      "site": "00b97740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
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
      "definition_site": "00b9880c",
      "incomplete_value": false,
      "site": "00b98814",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97818",
      "incomplete_value": false,
      "site": "00b97820",
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
            "const:b69:8"
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
      "00b98724",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b98758",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b98758",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98724",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b98758",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b98758",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b976d0.md#insn-00b97740) · [`00b97820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b976d0.md#insn-00b97820) · [`00b97728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b976d0.md#insn-00b97728)
- 新版 [`00b98734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b986c4.md#insn-00b98734) · [`00b98814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b986c4.md#insn-00b98814) · [`00b9871c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b986c4.md#insn-00b9871c)

~~~diff
- 00b97740 ["INT_ADD", "register:40f0:8", ["const:b97740:8", "const:4:8"]]
- 00b97740 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b98734 ["INT_ADD", "register:40f0:8", ["const:b98734:8", "const:4:8"]]
+ 00b98734 ["CALL", null, ["callee:00c5a070:8"]]
- 00b97740 bytes 58060394
+ 00b98734 bytes 4f060394
- 00b97820 ["INT_ADD", "register:40f0:8", ["const:b97820:8", "const:4:8"]]
- 00b97820 ["CALL", null, ["callee:00c59150:8"]]
+ 00b98814 ["INT_ADD", "register:40f0:8", ["const:b98814:8", "const:4:8"]]
+ 00b98814 ["CALL", null, ["callee:00c59150:8"]]
- 00b97820 bytes 58020394
+ 00b98814 bytes 4f020394
- 00b97728 ["INT_ADD", "register:40f0:8", ["const:b97728:8", "const:4:8"]]
- 00b97728 ["CALL", null, ["callee:00c5d0a0:8"]]
+ 00b9871c ["INT_ADD", "register:40f0:8", ["const:b9871c:8", "const:4:8"]]
+ 00b9871c ["CALL", null, ["callee:00c5d0a0:8"]]
- 00b97728 bytes 6a120394
+ 00b9871c bytes 61120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef255b29b188597622dc8fdc24421e5"></a>

### [`00b9790c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9790c.md) → [`00b98900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98900.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE8EjEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c220.md) · 呼出先 8件 [`00b987bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d1f0.md) · 呼出先 8件 [`00b997b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98958",
      "incomplete_value": false,
      "site": "00b98968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97964",
      "incomplete_value": false,
      "site": "00b97974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
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
      "definition_site": "00b989b8",
      "incomplete_value": false,
      "site": "00b989d4",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b979c4",
      "incomplete_value": false,
      "site": "00b979e0",
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
            "const:b9f:8"
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
      "definition_site": "00b98a40",
      "incomplete_value": false,
      "site": "00b98a48",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97a4c",
      "incomplete_value": false,
      "site": "00b97a54",
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
            "const:b69:8"
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
      "00b98958",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b9898c",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b9898c",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98958",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b9898c",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b9898c",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9790c.md#insn-00b97974) · [`00b979e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9790c.md#insn-00b979e0) · [`00b97a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9790c.md#insn-00b97a54)
- 新版 [`00b98968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98900.md#insn-00b98968) · [`00b989d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98900.md#insn-00b989d4) · [`00b98a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98900.md#insn-00b98a48)

~~~diff
- 00b97974 ["INT_ADD", "register:40f0:8", ["const:b97974:8", "const:4:8"]]
- 00b97974 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b98968 ["INT_ADD", "register:40f0:8", ["const:b98968:8", "const:4:8"]]
+ 00b98968 ["CALL", null, ["callee:00c5a070:8"]]
- 00b97974 bytes cb050394
+ 00b98968 bytes c2050394
- 00b979e0 ["INT_ADD", "register:40f0:8", ["const:b979e0:8", "const:4:8"]]
- 00b979e0 ["CALL", null, ["callee:00c59020:8"]]
+ 00b989d4 ["INT_ADD", "register:40f0:8", ["const:b989d4:8", "const:4:8"]]
+ 00b989d4 ["CALL", null, ["callee:00c59020:8"]]
- 00b979e0 bytes 9c010394
+ 00b989d4 bytes 93010394
- 00b97a54 ["INT_ADD", "register:40f0:8", ["const:b97a54:8", "const:4:8"]]
- 00b97a54 ["CALL", null, ["callee:00c59150:8"]]
+ 00b98a48 ["INT_ADD", "register:40f0:8", ["const:b98a48:8", "const:4:8"]]
+ 00b98a48 ["CALL", null, ["callee:00c59150:8"]]
- 00b97a54 bytes cb010394
+ 00b98a48 bytes c2010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df5a08746c472c69064852230cf6a92d"></a>

### [`00b97b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97b40.md) → [`00b98b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98b34.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE9ElEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c230.md) · 呼出先 8件 [`00b9895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d200.md) · 呼出先 8件 [`00b99950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98b88",
      "incomplete_value": false,
      "site": "00b98b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97b94",
      "incomplete_value": false,
      "site": "00b97ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
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
      "definition_site": "00b98be8",
      "incomplete_value": false,
      "site": "00b98c04",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97bf4",
      "incomplete_value": false,
      "site": "00b97c10",
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
            "const:b9f:8"
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
      "definition_site": "00b98c70",
      "incomplete_value": false,
      "site": "00b98c78",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97c7c",
      "incomplete_value": false,
      "site": "00b97c84",
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
            "const:b69:8"
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
      "00b98b88",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b98bbc",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b98bbc",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98b88",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b98bbc",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b98bbc",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97b40.md#insn-00b97ba4) · [`00b97c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97b40.md#insn-00b97c10) · [`00b97c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97b40.md#insn-00b97c84)
- 新版 [`00b98b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98b34.md#insn-00b98b98) · [`00b98c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98b34.md#insn-00b98c04) · [`00b98c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98b34.md#insn-00b98c78)

~~~diff
- 00b97ba4 ["INT_ADD", "register:40f0:8", ["const:b97ba4:8", "const:4:8"]]
- 00b97ba4 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b98b98 ["INT_ADD", "register:40f0:8", ["const:b98b98:8", "const:4:8"]]
+ 00b98b98 ["CALL", null, ["callee:00c5a070:8"]]
- 00b97ba4 bytes 3f050394
+ 00b98b98 bytes 36050394
- 00b97c10 ["INT_ADD", "register:40f0:8", ["const:b97c10:8", "const:4:8"]]
- 00b97c10 ["CALL", null, ["callee:00c59020:8"]]
+ 00b98c04 ["INT_ADD", "register:40f0:8", ["const:b98c04:8", "const:4:8"]]
+ 00b98c04 ["CALL", null, ["callee:00c59020:8"]]
- 00b97c10 bytes 10010394
+ 00b98c04 bytes 07010394
- 00b97c84 ["INT_ADD", "register:40f0:8", ["const:b97c84:8", "const:4:8"]]
- 00b97c84 ["CALL", null, ["callee:00c59150:8"]]
+ 00b98c78 ["INT_ADD", "register:40f0:8", ["const:b98c78:8", "const:4:8"]]
+ 00b98c78 ["CALL", null, ["callee:00c59150:8"]]
- 00b97c84 bytes 3f010394
+ 00b98c78 bytes 36010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f7b33103e8f33c1d6be6b6d10a8cf6"></a>

### [`00b97d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97d70.md) → [`00b98d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98d64.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE10EmEENS_12CheckedErrorEPli

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c1a0.md) · 呼出先 8件 [`00b98afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00c5d170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d170.md) · 呼出先 8件 [`00b99af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.68% / 新版 95.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b98db4",
      "incomplete_value": false,
      "site": "00b98dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:be7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97dc0",
      "incomplete_value": false,
      "site": "00b97dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:b9d:8"
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
      "definition_site": "00b98e14",
      "incomplete_value": false,
      "site": "00b98e30",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b97e20",
      "incomplete_value": false,
      "site": "00b97e3c",
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
            "const:b9f:8"
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
      "00b98db4",
      "PARAM",
      [
        "storage",
        "002c0b9d",
        null,
        "string"
      ]
    ],
    [
      "00b98de8",
      "PARAM",
      [
        "storage",
        "002c1cc1",
        null,
        "string"
      ]
    ],
    [
      "00b98de8",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98db4",
      "PARAM",
      [
        "storage",
        "002c0be7",
        null,
        "string"
      ]
    ],
    [
      "00b98de8",
      "PARAM",
      [
        "storage",
        "002c1d0b",
        null,
        "string"
      ]
    ],
    [
      "00b98de8",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97d70.md#insn-00b97dd0) · [`00b97e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97d70.md#insn-00b97e3c) · [`00b97db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97d70.md#insn-00b97db8)
- 新版 [`00b98dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98d64.md#insn-00b98dc4) · [`00b98e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98d64.md#insn-00b98e30) · [`00b98dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98d64.md#insn-00b98dac)

~~~diff
- 00b97dd0 ["INT_ADD", "register:40f0:8", ["const:b97dd0:8", "const:4:8"]]
- 00b97dd0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b98dc4 ["INT_ADD", "register:40f0:8", ["const:b98dc4:8", "const:4:8"]]
+ 00b98dc4 ["CALL", null, ["callee:00c5a070:8"]]
- 00b97dd0 bytes b4040394
+ 00b98dc4 bytes ab040394
- 00b97e3c ["INT_ADD", "register:40f0:8", ["const:b97e3c:8", "const:4:8"]]
- 00b97e3c ["CALL", null, ["callee:00c59020:8"]]
+ 00b98e30 ["INT_ADD", "register:40f0:8", ["const:b98e30:8", "const:4:8"]]
+ 00b98e30 ["CALL", null, ["callee:00c59020:8"]]
- 00b97e3c bytes 85000394
+ 00b98e30 bytes 7c000394
- 00b97db8 ["INT_ADD", "register:40f0:8", ["const:b97db8:8", "const:4:8"]]
- 00b97db8 ["CALL", null, ["callee:00c5d0b0:8"]]
+ 00b98dac ["INT_ADD", "register:40f0:8", ["const:b98dac:8", "const:4:8"]]
+ 00b98dac ["CALL", null, ["callee:00c5d0b0:8"]]
- 00b97db8 bytes ca100394
+ 00b98dac bytes c1100394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3898348567f9b69a22d51c58732d6cb8"></a>

### [`00b97f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md) → [`00b98f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md) FUN_00b98f90

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b789fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b789fc.md) [`00b96990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96990.md) [`00b96bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96bc4.md) [`00b97030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97030.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md)
- 新版 呼出元 4件 [`00b799f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b799f0.md) [`00b97984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97984.md) [`00b97bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b97/00b97bb8.md) [`00b98024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98024.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b9905c",
      "incomplete_value": false,
      "site": "00b99078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98068",
      "incomplete_value": false,
      "site": "00b98084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b98fc4",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b98fe4",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b9905c",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b98fc4",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b98fe4",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b9905c",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md#insn-00b98084) · [`00b97fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md#insn-00b97fc8) · [`00b97fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97f9c.md#insn-00b97fd0)
- 新版 [`00b99078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md#insn-00b99078) · [`00b98fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md#insn-00b98fbc) · [`00b98fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98f90.md#insn-00b98fc4)

~~~diff
- 00b98084 ["INT_ADD", "register:40f0:8", ["const:b98084:8", "const:4:8"]]
- 00b98084 ["CALL", null, ["callee:00c59020:8"]]
+ 00b99078 ["INT_ADD", "register:40f0:8", ["const:b99078:8", "const:4:8"]]
+ 00b99078 ["CALL", null, ["callee:00c59020:8"]]
- 00b98084 bytes f3ff0294
+ 00b99078 bytes eaff0294
- 00b97fc8 ["INT_ADD", "register:40f0:8", ["const:b97fc8:8", "const:4:8"]]
- 00b97fc8 ["CALL", null, ["callee:00c5d080:8"]]
+ 00b98fbc ["INT_ADD", "register:40f0:8", ["const:b98fbc:8", "const:4:8"]]
+ 00b98fbc ["CALL", null, ["callee:00c5d080:8"]]
- 00b97fc8 bytes 3a100394
+ 00b98fbc bytes 31100394
- 00b97fd0 ["COPY", "tmp:0:8", ["const:a89:8"]]
- 00b97fd0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b97fd0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b97fd0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b98fc4 ["COPY", "tmp:0:8", ["const:b56:8"]]
+ 00b98fc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b98fc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b98fc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b97fd0 bytes 42242a91
+ 00b98fc4 bytes 42582d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d09b61f471094de81f0708f04653dd1"></a>

### [`00b982dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md) → [`00b992d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md) FUN_00b992d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b7d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d724.md) [`00b97264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97264.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0f0.md)
- 新版 呼出元 2件 [`00b7e718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7e718.md) [`00b98258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98258.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99304",
      "incomplete_value": false,
      "site": "00b99314",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98310",
      "incomplete_value": false,
      "site": "00b98320",
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
            "const:a89:8"
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
      "definition_site": "00b99324",
      "incomplete_value": false,
      "site": "00b99340",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98330",
      "incomplete_value": false,
      "site": "00b9834c",
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
            "const:715:8"
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
      "definition_site": "00b9939c",
      "incomplete_value": false,
      "site": "00b993b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b983a8",
      "incomplete_value": false,
      "site": "00b983c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b99304",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b99324",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b9939c",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b99304",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b99324",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b9939c",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md#insn-00b98320) · [`00b9834c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md#insn-00b9834c) · [`00b983c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b982dc.md#insn-00b983c4)
- 新版 [`00b99314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md#insn-00b99314) · [`00b99340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md#insn-00b99340) · [`00b993b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b992d0.md#insn-00b993b8)

~~~diff
- 00b98320 ["INT_ADD", "register:40f0:8", ["const:b98320:8", "const:4:8"]]
- 00b98320 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b99314 ["INT_ADD", "register:40f0:8", ["const:b99314:8", "const:4:8"]]
+ 00b99314 ["CALL", null, ["callee:00c5a070:8"]]
- 00b98320 bytes 60030394
+ 00b99314 bytes 57030394
- 00b9834c ["INT_ADD", "register:40f0:8", ["const:b9834c:8", "const:4:8"]]
- 00b9834c ["CALL", null, ["callee:00c59020:8"]]
+ 00b99340 ["INT_ADD", "register:40f0:8", ["const:b99340:8", "const:4:8"]]
+ 00b99340 ["CALL", null, ["callee:00c59020:8"]]
- 00b9834c bytes 41ff0294
+ 00b99340 bytes 38ff0294
- 00b983c4 ["INT_ADD", "register:40f0:8", ["const:b983c4:8", "const:4:8"]]
- 00b983c4 ["CALL", null, ["callee:00c59020:8"]]
+ 00b993b8 ["INT_ADD", "register:40f0:8", ["const:b993b8:8", "const:4:8"]]
+ 00b993b8 ["CALL", null, ["callee:00c59020:8"]]
- 00b983c4 bytes 23ff0294
+ 00b993b8 bytes 1aff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-389ab6787c6f7c6f3405d6a7c38ca53b"></a>

### [`00b9847c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md) → [`00b99470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md) FUN_00b99470

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b76dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b76dc8.md) [`00b9749c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9749c.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c100.md)
- 新版 呼出元 2件 [`00b77dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b77dbc.md) [`00b98490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98490.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b994a4",
      "incomplete_value": false,
      "site": "00b994b4",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b984b0",
      "incomplete_value": false,
      "site": "00b984c0",
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
            "const:a89:8"
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
      "definition_site": "00b9953c",
      "incomplete_value": false,
      "site": "00b99558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98548",
      "incomplete_value": false,
      "site": "00b98564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b994a4",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b994c4",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b9953c",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b994a4",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b994c4",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b9953c",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b984c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md#insn-00b984c0) · [`00b98564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md#insn-00b98564) · [`00b984a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9847c.md#insn-00b984a8)
- 新版 [`00b994b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md#insn-00b994b4) · [`00b99558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md#insn-00b99558) · [`00b9949c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99470.md#insn-00b9949c)

~~~diff
- 00b984c0 ["INT_ADD", "register:40f0:8", ["const:b984c0:8", "const:4:8"]]
- 00b984c0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b994b4 ["INT_ADD", "register:40f0:8", ["const:b994b4:8", "const:4:8"]]
+ 00b994b4 ["CALL", null, ["callee:00c5a070:8"]]
- 00b984c0 bytes f8020394
+ 00b994b4 bytes ef020394
- 00b98564 ["INT_ADD", "register:40f0:8", ["const:b98564:8", "const:4:8"]]
- 00b98564 ["CALL", null, ["callee:00c59020:8"]]
+ 00b99558 ["INT_ADD", "register:40f0:8", ["const:b99558:8", "const:4:8"]]
+ 00b99558 ["CALL", null, ["callee:00c59020:8"]]
- 00b98564 bytes bbfe0294
+ 00b99558 bytes b2fe0294
- 00b984a8 ["INT_ADD", "register:40f0:8", ["const:b984a8:8", "const:4:8"]]
- 00b984a8 ["CALL", null, ["callee:00c5d0d0:8"]]
+ 00b9949c ["INT_ADD", "register:40f0:8", ["const:b9949c:8", "const:4:8"]]
+ 00b9949c ["CALL", null, ["callee:00c5d0d0:8"]]
- 00b984a8 bytes 160f0394
+ 00b9949c bytes 0d0f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-808d3cc5e29c54cb7f3bb94d5df98c71"></a>

### [`00b9861c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md) → [`00b99610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md) FUN_00b99610

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b7dee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7dee8.md) [`00b976d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b976d0.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md)
- 新版 呼出元 2件 [`00b7eedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7e/00b7eedc.md) [`00b986c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b986c4.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99644",
      "incomplete_value": false,
      "site": "00b99654",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98650",
      "incomplete_value": false,
      "site": "00b98660",
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
            "const:a89:8"
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
      "definition_site": "00b99664",
      "incomplete_value": false,
      "site": "00b99680",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98670",
      "incomplete_value": false,
      "site": "00b9868c",
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
            "const:715:8"
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
      "definition_site": "00b996dc",
      "incomplete_value": false,
      "site": "00b996f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b986e8",
      "incomplete_value": false,
      "site": "00b98704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b99644",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b99664",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b996dc",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b99644",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b99664",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b996dc",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md#insn-00b98660) · [`00b9868c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md#insn-00b9868c) · [`00b98704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9861c.md#insn-00b98704)
- 新版 [`00b99654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md#insn-00b99654) · [`00b99680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md#insn-00b99680) · [`00b996f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99610.md#insn-00b996f8)

~~~diff
- 00b98660 ["INT_ADD", "register:40f0:8", ["const:b98660:8", "const:4:8"]]
- 00b98660 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b99654 ["INT_ADD", "register:40f0:8", ["const:b99654:8", "const:4:8"]]
+ 00b99654 ["CALL", null, ["callee:00c5a070:8"]]
- 00b98660 bytes 90020394
+ 00b99654 bytes 87020394
- 00b9868c ["INT_ADD", "register:40f0:8", ["const:b9868c:8", "const:4:8"]]
- 00b9868c ["CALL", null, ["callee:00c59020:8"]]
+ 00b99680 ["INT_ADD", "register:40f0:8", ["const:b99680:8", "const:4:8"]]
+ 00b99680 ["CALL", null, ["callee:00c59020:8"]]
- 00b9868c bytes 71fe0294
+ 00b99680 bytes 68fe0294
- 00b98704 ["INT_ADD", "register:40f0:8", ["const:b98704:8", "const:4:8"]]
- 00b98704 ["CALL", null, ["callee:00c59020:8"]]
+ 00b996f8 ["INT_ADD", "register:40f0:8", ["const:b996f8:8", "const:4:8"]]
+ 00b996f8 ["CALL", null, ["callee:00c59020:8"]]
- 00b98704 bytes 53fe0294
+ 00b996f8 bytes 4afe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2330cd8852c8f51cc0400b604f2582ef"></a>

### [`00b987bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md) → [`00b997b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md) FUN_00b997b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b78158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78158.md) [`00b9790c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b9790c.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0c0.md)
- 新版 呼出元 2件 [`00b7914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b7914c.md) [`00b98900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98900.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b997e4",
      "incomplete_value": false,
      "site": "00b997f4",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b987f0",
      "incomplete_value": false,
      "site": "00b98800",
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
            "const:a89:8"
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
      "definition_site": "00b99804",
      "incomplete_value": false,
      "site": "00b99820",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98810",
      "incomplete_value": false,
      "site": "00b9882c",
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
            "const:715:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b997e4",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b99804",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b9987c",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b997e4",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b99804",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b9987c",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md#insn-00b98800) · [`00b9882c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md#insn-00b9882c) · [`00b987e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b987bc.md#insn-00b987e8)
- 新版 [`00b997f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md#insn-00b997f4) · [`00b99820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md#insn-00b99820) · [`00b997dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b997b0.md#insn-00b997dc)

~~~diff
- 00b98800 ["INT_ADD", "register:40f0:8", ["const:b98800:8", "const:4:8"]]
- 00b98800 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b997f4 ["INT_ADD", "register:40f0:8", ["const:b997f4:8", "const:4:8"]]
+ 00b997f4 ["CALL", null, ["callee:00c5a070:8"]]
- 00b98800 bytes 28020394
+ 00b997f4 bytes 1f020394
- 00b9882c ["INT_ADD", "register:40f0:8", ["const:b9882c:8", "const:4:8"]]
- 00b9882c ["CALL", null, ["callee:00c59020:8"]]
+ 00b99820 ["INT_ADD", "register:40f0:8", ["const:b99820:8", "const:4:8"]]
+ 00b99820 ["CALL", null, ["callee:00c59020:8"]]
- 00b9882c bytes 09fe0294
+ 00b99820 bytes 00fe0294
- 00b987e8 ["INT_ADD", "register:40f0:8", ["const:b987e8:8", "const:4:8"]]
- 00b987e8 ["CALL", null, ["callee:00c5d090:8"]]
+ 00b997dc ["INT_ADD", "register:40f0:8", ["const:b997dc:8", "const:4:8"]]
+ 00b997dc ["CALL", null, ["callee:00c5d090:8"]]
- 00b987e8 bytes 360e0394
+ 00b997dc bytes 2d0e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2799c96ed88eb78b5fc3993a515aac7c"></a>

### [`00b9895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md) → [`00b99950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md) FUN_00b99950

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b7e52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e52c.md) [`00b97b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97b40.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0d0.md)
- 新版 呼出元 2件 [`00b7f520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f520.md) [`00b98b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98b34.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99984",
      "incomplete_value": false,
      "site": "00b99994",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98990",
      "incomplete_value": false,
      "site": "00b989a0",
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
            "const:a89:8"
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
      "definition_site": "00b999a4",
      "incomplete_value": false,
      "site": "00b999c0",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b989b0",
      "incomplete_value": false,
      "site": "00b989cc",
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
            "const:715:8"
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
      "definition_site": "00b99a1c",
      "incomplete_value": false,
      "site": "00b99a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98a28",
      "incomplete_value": false,
      "site": "00b98a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b99984",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b999a4",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b99a1c",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b99984",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b999a4",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b99a1c",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b989a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md#insn-00b989a0) · [`00b989cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md#insn-00b989cc) · [`00b98a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b9895c.md#insn-00b98a44)
- 新版 [`00b99994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md#insn-00b99994) · [`00b999c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md#insn-00b999c0) · [`00b99a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99950.md#insn-00b99a38)

~~~diff
- 00b989a0 ["INT_ADD", "register:40f0:8", ["const:b989a0:8", "const:4:8"]]
- 00b989a0 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b99994 ["INT_ADD", "register:40f0:8", ["const:b99994:8", "const:4:8"]]
+ 00b99994 ["CALL", null, ["callee:00c5a070:8"]]
- 00b989a0 bytes c0010394
+ 00b99994 bytes b7010394
- 00b989cc ["INT_ADD", "register:40f0:8", ["const:b989cc:8", "const:4:8"]]
- 00b989cc ["CALL", null, ["callee:00c59020:8"]]
+ 00b999c0 ["INT_ADD", "register:40f0:8", ["const:b999c0:8", "const:4:8"]]
+ 00b999c0 ["CALL", null, ["callee:00c59020:8"]]
- 00b989cc bytes a1fd0294
+ 00b999c0 bytes 98fd0294
- 00b98a44 ["INT_ADD", "register:40f0:8", ["const:b98a44:8", "const:4:8"]]
- 00b98a44 ["CALL", null, ["callee:00c59020:8"]]
+ 00b99a38 ["INT_ADD", "register:40f0:8", ["const:b99a38:8", "const:4:8"]]
+ 00b99a38 ["CALL", null, ["callee:00c59020:8"]]
- 00b98a44 bytes 83fd0294
+ 00b99a38 bytes 7afd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf536a7eb0a4c9f789fd916120a00d43"></a>

### [`00b98afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md) → [`00b99af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md) FUN_00b99af0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b7e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e9f0.md) [`00b97d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b97/00b97d70.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md) [`00c5c0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0e0.md)
- 新版 呼出元 2件 [`00b7f9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b7f/00b7f9e4.md) [`00b98d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b98/00b98d64.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md) [`00c5d0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d0b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b99b24",
      "incomplete_value": false,
      "site": "00b99b34",
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
            "const:b56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98b30",
      "incomplete_value": false,
      "site": "00b98b40",
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
            "const:a89:8"
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
      "definition_site": "00b99b44",
      "incomplete_value": false,
      "site": "00b99b60",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98b50",
      "incomplete_value": false,
      "site": "00b98b6c",
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
            "const:715:8"
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
      "definition_site": "00b99bbc",
      "incomplete_value": false,
      "site": "00b99bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:9b6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98bc8",
      "incomplete_value": false,
      "site": "00b98be4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96c:8"
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
      "00b99b24",
      "PARAM",
      [
        "storage",
        "002a9a89",
        null,
        null
      ]
    ],
    [
      "00b99b44",
      "PARAM",
      [
        "storage",
        "002b0715",
        null,
        null
      ]
    ],
    [
      "00b99bbc",
      "PARAM",
      [
        "storage",
        "002b396c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b99b24",
      "PARAM",
      [
        "storage",
        "002a9b56",
        null,
        null
      ]
    ],
    [
      "00b99b44",
      "PARAM",
      [
        "storage",
        "002b07ec",
        null,
        null
      ]
    ],
    [
      "00b99bbc",
      "PARAM",
      [
        "storage",
        "002b39b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md#insn-00b98b40) · [`00b98b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md#insn-00b98b6c) · [`00b98be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98afc.md#insn-00b98be4)
- 新版 [`00b99b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md#insn-00b99b34) · [`00b99b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md#insn-00b99b60) · [`00b99bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99af0.md#insn-00b99bd8)

~~~diff
- 00b98b40 ["INT_ADD", "register:40f0:8", ["const:b98b40:8", "const:4:8"]]
- 00b98b40 ["CALL", null, ["callee:00c5a070:8"]]
+ 00b99b34 ["INT_ADD", "register:40f0:8", ["const:b99b34:8", "const:4:8"]]
+ 00b99b34 ["CALL", null, ["callee:00c5a070:8"]]
- 00b98b40 bytes 58010394
+ 00b99b34 bytes 4f010394
- 00b98b6c ["INT_ADD", "register:40f0:8", ["const:b98b6c:8", "const:4:8"]]
- 00b98b6c ["CALL", null, ["callee:00c59020:8"]]
+ 00b99b60 ["INT_ADD", "register:40f0:8", ["const:b99b60:8", "const:4:8"]]
+ 00b99b60 ["CALL", null, ["callee:00c59020:8"]]
- 00b98b6c bytes 39fd0294
+ 00b99b60 bytes 30fd0294
- 00b98be4 ["INT_ADD", "register:40f0:8", ["const:b98be4:8", "const:4:8"]]
- 00b98be4 ["CALL", null, ["callee:00c59020:8"]]
+ 00b99bd8 ["INT_ADD", "register:40f0:8", ["const:b99bd8:8", "const:4:8"]]
+ 00b99bd8 ["CALL", null, ["callee:00c59020:8"]]
- 00b98be4 bytes 1bfd0294
+ 00b99bd8 bytes 12fd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-266fb4578077fb68141c63bef5a765fa"></a>

### [`00b98d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d10.md) → [`00b99d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d04.md) FUN_00b99d04

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 70.97% / 新版 70.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99d28",
      "incomplete_value": true,
      "site": "00b99d38",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98d34",
      "incomplete_value": true,
      "site": "00b98d44",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99d2c",
      "incomplete_value": true,
      "site": "00b99d3c",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98d38",
      "incomplete_value": true,
      "site": "00b98d48",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99d40",
      "incomplete_value": true,
      "site": "00b99d40",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98d4c",
      "incomplete_value": true,
      "site": "00b98d4c",
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
            "const:40:8"
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
      "00b99d18",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99d1c",
      "READ",
      [
        "storage",
        "00c9ac90",
        null,
        "pointer"
      ]
    ],
    [
      "00b99d38",
      "DATA",
      [
        "storage",
        "00c90b60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99d18",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99d1c",
      "READ",
      [
        "storage",
        "00c9bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99d38",
      "DATA",
      [
        "storage",
        "00c91b30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d10.md#insn-00b98d1c) · [`00b98d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d10.md#insn-00b98d20) · [`00b98d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d10.md#insn-00b98d24)
- 新版 [`00b99d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d04.md#insn-00b99d10) · [`00b99d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d04.md#insn-00b99d14) · [`00b99d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d04.md#insn-00b99d18)

~~~diff
- 00b98d1c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00b99d10 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b98d1c bytes 080800d0
+ 00b99d10 bytes 080800d0
- 00b98d20 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00b99d14 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b98d20 bytes 090800d0
+ 00b99d14 bytes 090800d0
- 00b98d24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
- 00b98d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99d18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
+ 00b99d18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98d24 bytes 087546f9
+ 00b99d18 bytes 085d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae83dea285dbe018ec687354c04c8c85"></a>

### [`00b98d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d8c.md) → [`00b99d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d80.md) FUN_00b99d80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99da4",
      "incomplete_value": true,
      "site": "00b99da4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98db0",
      "incomplete_value": true,
      "site": "00b98db0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99da8",
      "incomplete_value": true,
      "site": "00b99da8",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98db4",
      "incomplete_value": true,
      "site": "00b98db4",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99dc0",
      "incomplete_value": true,
      "site": "00b99dc0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98dcc",
      "incomplete_value": true,
      "site": "00b98dcc",
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
            "const:40:8"
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
      "00b99d90",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99da4",
      "DATA",
      [
        "storage",
        "00c90b60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99da8",
      "DATA",
      [
        "storage",
        "00c90bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99d90",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99da4",
      "DATA",
      [
        "storage",
        "00c91b30",
        null,
        "pointer"
      ]
    ],
    [
      "00b99da8",
      "DATA",
      [
        "storage",
        "00c91b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d8c.md#insn-00b98d98) · [`00b98d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d8c.md#insn-00b98d9c) · [`00b98db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98d8c.md#insn-00b98db8)
- 新版 [`00b99d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d80.md#insn-00b99d8c) · [`00b99d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d80.md#insn-00b99d90) · [`00b99dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99d80.md#insn-00b99dac)

~~~diff
- 00b98d98 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00b99d8c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b98d98 bytes 080800d0
+ 00b99d8c bytes 080800d0
- 00b98d9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
- 00b98d9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99d90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
+ 00b99d90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98d9c bytes 087546f9
+ 00b99d90 bytes 085d46f9
- 00b98db8 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00b99dac ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00b98db8 bytes 0a0800d0
+ 00b99dac bytes 0a0800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ecb4408ffb1841019acbd65b9218d0f"></a>

### [`00b98e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e04.md) → [`00b99df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99df8.md) FUN_00b99df8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99e1c",
      "incomplete_value": true,
      "site": "00b99e1c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98e28",
      "incomplete_value": true,
      "site": "00b98e28",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99e20",
      "incomplete_value": true,
      "site": "00b99e20",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98e2c",
      "incomplete_value": true,
      "site": "00b98e2c",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99e38",
      "incomplete_value": true,
      "site": "00b99e38",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98e44",
      "incomplete_value": true,
      "site": "00b98e44",
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
            "const:40:8"
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
      "00b99e08",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99e1c",
      "DATA",
      [
        "storage",
        "00c90b60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99e20",
      "DATA",
      [
        "storage",
        "00c90bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99e08",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99e1c",
      "DATA",
      [
        "storage",
        "00c91b30",
        null,
        "pointer"
      ]
    ],
    [
      "00b99e20",
      "DATA",
      [
        "storage",
        "00c91b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e04.md#insn-00b98e10) · [`00b98e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e04.md#insn-00b98e14) · [`00b98e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e04.md#insn-00b98e30)
- 新版 [`00b99e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99df8.md#insn-00b99e04) · [`00b99e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99df8.md#insn-00b99e08) · [`00b99e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99df8.md#insn-00b99e24)

~~~diff
- 00b98e10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00b99e04 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b98e10 bytes 080800d0
+ 00b99e04 bytes 080800d0
- 00b98e14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
- 00b98e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99e08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
+ 00b99e08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98e14 bytes 087546f9
+ 00b99e08 bytes 085d46f9
- 00b98e30 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00b99e24 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00b98e30 bytes 0a0800d0
+ 00b99e24 bytes 0a0800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc53b15efa737b9a871fce441742e77a"></a>

### [`00b98e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e84.md) → [`00b99e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99e78.md) FUN_00b99e78

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99e98",
      "incomplete_value": true,
      "site": "00b99ea4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98ea4",
      "incomplete_value": true,
      "site": "00b98eb0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99ea8",
      "incomplete_value": true,
      "site": "00b99ea8",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98eb4",
      "incomplete_value": true,
      "site": "00b98eb4",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99ec0",
      "incomplete_value": true,
      "site": "00b99ec0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98ecc",
      "incomplete_value": true,
      "site": "00b98ecc",
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
            "const:40:8"
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
      "00b99e90",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ea4",
      "DATA",
      [
        "storage",
        "00c90b60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ea8",
      "DATA",
      [
        "storage",
        "00c90bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99e90",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ea4",
      "DATA",
      [
        "storage",
        "00c91b30",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ea8",
      "DATA",
      [
        "storage",
        "00c91b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e84.md#insn-00b98e94) · [`00b98e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e84.md#insn-00b98e9c) · [`00b98eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98e84.md#insn-00b98eb8)
- 新版 [`00b99e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99e78.md#insn-00b99e88) · [`00b99e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99e78.md#insn-00b99e90)

~~~diff
- 00b98e94 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00b99e88 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b98e94 bytes 090800d0
+ 00b99e88 bytes 090800d0
- 00b98e9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ce8:8"]]
- 00b98e9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99e90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cb8:8"]]
+ 00b99e90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98e9c bytes 297546f9
+ 00b99e90 bytes 295d46f9
- 00b98eb8 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00b98eb8 bytes 0a0800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6cd95213f895760e4382633f9a2daf8"></a>

### [`00b98f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f04.md) → [`00b99ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99ef8.md) FUN_00b99ef8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99f18",
      "incomplete_value": true,
      "site": "00b99f24",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98f24",
      "incomplete_value": true,
      "site": "00b98f30",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99f28",
      "incomplete_value": true,
      "site": "00b99f28",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98f34",
      "incomplete_value": true,
      "site": "00b98f34",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99f40",
      "incomplete_value": true,
      "site": "00b99f40",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98f4c",
      "incomplete_value": true,
      "site": "00b98f4c",
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
            "const:40:8"
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
      "00b99f10",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f24",
      "DATA",
      [
        "storage",
        "00c90b60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f28",
      "DATA",
      [
        "storage",
        "00c90bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99f10",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f24",
      "DATA",
      [
        "storage",
        "00c91b30",
        null,
        "pointer"
      ]
    ],
    [
      "00b99f28",
      "DATA",
      [
        "storage",
        "00c91b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f04.md#insn-00b98f14) · [`00b98f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f04.md#insn-00b98f1c) · [`00b98f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f04.md#insn-00b98f38)
- 新版 [`00b99f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99ef8.md#insn-00b99f08) · [`00b99f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99ef8.md#insn-00b99f10)

~~~diff
- 00b98f14 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00b99f08 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b98f14 bytes 090800d0
+ 00b99f08 bytes 090800d0
- 00b98f1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ce8:8"]]
- 00b98f1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99f10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cb8:8"]]
+ 00b99f10 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98f1c bytes 297546f9
+ 00b99f10 bytes 295d46f9
- 00b98f38 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00b98f38 bytes 0a0800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b5479929c53cbb93eb758e7d585190f"></a>

### [`00b98f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f8c.md) → [`00b99f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99f80.md) FUN_00b99f80

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99f9c",
      "incomplete_value": true,
      "site": "00b99fa0",
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
      "definition_site": "00b98fa8",
      "incomplete_value": true,
      "site": "00b98fac",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99fbc",
      "incomplete_value": true,
      "site": "00b99fbc",
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
      "definition_site": "00b98fc8",
      "incomplete_value": true,
      "site": "00b98fc8",
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
      "00b99f94",
      "READ",
      [
        "storage",
        "00c9ac90",
        null,
        "pointer"
      ]
    ],
    [
      "00b99fa0",
      "DATA",
      [
        "storage",
        "00c90cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b99fb4",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99f94",
      "READ",
      [
        "storage",
        "00c9bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99fa0",
      "DATA",
      [
        "storage",
        "00c91ca8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b99fb4",
      "READ",
      [
        "storage",
        "00c9c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f8c.md#insn-00b98f98) · [`00b98fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f8c.md#insn-00b98fa0) · [`00b98fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98f8c.md#insn-00b98fb8)
- 新版 [`00b99f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99f80.md#insn-00b99f8c) · [`00b99f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99f80.md#insn-00b99f94) · [`00b99fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99f80.md#insn-00b99fac)

~~~diff
- 00b98f98 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00b99f8c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b98f98 bytes 090800d0
+ 00b99f8c bytes 090800d0
- 00b98fa0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
- 00b98fa0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99f94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c60:8"]]
+ 00b99f94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98fa0 bytes 294946f9
+ 00b99f94 bytes 293146f9
- 00b98fb8 ["INT_ADD", "register:40f0:8", ["const:b98fb8:8", "const:4:8"]]
- 00b98fb8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b99fac ["INT_ADD", "register:40f0:8", ["const:b99fac:8", "const:4:8"]]
+ 00b99fac ["CALL", null, ["callee:00c58f50:8"]]
- 00b98fb8 bytes f2fb0294
+ 00b99fac bytes e9fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95afa2a1251d0bd53d495ee049564c56"></a>

### [`00b98fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98fdc.md) → [`00b99fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99fd0.md) FUN_00b99fd0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b99fec",
      "incomplete_value": true,
      "site": "00b99ff0",
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
      "definition_site": "00b98ff8",
      "incomplete_value": true,
      "site": "00b98ffc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9a010",
      "incomplete_value": true,
      "site": "00b9a010",
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
      "definition_site": "00b9901c",
      "incomplete_value": true,
      "site": "00b9901c",
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
      "00b99fe4",
      "READ",
      [
        "storage",
        "00c9ac90",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ff0",
      "DATA",
      [
        "storage",
        "00c90cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b9a004",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99fe4",
      "READ",
      [
        "storage",
        "00c9bc60",
        null,
        "pointer"
      ]
    ],
    [
      "00b99ff0",
      "DATA",
      [
        "storage",
        "00c91ca8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b9a004",
      "READ",
      [
        "storage",
        "00c9c8e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98fdc.md#insn-00b98fe8) · [`00b98ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98fdc.md#insn-00b98ff0) · [`00b99008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b98/00b98fdc.md#insn-00b99008)
- 新版 [`00b99fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99fd0.md#insn-00b99fdc) · [`00b99fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99fd0.md#insn-00b99fe4) · [`00b99ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b99/00b99fd0.md#insn-00b99ffc)

~~~diff
- 00b98fe8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00b99fdc ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b98fe8 bytes 090800d0
+ 00b99fdc bytes 090800d0
- 00b98ff0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
- 00b98ff0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b99fe4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c60:8"]]
+ 00b99fe4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b98ff0 bytes 294946f9
+ 00b99fe4 bytes 293146f9
- 00b99008 ["INT_ADD", "register:40f0:8", ["const:b99008:8", "const:4:8"]]
- 00b99008 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b99ffc ["INT_ADD", "register:40f0:8", ["const:b99ffc:8", "const:4:8"]]
+ 00b99ffc ["CALL", null, ["callee:00c58f50:8"]]
- 00b99008 bytes defb0294
+ 00b99ffc bytes d5fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

