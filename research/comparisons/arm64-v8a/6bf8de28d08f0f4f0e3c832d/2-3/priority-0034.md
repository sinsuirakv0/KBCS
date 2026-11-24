# v16.0.2 → v16.0.3 · 最優先の変更候補 (34)

[一覧の目次](README.md)

<a id="compare-b4c2ab328de0c9dbd64e3873b71b5c20"></a>

### [`006b8fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8fa4.md) → [`006b9354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b9/006b9354.md) FUN_006b9354

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8cb0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`006b9060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b9/006b9060.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "006b9360",
      "incomplete_value": false,
      "site": "006b9364",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8fb0",
      "incomplete_value": false,
      "site": "006b8fb4",
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
            "const:f8c:8"
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
      "006b9360",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b9360",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8fa4.md#insn-006b8fb4) · [`006b8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8fa4.md#insn-006b8fac) · [`006b8fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8fa4.md#insn-006b8fb0)
- 新版 [`006b9364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b9/006b9354.md#insn-006b9364) · [`006b935c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b9/006b9354.md#insn-006b935c) · [`006b9360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b9/006b9354.md#insn-006b9360)

~~~diff
- 006b8fb4 ["INT_ADD", "register:40f0:8", ["const:6b8fb4:8", "const:4:8"]]
- 006b8fb4 ["CALL", null, ["callee:0043bad8:8"]]
+ 006b9364 ["INT_ADD", "register:40f0:8", ["const:6b9364:8", "const:4:8"]]
+ 006b9364 ["CALL", null, ["callee:0043bad8:8"]]
- 006b8fb4 bytes 010af697
+ 006b9364 bytes dd09f697
- 006b8fac ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 006b935c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 006b8fac bytes e0dffff0
+ 006b935c bytes e0dffff0
- 006b8fb0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 006b8fb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b8fb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b8fb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006b9360 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 006b9360 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006b9360 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006b9360 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b8fb0 bytes 00303e91
+ 006b9360 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10eebfdfc1216ef499d175c37692a519"></a>

### [`006bb3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb3bc.md) → [`006bb76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bb76c.md) _INIT_106

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb7a8",
      "incomplete_value": true,
      "site": "006bb7c4",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb3f8",
      "incomplete_value": true,
      "site": "006bb414",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb828",
      "incomplete_value": true,
      "site": "006bb844",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb478",
      "incomplete_value": true,
      "site": "006bb494",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006bb98c",
      "incomplete_value": false,
      "site": "006bb9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43b000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb5dc",
      "incomplete_value": false,
      "site": "006bb5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "006bb7a8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "006bb7cc",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "006bb7ec",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006bb7a8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "006bb7cc",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "006bb7ec",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bb5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb3bc.md#insn-006bb5f0) · [`006bb3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb3bc.md#insn-006bb3e4) · [`006bb3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb3bc.md#insn-006bb3e8)
- 新版 [`006bb9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bb76c.md#insn-006bb9a0) · [`006bb794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bb76c.md#insn-006bb794) · [`006bb798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bb76c.md#insn-006bb798)

~~~diff
- 006bb5f0 ["INT_ADD", "register:40f0:8", ["const:6bb5f0:8", "const:4:8"]]
- 006bb5f0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006bb9a0 ["INT_ADD", "register:40f0:8", ["const:6bb9a0:8", "const:4:8"]]
+ 006bb9a0 ["CALL", null, ["callee:00c58ed0:8"]]
- 006bb5f0 bytes 44721694
+ 006bb9a0 bytes 4c751694
- 006bb3e4 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 006bb794 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 006bb3e4 bytes 732f0090
+ 006bb794 bytes 732f00b0
- 006bb3e8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 006bb3e8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006bb3e8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006bb3e8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006bb798 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 006bb798 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006bb798 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006bb798 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006bb3e8 bytes 73c22091
+ 006bb798 bytes 73c21f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2904bd5e69982c49d9aeab48feaf950"></a>

### [`006bb960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb960.md) → [`006bbd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bbd10.md) _INIT_107

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bbd4c",
      "incomplete_value": true,
      "site": "006bbd68",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb99c",
      "incomplete_value": true,
      "site": "006bb9b8",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bbd70",
      "incomplete_value": true,
      "site": "006bbd8c",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb9c0",
      "incomplete_value": true,
      "site": "006bb9dc",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "006bbd90",
      "incomplete_value": true,
      "site": "006bbdac",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb9e0",
      "incomplete_value": true,
      "site": "006bb9fc",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
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
      "006bbd4c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "006bbd70",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "006bbd90",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006bbd4c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "006bbd70",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "006bbd90",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bbac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb960.md#insn-006bbac0) · [`006bbb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb960.md#insn-006bbb94) · [`006bb988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb960.md#insn-006bb988)
- 新版 [`006bbe70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bbd10.md#insn-006bbe70) · [`006bbf44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bbd10.md#insn-006bbf44) · [`006bbd38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bb/006bbd10.md#insn-006bbd38)

~~~diff
- 006bbac0 ["INT_ADD", "register:40f0:8", ["const:6bbac0:8", "const:4:8"]]
- 006bbac0 ["CALL", null, ["callee:0043bb58:8"]]
+ 006bbe70 ["INT_ADD", "register:40f0:8", ["const:6bbe70:8", "const:4:8"]]
+ 006bbe70 ["CALL", null, ["callee:0043bb58:8"]]
- 006bbac0 bytes 5efff597
+ 006bbe70 bytes 3afff597
- 006bbb94 ["INT_ADD", "register:40f0:8", ["const:6bbb94:8", "const:4:8"]]
- 006bbb94 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006bbf44 ["INT_ADD", "register:40f0:8", ["const:6bbf44:8", "const:4:8"]]
+ 006bbf44 ["CALL", null, ["callee:00c58ed0:8"]]
- 006bbb94 bytes db701694
+ 006bbf44 bytes e3731694
- 006bb988 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 006bbd38 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 006bb988 bytes 732f0090
+ 006bbd38 bytes 732f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da73bbb3da391a2e0046990b26f2170"></a>

### [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) → [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) FUN_006bc0a0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00678920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00678/00678920.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0092491c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00924/0092491c.md) · 呼出先 105件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md)
- 新版 呼出元 4件 [`00678cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00678/00678cd0.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) [`009258c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00925/009258c8.md) · 呼出先 105件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0043eb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043eb88.md) [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 23件, `store_destination` 7件, `store_value` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bcfc0",
      "incomplete_value": true,
      "site": "006bcfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bcc10",
      "incomplete_value": true,
      "site": "006bcc28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 136,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bd940",
      "incomplete_value": true,
      "site": "006bd94c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bd590",
      "incomplete_value": true,
      "site": "006bd59c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 224,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006be278",
      "incomplete_value": true,
      "site": "006be284",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bdec8",
      "incomplete_value": true,
      "site": "006bded4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 345,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bc234",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "qword"
      ]
    ],
    [
      "006bc23c",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "006bc24c",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006bc234",
      "DATA",
      [
        "storage",
        "0039badc",
        "fde_0039badc",
        "dword"
      ]
    ],
    [
      "006bc23c",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[11]"
      ]
    ],
    [
      "006bc24c",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bbf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md#insn-006bbf8c) · [`006bc4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md#insn-006bc4d8) · [`006bc560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md#insn-006bc560)
- 新版 [`006bc33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md#insn-006bc33c) · [`006bc888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md#insn-006bc888) · [`006bc910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md#insn-006bc910)

~~~diff
- 006bbf8c ["INT_ADD", "register:40f0:8", ["const:6bbf8c:8", "const:4:8"]]
- 006bbf8c ["CALL", null, ["ram:47ad34:8"]]
+ 006bc33c ["INT_ADD", "register:40f0:8", ["const:6bc33c:8", "const:4:8"]]
+ 006bc33c ["CALL", null, ["ram:47b054:8"]]
- 006bbf8c bytes 6afbf697
+ 006bc33c bytes 46fbf697
- 006bc4d8 ["INT_ADD", "register:40f0:8", ["const:6bc4d8:8", "const:4:8"]]
- 006bc4d8 ["CALL", null, ["ram:47ad34:8"]]
+ 006bc888 ["INT_ADD", "register:40f0:8", ["const:6bc888:8", "const:4:8"]]
+ 006bc888 ["CALL", null, ["ram:47b054:8"]]
- 006bc4d8 bytes 17faf697
+ 006bc888 bytes f3f9f697
- 006bc560 ["INT_ADD", "register:40f0:8", ["const:6bc560:8", "const:4:8"]]
- 006bc560 ["CALL", null, ["callee:008b8a14:8"]]
+ 006bc910 ["INT_ADD", "register:40f0:8", ["const:6bc910:8", "const:4:8"]]
+ 006bc910 ["CALL", null, ["callee:008b8a14:8"]]
- 006bc560 bytes 42ed0794
+ 006bc910 bytes 41f00794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eab52f89ac3477c5b71feb9ca88753b"></a>

### [`006bea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bea44.md) → [`006bedf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006be/006bedf4.md) FUN_006bedf4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 5件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006c0100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0100.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 5件 [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`006c04b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c04b0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 8件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bee04",
      "incomplete_value": false,
      "site": "006bee04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bea54",
      "incomplete_value": false,
      "site": "006bea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bee64",
      "incomplete_value": false,
      "site": "006bee64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
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
      "definition_site": "006beab4",
      "incomplete_value": false,
      "site": "006beab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bee68",
      "incomplete_value": false,
      "site": "006bee68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006beab8",
      "incomplete_value": false,
      "site": "006beab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "006bee00",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee04",
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee20",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006bee00",
      "READ",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee04",
      "WRITE",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee20",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bea54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bea44.md#insn-006bea54) · [`006bea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bea44.md#insn-006bea90) · [`006beacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bea44.md#insn-006beacc)
- 新版 [`006bee04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006be/006bedf4.md#insn-006bee04) · [`006bee40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006be/006bedf4.md#insn-006bee40) · [`006bee7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006be/006bedf4.md#insn-006bee7c)

~~~diff
- 006bea54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 006bea54 ["COPY", "tmp:1:8", ["const:0:8"]]
- 006bea54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 006bee04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a28:8"]]
+ 006bee04 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 006bee04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 006bea54 bytes 1f3505f9
+ 006bee04 bytes 1f1505f9
- 006bea90 ["INT_ADD", "register:40f0:8", ["const:6bea90:8", "const:4:8"]]
- 006bea90 ["CALL", null, ["callee:00c58ef0:8"]]
+ 006bee40 ["INT_ADD", "register:40f0:8", ["const:6bee40:8", "const:4:8"]]
+ 006bee40 ["CALL", null, ["callee:00c58ef0:8"]]
- 006bea90 bytes 24651694
+ 006bee40 bytes 2c681694
- 006beacc ["INT_ADD", "register:40f0:8", ["const:6beacc:8", "const:4:8"]]
- 006beacc ["CALL", null, ["callee:00c58ed0:8"]]
+ 006bee7c ["INT_ADD", "register:40f0:8", ["const:6bee7c:8", "const:4:8"]]
+ 006bee7c ["CALL", null, ["callee:00c58ed0:8"]]
- 006beacc bytes 0d651694
+ 006bee7c bytes 15681694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f38088da619fc9bb79a2e0cbbb2db8f5"></a>

### [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) → [`006bf164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md) FUN_006bf164

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) · 呼出先 24件 [`005e48ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e48ec.md) [`005e4e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4e58.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md) [`006c0074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0074.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)
- 新版 呼出元 1件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) · 呼出先 24件 [`005e4c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e4/005e4c9c.md) [`005e5208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e5/005e5208.md) [`005e8588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e8/005e8588.md) [`006c0424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0424.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 19件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf1e4",
      "incomplete_value": false,
      "site": "006bf1ec",
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
            "const:b6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bee34",
      "incomplete_value": false,
      "site": "006bee3c",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf244",
      "incomplete_value": false,
      "site": "006bf248",
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
            "const:ec3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bee94",
      "incomplete_value": false,
      "site": "006bee98",
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
            "const:e79:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf28c",
      "incomplete_value": false,
      "site": "006bf294",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006beedc",
      "incomplete_value": false,
      "site": "006beee4",
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
            "const:a5e:8"
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
      "006bf1ec",
      "DATA",
      [
        "storage",
        "002aea98",
        null,
        "string"
      ]
    ],
    [
      "006bf218",
      "DATA",
      [
        "storage",
        "002b75ae",
        null,
        "string"
      ]
    ],
    [
      "006bf248",
      "DATA",
      [
        "storage",
        "002b1e79",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006bf1ec",
      "DATA",
      [
        "storage",
        "002aeb6f",
        null,
        "string"
      ]
    ],
    [
      "006bf218",
      "DATA",
      [
        "storage",
        "002b767d",
        null,
        "string"
      ]
    ],
    [
      "006bf248",
      "DATA",
      [
        "storage",
        "002b1ec3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md#insn-006bee5c) · [`006bee88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md#insn-006bee88) · [`006bef2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md#insn-006bef2c)
- 新版 [`006bf20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md#insn-006bf20c) · [`006bf238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md#insn-006bf238) · [`006bf2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md#insn-006bf2dc)

~~~diff
- 006bee5c ["COPY", "tmp:0:8", ["const:5ae:8"]]
- 006bee5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006bee5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006bee5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006bf20c ["COPY", "tmp:0:8", ["const:67d:8"]]
+ 006bf20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006bf20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006bf20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006bee5c bytes 08b91691
+ 006bf20c bytes 08f51991
- 006bee88 ["INT_ADD", "register:40f0:8", ["const:6bee88:8", "const:4:8"]]
- 006bee88 ["CALL", null, ["callee:00803b14:8"]]
+ 006bf238 ["INT_ADD", "register:40f0:8", ["const:6bf238:8", "const:4:8"]]
+ 006bf238 ["CALL", null, ["callee:00803b14:8"]]
- 006bee88 bytes 4a0f0594
+ 006bf238 bytes 37120594
- 006bef2c ["INT_ADD", "register:40f0:8", ["const:6bef2c:8", "const:4:8"]]
- 006bef2c ["CALL", null, ["callee:00803c64:8"]]
+ 006bf2dc ["INT_ADD", "register:40f0:8", ["const:6bf2dc:8", "const:4:8"]]
+ 006bf2dc ["CALL", null, ["callee:00803c64:8"]]
- 006bef2c bytes 750f0594
+ 006bf2dc bytes 62120594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd67c3dc44c8d74236dc0a8ad7438e62"></a>

### [`006bf8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md) → [`006bfc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc94.md) FUN_006bfc94

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00679840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00679/00679840.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) [`00925a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00925/00925a24.md) · 呼出先 10件 [`00467b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b3c.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f5c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`0046803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/0046803c.md)
- 新版 呼出元 4件 [`00679bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00679/00679bf0.md) [`007082e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/007082e8.md) [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) [`009269d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00926/009269d0.md) · 呼出先 10件 [`00467e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e5c.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`0046827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/0046827c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`0046835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/0046835c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.14% / 新版 98.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006bfe00",
      "incomplete_value": false,
      "site": "006bfe04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bfa50",
      "incomplete_value": false,
      "site": "006bfa54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "006bfe70",
      "incomplete_value": false,
      "site": "006bfe74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bfac0",
      "incomplete_value": false,
      "site": "006bfac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006bfed0",
      "incomplete_value": false,
      "site": "006bfed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bfb20",
      "incomplete_value": false,
      "site": "006bfb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bfccc",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "006bfce0",
      "READ",
      [
        "storage",
        "00ca4d94",
        null,
        "undefined4"
      ]
    ],
    [
      "006bfe00",
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006bfccc",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "006bfce0",
      "READ",
      [
        "storage",
        "00ca5d54",
        null,
        "undefined4"
      ]
    ],
    [
      "006bfe00",
      "PARAM",
      [
        "storage",
        "00ca5d30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bfa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md#insn-006bfa54) · [`006bfac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md#insn-006bfac4) · [`006bfb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md#insn-006bfb24)
- 新版 [`006bfe04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc94.md#insn-006bfe04) · [`006bfe74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc94.md#insn-006bfe74) · [`006bfed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bfc94.md#insn-006bfed4)

~~~diff
- 006bfa54 ["INT_ADD", "register:40f0:8", ["const:6bfa54:8", "const:4:8"]]
- 006bfa54 ["CALL", null, ["callee:0046ce6c:8"]]
+ 006bfe04 ["INT_ADD", "register:40f0:8", ["const:6bfe04:8", "const:4:8"]]
+ 006bfe04 ["CALL", null, ["callee:0046ce6c:8"]]
- 006bfa54 bytes 3eb4f697
+ 006bfe04 bytes 1ab4f697
- 006bfac4 ["INT_ADD", "register:40f0:8", ["const:6bfac4:8", "const:4:8"]]
- 006bfac4 ["CALL", null, ["callee:0046ce6c:8"]]
+ 006bfe74 ["INT_ADD", "register:40f0:8", ["const:6bfe74:8", "const:4:8"]]
+ 006bfe74 ["CALL", null, ["callee:0046ce6c:8"]]
- 006bfac4 bytes 22b4f697
+ 006bfe74 bytes feb3f697
- 006bfb24 ["INT_ADD", "register:40f0:8", ["const:6bfb24:8", "const:4:8"]]
- 006bfb24 ["CALL", null, ["callee:0046ce6c:8"]]
+ 006bfed4 ["INT_ADD", "register:40f0:8", ["const:6bfed4:8", "const:4:8"]]
+ 006bfed4 ["CALL", null, ["callee:0046ce6c:8"]]
- 006bfb24 bytes 0ab4f697
+ 006bfed4 bytes e6b3f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197499ae3cb9aef60bcf1aec157f0d57"></a>

### [`006c03c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03c8.md) → [`006c0778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0778.md) FUN_006c0778

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c078c",
      "incomplete_value": false,
      "site": "006c0790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c03dc",
      "incomplete_value": false,
      "site": "006c03e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "006c0790",
      "DATA",
      [
        "storage",
        "00c762f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c0790",
      "DATA",
      [
        "storage",
        "00c772c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c03d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03c8.md#insn-006c03d4) · [`006c03d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03c8.md#insn-006c03d8) · [`006c03dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03c8.md#insn-006c03dc)
- 新版 [`006c0784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0778.md#insn-006c0784) · [`006c0788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0778.md#insn-006c0788) · [`006c078c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0778.md#insn-006c078c)

~~~diff
- 006c03d4 ["INT_ADD", "register:40f0:8", ["const:6c03d4:8", "const:4:8"]]
- 006c03d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006c0784 ["INT_ADD", "register:40f0:8", ["const:6c0784:8", "const:4:8"]]
+ 006c0784 ["CALL", null, ["callee:00c58f30:8"]]
- 006c03d4 bytes e35e1694
+ 006c0784 bytes eb611694
- 006c03d8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006c0788 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006c03d8 bytes a82d00d0
+ 006c0788 bytes a82d00f0
- 006c03dc ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 006c03dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c03dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c03dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c078c ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 006c078c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c078c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c078c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c03dc bytes 08c10b91
+ 006c078c bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b51f535783b12a81a9ae1edce189620"></a>

### [`006c0404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0404.md) → [`006c07b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c07b4.md) FUN_006c07b4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.28% / 新版 94.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c088c",
      "incomplete_value": true,
      "site": "006c089c",
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
                "const:3c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c04dc",
      "incomplete_value": true,
      "site": "006c04ec",
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
                "const:383:8"
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
      "definition_site": "006c08a0",
      "incomplete_value": true,
      "site": "006c08a0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "006c04f0",
      "incomplete_value": true,
      "site": "006c04f0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c093c",
      "incomplete_value": true,
      "site": "006c094c",
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
                "const:3c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c058c",
      "incomplete_value": true,
      "site": "006c059c",
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
                "const:383:8"
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
      "006c0800",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "006c0818",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ],
    [
      "006c086c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006c0800",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[11]"
      ]
    ],
    [
      "006c0818",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "byte[23]"
      ]
    ],
    [
      "006c086c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c04bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0404.md#insn-006c04bc) · [`006c05f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0404.md#insn-006c05f0) · [`006c0618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0404.md#insn-006c0618)
- 新版 [`006c086c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c07b4.md#insn-006c086c) · [`006c09a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c07b4.md#insn-006c09a0) · [`006c09c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c07b4.md#insn-006c09c8)

~~~diff
- 006c04bc ["INT_ADD", "register:40f0:8", ["const:6c04bc:8", "const:4:8"]]
- 006c04bc ["CALL", null, ["ram:47ad34:8"]]
+ 006c086c ["INT_ADD", "register:40f0:8", ["const:6c086c:8", "const:4:8"]]
+ 006c086c ["CALL", null, ["ram:47b054:8"]]
- 006c04bc bytes 1eeaf697
+ 006c086c bytes fae9f697
- 006c05f0 ["INT_ADD", "register:40f0:8", ["const:6c05f0:8", "const:4:8"]]
- 006c05f0 ["CALL", null, ["ram:48cd38:8"]]
+ 006c09a0 ["INT_ADD", "register:40f0:8", ["const:6c09a0:8", "const:4:8"]]
+ 006c09a0 ["CALL", null, ["ram:48d058:8"]]
- 006c05f0 bytes d231f797
+ 006c09a0 bytes ae31f797
- 006c0618 ["INT_ADD", "register:40f0:8", ["const:6c0618:8", "const:4:8"]]
- 006c0618 ["CALL", null, ["callee:00c59000:8"]]
+ 006c09c8 ["INT_ADD", "register:40f0:8", ["const:6c09c8:8", "const:4:8"]]
+ 006c09c8 ["CALL", null, ["callee:00c59000:8"]]
- 006c0618 bytes 865e1694
+ 006c09c8 bytes 8e611694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506a57c21614203a02fe75f6f5aa9c0f"></a>

### [`006c09d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c09d4.md) → [`006c0d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0d84.md) _INIT_108

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0dc0",
      "incomplete_value": true,
      "site": "006c0ddc",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0a10",
      "incomplete_value": true,
      "site": "006c0a2c",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0de4",
      "incomplete_value": true,
      "site": "006c0e00",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0a34",
      "incomplete_value": true,
      "site": "006c0a50",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "006c0e04",
      "incomplete_value": true,
      "site": "006c0e20",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c0a54",
      "incomplete_value": true,
      "site": "006c0a70",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
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
      "006c0dc0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "006c0de4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "006c0e04",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c0dc0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "006c0de4",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "006c0e04",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c0b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c09d4.md#insn-006c0b34) · [`006c0c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c09d4.md#insn-006c0c08) · [`006c09fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c09d4.md#insn-006c09fc)
- 新版 [`006c0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0d84.md#insn-006c0ee4) · [`006c0fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0d84.md#insn-006c0fb8) · [`006c0dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c0/006c0d84.md#insn-006c0dac)

~~~diff
- 006c0b34 ["INT_ADD", "register:40f0:8", ["const:6c0b34:8", "const:4:8"]]
- 006c0b34 ["CALL", null, ["callee:0043bb58:8"]]
+ 006c0ee4 ["INT_ADD", "register:40f0:8", ["const:6c0ee4:8", "const:4:8"]]
+ 006c0ee4 ["CALL", null, ["callee:0043bb58:8"]]
- 006c0b34 bytes 41ebf597
+ 006c0ee4 bytes 1debf597
- 006c0c08 ["INT_ADD", "register:40f0:8", ["const:6c0c08:8", "const:4:8"]]
- 006c0c08 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006c0fb8 ["INT_ADD", "register:40f0:8", ["const:6c0fb8:8", "const:4:8"]]
+ 006c0fb8 ["CALL", null, ["callee:00c58ed0:8"]]
- 006c0c08 bytes be5c1694
+ 006c0fb8 bytes c65f1694
- 006c09fc ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 006c0dac ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 006c09fc bytes 332f00f0
+ 006c0dac bytes 532f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952110598ed45e875627b54040fd9fd3"></a>

### [`006c2070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c2/006c2070.md) → [`006c2420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2420.md) FUN_006c2420

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) [`008f5c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5c38.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006c1de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1de0.md) [`006c1e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1e6c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 6件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) [`008f6be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f6be4.md) [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) · 呼出先 10件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006c2190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2190.md) [`006c221c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c221c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.25% / 新版 99.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c2530",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c2180",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c26e4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c2334",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c2530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006c26e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006c2530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006c26e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c2180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c2/006c2070.md#insn-006c2180) · [`006c2334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c2/006c2070.md#insn-006c2334) · [`006c2110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c2/006c2070.md#insn-006c2110)
- 新版 [`006c2530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2420.md#insn-006c2530) · [`006c26e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2420.md#insn-006c26e4) · [`006c24c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2420.md#insn-006c24c0)

~~~diff
- 006c2180 ["INT_ADD", "register:40f0:8", ["const:6c2180:8", "const:4:8"]]
- 006c2180 ["CALL", null, ["ram:47ad34:8"]]
+ 006c2530 ["INT_ADD", "register:40f0:8", ["const:6c2530:8", "const:4:8"]]
+ 006c2530 ["CALL", null, ["ram:47b054:8"]]
- 006c2180 bytes ede2f697
+ 006c2530 bytes c9e2f697
- 006c2334 ["INT_ADD", "register:40f0:8", ["const:6c2334:8", "const:4:8"]]
- 006c2334 ["CALL", null, ["ram:47ad34:8"]]
+ 006c26e4 ["INT_ADD", "register:40f0:8", ["const:6c26e4:8", "const:4:8"]]
+ 006c26e4 ["CALL", null, ["ram:47b054:8"]]
- 006c2334 bytes 80e2f697
+ 006c26e4 bytes 5ce2f697
- 006c2110 ["INT_ADD", "register:40f0:8", ["const:6c2110:8", "const:4:8"]]
- 006c2110 ["CALL", null, ["callee:008524fc:8"]]
+ 006c24c0 ["INT_ADD", "register:40f0:8", ["const:6c24c0:8", "const:4:8"]]
+ 006c24c0 ["CALL", null, ["callee:008524fc:8"]]
- 006c2110 bytes 103d0694
+ 006c24c0 bytes 0f400694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10f8d9113cdd6a6295646a4fbaee62a2"></a>

### [`006c32d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md) → [`006c3680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md) FUN_006c3680

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006c3114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3114.md) [`006c3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3148.md) [`006c3170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3170.md) [`006c320c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c320c.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 10件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006c34c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34c4.md) [`006c34f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c34f8.md) [`006c3520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3520.md) [`006c35bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c35bc.md) · 呼出先 12件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3a70",
      "incomplete_value": true,
      "site": "006c3a80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c36c0",
      "incomplete_value": true,
      "site": "006c36d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c3a88",
      "incomplete_value": true,
      "site": "006c3a94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c36d8",
      "incomplete_value": true,
      "site": "006c36e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c38ec",
      "incomplete_value": false,
      "site": "006c3904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c353c",
      "incomplete_value": false,
      "site": "006c3554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "006c37bc",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ],
    [
      "006c3814",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "006c3824",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006c37bc",
      "READ",
      [
        "storage",
        "00c9bd40",
        null,
        "pointer"
      ]
    ],
    [
      "006c3814",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "006c3824",
      "PARAM",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c3554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md#insn-006c3554) · [`006c3a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md#insn-006c3a7c) · [`006c3354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c32d0.md#insn-006c3354)
- 新版 [`006c3904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md#insn-006c3904) · [`006c3e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md#insn-006c3e2c) · [`006c3704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c3/006c3680.md#insn-006c3704)

~~~diff
- 006c3554 ["INT_ADD", "register:40f0:8", ["const:6c3554:8", "const:4:8"]]
- 006c3554 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006c3904 ["INT_ADD", "register:40f0:8", ["const:6c3904:8", "const:4:8"]]
+ 006c3904 ["CALL", null, ["callee:00c58ed0:8"]]
- 006c3554 bytes 6b521694
+ 006c3904 bytes 73551694
- 006c3a7c ["INT_ADD", "register:40f0:8", ["const:6c3a7c:8", "const:4:8"]]
- 006c3a7c ["CALL", null, ["callee:00c58ed0:8"]]
+ 006c3e2c ["INT_ADD", "register:40f0:8", ["const:6c3e2c:8", "const:4:8"]]
+ 006c3e2c ["CALL", null, ["callee:00c58ed0:8"]]
- 006c3a7c bytes 21511694
+ 006c3e2c bytes 29541694
- 006c3354 ["COPY", "register:0:8", ["register:4040:8"]]
- 006c3354 ["INT_ADD", "register:40f0:8", ["const:6c3354:8", "const:4:8"]]
- 006c3354 ["CALLIND", null, ["register:0:8"]]
+ 006c3704 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006c3704 ["INT_ADD", "register:40f0:8", ["const:6c3704:8", "const:4:8"]]
+ 006c3704 ["CALLIND", null, ["register:0:8"]]
- 006c3354 bytes 00013fd6
+ 006c3704 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe554c22c3825af66949e7e50026f496"></a>

### [`006c3da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3da8.md) → [`006c4158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4158.md) FUN_006c4158

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 4件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a82a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a82/00a82a40.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 4件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a83a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a83/00a83a34.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.88% / 新版 97.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c4388",
      "incomplete_value": true,
      "site": "006c4398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3fd8",
      "incomplete_value": true,
      "site": "006c3fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c43a0",
      "incomplete_value": true,
      "site": "006c43a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c3ff0",
      "incomplete_value": true,
      "site": "006c3ff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c41e4",
      "READ",
      [
        "storage",
        "002c4038",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4388",
      "READ",
      [
        "storage",
        "002c3f28",
        null,
        "undefined8"
      ]
    ],
    [
      "006c43a0",
      "READ",
      [
        "storage",
        "002c3d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006c41e4",
      "READ",
      [
        "storage",
        "002c4088",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4388",
      "READ",
      [
        "storage",
        "002c3f78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c43a0",
      "READ",
      [
        "storage",
        "002c3dd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c3df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3da8.md#insn-006c3df8) · [`006c3e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3da8.md#insn-006c3e08) · [`006c3e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c3/006c3da8.md#insn-006c3e34)
- 新版 [`006c41a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4158.md#insn-006c41a8) · [`006c41b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4158.md#insn-006c41b8) · [`006c41e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4158.md#insn-006c41e4)

~~~diff
- 006c3df8 ["INT_ADD", "register:40f0:8", ["const:6c3df8:8", "const:4:8"]]
- 006c3df8 ["CALL", null, ["callee:008524fc:8"]]
+ 006c41a8 ["INT_ADD", "register:40f0:8", ["const:6c41a8:8", "const:4:8"]]
+ 006c41a8 ["CALL", null, ["callee:008524fc:8"]]
- 006c3df8 bytes d6350694
+ 006c41a8 bytes d5380694
- 006c3e08 ["INT_ADD", "register:40f0:8", ["const:6c3e08:8", "const:4:8"]]
- 006c3e08 ["CALL", null, ["callee:00a83a34:8"]]
+ 006c41b8 ["INT_ADD", "register:40f0:8", ["const:6c41b8:8", "const:4:8"]]
+ 006c41b8 ["CALL", null, ["callee:00a83a34:8"]]
- 006c3e08 bytes 0efb0e94
+ 006c41b8 bytes 1ffe0e94
- 006c3e34 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:38:8"]]
- 006c3e34 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 006c3e34 ["COPY", "register:5008:8", ["const:0:8"]]
- 006c3e34 ["COPY", "register:5010:8", ["const:0:8"]]
+ 006c41e4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:88:8"]]
+ 006c41e4 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c41e4 ["COPY", "register:5008:8", ["const:0:8"]]
+ 006c41e4 ["COPY", "register:5010:8", ["const:0:8"]]
- 006c3e34 bytes 401d40fd
+ 006c41e4 bytes 404540fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85522c1796975249509c31c10d115643"></a>

### [`006c4290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4290.md) → [`006c4640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4640.md) FUN_006c4640

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) [`006e93fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e93fc.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006c0f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0f90.md) [`006c4218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4218.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 7件 [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) [`006e97ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e97ac.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006c1340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c1340.md) [`006c45c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.33% / 新版 95.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c46e0",
      "value": [
        "leaf",
        "ram:6c1340:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4330",
      "value": [
        "leaf",
        "ram:6c0f90:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4774",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c43c4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c47b8",
      "value": [
        "leaf",
        "ram:6c1340:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4408",
      "value": [
        "leaf",
        "ram:6c0f90:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c46e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0f90"
      ]
    ],
    [
      "006c4774",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006c47b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0f90"
      ]
    ]
  ],
  "added": [
    [
      "006c46e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c1340"
      ]
    ],
    [
      "006c4774",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006c47b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c1340"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4290.md#insn-006c4330) · [`006c43c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4290.md#insn-006c43c4) · [`006c4408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4290.md#insn-006c4408)
- 新版 [`006c46e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4640.md#insn-006c46e0) · [`006c4774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4640.md#insn-006c4774) · [`006c47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c4640.md#insn-006c47b8)

~~~diff
- 006c4330 ["INT_ADD", "register:40f0:8", ["const:6c4330:8", "const:4:8"]]
- 006c4330 ["CALL", null, ["ram:6c0f90:8"]]
+ 006c46e0 ["INT_ADD", "register:40f0:8", ["const:6c46e0:8", "const:4:8"]]
+ 006c46e0 ["CALL", null, ["ram:6c1340:8"]]
- 006c4330 bytes 18f3ff97
+ 006c46e0 bytes 18f3ff97
- 006c43c4 ["INT_ADD", "register:40f0:8", ["const:6c43c4:8", "const:4:8"]]
- 006c43c4 ["CALL", null, ["ram:47ad34:8"]]
+ 006c4774 ["INT_ADD", "register:40f0:8", ["const:6c4774:8", "const:4:8"]]
+ 006c4774 ["CALL", null, ["ram:47b054:8"]]
- 006c43c4 bytes 5cdaf697
+ 006c4774 bytes 38daf697
- 006c4408 ["INT_ADD", "register:40f0:8", ["const:6c4408:8", "const:4:8"]]
- 006c4408 ["CALL", null, ["ram:6c0f90:8"]]
+ 006c47b8 ["INT_ADD", "register:40f0:8", ["const:6c47b8:8", "const:4:8"]]
+ 006c47b8 ["CALL", null, ["ram:6c1340:8"]]
- 006c4408 bytes e2f2ff97
+ 006c47b8 bytes e2f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b35077a7aa9481974469a7170b5b150f"></a>

### [`006c443c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c443c.md) → [`006c47ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c47ec.md) FUN_006c47ec

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0064bec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bec8.md) [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) [`006e79e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md) [`006e9ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e9/006e9ebc.md) [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 18件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`00469184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469184.md)
- 新版 呼出元 6件 [`0064c278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064c278.md) [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) [`006e7d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md) [`006ea26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea26c.md) [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) · 呼出先 18件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`004694a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004694a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.26% / 新版 99.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c5180",
      "value": [
        "leaf",
        "ram:63c978:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006c4dd0",
      "value": [
        "leaf",
        "ram:63c5c8:8"
      ]
    },
    "ordinal": 99,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c48f8",
      "READ",
      [
        "storage",
        "00c9b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "006c4904",
      "DATA",
      [
        "storage",
        "00ca4580",
        null,
        null
      ]
    ],
    [
      "006c493c",
      "DATA",
      [
        "storage",
        "00ca4580",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006c48f8",
      "READ",
      [
        "storage",
        "00c9c590",
        null,
        "pointer"
      ]
    ],
    [
      "006c4904",
      "DATA",
      [
        "storage",
        "00ca5550",
        null,
        null
      ]
    ],
    [
      "006c493c",
      "DATA",
      [
        "storage",
        "00ca5550",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c443c.md#insn-006c4dd0) · [`006c4464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c443c.md#insn-006c4464) · [`006c4494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c443c.md#insn-006c4494)
- 新版 [`006c5180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c47ec.md#insn-006c5180) · [`006c4814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c47ec.md#insn-006c4814) · [`006c4844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c47ec.md#insn-006c4844)

~~~diff
- 006c4dd0 ["INT_ADD", "register:40f0:8", ["const:6c4dd0:8", "const:4:8"]]
- 006c4dd0 ["CALL", null, ["ram:63c5c8:8"]]
+ 006c5180 ["INT_ADD", "register:40f0:8", ["const:6c5180:8", "const:4:8"]]
+ 006c5180 ["CALL", null, ["ram:63c978:8"]]
- 006c4dd0 bytes feddfd97
+ 006c5180 bytes feddfd97
- 006c4464 ["INT_ADD", "register:40f0:8", ["const:6c4464:8", "const:4:8"]]
- 006c4464 ["CALL", null, ["callee:00467bc0:8"]]
+ 006c4814 ["INT_ADD", "register:40f0:8", ["const:6c4814:8", "const:4:8"]]
+ 006c4814 ["CALL", null, ["callee:00467bc0:8"]]
- 006c4464 bytes 0f8df697
+ 006c4814 bytes eb8cf697
- 006c4494 ["INT_ADD", "register:40f0:8", ["const:6c4494:8", "const:4:8"]]
- 006c4494 ["CALL", null, ["callee:00467e8c:8"]]
+ 006c4844 ["INT_ADD", "register:40f0:8", ["const:6c4844:8", "const:4:8"]]
+ 006c4844 ["CALL", null, ["callee:00467e8c:8"]]
- 006c4494 bytes b68df697
+ 006c4844 bytes 928df697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ef54c2c05ee462d646cdc355d22315"></a>

### [`006c50e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c50e0.md) → [`006c5490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5490.md) FUN_006c5490

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`00682b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682b24.md) [`00683520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00683/00683520.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 9件 [`00682ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682ed4.md) [`006838d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00683/006838d0.md) [`007599e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00759/007599e4.md) [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c5504",
      "incomplete_value": false,
      "site": "006c5508",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c5154",
      "incomplete_value": false,
      "site": "006c5158",
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
            "const:170:8"
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
      "006c5504",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c5504",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c5158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c50e0.md#insn-006c5158) · [`006c5154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c50e0.md#insn-006c5154)
- 新版 [`006c5508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5490.md#insn-006c5508) · [`006c5504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5490.md#insn-006c5504)

~~~diff
- 006c5158 ["INT_ADD", "register:40f0:8", ["const:6c5158:8", "const:4:8"]]
- 006c5158 ["CALL", null, ["callee:00442c90:8"]]
+ 006c5508 ["INT_ADD", "register:40f0:8", ["const:6c5508:8", "const:4:8"]]
+ 006c5508 ["CALL", null, ["callee:00442c90:8"]]
- 006c5158 bytes 06f6f597
+ 006c5508 bytes e2f5f597
- 006c5154 ["COPY", "tmp:0:8", ["const:170:8"]]
- 006c5154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c5154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c5154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c5504 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 006c5504 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c5504 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c5504 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c5154 bytes 00c00591
+ 006c5504 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb399cdf985a1927aff4d85f4519e05a"></a>

### [`006c5168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5168.md) → [`006c5518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5518.md) FUN_006c5518

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`008f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39fc.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 3件 [`007599e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00759/007599e4.md) [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) [`008f49a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f49a8.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.18% / 新版 99.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c56f8",
      "incomplete_value": false,
      "site": "006c56fc",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c5348",
      "incomplete_value": false,
      "site": "006c534c",
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
            "const:170:8"
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
      "006c56f8",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c56f8",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c534c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5168.md#insn-006c534c) · [`006c5348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5168.md#insn-006c5348)
- 新版 [`006c56fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5518.md#insn-006c56fc) · [`006c56f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5518.md#insn-006c56f8)

~~~diff
- 006c534c ["INT_ADD", "register:40f0:8", ["const:6c534c:8", "const:4:8"]]
- 006c534c ["CALL", null, ["callee:00442c90:8"]]
+ 006c56fc ["INT_ADD", "register:40f0:8", ["const:6c56fc:8", "const:4:8"]]
+ 006c56fc ["CALL", null, ["callee:00442c90:8"]]
- 006c534c bytes 89f5f597
+ 006c56fc bytes 65f5f597
- 006c5348 ["COPY", "tmp:0:8", ["const:170:8"]]
- 006c5348 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006c5348 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006c5348 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006c56f8 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 006c56f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006c56f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006c56f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006c5348 bytes 00c00591
+ 006c56f8 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c3818761c93394b0c624cefd44d587"></a>

### [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) → [`006c7218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md) FUN_006c7218

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 14件 [`006829d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/006829d0.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) [`0075a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075a/0075a470.md) [`007fb288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fb/007fb288.md) · 呼出先 71件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006899ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/006899ec.md) [`006cb10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb10c.md) [`006d5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d5/006d5efc.md)
- 新版 呼出元 14件 [`00682d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682d80.md) [`007082e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00708/007082e8.md) [`007599e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00759/007599e4.md) [`0075a820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075a/0075a820.md) [`007fc1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fc/007fc1ec.md) · 呼出先 71件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00689d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00689/00689d9c.md) [`006cb4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cb4bc.md) [`006d62ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d6/006d62ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.98% / 新版 99.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006caf90",
      "incomplete_value": false,
      "site": "006caf9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2df000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cabe0",
      "incomplete_value": false,
      "site": "006cabec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2df000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "ordinal": 264,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006caf90",
      "PARAM",
      [
        "storage",
        "002dfcf8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006caf90",
      "PARAM",
      [
        "storage",
        "002dfd38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md#insn-006cabec) · [`006c6ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md#insn-006c6ec8) · [`006c6ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md#insn-006c6ee8)
- 新版 [`006caf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md#insn-006caf9c) · [`006c7278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md#insn-006c7278) · [`006c7298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c7/006c7218.md#insn-006c7298)

~~~diff
- 006cabec ["INT_ADD", "register:40f0:8", ["const:6cabec:8", "const:4:8"]]
- 006cabec ["CALL", null, ["callee:00c590a0:8"]]
+ 006caf9c ["INT_ADD", "register:40f0:8", ["const:6caf9c:8", "const:4:8"]]
+ 006caf9c ["CALL", null, ["callee:00c590a0:8"]]
- 006cabec bytes 39351694
+ 006caf9c bytes 41381694
- 006c6ec8 ["INT_ADD", "register:40f0:8", ["const:6c6ec8:8", "const:4:8"]]
- 006c6ec8 ["CALL", null, ["callee:00676e50:8"]]
+ 006c7278 ["INT_ADD", "register:40f0:8", ["const:6c7278:8", "const:4:8"]]
+ 006c7278 ["CALL", null, ["callee:00676e50:8"]]
- 006c6ec8 bytes f6befe97
+ 006c7278 bytes f6befe97
- 006c6ee8 ["INT_ADD", "register:40f0:8", ["const:6c6ee8:8", "const:4:8"]]
- 006c6ee8 ["CALL", null, ["callee:008524fc:8"]]
+ 006c7298 ["INT_ADD", "register:40f0:8", ["const:6c7298:8", "const:4:8"]]
+ 006c7298 ["CALL", null, ["callee:008524fc:8"]]
- 006c6ee8 bytes 9a290694
+ 006c7298 bytes 992c0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b483724a34a8a2097baa85bf30819d04"></a>

### [`006cb8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb8e4.md) → [`006cbc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbc94.md) FUN_006cbc94

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006cbacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cbacc.md) [`006ccbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cc/006ccbd0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006d7078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7078.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`006cbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbe7c.md) [`006ccf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cc/006ccf80.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006d7428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7428.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006cbce4",
      "incomplete_value": true,
      "site": "006cbcf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb934",
      "incomplete_value": true,
      "site": "006cb940",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c4000:8"
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
      "definition_site": "006cbd68",
      "incomplete_value": true,
      "site": "006cbd74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:358:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb9b8",
      "incomplete_value": true,
      "site": "006cb9c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:308:8"
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
      "006cbce4",
      "READ",
      [
        "storage",
        "002c4000",
        null,
        "undefined8"
      ]
    ],
    [
      "006cbd68",
      "READ",
      [
        "storage",
        "002c4308",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006cbce4",
      "READ",
      [
        "storage",
        "002c4050",
        null,
        "undefined8"
      ]
    ],
    [
      "006cbd68",
      "READ",
      [
        "storage",
        "002c4358",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cb924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb8e4.md#insn-006cb924) · [`006cb934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb8e4.md#insn-006cb934) · [`006cb948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb8e4.md#insn-006cb948)
- 新版 [`006cbcd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbc94.md#insn-006cbcd4) · [`006cbce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbc94.md#insn-006cbce4) · [`006cbcf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006cb/006cbc94.md#insn-006cbcf8)

~~~diff
- 006cb924 ["INT_ADD", "register:40f0:8", ["const:6cb924:8", "const:4:8"]]
- 006cb924 ["CALL", null, ["callee:00c58f30:8"]]
+ 006cbcd4 ["INT_ADD", "register:40f0:8", ["const:6cbcd4:8", "const:4:8"]]
+ 006cbcd4 ["CALL", null, ["callee:00c58f30:8"]]
- 006cb924 bytes 8f311694
+ 006cbcd4 bytes 97341694
- 006cb934 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006cb934 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 006cb934 ["COPY", "register:5008:8", ["const:0:8"]]
- 006cb934 ["COPY", "register:5010:8", ["const:0:8"]]
+ 006cbce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 006cbce4 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006cbce4 ["COPY", "register:5008:8", ["const:0:8"]]
+ 006cbce4 ["COPY", "register:5010:8", ["const:0:8"]]
- 006cb934 bytes 000140fd
+ 006cbce4 bytes 002940fd
- 006cb948 ["INT_ADD", "register:40f0:8", ["const:6cb948:8", "const:4:8"]]
- 006cb948 ["CALL", null, ["callee:0043bf04:8"]]
+ 006cbcf8 ["INT_ADD", "register:40f0:8", ["const:6cbcf8:8", "const:4:8"]]
+ 006cbcf8 ["CALL", null, ["callee:0043bf04:8"]]
- 006cb948 bytes a7c0f597
+ 006cbcf8 bytes 83c0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7125d988ff8300f656710ce6b297d9f2"></a>

### [`006d0a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0a74.md) → [`006d0e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0e24.md) FUN_006d0e24

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 13件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`006d7ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7ec8.md) [`006d7ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7ecc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) · 呼出先 13件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`006d8278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8278.md) [`006d827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d827c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d0ec0",
      "incomplete_value": true,
      "site": "006d0ec0",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0b10",
      "incomplete_value": true,
      "site": "006d0b10",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d0f70",
      "incomplete_value": false,
      "site": "006d0f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c8c000:8"
              ],
              [
                "leaf",
                "const:840:8"
              ]
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
      "definition_site": "006d0bc0",
      "incomplete_value": false,
      "site": "006d0bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "006d0ec0",
      "DATA",
      [
        "storage",
        "00c763e8",
        null,
        "undefined *"
      ]
    ],
    [
      "006d0f24",
      "READ",
      [
        "storage",
        "00c76408",
        null,
        "pointer"
      ]
    ],
    [
      "006d0f24",
      "READ",
      [
        "storage",
        "00c76410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0ec0",
      "DATA",
      [
        "storage",
        "00c773b8",
        null,
        "undefined *"
      ]
    ],
    [
      "006d0f24",
      "READ",
      [
        "storage",
        "00c773d8",
        null,
        "pointer"
      ]
    ],
    [
      "006d0f24",
      "READ",
      [
        "storage",
        "00c773e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0a74.md#insn-006d0a9c) · [`006d0aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0a74.md#insn-006d0aa0) · [`006d0ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0a74.md#insn-006d0ad8)
- 新版 [`006d0e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0e24.md#insn-006d0e4c) · [`006d0e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0e24.md#insn-006d0e50) · [`006d0e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d0e24.md#insn-006d0e88)

~~~diff
- 006d0a9c ["INT_ADD", "register:40f0:8", ["const:6d0a9c:8", "const:4:8"]]
- 006d0a9c ["CALL", null, ["callee:008524fc:8"]]
+ 006d0e4c ["INT_ADD", "register:40f0:8", ["const:6d0e4c:8", "const:4:8"]]
+ 006d0e4c ["CALL", null, ["callee:008524fc:8"]]
- 006d0a9c bytes ad020694
+ 006d0e4c bytes ac050694
- 006d0aa0 ["INT_ADD", "register:40f0:8", ["const:6d0aa0:8", "const:4:8"]]
- 006d0aa0 ["CALL", null, ["callee:0046cd24:8"]]
+ 006d0e50 ["INT_ADD", "register:40f0:8", ["const:6d0e50:8", "const:4:8"]]
+ 006d0e50 ["CALL", null, ["callee:0046cd24:8"]]
- 006d0aa0 bytes d96ff697
+ 006d0e50 bytes b56ff697
- 006d0ad8 ["INT_ADD", "register:40f0:8", ["const:6d0ad8:8", "const:4:8"]]
- 006d0ad8 ["CALL", null, ["callee:00a47944:8"]]
+ 006d0e88 ["INT_ADD", "register:40f0:8", ["const:6d0e88:8", "const:4:8"]]
+ 006d0e88 ["CALL", null, ["callee:00a47944:8"]]
- 006d0ad8 bytes 9ed70d94
+ 006d0e88 bytes afda0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e4e841c80b0e873f834f62de8ca928"></a>

### [`006d0c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0c98.md) → [`006d1048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md) FUN_006d1048

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 13件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`006d82a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d82a8.md) [`006d82ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d82ac.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) · 呼出先 13件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`006d8658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8658.md) [`006d865c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d865c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d11c4",
      "incomplete_value": false,
      "site": "006d11c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0e14",
      "incomplete_value": false,
      "site": "006d0e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:468:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d1128",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "006d113c",
      "DATA",
      [
        "storage",
        "00c8b828",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1154",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d1128",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ],
    [
      "006d113c",
      "DATA",
      [
        "storage",
        "00c8c7f8",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1154",
      "READ",
      [
        "storage",
        "00c9c410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0c98.md#insn-006d0cc8) · [`006d0ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0c98.md#insn-006d0ccc) · [`006d0d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0c98.md#insn-006d0d04)
- 新版 [`006d1078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md#insn-006d1078) · [`006d107c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md#insn-006d107c) · [`006d10b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1048.md#insn-006d10b4)

~~~diff
- 006d0cc8 ["INT_ADD", "register:40f0:8", ["const:6d0cc8:8", "const:4:8"]]
- 006d0cc8 ["CALL", null, ["callee:008524fc:8"]]
+ 006d1078 ["INT_ADD", "register:40f0:8", ["const:6d1078:8", "const:4:8"]]
+ 006d1078 ["CALL", null, ["callee:008524fc:8"]]
- 006d0cc8 bytes 22020694
+ 006d1078 bytes 21050694
- 006d0ccc ["INT_ADD", "register:40f0:8", ["const:6d0ccc:8", "const:4:8"]]
- 006d0ccc ["CALL", null, ["callee:0046cd24:8"]]
+ 006d107c ["INT_ADD", "register:40f0:8", ["const:6d107c:8", "const:4:8"]]
+ 006d107c ["CALL", null, ["callee:0046cd24:8"]]
- 006d0ccc bytes 4e6ff697
+ 006d107c bytes 2a6ff697
- 006d0d04 ["INT_ADD", "register:40f0:8", ["const:6d0d04:8", "const:4:8"]]
- 006d0d04 ["CALL", null, ["callee:00a47944:8"]]
+ 006d10b4 ["INT_ADD", "register:40f0:8", ["const:6d10b4:8", "const:4:8"]]
+ 006d10b4 ["CALL", null, ["callee:00a47944:8"]]
- 006d0d04 bytes 13d70d94
+ 006d10b4 bytes 24da0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a500309ba99b69d75b059bc6ad31f2eb"></a>

### [`006d0fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0fa4.md) → [`006d1354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md) FUN_006d1354

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006d203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d2/006d203c.md) · 呼出先 13件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`006d8438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8438.md) [`006d843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d843c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006d23ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d2/006d23ec.md) · 呼出先 13件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`006d87e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87e8.md) [`006d87ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87ec.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d14d0",
      "incomplete_value": false,
      "site": "006d14d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1120",
      "incomplete_value": false,
      "site": "006d1120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d1434",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "006d1448",
      "DATA",
      [
        "storage",
        "00c8b828",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1460",
      "READ",
      [
        "storage",
        "00c9b440",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d1434",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ],
    [
      "006d1448",
      "DATA",
      [
        "storage",
        "00c8c7f8",
        null,
        "undefined *"
      ]
    ],
    [
      "006d1460",
      "READ",
      [
        "storage",
        "00c9c410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0fa4.md#insn-006d0fd4) · [`006d0fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0fa4.md#insn-006d0fd8) · [`006d1010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d0fa4.md#insn-006d1010)
- 新版 [`006d1384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md#insn-006d1384) · [`006d1388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md#insn-006d1388) · [`006d13c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1354.md#insn-006d13c0)

~~~diff
- 006d0fd4 ["INT_ADD", "register:40f0:8", ["const:6d0fd4:8", "const:4:8"]]
- 006d0fd4 ["CALL", null, ["callee:008524fc:8"]]
+ 006d1384 ["INT_ADD", "register:40f0:8", ["const:6d1384:8", "const:4:8"]]
+ 006d1384 ["CALL", null, ["callee:008524fc:8"]]
- 006d0fd4 bytes 5f010694
+ 006d1384 bytes 5e040694
- 006d0fd8 ["INT_ADD", "register:40f0:8", ["const:6d0fd8:8", "const:4:8"]]
- 006d0fd8 ["CALL", null, ["callee:0046cd24:8"]]
+ 006d1388 ["INT_ADD", "register:40f0:8", ["const:6d1388:8", "const:4:8"]]
+ 006d1388 ["CALL", null, ["callee:0046cd24:8"]]
- 006d0fd8 bytes 8b6ef697
+ 006d1388 bytes 676ef697
- 006d1010 ["INT_ADD", "register:40f0:8", ["const:6d1010:8", "const:4:8"]]
- 006d1010 ["CALL", null, ["callee:00a47944:8"]]
+ 006d13c0 ["INT_ADD", "register:40f0:8", ["const:6d13c0:8", "const:4:8"]]
+ 006d13c0 ["CALL", null, ["callee:00a47944:8"]]
- 006d1010 bytes 50d60d94
+ 006d13c0 bytes 61d90d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca4a1b5963dde6138d871703a916d171"></a>

### [`006d4dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md) → [`006d519c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d519c.md) FUN_006d519c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008f7ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f7/008f7ecc.md) [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 26件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00467edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467edc.md) [`00467ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ee4.md)
- 新版 呼出元 3件 [`008f8e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8e78.md) [`0099803c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00998/0099803c.md) [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) · 呼出先 26件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md) [`004681fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004681fc.md) [`00468204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468204.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d53f8",
      "value": [
        "leaf",
        "ram:4681fc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5048",
      "value": [
        "leaf",
        "ram:467edc:8"
      ]
    },
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5410",
      "value": [
        "leaf",
        "ram:468204:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5060",
      "value": [
        "leaf",
        "ram:467ee4:8"
      ]
    },
    "ordinal": 30,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d57a0",
      "incomplete_value": true,
      "site": "006d57b0",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "006d53f0",
      "incomplete_value": true,
      "site": "006d5400",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 52,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d53f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00467edc"
      ]
    ],
    [
      "006d5410",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00467ee4"
      ]
    ],
    [
      "006d5518",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006d53f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004681fc"
      ]
    ],
    [
      "006d5410",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00468204"
      ]
    ],
    [
      "006d5518",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md#insn-006d5048) · [`006d5060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md#insn-006d5060) · [`006d5400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4dec.md#insn-006d5400)
- 新版 [`006d53f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d519c.md#insn-006d53f8) · [`006d5410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d519c.md#insn-006d5410) · [`006d57b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d519c.md#insn-006d57b0)

~~~diff
- 006d5048 ["INT_ADD", "register:40f0:8", ["const:6d5048:8", "const:4:8"]]
- 006d5048 ["CALL", null, ["ram:467edc:8"]]
+ 006d53f8 ["INT_ADD", "register:40f0:8", ["const:6d53f8:8", "const:4:8"]]
+ 006d53f8 ["CALL", null, ["ram:4681fc:8"]]
- 006d5048 bytes a54bf697
+ 006d53f8 bytes 814bf697
- 006d5060 ["INT_ADD", "register:40f0:8", ["const:6d5060:8", "const:4:8"]]
- 006d5060 ["CALL", null, ["ram:467ee4:8"]]
+ 006d5410 ["INT_ADD", "register:40f0:8", ["const:6d5410:8", "const:4:8"]]
+ 006d5410 ["CALL", null, ["ram:468204:8"]]
- 006d5060 bytes a14bf697
+ 006d5410 bytes 7d4bf697
- 006d5400 ["INT_ADD", "register:40f0:8", ["const:6d5400:8", "const:4:8"]]
- 006d5400 ["CALL", null, ["callee:004692e8:8"]]
+ 006d57b0 ["INT_ADD", "register:40f0:8", ["const:6d57b0:8", "const:4:8"]]
+ 006d57b0 ["CALL", null, ["callee:004692e8:8"]]
- 006d5400 bytes f24ef697
+ 006d57b0 bytes ce4ef697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0672d811ba9929e6a034743cd8daa8d6"></a>

### [`006d70e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md) → [`006d7490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md) FUN_006d7490

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006cff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cf/006cff44.md) · 呼出先 10件 [`006d73e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md) [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`006d02f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d02f4.md) · 呼出先 10件 [`006d7794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md) [`006d7a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`006d7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d7750",
      "incomplete_value": false,
      "site": "006d7754",
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
            "const:42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d73a0",
      "incomplete_value": false,
      "site": "006d73a4",
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
            "const:f75:8"
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
      "006d7750",
      "PARAM",
      [
        "storage",
        "002a9f75",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d7750",
      "PARAM",
      [
        "storage",
        "002aa042",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d73a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md#insn-006d73a4) · [`006d7160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md#insn-006d7160) · [`006d7180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md#insn-006d7180)
- 新版 [`006d7754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md#insn-006d7754) · [`006d7510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md#insn-006d7510) · [`006d7530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md#insn-006d7530)

~~~diff
- 006d73a4 ["INT_ADD", "register:40f0:8", ["const:6d73a4:8", "const:4:8"]]
- 006d73a4 ["CALL", null, ["callee:006d7a58:8"]]
+ 006d7754 ["INT_ADD", "register:40f0:8", ["const:6d7754:8", "const:4:8"]]
+ 006d7754 ["CALL", null, ["callee:006d7a58:8"]]
- 006d73a4 bytes c1000094
+ 006d7754 bytes c1000094
- 006d7160 ["INT_ADD", "register:40f0:8", ["const:6d7160:8", "const:4:8"]]
- 006d7160 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d7510 ["INT_ADD", "register:40f0:8", ["const:6d7510:8", "const:4:8"]]
+ 006d7510 ["CALL", null, ["callee:00c58f30:8"]]
- 006d7160 bytes 80031694
+ 006d7510 bytes 88061694
- 006d7180 ["INT_ADD", "register:40f0:8", ["const:6d7180:8", "const:4:8"]]
- 006d7180 ["CALL", null, ["callee:00c59130:8"]]
+ 006d7530 ["INT_ADD", "register:40f0:8", ["const:6d7530:8", "const:4:8"]]
+ 006d7530 ["CALL", null, ["callee:00c59130:8"]]
- 006d7180 bytes f8031694
+ 006d7530 bytes 00071694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e41e3b1513bf792c962b90d603b000c"></a>

### [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) → [`006d7a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md) FUN_006d7a58

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006d70e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md) [`006d77d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md) [`007f3ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ee4.md) [`007f41e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f41e8.md) · 呼出先 4件 [`006d770c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d770c.md) [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`006d7490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md) [`006d7b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md) [`007f4e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f4/007f4e48.md) [`007f514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f5/007f514c.md) · 呼出先 4件 [`006d7abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7abc.md) [`00c38dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d7a88",
      "incomplete_value": true,
      "site": "006d7a90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
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
      "definition_site": "006d76d8",
      "incomplete_value": true,
      "site": "006d76e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "006d7a8c",
      "incomplete_value": true,
      "site": "006d7a90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:5f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d76dc",
      "incomplete_value": true,
      "site": "006d76e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
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
      "006d7a88",
      "READ",
      [
        "storage",
        "00c9b618",
        null,
        "pointer"
      ]
    ],
    [
      "006d7a88",
      "PARAM",
      [
        "storage",
        "00c96940",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d7a8c",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006d7a88",
      "READ",
      [
        "storage",
        "00c9c5e8",
        null,
        "pointer"
      ]
    ],
    [
      "006d7a88",
      "PARAM",
      [
        "storage",
        "00c97910",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006d7a8c",
      "READ",
      [
        "storage",
        "00c9c5f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d76e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md#insn-006d76e0) · [`006d76bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md#insn-006d76bc) · [`006d76c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md#insn-006d76c8)
- 新版 [`006d7a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md#insn-006d7a90) · [`006d7a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md#insn-006d7a6c) · [`006d7a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md#insn-006d7a78)

~~~diff
- 006d76e0 ["INT_ADD", "register:40f0:8", ["const:6d76e0:8", "const:4:8"]]
- 006d76e0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 006d7a90 ["INT_ADD", "register:40f0:8", ["const:6d7a90:8", "const:4:8"]]
+ 006d7a90 ["CALL", null, ["callee:00c58fb0:8"]]
- 006d76e0 bytes 40021694
+ 006d7a90 bytes 48051694
- 006d76bc ["INT_ADD", "register:40f0:8", ["const:6d76bc:8", "const:4:8"]]
- 006d76bc ["CALL", null, ["callee:00c58f90:8"]]
+ 006d7a6c ["INT_ADD", "register:40f0:8", ["const:6d7a6c:8", "const:4:8"]]
+ 006d7a6c ["CALL", null, ["callee:00c58f90:8"]]
- 006d76bc bytes 41021694
+ 006d7a6c bytes 49051694
- 006d76c8 ["INT_ADD", "register:40f0:8", ["const:6d76c8:8", "const:4:8"]]
- 006d76c8 ["CALL", null, ["callee:006d7abc:8"]]
+ 006d7a78 ["INT_ADD", "register:40f0:8", ["const:6d7a78:8", "const:4:8"]]
+ 006d7a78 ["CALL", null, ["callee:006d7abc:8"]]
- 006d76c8 bytes 11000094
+ 006d7a78 bytes 11000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5170b4792936a79cabc69dea2abb6b"></a>

### [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) → [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) FUN_006d7aa8

採用 · 移動量 `+0x3b0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`006cff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cf/006cff44.md) [`006d70e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d70e0.md) [`006d73e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`007f3ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ee4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 25件 [`006d02f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d02f4.md) [`006d7490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7490.md) [`006d7794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7794.md) [`006d7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md) [`007f4e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f4/007f4e48.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "006d7ab4",
      "incomplete_value": false,
      "site": "006d7ab8",
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
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7704",
      "incomplete_value": false,
      "site": "006d7708",
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
            "const:ecf:8"
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
      "006d7ab4",
      "PARAM",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d7ab4",
      "PARAM",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md#insn-006d7708) · [`006d7704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md#insn-006d7704)
- 新版 [`006d7ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md#insn-006d7ab8) · [`006d7ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md#insn-006d7ab4)

~~~diff
- 006d7708 ["INT_ADD", "register:40f0:8", ["const:6d7708:8", "const:4:8"]]
- 006d7708 ["CALL", null, ["callee:0043bad8:8"]]
+ 006d7ab8 ["INT_ADD", "register:40f0:8", ["const:6d7ab8:8", "const:4:8"]]
+ 006d7ab8 ["CALL", null, ["callee:0043bad8:8"]]
- 006d7708 bytes 2c90f597
+ 006d7ab8 bytes 0890f597
- 006d7704 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 006d7704 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d7704 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d7704 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d7ab4 ["COPY", "tmp:0:8", ["const:fad:8"]]
+ 006d7ab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d7ab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d7ab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d7704 bytes 003c3b91
+ 006d7ab4 bytes 00b43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf3bbf298a38c4216700af9c490556e"></a>

### [`006d77d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md) → [`006d7b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md) FUN_006d7b84

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006cff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cf/006cff44.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`006d7be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006d02f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d02f4.md) · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`006d7a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md) [`006d7f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7f98.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.59% / 新版 99.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006d7f2c",
      "incomplete_value": false,
      "site": "006d7f30",
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
            "const:cd3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7b7c",
      "incomplete_value": false,
      "site": "006d7b80",
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
            "const:b7b:8"
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
      "006d7f2c",
      "PARAM",
      [
        "storage",
        "002a7b7b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d7f2c",
      "PARAM",
      [
        "storage",
        "002a7cd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md#insn-006d7b80) · [`006d7864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md#insn-006d7864) · [`006d7884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d77d4.md#insn-006d7884)
- 新版 [`006d7f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md#insn-006d7f30) · [`006d7c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md#insn-006d7c14) · [`006d7c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7b84.md#insn-006d7c34)

~~~diff
- 006d7b80 ["INT_ADD", "register:40f0:8", ["const:6d7b80:8", "const:4:8"]]
- 006d7b80 ["CALL", null, ["callee:006d7a58:8"]]
+ 006d7f30 ["INT_ADD", "register:40f0:8", ["const:6d7f30:8", "const:4:8"]]
+ 006d7f30 ["CALL", null, ["callee:006d7a58:8"]]
- 006d7b80 bytes cafeff97
+ 006d7f30 bytes cafeff97
- 006d7864 ["INT_ADD", "register:40f0:8", ["const:6d7864:8", "const:4:8"]]
- 006d7864 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d7c14 ["INT_ADD", "register:40f0:8", ["const:6d7c14:8", "const:4:8"]]
+ 006d7c14 ["CALL", null, ["callee:00c58f30:8"]]
- 006d7864 bytes bf011694
+ 006d7c14 bytes c7041694
- 006d7884 ["INT_ADD", "register:40f0:8", ["const:6d7884:8", "const:4:8"]]
- 006d7884 ["CALL", null, ["callee:00c59130:8"]]
+ 006d7c34 ["INT_ADD", "register:40f0:8", ["const:6d7c34:8", "const:4:8"]]
+ 006d7c34 ["CALL", null, ["callee:00c59130:8"]]
- 006d7884 bytes 37021694
+ 006d7c34 bytes 3f051694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7260e9a35d26ca06c378602c48874b8c"></a>

### [`006d7e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7e80.md) → [`006d8230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8230.md) FUN_006d8230

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d8254",
      "incomplete_value": false,
      "site": "006d8254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7ea4",
      "incomplete_value": false,
      "site": "006d7ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "006d8254",
      "DATA",
      [
        "storage",
        "00c763e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8254",
      "DATA",
      [
        "storage",
        "00c773b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7e80.md#insn-006d7e94) · [`006d7e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7e80.md#insn-006d7e9c) · [`006d7ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7e80.md#insn-006d7ea0)
- 新版 [`006d8244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8230.md#insn-006d8244) · [`006d824c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8230.md#insn-006d824c) · [`006d8250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8230.md#insn-006d8250)

~~~diff
- 006d7e94 ["INT_ADD", "register:40f0:8", ["const:6d7e94:8", "const:4:8"]]
- 006d7e94 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d8244 ["INT_ADD", "register:40f0:8", ["const:6d8244:8", "const:4:8"]]
+ 006d8244 ["CALL", null, ["callee:00c58f30:8"]]
- 006d7e94 bytes 33001694
+ 006d8244 bytes 3b031694
- 006d7e9c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d824c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d7e9c bytes e82c00f0
+ 006d824c bytes e82c00f0
- 006d7ea0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 006d7ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d7ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d7ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8250 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 006d8250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d7ea0 bytes 08a10f91
+ 006d8250 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c0975356c1568a2324d418a9e132e81"></a>

### [`006d7eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7eb4.md) → [`006d8264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8264.md) FUN_006d8264

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d8270",
      "incomplete_value": false,
      "site": "006d8270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d7ec0",
      "incomplete_value": false,
      "site": "006d7ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "006d8270",
      "DATA",
      [
        "storage",
        "00c763e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8270",
      "DATA",
      [
        "storage",
        "00c773b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7eb4.md#insn-006d7eb8) · [`006d7ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7eb4.md#insn-006d7ebc)
- 新版 [`006d8268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8264.md#insn-006d8268) · [`006d826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8264.md#insn-006d826c)

~~~diff
- 006d7eb8 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006d8268 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006d7eb8 bytes e92c00f0
+ 006d8268 bytes e92c00f0
- 006d7ebc ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 006d7ebc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d7ebc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d7ebc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d826c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 006d826c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d826c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d826c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d7ebc bytes 29a10f91
+ 006d826c bytes 29e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40227c4eef23c222333d27a68b4031d3"></a>

### [`006d7ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7ed0.md) → [`006d8280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8280.md) FUN_006d8280

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006d4c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d4/006d4c9c.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006d504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d5/006d504c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d82a0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7ef0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d82ac",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7efc",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006d82a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006d82ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006d82a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006d82ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d7ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7ed0.md#insn-006d7ef0) · [`006d7efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7ed0.md#insn-006d7efc)
- 新版 [`006d82a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8280.md#insn-006d82a0) · [`006d82ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8280.md#insn-006d82ac)

~~~diff
- 006d7ef0 ["INT_ADD", "register:40f0:8", ["const:6d7ef0:8", "const:4:8"]]
- 006d7ef0 ["CALL", null, ["ram:47ad34:8"]]
+ 006d82a0 ["INT_ADD", "register:40f0:8", ["const:6d82a0:8", "const:4:8"]]
+ 006d82a0 ["CALL", null, ["ram:47b054:8"]]
- 006d7ef0 bytes 918bf697
+ 006d82a0 bytes 6d8bf697
- 006d7efc ["INT_ADD", "register:40f0:8", ["const:6d7efc:8", "const:4:8"]]
- 006d7efc ["CALL", null, ["ram:47ad34:8"]]
+ 006d82ac ["INT_ADD", "register:40f0:8", ["const:6d82ac:8", "const:4:8"]]
+ 006d82ac ["CALL", null, ["ram:47b054:8"]]
- 006d7efc bytes 8e8bf697
+ 006d82ac bytes 6a8bf697
~~~


<a id="compare-dffdc993cac17ee1a481143c69b21201"></a>

### [`006d8260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8260.md) → [`006d8610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8610.md) FUN_006d8610

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d8634",
      "incomplete_value": false,
      "site": "006d8634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8284",
      "incomplete_value": false,
      "site": "006d8284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "006d8634",
      "DATA",
      [
        "storage",
        "00c76468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8634",
      "DATA",
      [
        "storage",
        "00c77438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8260.md#insn-006d8274) · [`006d827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8260.md#insn-006d827c) · [`006d8280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8260.md#insn-006d8280)
- 新版 [`006d8624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8610.md#insn-006d8624) · [`006d862c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8610.md#insn-006d862c) · [`006d8630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8610.md#insn-006d8630)

~~~diff
- 006d8274 ["INT_ADD", "register:40f0:8", ["const:6d8274:8", "const:4:8"]]
- 006d8274 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d8624 ["INT_ADD", "register:40f0:8", ["const:6d8624:8", "const:4:8"]]
+ 006d8624 ["CALL", null, ["callee:00c58f30:8"]]
- 006d8274 bytes 3bff1594
+ 006d8624 bytes 43021694
- 006d827c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d862c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d827c bytes e82c00d0
+ 006d862c bytes e82c00f0
- 006d8280 ["COPY", "tmp:0:8", ["const:468:8"]]
- 006d8280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8630 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 006d8630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8280 bytes 08a11191
+ 006d8630 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936fab56be447b69027f72dd75f5ddae"></a>

### [`006d8294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8294.md) → [`006d8644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8644.md) FUN_006d8644

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d8650",
      "incomplete_value": false,
      "site": "006d8650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d82a0",
      "incomplete_value": false,
      "site": "006d82a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "006d8650",
      "DATA",
      [
        "storage",
        "00c76468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8650",
      "DATA",
      [
        "storage",
        "00c77438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8294.md#insn-006d8298) · [`006d829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8294.md#insn-006d829c)
- 新版 [`006d8648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8644.md#insn-006d8648) · [`006d864c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8644.md#insn-006d864c)

~~~diff
- 006d8298 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006d8648 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006d8298 bytes e92c00d0
+ 006d8648 bytes e92c00f0
- 006d829c ["COPY", "tmp:0:8", ["const:468:8"]]
- 006d829c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d829c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d829c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d864c ["COPY", "tmp:0:8", ["const:438:8"]]
+ 006d864c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d864c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d864c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d829c bytes 29a11191
+ 006d864c bytes 29e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3245ae26e17398d9ca8668d1dccc99ef"></a>

### [`006d83f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d83f0.md) → [`006d87a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87a0.md) FUN_006d87a0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d87c4",
      "incomplete_value": false,
      "site": "006d87c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8414",
      "incomplete_value": false,
      "site": "006d8414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "006d87c4",
      "DATA",
      [
        "storage",
        "00c764e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d87c4",
      "DATA",
      [
        "storage",
        "00c774b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d83f0.md#insn-006d8404) · [`006d840c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d83f0.md#insn-006d840c) · [`006d8410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d83f0.md#insn-006d8410)
- 新版 [`006d87b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87a0.md#insn-006d87b4) · [`006d87bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87a0.md#insn-006d87bc) · [`006d87c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87a0.md#insn-006d87c0)

~~~diff
- 006d8404 ["INT_ADD", "register:40f0:8", ["const:6d8404:8", "const:4:8"]]
- 006d8404 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d87b4 ["INT_ADD", "register:40f0:8", ["const:6d87b4:8", "const:4:8"]]
+ 006d87b4 ["CALL", null, ["callee:00c58f30:8"]]
- 006d8404 bytes d7fe1594
+ 006d87b4 bytes df011694
- 006d840c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d87bc ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d840c bytes e82c00d0
+ 006d87bc bytes e82c00f0
- 006d8410 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 006d8410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d87c0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 006d87c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d87c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d87c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8410 bytes 08a11391
+ 006d87c0 bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce431c5caf60fa87a49f2aba617bc65a"></a>

### [`006d8424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8424.md) → [`006d87d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87d4.md) FUN_006d87d4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d87e0",
      "incomplete_value": false,
      "site": "006d87e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8430",
      "incomplete_value": false,
      "site": "006d8430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "006d87e0",
      "DATA",
      [
        "storage",
        "00c764e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d87e0",
      "DATA",
      [
        "storage",
        "00c774b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8424.md#insn-006d8428) · [`006d842c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8424.md#insn-006d842c)
- 新版 [`006d87d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87d4.md#insn-006d87d8) · [`006d87dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87d4.md#insn-006d87dc)

~~~diff
- 006d8428 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006d87d8 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006d8428 bytes e92c00d0
+ 006d87d8 bytes e92c00f0
- 006d842c ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 006d842c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d842c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d842c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d87dc ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 006d87dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d87dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d87dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d842c bytes 29a11391
+ 006d87dc bytes 29e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6136667c74e536dfd3fc863662830e"></a>

### [`006d8440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md) → [`006d87f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md) FUN_006d87f0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006c4ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4ec4.md) [`006d12b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d12b0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`006c5274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5274.md) [`006d1660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1660.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d8834",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d8484",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d885c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d84ac",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006d8834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006d885c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006d8a78",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006d8834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006d885c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006d8a78",
      "DATA",
      [
        "storage",
        "003c9698",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md#insn-006d8484) · [`006d84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md#insn-006d84ac) · [`006d84a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8440.md#insn-006d84a4)
- 新版 [`006d8834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md#insn-006d8834) · [`006d885c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md#insn-006d885c) · [`006d8854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d87f0.md#insn-006d8854)

~~~diff
- 006d8484 ["INT_ADD", "register:40f0:8", ["const:6d8484:8", "const:4:8"]]
- 006d8484 ["CALL", null, ["ram:47ad34:8"]]
+ 006d8834 ["INT_ADD", "register:40f0:8", ["const:6d8834:8", "const:4:8"]]
+ 006d8834 ["CALL", null, ["ram:47b054:8"]]
- 006d8484 bytes 2c8af697
+ 006d8834 bytes 088af697
- 006d84ac ["INT_ADD", "register:40f0:8", ["const:6d84ac:8", "const:4:8"]]
- 006d84ac ["CALL", null, ["ram:47ad34:8"]]
+ 006d885c ["INT_ADD", "register:40f0:8", ["const:6d885c:8", "const:4:8"]]
+ 006d885c ["CALL", null, ["ram:47b054:8"]]
- 006d84ac bytes 228af697
+ 006d885c bytes fe89f697
- 006d84a4 ["INT_ADD", "register:40f0:8", ["const:6d84a4:8", "const:4:8"]]
- 006d84a4 ["CALL", null, ["callee:006d1660:8"]]
+ 006d8854 ["INT_ADD", "register:40f0:8", ["const:6d8854:8", "const:4:8"]]
+ 006d8854 ["CALL", null, ["callee:006d1660:8"]]
- 006d84a4 bytes 83e3ff97
+ 006d8854 bytes 83e3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb6078ec5bb720919e68e178ef94680e"></a>

### [`006d8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8770.md) → [`006d8b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b20.md) FUN_006d8b20

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d8b44",
      "incomplete_value": false,
      "site": "006d8b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8794",
      "incomplete_value": false,
      "site": "006d8794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "006d8b44",
      "DATA",
      [
        "storage",
        "00c76568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8b44",
      "DATA",
      [
        "storage",
        "00c77538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8770.md#insn-006d8784) · [`006d878c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8770.md#insn-006d878c) · [`006d8790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8770.md#insn-006d8790)
- 新版 [`006d8b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b20.md#insn-006d8b34) · [`006d8b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b20.md#insn-006d8b3c) · [`006d8b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b20.md#insn-006d8b40)

~~~diff
- 006d8784 ["INT_ADD", "register:40f0:8", ["const:6d8784:8", "const:4:8"]]
- 006d8784 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d8b34 ["INT_ADD", "register:40f0:8", ["const:6d8b34:8", "const:4:8"]]
+ 006d8b34 ["CALL", null, ["callee:00c58f30:8"]]
- 006d8784 bytes f7fd1594
+ 006d8b34 bytes ff001694
- 006d878c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d8b3c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d878c bytes e82c00d0
+ 006d8b3c bytes e82c00f0
- 006d8790 ["COPY", "tmp:0:8", ["const:568:8"]]
- 006d8790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8b40 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 006d8b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8790 bytes 08a11591
+ 006d8b40 bytes 08e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b26aa823f936a5a39a17a7f5b7d03e6"></a>

### [`006d8d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d08.md) → [`006d90b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d90b8.md) FUN_006d90b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d90dc",
      "incomplete_value": false,
      "site": "006d90dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d8d2c",
      "incomplete_value": false,
      "site": "006d8d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "006d90dc",
      "DATA",
      [
        "storage",
        "00c765e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d90dc",
      "DATA",
      [
        "storage",
        "00c775b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d8d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d08.md#insn-006d8d1c) · [`006d8d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d08.md#insn-006d8d24) · [`006d8d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d8d08.md#insn-006d8d28)
- 新版 [`006d90cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d90b8.md#insn-006d90cc) · [`006d90d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d90b8.md#insn-006d90d4) · [`006d90d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d90b8.md#insn-006d90d8)

~~~diff
- 006d8d1c ["INT_ADD", "register:40f0:8", ["const:6d8d1c:8", "const:4:8"]]
- 006d8d1c ["CALL", null, ["callee:00c58f30:8"]]
+ 006d90cc ["INT_ADD", "register:40f0:8", ["const:6d90cc:8", "const:4:8"]]
+ 006d90cc ["CALL", null, ["callee:00c58f30:8"]]
- 006d8d1c bytes 91fc1594
+ 006d90cc bytes 99ff1594
- 006d8d24 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d90d4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d8d24 bytes e82c00d0
+ 006d90d4 bytes e82c00d0
- 006d8d28 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 006d8d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d8d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d8d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d90d8 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 006d90d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d90d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d90d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d8d28 bytes 08a11791
+ 006d90d8 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44dd658d1e9a7aa8598979f17adb570f"></a>

### [`006d988c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d988c.md) → [`006d9c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c3c.md) FUN_006d9c3c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d9c60",
      "incomplete_value": false,
      "site": "006d9c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d98b0",
      "incomplete_value": false,
      "site": "006d98b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "006d9c60",
      "DATA",
      [
        "storage",
        "00c76668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9c60",
      "DATA",
      [
        "storage",
        "00c77638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d98a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d988c.md#insn-006d98a0) · [`006d98a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d988c.md#insn-006d98a8) · [`006d98ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d988c.md#insn-006d98ac)
- 新版 [`006d9c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c3c.md#insn-006d9c50) · [`006d9c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c3c.md#insn-006d9c58) · [`006d9c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c3c.md#insn-006d9c5c)

~~~diff
- 006d98a0 ["INT_ADD", "register:40f0:8", ["const:6d98a0:8", "const:4:8"]]
- 006d98a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d9c50 ["INT_ADD", "register:40f0:8", ["const:6d9c50:8", "const:4:8"]]
+ 006d9c50 ["CALL", null, ["callee:00c58f30:8"]]
- 006d98a0 bytes b0f91594
+ 006d9c50 bytes b8fc1594
- 006d98a8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d9c58 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d98a8 bytes e82c00b0
+ 006d9c58 bytes e82c00d0
- 006d98ac ["COPY", "tmp:0:8", ["const:668:8"]]
- 006d98ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d98ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d98ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9c5c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 006d9c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d98ac bytes 08a11991
+ 006d9c5c bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34281a8fef6a9edcf589f9d4cd28aa01"></a>

### [`006d98dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d98dc.md) → [`006d9c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c8c.md) FUN_006d9c8c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md) [`00a46944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46944.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47920.md) [`00a47938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47938.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9d08",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9958",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9d30",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9980",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006d9d08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006d9d30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006d9d08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006d9d30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d98dc.md#insn-006d9958) · [`006d9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d98dc.md#insn-006d9980) · [`006d992c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d98dc.md#insn-006d992c)
- 新版 [`006d9d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c8c.md#insn-006d9d08) · [`006d9d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c8c.md#insn-006d9d30) · [`006d9cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9c8c.md#insn-006d9cdc)

~~~diff
- 006d9958 ["INT_ADD", "register:40f0:8", ["const:6d9958:8", "const:4:8"]]
- 006d9958 ["CALL", null, ["ram:47ad34:8"]]
+ 006d9d08 ["INT_ADD", "register:40f0:8", ["const:6d9d08:8", "const:4:8"]]
+ 006d9d08 ["CALL", null, ["ram:47b054:8"]]
- 006d9958 bytes f784f697
+ 006d9d08 bytes d384f697
- 006d9980 ["INT_ADD", "register:40f0:8", ["const:6d9980:8", "const:4:8"]]
- 006d9980 ["CALL", null, ["ram:47ad34:8"]]
+ 006d9d30 ["INT_ADD", "register:40f0:8", ["const:6d9d30:8", "const:4:8"]]
+ 006d9d30 ["CALL", null, ["ram:47b054:8"]]
- 006d9980 bytes ed84f697
+ 006d9d30 bytes c984f697
- 006d992c ["INT_ADD", "register:40f0:8", ["const:6d992c:8", "const:4:8"]]
- 006d992c ["CALL", null, ["callee:008b7ea8:8"]]
+ 006d9cdc ["INT_ADD", "register:40f0:8", ["const:6d9cdc:8", "const:4:8"]]
+ 006d9cdc ["CALL", null, ["callee:008b7ea8:8"]]
- 006d992c bytes 74750794
+ 006d9cdc bytes 73780794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b2e6a4bdf298f4d3ee205dcd41cc9e"></a>

### [`006d99c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d99c4.md) → [`006d9d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9d74.md) FUN_006d9d74

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d9d98",
      "incomplete_value": false,
      "site": "006d9d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d99e8",
      "incomplete_value": false,
      "site": "006d99e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d9d98",
      "DATA",
      [
        "storage",
        "00c766e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9d98",
      "DATA",
      [
        "storage",
        "00c776b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d99d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d99c4.md#insn-006d99d8) · [`006d99e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d99c4.md#insn-006d99e0) · [`006d99e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d99c4.md#insn-006d99e4)
- 新版 [`006d9d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9d74.md#insn-006d9d88) · [`006d9d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9d74.md#insn-006d9d90) · [`006d9d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9d74.md#insn-006d9d94)

~~~diff
- 006d99d8 ["INT_ADD", "register:40f0:8", ["const:6d99d8:8", "const:4:8"]]
- 006d99d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d9d88 ["INT_ADD", "register:40f0:8", ["const:6d9d88:8", "const:4:8"]]
+ 006d9d88 ["CALL", null, ["callee:00c58f30:8"]]
- 006d99d8 bytes 62f91594
+ 006d9d88 bytes 6afc1594
- 006d99e0 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d9d90 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d99e0 bytes e82c00b0
+ 006d9d90 bytes e82c00d0
- 006d99e4 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 006d99e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d99e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d99e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9d94 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 006d9d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d99e4 bytes 08a11b91
+ 006d9d94 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42c631121c8c95fecbc4d1c9eac7840"></a>

### [`006d9a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9a14.md) → [`006d9dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9dc4.md) FUN_006d9dc4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9e34",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9a84",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9e5c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9aac",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006d9e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006d9e5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006d9e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006d9e5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9a14.md#insn-006d9a84) · [`006d9aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9a14.md#insn-006d9aac) · [`006d9a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9a14.md#insn-006d9a64)
- 新版 [`006d9e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9dc4.md#insn-006d9e34) · [`006d9e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9dc4.md#insn-006d9e5c) · [`006d9e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9dc4.md#insn-006d9e14)

~~~diff
- 006d9a84 ["INT_ADD", "register:40f0:8", ["const:6d9a84:8", "const:4:8"]]
- 006d9a84 ["CALL", null, ["ram:47ad34:8"]]
+ 006d9e34 ["INT_ADD", "register:40f0:8", ["const:6d9e34:8", "const:4:8"]]
+ 006d9e34 ["CALL", null, ["ram:47b054:8"]]
- 006d9a84 bytes ac84f697
+ 006d9e34 bytes 8884f697
- 006d9aac ["INT_ADD", "register:40f0:8", ["const:6d9aac:8", "const:4:8"]]
- 006d9aac ["CALL", null, ["ram:47ad34:8"]]
+ 006d9e5c ["INT_ADD", "register:40f0:8", ["const:6d9e5c:8", "const:4:8"]]
+ 006d9e5c ["CALL", null, ["ram:47b054:8"]]
- 006d9aac bytes a284f697
+ 006d9e5c bytes 7e84f697
- 006d9a64 ["INT_ADD", "register:40f0:8", ["const:6d9a64:8", "const:4:8"]]
- 006d9a64 ["CALL", null, ["callee:008b7ea8:8"]]
+ 006d9e14 ["INT_ADD", "register:40f0:8", ["const:6d9e14:8", "const:4:8"]]
+ 006d9e14 ["CALL", null, ["callee:008b7ea8:8"]]
- 006d9a64 bytes 26750794
+ 006d9e14 bytes 25780794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac34cda83694c6ce9366d48a638469ad"></a>

### [`006d9af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md) → [`006d9ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9ea0.md) FUN_006d9ea0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d9ec4",
      "incomplete_value": false,
      "site": "006d9ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9b14",
      "incomplete_value": false,
      "site": "006d9b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "006d9ec4",
      "DATA",
      [
        "storage",
        "00c76768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9ec4",
      "DATA",
      [
        "storage",
        "00c77738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md#insn-006d9b04) · [`006d9b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md#insn-006d9b0c) · [`006d9b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md#insn-006d9b10)
- 新版 [`006d9eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9ea0.md#insn-006d9eb4) · [`006d9ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9ea0.md#insn-006d9ebc) · [`006d9ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d9/006d9ea0.md#insn-006d9ec0)

~~~diff
- 006d9b04 ["INT_ADD", "register:40f0:8", ["const:6d9b04:8", "const:4:8"]]
- 006d9b04 ["CALL", null, ["callee:00c58f30:8"]]
+ 006d9eb4 ["INT_ADD", "register:40f0:8", ["const:6d9eb4:8", "const:4:8"]]
+ 006d9eb4 ["CALL", null, ["callee:00c58f30:8"]]
- 006d9b04 bytes 17f91594
+ 006d9eb4 bytes 1ffc1594
- 006d9b0c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006d9ebc ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d9b0c bytes e82c00b0
+ 006d9ebc bytes e82c00d0
- 006d9b10 ["COPY", "tmp:0:8", ["const:768:8"]]
- 006d9b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9ec0 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 006d9ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9b10 bytes 08a11d91
+ 006d9ec0 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85c31b884e5b7d8563a19f85d9f04f63"></a>

### [`006d9cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9cbc.md) → [`006da06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da06c.md) FUN_006da06c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006da08c",
      "incomplete_value": false,
      "site": "006da090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9cdc",
      "incomplete_value": false,
      "site": "006d9ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "006da090",
      "DATA",
      [
        "storage",
        "00c767e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da090",
      "DATA",
      [
        "storage",
        "00c777b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9cbc.md#insn-006d9cd0) · [`006d9cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9cbc.md#insn-006d9cd8) · [`006d9cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9cbc.md#insn-006d9cdc)
- 新版 [`006da080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da06c.md#insn-006da080) · [`006da088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da06c.md#insn-006da088) · [`006da08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da06c.md#insn-006da08c)

~~~diff
- 006d9cd0 ["INT_ADD", "register:40f0:8", ["const:6d9cd0:8", "const:4:8"]]
- 006d9cd0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006da080 ["INT_ADD", "register:40f0:8", ["const:6da080:8", "const:4:8"]]
+ 006da080 ["CALL", null, ["callee:00c58f30:8"]]
- 006d9cd0 bytes a4f81594
+ 006da080 bytes acfb1594
- 006d9cd8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006da088 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d9cd8 bytes e82c00b0
+ 006da088 bytes e82c00b0
- 006d9cdc ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 006d9cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da08c ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 006da08c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da08c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da08c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9cdc bytes 08a11f91
+ 006da08c bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51dcfb0cedc8e5220c44a5eb73f09903"></a>

### [`006d9d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9d14.md) → [`006da0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da0c4.md) FUN_006da0c4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da0f8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9d48",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da104",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d9d54",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006da0f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006da104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006da0f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006da104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9d14.md#insn-006d9d48) · [`006d9d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9d14.md#insn-006d9d54) · [`006d9de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9d14.md#insn-006d9de0)
- 新版 [`006da0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da0c4.md#insn-006da0f8) · [`006da104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da0c4.md#insn-006da104) · [`006da190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da0c4.md#insn-006da190)

~~~diff
- 006d9d48 ["INT_ADD", "register:40f0:8", ["const:6d9d48:8", "const:4:8"]]
- 006d9d48 ["CALL", null, ["ram:47ad34:8"]]
+ 006da0f8 ["INT_ADD", "register:40f0:8", ["const:6da0f8:8", "const:4:8"]]
+ 006da0f8 ["CALL", null, ["ram:47b054:8"]]
- 006d9d48 bytes fb83f697
+ 006da0f8 bytes d783f697
- 006d9d54 ["INT_ADD", "register:40f0:8", ["const:6d9d54:8", "const:4:8"]]
- 006d9d54 ["CALL", null, ["ram:47ad34:8"]]
+ 006da104 ["INT_ADD", "register:40f0:8", ["const:6da104:8", "const:4:8"]]
+ 006da104 ["CALL", null, ["ram:47b054:8"]]
- 006d9d54 bytes f883f697
+ 006da104 bytes d483f697
- 006d9de0 ["INT_ADD", "register:40f0:8", ["const:6d9de0:8", "const:4:8"]]
- 006d9de0 ["CALL", null, ["callee:00c58f30:8"]]
+ 006da190 ["INT_ADD", "register:40f0:8", ["const:6da190:8", "const:4:8"]]
+ 006da190 ["CALL", null, ["callee:00c58f30:8"]]
- 006d9de0 bytes 60f81594
+ 006da190 bytes 68fb1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eda2d8daba5af7d59dfd79a01c4d1b1e"></a>

### [`006d9fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9fd8.md) → [`006da388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da388.md) FUN_006da388

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006da3a8",
      "incomplete_value": false,
      "site": "006da3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d9ff8",
      "incomplete_value": false,
      "site": "006d9ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "006da3ac",
      "DATA",
      [
        "storage",
        "00c76868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da3ac",
      "DATA",
      [
        "storage",
        "00c77838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9fd8.md#insn-006d9fec) · [`006d9ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9fd8.md#insn-006d9ff4) · [`006d9ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9fd8.md#insn-006d9ff8)
- 新版 [`006da39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da388.md#insn-006da39c) · [`006da3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da388.md#insn-006da3a4) · [`006da3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da388.md#insn-006da3a8)

~~~diff
- 006d9fec ["INT_ADD", "register:40f0:8", ["const:6d9fec:8", "const:4:8"]]
- 006d9fec ["CALL", null, ["callee:00c58f30:8"]]
+ 006da39c ["INT_ADD", "register:40f0:8", ["const:6da39c:8", "const:4:8"]]
+ 006da39c ["CALL", null, ["callee:00c58f30:8"]]
- 006d9fec bytes ddf71594
+ 006da39c bytes e5fa1594
- 006d9ff4 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006da3a4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d9ff4 bytes e82c00b0
+ 006da3a4 bytes e82c00b0
- 006d9ff8 ["COPY", "tmp:0:8", ["const:868:8"]]
- 006d9ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d9ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d9ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da3a8 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 006da3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d9ff8 bytes 08a12191
+ 006da3a8 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044775ace0c4383da5d9b0c4a9fe21eb"></a>

### [`006da030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da030.md) → [`006da3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da3e0.md) FUN_006da3e0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.87% / 新版 98.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da414",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da064",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da420",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da070",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006da414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006da420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006da414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006da420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da030.md#insn-006da064) · [`006da070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da030.md#insn-006da070) · [`006da0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da030.md#insn-006da0fc)
- 新版 [`006da414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da3e0.md#insn-006da414) · [`006da420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da3e0.md#insn-006da420) · [`006da4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da3e0.md#insn-006da4ac)

~~~diff
- 006da064 ["INT_ADD", "register:40f0:8", ["const:6da064:8", "const:4:8"]]
- 006da064 ["CALL", null, ["ram:47ad34:8"]]
+ 006da414 ["INT_ADD", "register:40f0:8", ["const:6da414:8", "const:4:8"]]
+ 006da414 ["CALL", null, ["ram:47b054:8"]]
- 006da064 bytes 3483f697
+ 006da414 bytes 1083f697
- 006da070 ["INT_ADD", "register:40f0:8", ["const:6da070:8", "const:4:8"]]
- 006da070 ["CALL", null, ["ram:47ad34:8"]]
+ 006da420 ["INT_ADD", "register:40f0:8", ["const:6da420:8", "const:4:8"]]
+ 006da420 ["CALL", null, ["ram:47b054:8"]]
- 006da070 bytes 3183f697
+ 006da420 bytes 0d83f697
- 006da0fc ["INT_ADD", "register:40f0:8", ["const:6da0fc:8", "const:4:8"]]
- 006da0fc ["CALL", null, ["callee:00c58f30:8"]]
+ 006da4ac ["INT_ADD", "register:40f0:8", ["const:6da4ac:8", "const:4:8"]]
+ 006da4ac ["CALL", null, ["callee:00c58f30:8"]]
- 006da0fc bytes 99f71594
+ 006da4ac bytes a1fa1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d286be9e6278c3c311172e39908800"></a>

### [`006da320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da320.md) → [`006da6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da6d0.md) FUN_006da6d0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006da6f0",
      "incomplete_value": false,
      "site": "006da6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da340",
      "incomplete_value": false,
      "site": "006da344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "006da6f4",
      "DATA",
      [
        "storage",
        "00c768e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da6f4",
      "DATA",
      [
        "storage",
        "00c778b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da320.md#insn-006da334) · [`006da33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da320.md#insn-006da33c) · [`006da340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da320.md#insn-006da340)
- 新版 [`006da6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da6d0.md#insn-006da6e4) · [`006da6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da6d0.md#insn-006da6ec) · [`006da6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da6d0.md#insn-006da6f0)

~~~diff
- 006da334 ["INT_ADD", "register:40f0:8", ["const:6da334:8", "const:4:8"]]
- 006da334 ["CALL", null, ["callee:00c58f30:8"]]
+ 006da6e4 ["INT_ADD", "register:40f0:8", ["const:6da6e4:8", "const:4:8"]]
+ 006da6e4 ["CALL", null, ["callee:00c58f30:8"]]
- 006da334 bytes 0bf71594
+ 006da6e4 bytes 13fa1594
- 006da33c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006da6ec ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006da33c bytes e82c0090
+ 006da6ec bytes e82c00b0
- 006da340 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 006da340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006da340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006da340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da6f0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 006da6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006da340 bytes 08a12391
+ 006da6f0 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5bd9afd4c63b575ad3b20799106ed7"></a>

### [`006da378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da378.md) → [`006da728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da728.md) FUN_006da728

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`00a47c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da9a0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da5f0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da9d4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da624",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006da9a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006da9d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006da9a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006da9d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da378.md#insn-006da5f0) · [`006da624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da378.md#insn-006da624) · [`006da438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da378.md#insn-006da438)
- 新版 [`006da9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da728.md#insn-006da9a0) · [`006da9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da728.md#insn-006da9d4) · [`006da7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006da728.md#insn-006da7e8)

~~~diff
- 006da5f0 ["INT_ADD", "register:40f0:8", ["const:6da5f0:8", "const:4:8"]]
- 006da5f0 ["CALL", null, ["ram:47ad34:8"]]
+ 006da9a0 ["INT_ADD", "register:40f0:8", ["const:6da9a0:8", "const:4:8"]]
+ 006da9a0 ["CALL", null, ["ram:47b054:8"]]
- 006da5f0 bytes d181f697
+ 006da9a0 bytes ad81f697
- 006da624 ["INT_ADD", "register:40f0:8", ["const:6da624:8", "const:4:8"]]
- 006da624 ["CALL", null, ["ram:47ad34:8"]]
+ 006da9d4 ["INT_ADD", "register:40f0:8", ["const:6da9d4:8", "const:4:8"]]
+ 006da9d4 ["CALL", null, ["ram:47b054:8"]]
- 006da624 bytes c481f697
+ 006da9d4 bytes a081f697
- 006da438 ["INT_ADD", "register:40f0:8", ["const:6da438:8", "const:4:8"]]
- 006da438 ["CALL", null, ["callee:00c58f30:8"]]
+ 006da7e8 ["INT_ADD", "register:40f0:8", ["const:6da7e8:8", "const:4:8"]]
+ 006da7e8 ["CALL", null, ["callee:00c58f30:8"]]
- 006da438 bytes caf61594
+ 006da7e8 bytes d2f91594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2a9da4d7f4c9ee6d137741fcf8a3af"></a>

### [`006da678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md) → [`006daa28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa28.md) FUN_006daa28

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006daa4c",
      "incomplete_value": false,
      "site": "006daa4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da69c",
      "incomplete_value": false,
      "site": "006da69c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "006daa4c",
      "DATA",
      [
        "storage",
        "00c76968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006daa4c",
      "DATA",
      [
        "storage",
        "00c77938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md#insn-006da68c) · [`006da694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md#insn-006da694) · [`006da698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md#insn-006da698)
- 新版 [`006daa3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa28.md#insn-006daa3c) · [`006daa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa28.md#insn-006daa44) · [`006daa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa28.md#insn-006daa48)

~~~diff
- 006da68c ["INT_ADD", "register:40f0:8", ["const:6da68c:8", "const:4:8"]]
- 006da68c ["CALL", null, ["callee:00c58f30:8"]]
+ 006daa3c ["INT_ADD", "register:40f0:8", ["const:6daa3c:8", "const:4:8"]]
+ 006daa3c ["CALL", null, ["callee:00c58f30:8"]]
- 006da68c bytes 35f61594
+ 006daa3c bytes 3df91594
- 006da694 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006daa44 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006da694 bytes e82c0090
+ 006daa44 bytes e82c00b0
- 006da698 ["COPY", "tmp:0:8", ["const:968:8"]]
- 006da698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006da698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006da698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006daa48 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 006daa48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006daa48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006daa48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006da698 bytes 08a12591
+ 006daa48 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ec427cdf8ab4909a32d9b23814ee869"></a>

### [`006da6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da6c8.md) → [`006daa78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa78.md) FUN_006daa78

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00492480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492480.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dab48",
      "incomplete_value": true,
      "site": "006dab48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:a70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da798",
      "incomplete_value": true,
      "site": "006da798",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ca000:8"
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dab4c",
      "incomplete_value": true,
      "site": "006dab4c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "006da79c",
      "incomplete_value": true,
      "site": "006da79c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006daaac",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006da6fc",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006daaac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006daac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006dab04",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006daaac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006daac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006dab04",
      "DATA",
      [
        "storage",
        "0039b1b8",
        "fde_0039b1b8",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da6c8.md#insn-006da6fc) · [`006da718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da6c8.md#insn-006da718) · [`006da778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da6c8.md#insn-006da778)
- 新版 [`006daaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa78.md#insn-006daaac) · [`006daac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa78.md#insn-006daac8) · [`006dab28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006daa78.md#insn-006dab28)

~~~diff
- 006da6fc ["INT_ADD", "register:40f0:8", ["const:6da6fc:8", "const:4:8"]]
- 006da6fc ["CALL", null, ["ram:47ad34:8"]]
+ 006daaac ["INT_ADD", "register:40f0:8", ["const:6daaac:8", "const:4:8"]]
+ 006daaac ["CALL", null, ["ram:47b054:8"]]
- 006da6fc bytes 8e81f697
+ 006daaac bytes 6a81f697
- 006da718 ["INT_ADD", "register:40f0:8", ["const:6da718:8", "const:4:8"]]
- 006da718 ["CALL", null, ["ram:47ad34:8"]]
+ 006daac8 ["INT_ADD", "register:40f0:8", ["const:6daac8:8", "const:4:8"]]
+ 006daac8 ["CALL", null, ["ram:47b054:8"]]
- 006da718 bytes 8781f697
+ 006daac8 bytes 6381f697
- 006da778 ["INT_ADD", "register:40f0:8", ["const:6da778:8", "const:4:8"]]
- 006da778 ["CALL", null, ["ram:48cd38:8"]]
+ 006dab28 ["INT_ADD", "register:40f0:8", ["const:6dab28:8", "const:4:8"]]
+ 006dab28 ["CALL", null, ["ram:48d058:8"]]
- 006da778 bytes 70c9f697
+ 006dab28 bytes 4cc9f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b8fecfd39f967642119a9a9d778269"></a>

### [`006da874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da874.md) → [`006dac24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dac24.md) _INIT_109

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dac60",
      "incomplete_value": true,
      "site": "006dac7c",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da8b0",
      "incomplete_value": true,
      "site": "006da8cc",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dac84",
      "incomplete_value": true,
      "site": "006daca0",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da8d4",
      "incomplete_value": true,
      "site": "006da8f0",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
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
      "definition_site": "006daca4",
      "incomplete_value": true,
      "site": "006dacc0",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006da8f4",
      "incomplete_value": true,
      "site": "006da910",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
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
      "006dac60",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "006dac84",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "006daca4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dac60",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "006dac84",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "006daca4",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006daaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da874.md#insn-006daaa8) · [`006da89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da874.md#insn-006da89c) · [`006da8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da874.md#insn-006da8a0)
- 新版 [`006dae58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dac24.md#insn-006dae58) · [`006dac4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dac24.md#insn-006dac4c) · [`006dac50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dac24.md#insn-006dac50)

~~~diff
- 006daaa8 ["INT_ADD", "register:40f0:8", ["const:6daaa8:8", "const:4:8"]]
- 006daaa8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006dae58 ["INT_ADD", "register:40f0:8", ["const:6dae58:8", "const:4:8"]]
+ 006dae58 ["CALL", null, ["callee:00c58ed0:8"]]
- 006daaa8 bytes 16f51594
+ 006dae58 bytes 1ef81594
- 006da89c ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 006dac4c ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 006da89c bytes 732e00b0
+ 006dac4c bytes 732e00d0
- 006da8a0 ["COPY", "tmp:0:8", ["const:878:8"]]
- 006da8a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006da8a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006da8a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006dac50 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 006dac50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006dac50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006dac50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006da8a0 bytes 73e22191
+ 006dac50 bytes 73e22091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95aa2fc9f868f2583fd88c0921573f33"></a>

### [`006dadcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dadcc.md) → [`006db17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md) FUN_006db17c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 9件 [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`006dac04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dac04.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00b12e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12e14.md) · 呼出先 9件 [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md) [`006dafb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006da/006dafb4.md) [`00b1217c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b1217c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.00% / 新版 89.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006db1b0",
      "incomplete_value": false,
      "site": "006db1b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dae00",
      "incomplete_value": false,
      "site": "006dae08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "definition_site": "006db26c",
      "incomplete_value": true,
      "site": "006db270",
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
      "definition_site": "006daebc",
      "incomplete_value": true,
      "site": "006daec0",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006db268",
      "incomplete_value": true,
      "site": "006db274",
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
      "definition_site": "006daeb8",
      "incomplete_value": true,
      "site": "006daec4",
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
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006db1b8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "006db1cc",
      "READ",
      [
        "storage",
        "002b76bb",
        null,
        "string"
      ]
    ],
    [
      "006db25c",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006db1b8",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "006db1cc",
      "READ",
      [
        "storage",
        "002b778a",
        null,
        "string"
      ]
    ],
    [
      "006db25c",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dadf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dadcc.md#insn-006dadf8) · [`006dadfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dadcc.md#insn-006dadfc) · [`006dae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006dadcc.md#insn-006dae00)
- 新版 [`006db1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md#insn-006db1a8) · [`006db1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md#insn-006db1ac) · [`006db1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db17c.md#insn-006db1b0)

~~~diff
- 006dadf8 ["INT_ADD", "register:40f0:8", ["const:6dadf8:8", "const:4:8"]]
- 006dadf8 ["CALL", null, ["callee:00488180:8"]]
+ 006db1a8 ["INT_ADD", "register:40f0:8", ["const:6db1a8:8", "const:4:8"]]
+ 006db1a8 ["CALL", null, ["callee:00488180:8"]]
- 006dadf8 bytes 1ab4f697
+ 006db1a8 bytes f6b3f697
- 006dadfc ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 006db1ac ["COPY", "register:4040:8", ["const:c65000:8"]]
- 006dadfc bytes 482c00d0
+ 006db1ac bytes 482c00d0
- 006dae00 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 006dae00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006dae00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006dae00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006db1b0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 006db1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006db1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006db1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006dae00 bytes 08213891
+ 006db1b0 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7870d99a68f43bd18543d3f84dfea99"></a>

### [`006db120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db120.md) → [`006db4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db4d0.md) FUN_006db4d0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`00b12e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12e14.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006db510",
      "incomplete_value": false,
      "site": "006db514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db160",
      "incomplete_value": false,
      "site": "006db164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006db530",
      "incomplete_value": true,
      "site": "006db53c",
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db180",
      "incomplete_value": true,
      "site": "006db18c",
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
                "const:9c0:8"
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
      "definition_site": "006db52c",
      "incomplete_value": true,
      "site": "006db540",
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
                "const:a74:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db17c",
      "incomplete_value": true,
      "site": "006db190",
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
                "const:9a7:8"
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
      "006db514",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "006db52c",
      "READ",
      [
        "storage",
        "002ad9a7",
        null,
        "string"
      ]
    ],
    [
      "006db52c",
      "READ",
      [
        "storage",
        "002ad9b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006db514",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "006db52c",
      "READ",
      [
        "storage",
        "002ada74",
        null,
        "string"
      ]
    ],
    [
      "006db52c",
      "READ",
      [
        "storage",
        "002ada84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006db158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db120.md#insn-006db158) · [`006db15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db120.md#insn-006db15c) · [`006db160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db120.md#insn-006db160)
- 新版 [`006db508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db4d0.md#insn-006db508) · [`006db50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db4d0.md#insn-006db50c) · [`006db510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db4d0.md#insn-006db510)

~~~diff
- 006db158 ["INT_ADD", "register:40f0:8", ["const:6db158:8", "const:4:8"]]
- 006db158 ["CALL", null, ["callee:00488180:8"]]
+ 006db508 ["INT_ADD", "register:40f0:8", ["const:6db508:8", "const:4:8"]]
+ 006db508 ["CALL", null, ["callee:00488180:8"]]
- 006db158 bytes 42b3f697
+ 006db508 bytes 1eb3f697
- 006db15c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 006db50c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 006db15c bytes 482c00b0
+ 006db50c bytes 482c00d0
- 006db160 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 006db160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006db160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006db160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006db510 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 006db510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006db510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006db510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006db160 bytes 08213891
+ 006db510 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af2fc7f10d52d4c0582995719c35f3d"></a>

### [`006db438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db438.md) → [`006db7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db7e8.md) FUN_006db7e8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 27件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 1件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 27件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.68% / 新版 89.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006db8a4",
      "incomplete_value": true,
      "site": "006db8b8",
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
                "const:31f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db4f4",
      "incomplete_value": true,
      "site": "006db508",
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
                "const:2df:8"
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
      "definition_site": "006db8d8",
      "incomplete_value": true,
      "site": "006db8e4",
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
                "const:2c1000:8"
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
    "old": {
      "definition_site": "006db528",
      "incomplete_value": true,
      "site": "006db534",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:536:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006dba28",
      "incomplete_value": false,
      "site": "006dba28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006db678",
      "incomplete_value": false,
      "site": "006db678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006db864",
      "READ",
      [
        "storage",
        "00ca7e14",
        null,
        "undefined4"
      ]
    ],
    [
      "006db880",
      "READ",
      [
        "storage",
        "00ca7e10",
        null,
        "undefined4"
      ]
    ],
    [
      "006db8a4",
      "READ",
      [
        "storage",
        "0029f2df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006db864",
      "READ",
      [
        "storage",
        "00ca8dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "006db880",
      "READ",
      [
        "storage",
        "00ca8dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "006db8a4",
      "READ",
      [
        "storage",
        "0029f31f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006db5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db438.md#insn-006db5a4) · [`006db5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db438.md#insn-006db5b0) · [`006db7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006db438.md#insn-006db7dc)
- 新版 [`006db954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db7e8.md#insn-006db954) · [`006db960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db7e8.md#insn-006db960) · [`006dbb8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006db7e8.md#insn-006dbb8c)

~~~diff
- 006db5a4 ["INT_ADD", "register:40f0:8", ["const:6db5a4:8", "const:4:8"]]
- 006db5a4 ["CALL", null, ["ram:6648e0:8"]]
+ 006db954 ["INT_ADD", "register:40f0:8", ["const:6db954:8", "const:4:8"]]
+ 006db954 ["CALL", null, ["ram:664c90:8"]]
- 006db5a4 bytes cf24fe97
+ 006db954 bytes cf24fe97
- 006db5b0 ["COPY", "tmp:0:8", ["const:59:8"]]
- 006db5b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006db5b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006db5b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006db960 ["COPY", "tmp:0:8", ["const:137:8"]]
+ 006db960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006db960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006db960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006db5b0 bytes 29650191
+ 006db960 bytes 29dd0491
- 006db7dc ["INT_ADD", "register:40f0:8", ["const:6db7dc:8", "const:4:8"]]
- 006db7dc ["CALL", null, ["callee:0047e96c:8"]]
+ 006dbb8c ["INT_ADD", "register:40f0:8", ["const:6dbb8c:8", "const:4:8"]]
+ 006dbb8c ["CALL", null, ["callee:0047e96c:8"]]
- 006db7dc bytes 9c8bf697
+ 006dbb8c bytes 788bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a991487665567e78d4623084de9063"></a>

### [`006dc16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc16c.md) → [`006dc51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc51c.md) FUN_006dc51c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006dbe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbe00.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0071d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d08c.md) [`00728890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/00728890.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006dc1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc1b0.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0071d43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d43c.md) [`00728c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00728/00728c40.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006dc77c",
      "incomplete_value": false,
      "site": "006dc780",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc3cc",
      "incomplete_value": false,
      "site": "006dc3d0",
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
            "const:170:8"
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
      "006dc77c",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ],
    [
      "006dc7a8",
      "READ",
      [
        "storage",
        "00ca7e14",
        null,
        "undefined4"
      ]
    ],
    [
      "006dc7c4",
      "READ",
      [
        "storage",
        "00ca7e10",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "006dc77c",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ],
    [
      "006dc7a8",
      "READ",
      [
        "storage",
        "00ca8dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "006dc7c4",
      "READ",
      [
        "storage",
        "00ca8dd0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dc3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc16c.md#insn-006dc3d0) · [`006dc22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc16c.md#insn-006dc22c) · [`006dc2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc16c.md#insn-006dc2bc)
- 新版 [`006dc780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc51c.md#insn-006dc780) · [`006dc5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc51c.md#insn-006dc5dc) · [`006dc66c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc51c.md#insn-006dc66c)

~~~diff
- 006dc3d0 ["INT_ADD", "register:40f0:8", ["const:6dc3d0:8", "const:4:8"]]
- 006dc3d0 ["CALL", null, ["callee:00442c90:8"]]
+ 006dc780 ["INT_ADD", "register:40f0:8", ["const:6dc780:8", "const:4:8"]]
+ 006dc780 ["CALL", null, ["callee:00442c90:8"]]
- 006dc3d0 bytes 6899f597
+ 006dc780 bytes 4499f597
- 006dc22c ["INT_ADD", "register:40f0:8", ["const:6dc22c:8", "const:4:8"]]
- 006dc22c ["CALL", null, ["callee:0071d43c:8"]]
+ 006dc5dc ["INT_ADD", "register:40f0:8", ["const:6dc5dc:8", "const:4:8"]]
+ 006dc5dc ["CALL", null, ["callee:0071d43c:8"]]
- 006dc22c bytes 98030194
+ 006dc5dc bytes 98030194
- 006dc2bc ["INT_ADD", "register:40f0:8", ["const:6dc2bc:8", "const:4:8"]]
- 006dc2bc ["CALL", null, ["callee:00c58f30:8"]]
+ 006dc66c ["INT_ADD", "register:40f0:8", ["const:6dc66c:8", "const:4:8"]]
+ 006dc66c ["CALL", null, ["callee:00c58f30:8"]]
- 006dc2bc bytes 29ef1594
+ 006dc66c bytes 31f21594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d525f71ae5acc2003aeb1e9a3290c48"></a>

### [`006dc998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc998.md) → [`006dcd48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcd48.md) FUN_006dcd48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f06ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f06ac.md) · 呼出先 18件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0046f6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f6ac.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md)
- 新版 呼出元 1件 [`006f0a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0a5c.md) · 呼出先 18件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md) [`0046f9cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f9cc.md) [`0046fa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046fa44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.60% / 新版 87.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 7件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dcd8c",
      "incomplete_value": true,
      "site": "006dcd9c",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:3dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc9dc",
      "incomplete_value": true,
      "site": "006dc9ec",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "006dcd8c",
      "incomplete_value": true,
      "site": "006dcda0",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:3dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dc9dc",
      "incomplete_value": true,
      "site": "006dc9f0",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
      "definition_site": "006dcdc4",
      "incomplete_value": true,
      "site": "006dcdd8",
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
                "const:efe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dca14",
      "incomplete_value": true,
      "site": "006dca28",
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
                "const:eb4:8"
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
      "006dcd78",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "006dcd8c",
      "READ",
      [
        "storage",
        "002a2312",
        null,
        "string"
      ]
    ],
    [
      "006dcdc4",
      "READ",
      [
        "storage",
        "002b2eb4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dcd78",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "006dcd8c",
      "READ",
      [
        "storage",
        "002a23dd",
        null,
        "string"
      ]
    ],
    [
      "006dcdc4",
      "READ",
      [
        "storage",
        "002b2efe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dca44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc998.md#insn-006dca44) · [`006dca64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc998.md#insn-006dca64) · [`006dcae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc998.md#insn-006dcae4)
- 新版 [`006dcdf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcd48.md#insn-006dcdf4) · [`006dce14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcd48.md#insn-006dce14) · [`006dce94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcd48.md#insn-006dce94)

~~~diff
- 006dca44 ["INT_ADD", "register:40f0:8", ["const:6dca44:8", "const:4:8"]]
- 006dca44 ["CALL", null, ["callee:00448254:8"]]
+ 006dcdf4 ["INT_ADD", "register:40f0:8", ["const:6dcdf4:8", "const:4:8"]]
+ 006dcdf4 ["CALL", null, ["callee:00448254:8"]]
- 006dca44 bytes 3cadf597
+ 006dcdf4 bytes 18adf597
- 006dca64 ["INT_ADD", "register:40f0:8", ["const:6dca64:8", "const:4:8"]]
- 006dca64 ["CALL", null, ["callee:0047e96c:8"]]
+ 006dce14 ["INT_ADD", "register:40f0:8", ["const:6dce14:8", "const:4:8"]]
+ 006dce14 ["CALL", null, ["callee:0047e96c:8"]]
- 006dca64 bytes fa86f697
+ 006dce14 bytes d686f697
- 006dcae4 ["INT_ADD", "register:40f0:8", ["const:6dcae4:8", "const:4:8"]]
- 006dcae4 ["CALL", null, ["callee:00c58f20:8"]]
+ 006dce94 ["INT_ADD", "register:40f0:8", ["const:6dce94:8", "const:4:8"]]
+ 006dce94 ["CALL", null, ["callee:00c58f20:8"]]
- 006dcae4 bytes 1bed1594
+ 006dce94 bytes 23f01594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af86d5874761950721b259cd4c758880"></a>

### [`006dd4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd4c8.md) → [`006dd878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006dd878.md) FUN_006dd878

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 10件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 10件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dd8bc",
      "incomplete_value": true,
      "site": "006dd8cc",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:3dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dd50c",
      "incomplete_value": true,
      "site": "006dd51c",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
      "definition_site": "006dd8ec",
      "incomplete_value": true,
      "site": "006dd900",
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
                "const:efe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dd53c",
      "incomplete_value": true,
      "site": "006dd550",
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
                "const:eb4:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006dda60",
      "incomplete_value": false,
      "site": "006dda60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
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
      "definition_site": "006dd6b0",
      "incomplete_value": false,
      "site": "006dd6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "006dd8a8",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd8bc",
      "READ",
      [
        "storage",
        "002a2312",
        null,
        "string"
      ]
    ],
    [
      "006dd8ec",
      "READ",
      [
        "storage",
        "002b2eb4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dd8a8",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd8bc",
      "READ",
      [
        "storage",
        "002a23dd",
        null,
        "string"
      ]
    ],
    [
      "006dd8ec",
      "READ",
      [
        "storage",
        "002b2efe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dd584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd4c8.md#insn-006dd584) · [`006dd688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd4c8.md#insn-006dd688) · [`006dd6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd4c8.md#insn-006dd6c8)
- 新版 [`006dd934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006dd878.md#insn-006dd934) · [`006dda38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006dd878.md#insn-006dda38) · [`006dda78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006dd878.md#insn-006dda78)

~~~diff
- 006dd584 ["INT_ADD", "register:40f0:8", ["const:6dd584:8", "const:4:8"]]
- 006dd584 ["CALL", null, ["callee:0047e96c:8"]]
+ 006dd934 ["INT_ADD", "register:40f0:8", ["const:6dd934:8", "const:4:8"]]
+ 006dd934 ["CALL", null, ["callee:0047e96c:8"]]
- 006dd584 bytes 3284f697
+ 006dd934 bytes 0e84f697
- 006dd688 ["INT_ADD", "register:40f0:8", ["const:6dd688:8", "const:4:8"]]
- 006dd688 ["CALL", null, ["callee:00c58ef0:8"]]
+ 006dda38 ["INT_ADD", "register:40f0:8", ["const:6dda38:8", "const:4:8"]]
+ 006dda38 ["CALL", null, ["callee:00c58ef0:8"]]
- 006dd688 bytes 26ea1594
+ 006dda38 bytes 2eed1594
- 006dd6c8 ["INT_ADD", "register:40f0:8", ["const:6dd6c8:8", "const:4:8"]]
- 006dd6c8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 006dda78 ["INT_ADD", "register:40f0:8", ["const:6dda78:8", "const:4:8"]]
+ 006dda78 ["CALL", null, ["callee:00c58ed0:8"]]
- 006dd6c8 bytes 0eea1594
+ 006dda78 bytes 16ed1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aa9105064adb4defcd970f3ab8fb2d9"></a>

### [`006dd77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd77c.md) → [`006ddb2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006ddb2c.md) FUN_006ddb2c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006b2bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 5件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee98.md) [`006dc95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc95c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`006b2f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 5件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046f1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f1b8.md) [`006dcd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcd0c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006de0cc",
      "incomplete_value": true,
      "site": "006de0dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ddd1c",
      "incomplete_value": true,
      "site": "006ddd2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006de244",
      "incomplete_value": true,
      "site": "006de254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "006dde94",
      "incomplete_value": true,
      "site": "006ddea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ddb4c",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[39]"
      ]
    ],
    [
      "006ddb60",
      "DATA",
      [
        "storage",
        "004341b0",
        "fde_004341b0",
        "dword"
      ]
    ],
    [
      "006ddb74",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "byte[39]"
      ]
    ]
  ],
  "added": [
    [
      "006ddb4c",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "dword"
      ]
    ],
    [
      "006ddb60",
      "DATA",
      [
        "storage",
        "004341b0",
        null,
        "byte[27]"
      ]
    ],
    [
      "006ddb74",
      "DATA",
      [
        "storage",
        "0042efb0",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dd790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd77c.md#insn-006dd790) · [`006dd7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd77c.md#insn-006dd7a4) · [`006dd7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd77c.md#insn-006dd7b8)
- 新版 [`006ddb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006ddb2c.md#insn-006ddb40) · [`006ddb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006ddb2c.md#insn-006ddb54) · [`006ddb68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dd/006ddb2c.md#insn-006ddb68)

~~~diff
- 006dd790 ["INT_ADD", "register:40f0:8", ["const:6dd790:8", "const:4:8"]]
- 006dd790 ["CALL", null, ["callee:008524fc:8"]]
+ 006ddb40 ["INT_ADD", "register:40f0:8", ["const:6ddb40:8", "const:4:8"]]
+ 006ddb40 ["CALL", null, ["callee:008524fc:8"]]
- 006dd790 bytes 70cf0594
+ 006ddb40 bytes 6fd20594
- 006dd7a4 ["INT_ADD", "register:40f0:8", ["const:6dd7a4:8", "const:4:8"]]
- 006dd7a4 ["CALL", null, ["callee:008524fc:8"]]
+ 006ddb54 ["INT_ADD", "register:40f0:8", ["const:6ddb54:8", "const:4:8"]]
+ 006ddb54 ["CALL", null, ["callee:008524fc:8"]]
- 006dd7a4 bytes 6bcf0594
+ 006ddb54 bytes 6ad20594
- 006dd7b8 ["INT_ADD", "register:40f0:8", ["const:6dd7b8:8", "const:4:8"]]
- 006dd7b8 ["CALL", null, ["callee:008524fc:8"]]
+ 006ddb68 ["INT_ADD", "register:40f0:8", ["const:6ddb68:8", "const:4:8"]]
+ 006ddb68 ["CALL", null, ["callee:008524fc:8"]]
- 006dd7b8 bytes 66cf0594
+ 006ddb68 bytes 65d20594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818d501bc7e64ef87d69da34d94ff301"></a>

### [`006dfe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md) → [`006e01d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e01d0.md) FUN_006e01d0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`00b12e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12e14.md) · 呼出先 19件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 96.28% / 新版 96.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e030c",
      "incomplete_value": true,
      "site": "006e0320",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006dff5c",
      "incomplete_value": true,
      "site": "006dff70",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:fad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006e0280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006e0284"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e022c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "006e030c",
      "READ",
      [
        "storage",
        "002a9fad",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006e0270",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006e022c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "006e030c",
      "READ",
      [
        "storage",
        "002aa07a",
        null,
        "string"
      ]
    ],
    [
      "006e0620",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e0280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md#insn-006e0280) · [`006e0284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md#insn-006e0284) · [`006e0290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfe20.md#insn-006e0290)

~~~diff
- 006e0280 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
- 006e0280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006e0280 bytes e88300f9
- 006e0284 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:148:8"]]
- 006e0284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006e0284 bytes e9a700f9
- 006e0290 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006e0290 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006e0290 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 006e0290 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 006e0290 bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f49a3c39b1cf27748f9b96c93af111e"></a>

### [`006e0504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0504.md) → [`006e08b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e08b4.md) FUN_006e08b4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e08f4",
      "incomplete_value": false,
      "site": "006e08f8",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e0544",
      "incomplete_value": false,
      "site": "006e0548",
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
            "const:170:8"
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
      "006e08f4",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e08f4",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e0548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0504.md#insn-006e0548) · [`006e0544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0504.md#insn-006e0544)
- 新版 [`006e08f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e08b4.md#insn-006e08f8) · [`006e08f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e0/006e08b4.md#insn-006e08f4)

~~~diff
- 006e0548 ["INT_ADD", "register:40f0:8", ["const:6e0548:8", "const:4:8"]]
- 006e0548 ["CALL", null, ["callee:00442c90:8"]]
+ 006e08f8 ["INT_ADD", "register:40f0:8", ["const:6e08f8:8", "const:4:8"]]
+ 006e08f8 ["CALL", null, ["callee:00442c90:8"]]
- 006e0548 bytes 0a89f597
+ 006e08f8 bytes e688f597
- 006e0544 ["COPY", "tmp:0:8", ["const:170:8"]]
- 006e0544 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006e0544 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006e0544 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006e08f4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 006e08f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006e08f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006e08f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006e0544 bytes 00c00591
+ 006e08f4 bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7277041f3c615a75bdc788ca2f700e12"></a>

### [`006e1638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md) → [`006e19e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e1/006e19e8.md) FUN_006e19e8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 24件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c0.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 24件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0046ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ead0.md) [`0046eae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e1b18",
      "incomplete_value": true,
      "site": "006e1b18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:471:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e1768",
      "incomplete_value": true,
      "site": "006e1768",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:427:8"
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
      "definition_site": "006e1c24",
      "incomplete_value": true,
      "site": "006e1c24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e1874",
      "incomplete_value": true,
      "site": "006e1874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006e1eac",
      "incomplete_value": false,
      "site": "006e1eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
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
      "definition_site": "006e1afc",
      "incomplete_value": false,
      "site": "006e1afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "006e1a18",
      "DATA",
      [
        "storage",
        "00434658",
        null,
        "byte[35]"
      ]
    ],
    [
      "006e1a20",
      "DATA",
      [
        "storage",
        "00434680",
        null,
        "byte[35]"
      ]
    ],
    [
      "006e1a64",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e1a18",
      "DATA",
      [
        "storage",
        "00434658",
        null,
        "byte[67]"
      ]
    ],
    [
      "006e1a20",
      "DATA",
      [
        "storage",
        "00434680",
        null,
        "byte[67]"
      ]
    ],
    [
      "006e1a64",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e16b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md#insn-006e16b8) · [`006e1750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md#insn-006e1750) · [`006e17bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1638.md#insn-006e17bc)
- 新版 [`006e1a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e1/006e19e8.md#insn-006e1a68) · [`006e1b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e1/006e19e8.md#insn-006e1b00) · [`006e1b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e1/006e19e8.md#insn-006e1b6c)

~~~diff
- 006e16b8 ["INT_ADD", "register:40f0:8", ["const:6e16b8:8", "const:4:8"]]
- 006e16b8 ["CALL", null, ["callee:00442c90:8"]]
+ 006e1a68 ["INT_ADD", "register:40f0:8", ["const:6e1a68:8", "const:4:8"]]
+ 006e1a68 ["CALL", null, ["callee:00442c90:8"]]
- 006e16b8 bytes ae84f597
+ 006e1a68 bytes 8a84f597
- 006e1750 ["COPY", "tmp:0:8", ["const:427:8"]]
- 006e1750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006e1750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006e1750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006e1b00 ["COPY", "tmp:0:8", ["const:471:8"]]
+ 006e1b00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006e1b00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006e1b00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006e1750 bytes 299d1091
+ 006e1b00 bytes 29c51191
- 006e17bc ["INT_ADD", "register:40f0:8", ["const:6e17bc:8", "const:4:8"]]
- 006e17bc ["CALL", null, ["callee:0047e96c:8"]]
+ 006e1b6c ["INT_ADD", "register:40f0:8", ["const:6e1b6c:8", "const:4:8"]]
+ 006e1b6c ["CALL", null, ["callee:0047e96c:8"]]
- 006e17bc bytes a473f697
+ 006e1b6c bytes 8073f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d98b33304f4b2bc331faa2b0c1ecd023"></a>

### [`006e2a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2a48.md) → [`006e2df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e2/006e2df8.md) FUN_006e2df8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006e2ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2ccc.md) · 呼出先 11件 [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`004879dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004879dc.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`006e307c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e307c.md) · 呼出先 11件 [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487cfc.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2e34",
      "incomplete_value": false,
      "site": "006e2e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e2a84",
      "incomplete_value": false,
      "site": "006e2a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2e38",
      "incomplete_value": true,
      "site": "006e2e4c",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:3ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e2a88",
      "incomplete_value": true,
      "site": "006e2a9c",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:324:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006e2bdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e2e38",
      "READ",
      [
        "storage",
        "002a2324",
        null,
        "string"
      ]
    ],
    [
      "006e2e40",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006e2bcc",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006e2e38",
      "READ",
      [
        "storage",
        "002a23ef",
        null,
        "string"
      ]
    ],
    [
      "006e2e40",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "006e2f7c",
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e2bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2a48.md#insn-006e2bdc) · [`006e2be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2a48.md#insn-006e2be0) · [`006e2bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2a48.md#insn-006e2bec)

~~~diff
- 006e2bdc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006e2bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006e2bdc bytes e81300f9
- 006e2be0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 006e2be0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006e2be0 bytes e93700f9
- 006e2bec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006e2bec ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006e2bec ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 006e2bec ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 006e2bec bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a691c4f28f3896fc1f18e2b73e48e63"></a>

### [`006e2ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2ccc.md) → [`006e307c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e307c.md) FUN_006e307c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 22件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c0.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 22件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0046ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ead0.md) [`0046eae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eae0.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.37% / 新版 91.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e3154",
      "incomplete_value": true,
      "site": "006e3154",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:471:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e2da4",
      "incomplete_value": true,
      "site": "006e2da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:427:8"
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
      "definition_site": "006e3264",
      "incomplete_value": true,
      "site": "006e3264",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e2eb4",
      "incomplete_value": true,
      "site": "006e2eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006e34a4",
      "incomplete_value": false,
      "site": "006e34a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
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
      "definition_site": "006e30f4",
      "incomplete_value": false,
      "site": "006e30f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "006e30d0",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "006e3144",
      "READ",
      [
        "storage",
        "002c1427",
        null,
        "string"
      ]
    ],
    [
      "006e3198",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e30d0",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "006e3144",
      "READ",
      [
        "storage",
        "002c1471",
        null,
        "string"
      ]
    ],
    [
      "006e3198",
      "PARAM",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e2dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2ccc.md#insn-006e2dfc) · [`006e30d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2ccc.md#insn-006e30d0) · [`006e310c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e2/006e2ccc.md#insn-006e310c)
- 新版 [`006e31ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e307c.md#insn-006e31ac) · [`006e3480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e307c.md#insn-006e3480) · [`006e34bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e307c.md#insn-006e34bc)

~~~diff
- 006e2dfc ["INT_ADD", "register:40f0:8", ["const:6e2dfc:8", "const:4:8"]]
- 006e2dfc ["CALL", null, ["callee:0047e96c:8"]]
+ 006e31ac ["INT_ADD", "register:40f0:8", ["const:6e31ac:8", "const:4:8"]]
+ 006e31ac ["CALL", null, ["callee:0047e96c:8"]]
- 006e2dfc bytes 146ef697
+ 006e31ac bytes f06df697
- 006e30d0 ["INT_ADD", "register:40f0:8", ["const:6e30d0:8", "const:4:8"]]
- 006e30d0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 006e3480 ["INT_ADD", "register:40f0:8", ["const:6e3480:8", "const:4:8"]]
+ 006e3480 ["CALL", null, ["callee:00c58ef0:8"]]
- 006e30d0 bytes 94d31594
+ 006e3480 bytes 9cd61594
- 006e310c ["INT_ADD", "register:40f0:8", ["const:6e310c:8", "const:4:8"]]
- 006e310c ["CALL", null, ["callee:00c58ed0:8"]]
+ 006e34bc ["INT_ADD", "register:40f0:8", ["const:6e34bc:8", "const:4:8"]]
+ 006e34bc ["CALL", null, ["callee:00c58ed0:8"]]
- 006e310c bytes 7dd31594
+ 006e34bc bytes 85d61594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dcb0aa2c668e68ebf4c9e6440ef9d2a"></a>

### [`006e32b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e32b0.md) → [`006e3660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e3660.md) FUN_006e3660

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 5件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee98.md) [`00470120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470120.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 5件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046f1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f1b8.md) [`00470440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470440.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e36c0",
      "incomplete_value": true,
      "site": "006e36d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4050:8"
              ],
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
      "definition_site": "006e3310",
      "incomplete_value": true,
      "site": "006e3324",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:fd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e36c0",
      "READ",
      [
        "storage",
        "002c3fd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e36c0",
      "READ",
      [
        "storage",
        "002c4020",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e32c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e32b0.md#insn-006e32c8) · [`006e32cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e32b0.md#insn-006e32cc) · [`006e32e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e32b0.md#insn-006e32e4)
- 新版 [`006e3678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e3660.md#insn-006e3678) · [`006e367c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e3660.md#insn-006e367c) · [`006e3694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e3/006e3660.md#insn-006e3694)

~~~diff
- 006e32c8 ["INT_ADD", "register:40f0:8", ["const:6e32c8:8", "const:4:8"]]
- 006e32c8 ["CALL", null, ["callee:008524fc:8"]]
+ 006e3678 ["INT_ADD", "register:40f0:8", ["const:6e3678:8", "const:4:8"]]
+ 006e3678 ["CALL", null, ["callee:008524fc:8"]]
- 006e32c8 bytes a2b80594
+ 006e3678 bytes a1bb0594
- 006e32cc ["INT_ADD", "register:40f0:8", ["const:6e32cc:8", "const:4:8"]]
- 006e32cc ["CALL", null, ["callee:0046cd24:8"]]
+ 006e367c ["INT_ADD", "register:40f0:8", ["const:6e367c:8", "const:4:8"]]
+ 006e367c ["CALL", null, ["callee:0046cd24:8"]]
- 006e32cc bytes ce25f697
+ 006e367c bytes aa25f697
- 006e32e4 ["INT_ADD", "register:40f0:8", ["const:6e32e4:8", "const:4:8"]]
- 006e32e4 ["CALL", null, ["callee:0046db10:8"]]
+ 006e3694 ["INT_ADD", "register:40f0:8", ["const:6e3694:8", "const:4:8"]]
+ 006e3694 ["CALL", null, ["callee:0046db10:8"]]
- 006e32e4 bytes 4329f697
+ 006e3694 bytes 1f29f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37db19f38b506f563f0e4be780d66889"></a>

### [`006e4538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md) → [`006e48e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e48e8.md) FUN_006e48e8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006e4dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4dc4.md) [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 2件 [`006e5174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e5174.md) [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) · 呼出先 16件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 83.70% / 新版 83.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 2件, `store_destination` 14件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e4954",
      "incomplete_value": true,
      "site": "006e4960",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e45a4",
      "incomplete_value": true,
      "site": "006e45b0",
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
                "const:490:8"
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
      "definition_site": "006e49cc",
      "incomplete_value": true,
      "site": "006e49d8",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e461c",
      "incomplete_value": true,
      "site": "006e4628",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:fd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e49dc",
      "incomplete_value": true,
      "site": "006e49dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e462c",
      "incomplete_value": true,
      "site": "006e462c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e4954",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "006e498c",
      "DATA",
      [
        "storage",
        "00430ee8",
        null,
        "byte[19]"
      ]
    ],
    [
      "006e49a8",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006e4954",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ],
    [
      "006e498c",
      "DATA",
      [
        "storage",
        "00430ee8",
        null,
        "qword"
      ]
    ],
    [
      "006e49a8",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e45a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md#insn-006e45a4) · [`006e45d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md#insn-006e45d8) · [`006e4630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4538.md#insn-006e4630)
- 新版 [`006e4954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e48e8.md#insn-006e4954) · [`006e4988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e48e8.md#insn-006e4988) · [`006e49e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e48e8.md#insn-006e49e0)

~~~diff
- 006e45a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
- 006e45a4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 006e45a4 ["COPY", "register:5010:8", ["const:0:8"]]
- 006e45a4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 006e4954 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
+ 006e4954 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 006e4954 ["COPY", "register:5010:8", ["const:0:8"]]
+ 006e4954 ["COPY", "register:5018:8", ["const:0:8"]]
- 006e45a4 bytes 0025c13d
+ 006e4954 bytes 0039c13d
- 006e45d8 ["INT_ADD", "register:40f0:8", ["const:6e45d8:8", "const:4:8"]]
- 006e45d8 ["CALL", null, ["callee:008524fc:8"]]
+ 006e4988 ["INT_ADD", "register:40f0:8", ["const:6e4988:8", "const:4:8"]]
+ 006e4988 ["CALL", null, ["callee:008524fc:8"]]
- 006e45d8 bytes deb30594
+ 006e4988 bytes ddb60594
- 006e4630 ["INT_ADD", "register:40f0:8", ["const:6e4630:8", "const:4:8"]]
- 006e4630 ["CALL", null, ["callee:008524fc:8"]]
+ 006e49e0 ["INT_ADD", "register:40f0:8", ["const:6e49e0:8", "const:4:8"]]
+ 006e49e0 ["CALL", null, ["callee:008524fc:8"]]
- 006e4630 bytes c8b30594
+ 006e49e0 bytes c7b60594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5067ae310e36e7be0c08c00f8a07894b"></a>

### [`006e542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md) → [`006e57dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md) FUN_006e57dc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006e4dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4dc4.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md) [`006fe65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fe/006fe65c.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md)
- 新版 呼出元 4件 [`006e5174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e5174.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006ef0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md) [`006fea0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fe/006fea0c.md) · 呼出先 15件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e5848",
      "value": [
        "leaf",
        "ram:9d1320:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e5498",
      "value": [
        "leaf",
        "ram:9d0374:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e594c",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e559c",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e5848",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d0374"
      ]
    ],
    [
      "006e58a0",
      "DATA",
      [
        "storage",
        "00436d8c",
        null,
        "byte[67]"
      ]
    ],
    [
      "006e594c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006e5848",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d1320"
      ]
    ],
    [
      "006e58a0",
      "DATA",
      [
        "storage",
        "00436d8c",
        null,
        "qword"
      ]
    ],
    [
      "006e594c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e5498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md#insn-006e5498) · [`006e559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md#insn-006e559c) · [`006e5464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md#insn-006e5464)
- 新版 [`006e5848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md#insn-006e5848) · [`006e594c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md#insn-006e594c) · [`006e5814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md#insn-006e5814)

~~~diff
- 006e5498 ["INT_ADD", "register:40f0:8", ["const:6e5498:8", "const:4:8"]]
- 006e5498 ["CALL", null, ["ram:9d0374:8"]]
+ 006e5848 ["INT_ADD", "register:40f0:8", ["const:6e5848:8", "const:4:8"]]
+ 006e5848 ["CALL", null, ["ram:9d1320:8"]]
- 006e5498 bytes b7ab0b94
+ 006e5848 bytes b6ae0b94
- 006e559c ["INT_ADD", "register:40f0:8", ["const:6e559c:8", "const:4:8"]]
- 006e559c ["CALL", null, ["ram:6e4b1c:8"]]
+ 006e594c ["INT_ADD", "register:40f0:8", ["const:6e594c:8", "const:4:8"]]
+ 006e594c ["CALL", null, ["ram:6e4ecc:8"]]
- 006e559c bytes 60fdff97
+ 006e594c bytes 60fdff97
- 006e5464 ["INT_ADD", "register:40f0:8", ["const:6e5464:8", "const:4:8"]]
- 006e5464 ["CALL", null, ["callee:0048d1e4:8"]]
+ 006e5814 ["INT_ADD", "register:40f0:8", ["const:6e5814:8", "const:4:8"]]
+ 006e5814 ["CALL", null, ["callee:0048d1e4:8"]]
- 006e5464 bytes 989ef697
+ 006e5814 bytes 749ef697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a635456bfce26a5411d5b0a403db365b"></a>

### [`006e5dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md) → [`006e6178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md) FUN_006e6178

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 59件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 59件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440e60.md) [`0045001c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045001c.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 16件, `call_target` 22件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6a50",
      "incomplete_value": false,
      "site": "006e6a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e66a0",
      "incomplete_value": false,
      "site": "006e66a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6b24",
      "incomplete_value": false,
      "site": "006e6b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e6774",
      "incomplete_value": false,
      "site": "006e6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6c84",
      "incomplete_value": false,
      "site": "006e6c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e68d4",
      "incomplete_value": false,
      "site": "006e68dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e61b4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006e61c0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e61c8",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006e61b4",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006e61c0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e61c8",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e5e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md#insn-006e5e20) · [`006e5ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md#insn-006e5ee8) · [`006e5f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e5dc8.md#insn-006e5f6c)
- 新版 [`006e61d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md#insn-006e61d0) · [`006e6298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md#insn-006e6298) · [`006e631c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e6/006e6178.md#insn-006e631c)

~~~diff
- 006e5e20 ["INT_ADD", "register:40f0:8", ["const:6e5e20:8", "const:4:8"]]
- 006e5e20 ["CALL", null, ["callee:00c596b0:8"]]
+ 006e61d0 ["INT_ADD", "register:40f0:8", ["const:6e61d0:8", "const:4:8"]]
+ 006e61d0 ["CALL", null, ["callee:00c596b0:8"]]
- 006e5e20 bytes 30ca1594
+ 006e61d0 bytes 38cd1594
- 006e5ee8 ["INT_ADD", "register:40f0:8", ["const:6e5ee8:8", "const:4:8"]]
- 006e5ee8 ["CALL", null, ["ram:6e7358:8"]]
+ 006e6298 ["INT_ADD", "register:40f0:8", ["const:6e6298:8", "const:4:8"]]
+ 006e6298 ["CALL", null, ["ram:6e7708:8"]]
- 006e5ee8 bytes 1c050094
+ 006e6298 bytes 1c050094
- 006e5f6c ["INT_ADD", "register:40f0:8", ["const:6e5f6c:8", "const:4:8"]]
- 006e5f6c ["CALL", null, ["ram:6e4b1c:8"]]
+ 006e631c ["INT_ADD", "register:40f0:8", ["const:6e631c:8", "const:4:8"]]
+ 006e631c ["CALL", null, ["ram:6e4ecc:8"]]
- 006e5f6c bytes ecfaff97
+ 006e631c bytes ecfaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70eef47aa40742a4242481d48c5ff5ca"></a>

### [`006e79e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md) → [`006e7d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md) FUN_006e7d98

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006f8a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md) · 呼出先 12件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md)
- 新版 呼出元 1件 [`006f8e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md) · 呼出先 12件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006e7dc8",
      "incomplete_value": true,
      "site": "006e7dc8",
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
      "definition_site": "006e7a18",
      "incomplete_value": true,
      "site": "006e7a18",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e7dd0",
      "incomplete_value": false,
      "site": "006e7de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e7a20",
      "incomplete_value": false,
      "site": "006e7a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "006e7dd8",
      "incomplete_value": false,
      "site": "006e7de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e7a28",
      "incomplete_value": false,
      "site": "006e7a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "006e7dc4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006e7dd0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e7dd8",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006e7dc4",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006e7dd0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e7dd8",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e7a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md#insn-006e7a30) · [`006e7a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md#insn-006e7a0c) · [`006e7a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md#insn-006e7a14)
- 新版 [`006e7de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md#insn-006e7de0) · [`006e7dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md#insn-006e7dbc) · [`006e7dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md#insn-006e7dc4)

~~~diff
- 006e7a30 ["INT_ADD", "register:40f0:8", ["const:6e7a30:8", "const:4:8"]]
- 006e7a30 ["CALL", null, ["callee:00c596b0:8"]]
+ 006e7de0 ["INT_ADD", "register:40f0:8", ["const:6e7de0:8", "const:4:8"]]
+ 006e7de0 ["CALL", null, ["callee:00c596b0:8"]]
- 006e7a30 bytes 2cc31594
+ 006e7de0 bytes 34c61594
- 006e7a0c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 006e7dbc ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 006e7a0c bytes e82d00b0
+ 006e7dbc bytes e82d00d0
- 006e7a14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 006e7a14 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006e7dc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a38:8"]]
+ 006e7dc4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006e7a14 bytes 003d45f9
+ 006e7dc4 bytes 001d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c43da1ac0e9838acf7d913e4470267f"></a>

### [`006e7c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7c98.md) → [`006e8048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8048.md) FUN_006e8048

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006e79e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e79e8.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0046af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md)
- 新版 呼出元 1件 [`006e7d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e7/006e7d98.md) · 呼出先 15件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`0046a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046a5b0.md) [`0046b278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b278.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006e809c",
      "incomplete_value": true,
      "site": "006e809c",
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
      "definition_site": "006e7cec",
      "incomplete_value": true,
      "site": "006e7cec",
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
      "definition_site": "006e80a4",
      "incomplete_value": false,
      "site": "006e80b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e7cf4",
      "incomplete_value": false,
      "site": "006e7d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "006e80ac",
      "incomplete_value": false,
      "site": "006e80b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e7cfc",
      "incomplete_value": false,
      "site": "006e7d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "006e8098",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006e80a4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e80ac",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006e8098",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006e80a4",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e80ac",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e7d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7c98.md#insn-006e7d08) · [`006e8370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7c98.md#insn-006e8370) · [`006e8658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e7/006e7c98.md#insn-006e8658)
- 新版 [`006e80b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8048.md#insn-006e80b8) · [`006e8720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8048.md#insn-006e8720) · [`006e8a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e8/006e8048.md#insn-006e8a08)

~~~diff
- 006e7d08 ["INT_ADD", "register:40f0:8", ["const:6e7d08:8", "const:4:8"]]
- 006e7d08 ["CALL", null, ["callee:00c596b0:8"]]
+ 006e80b8 ["INT_ADD", "register:40f0:8", ["const:6e80b8:8", "const:4:8"]]
+ 006e80b8 ["CALL", null, ["callee:00c596b0:8"]]
- 006e7d08 bytes 76c21594
+ 006e80b8 bytes 7ec51594
- 006e8370 ["INT_ADD", "register:40f0:8", ["const:6e8370:8", "const:4:8"]]
- 006e8370 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006e8720 ["INT_ADD", "register:40f0:8", ["const:6e8720:8", "const:4:8"]]
+ 006e8720 ["CALL", null, ["ram:6e4ecc:8"]]
- 006e8370 bytes ebf1ff97
+ 006e8720 bytes ebf1ff97
- 006e8658 ["INT_ADD", "register:40f0:8", ["const:6e8658:8", "const:4:8"]]
- 006e8658 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006e8a08 ["INT_ADD", "register:40f0:8", ["const:6e8a08:8", "const:4:8"]]
+ 006e8a08 ["CALL", null, ["ram:6e4ecc:8"]]
- 006e8658 bytes 31f1ff97
+ 006e8a08 bytes 31f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11888da7a991fdd32790e05398dd7153"></a>

### [`006e8c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8c74.md) → [`006e9024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e9024.md) FUN_006e9024

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 19件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 1件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 19件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.91% / 新版 87.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 2件, `store_destination` 14件, `store_value` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e9324",
      "incomplete_value": true,
      "site": "006e9334",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8f74",
      "incomplete_value": true,
      "site": "006e8f84",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:fd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e9338",
      "incomplete_value": true,
      "site": "006e9338",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8f88",
      "incomplete_value": true,
      "site": "006e8f88",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f:8"
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
      "definition_site": "006e932c",
      "incomplete_value": true,
      "site": "006e933c",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8f7c",
      "incomplete_value": true,
      "site": "006e8f8c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e9060",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006e906c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e9074",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006e9060",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006e906c",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e9074",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e8cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8c74.md#insn-006e8cd0) · [`006e8f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8c74.md#insn-006e8f50) · [`006e8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e8/006e8c74.md#insn-006e8fac)
- 新版 [`006e9080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e9024.md#insn-006e9080) · [`006e9300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e9024.md#insn-006e9300) · [`006e935c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e9/006e9024.md#insn-006e935c)

~~~diff
- 006e8cd0 ["INT_ADD", "register:40f0:8", ["const:6e8cd0:8", "const:4:8"]]
- 006e8cd0 ["CALL", null, ["callee:00c596b0:8"]]
+ 006e9080 ["INT_ADD", "register:40f0:8", ["const:6e9080:8", "const:4:8"]]
+ 006e9080 ["CALL", null, ["callee:00c596b0:8"]]
- 006e8cd0 bytes 84be1594
+ 006e9080 bytes 8cc11594
- 006e8f50 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006e8f50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006e8f50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006e8f50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006e9300 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 006e9300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006e9300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006e9300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006e8f50 bytes 08e10091
+ 006e9300 bytes 08e13f91
- 006e8fac ["INT_ADD", "register:40f0:8", ["const:6e8fac:8", "const:4:8"]]
- 006e8fac ["CALL", null, ["ram:6e4b1c:8"]]
+ 006e935c ["INT_ADD", "register:40f0:8", ["const:6e935c:8", "const:4:8"]]
+ 006e935c ["CALL", null, ["ram:6e4ecc:8"]]
- 006e8fac bytes dceeff97
+ 006e935c bytes dceeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec0dbf847a52f3f011750a7e9c6d6e47"></a>

### [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) → [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) FUN_006ea990

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) [`006ea5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5d8.md) [`006f16e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f16e0.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`006fb968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md) · 呼出先 52件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 8件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) [`006ea988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea988.md) [`006f1a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f1a90.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`006fbd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md) · 呼出先 52件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.95% / 新版 90.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 55件, `call_target` 37件, `store_destination` 35件, `store_value` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006eafb4",
      "incomplete_value": true,
      "site": "006eafc4",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:b8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006eac04",
      "incomplete_value": true,
      "site": "006eac14",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006eafc8",
      "incomplete_value": true,
      "site": "006eafc8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "006eac18",
      "incomplete_value": true,
      "site": "006eac18",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006eb290",
      "incomplete_value": true,
      "site": "006eb29c",
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
                "const:4f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006eaee0",
      "incomplete_value": true,
      "site": "006eaeec",
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
                "const:4a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 79,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006eab64",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "006eabd8",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ],
    [
      "006eacd4",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006eab64",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "006eabd8",
      "PARAM",
      [
        "storage",
        "00ca5fc0",
        null,
        "undefined8"
      ]
    ],
    [
      "006eacd4",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006eafc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md#insn-006eafc8) · [`006ebcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md#insn-006ebcd0) · [`006ebff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md#insn-006ebff8)
- 新版 [`006eb378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md#insn-006eb378) · [`006ec080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md#insn-006ec080) · [`006ec3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md#insn-006ec3a8)

~~~diff
- 006eafc8 ["INT_ADD", "register:40f0:8", ["const:6eafc8:8", "const:4:8"]]
- 006eafc8 ["CALL", null, ["callee:008524fc:8"]]
+ 006eb378 ["INT_ADD", "register:40f0:8", ["const:6eb378:8", "const:4:8"]]
+ 006eb378 ["CALL", null, ["callee:008524fc:8"]]
- 006eafc8 bytes 62990594
+ 006eb378 bytes 619c0594
- 006ebcd0 ["INT_ADD", "register:40f0:8", ["const:6ebcd0:8", "const:4:8"]]
- 006ebcd0 ["CALL", null, ["callee:0046db10:8"]]
+ 006ec080 ["INT_ADD", "register:40f0:8", ["const:6ec080:8", "const:4:8"]]
+ 006ec080 ["CALL", null, ["callee:0046db10:8"]]
- 006ebcd0 bytes c806f697
+ 006ec080 bytes a406f697
- 006ebff8 ["INT_ADD", "register:40f0:8", ["const:6ebff8:8", "const:4:8"]]
- 006ebff8 ["CALL", null, ["callee:008b89cc:8"]]
+ 006ec3a8 ["INT_ADD", "register:40f0:8", ["const:6ec3a8:8", "const:4:8"]]
+ 006ec3a8 ["CALL", null, ["callee:008b89cc:8"]]
- 006ebff8 bytes 8a2e0794
+ 006ec3a8 bytes 89310794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0426a7ab24e31ecd7628632bff327bf"></a>

### [`006eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md) → [`006ef0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md) FUN_006ef0b4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 18件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`006dbe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbe00.md) [`006e4440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4440.md) [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md)
- 新版 呼出元 1件 [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) · 呼出先 18件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`006dc1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc1b0.md) [`006e47f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e47f0.md) [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.37% / 新版 90.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 34件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ef4b8",
      "incomplete_value": false,
      "site": "006ef4c0",
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
            "const:bb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ef108",
      "incomplete_value": false,
      "site": "006ef110",
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
            "const:a5e:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ef4dc",
      "incomplete_value": false,
      "site": "006ef4e8",
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
            "const:98e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ef12c",
      "incomplete_value": false,
      "site": "006ef138",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ef500",
      "incomplete_value": false,
      "site": "006ef508",
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
            "const:ca6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ef150",
      "incomplete_value": false,
      "site": "006ef158",
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
            "const:bcf:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ef190",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006ef1b0",
      "DATA",
      [
        "storage",
        "00436d88",
        null,
        "byte[67]"
      ]
    ],
    [
      "006ef1d8",
      "DATA",
      [
        "storage",
        "00ca3fa0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006ef190",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006ef1b0",
      "DATA",
      [
        "storage",
        "00436d88",
        null,
        "uleb128"
      ]
    ],
    [
      "006ef1d8",
      "DATA",
      [
        "storage",
        "00ca4f70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006eede0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md#insn-006eede0) · [`006eee3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md#insn-006eee3c) · [`006eeeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md#insn-006eeeac)
- 新版 [`006ef190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md#insn-006ef190) · [`006ef1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md#insn-006ef1ec) · [`006ef25c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md#insn-006ef25c)

~~~diff
- 006eede0 ["INT_ADD", "register:40f0:8", ["const:6eede0:8", "const:4:8"]]
- 006eede0 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006ef190 ["INT_ADD", "register:40f0:8", ["const:6ef190:8", "const:4:8"]]
+ 006ef190 ["CALL", null, ["ram:6e4ecc:8"]]
- 006eede0 bytes 4fd7ff97
+ 006ef190 bytes 4fd7ff97
- 006eee3c ["INT_ADD", "register:40f0:8", ["const:6eee3c:8", "const:4:8"]]
- 006eee3c ["CALL", null, ["callee:006dc1b0:8"]]
+ 006ef1ec ["INT_ADD", "register:40f0:8", ["const:6ef1ec:8", "const:4:8"]]
+ 006ef1ec ["CALL", null, ["callee:006dc1b0:8"]]
- 006eee3c bytes f1b3ff97
+ 006ef1ec bytes f1b3ff97
- 006eeeac ["INT_ADD", "register:40f0:8", ["const:6eeeac:8", "const:4:8"]]
- 006eeeac ["CALL", null, ["ram:6e4b1c:8"]]
+ 006ef25c ["INT_ADD", "register:40f0:8", ["const:6ef25c:8", "const:4:8"]]
+ 006ef25c ["CALL", null, ["ram:6e4ecc:8"]]
- 006eeeac bytes 1cd7ff97
+ 006ef25c bytes 1cd7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd9df25b5da14a486b81b3a9e03d7335"></a>

### [`006f06ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f06ac.md) → [`006f0a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0a5c.md) FUN_006f0a5c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f16e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f1/006f16e0.md) · 呼出先 23件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c0.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md)
- 新版 呼出元 1件 [`006f1a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f1/006f1a90.md) · 呼出先 23件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ead0.md) [`0046eae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eae0.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.68% / 新版 89.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 32件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006f0ae0",
      "incomplete_value": true,
      "site": "006f0af4",
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
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f0730",
      "incomplete_value": true,
      "site": "006f0744",
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
                "const:6d0:8"
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
      "definition_site": "006f0aec",
      "incomplete_value": true,
      "site": "006f0af8",
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
                "const:f25:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f073c",
      "incomplete_value": true,
      "site": "006f0748",
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
                "const:edb:8"
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
      "definition_site": "006f0aec",
      "incomplete_value": true,
      "site": "006f0af8",
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
      "definition_site": "006f073c",
      "incomplete_value": true,
      "site": "006f0748",
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
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f0a94",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006f0aa0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f0aa8",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006f0a94",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006f0aa0",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f0aa8",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f06ac.md#insn-006f09f8) · [`006f0a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f06ac.md#insn-006f0a80) · [`006f0ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f06ac.md#insn-006f0ad4)
- 新版 [`006f0da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0a5c.md#insn-006f0da8) · [`006f0e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0a5c.md#insn-006f0e30) · [`006f0e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0a5c.md#insn-006f0e84)

~~~diff
- 006f09f8 ["INT_ADD", "register:40f0:8", ["const:6f09f8:8", "const:4:8"]]
- 006f09f8 ["CALL", null, ["callee:00448254:8"]]
+ 006f0da8 ["INT_ADD", "register:40f0:8", ["const:6f0da8:8", "const:4:8"]]
+ 006f0da8 ["CALL", null, ["callee:00448254:8"]]
- 006f09f8 bytes 4f5df597
+ 006f0da8 bytes 2b5df597
- 006f0a80 ["INT_ADD", "register:40f0:8", ["const:6f0a80:8", "const:4:8"]]
- 006f0a80 ["CALL", null, ["callee:00c58f20:8"]]
+ 006f0e30 ["INT_ADD", "register:40f0:8", ["const:6f0e30:8", "const:4:8"]]
+ 006f0e30 ["CALL", null, ["callee:00c58f20:8"]]
- 006f0a80 bytes 349d1594
+ 006f0e30 bytes 3ca01594
- 006f0ad4 ["INT_ADD", "register:40f0:8", ["const:6f0ad4:8", "const:4:8"]]
- 006f0ad4 ["CALL", null, ["callee:00c58f50:8"]]
+ 006f0e84 ["INT_ADD", "register:40f0:8", ["const:6f0e84:8", "const:4:8"]]
+ 006f0e84 ["CALL", null, ["callee:00c58f50:8"]]
- 006f0ad4 bytes 2b9d1594
+ 006f0e84 bytes 33a01594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84a8f4911c2ec5723ae0a85bd1e040e"></a>

### [`006f8720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md) → [`006f8ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md) FUN_006f8ad0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 11件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7e0.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 11件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb00.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f8c40",
      "value": [
        "leaf",
        "ram:6df95c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f8890",
      "value": [
        "leaf",
        "ram:6df5ac:8"
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
      "006f8c0c",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "006f8c34",
      "DATA",
      [
        "storage",
        "00ca4554",
        null,
        null
      ]
    ],
    [
      "006f8c40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006df5ac"
      ]
    ]
  ],
  "added": [
    [
      "006f8c0c",
      "READ",
      [
        "storage",
        "00c9c548",
        null,
        "pointer"
      ]
    ],
    [
      "006f8c34",
      "DATA",
      [
        "storage",
        "00ca5524",
        null,
        null
      ]
    ],
    [
      "006f8c40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006df95c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md#insn-006f8890) · [`006f8744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md#insn-006f8744) · [`006f874c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8720.md#insn-006f874c)
- 新版 [`006f8c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md#insn-006f8c40) · [`006f8af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md#insn-006f8af4) · [`006f8afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8ad0.md#insn-006f8afc)

~~~diff
- 006f8890 ["INT_ADD", "register:40f0:8", ["const:6f8890:8", "const:4:8"]]
- 006f8890 ["CALL", null, ["ram:6df5ac:8"]]
+ 006f8c40 ["INT_ADD", "register:40f0:8", ["const:6f8c40:8", "const:4:8"]]
+ 006f8c40 ["CALL", null, ["ram:6df95c:8"]]
- 006f8890 bytes 479bff97
+ 006f8c40 bytes 479bff97
- 006f8744 ["INT_ADD", "register:40f0:8", ["const:6f8744:8", "const:4:8"]]
- 006f8744 ["CALL", null, ["callee:00467bc0:8"]]
+ 006f8af4 ["INT_ADD", "register:40f0:8", ["const:6f8af4:8", "const:4:8"]]
+ 006f8af4 ["CALL", null, ["callee:00467bc0:8"]]
- 006f8744 bytes 57bcf597
+ 006f8af4 bytes 33bcf597
- 006f874c ["INT_ADD", "register:40f0:8", ["const:6f874c:8", "const:4:8"]]
- 006f874c ["CALL", null, ["callee:008524fc:8"]]
+ 006f8afc ["INT_ADD", "register:40f0:8", ["const:6f8afc:8", "const:4:8"]]
+ 006f8afc ["CALL", null, ["callee:008524fc:8"]]
- 006f874c bytes 81630594
+ 006f8afc bytes 80660594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbdfcfbdda0a93d7457c21a36dcdb75e"></a>

### [`006f8a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md) → [`006f8e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md) FUN_006f8e10

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 30件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f5c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 30件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`0046827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/0046827c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006f8e5c",
      "incomplete_value": true,
      "site": "006f8e5c",
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
      "definition_site": "006f8aac",
      "incomplete_value": true,
      "site": "006f8aac",
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
      "definition_site": "006f8e64",
      "incomplete_value": false,
      "site": "006f8e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c66000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f8ab4",
      "incomplete_value": false,
      "site": "006f8ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "006f8e6c",
      "incomplete_value": false,
      "site": "006f8e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f8abc",
      "incomplete_value": false,
      "site": "006f8ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "006f8e48",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8e64",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8e6c",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006f8e48",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8e64",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8e6c",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f8ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md#insn-006f8ac4) · [`006f9360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md#insn-006f9360) · [`006f9edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f8/006f8a60.md#insn-006f9edc)
- 新版 [`006f8e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md#insn-006f8e74) · [`006f9710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md#insn-006f9710) · [`006fa28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f8/006f8e10.md#insn-006fa28c)

~~~diff
- 006f8ac4 ["INT_ADD", "register:40f0:8", ["const:6f8ac4:8", "const:4:8"]]
- 006f8ac4 ["CALL", null, ["callee:00c596b0:8"]]
+ 006f8e74 ["INT_ADD", "register:40f0:8", ["const:6f8e74:8", "const:4:8"]]
+ 006f8e74 ["CALL", null, ["callee:00c596b0:8"]]
- 006f8ac4 bytes 077f1594
+ 006f8e74 bytes 0f821594
- 006f9360 ["INT_ADD", "register:40f0:8", ["const:6f9360:8", "const:4:8"]]
- 006f9360 ["CALL", null, ["ram:6e9ebc:8"]]
+ 006f9710 ["INT_ADD", "register:40f0:8", ["const:6f9710:8", "const:4:8"]]
+ 006f9710 ["CALL", null, ["ram:6ea26c:8"]]
- 006f9360 bytes d7c2ff97
+ 006f9710 bytes d7c2ff97
- 006f9edc ["INT_ADD", "register:40f0:8", ["const:6f9edc:8", "const:4:8"]]
- 006f9edc ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fa28c ["INT_ADD", "register:40f0:8", ["const:6fa28c:8", "const:4:8"]]
+ 006fa28c ["CALL", null, ["ram:6e4ecc:8"]]
- 006f9edc bytes 10abff97
+ 006fa28c bytes 10abff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-621f1f57a8c06a5c3dc5a0166457d5c2"></a>

### [`006f9f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f48.md) → [`006fa2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa2f8.md) FUN_006fa2f8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa31c",
      "incomplete_value": true,
      "site": "006fa31c",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9f6c",
      "incomplete_value": true,
      "site": "006f9f6c",
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
            "const:9e8:8"
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
      "006fa31c",
      "DATA",
      [
        "storage",
        "00c769e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fa31c",
      "DATA",
      [
        "storage",
        "00c779b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f48.md#insn-006f9f5c) · [`006f9f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f48.md#insn-006f9f64) · [`006f9f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f48.md#insn-006f9f68)
- 新版 [`006fa30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa2f8.md#insn-006fa30c) · [`006fa314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa2f8.md#insn-006fa314) · [`006fa318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa2f8.md#insn-006fa318)

~~~diff
- 006f9f5c ["INT_ADD", "register:40f0:8", ["const:6f9f5c:8", "const:4:8"]]
- 006f9f5c ["CALL", null, ["callee:00c58f30:8"]]
+ 006fa30c ["INT_ADD", "register:40f0:8", ["const:6fa30c:8", "const:4:8"]]
+ 006fa30c ["CALL", null, ["callee:00c58f30:8"]]
- 006f9f5c bytes 01781594
+ 006fa30c bytes 097b1594
- 006f9f64 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fa314 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006f9f64 bytes e82b00b0
+ 006fa314 bytes e82b00b0
- 006f9f68 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 006f9f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f9f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f9f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fa318 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 006fa318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f9f68 bytes 08a12791
+ 006fa318 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a009742c45f9f24a2ccbf26ac9783cd4"></a>

### [`006f9f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f7c.md) → [`006fa32c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa32c.md) FUN_006fa32c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa338",
      "incomplete_value": false,
      "site": "006fa338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9f88",
      "incomplete_value": false,
      "site": "006f9f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "006fa338",
      "DATA",
      [
        "storage",
        "00c769e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fa338",
      "DATA",
      [
        "storage",
        "00c779b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f7c.md#insn-006f9f80) · [`006f9f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f7c.md#insn-006f9f84)
- 新版 [`006fa330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa32c.md#insn-006fa330) · [`006fa334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa32c.md#insn-006fa334)

~~~diff
- 006f9f80 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006fa330 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006f9f80 bytes e92b00b0
+ 006fa330 bytes e92b00b0
- 006f9f84 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 006f9f84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006f9f84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006f9f84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fa334 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 006fa334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006f9f84 bytes 29a12791
+ 006fa334 bytes 29e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33207d8d0a7be6b2fa3eee62ba0a6744"></a>

### [`006f9f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f98.md) → [`006fa348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa348.md) FUN_006fa348

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa360",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f9fb0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa38c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f9fdc",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006fa360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fa38c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "006fa360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fa38c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f98.md#insn-006f9fb0) · [`006f9fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f98.md#insn-006f9fdc) · [`006f9fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f9/006f9f98.md#insn-006f9fe8)
- 新版 [`006fa360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa348.md#insn-006fa360) · [`006fa38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa348.md#insn-006fa38c) · [`006fa398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa348.md#insn-006fa398)

~~~diff
- 006f9fb0 ["INT_ADD", "register:40f0:8", ["const:6f9fb0:8", "const:4:8"]]
- 006f9fb0 ["CALL", null, ["ram:47ad34:8"]]
+ 006fa360 ["INT_ADD", "register:40f0:8", ["const:6fa360:8", "const:4:8"]]
+ 006fa360 ["CALL", null, ["ram:47b054:8"]]
- 006f9fb0 bytes 6103f697
+ 006fa360 bytes 3d03f697
- 006f9fdc ["INT_ADD", "register:40f0:8", ["const:6f9fdc:8", "const:4:8"]]
- 006f9fdc ["CALL", null, ["ram:47ad34:8"]]
+ 006fa38c ["INT_ADD", "register:40f0:8", ["const:6fa38c:8", "const:4:8"]]
+ 006fa38c ["CALL", null, ["ram:47b054:8"]]
- 006f9fdc bytes 5603f697
+ 006fa38c bytes 3203f697
- 006f9fe8 ["INT_ADD", "register:40f0:8", ["const:6f9fe8:8", "const:4:8"]]
- 006f9fe8 ["CALL", null, ["callee:0047d134:8"]]
+ 006fa398 ["INT_ADD", "register:40f0:8", ["const:6fa398:8", "const:4:8"]]
+ 006fa398 ["CALL", null, ["callee:0047d134:8"]]
- 006f9fe8 bytes 8b0bf697
+ 006fa398 bytes 670bf697
~~~


<a id="compare-fc7ebc0d214a2095784a51021e38d207"></a>

### [`006fa034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa034.md) → [`006fa3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa3e4.md) FUN_006fa3e4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa408",
      "incomplete_value": false,
      "site": "006fa408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fa058",
      "incomplete_value": false,
      "site": "006fa058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "006fa408",
      "DATA",
      [
        "storage",
        "00c76a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fa408",
      "DATA",
      [
        "storage",
        "00c77a38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa034.md#insn-006fa048) · [`006fa050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa034.md#insn-006fa050) · [`006fa054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa034.md#insn-006fa054)
- 新版 [`006fa3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa3e4.md#insn-006fa3f8) · [`006fa400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa3e4.md#insn-006fa400) · [`006fa404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa3e4.md#insn-006fa404)

~~~diff
- 006fa048 ["INT_ADD", "register:40f0:8", ["const:6fa048:8", "const:4:8"]]
- 006fa048 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fa3f8 ["INT_ADD", "register:40f0:8", ["const:6fa3f8:8", "const:4:8"]]
+ 006fa3f8 ["CALL", null, ["callee:00c58f30:8"]]
- 006fa048 bytes c6771594
+ 006fa3f8 bytes ce7a1594
- 006fa050 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fa400 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fa050 bytes e82b0090
+ 006fa400 bytes e82b00b0
- 006fa054 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 006fa054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fa054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fa054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fa404 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 006fa404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fa404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fa054 bytes 08a12991
+ 006fa404 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d757be9c016811fd5d050e666338b245"></a>

### [`006fa138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa138.md) → [`006fa4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4e8.md) FUN_006fa4e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006dbbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbbc4.md) [`006dbe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006db/006dbe00.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`006dbf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006db/006dbf74.md) [`006dc1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dc1b0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "006fa4f4",
      "incomplete_value": false,
      "site": "006fa4f8",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fa144",
      "incomplete_value": false,
      "site": "006fa148",
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
            "const:f8c:8"
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
      "006fa4f4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006fa4f4",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa138.md#insn-006fa148) · [`006fa140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa138.md#insn-006fa140) · [`006fa144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa138.md#insn-006fa144)
- 新版 [`006fa4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4e8.md#insn-006fa4f8) · [`006fa4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4e8.md#insn-006fa4f0) · [`006fa4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa4e8.md#insn-006fa4f4)

~~~diff
- 006fa148 ["INT_ADD", "register:40f0:8", ["const:6fa148:8", "const:4:8"]]
- 006fa148 ["CALL", null, ["callee:0043bad8:8"]]
+ 006fa4f8 ["INT_ADD", "register:40f0:8", ["const:6fa4f8:8", "const:4:8"]]
+ 006fa4f8 ["CALL", null, ["callee:0043bad8:8"]]
- 006fa148 bytes 9c05f597
+ 006fa4f8 bytes 7805f597
- 006fa140 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 006fa4f0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 006fa140 bytes e0ddffb0
+ 006fa4f0 bytes e0ddffd0
- 006fa144 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 006fa144 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006fa144 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006fa144 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006fa4f4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 006fa4f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa4f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa4f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006fa144 bytes 00303e91
+ 006fa4f4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4986c0daad5cb225d324af2f91bc1c97"></a>

### [`006fa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md) → [`006fa6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md) FUN_006fa6dc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006e3ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3ea8.md) [`006fa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md) [`006fa7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md) · 呼出先 4件 [`006fa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md) [`006fa630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa630.md) [`006fa7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md) [`006faac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006faac0.md)
- 新版 呼出元 3件 [`006e4258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4258.md) [`006fa6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md) [`006faba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md) · 呼出先 4件 [`006fa6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md) [`006fa9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa9e0.md) [`006faba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md) [`006fae70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fae70.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa728",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa378",
      "value": [
        "leaf",
        "ram:6fa630:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa794",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa3e4",
      "value": [
        "leaf",
        "ram:6fa630:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa7bc",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa40c",
      "value": [
        "leaf",
        "ram:6fa630:8"
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
      "006fa728",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ],
    [
      "006fa794",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ],
    [
      "006fa7bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ]
  ],
  "added": [
    [
      "006fa728",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ],
    [
      "006fa794",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ],
    [
      "006fa7bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md#insn-006fa378) · [`006fa3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md#insn-006fa3e4) · [`006fa40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md#insn-006fa40c)
- 新版 [`006fa728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md#insn-006fa728) · [`006fa794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md#insn-006fa794) · [`006fa7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md#insn-006fa7bc)

~~~diff
- 006fa378 ["INT_ADD", "register:40f0:8", ["const:6fa378:8", "const:4:8"]]
- 006fa378 ["CALL", null, ["ram:6fa630:8"]]
+ 006fa728 ["INT_ADD", "register:40f0:8", ["const:6fa728:8", "const:4:8"]]
+ 006fa728 ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa378 bytes ae000094
+ 006fa728 bytes ae000094
- 006fa3e4 ["INT_ADD", "register:40f0:8", ["const:6fa3e4:8", "const:4:8"]]
- 006fa3e4 ["CALL", null, ["ram:6fa630:8"]]
+ 006fa794 ["INT_ADD", "register:40f0:8", ["const:6fa794:8", "const:4:8"]]
+ 006fa794 ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa3e4 bytes 93000094
+ 006fa794 bytes 93000094
- 006fa40c ["INT_ADD", "register:40f0:8", ["const:6fa40c:8", "const:4:8"]]
- 006fa40c ["CALL", null, ["ram:6fa630:8"]]
+ 006fa7bc ["INT_ADD", "register:40f0:8", ["const:6fa7bc:8", "const:4:8"]]
+ 006fa7bc ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa40c bytes 89000094
+ 006fa7bc bytes 89000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c98b23f402cdcfa9aa0b908974d6fb"></a>

### [`006fa7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md) → [`006faba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md) FUN_006faba8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006fa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md) · 呼出先 2件 [`006fa32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa32c.md) [`006fa630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa630.md)
- 新版 呼出元 1件 [`006fa6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md) · 呼出先 2件 [`006fa6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa6dc.md) [`006fa9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006fa9e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fabec",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa83c",
      "value": [
        "leaf",
        "ram:6fa630:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fac78",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa8c8",
      "value": [
        "leaf",
        "ram:6fa630:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006faca8",
      "value": [
        "leaf",
        "ram:6fa9e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa8f8",
      "value": [
        "leaf",
        "ram:6fa630:8"
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
      "006fabec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ],
    [
      "006fac78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ],
    [
      "006faca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa630"
      ]
    ]
  ],
  "added": [
    [
      "006fabec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ],
    [
      "006fac78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ],
    [
      "006faca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fa9e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md#insn-006fa83c) · [`006fa8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md#insn-006fa8c8) · [`006fa8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fa/006fa7f8.md#insn-006fa8f8)
- 新版 [`006fabec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md#insn-006fabec) · [`006fac78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md#insn-006fac78) · [`006faca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fa/006faba8.md#insn-006faca8)

~~~diff
- 006fa83c ["INT_ADD", "register:40f0:8", ["const:6fa83c:8", "const:4:8"]]
- 006fa83c ["CALL", null, ["ram:6fa630:8"]]
+ 006fabec ["INT_ADD", "register:40f0:8", ["const:6fabec:8", "const:4:8"]]
+ 006fabec ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa83c bytes 7dffff97
+ 006fabec bytes 7dffff97
- 006fa8c8 ["INT_ADD", "register:40f0:8", ["const:6fa8c8:8", "const:4:8"]]
- 006fa8c8 ["CALL", null, ["ram:6fa630:8"]]
+ 006fac78 ["INT_ADD", "register:40f0:8", ["const:6fac78:8", "const:4:8"]]
+ 006fac78 ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa8c8 bytes 5affff97
+ 006fac78 bytes 5affff97
- 006fa8f8 ["INT_ADD", "register:40f0:8", ["const:6fa8f8:8", "const:4:8"]]
- 006fa8f8 ["CALL", null, ["ram:6fa630:8"]]
+ 006faca8 ["INT_ADD", "register:40f0:8", ["const:6faca8:8", "const:4:8"]]
+ 006faca8 ["CALL", null, ["ram:6fa9e0:8"]]
- 006fa8f8 bytes 4effff97
+ 006faca8 bytes 4effff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c1af4b3a3b2df1d8984d6f662cbc8fb"></a>

### [`006fb140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb140.md) → [`006fb4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb4f0.md) FUN_006fb4f0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb504",
      "incomplete_value": false,
      "site": "006fb508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb154",
      "incomplete_value": false,
      "site": "006fb158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "006fb508",
      "DATA",
      [
        "storage",
        "00c76ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb508",
      "DATA",
      [
        "storage",
        "00c77ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb140.md#insn-006fb14c) · [`006fb150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb140.md#insn-006fb150) · [`006fb154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb140.md#insn-006fb154)
- 新版 [`006fb4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb4f0.md#insn-006fb4fc) · [`006fb500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb4f0.md#insn-006fb500) · [`006fb504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb4f0.md#insn-006fb504)

~~~diff
- 006fb14c ["INT_ADD", "register:40f0:8", ["const:6fb14c:8", "const:4:8"]]
- 006fb14c ["CALL", null, ["callee:00c58f30:8"]]
+ 006fb4fc ["INT_ADD", "register:40f0:8", ["const:6fb4fc:8", "const:4:8"]]
+ 006fb4fc ["CALL", null, ["callee:00c58f30:8"]]
- 006fb14c bytes 85731594
+ 006fb4fc bytes 8d761594
- 006fb150 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fb500 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fb150 bytes c82b00f0
+ 006fb500 bytes e82b0090
- 006fb154 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 006fb154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb504 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 006fb504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb154 bytes 08a12b91
+ 006fb504 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1acdebce7876947fa0b260b7f283a3c0"></a>

### [`006fb1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb1e4.md) → [`006fb594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb594.md) FUN_006fb594

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb5b8",
      "incomplete_value": false,
      "site": "006fb5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb208",
      "incomplete_value": false,
      "site": "006fb20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "006fb5bc",
      "DATA",
      [
        "storage",
        "00c76b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb5bc",
      "DATA",
      [
        "storage",
        "00c77b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb1e4.md#insn-006fb1f8) · [`006fb204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb1e4.md#insn-006fb204) · [`006fb208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb1e4.md#insn-006fb208)
- 新版 [`006fb5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb594.md#insn-006fb5a8) · [`006fb5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb594.md#insn-006fb5b4) · [`006fb5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb594.md#insn-006fb5b8)

~~~diff
- 006fb1f8 ["INT_ADD", "register:40f0:8", ["const:6fb1f8:8", "const:4:8"]]
- 006fb1f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fb5a8 ["INT_ADD", "register:40f0:8", ["const:6fb5a8:8", "const:4:8"]]
+ 006fb5a8 ["CALL", null, ["callee:00c58f30:8"]]
- 006fb1f8 bytes 5a731594
+ 006fb5a8 bytes 62761594
- 006fb204 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fb5b4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fb204 bytes c82b00f0
+ 006fb5b4 bytes e82b0090
- 006fb208 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 006fb208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb5b8 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 006fb5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb208 bytes 08a12d91
+ 006fb5b8 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dfc4ddf91016dd7b43176d93f1989c6"></a>

### [`006fb224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb224.md) → [`006fb5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5d4.md) FUN_006fb5d4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb5d8",
      "incomplete_value": false,
      "site": "006fb5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb228",
      "incomplete_value": false,
      "site": "006fb22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "006fb5dc",
      "DATA",
      [
        "storage",
        "00c76b68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb5dc",
      "DATA",
      [
        "storage",
        "00c77b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb224.md#insn-006fb224) · [`006fb228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb224.md#insn-006fb228)
- 新版 [`006fb5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5d4.md#insn-006fb5d4) · [`006fb5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5d4.md#insn-006fb5d8)

~~~diff
- 006fb224 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fb5d4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fb224 bytes c82b00f0
+ 006fb5d4 bytes e82b0090
- 006fb228 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 006fb228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb5d8 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 006fb5d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb5d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb5d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb228 bytes 08a12d91
+ 006fb5d8 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d40a94c06516a92b09073a2d2fff26e"></a>

### [`006fb24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb24c.md) → [`006fb5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5fc.md) FUN_006fb5fc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb720",
      "incomplete_value": true,
      "site": "006fb734",
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
                "const:fee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb370",
      "incomplete_value": true,
      "site": "006fb384",
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
                "const:f10:8"
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
      "definition_site": "006fb780",
      "incomplete_value": true,
      "site": "006fb780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb3d0",
      "incomplete_value": true,
      "site": "006fb3d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c37:8"
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
      "definition_site": "006fb784",
      "incomplete_value": true,
      "site": "006fb784",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb3d4",
      "incomplete_value": true,
      "site": "006fb3d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5:8"
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
      "006fb648",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fb6ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ede3c"
      ]
    ],
    [
      "006fb6bc",
      "DATA",
      [
        "storage",
        "0042ef82",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006fb648",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fb6ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ee1ec"
      ]
    ],
    [
      "006fb6bc",
      "DATA",
      [
        "storage",
        "0042ef82",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb24c.md#insn-006fb298) · [`006fb2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb24c.md#insn-006fb2fc) · [`006fb320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb24c.md#insn-006fb320)
- 新版 [`006fb648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5fc.md#insn-006fb648) · [`006fb6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5fc.md#insn-006fb6ac) · [`006fb6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5fc.md#insn-006fb6d0)

~~~diff
- 006fb298 ["INT_ADD", "register:40f0:8", ["const:6fb298:8", "const:4:8"]]
- 006fb298 ["CALL", null, ["ram:47ad34:8"]]
+ 006fb648 ["INT_ADD", "register:40f0:8", ["const:6fb648:8", "const:4:8"]]
+ 006fb648 ["CALL", null, ["ram:47b054:8"]]
- 006fb298 bytes a7fef597
+ 006fb648 bytes 83fef597
- 006fb2fc ["INT_ADD", "register:40f0:8", ["const:6fb2fc:8", "const:4:8"]]
- 006fb2fc ["CALL", null, ["ram:6ede3c:8"]]
+ 006fb6ac ["INT_ADD", "register:40f0:8", ["const:6fb6ac:8", "const:4:8"]]
+ 006fb6ac ["CALL", null, ["ram:6ee1ec:8"]]
- 006fb2fc bytes d0caff97
+ 006fb6ac bytes d0caff97
- 006fb320 ["INT_ADD", "register:40f0:8", ["const:6fb320:8", "const:4:8"]]
- 006fb320 ["CALL", null, ["ram:63c5c8:8"]]
+ 006fb6d0 ["INT_ADD", "register:40f0:8", ["const:6fb6d0:8", "const:4:8"]]
+ 006fb6d0 ["CALL", null, ["ram:63c978:8"]]
- 006fb320 bytes aa04fd97
+ 006fb6d0 bytes aa04fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed1269bf87d8ea9b55b83f0f3e7ed8f"></a>

### [`006fb918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb918.md) → [`006fbcc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcc8.md) FUN_006fbcc8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fbcec",
      "incomplete_value": false,
      "site": "006fbcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb93c",
      "incomplete_value": false,
      "site": "006fb93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "006fbcec",
      "DATA",
      [
        "storage",
        "00c76bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbcec",
      "DATA",
      [
        "storage",
        "00c77ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb918.md#insn-006fb92c) · [`006fb934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb918.md#insn-006fb934) · [`006fb938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb918.md#insn-006fb938)
- 新版 [`006fbcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcc8.md#insn-006fbcdc) · [`006fbce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcc8.md#insn-006fbce4) · [`006fbce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcc8.md#insn-006fbce8)

~~~diff
- 006fb92c ["INT_ADD", "register:40f0:8", ["const:6fb92c:8", "const:4:8"]]
- 006fb92c ["CALL", null, ["callee:00c58f30:8"]]
+ 006fbcdc ["INT_ADD", "register:40f0:8", ["const:6fbcdc:8", "const:4:8"]]
+ 006fbcdc ["CALL", null, ["callee:00c58f30:8"]]
- 006fb92c bytes 8d711594
+ 006fbcdc bytes 95741594
- 006fb934 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fbce4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fb934 bytes c82b00f0
+ 006fbce4 bytes e82b0090
- 006fb938 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 006fb938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fbce8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 006fbce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb938 bytes 08612f91
+ 006fbce8 bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4228e6f9fcd70211a1858421358ac6e"></a>

### [`006fb94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb94c.md) → [`006fbcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcfc.md) FUN_006fbcfc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fbd08",
      "incomplete_value": false,
      "site": "006fbd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb958",
      "incomplete_value": false,
      "site": "006fb958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "006fbd08",
      "DATA",
      [
        "storage",
        "00c76bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbd08",
      "DATA",
      [
        "storage",
        "00c77ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb94c.md#insn-006fb950) · [`006fb954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb94c.md#insn-006fb954)
- 新版 [`006fbd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcfc.md#insn-006fbd00) · [`006fbd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbcfc.md#insn-006fbd04)

~~~diff
- 006fb950 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006fbd00 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006fb950 bytes c92b00f0
+ 006fbd00 bytes e92b0090
- 006fb954 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 006fb954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fb954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fb954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fbd04 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 006fbd04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fbd04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fbd04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fb954 bytes 29612f91
+ 006fbd04 bytes 29a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292a62bd34b785d64decb15be4b0bcae"></a>

### [`006fb968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md) → [`006fbd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md) FUN_006fbd18

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006b247c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b247c.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006f0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0558.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006b282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b282c.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0908.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbd44",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fb994",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbdec",
      "value": [
        "leaf",
        "ram:6f0908:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fba3c",
      "value": [
        "leaf",
        "ram:6f0558:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbd44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fbdec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0558"
      ]
    ]
  ],
  "added": [
    [
      "006fbd44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fbdec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md#insn-006fb994) · [`006fba3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md#insn-006fba3c) · [`006fb9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb968.md#insn-006fb9a0)
- 新版 [`006fbd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md#insn-006fbd44) · [`006fbdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md#insn-006fbdec) · [`006fbd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbd18.md#insn-006fbd50)

~~~diff
- 006fb994 ["INT_ADD", "register:40f0:8", ["const:6fb994:8", "const:4:8"]]
- 006fb994 ["CALL", null, ["ram:47ad34:8"]]
+ 006fbd44 ["INT_ADD", "register:40f0:8", ["const:6fbd44:8", "const:4:8"]]
+ 006fbd44 ["CALL", null, ["ram:47b054:8"]]
- 006fb994 bytes e8fcf597
+ 006fbd44 bytes c4fcf597
- 006fba3c ["INT_ADD", "register:40f0:8", ["const:6fba3c:8", "const:4:8"]]
- 006fba3c ["CALL", null, ["ram:6f0558:8"]]
+ 006fbdec ["INT_ADD", "register:40f0:8", ["const:6fbdec:8", "const:4:8"]]
+ 006fbdec ["CALL", null, ["ram:6f0908:8"]]
- 006fba3c bytes c7d2ff97
+ 006fbdec bytes c7d2ff97
- 006fb9a0 ["INT_ADD", "register:40f0:8", ["const:6fb9a0:8", "const:4:8"]]
- 006fb9a0 ["CALL", null, ["callee:0047d134:8"]]
+ 006fbd50 ["INT_ADD", "register:40f0:8", ["const:6fbd50:8", "const:4:8"]]
+ 006fbd50 ["CALL", null, ["callee:0047d134:8"]]
- 006fb9a0 bytes 1d05f697
+ 006fbd50 bytes f904f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b697fc941981e03c512c8db95bc772"></a>

### [`006fba90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fba90.md) → [`006fbe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe40.md) FUN_006fbe40

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006fbe60",
      "incomplete_value": false,
      "site": "006fbe64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbab0",
      "incomplete_value": false,
      "site": "006fbab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "006fbe64",
      "DATA",
      [
        "storage",
        "00c76c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbe64",
      "DATA",
      [
        "storage",
        "00c77c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbaa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fba90.md#insn-006fbaa4) · [`006fbaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fba90.md#insn-006fbaac) · [`006fbab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fba90.md#insn-006fbab0)
- 新版 [`006fbe54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe40.md#insn-006fbe54) · [`006fbe5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe40.md#insn-006fbe5c) · [`006fbe60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe40.md#insn-006fbe60)

~~~diff
- 006fbaa4 ["INT_ADD", "register:40f0:8", ["const:6fbaa4:8", "const:4:8"]]
- 006fbaa4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fbe54 ["INT_ADD", "register:40f0:8", ["const:6fbe54:8", "const:4:8"]]
+ 006fbe54 ["CALL", null, ["callee:00c58f30:8"]]
- 006fbaa4 bytes 2f711594
+ 006fbe54 bytes 37741594
- 006fbaac ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fbe5c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fbaac bytes c82b00f0
+ 006fbe5c bytes e82b0090
- 006fbab0 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 006fbab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fbab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fbab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fbe60 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 006fbe60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbe60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbe60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fbab0 bytes 08a13191
+ 006fbe60 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c727329db86eca1790f1b193931e77d2"></a>

### [`006fbac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbac8.md) → [`006fbe78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe78.md) FUN_006fbe78

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fbe7c",
      "incomplete_value": false,
      "site": "006fbe80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbacc",
      "incomplete_value": false,
      "site": "006fbad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "006fbe80",
      "DATA",
      [
        "storage",
        "00c76c68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbe80",
      "DATA",
      [
        "storage",
        "00c77c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbac8.md#insn-006fbac8) · [`006fbacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbac8.md#insn-006fbacc)
- 新版 [`006fbe78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe78.md#insn-006fbe78) · [`006fbe7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fbe78.md#insn-006fbe7c)

~~~diff
- 006fbac8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fbe78 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fbac8 bytes c82b00f0
+ 006fbe78 bytes e82b0090
- 006fbacc ["COPY", "tmp:0:8", ["const:c68:8"]]
- 006fbacc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fbacc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fbacc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fbe7c ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 006fbe7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbe7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbe7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fbacc bytes 08a13191
+ 006fbe7c bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1f6eb5e47bed8f506b4ec311ff9f77"></a>

### [`006fbcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbcb4.md) → [`006fc064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc064.md) FUN_006fc064

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fc088",
      "incomplete_value": false,
      "site": "006fc088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbcd8",
      "incomplete_value": false,
      "site": "006fbcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "006fc088",
      "DATA",
      [
        "storage",
        "00c76ce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fc088",
      "DATA",
      [
        "storage",
        "00c77cb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbcb4.md#insn-006fbcc8) · [`006fbcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbcb4.md#insn-006fbcd0) · [`006fbcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbcb4.md#insn-006fbcd4)
- 新版 [`006fc078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc064.md#insn-006fc078) · [`006fc080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc064.md#insn-006fc080) · [`006fc084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc064.md#insn-006fc084)

~~~diff
- 006fbcc8 ["INT_ADD", "register:40f0:8", ["const:6fbcc8:8", "const:4:8"]]
- 006fbcc8 ["CALL", null, ["callee:00c58f30:8"]]
+ 006fc078 ["INT_ADD", "register:40f0:8", ["const:6fc078:8", "const:4:8"]]
+ 006fc078 ["CALL", null, ["callee:00c58f30:8"]]
- 006fbcc8 bytes a6701594
+ 006fc078 bytes ae731594
- 006fbcd0 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fc080 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fbcd0 bytes c82b00f0
+ 006fc080 bytes c82b00f0
- 006fbcd4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 006fbcd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fbcd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fbcd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fc084 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 006fc084 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fc084 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fc084 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fbcd4 bytes 08a13391
+ 006fc084 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8962e00244b7686241e59ad0efc2c1f"></a>

### [`006fbce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbce8.md) → [`006fc098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc098.md) FUN_006fc098

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fc0a4",
      "incomplete_value": false,
      "site": "006fc0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbcf4",
      "incomplete_value": false,
      "site": "006fbcf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "006fc0a4",
      "DATA",
      [
        "storage",
        "00c76ce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fc0a4",
      "DATA",
      [
        "storage",
        "00c77cb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbce8.md#insn-006fbcec) · [`006fbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbce8.md#insn-006fbcf0)
- 新版 [`006fc09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc098.md#insn-006fc09c) · [`006fc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc098.md#insn-006fc0a0)

~~~diff
- 006fbcec ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006fc09c ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006fbcec bytes c92b00f0
+ 006fc09c bytes c92b00f0
- 006fbcf0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 006fbcf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fbcf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fbcf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fc0a0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 006fc0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fc0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fc0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fbcf0 bytes 29a13391
+ 006fc0a0 bytes 29e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17450125321ef19303df64eef3fa4e36"></a>

### [`006fbd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md) → [`006fc0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc0b4.md) FUN_006fc0b4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006b247c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b247c.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006f0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f0/006f0558.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`006b282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b282c.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f0/006f0908.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc0e0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbd30",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc188",
      "value": [
        "leaf",
        "ram:6f0908:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbdd8",
      "value": [
        "leaf",
        "ram:6f0558:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fc0e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006fc188",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0558"
      ]
    ]
  ],
  "added": [
    [
      "006fc0e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006fc188",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md#insn-006fbd30) · [`006fbdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md#insn-006fbdd8) · [`006fbd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbd04.md#insn-006fbd3c)
- 新版 [`006fc0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc0b4.md#insn-006fc0e0) · [`006fc188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc0b4.md#insn-006fc188) · [`006fc0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc0b4.md#insn-006fc0ec)

~~~diff
- 006fbd30 ["INT_ADD", "register:40f0:8", ["const:6fbd30:8", "const:4:8"]]
- 006fbd30 ["CALL", null, ["ram:47ad34:8"]]
+ 006fc0e0 ["INT_ADD", "register:40f0:8", ["const:6fc0e0:8", "const:4:8"]]
+ 006fc0e0 ["CALL", null, ["ram:47b054:8"]]
- 006fbd30 bytes 01fcf597
+ 006fc0e0 bytes ddfbf597
- 006fbdd8 ["INT_ADD", "register:40f0:8", ["const:6fbdd8:8", "const:4:8"]]
- 006fbdd8 ["CALL", null, ["ram:6f0558:8"]]
+ 006fc188 ["INT_ADD", "register:40f0:8", ["const:6fc188:8", "const:4:8"]]
+ 006fc188 ["CALL", null, ["ram:6f0908:8"]]
- 006fbdd8 bytes e0d1ff97
+ 006fc188 bytes e0d1ff97
- 006fbd3c ["INT_ADD", "register:40f0:8", ["const:6fbd3c:8", "const:4:8"]]
- 006fbd3c ["CALL", null, ["callee:0047d134:8"]]
+ 006fc0ec ["INT_ADD", "register:40f0:8", ["const:6fc0ec:8", "const:4:8"]]
+ 006fc0ec ["CALL", null, ["callee:0047d134:8"]]
- 006fbd3c bytes 3604f697
+ 006fc0ec bytes 1204f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1fa8dd1def5411ef1667166cb2e4308"></a>

### [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) → [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) FUN_006fc1d8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006e542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md) [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) [`006fc1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md) · 呼出先 5件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) [`006fc1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md) [`006fc504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 3件 [`006e57dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md) [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) [`006fc564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md) · 呼出先 5件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) [`006fc564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md) [`006fc8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc230",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbe80",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc244",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbe94",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc2c0",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbf10",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fc230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc244",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc2c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fc230",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc244",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc2c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbe80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md#insn-006fbe80) · [`006fbe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md#insn-006fbe94) · [`006fbf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md#insn-006fbf10)
- 新版 [`006fc230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md#insn-006fc230) · [`006fc244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md#insn-006fc244) · [`006fc2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md#insn-006fc2c0)

~~~diff
- 006fbe80 ["INT_ADD", "register:40f0:8", ["const:6fbe80:8", "const:4:8"]]
- 006fbe80 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc230 ["INT_ADD", "register:40f0:8", ["const:6fc230:8", "const:4:8"]]
+ 006fc230 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fbe80 bytes 27a3ff97
+ 006fc230 bytes 27a3ff97
- 006fbe94 ["INT_ADD", "register:40f0:8", ["const:6fbe94:8", "const:4:8"]]
- 006fbe94 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc244 ["INT_ADD", "register:40f0:8", ["const:6fc244:8", "const:4:8"]]
+ 006fc244 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fbe94 bytes 22a3ff97
+ 006fc244 bytes 22a3ff97
- 006fbf10 ["INT_ADD", "register:40f0:8", ["const:6fbf10:8", "const:4:8"]]
- 006fbf10 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc2c0 ["INT_ADD", "register:40f0:8", ["const:6fc2c0:8", "const:4:8"]]
+ 006fc2c0 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fbf10 bytes 03a3ff97
+ 006fc2c0 bytes 03a3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdd36ac9d581e0773ce2d934b57d0c5f"></a>

### [`006fc1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md) → [`006fc564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md) FUN_006fc564

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) · 呼出先 3件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) · 呼出先 3件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc5b4",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc204",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc5c8",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc218",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc660",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc2b0",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fc5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc5c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fc5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc5c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fc204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md#insn-006fc204) · [`006fc218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md#insn-006fc218) · [`006fc2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc1b4.md#insn-006fc2b0)
- 新版 [`006fc5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md#insn-006fc5b4) · [`006fc5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md#insn-006fc5c8) · [`006fc660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc564.md#insn-006fc660)

~~~diff
- 006fc204 ["INT_ADD", "register:40f0:8", ["const:6fc204:8", "const:4:8"]]
- 006fc204 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc5b4 ["INT_ADD", "register:40f0:8", ["const:6fc5b4:8", "const:4:8"]]
+ 006fc5b4 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc204 bytes 46a2ff97
+ 006fc5b4 bytes 46a2ff97
- 006fc218 ["INT_ADD", "register:40f0:8", ["const:6fc218:8", "const:4:8"]]
- 006fc218 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc5c8 ["INT_ADD", "register:40f0:8", ["const:6fc5c8:8", "const:4:8"]]
+ 006fc5c8 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc218 bytes 41a2ff97
+ 006fc5c8 bytes 41a2ff97
- 006fc2b0 ["INT_ADD", "register:40f0:8", ["const:6fc2b0:8", "const:4:8"]]
- 006fc2b0 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc660 ["INT_ADD", "register:40f0:8", ["const:6fc660:8", "const:4:8"]]
+ 006fc660 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc2b0 bytes 1ba2ff97
+ 006fc660 bytes 1ba2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22ac9fbc08a70dfb038faea8d2bc71bb"></a>

### [`006fc504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md) → [`006fc8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md) FUN_006fc8b4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006fbe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fbe28.md) [`006fc504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md) · 呼出先 4件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fc504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`006fc1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc1d8.md) [`006fc8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md) · 呼出先 4件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fc8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc920",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc570",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc934",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc584",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc9b8",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc608",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fc920",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc934",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fc9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fc920",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc934",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fc9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fc570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md#insn-006fc570) · [`006fc584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md#insn-006fc584) · [`006fc608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fc504.md#insn-006fc608)
- 新版 [`006fc920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md#insn-006fc920) · [`006fc934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md#insn-006fc934) · [`006fc9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fc8b4.md#insn-006fc9b8)

~~~diff
- 006fc570 ["INT_ADD", "register:40f0:8", ["const:6fc570:8", "const:4:8"]]
- 006fc570 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc920 ["INT_ADD", "register:40f0:8", ["const:6fc920:8", "const:4:8"]]
+ 006fc920 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc570 bytes 6ba1ff97
+ 006fc920 bytes 6ba1ff97
- 006fc584 ["INT_ADD", "register:40f0:8", ["const:6fc584:8", "const:4:8"]]
- 006fc584 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc934 ["INT_ADD", "register:40f0:8", ["const:6fc934:8", "const:4:8"]]
+ 006fc934 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc584 bytes 66a1ff97
+ 006fc934 bytes 66a1ff97
- 006fc608 ["INT_ADD", "register:40f0:8", ["const:6fc608:8", "const:4:8"]]
- 006fc608 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fc9b8 ["INT_ADD", "register:40f0:8", ["const:6fc9b8:8", "const:4:8"]]
+ 006fc9b8 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fc608 bytes 45a1ff97
+ 006fc9b8 bytes 45a1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d07a64905bda218cef776f7fa8a3a3b"></a>

### [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) → [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) FUN_006fcf7c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006e542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e5/006e542c.md) [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) [`006fcf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md) · 呼出先 5件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) [`006fcf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md) [`006fd2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 3件 [`006e57dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e5/006e57dc.md) [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) [`006fd308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md) · 呼出先 5件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) [`006fd308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md) [`006fd658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcfd4",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcc24",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcfe8",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcc38",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd064",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fccb4",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fcfd4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fcfe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fd064",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fcfd4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fcfe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fd064",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fcc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md#insn-006fcc24) · [`006fcc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md#insn-006fcc38) · [`006fccb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md#insn-006fccb4)
- 新版 [`006fcfd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md#insn-006fcfd4) · [`006fcfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md#insn-006fcfe8) · [`006fd064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md#insn-006fd064)

~~~diff
- 006fcc24 ["INT_ADD", "register:40f0:8", ["const:6fcc24:8", "const:4:8"]]
- 006fcc24 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fcfd4 ["INT_ADD", "register:40f0:8", ["const:6fcfd4:8", "const:4:8"]]
+ 006fcfd4 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fcc24 bytes be9fff97
+ 006fcfd4 bytes be9fff97
- 006fcc38 ["INT_ADD", "register:40f0:8", ["const:6fcc38:8", "const:4:8"]]
- 006fcc38 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fcfe8 ["INT_ADD", "register:40f0:8", ["const:6fcfe8:8", "const:4:8"]]
+ 006fcfe8 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fcc38 bytes b99fff97
+ 006fcfe8 bytes b99fff97
- 006fccb4 ["INT_ADD", "register:40f0:8", ["const:6fccb4:8", "const:4:8"]]
- 006fccb4 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd064 ["INT_ADD", "register:40f0:8", ["const:6fd064:8", "const:4:8"]]
+ 006fd064 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fccb4 bytes 9a9fff97
+ 006fd064 bytes 9a9fff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c91dbb70a5319f3a09fa6dacb453b102"></a>

### [`006fcf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md) → [`006fd308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md) FUN_006fd308

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) · 呼出先 3件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) · 呼出先 3件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd358",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcfa8",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd36c",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcfbc",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd404",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd054",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fd358",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fd36c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fd404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fd358",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fd36c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fd404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fcfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md#insn-006fcfa8) · [`006fcfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md#insn-006fcfbc) · [`006fd054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcf58.md#insn-006fd054)
- 新版 [`006fd358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md#insn-006fd358) · [`006fd36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md#insn-006fd36c) · [`006fd404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd308.md#insn-006fd404)

~~~diff
- 006fcfa8 ["INT_ADD", "register:40f0:8", ["const:6fcfa8:8", "const:4:8"]]
- 006fcfa8 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd358 ["INT_ADD", "register:40f0:8", ["const:6fd358:8", "const:4:8"]]
+ 006fd358 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fcfa8 bytes dd9eff97
+ 006fd358 bytes dd9eff97
- 006fcfbc ["INT_ADD", "register:40f0:8", ["const:6fcfbc:8", "const:4:8"]]
- 006fcfbc ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd36c ["INT_ADD", "register:40f0:8", ["const:6fd36c:8", "const:4:8"]]
+ 006fd36c ["CALL", null, ["ram:6e4ecc:8"]]
- 006fcfbc bytes d89eff97
+ 006fd36c bytes d89eff97
- 006fd054 ["INT_ADD", "register:40f0:8", ["const:6fd054:8", "const:4:8"]]
- 006fd054 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd404 ["INT_ADD", "register:40f0:8", ["const:6fd404:8", "const:4:8"]]
+ 006fd404 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fd054 bytes b29eff97
+ 006fd404 bytes b29eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30b18cbc4a2d5355c9e8b261ca66dbd7"></a>

### [`006fd2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md) → [`006fd658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md) FUN_006fd658

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006fcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fc/006fcbcc.md) [`006fd2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md) · 呼出先 4件 [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`006fd2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`006fcf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fc/006fcf7c.md) [`006fd658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md) · 呼出先 4件 [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`006fd658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd6c4",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd314",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd6d8",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd328",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd75c",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd3ac",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
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
      "006fd6c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fd6d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006fd75c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ]
  ],
  "added": [
    [
      "006fd6c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fd6d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006fd75c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md#insn-006fd314) · [`006fd328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md#insn-006fd328) · [`006fd3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fd2a8.md#insn-006fd3ac)
- 新版 [`006fd6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md#insn-006fd6c4) · [`006fd6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md#insn-006fd6d8) · [`006fd75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fd658.md#insn-006fd75c)

~~~diff
- 006fd314 ["INT_ADD", "register:40f0:8", ["const:6fd314:8", "const:4:8"]]
- 006fd314 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd6c4 ["INT_ADD", "register:40f0:8", ["const:6fd6c4:8", "const:4:8"]]
+ 006fd6c4 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fd314 bytes 029eff97
+ 006fd6c4 bytes 029eff97
- 006fd328 ["INT_ADD", "register:40f0:8", ["const:6fd328:8", "const:4:8"]]
- 006fd328 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd6d8 ["INT_ADD", "register:40f0:8", ["const:6fd6d8:8", "const:4:8"]]
+ 006fd6d8 ["CALL", null, ["ram:6e4ecc:8"]]
- 006fd328 bytes fd9dff97
+ 006fd6d8 bytes fd9dff97
- 006fd3ac ["INT_ADD", "register:40f0:8", ["const:6fd3ac:8", "const:4:8"]]
- 006fd3ac ["CALL", null, ["ram:6e4b1c:8"]]
+ 006fd75c ["INT_ADD", "register:40f0:8", ["const:6fd75c:8", "const:4:8"]]
+ 006fd75c ["CALL", null, ["ram:6e4ecc:8"]]
- 006fd3ac bytes dc9dff97
+ 006fd75c bytes dc9dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

