# v16.0.2 → v16.0.3 · 最優先の変更候補 (89)

[一覧の目次](README.md)

<a id="compare-2fdffc4639348dab504542de6eb9b287"></a>

### [`00c24c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24c44.md) → [`00c25c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25c38.md) FUN_00c25c38

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c24d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d18.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 1件 [`00c25d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25d0c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25c58",
      "incomplete_value": false,
      "site": "00c25c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c94000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24c64",
      "incomplete_value": false,
      "site": "00c24c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "00c25c60",
      "DATA",
      [
        "storage",
        "00c93790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c25c60",
      "DATA",
      [
        "storage",
        "00c94760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24c44.md#insn-00c24c60) · [`00c24c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24c44.md#insn-00c24c64) · [`00c24cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24c44.md#insn-00c24cb0)
- 新版 [`00c25c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25c38.md#insn-00c25c54) · [`00c25c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25c38.md#insn-00c25c58) · [`00c25ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25c38.md#insn-00c25ca4)

~~~diff
- 00c24c60 ["COPY", "register:4040:8", ["const:c93000:8"]]
+ 00c25c54 ["COPY", "register:4040:8", ["const:c94000:8"]]
- 00c24c60 bytes 680300f0
+ 00c25c54 bytes 680300f0
- 00c24c64 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00c24c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c24c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c24c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c25c58 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00c25c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c24c64 bytes 08411e91
+ 00c25c58 bytes 08811d91
- 00c24cb0 ["INT_ADD", "register:40f0:8", ["const:c24cb0:8", "const:4:8"]]
- 00c24cb0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00c25ca4 ["INT_ADD", "register:40f0:8", ["const:c25ca4:8", "const:4:8"]]
+ 00c25ca4 ["CALL", null, ["callee:00c54d90:8"]]
- 00c24cb0 bytes 3cbc0094
+ 00c25ca4 bytes 3bbc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce00ad42b0a6ce5220b9199f6f627488"></a>

### [`00c24d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d44.md) → [`00c25d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25d38.md) _ZNSt6__ndk16locale8__globalEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e990.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f960.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c25d8c",
      "incomplete_value": false,
      "site": "00c25d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24d98",
      "incomplete_value": false,
      "site": "00c24d9c",
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
            "const:ef0:8"
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
      "definition_site": "00c25d98",
      "incomplete_value": false,
      "site": "00c25d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24da4",
      "incomplete_value": false,
      "site": "00c24da8",
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
            "const:ef8:8"
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
      "00c25d50",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c25d5c",
      "DATA",
      [
        "storage",
        "01127ef0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25d74",
      "PARAM",
      [
        "storage",
        "01127ef8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c25d50",
      "READ",
      [
        "storage",
        "01128eb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c25d5c",
      "DATA",
      [
        "storage",
        "01128eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25d74",
      "PARAM",
      [
        "storage",
        "01128eb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d44.md#insn-00c24d9c) · [`00c24da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d44.md#insn-00c24da8) · [`00c24d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24d44.md#insn-00c24d54)
- 新版 [`00c25d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25d38.md#insn-00c25d90) · [`00c25d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25d38.md#insn-00c25d9c) · [`00c25d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25d38.md#insn-00c25d48)

~~~diff
- 00c24d9c ["INT_ADD", "register:40f0:8", ["const:c24d9c:8", "const:4:8"]]
- 00c24d9c ["CALL", null, ["callee:00c5b870:8"]]
+ 00c25d90 ["INT_ADD", "register:40f0:8", ["const:c25d90:8", "const:4:8"]]
+ 00c25d90 ["CALL", null, ["callee:00c5b870:8"]]
- 00c24d9c bytes c1d60094
+ 00c25d90 bytes b8d60094
- 00c24da8 ["INT_ADD", "register:40f0:8", ["const:c24da8:8", "const:4:8"]]
- 00c24da8 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c25d9c ["INT_ADD", "register:40f0:8", ["const:c25d9c:8", "const:4:8"]]
+ 00c25d9c ["CALL", null, ["callee:00c58f10:8"]]
- 00c24da8 bytes 66cc0094
+ 00c25d9c bytes 5dcc0094
- 00c24d54 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00c25d48 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00c24d54 bytes 082800f0
+ 00c25d48 bytes 082800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4db4e2d93bb689ade4e35db654d3c851"></a>

### [`00c24dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24dc8.md) → [`00c25dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25dbc.md) _ZNSt6__ndk16localeC2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md) · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5e990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e990.md)
- 新版 呼出元 1件 [`00c5b840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b840.md) · 呼出先 5件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5f960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f960.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 63.89% / 新版 63.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25dec",
      "incomplete_value": true,
      "site": "00c25df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1128000:8"
              ],
              [
                "leaf",
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24df8",
      "incomplete_value": true,
      "site": "00c24e00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25df0",
      "incomplete_value": true,
      "site": "00c25df8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24dfc",
      "incomplete_value": true,
      "site": "00c24e04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
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
      "definition_site": "00c25e1c",
      "incomplete_value": false,
      "site": "00c25e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24e28",
      "incomplete_value": false,
      "site": "00c24e2c",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c25dd8",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c25dec",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25e1c",
      "PARAM",
      [
        "storage",
        "01127ef8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c25dd8",
      "READ",
      [
        "storage",
        "01128eb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c25dec",
      "READ",
      [
        "storage",
        "01128eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25e1c",
      "PARAM",
      [
        "storage",
        "01128eb8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24dc8.md#insn-00c24e2c) · [`00c24e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24dc8.md#insn-00c24e44) · [`00c24e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24dc8.md#insn-00c24e50)
- 新版 [`00c25e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25dbc.md#insn-00c25e20) · [`00c25e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25dbc.md#insn-00c25e38) · [`00c25e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25dbc.md#insn-00c25e44)

~~~diff
- 00c24e2c ["INT_ADD", "register:40f0:8", ["const:c24e2c:8", "const:4:8"]]
- 00c24e2c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c25e20 ["INT_ADD", "register:40f0:8", ["const:c25e20:8", "const:4:8"]]
+ 00c25e20 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c24e2c bytes 3dcc0094
+ 00c25e20 bytes 34cc0094
- 00c24e44 ["INT_ADD", "register:40f0:8", ["const:c24e44:8", "const:4:8"]]
- 00c24e44 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c25e38 ["INT_ADD", "register:40f0:8", ["const:c25e38:8", "const:4:8"]]
+ 00c25e38 ["CALL", null, ["callee:00c5b870:8"]]
- 00c24e44 bytes 97d60094
+ 00c25e38 bytes 8ed60094
- 00c24e50 ["INT_ADD", "register:40f0:8", ["const:c24e50:8", "const:4:8"]]
- 00c24e50 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c25e44 ["INT_ADD", "register:40f0:8", ["const:c25e44:8", "const:4:8"]]
+ 00c25e44 ["CALL", null, ["callee:00c58f10:8"]]
- 00c24e50 bytes 3ccc0094
+ 00c25e44 bytes 33cc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7356285f30e833b5e19b6ed9f0543337"></a>

### [`00c24e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24e70.md) → [`00c25e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25e64.md) _ZNSt6__ndk16localeC1ERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25e74",
      "incomplete_value": true,
      "site": "00c25e7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24e80",
      "incomplete_value": true,
      "site": "00c24e88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00c24e88"
      ],
      [
        "FALL_THROUGH",
        "00c25e7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c25e74",
      "incomplete_value": true,
      "site": "00c25e84",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24e80",
      "incomplete_value": true,
      "site": "00c24e90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
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
    "guard": [
      [
        "FALL_THROUGH",
        "00c24e88"
      ],
      [
        "FALL_THROUGH",
        "00c25e7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c25e74",
      "incomplete_value": true,
      "site": "00c25e84",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24e80",
      "incomplete_value": true,
      "site": "00c24e90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
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


#### 変更候補の命令位置

- 旧版 [`00c24e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24e70.md#insn-00c24e78) · [`00c24e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24e70.md#insn-00c24e7c) · [`00c24ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24e70.md#insn-00c24ea0)
- 新版 [`00c25e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25e64.md#insn-00c25e6c) · [`00c25e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25e64.md#insn-00c25e70) · [`00c25e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25e64.md#insn-00c25e94)

~~~diff
- 00c24e78 ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00c25e6c ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00c24e78 bytes 092800f0
+ 00c25e6c bytes 092800f0
- 00c24e7c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00c24e7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c24e7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c24e7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c25e70 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00c25e70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c25e70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c25e70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c24e7c bytes 29a13691
+ 00c25e70 bytes 29a13591
- 00c24ea0 ["INT_ADD", "register:40f0:8", ["const:c24ea0:8", "const:4:8"]]
- 00c24ea0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00c25e94 ["INT_ADD", "register:40f0:8", ["const:c25e94:8", "const:4:8"]]
+ 00c25e94 ["CALL", null, ["callee:00c54d60:8"]]
- 00c24ea0 bytes b4bb0094
+ 00c25e94 bytes b3bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9451b1899e9d111ee890ee50182ccae"></a>

### [`00c24eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24eb0.md) → [`00c25ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25ea4.md) _ZNSt6__ndk16localeD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25ec0",
      "incomplete_value": true,
      "site": "00c25ec4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24ecc",
      "incomplete_value": true,
      "site": "00c24ed0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
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


#### 変更候補の命令位置

- 旧版 [`00c24ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24eb0.md#insn-00c24ec4) · [`00c24ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24eb0.md#insn-00c24ec8) · [`00c24edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24eb0.md#insn-00c24edc)
- 新版 [`00c25eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25ea4.md#insn-00c25eb8) · [`00c25ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25ea4.md#insn-00c25ebc) · [`00c25ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25ea4.md#insn-00c25ed0)

~~~diff
- 00c24ec4 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00c25eb8 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00c24ec4 bytes 082800f0
+ 00c25eb8 bytes 082800f0
- 00c24ec8 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00c24ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c24ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c24ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c25ebc ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00c25ebc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25ebc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25ebc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c24ec8 bytes 08a13691
+ 00c25ebc bytes 08a13591
- 00c24edc ["INT_ADD", "register:40f0:8", ["const:c24edc:8", "const:4:8"]]
- 00c24edc ["CALL", null, ["callee:00c54d90:8"]]
+ 00c25ed0 ["INT_ADD", "register:40f0:8", ["const:c25ed0:8", "const:4:8"]]
+ 00c25ed0 ["CALL", null, ["callee:00c54d90:8"]]
- 00c24edc bytes b1bb0094
+ 00c25ed0 bytes b0bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3882ec6e48d6698c0c19dd4261d3f978"></a>

### [`00c24f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f10.md) → [`00c25f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f04.md) _ZNSt6__ndk16localeaSERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e3b0.md) · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5f380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f380.md) · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25f2c",
      "incomplete_value": true,
      "site": "00c25f30",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24f38",
      "incomplete_value": true,
      "site": "00c24f3c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
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


#### 変更候補の命令位置

- 旧版 [`00c24f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f10.md#insn-00c24f28) · [`00c24f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f10.md#insn-00c24f2c) · [`00c24f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f10.md#insn-00c24f48)
- 新版 [`00c25f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f04.md#insn-00c25f1c) · [`00c25f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f04.md#insn-00c25f20) · [`00c25f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f04.md#insn-00c25f3c)

~~~diff
- 00c24f28 ["COPY", "register:40b0:8", ["const:1127000:8"]]
+ 00c25f1c ["COPY", "register:40b0:8", ["const:1128000:8"]]
- 00c24f28 bytes 162800f0
+ 00c25f1c bytes 162800f0
- 00c24f2c ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00c24f2c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00c24f2c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00c24f2c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00c25f20 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00c25f20 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c25f20 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c25f20 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00c24f2c bytes d6a23691
+ 00c25f20 bytes d6a23591
- 00c24f48 ["INT_ADD", "register:40f0:8", ["const:c24f48:8", "const:4:8"]]
- 00c24f48 ["CALL", null, ["callee:00c54d60:8"]]
+ 00c25f3c ["INT_ADD", "register:40f0:8", ["const:c25f3c:8", "const:4:8"]]
+ 00c25f3c ["CALL", null, ["callee:00c54d60:8"]]
- 00c24f48 bytes 8abb0094
+ 00c25f3c bytes 89bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6212412f9540e750c228e4887dc09a15"></a>

### [`00c24f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f98.md) → [`00c25f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f8c.md) _ZNSt6__ndk16localeC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c1f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1f528.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c2051c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c20/00c2051c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c26088",
      "incomplete_value": false,
      "site": "00c2608c",
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
            "const:e6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25094",
      "incomplete_value": false,
      "site": "00c25098",
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
            "const:d9d:8"
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
      "00c26088",
      "PARAM",
      [
        "storage",
        "002b5d9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c26088",
      "PARAM",
      [
        "storage",
        "002b5e6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f98.md#insn-00c25098) · [`00c24fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f98.md#insn-00c24fc4) · [`00c24fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24f98.md#insn-00c24fd0)
- 新版 [`00c2608c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f8c.md#insn-00c2608c) · [`00c25fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f8c.md#insn-00c25fb8) · [`00c25fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25f8c.md#insn-00c25fc4)

~~~diff
- 00c25098 ["INT_ADD", "register:40f0:8", ["const:c25098:8", "const:4:8"]]
- 00c25098 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c2608c ["INT_ADD", "register:40f0:8", ["const:c2608c:8", "const:4:8"]]
+ 00c2608c ["CALL", null, ["callee:00c5f050:8"]]
- 00c25098 bytes fae30094
+ 00c2608c bytes f1e30094
- 00c24fc4 ["INT_ADD", "register:40f0:8", ["const:c24fc4:8", "const:4:8"]]
- 00c24fc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c25fb8 ["INT_ADD", "register:40f0:8", ["const:c25fb8:8", "const:4:8"]]
+ 00c25fb8 ["CALL", null, ["callee:00c58f30:8"]]
- 00c24fc4 bytes e7cb0094
+ 00c25fb8 bytes decb0094
- 00c24fd0 ["INT_ADD", "register:40f0:8", ["const:c24fd0:8", "const:4:8"]]
- 00c24fd0 ["CALL", null, ["callee:00c59080:8"]]
+ 00c25fc4 ["INT_ADD", "register:40f0:8", ["const:c25fc4:8", "const:4:8"]]
+ 00c25fc4 ["CALL", null, ["callee:00c59080:8"]]
- 00c24fd0 bytes 38cc0094
+ 00c25fc4 bytes 2fcc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d108d26c437963f6b98c850f16708d4"></a>

### [`00c2513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2513c.md) → [`00c26130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26130.md) _ZNSt6__ndk16localeC1ERKS0_PKci

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c219c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c21/00c219c4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c229b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c22/00c229b8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00c26244",
      "incomplete_value": false,
      "site": "00c26248",
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
            "const:e6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25250",
      "incomplete_value": false,
      "site": "00c25254",
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
            "const:d9d:8"
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
      "00c26244",
      "PARAM",
      [
        "storage",
        "002b5d9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c26244",
      "PARAM",
      [
        "storage",
        "002b5e6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2513c.md#insn-00c25254) · [`00c25174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2513c.md#insn-00c25174) · [`00c25184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c2513c.md#insn-00c25184)
- 新版 [`00c26248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26130.md#insn-00c26248) · [`00c26168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26130.md#insn-00c26168) · [`00c26178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26130.md#insn-00c26178)

~~~diff
- 00c25254 ["INT_ADD", "register:40f0:8", ["const:c25254:8", "const:4:8"]]
- 00c25254 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c26248 ["INT_ADD", "register:40f0:8", ["const:c26248:8", "const:4:8"]]
+ 00c26248 ["CALL", null, ["callee:00c5f050:8"]]
- 00c25254 bytes 8be30094
+ 00c26248 bytes 82e30094
- 00c25174 ["INT_ADD", "register:40f0:8", ["const:c25174:8", "const:4:8"]]
- 00c25174 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c26168 ["INT_ADD", "register:40f0:8", ["const:c26168:8", "const:4:8"]]
+ 00c26168 ["CALL", null, ["callee:00c58f30:8"]]
- 00c25174 bytes 7bcb0094
+ 00c26168 bytes 72cb0094
- 00c25184 ["INT_ADD", "register:40f0:8", ["const:c25184:8", "const:4:8"]]
- 00c25184 ["CALL", null, ["callee:00c59080:8"]]
+ 00c26178 ["INT_ADD", "register:40f0:8", ["const:c26178:8", "const:4:8"]]
+ 00c26178 ["CALL", null, ["callee:00c59080:8"]]
- 00c25184 bytes cbcb0094
+ 00c26178 bytes c2cb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df04ada30090785f2b85cb14c49e9300"></a>

### [`00c253ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c253ac.md) → [`00c263a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c263a0.md) _ZNSt6__ndk16locale14__install_ctorERKS0_PNS0_5facetEl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c25964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c263f8",
      "incomplete_value": true,
      "site": "00c26400",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25404",
      "incomplete_value": true,
      "site": "00c2540c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4098:8"
              ],
              "INT_ADD"
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00c253d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c253ac.md#insn-00c253d8) · [`00c253ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c253ac.md#insn-00c253ec) · [`00c253fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c253ac.md#insn-00c253fc)
- 新版 [`00c263cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c263a0.md#insn-00c263cc) · [`00c263e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c263a0.md#insn-00c263e0) · [`00c263f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c263a0.md#insn-00c263f0)

~~~diff
- 00c253d8 ["INT_ADD", "register:40f0:8", ["const:c253d8:8", "const:4:8"]]
- 00c253d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c263cc ["INT_ADD", "register:40f0:8", ["const:c263cc:8", "const:4:8"]]
+ 00c263cc ["CALL", null, ["callee:00c58f30:8"]]
- 00c253d8 bytes e2ca0094
+ 00c263cc bytes d9ca0094
- 00c253ec ["INT_ADD", "register:40f0:8", ["const:c253ec:8", "const:4:8"]]
- 00c253ec ["CALL", null, ["callee:00c25964:8"]]
+ 00c263e0 ["INT_ADD", "register:40f0:8", ["const:c263e0:8", "const:4:8"]]
+ 00c263e0 ["CALL", null, ["callee:00c25964:8"]]
- 00c253ec bytes 61fdff97
+ 00c263e0 bytes 61fdff97
- 00c253fc ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00c263f0 ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00c253fc bytes 082800d0
+ 00c263f0 bytes 082800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a934e6b0f2ad6bb5fc12112580b6402"></a>

### [`00c25444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25444.md) → [`00c26438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26438.md) _ZNSt6__ndk16locale6globalERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c264d4",
      "incomplete_value": true,
      "site": "00c264d4",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c254e0",
      "incomplete_value": true,
      "site": "00c254e0",
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
            "const:ef0:8"
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
      "definition_site": "00c264a4",
      "incomplete_value": true,
      "site": "00c264a8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c254b0",
      "incomplete_value": true,
      "site": "00c254b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c26470",
      "incomplete_value": false,
      "site": "00c26478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2547c",
      "incomplete_value": false,
      "site": "00c25484",
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
            "const:ef0:8"
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
      "00c26460",
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26470",
      "PARAM",
      [
        "storage",
        "01127ef0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c264a0",
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c26460",
      "READ",
      [
        "storage",
        "01128eb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26470",
      "PARAM",
      [
        "storage",
        "01128eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c264a0",
      "READ",
      [
        "storage",
        "01128eb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25444.md#insn-00c25484) · [`00c254e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25444.md#insn-00c254e0) · [`00c255d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25444.md#insn-00c255d8)
- 新版 [`00c26478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26438.md#insn-00c26478) · [`00c264d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26438.md#insn-00c264d4) · [`00c265cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26438.md#insn-00c265cc)

~~~diff
- 00c25484 ["INT_ADD", "register:40f0:8", ["const:c25484:8", "const:4:8"]]
- 00c25484 ["CALL", null, ["callee:00c5b870:8"]]
+ 00c26478 ["INT_ADD", "register:40f0:8", ["const:c26478:8", "const:4:8"]]
+ 00c26478 ["CALL", null, ["callee:00c5b870:8"]]
- 00c25484 bytes 07d50094
+ 00c26478 bytes fed40094
- 00c254e0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ef0:8"]]
- 00c254e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c264d4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:eb0:8"]]
+ 00c264d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c254e0 bytes c87a07f9
+ 00c264d4 bytes c85a07f9
- 00c255d8 ["INT_ADD", "register:40f0:8", ["const:c255d8:8", "const:4:8"]]
- 00c255d8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c265cc ["INT_ADD", "register:40f0:8", ["const:c265cc:8", "const:4:8"]]
+ 00c265cc ["CALL", null, ["callee:00c58ef0:8"]]
- 00c255d8 bytes 52ca0094
+ 00c265cc bytes 49ca0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69db7057711486d86654311231f1fec"></a>

### [`00c258f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258f8.md) → [`00c268ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c268ec.md) _ZNSt6__ndk114collate_bynameIcEC1EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26918",
      "incomplete_value": true,
      "site": "00c26918",
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
      "definition_site": "00c25924",
      "incomplete_value": true,
      "site": "00c25924",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c26954",
      "incomplete_value": false,
      "site": "00c26964",
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
            "const:b3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25960",
      "incomplete_value": false,
      "site": "00c25970",
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
            "const:a71:8"
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
      "00c2690c",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c26918",
      "DATA",
      [
        "storage",
        "00c937b8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26954",
      "PARAM",
      [
        "storage",
        "002aaa71",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2690c",
      "READ",
      [
        "storage",
        "00c9ce58",
        null,
        "pointer"
      ]
    ],
    [
      "00c26918",
      "DATA",
      [
        "storage",
        "00c94788",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26954",
      "PARAM",
      [
        "storage",
        "002aab3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258f8.md#insn-00c25970) · [`00c2590c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258f8.md#insn-00c2590c) · [`00c25918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c258f8.md#insn-00c25918)
- 新版 [`00c26964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c268ec.md#insn-00c26964) · [`00c26900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c268ec.md#insn-00c26900) · [`00c2690c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c268ec.md#insn-00c2690c)

~~~diff
- 00c25970 ["INT_ADD", "register:40f0:8", ["const:c25970:8", "const:4:8"]]
- 00c25970 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c26964 ["INT_ADD", "register:40f0:8", ["const:c26964:8", "const:4:8"]]
+ 00c26964 ["CALL", null, ["callee:00c269c4:8"]]
- 00c25970 bytes 18000094
+ 00c26964 bytes 18000094
- 00c2590c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c26900 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c2590c bytes a80300d0
+ 00c26900 bytes a80300d0
- 00c25918 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 00c25918 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2690c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
+ 00c2690c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25918 bytes 084547f9
+ 00c2690c bytes 082d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc7b2da110fbd0767730c30c5920e04"></a>

### [`00c25a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25a34.md) → [`00c26a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26a28.md) _ZNSt6__ndk114collate_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8f0.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5f8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8c0.md) · 呼出先 6件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26a54",
      "incomplete_value": true,
      "site": "00c26a54",
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
      "definition_site": "00c25a60",
      "incomplete_value": true,
      "site": "00c25a60",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c26a94",
      "incomplete_value": false,
      "site": "00c26aa4",
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
            "const:b3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25aa0",
      "incomplete_value": false,
      "site": "00c25ab0",
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
            "const:a71:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c26a48",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c26a54",
      "DATA",
      [
        "storage",
        "00c937b8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26a94",
      "PARAM",
      [
        "storage",
        "002aaa71",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c26a48",
      "READ",
      [
        "storage",
        "00c9ce58",
        null,
        "pointer"
      ]
    ],
    [
      "00c26a54",
      "DATA",
      [
        "storage",
        "00c94788",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26a94",
      "PARAM",
      [
        "storage",
        "002aab3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25a34.md#insn-00c25ab0) · [`00c25a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25a34.md#insn-00c25a48) · [`00c25a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25a34.md#insn-00c25a54)
- 新版 [`00c26aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26a28.md#insn-00c26aa4) · [`00c26a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26a28.md#insn-00c26a3c) · [`00c26a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26a28.md#insn-00c26a48)

~~~diff
- 00c25ab0 ["INT_ADD", "register:40f0:8", ["const:c25ab0:8", "const:4:8"]]
- 00c25ab0 ["CALL", null, ["callee:00c59150:8"]]
+ 00c26aa4 ["INT_ADD", "register:40f0:8", ["const:c26aa4:8", "const:4:8"]]
+ 00c26aa4 ["CALL", null, ["callee:00c59150:8"]]
- 00c25ab0 bytes b4c90094
+ 00c26aa4 bytes abc90094
- 00c25a48 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c26a3c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c25a48 bytes a80300d0
+ 00c26a3c bytes a80300d0
- 00c25a54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 00c25a54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26a48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
+ 00c26a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25a54 bytes 084547f9
+ 00c26a48 bytes 082d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a8e032d29ffb395a7f0aff6abbc6745"></a>

### [`00c25af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25af8.md) → [`00c26aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26aec.md) _ZNSt6__ndk114collate_bynameIcED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9f0.md) · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 1件 [`00c5f9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f9c0.md) · 呼出先 2件 [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26b0c",
      "incomplete_value": true,
      "site": "00c26b10",
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
      "definition_site": "00c25b18",
      "incomplete_value": true,
      "site": "00c25b1c",
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
      "00c26b04",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00c26b10",
      "DATA",
      [
        "storage",
        "00c937b8",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00c26b04",
      "READ",
      [
        "storage",
        "00c9ce58",
        null,
        "pointer"
      ]
    ],
    [
      "00c26b10",
      "DATA",
      [
        "storage",
        "00c94788",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25af8.md#insn-00c25b08) · [`00c25b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25af8.md#insn-00c25b10) · [`00c25b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25af8.md#insn-00c25b20)
- 新版 [`00c26afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26aec.md#insn-00c26afc) · [`00c26b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26aec.md#insn-00c26b04) · [`00c26b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26aec.md#insn-00c26b14)

~~~diff
- 00c25b08 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c26afc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c25b08 bytes a80300d0
+ 00c26afc bytes a80300d0
- 00c25b10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 00c25b10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
+ 00c26b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25b10 bytes 084547f9
+ 00c26b04 bytes 082d47f9
- 00c25b20 ["INT_ADD", "register:40f0:8", ["const:c25b20:8", "const:4:8"]]
- 00c25b20 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c26b14 ["INT_ADD", "register:40f0:8", ["const:c26b14:8", "const:4:8"]]
+ 00c26b14 ["CALL", null, ["callee:00c5e270:8"]]
- 00c25b20 bytes e0dd0094
+ 00c26b14 bytes d7dd0094
~~~


<a id="compare-893d18ddf23591d6ad4d2a2ead7964e2"></a>

### [`00c25f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25f3c.md) → [`00c26f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26f30.md) _ZNSt6__ndk114collate_bynameIwEC1EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c26f98",
      "incomplete_value": false,
      "site": "00c26fa8",
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
            "const:d8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25fa4",
      "incomplete_value": false,
      "site": "00c25fb4",
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
            "const:d4a:8"
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
      "00c26f50",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c26f5c",
      "DATA",
      [
        "storage",
        "00c937f8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26f98",
      "PARAM",
      [
        "storage",
        "0029fd4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c26f50",
      "READ",
      [
        "storage",
        "00c9ce60",
        null,
        "pointer"
      ]
    ],
    [
      "00c26f5c",
      "DATA",
      [
        "storage",
        "00c947c8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c26f98",
      "PARAM",
      [
        "storage",
        "0029fd8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25f3c.md#insn-00c25fb4) · [`00c25f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25f3c.md#insn-00c25f50) · [`00c25f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c25f3c.md#insn-00c25f5c)
- 新版 [`00c26fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26f30.md#insn-00c26fa8) · [`00c26f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26f30.md#insn-00c26f44) · [`00c26f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c26f30.md#insn-00c26f50)

~~~diff
- 00c25fb4 ["INT_ADD", "register:40f0:8", ["const:c25fb4:8", "const:4:8"]]
- 00c25fb4 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c26fa8 ["INT_ADD", "register:40f0:8", ["const:c26fa8:8", "const:4:8"]]
+ 00c26fa8 ["CALL", null, ["callee:00c269c4:8"]]
- 00c25fb4 bytes 87feff97
+ 00c26fa8 bytes 87feff97
- 00c25f50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c26f44 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c25f50 bytes a80300d0
+ 00c26f44 bytes a80300d0
- 00c25f5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c25f5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26f50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00c26f50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25f5c bytes 084947f9
+ 00c26f50 bytes 083147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb09cf0d185dc13312ec91c0881ce426"></a>

### [`00c26014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26014.md) → [`00c27008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27008.md) _ZNSt6__ndk114collate_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e900.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5f8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8d0.md) · 呼出先 6件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27034",
      "incomplete_value": true,
      "site": "00c27034",
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
      "definition_site": "00c26040",
      "incomplete_value": true,
      "site": "00c26040",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c27074",
      "incomplete_value": true,
      "site": "00c27084",
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
            "const:d8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26080",
      "incomplete_value": true,
      "site": "00c26090",
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
            "const:d4a:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c27028",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c27034",
      "DATA",
      [
        "storage",
        "00c937f8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c27074",
      "PARAM",
      [
        "storage",
        "0029fd4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c27028",
      "READ",
      [
        "storage",
        "00c9ce60",
        null,
        "pointer"
      ]
    ],
    [
      "00c27034",
      "DATA",
      [
        "storage",
        "00c947c8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c27074",
      "PARAM",
      [
        "storage",
        "0029fd8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26014.md#insn-00c26090) · [`00c26028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26014.md#insn-00c26028) · [`00c26034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26014.md#insn-00c26034)
- 新版 [`00c27084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27008.md#insn-00c27084) · [`00c2701c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27008.md#insn-00c2701c) · [`00c27028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27008.md#insn-00c27028)

~~~diff
- 00c26090 ["INT_ADD", "register:40f0:8", ["const:c26090:8", "const:4:8"]]
- 00c26090 ["CALL", null, ["callee:00c59150:8"]]
+ 00c27084 ["INT_ADD", "register:40f0:8", ["const:c27084:8", "const:4:8"]]
+ 00c27084 ["CALL", null, ["callee:00c59150:8"]]
- 00c26090 bytes 3cc80094
+ 00c27084 bytes 33c80094
- 00c26028 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2701c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c26028 bytes a80300b0
+ 00c2701c bytes a80300b0
- 00c26034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c26034 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00c27028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c26034 bytes 084947f9
+ 00c27028 bytes 083147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e116dac69b398bcb679ddd93b35215"></a>

### [`00c260d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c260d8.md) → [`00c270cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c270cc.md) _ZNSt6__ndk114collate_bynameIwED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ea20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea20.md) · 呼出先 2件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 1件 [`00c5f9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f9f0.md) · 呼出先 2件 [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c270ec",
      "incomplete_value": true,
      "site": "00c270f0",
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
      "definition_site": "00c260f8",
      "incomplete_value": true,
      "site": "00c260fc",
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
      "00c270e4",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ],
    [
      "00c270f0",
      "DATA",
      [
        "storage",
        "00c937f8",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00c270e4",
      "READ",
      [
        "storage",
        "00c9ce60",
        null,
        "pointer"
      ]
    ],
    [
      "00c270f0",
      "DATA",
      [
        "storage",
        "00c947c8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c260e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c260d8.md#insn-00c260e8) · [`00c260f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c260d8.md#insn-00c260f0) · [`00c26100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c260d8.md#insn-00c26100)
- 新版 [`00c270dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c270cc.md#insn-00c270dc) · [`00c270e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c270cc.md#insn-00c270e4) · [`00c270f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c270cc.md#insn-00c270f4)

~~~diff
- 00c260e8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c270dc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c260e8 bytes a80300b0
+ 00c270dc bytes a80300b0
- 00c260f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00c260f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c270e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 00c270e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c260f0 bytes 084947f9
+ 00c270e4 bytes 083147f9
- 00c26100 ["INT_ADD", "register:40f0:8", ["const:c26100:8", "const:4:8"]]
- 00c26100 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c270f4 ["INT_ADD", "register:40f0:8", ["const:c270f4:8", "const:4:8"]]
+ 00c270f4 ["CALL", null, ["callee:00c5e270:8"]]
- 00c26100 bytes 68dc0094
+ 00c270f4 bytes 5fdc0094
~~~


<a id="compare-f10c93de228339f32b39bc9c655d6c3d"></a>

### [`00c265c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c265c0.md) → [`00c275b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c275b4.md) _ZNKSt6__ndk15ctypeIwE5do_isEmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c275d8",
      "incomplete_value": true,
      "site": "00c275dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c265e4",
      "incomplete_value": true,
      "site": "00c265e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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
      "00c275d0",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c275d0",
      "DATA",
      [
        "storage",
        "00311018",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c265d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c265c0.md#insn-00c265d4) · [`00c265d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c265c0.md#insn-00c265d8)
- 新版 [`00c275c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c275b4.md#insn-00c275c8) · [`00c275cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c275b4.md#insn-00c275cc)

~~~diff
- 00c265d4 ["COPY", "register:4040:8", ["const:310000:8"]]
+ 00c275c8 ["COPY", "register:4040:8", ["const:311000:8"]]
- 00c265d4 bytes 48b7ffd0
+ 00c275c8 bytes 48b7ffd0
- 00c265d8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00c265d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c265d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c265d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c275cc ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00c275cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c275cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c275cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c265d8 bytes 08613f91
+ 00c275cc bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4efa692115ab788e51d1fc9dcd3688c"></a>

### [`00c266d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c266d8.md) → [`00c276cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c276cc.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5ea60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5fa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2774c",
      "incomplete_value": true,
      "site": "00c2774c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26758",
      "incomplete_value": true,
      "site": "00c26758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c2772c",
      "incomplete_value": false,
      "site": "00c27730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26738",
      "incomplete_value": false,
      "site": "00c2673c",
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
            "const:da0:8"
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
      "definition_site": "00c2773c",
      "incomplete_value": false,
      "site": "00c27748",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26748",
      "incomplete_value": false,
      "site": "00c26754",
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
            "const:1bc:8"
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
      "00c276f4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c276fc",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2772c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c276f4",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c276fc",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2772c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c266d8.md#insn-00c2673c) · [`00c26754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c266d8.md#insn-00c26754) · [`00c26758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c266d8.md#insn-00c26758)
- 新版 [`00c27730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c276cc.md#insn-00c27730) · [`00c27748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c276cc.md#insn-00c27748) · [`00c2774c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c276cc.md#insn-00c2774c)

~~~diff
- 00c2673c ["INT_ADD", "register:40f0:8", ["const:c2673c:8", "const:4:8"]]
- 00c2673c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c27730 ["INT_ADD", "register:40f0:8", ["const:c27730:8", "const:4:8"]]
+ 00c27730 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2673c bytes f9c50094
+ 00c27730 bytes f0c50094
- 00c26754 ["INT_ADD", "register:40f0:8", ["const:c26754:8", "const:4:8"]]
- 00c26754 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c27748 ["INT_ADD", "register:40f0:8", ["const:c27748:8", "const:4:8"]]
+ 00c27748 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c26754 bytes e7da0094
+ 00c27748 bytes deda0094
- 00c26758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00c26758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c2774c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00c2774c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26758 bytes 80ce06f9
+ 00c2774c bytes 80ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f7fca5ea1dacc7f696bbc93cd8d508"></a>

### [`00c26784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26784.md) → [`00c27778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27778.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEPwPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27804",
      "incomplete_value": true,
      "site": "00c27804",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26810",
      "incomplete_value": true,
      "site": "00c26810",
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
            "const:d98:8"
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
      "00c277dc",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c277e4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c277f0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c277dc",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c277e4",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c277f0",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26784.md#insn-00c26810) · [`00c267ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26784.md#insn-00c267ac) · [`00c267b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26784.md#insn-00c267b0)
- 新版 [`00c27804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27778.md#insn-00c27804) · [`00c277a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27778.md#insn-00c277a0) · [`00c277a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27778.md#insn-00c277a4)

~~~diff
- 00c26810 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
- 00c26810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27804 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d58:8"]]
+ 00c27804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26810 bytes c0ce06f9
+ 00c27804 bytes c0ae06f9
- 00c267ac ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00c277a0 ["COPY", "register:40a8:8", ["const:1128000:8"]]
- 00c267ac bytes 152800b0
+ 00c277a0 bytes 152800b0
- 00c267b0 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00c267b0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c267b0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c267b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c277a4 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c277a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c277a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c277a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c267b0 bytes b5823691
+ 00c277a4 bytes b5823591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8312368cf4beb495efb48a4e6c9e37af"></a>

### [`00c26858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26858.md) → [`00c2784c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c2784c.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c278c4",
      "incomplete_value": false,
      "site": "00c278c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268d0",
      "incomplete_value": false,
      "site": "00c268d0",
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
            "const:d98:8"
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
      "definition_site": "00c278a0",
      "incomplete_value": false,
      "site": "00c278a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268ac",
      "incomplete_value": false,
      "site": "00c268b0",
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
            "const:da0:8"
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
      "definition_site": "00c278b0",
      "incomplete_value": false,
      "site": "00c278bc",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268bc",
      "incomplete_value": false,
      "site": "00c268c8",
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
            "const:1bc:8"
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
      "00c27870",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c278a0",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c278b0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27870",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c278a0",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c278b0",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c268b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26858.md#insn-00c268b0) · [`00c268c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26858.md#insn-00c268c8) · [`00c268d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26858.md#insn-00c268d0)
- 新版 [`00c278a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c2784c.md#insn-00c278a4) · [`00c278bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c2784c.md#insn-00c278bc) · [`00c278c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c2784c.md#insn-00c278c4)

~~~diff
- 00c268b0 ["INT_ADD", "register:40f0:8", ["const:c268b0:8", "const:4:8"]]
- 00c268b0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c278a4 ["INT_ADD", "register:40f0:8", ["const:c278a4:8", "const:4:8"]]
+ 00c278a4 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c268b0 bytes 9cc50094
+ 00c278a4 bytes 93c50094
- 00c268c8 ["INT_ADD", "register:40f0:8", ["const:c268c8:8", "const:4:8"]]
- 00c268c8 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c278bc ["INT_ADD", "register:40f0:8", ["const:c278bc:8", "const:4:8"]]
+ 00c278bc ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c268c8 bytes 8ada0094
+ 00c278bc bytes 81da0094
- 00c268d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c268d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c278c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c278c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c268d0 bytes 00cd06f9
+ 00c278c4 bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f664b62ba57d3e9679ef9cb0ea3fbfc8"></a>

### [`00c268fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c268fc.md) → [`00c278f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c278f0.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEPwPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2797c",
      "incomplete_value": true,
      "site": "00c2797c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26988",
      "incomplete_value": true,
      "site": "00c26988",
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
            "const:d98:8"
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
      "00c27954",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2795c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27968",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27954",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2795c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27968",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c268fc.md#insn-00c26988) · [`00c26924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c268fc.md#insn-00c26924) · [`00c26928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c268fc.md#insn-00c26928)
- 新版 [`00c2797c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c278f0.md#insn-00c2797c) · [`00c27918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c278f0.md#insn-00c27918) · [`00c2791c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c278f0.md#insn-00c2791c)

~~~diff
- 00c26988 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
- 00c26988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c2797c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d58:8"]]
+ 00c2797c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26988 bytes c0ce06f9
+ 00c2797c bytes c0ae06f9
- 00c26924 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00c27918 ["COPY", "register:40a8:8", ["const:1128000:8"]]
- 00c26924 bytes 152800b0
+ 00c27918 bytes 152800b0
- 00c26928 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00c26928 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26928 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26928 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c2791c ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c2791c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c2791c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c2791c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26928 bytes b5823691
+ 00c2791c bytes b5823591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc212a95ec30063db8690c99089da5c7"></a>

### [`00c26ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ca4.md) → [`00c27c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27c98.md) _ZNSt6__ndk15ctypeIcEC1EPKmbm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f880.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c27cb0",
      "incomplete_value": true,
      "site": "00c27cb4",
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
      "definition_site": "00c26cbc",
      "incomplete_value": true,
      "site": "00c26cc0",
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
      "definition_site": "00c27cc4",
      "incomplete_value": true,
      "site": "00c27cc8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26cd0",
      "incomplete_value": true,
      "site": "00c26cd4",
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
            "const:fd8:8"
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
      "00c27ca4",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ],
    [
      "00c27cb4",
      "DATA",
      [
        "storage",
        "00c93838",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c27cc8",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27ca4",
      "READ",
      [
        "storage",
        "00c9ce68",
        null,
        "pointer"
      ]
    ],
    [
      "00c27cb4",
      "DATA",
      [
        "storage",
        "00c94808",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c27cc8",
      "DATA",
      [
        "storage",
        "00311018",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ca4.md#insn-00c26ca8) · [`00c26cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ca4.md#insn-00c26cb0) · [`00c26ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ca4.md#insn-00c26ccc)
- 新版 [`00c27c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27c98.md#insn-00c27c9c) · [`00c27ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27c98.md#insn-00c27ca4) · [`00c27cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27c98.md#insn-00c27cc0)

~~~diff
- 00c26ca8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c27c9c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c26ca8 bytes a80300b0
+ 00c27c9c bytes a80300b0
- 00c26cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
- 00c26cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c27ca4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
+ 00c27ca4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c26cb0 bytes 084d47f9
+ 00c27ca4 bytes 083547f9
- 00c26ccc ["COPY", "register:4040:8", ["const:310000:8"]]
+ 00c27cc0 ["COPY", "register:4040:8", ["const:311000:8"]]
- 00c26ccc bytes 48b7ffd0
+ 00c27cc0 bytes 48b7ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54e41a355afcb68d0538c7ac0a05b8ce"></a>

### [`00c26d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d5c.md) → [`00c27d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27d50.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27dc8",
      "incomplete_value": false,
      "site": "00c27dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26dd4",
      "incomplete_value": false,
      "site": "00c26dd4",
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
            "const:d98:8"
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
      "definition_site": "00c27da4",
      "incomplete_value": false,
      "site": "00c27da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26db0",
      "incomplete_value": false,
      "site": "00c26db4",
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
            "const:da0:8"
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
      "definition_site": "00c27db4",
      "incomplete_value": false,
      "site": "00c27dc0",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26dc0",
      "incomplete_value": false,
      "site": "00c26dcc",
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
            "const:1bc:8"
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
      "00c27d70",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27da4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27db4",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27d70",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27da4",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27db4",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d5c.md#insn-00c26db4) · [`00c26dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d5c.md#insn-00c26dcc) · [`00c26dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26d5c.md#insn-00c26dd4)
- 新版 [`00c27da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27d50.md#insn-00c27da8) · [`00c27dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27d50.md#insn-00c27dc0) · [`00c27dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27d50.md#insn-00c27dc8)

~~~diff
- 00c26db4 ["INT_ADD", "register:40f0:8", ["const:c26db4:8", "const:4:8"]]
- 00c26db4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c27da8 ["INT_ADD", "register:40f0:8", ["const:c27da8:8", "const:4:8"]]
+ 00c27da8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c26db4 bytes 5bc40094
+ 00c27da8 bytes 52c40094
- 00c26dcc ["INT_ADD", "register:40f0:8", ["const:c26dcc:8", "const:4:8"]]
- 00c26dcc ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c27dc0 ["INT_ADD", "register:40f0:8", ["const:c27dc0:8", "const:4:8"]]
+ 00c27dc0 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c26dcc bytes 49d90094
+ 00c27dc0 bytes 40d90094
- 00c26dd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c26dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c27dc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26dd4 bytes 00cd06f9
+ 00c27dc8 bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b61f43c4c35c1afd4017ecd3323c360"></a>

### [`00c26e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26e00.md) → [`00c27df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27df4.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEPcPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27e80",
      "incomplete_value": true,
      "site": "00c27e80",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26e8c",
      "incomplete_value": true,
      "site": "00c26e8c",
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
            "const:d98:8"
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
      "00c27e58",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27e60",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27e6c",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27e58",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27e60",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27e6c",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26e00.md#insn-00c26e8c) · [`00c26e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26e00.md#insn-00c26e28) · [`00c26e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26e00.md#insn-00c26e2c)
- 新版 [`00c27e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27df4.md#insn-00c27e80) · [`00c27e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27df4.md#insn-00c27e1c) · [`00c27e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27df4.md#insn-00c27e20)

~~~diff
- 00c26e8c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
- 00c26e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27e80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d58:8"]]
+ 00c27e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26e8c bytes c0ce06f9
+ 00c27e80 bytes c0ae06f9
- 00c26e28 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00c27e1c ["COPY", "register:40a8:8", ["const:1128000:8"]]
- 00c26e28 bytes 152800b0
+ 00c27e1c bytes 152800b0
- 00c26e2c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00c26e2c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26e2c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26e2c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c27e20 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c27e20 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c27e20 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c27e20 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26e2c bytes b5823691
+ 00c27e20 bytes b5823591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c8545fd446d1cee430ab216879918f7"></a>

### [`00c26ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ed4.md) → [`00c27ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27ec8.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27f40",
      "incomplete_value": false,
      "site": "00c27f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26f4c",
      "incomplete_value": false,
      "site": "00c26f4c",
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
            "const:d98:8"
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
      "definition_site": "00c27f1c",
      "incomplete_value": false,
      "site": "00c27f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26f28",
      "incomplete_value": false,
      "site": "00c26f2c",
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
            "const:da0:8"
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
      "definition_site": "00c27f2c",
      "incomplete_value": true,
      "site": "00c27f38",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26f38",
      "incomplete_value": true,
      "site": "00c26f44",
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
            "const:1bc:8"
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
      "00c27ee8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27f1c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27f2c",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27ee8",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27f1c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27f2c",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ed4.md#insn-00c26f2c) · [`00c26f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ed4.md#insn-00c26f44) · [`00c26f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26ed4.md#insn-00c26f4c)
- 新版 [`00c27f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27ec8.md#insn-00c27f20) · [`00c27f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27ec8.md#insn-00c27f38) · [`00c27f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27ec8.md#insn-00c27f40)

~~~diff
- 00c26f2c ["INT_ADD", "register:40f0:8", ["const:c26f2c:8", "const:4:8"]]
- 00c26f2c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c27f20 ["INT_ADD", "register:40f0:8", ["const:c27f20:8", "const:4:8"]]
+ 00c27f20 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c26f2c bytes fdc30094
+ 00c27f20 bytes f4c30094
- 00c26f44 ["INT_ADD", "register:40f0:8", ["const:c26f44:8", "const:4:8"]]
- 00c26f44 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c27f38 ["INT_ADD", "register:40f0:8", ["const:c27f38:8", "const:4:8"]]
+ 00c27f38 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c26f44 bytes ebd80094
+ 00c27f38 bytes e2d80094
- 00c26f4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c26f4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27f40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c27f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26f4c bytes 00cd06f9
+ 00c27f40 bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42e534016a33a347cd8db35bc592ede6"></a>

### [`00c26f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26f78.md) → [`00c27f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27f6c.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c27ff8",
      "incomplete_value": true,
      "site": "00c27ff8",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27004",
      "incomplete_value": true,
      "site": "00c27004",
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
            "const:d98:8"
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
      "00c27fd0",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27fd8",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27fe4",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c27fd0",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27fd8",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c27fe4",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26f78.md#insn-00c27004) · [`00c26fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26f78.md#insn-00c26fa0) · [`00c26fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c26/00c26f78.md#insn-00c26fa4)
- 新版 [`00c27ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27f6c.md#insn-00c27ff8) · [`00c27f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27f6c.md#insn-00c27f94) · [`00c27f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c27/00c27f6c.md#insn-00c27f98)

~~~diff
- 00c27004 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d98:8"]]
- 00c27004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c27ff8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d58:8"]]
+ 00c27ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c27004 bytes c0ce06f9
+ 00c27ff8 bytes c0ae06f9
- 00c26fa0 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00c27f94 ["COPY", "register:40a8:8", ["const:1128000:8"]]
- 00c26fa0 bytes 152800b0
+ 00c27f94 bytes 152800b0
- 00c26fa4 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00c26fa4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26fa4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26fa4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c27f98 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c27f98 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c27f98 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c27f98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26fa4 bytes b5823691
+ 00c27f98 bytes b5823591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abe349df576258f4f694336e64c25976"></a>

### [`00c27234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md) → [`00c28228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28228.md) _ZNSt6__ndk112ctype_bynameIcEC1EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea90.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5fa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa60.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c28260",
      "incomplete_value": false,
      "site": "00c28260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:311000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2726c",
      "incomplete_value": false,
      "site": "00c2726c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "definition_site": "00c282a0",
      "incomplete_value": false,
      "site": "00c282b0",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c272ac",
      "incomplete_value": false,
      "site": "00c272bc",
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
            "const:a51:8"
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
      "00c28248",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c28260",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ],
    [
      "00c28264",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c28248",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c28260",
      "DATA",
      [
        "storage",
        "00311018",
        null,
        null
      ]
    ],
    [
      "00c28264",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c272bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md#insn-00c272bc) · [`00c2724c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md#insn-00c2724c) · [`00c27254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27234.md#insn-00c27254)
- 新版 [`00c282b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28228.md#insn-00c282b0) · [`00c28240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28228.md#insn-00c28240) · [`00c28248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28228.md#insn-00c28248)

~~~diff
- 00c272bc ["INT_ADD", "register:40f0:8", ["const:c272bc:8", "const:4:8"]]
- 00c272bc ["CALL", null, ["callee:00c269c4:8"]]
+ 00c282b0 ["INT_ADD", "register:40f0:8", ["const:c282b0:8", "const:4:8"]]
+ 00c282b0 ["CALL", null, ["callee:00c269c4:8"]]
- 00c272bc bytes c5f9ff97
+ 00c282b0 bytes c5f9ff97
- 00c2724c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00c28240 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00c2724c bytes a9030090
+ 00c28240 bytes a9030090
- 00c27254 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
- 00c27254 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c28248 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 00c28248 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c27254 bytes 295147f9
+ 00c28248 bytes 293947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2367b160ee022e80cf0a5c515c9734c"></a>

### [`00c2731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c2731c.md) → [`00c28310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28310.md) _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e910.md) [`00c5eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eaa0.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)
- 新版 呼出元 2件 [`00c5f8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8e0.md) [`00c5fa70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa70.md) · 呼出先 6件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c28328",
      "incomplete_value": true,
      "site": "00c28330",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27334",
      "incomplete_value": true,
      "site": "00c2733c",
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
            "const:fd8:8"
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
      "definition_site": "00c2834c",
      "incomplete_value": true,
      "site": "00c2834c",
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
      "definition_site": "00c27358",
      "incomplete_value": true,
      "site": "00c27358",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2838c",
      "incomplete_value": false,
      "site": "00c2839c",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27398",
      "incomplete_value": false,
      "site": "00c273a8",
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
            "const:a51:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c28330",
      "DATA",
      [
        "storage",
        "00310fd8",
        null,
        null
      ]
    ],
    [
      "00c2833c",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2834c",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c28330",
      "DATA",
      [
        "storage",
        "00311018",
        null,
        null
      ]
    ],
    [
      "00c2833c",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c2834c",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c273a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c2731c.md#insn-00c273a8) · [`00c27330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c2731c.md#insn-00c27330) · [`00c27334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c2731c.md#insn-00c27334)
- 新版 [`00c2839c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28310.md#insn-00c2839c) · [`00c28324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28310.md#insn-00c28324) · [`00c28328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28310.md#insn-00c28328)

~~~diff
- 00c273a8 ["INT_ADD", "register:40f0:8", ["const:c273a8:8", "const:4:8"]]
- 00c273a8 ["CALL", null, ["callee:00c59150:8"]]
+ 00c2839c ["INT_ADD", "register:40f0:8", ["const:c2839c:8", "const:4:8"]]
+ 00c2839c ["CALL", null, ["callee:00c59150:8"]]
- 00c273a8 bytes 76c30094
+ 00c2839c bytes 6dc30094
- 00c27330 ["COPY", "register:4040:8", ["const:310000:8"]]
+ 00c28324 ["COPY", "register:4040:8", ["const:311000:8"]]
- 00c27330 bytes 48b7ffb0
+ 00c28324 bytes 48b7ffb0
- 00c27334 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00c27334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c27334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c27334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c28328 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00c28328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c28328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c28328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c27334 bytes 08613f91
+ 00c28328 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b960c751c3cbe7b11c292d036cfdf1d"></a>

### [`00c277ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md) → [`00c287a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c287a0.md) _ZNSt6__ndk112ctype_bynameIwEC2EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5eac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eac0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5fa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa90.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c287cc",
      "incomplete_value": true,
      "site": "00c287cc",
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
      "definition_site": "00c277d8",
      "incomplete_value": true,
      "site": "00c277d8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c28808",
      "incomplete_value": false,
      "site": "00c28818",
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
            "const:b6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c27814",
      "incomplete_value": false,
      "site": "00c27824",
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
            "const:a8c:8"
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
      "00c287c0",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c287cc",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c28808",
      "PARAM",
      [
        "storage",
        "002bfa8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c287c0",
      "READ",
      [
        "storage",
        "00c9ce78",
        null,
        "pointer"
      ]
    ],
    [
      "00c287cc",
      "DATA",
      [
        "storage",
        "00c948d8",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c28808",
      "PARAM",
      [
        "storage",
        "002bfb6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md#insn-00c27824) · [`00c277c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md#insn-00c277c0) · [`00c277cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c277ac.md#insn-00c277cc)
- 新版 [`00c28818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c287a0.md#insn-00c28818) · [`00c287b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c287a0.md#insn-00c287b4) · [`00c287c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c287a0.md#insn-00c287c0)

~~~diff
- 00c27824 ["INT_ADD", "register:40f0:8", ["const:c27824:8", "const:4:8"]]
- 00c27824 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c28818 ["INT_ADD", "register:40f0:8", ["const:c28818:8", "const:4:8"]]
+ 00c28818 ["CALL", null, ["callee:00c269c4:8"]]
- 00c27824 bytes 6bf8ff97
+ 00c28818 bytes 6bf8ff97
- 00c277c0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c287b4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c277c0 bytes a8030090
+ 00c287b4 bytes a8030090
- 00c277cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00c277cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c287c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c287c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c277cc bytes 085547f9
+ 00c287c0 bytes 083d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dcfc20efe9b227494aa7dcf1917e91a"></a>

### [`00c27884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27884.md) → [`00c28878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28878.md) _ZNSt6__ndk112ctype_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5e920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e920.md) [`00c5eae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eae0.md) · 呼出先 6件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)
- 新版 呼出元 2件 [`00c5f8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8f0.md) [`00c5fab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fab0.md) · 呼出先 6件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c288a4",
      "incomplete_value": true,
      "site": "00c288a4",
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
      "definition_site": "00c278b0",
      "incomplete_value": true,
      "site": "00c278b0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c288e4",
      "incomplete_value": false,
      "site": "00c288f4",
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
            "const:b6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c278f0",
      "incomplete_value": false,
      "site": "00c27900",
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
            "const:a8c:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c28898",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c288a4",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c288e4",
      "PARAM",
      [
        "storage",
        "002bfa8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c28898",
      "READ",
      [
        "storage",
        "00c9ce78",
        null,
        "pointer"
      ]
    ],
    [
      "00c288a4",
      "DATA",
      [
        "storage",
        "00c948d8",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c288e4",
      "PARAM",
      [
        "storage",
        "002bfb6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c27900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27884.md#insn-00c27900) · [`00c27898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27884.md#insn-00c27898) · [`00c278a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c27/00c27884.md#insn-00c278a4)
- 新版 [`00c288f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28878.md#insn-00c288f4) · [`00c2888c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28878.md#insn-00c2888c) · [`00c28898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c28/00c28878.md#insn-00c28898)

~~~diff
- 00c27900 ["INT_ADD", "register:40f0:8", ["const:c27900:8", "const:4:8"]]
- 00c27900 ["CALL", null, ["callee:00c59150:8"]]
+ 00c288f4 ["INT_ADD", "register:40f0:8", ["const:c288f4:8", "const:4:8"]]
+ 00c288f4 ["CALL", null, ["callee:00c59150:8"]]
- 00c27900 bytes 20c20094
+ 00c288f4 bytes 17c20094
- 00c27898 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2888c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c27898 bytes a8030090
+ 00c2888c bytes a8030090
- 00c278a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00c278a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c28898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c28898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c278a4 bytes 085547f9
+ 00c28898 bytes 083d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0518057ee57fa8ed73fe297aa78b22e8"></a>

### [`00c2829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2829c.md) → [`00c29290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c29/00c29290.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a940.md) [`00c5e8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8c0.md) · 呼出先 3件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c5b910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b910.md) [`00c5f890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f890.md) · 呼出先 3件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c292cc",
      "incomplete_value": true,
      "site": "00c292d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c282d8",
      "incomplete_value": true,
      "site": "00c282dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c29308",
      "incomplete_value": true,
      "site": "00c29308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c28314",
      "incomplete_value": true,
      "site": "00c28314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c292e8",
      "incomplete_value": false,
      "site": "00c292ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c282f4",
      "incomplete_value": false,
      "site": "00c282f8",
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
            "const:da0:8"
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
      "00c292ac",
      "READ",
      [
        "storage",
        "00c9beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c292b8",
      "DATA",
      [
        "storage",
        "00c93990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c292c4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c292ac",
      "READ",
      [
        "storage",
        "00c9ce80",
        null,
        "pointer"
      ]
    ],
    [
      "00c292b8",
      "DATA",
      [
        "storage",
        "00c94960",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c292c4",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c282f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2829c.md#insn-00c282f8) · [`00c28314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2829c.md#insn-00c28314) · [`00c282ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c28/00c2829c.md#insn-00c282ac)
- 新版 [`00c292ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c29/00c29290.md#insn-00c292ec) · [`00c29308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c29/00c29290.md#insn-00c29308) · [`00c292a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c29/00c29290.md#insn-00c292a0)

~~~diff
- 00c282f8 ["INT_ADD", "register:40f0:8", ["const:c282f8:8", "const:4:8"]]
- 00c282f8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c292ec ["INT_ADD", "register:40f0:8", ["const:c292ec:8", "const:4:8"]]
+ 00c292ec ["CALL", null, ["callee:00c58ef0:8"]]
- 00c282f8 bytes 0abf0094
+ 00c292ec bytes 01bf0094
- 00c28314 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00c28314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c29308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
+ 00c29308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c28314 bytes 80ce06f9
+ 00c29308 bytes 80ae06f9
- 00c282ac ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c292a0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c282ac bytes 880300f0
+ 00c292a0 bytes 880300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9127fe6ed6692e272cf65ca82d7c5b47"></a>

### [`00c2bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf08.md) → [`00c2cefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cefc.md) _ZNSt6__ndk18numpunctIcEC2Em

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5f8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cf20",
      "incomplete_value": true,
      "site": "00c2cf20",
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
      "definition_site": "00c2bf2c",
      "incomplete_value": true,
      "site": "00c2bf2c",
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
      "00c2cf08",
      "READ",
      [
        "storage",
        "00c9beb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2cf20",
      "DATA",
      [
        "storage",
        "00c939f0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2cf08",
      "READ",
      [
        "storage",
        "00c9ce88",
        null,
        "pointer"
      ]
    ],
    [
      "00c2cf20",
      "DATA",
      [
        "storage",
        "00c949c0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bf0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf08.md#insn-00c2bf0c) · [`00c2bf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf08.md#insn-00c2bf14)
- 新版 [`00c2cf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cefc.md#insn-00c2cf00) · [`00c2cf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cefc.md#insn-00c2cf08)

~~~diff
- 00c2bf0c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00c2cf00 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00c2bf0c bytes 89030090
+ 00c2cf00 bytes 89030090
- 00c2bf14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:eb8:8"]]
- 00c2bf14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2cf08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e88:8"]]
+ 00c2cf08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2bf14 bytes 295d47f9
+ 00c2cf08 bytes 294547f9
~~~


<a id="compare-cdee0dcd2f9b4ba0f8c71e53e78069fa"></a>

### [`00c2bf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf34.md) → [`00c2cf28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cf28.md) _ZNSt6__ndk18numpunctIwEC1Em

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e8e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5f8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f8b0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cf3c",
      "incomplete_value": true,
      "site": "00c2cf4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2bf48",
      "incomplete_value": true,
      "site": "00c2bf58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c2cf50",
      "incomplete_value": true,
      "site": "00c2cf50",
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
      "definition_site": "00c2bf5c",
      "incomplete_value": true,
      "site": "00c2bf5c",
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
      "00c2cf38",
      "READ",
      [
        "storage",
        "00c9bec0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2cf3c",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cf50",
      "DATA",
      [
        "storage",
        "00c93a40",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2cf38",
      "READ",
      [
        "storage",
        "00c9ce90",
        null,
        "pointer"
      ]
    ],
    [
      "00c2cf3c",
      "READ",
      [
        "storage",
        "002c4378",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2cf50",
      "DATA",
      [
        "storage",
        "00c94a10",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2bf38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf34.md#insn-00c2bf38) · [`00c2bf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf34.md#insn-00c2bf44) · [`00c2bf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf34.md#insn-00c2bf48)
- 新版 [`00c2cf2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cf28.md#insn-00c2cf2c) · [`00c2cf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cf28.md#insn-00c2cf38) · [`00c2cf3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2c/00c2cf28.md#insn-00c2cf3c)

~~~diff
- 00c2bf38 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00c2cf2c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00c2bf38 bytes 89030090
+ 00c2cf2c bytes 89030090
- 00c2bf44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
- 00c2bf44 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2cf38 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e90:8"]]
+ 00c2cf38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2bf44 bytes 296147f9
+ 00c2cf38 bytes 294947f9
- 00c2bf48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
- 00c2bf48 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2bf48 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2bf48 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2cf3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 00c2cf3c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2cf3c ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2cf3c ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2bf48 bytes 009541fd
+ 00c2cf3c bytes 00bd41fd
~~~


<a id="compare-ea03faab4738616fb588de34aae0ae7d"></a>

### [`00c2c10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c10c.md) → [`00c2d100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d100.md) _ZNKSt6__ndk18numpunctIwE11do_truenameEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d110",
      "incomplete_value": true,
      "site": "00c2d11c",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c11c",
      "incomplete_value": true,
      "site": "00c2c128",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:778:8"
              ]
            ]
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
      "00c2d110",
      "READ",
      [
        "storage",
        "00310778",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2d110",
      "READ",
      [
        "storage",
        "003107b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c10c.md#insn-00c2c114)
- 新版 [`00c2d108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d100.md#insn-00c2d108)

~~~diff
- 00c2c114 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00c2c114 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c2c114 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c2c114 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c2d108 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00c2d108 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2d108 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c2d108 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c2c114 bytes 4ae11d91
+ 00c2d108 bytes 4ae11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e73dcff24744d97a86216aaa4951608f"></a>

### [`00c2c210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c210.md) → [`00c2d204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d204.md) _ZNKSt6__ndk18numpunctIwE12do_falsenameEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d22c",
      "incomplete_value": true,
      "site": "00c2d240",
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c238",
      "incomplete_value": true,
      "site": "00c2c24c",
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
                "const:570:8"
              ]
            ]
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
      "definition_site": "00c2d238",
      "incomplete_value": true,
      "site": "00c2d244",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:834:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c244",
      "incomplete_value": true,
      "site": "00c2c250",
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
                "const:310000:8"
              ],
              [
                "leaf",
                "const:7f4:8"
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
      "00c2d22c",
      "READ",
      [
        "storage",
        "002c2570",
        null,
        null
      ]
    ],
    [
      "00c2d238",
      "READ",
      [
        "storage",
        "003107f4",
        null,
        "unicode32"
      ]
    ]
  ],
  "added": [
    [
      "00c2d22c",
      "READ",
      [
        "storage",
        "002c25c0",
        null,
        null
      ]
    ],
    [
      "00c2d238",
      "READ",
      [
        "storage",
        "00310834",
        null,
        "unicode32"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c210.md#insn-00c2c228) · [`00c2c238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c210.md#insn-00c2c238) · [`00c2c23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c210.md#insn-00c2c23c)
- 新版 [`00c2d21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d204.md#insn-00c2d21c) · [`00c2d22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d204.md#insn-00c2d22c)

~~~diff
- 00c2c228 ["INT_ADD", "register:40f0:8", ["const:c2c228:8", "const:4:8"]]
- 00c2c228 ["CALL", null, ["callee:00c58f30:8"]]
+ 00c2d21c ["INT_ADD", "register:40f0:8", ["const:c2d21c:8", "const:4:8"]]
+ 00c2d21c ["CALL", null, ["callee:00c58f30:8"]]
- 00c2c228 bytes 4eaf0094
+ 00c2d21c bytes 45af0094
- 00c2c238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:570:8"]]
- 00c2c238 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2c238 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c238 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2d22c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 00c2d22c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d22c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2d22c ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2c238 bytes 005dc13d
+ 00c2d22c bytes 0071c13d
- 00c2c23c ["COPY", "register:4040:8", ["const:310000:8"]]
- 00c2c23c bytes 28b7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4388b166c82ed602a82924c240dca9bd"></a>

### [`00c2c264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c264.md) → [`00c2d258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d258.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5fcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fcf0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d28c",
      "incomplete_value": true,
      "site": "00c2d28c",
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
      "definition_site": "00c2c298",
      "incomplete_value": true,
      "site": "00c2c298",
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
      "00c2d280",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d28c",
      "DATA",
      [
        "storage",
        "00c93a90",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2d280",
      "READ",
      [
        "storage",
        "00c9ce98",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d28c",
      "DATA",
      [
        "storage",
        "00c94a60",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c264.md#insn-00c2c284) · [`00c2c28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c264.md#insn-00c2c28c) · [`00c2c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c264.md#insn-00c2c29c)
- 新版 [`00c2d278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d258.md#insn-00c2d278) · [`00c2d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d258.md#insn-00c2d280) · [`00c2d290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d258.md#insn-00c2d290)

~~~diff
- 00c2c284 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2d278 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c2c284 bytes 680300f0
+ 00c2d278 bytes 680300f0
- 00c2c28c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
- 00c2c28c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00c2d280 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c28c bytes 086547f9
+ 00c2d280 bytes 084d47f9
- 00c2c29c ["INT_ADD", "register:40f0:8", ["const:c2c29c:8", "const:4:8"]]
- 00c2c29c ["CALL", null, ["callee:00c5fcf0:8"]]
+ 00c2d290 ["INT_ADD", "register:40f0:8", ["const:c2d290:8", "const:4:8"]]
+ 00c2d290 ["CALL", null, ["callee:00c5fcf0:8"]]
- 00c2c29c bytes a1ca0094
+ 00c2d290 bytes 98ca0094
~~~


<a id="compare-8a4518d87d8c998fa6a8532bf58b8819"></a>

### [`00c2c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md) → [`00c2d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d2b8.md) _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md) · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5fcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fcf0.md) · 呼出先 13件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2d4e4",
      "incomplete_value": false,
      "site": "00c2d4f4",
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
            "const:a3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c4f0",
      "incomplete_value": false,
      "site": "00c2c500",
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
            "const:96f:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2d2e0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00c2d4e4",
      "PARAM",
      [
        "storage",
        "002a996f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2d2e0",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ],
    [
      "00c2d4e4",
      "PARAM",
      [
        "storage",
        "002a9a3c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md#insn-00c2c500) · [`00c2c2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md#insn-00c2c2ec) · [`00c2c2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md#insn-00c2c2f4)
- 新版 [`00c2d4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d2b8.md#insn-00c2d4f4) · [`00c2d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d2b8.md#insn-00c2d2e0) · [`00c2d2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d2b8.md#insn-00c2d2e8)

~~~diff
- 00c2c500 ["INT_ADD", "register:40f0:8", ["const:c2c500:8", "const:4:8"]]
- 00c2c500 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c2d4f4 ["INT_ADD", "register:40f0:8", ["const:c2d4f4:8", "const:4:8"]]
+ 00c2d4f4 ["CALL", null, ["callee:00c269c4:8"]]
- 00c2c500 bytes 34e5ff97
+ 00c2d4f4 bytes 34e5ff97
- 00c2c2ec ["COPY", "tmp:0:8", ["const:1bc:8"]]
- 00c2c2ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c2ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c2ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c2d2e0 ["COPY", "tmp:0:8", ["const:28b:8"]]
+ 00c2d2e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2d2e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2d2e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c2c2ec bytes 21f00691
+ 00c2d2e0 bytes 212c0a91
- 00c2c2f4 ["INT_ADD", "register:40f0:8", ["const:c2c2f4:8", "const:4:8"]]
- 00c2c2f4 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c2d2e8 ["INT_ADD", "register:40f0:8", ["const:c2d2e8:8", "const:4:8"]]
+ 00c2d2e8 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c2c2f4 bytes 8bbd0094
+ 00c2d2e8 bytes 82bd0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e466ce26542cebaad1f4397a972bfa5b"></a>

### [`00c2c598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c598.md) → [`00c2d58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d58c.md) _ZNSt6__ndk115numpunct_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e940.md) · 呼出先 1件 [`00c5ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed20.md)
- 新版 呼出元 1件 [`00c5f910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f910.md) · 呼出先 1件 [`00c5fcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fcf0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2d5c0",
      "incomplete_value": true,
      "site": "00c2d5c0",
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
      "definition_site": "00c2c5cc",
      "incomplete_value": true,
      "site": "00c2c5cc",
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
      "00c2d5b4",
      "READ",
      [
        "storage",
        "00c9bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d5c0",
      "DATA",
      [
        "storage",
        "00c93a90",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2d5b4",
      "READ",
      [
        "storage",
        "00c9ce98",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d5c0",
      "DATA",
      [
        "storage",
        "00c94a60",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c598.md#insn-00c2c5b8) · [`00c2c5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c598.md#insn-00c2c5c0) · [`00c2c5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c598.md#insn-00c2c5e0)
- 新版 [`00c2d5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d58c.md#insn-00c2d5ac) · [`00c2d5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d58c.md#insn-00c2d5b4) · [`00c2d5d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d58c.md#insn-00c2d5d4)

~~~diff
- 00c2c5b8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2d5ac ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c2c5b8 bytes 680300f0
+ 00c2d5ac bytes 680300f0
- 00c2c5c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
- 00c2c5c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d5b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00c2d5b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c5c0 bytes 086547f9
+ 00c2d5b4 bytes 084d47f9
- 00c2c5e0 ["INT_ADD", "register:40f0:8", ["const:c2c5e0:8", "const:4:8"]]
- 00c2c5e0 ["CALL", null, ["callee:00c5fcf0:8"]]
+ 00c2d5d4 ["INT_ADD", "register:40f0:8", ["const:c2d5d4:8", "const:4:8"]]
+ 00c2d5d4 ["CALL", null, ["callee:00c5fcf0:8"]]
- 00c2c5e0 bytes d0c90094
+ 00c2d5d4 bytes c7c90094
~~~


<a id="compare-dce5ff799e89a2b16aa24857e1f6a3e9"></a>

### [`00c2c65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c65c.md) → [`00c2d650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d650.md) _ZNSt6__ndk115numpunct_bynameIwEC1EPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5fd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

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
      "definition_site": "00c2d66c",
      "incomplete_value": true,
      "site": "00c2d680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c678",
      "incomplete_value": true,
      "site": "00c2c68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
      "definition_site": "00c2d688",
      "incomplete_value": true,
      "site": "00c2d688",
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
      "definition_site": "00c2c694",
      "incomplete_value": true,
      "site": "00c2c694",
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
      "00c2d66c",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d678",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d688",
      "DATA",
      [
        "storage",
        "00c93ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2d66c",
      "READ",
      [
        "storage",
        "002c4378",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d678",
      "READ",
      [
        "storage",
        "00c9cea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d688",
      "DATA",
      [
        "storage",
        "00c94ab0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c65c.md#insn-00c2c678) · [`00c2c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c65c.md#insn-00c2c680) · [`00c2c684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c65c.md#insn-00c2c684)
- 新版 [`00c2d66c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d650.md#insn-00c2d66c) · [`00c2d674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d650.md#insn-00c2d674) · [`00c2d678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d650.md#insn-00c2d678)

~~~diff
- 00c2c678 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
- 00c2c678 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c678 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c678 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2d66c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 00c2d66c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d66c ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2d66c ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c678 bytes 009541fd
+ 00c2d66c bytes 00bd41fd
- 00c2c680 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2d674 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c2c680 bytes 680300f0
+ 00c2d674 bytes 680300f0
- 00c2c684 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
- 00c2c684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d678 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c2d678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c684 bytes 086947f9
+ 00c2d678 bytes 085147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9080c6ada4c3096d98799b3e1be7a677"></a>

### [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) → [`00c2d6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md) _ZNSt6__ndk115numpunct_bynameIwE6__initEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md) · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`00c5fd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd20.md) · 呼出先 14件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c2d628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d628.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2d6dc",
      "incomplete_value": false,
      "site": "00c2d6e4",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c6e8",
      "incomplete_value": false,
      "site": "00c2c6f0",
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
            "const:1bc:8"
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
      "definition_site": "00c2d828",
      "incomplete_value": false,
      "site": "00c2d838",
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
            "const:831:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c834",
      "incomplete_value": false,
      "site": "00c2c844",
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
            "const:75a:8"
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
      "00c2d6dc",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00c2d828",
      "PARAM",
      [
        "storage",
        "002b175a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2d6dc",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ],
    [
      "00c2d828",
      "PARAM",
      [
        "storage",
        "002b1831",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md#insn-00c2c6f0) · [`00c2c844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md#insn-00c2c844) · [`00c2c6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md#insn-00c2c6e8)
- 新版 [`00c2d6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md#insn-00c2d6e4) · [`00c2d838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md#insn-00c2d838) · [`00c2d6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md#insn-00c2d6dc)

~~~diff
- 00c2c6f0 ["INT_ADD", "register:40f0:8", ["const:c2c6f0:8", "const:4:8"]]
- 00c2c6f0 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c2d6e4 ["INT_ADD", "register:40f0:8", ["const:c2d6e4:8", "const:4:8"]]
+ 00c2d6e4 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c2c6f0 bytes 8cbc0094
+ 00c2d6e4 bytes 83bc0094
- 00c2c844 ["INT_ADD", "register:40f0:8", ["const:c2c844:8", "const:4:8"]]
- 00c2c844 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c2d838 ["INT_ADD", "register:40f0:8", ["const:c2d838:8", "const:4:8"]]
+ 00c2d838 ["CALL", null, ["callee:00c269c4:8"]]
- 00c2c844 bytes 63e4ff97
+ 00c2d838 bytes 63e4ff97
- 00c2c6e8 ["COPY", "tmp:0:8", ["const:1bc:8"]]
- 00c2c6e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c6e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c2c6e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c2d6dc ["COPY", "tmp:0:8", ["const:28b:8"]]
+ 00c2d6dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2d6dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c2d6dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c2c6e8 bytes 21f00691
+ 00c2d6dc bytes 212c0a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6b628d1e6a7dc128dc1240eb51a85c9"></a>

### [`00c2c8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c8cc.md) → [`00c2d8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d8c0.md) _ZNSt6__ndk115numpunct_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e950.md) · 呼出先 1件 [`00c5ed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed50.md)
- 新版 呼出元 1件 [`00c5f920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f920.md) · 呼出先 1件 [`00c5fd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "00c2d8dc",
      "incomplete_value": true,
      "site": "00c2d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2c8e8",
      "incomplete_value": true,
      "site": "00c2c8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
      "definition_site": "00c2d8f8",
      "incomplete_value": true,
      "site": "00c2d8f8",
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
      "definition_site": "00c2c904",
      "incomplete_value": true,
      "site": "00c2c904",
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
      "00c2d8dc",
      "READ",
      [
        "storage",
        "002c4328",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d8e8",
      "READ",
      [
        "storage",
        "00c9bed0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d8f8",
      "DATA",
      [
        "storage",
        "00c93ae0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2d8dc",
      "READ",
      [
        "storage",
        "002c4378",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2d8e8",
      "READ",
      [
        "storage",
        "00c9cea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2d8f8",
      "DATA",
      [
        "storage",
        "00c94ab0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2c8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c8cc.md#insn-00c2c8e8) · [`00c2c8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c8cc.md#insn-00c2c8f0) · [`00c2c8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c8cc.md#insn-00c2c8f4)
- 新版 [`00c2d8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d8c0.md#insn-00c2d8dc) · [`00c2d8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d8c0.md#insn-00c2d8e4) · [`00c2d8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d8c0.md#insn-00c2d8e8)

~~~diff
- 00c2c8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
- 00c2c8e8 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c8e8 ["COPY", "register:5008:8", ["const:0:8"]]
- 00c2c8e8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2d8dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:378:8"]]
+ 00c2d8dc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d8dc ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c2d8dc ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2c8e8 bytes 009541fd
+ 00c2d8dc bytes 00bd41fd
- 00c2c8f0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c2d8e4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c2c8f0 bytes 680300f0
+ 00c2d8e4 bytes 680300f0
- 00c2c8f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
- 00c2c8f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2d8e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 00c2d8e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2c8f4 bytes 086947f9
+ 00c2d8e8 bytes 085147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e431110b86835b2e00dcd59f765dacdb"></a>

### [`00c2cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md) → [`00c2db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db00.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2cb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2db5c",
      "incomplete_value": false,
      "site": "00c2db5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb68",
      "incomplete_value": false,
      "site": "00c2cb68",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2db4c",
      "incomplete_value": false,
      "site": "00c2db5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb58",
      "incomplete_value": false,
      "site": "00c2cb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "definition_site": "00c2db34",
      "incomplete_value": false,
      "site": "00c2db38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cb40",
      "incomplete_value": false,
      "site": "00c2cb44",
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
            "const:fb0:8"
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
      "00c2db14",
      "READ",
      [
        "storage",
        "01127fb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2db20",
      "READ",
      [
        "storage",
        "01127fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2db20",
      "DATA",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2db14",
      "READ",
      [
        "storage",
        "01128f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2db20",
      "READ",
      [
        "storage",
        "01128f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2db20",
      "DATA",
      [
        "storage",
        "01129068",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md#insn-00c2cb44) · [`00c2cb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md#insn-00c2cb68) · [`00c2cb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md#insn-00c2cb6c)
- 新版 [`00c2db38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db00.md#insn-00c2db38) · [`00c2db5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db00.md#insn-00c2db5c) · [`00c2db60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db00.md#insn-00c2db60)

~~~diff
- 00c2cb44 ["INT_ADD", "register:40f0:8", ["const:c2cb44:8", "const:4:8"]]
- 00c2cb44 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2db38 ["INT_ADD", "register:40f0:8", ["const:c2db38:8", "const:4:8"]]
+ 00c2db38 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2cb44 bytes f7ac0094
+ 00c2db38 bytes eeac0094
- 00c2cb68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
- 00c2cb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2db5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 00c2db5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2cb68 bytes 09d507f9
+ 00c2db5c bytes 09b507f9
- 00c2cb6c ["INT_ADD", "register:40f0:8", ["const:c2cb6c:8", "const:4:8"]]
- 00c2cb6c ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2db60 ["INT_ADD", "register:40f0:8", ["const:c2db60:8", "const:4:8"]]
+ 00c2db60 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2cb6c bytes f5ac0094
+ 00c2db60 bytes ecac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261818de5536422963dddbb1fa0f22cb"></a>

### [`00c2cb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md) → [`00c2db6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md) FUN_00c2db6c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2cb0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb0c.md) · 呼出先 4件 [`00c35c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35c3c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c2db00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db00.md) · 呼出先 4件 [`00c36c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36c30.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.48% / 新版 71.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 21件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2dba0",
      "incomplete_value": false,
      "site": "00c2dba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cbac",
      "incomplete_value": false,
      "site": "00c2cbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "definition_site": "00c2dbb8",
      "incomplete_value": false,
      "site": "00c2dbb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cbc4",
      "incomplete_value": false,
      "site": "00c2cbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "definition_site": "00c2dbec",
      "incomplete_value": false,
      "site": "00c2dbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cbf8",
      "incomplete_value": false,
      "site": "00c2cbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "00c2db80",
      "READ",
      [
        "storage",
        "011281f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2db8c",
      "READ",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dba0",
      "WRITE",
      [
        "storage",
        "011280a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2db80",
      "READ",
      [
        "storage",
        "011291b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2db8c",
      "READ",
      [
        "storage",
        "01129068",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dba0",
      "WRITE",
      [
        "storage",
        "01129068",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md#insn-00c2cf80) · [`00c2cf9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md#insn-00c2cf9c) · [`00c2cfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cb78.md#insn-00c2cfa8)
- 新版 [`00c2df74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md#insn-00c2df74) · [`00c2df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md#insn-00c2df90) · [`00c2df9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2db6c.md#insn-00c2df9c)

~~~diff
- 00c2cf80 ["INT_ADD", "register:40f0:8", ["const:c2cf80:8", "const:4:8"]]
- 00c2cf80 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2df74 ["INT_ADD", "register:40f0:8", ["const:c2df74:8", "const:4:8"]]
+ 00c2df74 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2cf80 bytes e8ab0094
+ 00c2df74 bytes dfab0094
- 00c2cf9c ["INT_ADD", "register:40f0:8", ["const:c2cf9c:8", "const:4:8"]]
- 00c2cf9c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2df90 ["INT_ADD", "register:40f0:8", ["const:c2df90:8", "const:4:8"]]
+ 00c2df90 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2cf9c bytes d9ab0094
+ 00c2df90 bytes d0ab0094
- 00c2cfa8 ["INT_ADD", "register:40f0:8", ["const:c2cfa8:8", "const:4:8"]]
- 00c2cfa8 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2df9c ["INT_ADD", "register:40f0:8", ["const:c2df9c:8", "const:4:8"]]
+ 00c2df9c ["CALL", null, ["callee:00c58f10:8"]]
- 00c2cfa8 bytes e6ab0094
+ 00c2df9c bytes ddab0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27805f0f7ebf19bcb334d41280f4da39"></a>

### [`00c2cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md) → [`00c2dfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2dfa4.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d030.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e024.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e000",
      "incomplete_value": true,
      "site": "00c2e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d00c",
      "incomplete_value": true,
      "site": "00c2d00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2dff4",
      "incomplete_value": false,
      "site": "00c2e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d000",
      "incomplete_value": false,
      "site": "00c2d00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "definition_site": "00c2dfe0",
      "incomplete_value": false,
      "site": "00c2dfe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2cfec",
      "incomplete_value": false,
      "site": "00c2cff0",
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
            "const:fc0:8"
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
      "00c2dfc0",
      "READ",
      [
        "storage",
        "01127fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dfc8",
      "READ",
      [
        "storage",
        "01127fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2dfc8",
      "DATA",
      [
        "storage",
        "01128200",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2dfc0",
      "READ",
      [
        "storage",
        "01128f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2dfc8",
      "READ",
      [
        "storage",
        "01128f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2dfc8",
      "DATA",
      [
        "storage",
        "011291c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2cff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md#insn-00c2cff0) · [`00c2cff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md#insn-00c2cff8) · [`00c2d00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2cfb0.md#insn-00c2d00c)
- 新版 [`00c2dfe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2dfa4.md#insn-00c2dfe4) · [`00c2dfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2dfa4.md#insn-00c2dfec) · [`00c2e000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2dfa4.md#insn-00c2e000)

~~~diff
- 00c2cff0 ["INT_ADD", "register:40f0:8", ["const:c2cff0:8", "const:4:8"]]
- 00c2cff0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2dfe4 ["INT_ADD", "register:40f0:8", ["const:c2dfe4:8", "const:4:8"]]
+ 00c2dfe4 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2cff0 bytes ccab0094
+ 00c2dfe4 bytes c3ab0094
- 00c2cff8 ["INT_ADD", "register:40f0:8", ["const:c2cff8:8", "const:4:8"]]
- 00c2cff8 ["CALL", null, ["ram:c2d030:8"]]
+ 00c2dfec ["INT_ADD", "register:40f0:8", ["const:c2dfec:8", "const:4:8"]]
+ 00c2dfec ["CALL", null, ["ram:c2e024:8"]]
- 00c2cff8 bytes 0e000094
+ 00c2dfec bytes 0e000094
- 00c2d00c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00c2d00c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2e000 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f78:8"]]
+ 00c2e000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2d00c bytes 68de07f9
+ 00c2e000 bytes 68be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d549bd54bda2f3b7af6220113f77a43"></a>

### [`00c2d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md) → [`00c2e2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e2f8.md) _ZNKSt6__ndk120__time_get_c_storageIcE8__monthsEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2e364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e354",
      "incomplete_value": false,
      "site": "00c2e354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d360",
      "incomplete_value": false,
      "site": "00c2d360",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2e344",
      "incomplete_value": false,
      "site": "00c2e354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d350",
      "incomplete_value": false,
      "site": "00c2d360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "definition_site": "00c2e32c",
      "incomplete_value": false,
      "site": "00c2e330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d338",
      "incomplete_value": false,
      "site": "00c2d33c",
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
            "const:fd0:8"
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
      "00c2e30c",
      "READ",
      [
        "storage",
        "01127fd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "READ",
      [
        "storage",
        "01127fc8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e30c",
      "READ",
      [
        "storage",
        "01128f90",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e318",
      "READ",
      [
        "storage",
        "01128f88",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2e318",
      "DATA",
      [
        "storage",
        "01129318",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md#insn-00c2d33c) · [`00c2d360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md#insn-00c2d360) · [`00c2d364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md#insn-00c2d364)
- 新版 [`00c2e330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e2f8.md#insn-00c2e330) · [`00c2e354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e2f8.md#insn-00c2e354) · [`00c2e358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e2f8.md#insn-00c2e358)

~~~diff
- 00c2d33c ["INT_ADD", "register:40f0:8", ["const:c2d33c:8", "const:4:8"]]
- 00c2d33c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2e330 ["INT_ADD", "register:40f0:8", ["const:c2e330:8", "const:4:8"]]
+ 00c2e330 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2d33c bytes f9aa0094
+ 00c2e330 bytes f0aa0094
- 00c2d360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
- 00c2d360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2e354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00c2e354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2d360 bytes 09e507f9
+ 00c2e354 bytes 09c507f9
- 00c2d364 ["INT_ADD", "register:40f0:8", ["const:c2d364:8", "const:4:8"]]
- 00c2d364 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2e358 ["INT_ADD", "register:40f0:8", ["const:c2e358:8", "const:4:8"]]
+ 00c2e358 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2d364 bytes f7aa0094
+ 00c2e358 bytes eeaa0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5888db51d61a134079d78d860d8b90c3"></a>

### [`00c2d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md) → [`00c2e364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md) FUN_00c2e364

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d304.md) · 呼出先 4件 [`00c35f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35f1c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c2e2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e2f8.md) · 呼出先 4件 [`00c36f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36f10.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 70.48% / 新版 70.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 45件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2e398",
      "incomplete_value": false,
      "site": "00c2e398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d3a4",
      "incomplete_value": false,
      "site": "00c2d3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "definition_site": "00c2e3b0",
      "incomplete_value": false,
      "site": "00c2e3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d3bc",
      "incomplete_value": false,
      "site": "00c2d3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "definition_site": "00c2e3e8",
      "incomplete_value": false,
      "site": "00c2e3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2d3f4",
      "incomplete_value": false,
      "site": "00c2d3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "00c2e378",
      "READ",
      [
        "storage",
        "01128598",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e384",
      "READ",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e398",
      "WRITE",
      [
        "storage",
        "01128358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2e378",
      "READ",
      [
        "storage",
        "01129558",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e384",
      "READ",
      [
        "storage",
        "01129318",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2e398",
      "WRITE",
      [
        "storage",
        "01129318",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2d37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md#insn-00c2d37c) · [`00c2d380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md#insn-00c2d380) · [`00c2d38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d370.md#insn-00c2d38c)
- 新版 [`00c2e370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md#insn-00c2e370) · [`00c2e374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md#insn-00c2e374) · [`00c2e380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e364.md#insn-00c2e380)

~~~diff
- 00c2d37c ["COPY", "register:4040:8", ["const:1128000:8"]]
+ 00c2e370 ["COPY", "register:4040:8", ["const:1129000:8"]]
- 00c2d37c bytes c82700f0
+ 00c2e370 bytes c82700f0
- 00c2d380 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00c2d380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c2d380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c2d380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c2e374 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00c2e374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2e374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c2d380 bytes 08611691
+ 00c2e374 bytes 08611591
- 00c2d38c ["COPY", "register:4040:8", ["const:1128000:8"]]
+ 00c2e380 ["COPY", "register:4040:8", ["const:1129000:8"]]
- 00c2d38c bytes c82700f0
+ 00c2e380 bytes c82700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1bd16e357ba345bc7f6f94cb0ce6b2"></a>

### [`00c2da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md) → [`00c2ea38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2ea38.md) _ZNKSt6__ndk120__time_get_c_storageIwE8__monthsEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dac4.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2eab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2eab8.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2ea94",
      "incomplete_value": true,
      "site": "00c2ea94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2daa0",
      "incomplete_value": true,
      "site": "00c2daa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2ea88",
      "incomplete_value": false,
      "site": "00c2ea94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2da94",
      "incomplete_value": false,
      "site": "00c2daa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "definition_site": "00c2ea74",
      "incomplete_value": true,
      "site": "00c2ea78",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2da80",
      "incomplete_value": true,
      "site": "00c2da84",
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
            "const:fe0:8"
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
      "00c2ea54",
      "READ",
      [
        "storage",
        "01127fe0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2ea5c",
      "READ",
      [
        "storage",
        "01127fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2ea5c",
      "DATA",
      [
        "storage",
        "011285a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2ea54",
      "READ",
      [
        "storage",
        "01128fa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2ea5c",
      "READ",
      [
        "storage",
        "01128f98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2ea5c",
      "DATA",
      [
        "storage",
        "01129560",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md#insn-00c2da84) · [`00c2da8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md#insn-00c2da8c) · [`00c2daa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2da44.md#insn-00c2daa0)
- 新版 [`00c2ea78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2ea38.md#insn-00c2ea78) · [`00c2ea80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2ea38.md#insn-00c2ea80) · [`00c2ea94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2ea38.md#insn-00c2ea94)

~~~diff
- 00c2da84 ["INT_ADD", "register:40f0:8", ["const:c2da84:8", "const:4:8"]]
- 00c2da84 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2ea78 ["INT_ADD", "register:40f0:8", ["const:c2ea78:8", "const:4:8"]]
+ 00c2ea78 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2da84 bytes 27a90094
+ 00c2ea78 bytes 1ea90094
- 00c2da8c ["INT_ADD", "register:40f0:8", ["const:c2da8c:8", "const:4:8"]]
- 00c2da8c ["CALL", null, ["ram:c2dac4:8"]]
+ 00c2ea80 ["INT_ADD", "register:40f0:8", ["const:c2ea80:8", "const:4:8"]]
+ 00c2ea80 ["CALL", null, ["ram:c2eab8:8"]]
- 00c2da8c bytes 0e000094
+ 00c2ea80 bytes 0e000094
- 00c2daa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd8:8"]]
- 00c2daa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c2ea94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f98:8"]]
+ 00c2ea94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2daa0 bytes 68ee07f9
+ 00c2ea94 bytes 68ce07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82c94ee279635166865e27d93e0d4377"></a>

### [`00c2dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md) → [`00c2efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2e058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2f04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2f03c",
      "incomplete_value": true,
      "site": "00c2f03c",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e048",
      "incomplete_value": true,
      "site": "00c2e048",
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
            "const:fe8:8"
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
      "definition_site": "00c2f014",
      "incomplete_value": false,
      "site": "00c2f018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e020",
      "incomplete_value": false,
      "site": "00c2e024",
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
            "const:ff0:8"
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
      "definition_site": "00c2f038",
      "incomplete_value": true,
      "site": "00c2f040",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e044",
      "incomplete_value": true,
      "site": "00c2e04c",
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
            "const:ff0:8"
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
      "00c2eff4",
      "READ",
      [
        "storage",
        "01127ff0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f000",
      "READ",
      [
        "storage",
        "01127fe8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2f000",
      "DATA",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2eff4",
      "READ",
      [
        "storage",
        "01128fb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f000",
      "READ",
      [
        "storage",
        "01128fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2f000",
      "DATA",
      [
        "storage",
        "011297a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md#insn-00c2e024) · [`00c2e048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md#insn-00c2e048) · [`00c2e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md#insn-00c2e04c)
- 新版 [`00c2f018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md#insn-00c2f018) · [`00c2f03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md#insn-00c2f03c) · [`00c2f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md#insn-00c2f040)

~~~diff
- 00c2e024 ["INT_ADD", "register:40f0:8", ["const:c2e024:8", "const:4:8"]]
- 00c2e024 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f018 ["INT_ADD", "register:40f0:8", ["const:c2f018:8", "const:4:8"]]
+ 00c2f018 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e024 bytes bfa70094
+ 00c2f018 bytes b6a70094
- 00c2e048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe8:8"]]
- 00c2e048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2f03c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 00c2f03c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2e048 bytes 09f507f9
+ 00c2f03c bytes 09d507f9
- 00c2e04c ["INT_ADD", "register:40f0:8", ["const:c2e04c:8", "const:4:8"]]
- 00c2e04c ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f040 ["INT_ADD", "register:40f0:8", ["const:c2f040:8", "const:4:8"]]
+ 00c2f040 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e04c bytes bda70094
+ 00c2f040 bytes b4a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4869d10b01134355dd83d0edbdced35"></a>

### [`00c2e058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md) → [`00c2f04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md) FUN_00c2f04c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dfec.md) · 呼出先 4件 [`00c35fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35fbc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c2efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2efe0.md) · 呼出先 4件 [`00c36fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36fb0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2f080",
      "incomplete_value": false,
      "site": "00c2f080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e08c",
      "incomplete_value": false,
      "site": "00c2e08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "definition_site": "00c2f098",
      "incomplete_value": false,
      "site": "00c2f098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e0a4",
      "incomplete_value": false,
      "site": "00c2e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "definition_site": "00c2f0c0",
      "incomplete_value": false,
      "site": "00c2f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e0cc",
      "incomplete_value": false,
      "site": "00c2e0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "00c2f060",
      "READ",
      [
        "storage",
        "01128818",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f06c",
      "READ",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f080",
      "WRITE",
      [
        "storage",
        "011287e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f060",
      "READ",
      [
        "storage",
        "011297d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f06c",
      "READ",
      [
        "storage",
        "011297a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f080",
      "WRITE",
      [
        "storage",
        "011297a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md#insn-00c2e108) · [`00c2e124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md#insn-00c2e124) · [`00c2e130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e058.md#insn-00c2e130)
- 新版 [`00c2f0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md#insn-00c2f0fc) · [`00c2f118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md#insn-00c2f118) · [`00c2f124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f04c.md#insn-00c2f124)

~~~diff
- 00c2e108 ["INT_ADD", "register:40f0:8", ["const:c2e108:8", "const:4:8"]]
- 00c2e108 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f0fc ["INT_ADD", "register:40f0:8", ["const:c2f0fc:8", "const:4:8"]]
+ 00c2f0fc ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e108 bytes 86a70094
+ 00c2f0fc bytes 7da70094
- 00c2e124 ["INT_ADD", "register:40f0:8", ["const:c2e124:8", "const:4:8"]]
- 00c2e124 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f118 ["INT_ADD", "register:40f0:8", ["const:c2f118:8", "const:4:8"]]
+ 00c2f118 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e124 bytes 77a70094
+ 00c2f118 bytes 6ea70094
- 00c2e130 ["INT_ADD", "register:40f0:8", ["const:c2e130:8", "const:4:8"]]
- 00c2e130 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f124 ["INT_ADD", "register:40f0:8", ["const:c2f124:8", "const:4:8"]]
+ 00c2f124 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e130 bytes 84a70094
+ 00c2f124 bytes 7ba70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a12bd18aae0d0e61c5e02183ae5e88"></a>

### [`00c2e138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md) → [`00c2f12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f12c.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__am_pmEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c2e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c2f198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2f188",
      "incomplete_value": false,
      "site": "00c2f188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e194",
      "incomplete_value": false,
      "site": "00c2e194",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2f178",
      "incomplete_value": false,
      "site": "00c2f188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e184",
      "incomplete_value": false,
      "site": "00c2e194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00c2f160",
      "incomplete_value": false,
      "site": "00c2f164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e16c",
      "incomplete_value": false,
      "site": "00c2e170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "00c2f140",
      "READ",
      [
        "storage",
        "01128000",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f14c",
      "READ",
      [
        "storage",
        "01127ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2f14c",
      "DATA",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f140",
      "READ",
      [
        "storage",
        "01128fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f14c",
      "READ",
      [
        "storage",
        "01128fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2f14c",
      "DATA",
      [
        "storage",
        "011297e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md#insn-00c2e170) · [`00c2e194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md#insn-00c2e194) · [`00c2e198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md#insn-00c2e198)
- 新版 [`00c2f164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f12c.md#insn-00c2f164) · [`00c2f188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f12c.md#insn-00c2f188) · [`00c2f18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f12c.md#insn-00c2f18c)

~~~diff
- 00c2e170 ["INT_ADD", "register:40f0:8", ["const:c2e170:8", "const:4:8"]]
- 00c2e170 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f164 ["INT_ADD", "register:40f0:8", ["const:c2f164:8", "const:4:8"]]
+ 00c2f164 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e170 bytes 6ca70094
+ 00c2f164 bytes 63a70094
- 00c2e194 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
- 00c2e194 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2f188 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb8:8"]]
+ 00c2f188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c2e194 bytes 09fd07f9
+ 00c2f188 bytes 09dd07f9
- 00c2e198 ["INT_ADD", "register:40f0:8", ["const:c2e198:8", "const:4:8"]]
- 00c2e198 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f18c ["INT_ADD", "register:40f0:8", ["const:c2f18c:8", "const:4:8"]]
+ 00c2f18c ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e198 bytes 6aa70094
+ 00c2f18c bytes 61a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fca6708c5d07dc1d4dc5982b177662bb"></a>

### [`00c2e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md) → [`00c2f198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md) FUN_00c2f198

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c2e138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e138.md) · 呼出先 4件 [`00c36008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36008.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c2f12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f12c.md) · 呼出先 4件 [`00c36ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ffc.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.93% / 新版 71.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2f1cc",
      "incomplete_value": true,
      "site": "00c2f1cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e1d8",
      "incomplete_value": true,
      "site": "00c2e1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "definition_site": "00c2f1e4",
      "incomplete_value": false,
      "site": "00c2f1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e1f0",
      "incomplete_value": false,
      "site": "00c2e1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c2f210",
      "incomplete_value": false,
      "site": "00c2f210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e21c",
      "incomplete_value": false,
      "site": "00c2e21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "00c2f1ac",
      "READ",
      [
        "storage",
        "01128850",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f1b8",
      "READ",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f1cc",
      "WRITE",
      [
        "storage",
        "01128820",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f1ac",
      "READ",
      [
        "storage",
        "01129810",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f1b8",
      "READ",
      [
        "storage",
        "011297e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f1cc",
      "WRITE",
      [
        "storage",
        "011297e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md#insn-00c2e258) · [`00c2e274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md#insn-00c2e274) · [`00c2e280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e1a4.md#insn-00c2e280)
- 新版 [`00c2f24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md#insn-00c2f24c) · [`00c2f268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md#insn-00c2f268) · [`00c2f274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f198.md#insn-00c2f274)

~~~diff
- 00c2e258 ["INT_ADD", "register:40f0:8", ["const:c2e258:8", "const:4:8"]]
- 00c2e258 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f24c ["INT_ADD", "register:40f0:8", ["const:c2f24c:8", "const:4:8"]]
+ 00c2f24c ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e258 bytes 32a70094
+ 00c2f24c bytes 29a70094
- 00c2e274 ["INT_ADD", "register:40f0:8", ["const:c2e274:8", "const:4:8"]]
- 00c2e274 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f268 ["INT_ADD", "register:40f0:8", ["const:c2f268:8", "const:4:8"]]
+ 00c2f268 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e274 bytes 23a70094
+ 00c2f268 bytes 1aa70094
- 00c2e280 ["INT_ADD", "register:40f0:8", ["const:c2e280:8", "const:4:8"]]
- 00c2e280 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f274 ["INT_ADD", "register:40f0:8", ["const:c2f274:8", "const:4:8"]]
+ 00c2f274 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e280 bytes 30a70094
+ 00c2f274 bytes 27a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c874936e0975c14c40ba840bc8889b3a"></a>

### [`00c2e288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e288.md) → [`00c2f27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f27c.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__xEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f2b0",
      "incomplete_value": false,
      "site": "00c2f2b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e2bc",
      "incomplete_value": false,
      "site": "00c2e2c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "definition_site": "00c2f2c8",
      "incomplete_value": true,
      "site": "00c2f2d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e2d4",
      "incomplete_value": true,
      "site": "00c2e2e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
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
      "definition_site": "00c2f2c4",
      "incomplete_value": false,
      "site": "00c2f2d4",
      "value": [
        "leaf",
        "const:ca58b0:8"
      ]
    },
    "old": {
      "definition_site": "00c2e2d0",
      "incomplete_value": false,
      "site": "00c2e2e0",
      "value": [
        "leaf",
        "const:ca48e0:8"
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
      "00c2f290",
      "READ",
      [
        "storage",
        "01128008",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f29c",
      "DATA",
      [
        "storage",
        "00ca48e0",
        null,
        null
      ]
    ],
    [
      "00c2f2b0",
      "PARAM",
      [
        "storage",
        "01128008",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f290",
      "READ",
      [
        "storage",
        "01128fc8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f29c",
      "DATA",
      [
        "storage",
        "00ca58b0",
        null,
        null
      ]
    ],
    [
      "00c2f2b0",
      "PARAM",
      [
        "storage",
        "01128fc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e288.md#insn-00c2e2c0) · [`00c2e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e288.md#insn-00c2e2e0) · [`00c2e2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e288.md#insn-00c2e2ec)
- 新版 [`00c2f2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f27c.md#insn-00c2f2b4) · [`00c2f2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f27c.md#insn-00c2f2d4) · [`00c2f2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f27c.md#insn-00c2f2e0)

~~~diff
- 00c2e2c0 ["INT_ADD", "register:40f0:8", ["const:c2e2c0:8", "const:4:8"]]
- 00c2e2c0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f2b4 ["INT_ADD", "register:40f0:8", ["const:c2f2b4:8", "const:4:8"]]
+ 00c2f2b4 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e2c0 bytes 18a70094
+ 00c2f2b4 bytes 0fa70094
- 00c2e2e0 ["INT_ADD", "register:40f0:8", ["const:c2e2e0:8", "const:4:8"]]
- 00c2e2e0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f2d4 ["INT_ADD", "register:40f0:8", ["const:c2f2d4:8", "const:4:8"]]
+ 00c2f2d4 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e2e0 bytes 08a70094
+ 00c2f2d4 bytes ffa60094
- 00c2e2ec ["INT_ADD", "register:40f0:8", ["const:c2e2ec:8", "const:4:8"]]
- 00c2e2ec ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f2e0 ["INT_ADD", "register:40f0:8", ["const:c2f2e0:8", "const:4:8"]]
+ 00c2f2e0 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e2ec bytes 15a70094
+ 00c2f2e0 bytes 0ca70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936347d39775b8ae6b013adb1d902ba5"></a>

### [`00c2e2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md) → [`00c2f2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f2e8.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__xEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf3db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3db8.md) [`00c2d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f324",
      "incomplete_value": false,
      "site": "00c2f328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e330",
      "incomplete_value": false,
      "site": "00c2e334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "00c2f334",
      "incomplete_value": false,
      "site": "00c2f340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e340",
      "incomplete_value": false,
      "site": "00c2e34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00c2f33c",
      "incomplete_value": false,
      "site": "00c2f340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e348",
      "incomplete_value": false,
      "site": "00c2e34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "00c2f300",
      "READ",
      [
        "storage",
        "01128028",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f30c",
      "DATA",
      [
        "storage",
        "01128010",
        null,
        null
      ]
    ],
    [
      "00c2f324",
      "PARAM",
      [
        "storage",
        "01128028",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f300",
      "READ",
      [
        "storage",
        "01128fe8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f30c",
      "DATA",
      [
        "storage",
        "01128fd0",
        null,
        null
      ]
    ],
    [
      "00c2f324",
      "PARAM",
      [
        "storage",
        "01128fe8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md#insn-00c2e334) · [`00c2e34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md#insn-00c2e34c) · [`00c2e368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e2f4.md#insn-00c2e368)
- 新版 [`00c2f328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f2e8.md#insn-00c2f328) · [`00c2f340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f2e8.md#insn-00c2f340) · [`00c2f35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f2e8.md#insn-00c2f35c)

~~~diff
- 00c2e334 ["INT_ADD", "register:40f0:8", ["const:c2e334:8", "const:4:8"]]
- 00c2e334 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f328 ["INT_ADD", "register:40f0:8", ["const:c2f328:8", "const:4:8"]]
+ 00c2f328 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e334 bytes fba60094
+ 00c2f328 bytes f2a60094
- 00c2e34c ["INT_ADD", "register:40f0:8", ["const:c2e34c:8", "const:4:8"]]
- 00c2e34c ["CALL", null, ["callee:00c2d124:8"]]
+ 00c2f340 ["INT_ADD", "register:40f0:8", ["const:c2f340:8", "const:4:8"]]
+ 00c2f340 ["CALL", null, ["callee:00c2d124:8"]]
- 00c2e34c bytes 79f7ff97
+ 00c2f340 bytes 79f7ff97
- 00c2e368 ["INT_ADD", "register:40f0:8", ["const:c2e368:8", "const:4:8"]]
- 00c2e368 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f35c ["INT_ADD", "register:40f0:8", ["const:c2f35c:8", "const:4:8"]]
+ 00c2f35c ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e368 bytes e6a60094
+ 00c2f35c bytes dda60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5c63f9aa3f9ad29e20129408eb55a78"></a>

### [`00c2e394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e394.md) → [`00c2f388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f388.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__XEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f3bc",
      "incomplete_value": false,
      "site": "00c2f3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3c8",
      "incomplete_value": false,
      "site": "00c2e3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      "definition_site": "00c2f3d4",
      "incomplete_value": true,
      "site": "00c2f3e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e3e0",
      "incomplete_value": true,
      "site": "00c2e3ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
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
      "definition_site": "00c2f3d0",
      "incomplete_value": false,
      "site": "00c2f3e0",
      "value": [
        "leaf",
        "const:ca58c8:8"
      ]
    },
    "old": {
      "definition_site": "00c2e3dc",
      "incomplete_value": false,
      "site": "00c2e3ec",
      "value": [
        "leaf",
        "const:ca48f8:8"
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
      "00c2f39c",
      "READ",
      [
        "storage",
        "01128030",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f3a8",
      "DATA",
      [
        "storage",
        "00ca48f8",
        null,
        null
      ]
    ],
    [
      "00c2f3bc",
      "PARAM",
      [
        "storage",
        "01128030",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f39c",
      "READ",
      [
        "storage",
        "01128ff0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f3a8",
      "DATA",
      [
        "storage",
        "00ca58c8",
        null,
        null
      ]
    ],
    [
      "00c2f3bc",
      "PARAM",
      [
        "storage",
        "01128ff0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e394.md#insn-00c2e3cc) · [`00c2e3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e394.md#insn-00c2e3ec) · [`00c2e3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e394.md#insn-00c2e3f8)
- 新版 [`00c2f3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f388.md#insn-00c2f3c0) · [`00c2f3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f388.md#insn-00c2f3e0) · [`00c2f3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f388.md#insn-00c2f3ec)

~~~diff
- 00c2e3cc ["INT_ADD", "register:40f0:8", ["const:c2e3cc:8", "const:4:8"]]
- 00c2e3cc ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f3c0 ["INT_ADD", "register:40f0:8", ["const:c2f3c0:8", "const:4:8"]]
+ 00c2f3c0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e3cc bytes d5a60094
+ 00c2f3c0 bytes cca60094
- 00c2e3ec ["INT_ADD", "register:40f0:8", ["const:c2e3ec:8", "const:4:8"]]
- 00c2e3ec ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f3e0 ["INT_ADD", "register:40f0:8", ["const:c2f3e0:8", "const:4:8"]]
+ 00c2f3e0 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e3ec bytes c5a60094
+ 00c2f3e0 bytes bca60094
- 00c2e3f8 ["INT_ADD", "register:40f0:8", ["const:c2e3f8:8", "const:4:8"]]
- 00c2e3f8 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f3ec ["INT_ADD", "register:40f0:8", ["const:c2f3ec:8", "const:4:8"]]
+ 00c2f3ec ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e3f8 bytes d2a60094
+ 00c2f3ec bytes c9a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253bec4e0e07d874248863accb110f6d"></a>

### [`00c2e400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md) → [`00c2f3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f3f4.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__XEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf3db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3db8.md) [`00c2d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f430",
      "incomplete_value": false,
      "site": "00c2f434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e43c",
      "incomplete_value": false,
      "site": "00c2e440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "definition_site": "00c2f440",
      "incomplete_value": false,
      "site": "00c2f44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e44c",
      "incomplete_value": false,
      "site": "00c2e458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "definition_site": "00c2f448",
      "incomplete_value": false,
      "site": "00c2f44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e454",
      "incomplete_value": false,
      "site": "00c2e458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "00c2f40c",
      "READ",
      [
        "storage",
        "01128050",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f418",
      "DATA",
      [
        "storage",
        "01128038",
        null,
        null
      ]
    ],
    [
      "00c2f430",
      "PARAM",
      [
        "storage",
        "01128050",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f40c",
      "READ",
      [
        "storage",
        "01129010",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f418",
      "DATA",
      [
        "storage",
        "01128ff8",
        null,
        null
      ]
    ],
    [
      "00c2f430",
      "PARAM",
      [
        "storage",
        "01129010",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md#insn-00c2e440) · [`00c2e458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md#insn-00c2e458) · [`00c2e474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e400.md#insn-00c2e474)
- 新版 [`00c2f434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f3f4.md#insn-00c2f434) · [`00c2f44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f3f4.md#insn-00c2f44c) · [`00c2f468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f3f4.md#insn-00c2f468)

~~~diff
- 00c2e440 ["INT_ADD", "register:40f0:8", ["const:c2e440:8", "const:4:8"]]
- 00c2e440 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f434 ["INT_ADD", "register:40f0:8", ["const:c2f434:8", "const:4:8"]]
+ 00c2f434 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e440 bytes b8a60094
+ 00c2f434 bytes afa60094
- 00c2e458 ["INT_ADD", "register:40f0:8", ["const:c2e458:8", "const:4:8"]]
- 00c2e458 ["CALL", null, ["callee:00c2d124:8"]]
+ 00c2f44c ["INT_ADD", "register:40f0:8", ["const:c2f44c:8", "const:4:8"]]
+ 00c2f44c ["CALL", null, ["callee:00c2d124:8"]]
- 00c2e458 bytes 36f7ff97
+ 00c2f44c bytes 36f7ff97
- 00c2e474 ["INT_ADD", "register:40f0:8", ["const:c2e474:8", "const:4:8"]]
- 00c2e474 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f468 ["INT_ADD", "register:40f0:8", ["const:c2f468:8", "const:4:8"]]
+ 00c2f468 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e474 bytes a3a60094
+ 00c2f468 bytes 9aa60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-924c8ea126a63972bd73a34e599c0a58"></a>

### [`00c2e4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e4a0.md) → [`00c2f494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f494.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f4c8",
      "incomplete_value": false,
      "site": "00c2f4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e4d4",
      "incomplete_value": false,
      "site": "00c2e4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "definition_site": "00c2f4e0",
      "incomplete_value": true,
      "site": "00c2f4ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e4ec",
      "incomplete_value": true,
      "site": "00c2e4f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
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
      "definition_site": "00c2f4dc",
      "incomplete_value": false,
      "site": "00c2f4ec",
      "value": [
        "leaf",
        "const:ca58e0:8"
      ]
    },
    "old": {
      "definition_site": "00c2e4e8",
      "incomplete_value": false,
      "site": "00c2e4f8",
      "value": [
        "leaf",
        "const:ca4910:8"
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
      "00c2f4a8",
      "READ",
      [
        "storage",
        "01128058",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f4b4",
      "DATA",
      [
        "storage",
        "00ca4910",
        null,
        "string"
      ]
    ],
    [
      "00c2f4c8",
      "PARAM",
      [
        "storage",
        "01128058",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f4a8",
      "READ",
      [
        "storage",
        "01129018",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f4b4",
      "DATA",
      [
        "storage",
        "00ca58e0",
        null,
        "string"
      ]
    ],
    [
      "00c2f4c8",
      "PARAM",
      [
        "storage",
        "01129018",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e4a0.md#insn-00c2e4d8) · [`00c2e4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e4a0.md#insn-00c2e4f8) · [`00c2e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e4a0.md#insn-00c2e4ac)
- 新版 [`00c2f4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f494.md#insn-00c2f4cc) · [`00c2f4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f494.md#insn-00c2f4ec) · [`00c2f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f494.md#insn-00c2f4a0)

~~~diff
- 00c2e4d8 ["INT_ADD", "register:40f0:8", ["const:c2e4d8:8", "const:4:8"]]
- 00c2e4d8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f4cc ["INT_ADD", "register:40f0:8", ["const:c2f4cc:8", "const:4:8"]]
+ 00c2f4cc ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e4d8 bytes 92a60094
+ 00c2f4cc bytes 89a60094
- 00c2e4f8 ["INT_ADD", "register:40f0:8", ["const:c2e4f8:8", "const:4:8"]]
- 00c2e4f8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f4ec ["INT_ADD", "register:40f0:8", ["const:c2f4ec:8", "const:4:8"]]
+ 00c2f4ec ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e4f8 bytes 82a60094
+ 00c2f4ec bytes 79a60094
- 00c2e4ac ["COPY", "register:4040:8", ["const:1128000:8"]]
+ 00c2f4a0 ["COPY", "register:4040:8", ["const:1129000:8"]]
- 00c2e4ac bytes c82700d0
+ 00c2f4a0 bytes c82700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20327e9f15f3530e31e3e52b0431e1d5"></a>

### [`00c2e50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md) → [`00c2f500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f500.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__cEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf3db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3db8.md) [`00c2d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f53c",
      "incomplete_value": false,
      "site": "00c2f540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e548",
      "incomplete_value": false,
      "site": "00c2e54c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "definition_site": "00c2f54c",
      "incomplete_value": false,
      "site": "00c2f558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e558",
      "incomplete_value": false,
      "site": "00c2e564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "definition_site": "00c2f554",
      "incomplete_value": false,
      "site": "00c2f558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e560",
      "incomplete_value": false,
      "site": "00c2e564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "00c2f518",
      "READ",
      [
        "storage",
        "01128078",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f524",
      "DATA",
      [
        "storage",
        "01128060",
        null,
        null
      ]
    ],
    [
      "00c2f53c",
      "PARAM",
      [
        "storage",
        "01128078",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f518",
      "READ",
      [
        "storage",
        "01129038",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f524",
      "DATA",
      [
        "storage",
        "01129020",
        null,
        null
      ]
    ],
    [
      "00c2f53c",
      "PARAM",
      [
        "storage",
        "01129038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md#insn-00c2e54c) · [`00c2e564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md#insn-00c2e564) · [`00c2e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e50c.md#insn-00c2e580)
- 新版 [`00c2f540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f500.md#insn-00c2f540) · [`00c2f558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f500.md#insn-00c2f558) · [`00c2f574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f500.md#insn-00c2f574)

~~~diff
- 00c2e54c ["INT_ADD", "register:40f0:8", ["const:c2e54c:8", "const:4:8"]]
- 00c2e54c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f540 ["INT_ADD", "register:40f0:8", ["const:c2f540:8", "const:4:8"]]
+ 00c2f540 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e54c bytes 75a60094
+ 00c2f540 bytes 6ca60094
- 00c2e564 ["INT_ADD", "register:40f0:8", ["const:c2e564:8", "const:4:8"]]
- 00c2e564 ["CALL", null, ["callee:00c2d124:8"]]
+ 00c2f558 ["INT_ADD", "register:40f0:8", ["const:c2f558:8", "const:4:8"]]
+ 00c2f558 ["CALL", null, ["callee:00c2d124:8"]]
- 00c2e564 bytes f3f6ff97
+ 00c2f558 bytes f3f6ff97
- 00c2e580 ["INT_ADD", "register:40f0:8", ["const:c2e580:8", "const:4:8"]]
- 00c2e580 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f574 ["INT_ADD", "register:40f0:8", ["const:c2f574:8", "const:4:8"]]
+ 00c2f574 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e580 bytes 60a60094
+ 00c2f574 bytes 57a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-271acb7774ecbc5b93d4a01b0f9e5f3e"></a>

### [`00c2e5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e5ac.md) → [`00c2f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f5a0.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__rEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f5d4",
      "incomplete_value": false,
      "site": "00c2f5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e5e0",
      "incomplete_value": false,
      "site": "00c2e5e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "definition_site": "00c2f5ec",
      "incomplete_value": true,
      "site": "00c2f5f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e5f8",
      "incomplete_value": true,
      "site": "00c2e604",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:cc8:8"
              ]
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
      "definition_site": "00c2f5e8",
      "incomplete_value": false,
      "site": "00c2f5f8",
      "value": [
        "leaf",
        "const:ca58f8:8"
      ]
    },
    "old": {
      "definition_site": "00c2e5f4",
      "incomplete_value": false,
      "site": "00c2e604",
      "value": [
        "leaf",
        "const:ca4928:8"
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
      "00c2f5b4",
      "READ",
      [
        "storage",
        "01128080",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f5c0",
      "DATA",
      [
        "storage",
        "00ca4928",
        null,
        null
      ]
    ],
    [
      "00c2f5d4",
      "PARAM",
      [
        "storage",
        "01128080",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f5b4",
      "READ",
      [
        "storage",
        "01129040",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f5c0",
      "DATA",
      [
        "storage",
        "00ca58f8",
        null,
        null
      ]
    ],
    [
      "00c2f5d4",
      "PARAM",
      [
        "storage",
        "01129040",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e5ac.md#insn-00c2e5e4) · [`00c2e604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e5ac.md#insn-00c2e604) · [`00c2e610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e5ac.md#insn-00c2e610)
- 新版 [`00c2f5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f5a0.md#insn-00c2f5d8) · [`00c2f5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f5a0.md#insn-00c2f5f8) · [`00c2f604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f5a0.md#insn-00c2f604)

~~~diff
- 00c2e5e4 ["INT_ADD", "register:40f0:8", ["const:c2e5e4:8", "const:4:8"]]
- 00c2e5e4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f5d8 ["INT_ADD", "register:40f0:8", ["const:c2f5d8:8", "const:4:8"]]
+ 00c2f5d8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e5e4 bytes 4fa60094
+ 00c2f5d8 bytes 46a60094
- 00c2e604 ["INT_ADD", "register:40f0:8", ["const:c2e604:8", "const:4:8"]]
- 00c2e604 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f5f8 ["INT_ADD", "register:40f0:8", ["const:c2f5f8:8", "const:4:8"]]
+ 00c2f5f8 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e604 bytes 3fa60094
+ 00c2f5f8 bytes 36a60094
- 00c2e610 ["INT_ADD", "register:40f0:8", ["const:c2e610:8", "const:4:8"]]
- 00c2e610 ["CALL", null, ["callee:00c58f10:8"]]
+ 00c2f604 ["INT_ADD", "register:40f0:8", ["const:c2f604:8", "const:4:8"]]
+ 00c2f604 ["CALL", null, ["callee:00c58f10:8"]]
- 00c2e610 bytes 4ca60094
+ 00c2f604 bytes 43a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-539a8382ac27eb47cf858dc2a1eedb1a"></a>

### [`00c2e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md) → [`00c2f60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f60c.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__rEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bf2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2dc4.md) [`00c2c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c130.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bf3db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3db8.md) [`00c2d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d124.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f648",
      "incomplete_value": false,
      "site": "00c2f64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e654",
      "incomplete_value": false,
      "site": "00c2e658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00c2f658",
      "incomplete_value": false,
      "site": "00c2f664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e664",
      "incomplete_value": false,
      "site": "00c2e670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "definition_site": "00c2f660",
      "incomplete_value": false,
      "site": "00c2f664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e66c",
      "incomplete_value": false,
      "site": "00c2e670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:310000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00c2f624",
      "READ",
      [
        "storage",
        "011280a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f630",
      "DATA",
      [
        "storage",
        "01128088",
        null,
        null
      ]
    ],
    [
      "00c2f648",
      "PARAM",
      [
        "storage",
        "011280a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c2f624",
      "READ",
      [
        "storage",
        "01129060",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2f630",
      "DATA",
      [
        "storage",
        "01129048",
        null,
        null
      ]
    ],
    [
      "00c2f648",
      "PARAM",
      [
        "storage",
        "01129060",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md#insn-00c2e658) · [`00c2e670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md#insn-00c2e670) · [`00c2e68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e618.md#insn-00c2e68c)
- 新版 [`00c2f64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f60c.md#insn-00c2f64c) · [`00c2f664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f60c.md#insn-00c2f664) · [`00c2f680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f60c.md#insn-00c2f680)

~~~diff
- 00c2e658 ["INT_ADD", "register:40f0:8", ["const:c2e658:8", "const:4:8"]]
- 00c2e658 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c2f64c ["INT_ADD", "register:40f0:8", ["const:c2f64c:8", "const:4:8"]]
+ 00c2f64c ["CALL", null, ["callee:00c58ef0:8"]]
- 00c2e658 bytes 32a60094
+ 00c2f64c bytes 29a60094
- 00c2e670 ["INT_ADD", "register:40f0:8", ["const:c2e670:8", "const:4:8"]]
- 00c2e670 ["CALL", null, ["callee:00c2d124:8"]]
+ 00c2f664 ["INT_ADD", "register:40f0:8", ["const:c2f664:8", "const:4:8"]]
+ 00c2f664 ["CALL", null, ["callee:00c2d124:8"]]
- 00c2e670 bytes b0f6ff97
+ 00c2f664 bytes b0f6ff97
- 00c2e68c ["INT_ADD", "register:40f0:8", ["const:c2e68c:8", "const:4:8"]]
- 00c2e68c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00c2f680 ["INT_ADD", "register:40f0:8", ["const:c2f680:8", "const:4:8"]]
+ 00c2f680 ["CALL", null, ["callee:00c58ed0:8"]]
- 00c2e68c bytes 1da60094
+ 00c2f680 bytes 14a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f3e6f4e9f19da41622cc3af4c77a31"></a>

### [`00c2e6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e6b8.md) → [`00c2f6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f6ac.md) _ZNSt6__ndk110__time_getC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed70.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5fd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd40.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2f700",
      "incomplete_value": false,
      "site": "00c2f710",
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
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e70c",
      "incomplete_value": false,
      "site": "00c2e71c",
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
            "const:12:8"
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
      "00c2f700",
      "PARAM",
      [
        "storage",
        "002b7012",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2f700",
      "PARAM",
      [
        "storage",
        "002b70e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e6b8.md#insn-00c2e71c) · [`00c2e6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e6b8.md#insn-00c2e6dc) · [`00c2e704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e6b8.md#insn-00c2e704)
- 新版 [`00c2f710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f6ac.md#insn-00c2f710) · [`00c2f6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f6ac.md#insn-00c2f6d0) · [`00c2f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f6ac.md#insn-00c2f6f8)

~~~diff
- 00c2e71c ["INT_ADD", "register:40f0:8", ["const:c2e71c:8", "const:4:8"]]
- 00c2e71c ["CALL", null, ["callee:00c269c4:8"]]
+ 00c2f710 ["INT_ADD", "register:40f0:8", ["const:c2f710:8", "const:4:8"]]
+ 00c2f710 ["CALL", null, ["callee:00c269c4:8"]]
- 00c2e71c bytes addcff97
+ 00c2f710 bytes addcff97
- 00c2e6dc ["INT_ADD", "register:40f0:8", ["const:c2e6dc:8", "const:4:8"]]
- 00c2e6dc ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c2f6d0 ["INT_ADD", "register:40f0:8", ["const:c2f6d0:8", "const:4:8"]]
+ 00c2f6d0 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c2e6dc bytes 05bb0094
+ 00c2f6d0 bytes fcba0094
- 00c2e704 ["INT_ADD", "register:40f0:8", ["const:c2e704:8", "const:4:8"]]
- 00c2e704 ["CALL", null, ["callee:0043e138:8"]]
+ 00c2f6f8 ["INT_ADD", "register:40f0:8", ["const:c2f6f8:8", "const:4:8"]]
+ 00c2f6f8 ["CALL", null, ["callee:0043e138:8"]]
- 00c2e704 bytes c53de097
+ 00c2f6f8 bytes 903ae097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6672aa2f6cdf0051b4773efbd8f3917b"></a>

### [`00c2e780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e780.md) → [`00c2f774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f774.md) _ZNSt6__ndk110__time_getC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed80.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)
- 新版 呼出元 1件 [`00c5fd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd50.md) · 呼出先 5件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md)

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
      "definition_site": "00c2f7cc",
      "incomplete_value": false,
      "site": "00c2f7dc",
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
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e7d8",
      "incomplete_value": false,
      "site": "00c2e7e8",
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
            "const:12:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2f7cc",
      "PARAM",
      [
        "storage",
        "002b7012",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2f7cc",
      "PARAM",
      [
        "storage",
        "002b70e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e780.md#insn-00c2e7e8) · [`00c2e7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e780.md#insn-00c2e7b4) · [`00c2e7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e780.md#insn-00c2e7d8)
- 新版 [`00c2f7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f774.md#insn-00c2f7dc) · [`00c2f7a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f774.md#insn-00c2f7a8) · [`00c2f7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f774.md#insn-00c2f7cc)

~~~diff
- 00c2e7e8 ["INT_ADD", "register:40f0:8", ["const:c2e7e8:8", "const:4:8"]]
- 00c2e7e8 ["CALL", null, ["callee:00c59150:8"]]
+ 00c2f7dc ["INT_ADD", "register:40f0:8", ["const:c2f7dc:8", "const:4:8"]]
+ 00c2f7dc ["CALL", null, ["callee:00c59150:8"]]
- 00c2e7e8 bytes 66a60094
+ 00c2f7dc bytes 5da60094
- 00c2e7b4 ["INT_ADD", "register:40f0:8", ["const:c2e7b4:8", "const:4:8"]]
- 00c2e7b4 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c2f7a8 ["INT_ADD", "register:40f0:8", ["const:c2f7a8:8", "const:4:8"]]
+ 00c2f7a8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c2e7b4 bytes cfba0094
+ 00c2f7a8 bytes c6ba0094
- 00c2e7d8 ["COPY", "tmp:0:8", ["const:12:8"]]
- 00c2e7d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c2e7d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c2e7d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c2f7cc ["COPY", "tmp:0:8", ["const:e1:8"]]
+ 00c2f7cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c2f7cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c2f7cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c2e7d8 bytes 00480091
+ 00c2f7cc bytes 00840391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc5fb53667d1f565c4ddf873529d235a"></a>

### [`00c2e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md) → [`00c2f834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f834.md) _ZNSt6__ndk118__time_get_storageIcE9__analyzeEcRKNS_5ctypeIcEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5eda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eda0.md) · 呼出先 3件 [`00c2ee28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2ee28.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md) [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md)
- 新版 呼出元 1件 [`00c5fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd70.md) · 呼出先 3件 [`00c2fe1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2fe1c.md) [`00c596a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596a0.md) [`00c5f700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f700.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2f864",
      "incomplete_value": true,
      "site": "00c2f87c",
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e870",
      "incomplete_value": true,
      "site": "00c2e888",
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
                "const:710:8"
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
      "definition_site": "00c2f880",
      "incomplete_value": true,
      "site": "00c2f894",
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2e88c",
      "incomplete_value": true,
      "site": "00c2e8a0",
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
                "const:c20:8"
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
      "00c2f864",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ],
    [
      "00c2f880",
      "READ",
      [
        "storage",
        "002c2c20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2f864",
      "READ",
      [
        "storage",
        "002c2760",
        null,
        null
      ]
    ],
    [
      "00c2f880",
      "READ",
      [
        "storage",
        "002c2c70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2e870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md#insn-00c2e870) · [`00c2e88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md#insn-00c2e88c) · [`00c2e8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2e/00c2e840.md#insn-00c2e8c8)
- 新版 [`00c2f864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f834.md#insn-00c2f864) · [`00c2f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f834.md#insn-00c2f880) · [`00c2f8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2f/00c2f834.md#insn-00c2f8bc)

~~~diff
- 00c2e870 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:710:8"]]
- 00c2e870 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e870 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e870 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2f864 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:760:8"]]
+ 00c2f864 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2f864 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2f864 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e870 bytes 20c5c13d
+ 00c2f864 bytes 20d9c13d
- 00c2e88c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
- 00c2e88c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2e88c ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2e88c ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c2f880 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c70:8"]]
+ 00c2f880 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c2f880 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c2f880 ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2e88c bytes 2009c33d
+ 00c2f880 bytes 201dc33d
- 00c2e8c8 ["INT_ADD", "register:40f0:8", ["const:c2e8c8:8", "const:4:8"]]
- 00c2e8c8 ["CALL", null, ["callee:00c5f700:8"]]
+ 00c2f8bc ["INT_ADD", "register:40f0:8", ["const:c2f8bc:8", "const:4:8"]]
+ 00c2f8bc ["CALL", null, ["callee:00c5f700:8"]]
- 00c2e8c8 bytes 9abf0094
+ 00c2f8bc bytes 91bf0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e909e399e0b710b80424a41140437d3"></a>

### [`00c2f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md) → [`00c3012c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c30/00c3012c.md) _ZNSt6__ndk118__time_get_storageIwE9__analyzeEcRKNS_5ctypeIwEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5edb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edb0.md) · 呼出先 8件 [`00c307e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c307e0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)
- 新版 呼出元 1件 [`00c5fd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd80.md) · 呼出先 8件 [`00c317d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c317d4.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.65% / 新版 99.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3015c",
      "incomplete_value": true,
      "site": "00c301a4",
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2f168",
      "incomplete_value": true,
      "site": "00c2f1b0",
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
                "const:710:8"
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
      "definition_site": "00c30168",
      "incomplete_value": true,
      "site": "00c301a4",
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2f174",
      "incomplete_value": true,
      "site": "00c2f1b0",
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
                "const:c20:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c31780",
      "incomplete_value": false,
      "site": "00c31784",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3078c",
      "incomplete_value": false,
      "site": "00c30790",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3015c",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ],
    [
      "00c30168",
      "READ",
      [
        "storage",
        "002c2c20",
        null,
        null
      ]
    ],
    [
      "00c31780",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3015c",
      "READ",
      [
        "storage",
        "002c2760",
        null,
        null
      ]
    ],
    [
      "00c30168",
      "READ",
      [
        "storage",
        "002c2c70",
        null,
        null
      ]
    ],
    [
      "00c31780",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md#insn-00c30790) · [`00c2f168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md#insn-00c2f168) · [`00c2f16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2f/00c2f138.md#insn-00c2f16c)
- 新版 [`00c31784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c30/00c3012c.md#insn-00c31784) · [`00c3015c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c30/00c3012c.md#insn-00c3015c)

~~~diff
- 00c30790 ["INT_ADD", "register:40f0:8", ["const:c30790:8", "const:4:8"]]
- 00c30790 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c31784 ["INT_ADD", "register:40f0:8", ["const:c31784:8", "const:4:8"]]
+ 00c31784 ["CALL", null, ["callee:00c5f050:8"]]
- 00c30790 bytes 3cb60094
+ 00c31784 bytes 33b60094
- 00c2f168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:710:8"]]
- 00c2f168 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00c2f168 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c2f168 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00c3015c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:760:8"]]
+ 00c3015c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00c3015c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c3015c ["COPY", "register:5018:8", ["const:0:8"]]
- 00c2f168 bytes 00c5c13d
+ 00c3015c bytes 00d9c13d
- 00c2f16c ["COPY", "register:4040:8", ["const:2c2000:8"]]
- 00c2f16c bytes 88b4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-381d96cc0be61f7238886b012472dd96"></a>

### [`00c30d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30d84.md) → [`00c31d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31d78.md) _ZNSt6__ndk118__time_get_storageIwE4initERKNS_5ctypeIwEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5edd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edd0.md) · 呼出先 8件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md) [`00c5e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e640.md)
- 新版 呼出元 1件 [`00c5fda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fda0.md) · 呼出先 8件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md) [`00c5f610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c31e00",
      "incomplete_value": false,
      "site": "00c31e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:87c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30e0c",
      "incomplete_value": false,
      "site": "00c30e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c31f60",
      "incomplete_value": false,
      "site": "00c31f64",
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
            "const:58e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c30f6c",
      "incomplete_value": false,
      "site": "00c30f70",
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
            "const:4c1:8"
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
      "definition_site": "00c32248",
      "incomplete_value": false,
      "site": "00c3224c",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31254",
      "incomplete_value": false,
      "site": "00c31258",
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
            "const:dcd:8"
          ]
        ]
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
      "00c31e00",
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        null
      ]
    ],
    [
      "00c31f60",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ],
    [
      "00c320e8",
      "PARAM",
      [
        "storage",
        "002af6eb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c31e00",
      "PARAM",
      [
        "storage",
        "002b287c",
        null,
        null
      ]
    ],
    [
      "00c31f60",
      "PARAM",
      [
        "storage",
        "002ac58e",
        null,
        null
      ]
    ],
    [
      "00c320e8",
      "PARAM",
      [
        "storage",
        "002af7c2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30d84.md#insn-00c30e14) · [`00c30f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30d84.md#insn-00c30f70) · [`00c31258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30d84.md#insn-00c31258)
- 新版 [`00c31e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31d78.md#insn-00c31e08) · [`00c31f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31d78.md#insn-00c31f64) · [`00c3224c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31d78.md#insn-00c3224c)

~~~diff
- 00c30e14 ["INT_ADD", "register:40f0:8", ["const:c30e14:8", "const:4:8"]]
- 00c30e14 ["CALL", null, ["callee:00c5f700:8"]]
+ 00c31e08 ["INT_ADD", "register:40f0:8", ["const:c31e08:8", "const:4:8"]]
+ 00c31e08 ["CALL", null, ["callee:00c5f700:8"]]
- 00c30e14 bytes 47b60094
+ 00c31e08 bytes 3eb60094
- 00c30f70 ["INT_ADD", "register:40f0:8", ["const:c30f70:8", "const:4:8"]]
- 00c30f70 ["CALL", null, ["callee:00c5f700:8"]]
+ 00c31f64 ["INT_ADD", "register:40f0:8", ["const:c31f64:8", "const:4:8"]]
+ 00c31f64 ["CALL", null, ["callee:00c5f700:8"]]
- 00c30f70 bytes f0b50094
+ 00c31f64 bytes e7b50094
- 00c31258 ["INT_ADD", "register:40f0:8", ["const:c31258:8", "const:4:8"]]
- 00c31258 ["CALL", null, ["callee:00c5f700:8"]]
+ 00c3224c ["INT_ADD", "register:40f0:8", ["const:c3224c:8", "const:4:8"]]
+ 00c3224c ["CALL", null, ["callee:00c5f700:8"]]
- 00c31258 bytes 36b50094
+ 00c3224c bytes 2db50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a166e000bc5f24ff7927d7c482df01"></a>

### [`00c317fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c317fc.md) → [`00c327f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c327f0.md) _ZNSt6__ndk118__time_get_storageIcEC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ea90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5fa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c32838",
      "incomplete_value": false,
      "site": "00c3283c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c96000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31844",
      "incomplete_value": false,
      "site": "00c31848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "00c32858",
      "incomplete_value": true,
      "site": "00c3285c",
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
      "definition_site": "00c31864",
      "incomplete_value": true,
      "site": "00c31868",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c32870",
      "incomplete_value": true,
      "site": "00c32874",
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
      "definition_site": "00c3187c",
      "incomplete_value": true,
      "site": "00c31880",
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
      "00c3283c",
      "DATA",
      [
        "storage",
        "00c95d70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32850",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c3285c",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c3283c",
      "DATA",
      [
        "storage",
        "00c96d40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32850",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c3285c",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3181c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c317fc.md#insn-00c3181c) · [`00c3182c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c317fc.md#insn-00c3182c) · [`00c3183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c317fc.md#insn-00c3183c)
- 新版 [`00c32810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c327f0.md#insn-00c32810) · [`00c32820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c327f0.md#insn-00c32820) · [`00c32830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c327f0.md#insn-00c32830)

~~~diff
- 00c3181c ["INT_ADD", "register:40f0:8", ["const:c3181c:8", "const:4:8"]]
- 00c3181c ["CALL", null, ["callee:00c5fd40:8"]]
+ 00c32810 ["INT_ADD", "register:40f0:8", ["const:c32810:8", "const:4:8"]]
+ 00c32810 ["CALL", null, ["callee:00c5fd40:8"]]
- 00c3181c bytes 55b50094
+ 00c32810 bytes 4cb50094
- 00c3182c ["INT_ADD", "register:40f0:8", ["const:c3182c:8", "const:4:8"]]
- 00c3182c ["CALL", null, ["callee:00c59130:8"]]
+ 00c32820 ["INT_ADD", "register:40f0:8", ["const:c32820:8", "const:4:8"]]
+ 00c32820 ["CALL", null, ["callee:00c59130:8"]]
- 00c3182c bytes 4d9a0094
+ 00c32820 bytes 449a0094
- 00c3183c ["INT_ADD", "register:40f0:8", ["const:c3183c:8", "const:4:8"]]
- 00c3183c ["CALL", null, ["callee:00c5fa60:8"]]
+ 00c32830 ["INT_ADD", "register:40f0:8", ["const:c32830:8", "const:4:8"]]
+ 00c32830 ["CALL", null, ["callee:00c5fa60:8"]]
- 00c3183c bytes 95b40094
+ 00c32830 bytes 8cb40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a7de3b9f39563808ba16c7e3400c4f"></a>

### [`00c31adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31adc.md) → [`00c32ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32ad0.md) _ZNSt6__ndk112ctype_bynameIcED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5eab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eab0.md) [`00c5ede0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ede0.md) · 呼出先 3件 [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 2件 [`00c5fa80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa80.md) [`00c5fdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdb0.md) · 呼出先 3件 [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "definition_site": "00c32af0",
      "incomplete_value": true,
      "site": "00c32af4",
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
      "definition_site": "00c31afc",
      "incomplete_value": true,
      "site": "00c31b00",
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
      "definition_site": "00c32b08",
      "incomplete_value": true,
      "site": "00c32b0c",
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
      "definition_site": "00c31b14",
      "incomplete_value": true,
      "site": "00c31b18",
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
      "00c32ae8",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c32af4",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c32b00",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c32ae8",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c32af4",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c32b00",
      "READ",
      [
        "storage",
        "00c9ce68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31adc.md#insn-00c31aec) · [`00c31af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31adc.md#insn-00c31af4) · [`00c31b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31adc.md#insn-00c31b04)
- 新版 [`00c32ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32ad0.md#insn-00c32ae0) · [`00c32ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32ad0.md#insn-00c32ae8) · [`00c32af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32ad0.md#insn-00c32af8)

~~~diff
- 00c31aec ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c32ae0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c31aec bytes 480300d0
+ 00c32ae0 bytes 480300d0
- 00c31af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00c31af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c32ae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00c32ae8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c31af4 bytes 085147f9
+ 00c32ae8 bytes 083947f9
- 00c31b04 ["INT_ADD", "register:40f0:8", ["const:c31b04:8", "const:4:8"]]
- 00c31b04 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c32af8 ["INT_ADD", "register:40f0:8", ["const:c32af8:8", "const:4:8"]]
+ 00c32af8 ["CALL", null, ["callee:00c5e270:8"]]
- 00c31b04 bytes e7ad0094
+ 00c32af8 bytes dead0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7740e37b76bc533264e57ccdbb5d4777"></a>

### [`00c31b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31b44.md) → [`00c32b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32b38.md) _ZNSt6__ndk118__time_get_storageIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e960.md) · 呼出先 7件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5eaa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eaa0.md)
- 新版 呼出元 1件 [`00c5f930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f930.md) · 呼出先 7件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5fa70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c32b80",
      "incomplete_value": false,
      "site": "00c32b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c96000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31b8c",
      "incomplete_value": false,
      "site": "00c31b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "00c32ba0",
      "incomplete_value": true,
      "site": "00c32ba4",
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
      "definition_site": "00c31bac",
      "incomplete_value": true,
      "site": "00c31bb0",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c32bb8",
      "incomplete_value": true,
      "site": "00c32bbc",
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
      "definition_site": "00c31bc4",
      "incomplete_value": true,
      "site": "00c31bc8",
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
      "00c32b84",
      "DATA",
      [
        "storage",
        "00c95d70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32b98",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c32ba4",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00c32b84",
      "DATA",
      [
        "storage",
        "00c96d40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32b98",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c32ba4",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31b44.md#insn-00c31b64) · [`00c31b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31b44.md#insn-00c31b74) · [`00c31b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31b44.md#insn-00c31b84)
- 新版 [`00c32b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32b38.md#insn-00c32b58) · [`00c32b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32b38.md#insn-00c32b68) · [`00c32b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32b38.md#insn-00c32b78)

~~~diff
- 00c31b64 ["INT_ADD", "register:40f0:8", ["const:c31b64:8", "const:4:8"]]
- 00c31b64 ["CALL", null, ["callee:00c5fd50:8"]]
+ 00c32b58 ["INT_ADD", "register:40f0:8", ["const:c32b58:8", "const:4:8"]]
+ 00c32b58 ["CALL", null, ["callee:00c5fd50:8"]]
- 00c31b64 bytes 87b40094
+ 00c32b58 bytes 7eb40094
- 00c31b74 ["INT_ADD", "register:40f0:8", ["const:c31b74:8", "const:4:8"]]
- 00c31b74 ["CALL", null, ["callee:00c59130:8"]]
+ 00c32b68 ["INT_ADD", "register:40f0:8", ["const:c32b68:8", "const:4:8"]]
+ 00c32b68 ["CALL", null, ["callee:00c59130:8"]]
- 00c31b74 bytes 7b990094
+ 00c32b68 bytes 72990094
- 00c31b84 ["INT_ADD", "register:40f0:8", ["const:c31b84:8", "const:4:8"]]
- 00c31b84 ["CALL", null, ["callee:00c5fa70:8"]]
+ 00c32b78 ["INT_ADD", "register:40f0:8", ["const:c32b78:8", "const:4:8"]]
+ 00c32b78 ["CALL", null, ["callee:00c5fa70:8"]]
- 00c31b84 bytes c7b30094
+ 00c32b78 bytes beb30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0301b58ace8dcaee48462132709758e6"></a>

### [`00c31e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31e24.md) → [`00c32e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32e18.md) _ZNSt6__ndk118__time_get_storageIwEC1EPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5eac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eac0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md) [`00c5ed70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5fa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fa90.md) [`00c5faa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5faa0.md) [`00c5fd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c32e60",
      "incomplete_value": false,
      "site": "00c32e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c96000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c31e6c",
      "incomplete_value": false,
      "site": "00c31e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "definition_site": "00c32e80",
      "incomplete_value": true,
      "site": "00c32e84",
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
      "definition_site": "00c31e8c",
      "incomplete_value": true,
      "site": "00c31e90",
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
      "00c32e64",
      "DATA",
      [
        "storage",
        "00c95df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32e78",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c32e84",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c32e64",
      "DATA",
      [
        "storage",
        "00c96dc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c32e78",
      "READ",
      [
        "storage",
        "00c9ce78",
        null,
        "pointer"
      ]
    ],
    [
      "00c32e84",
      "DATA",
      [
        "storage",
        "00c948d8",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c31e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31e24.md#insn-00c31e44) · [`00c31e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31e24.md#insn-00c31e54) · [`00c31e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c31/00c31e24.md#insn-00c31e64)
- 新版 [`00c32e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32e18.md#insn-00c32e38) · [`00c32e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32e18.md#insn-00c32e48) · [`00c32e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c32/00c32e18.md#insn-00c32e58)

~~~diff
- 00c31e44 ["INT_ADD", "register:40f0:8", ["const:c31e44:8", "const:4:8"]]
- 00c31e44 ["CALL", null, ["callee:00c5fd40:8"]]
+ 00c32e38 ["INT_ADD", "register:40f0:8", ["const:c32e38:8", "const:4:8"]]
+ 00c32e38 ["CALL", null, ["callee:00c5fd40:8"]]
- 00c31e44 bytes cbb30094
+ 00c32e38 bytes c2b30094
- 00c31e54 ["INT_ADD", "register:40f0:8", ["const:c31e54:8", "const:4:8"]]
- 00c31e54 ["CALL", null, ["callee:00c59130:8"]]
+ 00c32e48 ["INT_ADD", "register:40f0:8", ["const:c32e48:8", "const:4:8"]]
+ 00c32e48 ["CALL", null, ["callee:00c59130:8"]]
- 00c31e54 bytes c3980094
+ 00c32e48 bytes ba980094
- 00c31e64 ["INT_ADD", "register:40f0:8", ["const:c31e64:8", "const:4:8"]]
- 00c31e64 ["CALL", null, ["callee:00c5fa90:8"]]
+ 00c32e58 ["INT_ADD", "register:40f0:8", ["const:c32e58:8", "const:4:8"]]
+ 00c32e58 ["CALL", null, ["callee:00c5fa90:8"]]
- 00c31e64 bytes 17b30094
+ 00c32e58 bytes 0eb30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e3016775904be0983a0f4197389a63e"></a>

### [`00c32124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32124.md) → [`00c33118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33118.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e970.md) · 呼出先 6件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md) [`00c5eae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eae0.md) [`00c5ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ed80.md)
- 新版 呼出元 1件 [`00c5f940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f940.md) · 呼出先 6件 [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5faa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5faa0.md) [`00c5fab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fab0.md) [`00c5fd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c33160",
      "incomplete_value": false,
      "site": "00c33164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c96000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3216c",
      "incomplete_value": false,
      "site": "00c32170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c95000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "definition_site": "00c33180",
      "incomplete_value": true,
      "site": "00c33184",
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
      "definition_site": "00c3218c",
      "incomplete_value": true,
      "site": "00c32190",
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
      "00c33164",
      "DATA",
      [
        "storage",
        "00c95df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c33178",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c33184",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c33164",
      "DATA",
      [
        "storage",
        "00c96dc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c33178",
      "READ",
      [
        "storage",
        "00c9ce78",
        null,
        "pointer"
      ]
    ],
    [
      "00c33184",
      "DATA",
      [
        "storage",
        "00c948d8",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32124.md#insn-00c32144) · [`00c32154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32124.md#insn-00c32154) · [`00c32164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32124.md#insn-00c32164)
- 新版 [`00c33138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33118.md#insn-00c33138) · [`00c33148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33118.md#insn-00c33148) · [`00c33158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33118.md#insn-00c33158)

~~~diff
- 00c32144 ["INT_ADD", "register:40f0:8", ["const:c32144:8", "const:4:8"]]
- 00c32144 ["CALL", null, ["callee:00c5fd50:8"]]
+ 00c33138 ["INT_ADD", "register:40f0:8", ["const:c33138:8", "const:4:8"]]
+ 00c33138 ["CALL", null, ["callee:00c5fd50:8"]]
- 00c32144 bytes 0fb30094
+ 00c33138 bytes 06b30094
- 00c32154 ["INT_ADD", "register:40f0:8", ["const:c32154:8", "const:4:8"]]
- 00c32154 ["CALL", null, ["callee:00c59130:8"]]
+ 00c33148 ["INT_ADD", "register:40f0:8", ["const:c33148:8", "const:4:8"]]
+ 00c33148 ["CALL", null, ["callee:00c59130:8"]]
- 00c32154 bytes 03980094
+ 00c33148 bytes fa970094
- 00c32164 ["INT_ADD", "register:40f0:8", ["const:c32164:8", "const:4:8"]]
- 00c32164 ["CALL", null, ["callee:00c5fab0:8"]]
+ 00c33158 ["INT_ADD", "register:40f0:8", ["const:c33158:8", "const:4:8"]]
+ 00c33158 ["CALL", null, ["callee:00c5fab0:8"]]
- 00c32164 bytes 5fb20094
+ 00c33158 bytes 56b20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6193c532372a6e10a9a286cdbd27af"></a>

### [`00c329d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c329d8.md) → [`00c339cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c339cc.md) _ZNSt6__ndk110__time_putC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e980.md) · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e080.md)
- 新版 呼出元 1件 [`00c5f950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f950.md) · 呼出先 5件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5f050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f050.md)

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
      "definition_site": "00c33a24",
      "incomplete_value": false,
      "site": "00c33a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:87f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32a30",
      "incomplete_value": false,
      "site": "00c32a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:835:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c33a24",
      "PARAM",
      [
        "storage",
        "002b2835",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c33a24",
      "PARAM",
      [
        "storage",
        "002b287f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c329d8.md#insn-00c32a40) · [`00c32a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c329d8.md#insn-00c32a0c) · [`00c32a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c329d8.md#insn-00c32a30)
- 新版 [`00c33a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c339cc.md#insn-00c33a34) · [`00c33a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c339cc.md#insn-00c33a00) · [`00c33a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c339cc.md#insn-00c33a24)

~~~diff
- 00c32a40 ["INT_ADD", "register:40f0:8", ["const:c32a40:8", "const:4:8"]]
- 00c32a40 ["CALL", null, ["callee:00c59150:8"]]
+ 00c33a34 ["INT_ADD", "register:40f0:8", ["const:c33a34:8", "const:4:8"]]
+ 00c33a34 ["CALL", null, ["callee:00c59150:8"]]
- 00c32a40 bytes d0950094
+ 00c33a34 bytes c7950094
- 00c32a0c ["INT_ADD", "register:40f0:8", ["const:c32a0c:8", "const:4:8"]]
- 00c32a0c ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c33a00 ["INT_ADD", "register:40f0:8", ["const:c33a00:8", "const:4:8"]]
+ 00c33a00 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c32a0c bytes 39aa0094
+ 00c33a00 bytes 30aa0094
- 00c32a30 ["COPY", "tmp:0:8", ["const:835:8"]]
- 00c32a30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c32a30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c32a30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c33a24 ["COPY", "tmp:0:8", ["const:87f:8"]]
+ 00c33a24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c33a24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c33a24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c32a30 bytes 00d42091
+ 00c33a24 bytes 00fc2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9899192d33bb381e8b769b572b2585b7"></a>

### [`00c32a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32a74.md) → [`00c33a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33a68.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ee20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee20.md) · 呼出先 4件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fdf0.md) · 呼出先 4件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c33ae4",
      "incomplete_value": true,
      "site": "00c33ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32af0",
      "incomplete_value": true,
      "site": "00c32af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c33a9c",
      "incomplete_value": true,
      "site": "00c33aa0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00c32aa8",
      "incomplete_value": true,
      "site": "00c32aac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33ac4",
      "incomplete_value": false,
      "site": "00c33ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32ad0",
      "incomplete_value": false,
      "site": "00c32ad4",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c33a88",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c33a98",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c33ac4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c33a88",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c33a98",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c33ac4",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32a74.md#insn-00c32ad4) · [`00c32aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32a74.md#insn-00c32aec) · [`00c32af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32a74.md#insn-00c32af0)
- 新版 [`00c33ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33a68.md#insn-00c33ac8) · [`00c33ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33a68.md#insn-00c33ae0) · [`00c33ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33a68.md#insn-00c33ae4)

~~~diff
- 00c32ad4 ["INT_ADD", "register:40f0:8", ["const:c32ad4:8", "const:4:8"]]
- 00c32ad4 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c33ac8 ["INT_ADD", "register:40f0:8", ["const:c33ac8:8", "const:4:8"]]
+ 00c33ac8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c32ad4 bytes 13950094
+ 00c33ac8 bytes 0a950094
- 00c32aec ["INT_ADD", "register:40f0:8", ["const:c32aec:8", "const:4:8"]]
- 00c32aec ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c33ae0 ["INT_ADD", "register:40f0:8", ["const:c33ae0:8", "const:4:8"]]
+ 00c33ae0 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c32aec bytes 01aa0094
+ 00c33ae0 bytes f8a90094
- 00c32af0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
- 00c32af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c33ae4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d58:8"]]
+ 00c33ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c32af0 bytes a0ce06f9
+ 00c33ae4 bytes a0ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134c06af03c21519ee785e912b16be80"></a>

### [`00c32b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md) → [`00c33b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33b14.md) _ZNSt6__ndk117moneypunct_bynameIcLb0EE4initEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9a0.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md)
- 新版 呼出元 1件 [`00c5f970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f970.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c33e3c",
      "incomplete_value": false,
      "site": "00c33e4c",
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
            "const:874:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c32e48",
      "incomplete_value": false,
      "site": "00c32e58",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c33e3c",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c33e3c",
      "PARAM",
      [
        "storage",
        "002b1874",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c32e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md#insn-00c32e58) · [`00c32b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md#insn-00c32b4c) · [`00c32b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md#insn-00c32b5c)
- 新版 [`00c33e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33b14.md#insn-00c33e4c) · [`00c33b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33b14.md#insn-00c33b40) · [`00c33b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33b14.md#insn-00c33b50)

~~~diff
- 00c32e58 ["INT_ADD", "register:40f0:8", ["const:c32e58:8", "const:4:8"]]
- 00c32e58 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c33e4c ["INT_ADD", "register:40f0:8", ["const:c33e4c:8", "const:4:8"]]
+ 00c33e4c ["CALL", null, ["callee:00c269c4:8"]]
- 00c32e58 bytes decaff97
+ 00c33e4c bytes decaff97
- 00c32b4c ["INT_ADD", "register:40f0:8", ["const:c32b4c:8", "const:4:8"]]
- 00c32b4c ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c33b40 ["INT_ADD", "register:40f0:8", ["const:c33b40:8", "const:4:8"]]
+ 00c33b40 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c32b4c bytes e9a90094
+ 00c33b40 bytes e0a90094
- 00c32b5c ["INT_ADD", "register:40f0:8", ["const:c32b5c:8", "const:4:8"]]
- 00c32b5c ["CALL", null, ["callee:00c5f610:8"]]
+ 00c33b50 ["INT_ADD", "register:40f0:8", ["const:c33b50:8", "const:4:8"]]
+ 00c33b50 ["CALL", null, ["callee:00c5f610:8"]]
- 00c32b5c bytes b9ae0094
+ 00c33b50 bytes b0ae0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa53bbf0e136bd43ea01c86436dcc87"></a>

### [`00c3381c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md) → [`00c34810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34810.md) _ZNSt6__ndk117moneypunct_bynameIwLb0EE4initEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9c0.md) · 呼出先 17件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md)
- 新版 呼出元 1件 [`00c5f990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f990.md) · 呼出先 17件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`006d7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c2d628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d628.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34ec8",
      "incomplete_value": false,
      "site": "00c34ecc",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33ed4",
      "incomplete_value": false,
      "site": "00c33ed8",
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
            "const:d98:8"
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
      "definition_site": "00c34ee0",
      "incomplete_value": true,
      "site": "00c34ef0",
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
            "const:874:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33eec",
      "incomplete_value": true,
      "site": "00c33efc",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c34f0c",
      "incomplete_value": false,
      "site": "00c34f10",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c33f18",
      "incomplete_value": false,
      "site": "00c33f1c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c34ec8",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ],
    [
      "00c34ee0",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ],
    [
      "00c34f0c",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c34ec8",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ],
    [
      "00c34ee0",
      "PARAM",
      [
        "storage",
        "002b1874",
        null,
        "string"
      ]
    ],
    [
      "00c34f0c",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c33ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md#insn-00c33ed8) · [`00c33efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md#insn-00c33efc) · [`00c33f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c33/00c3381c.md#insn-00c33f1c)
- 新版 [`00c34ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34810.md#insn-00c34ecc) · [`00c34ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34810.md#insn-00c34ef0) · [`00c34f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c34/00c34810.md#insn-00c34f10)

~~~diff
- 00c33ed8 ["INT_ADD", "register:40f0:8", ["const:c33ed8:8", "const:4:8"]]
- 00c33ed8 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c34ecc ["INT_ADD", "register:40f0:8", ["const:c34ecc:8", "const:4:8"]]
+ 00c34ecc ["CALL", null, ["callee:00c5f050:8"]]
- 00c33ed8 bytes 6aa80094
+ 00c34ecc bytes 61a80094
- 00c33efc ["INT_ADD", "register:40f0:8", ["const:c33efc:8", "const:4:8"]]
- 00c33efc ["CALL", null, ["callee:00c269c4:8"]]
+ 00c34ef0 ["INT_ADD", "register:40f0:8", ["const:c34ef0:8", "const:4:8"]]
+ 00c34ef0 ["CALL", null, ["callee:00c269c4:8"]]
- 00c33efc bytes b5c6ff97
+ 00c34ef0 bytes b5c6ff97
- 00c33f1c ["INT_ADD", "register:40f0:8", ["const:c33f1c:8", "const:4:8"]]
- 00c33f1c ["CALL", null, ["callee:00c5f050:8"]]
+ 00c34f10 ["INT_ADD", "register:40f0:8", ["const:c34f10:8", "const:4:8"]]
+ 00c34f10 ["CALL", null, ["callee:00c5f050:8"]]
- 00c33f1c bytes 59a80094
+ 00c34f10 bytes 50a80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06431a67ad2caeda46120d2c33189e06"></a>

### [`00c34518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md) → [`00c3550c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c3550c.md) _ZNSt6__ndk117moneypunct_bynameIwLb1EE4initEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e9d0.md) · 呼出先 17件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c259d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c25/00c259d0.md) [`00c2c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c634.md)
- 新版 呼出元 1件 [`00c5f9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f9a0.md) · 呼出先 17件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`006d7aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aec.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c269c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c26/00c269c4.md) [`00c2d628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d628.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35bc4",
      "incomplete_value": false,
      "site": "00c35bc8",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34bd0",
      "incomplete_value": false,
      "site": "00c34bd4",
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
            "const:d98:8"
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
      "definition_site": "00c35bdc",
      "incomplete_value": false,
      "site": "00c35bec",
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
            "const:874:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34be8",
      "incomplete_value": false,
      "site": "00c34bf8",
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
            "const:79d:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c35c08",
      "incomplete_value": false,
      "site": "00c35c0c",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34c14",
      "incomplete_value": false,
      "site": "00c34c18",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c35bc4",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ],
    [
      "00c35bdc",
      "PARAM",
      [
        "storage",
        "002b179d",
        null,
        "string"
      ]
    ],
    [
      "00c35c08",
      "PARAM",
      [
        "storage",
        "0029fd98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c35bc4",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ],
    [
      "00c35bdc",
      "PARAM",
      [
        "storage",
        "002b1874",
        null,
        "string"
      ]
    ],
    [
      "00c35c08",
      "PARAM",
      [
        "storage",
        "0029fdd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md#insn-00c34bd4) · [`00c34bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md#insn-00c34bf8) · [`00c34c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34518.md#insn-00c34c18)
- 新版 [`00c35bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c3550c.md#insn-00c35bc8) · [`00c35bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c3550c.md#insn-00c35bec) · [`00c35c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c3550c.md#insn-00c35c0c)

~~~diff
- 00c34bd4 ["INT_ADD", "register:40f0:8", ["const:c34bd4:8", "const:4:8"]]
- 00c34bd4 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c35bc8 ["INT_ADD", "register:40f0:8", ["const:c35bc8:8", "const:4:8"]]
+ 00c35bc8 ["CALL", null, ["callee:00c5f050:8"]]
- 00c34bd4 bytes 2ba50094
+ 00c35bc8 bytes 22a50094
- 00c34bf8 ["INT_ADD", "register:40f0:8", ["const:c34bf8:8", "const:4:8"]]
- 00c34bf8 ["CALL", null, ["callee:00c269c4:8"]]
+ 00c35bec ["INT_ADD", "register:40f0:8", ["const:c35bec:8", "const:4:8"]]
+ 00c35bec ["CALL", null, ["callee:00c269c4:8"]]
- 00c34bf8 bytes 76c3ff97
+ 00c35bec bytes 76c3ff97
- 00c34c18 ["INT_ADD", "register:40f0:8", ["const:c34c18:8", "const:4:8"]]
- 00c34c18 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c35c0c ["INT_ADD", "register:40f0:8", ["const:c35c0c:8", "const:4:8"]]
+ 00c35c0c ["CALL", null, ["callee:00c5f050:8"]]
- 00c34c18 bytes 1aa50094
+ 00c35c0c bytes 11a50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca7ba825de14645823029e67b6e8c0e"></a>

### [`00c34e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e58.md) → [`00c35e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e4c.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c5a950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a950.md) [`00c5ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ebe0.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c5b920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b920.md) [`00c5fbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fbb0.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c35e74",
      "incomplete_value": true,
      "site": "00c35e78",
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
      "definition_site": "00c34e80",
      "incomplete_value": true,
      "site": "00c34e84",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c35edc",
      "incomplete_value": true,
      "site": "00c35edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c34ee8",
      "incomplete_value": true,
      "site": "00c34ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c35e90",
      "incomplete_value": true,
      "site": "00c35e94",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00c34e9c",
      "incomplete_value": true,
      "site": "00c34ea0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "00c35e6c",
      "READ",
      [
        "storage",
        "00c9beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c35e78",
      "DATA",
      [
        "storage",
        "00c93990",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c35e84",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c35e6c",
      "READ",
      [
        "storage",
        "00c9ce80",
        null,
        "pointer"
      ]
    ],
    [
      "00c35e78",
      "DATA",
      [
        "storage",
        "00c94960",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c35e84",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c34ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e58.md#insn-00c34ecc) · [`00c34ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e58.md#insn-00c34ee4) · [`00c34ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c34/00c34e58.md#insn-00c34ee8)
- 新版 [`00c35ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e4c.md#insn-00c35ec0) · [`00c35ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e4c.md#insn-00c35ed8) · [`00c35edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c35/00c35e4c.md#insn-00c35edc)

~~~diff
- 00c34ecc ["INT_ADD", "register:40f0:8", ["const:c34ecc:8", "const:4:8"]]
- 00c34ecc ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c35ec0 ["INT_ADD", "register:40f0:8", ["const:c35ec0:8", "const:4:8"]]
+ 00c35ec0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c34ecc bytes 158c0094
+ 00c35ec0 bytes 0c8c0094
- 00c34ee4 ["INT_ADD", "register:40f0:8", ["const:c34ee4:8", "const:4:8"]]
- 00c34ee4 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c35ed8 ["INT_ADD", "register:40f0:8", ["const:c35ed8:8", "const:4:8"]]
+ 00c35ed8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c34ee4 bytes 03a10094
+ 00c35ed8 bytes faa00094
- 00c34ee8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
- 00c34ee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c35edc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d58:8"]]
+ 00c35edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c34ee8 bytes a0ce06f9
+ 00c35edc bytes a0ae06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe4332c3ccb327bbe10bdd9063dc0ef"></a>

### [`00c354dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md) → [`00c364d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364d0.md) FUN_00c364d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c35570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35570.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 1件 [`00c36564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36564.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c364f0",
      "incomplete_value": true,
      "site": "00c364f4",
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
      "definition_site": "00c354fc",
      "incomplete_value": true,
      "site": "00c35500",
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
      "00c364e8",
      "READ",
      [
        "storage",
        "00c9be68",
        null,
        "pointer"
      ]
    ],
    [
      "00c364f4",
      "DATA",
      [
        "storage",
        "00c954d0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c364e8",
      "READ",
      [
        "storage",
        "00c9ce38",
        null,
        "pointer"
      ]
    ],
    [
      "00c364f4",
      "DATA",
      [
        "storage",
        "00c964a0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c354ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md#insn-00c354ec) · [`00c354f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md#insn-00c354f4) · [`00c35524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c354dc.md#insn-00c35524)
- 新版 [`00c364e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364d0.md#insn-00c364e0) · [`00c364e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364d0.md#insn-00c364e8) · [`00c36518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c364d0.md#insn-00c36518)

~~~diff
- 00c354ec ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c364e0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c354ec bytes 280300d0
+ 00c364e0 bytes 280300d0
- 00c354f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 00c354f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c364e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e38:8"]]
+ 00c364e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c354f4 bytes 083547f9
+ 00c364e8 bytes 081d47f9
- 00c35524 ["INT_ADD", "register:40f0:8", ["const:c35524:8", "const:4:8"]]
- 00c35524 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c36518 ["INT_ADD", "register:40f0:8", ["const:c36518:8", "const:4:8"]]
+ 00c36518 ["CALL", null, ["callee:00c58f50:8"]]
- 00c35524 bytes 978a0094
+ 00c36518 bytes 8e8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbcc8f82cfe8dec34ca9341c569fa6e4"></a>

### [`00c3559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md) → [`00c36590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36590.md) FUN_00c36590

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c35630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35630.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 1件 [`00c36624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36624.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c365b0",
      "incomplete_value": true,
      "site": "00c365b4",
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
      "definition_site": "00c355bc",
      "incomplete_value": true,
      "site": "00c355c0",
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
      "00c365a8",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00c365b4",
      "DATA",
      [
        "storage",
        "00c95558",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c365a8",
      "READ",
      [
        "storage",
        "00c9ce40",
        null,
        "pointer"
      ]
    ],
    [
      "00c365b4",
      "DATA",
      [
        "storage",
        "00c96528",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c355ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md#insn-00c355ac) · [`00c355b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md#insn-00c355b4) · [`00c355e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3559c.md#insn-00c355e4)
- 新版 [`00c365a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36590.md#insn-00c365a0) · [`00c365a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36590.md#insn-00c365a8) · [`00c365d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36590.md#insn-00c365d8)

~~~diff
- 00c355ac ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c365a0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c355ac bytes 280300d0
+ 00c365a0 bytes 280300d0
- 00c355b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00c355b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c365a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e40:8"]]
+ 00c365a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c355b4 bytes 083947f9
+ 00c365a8 bytes 082147f9
- 00c355e4 ["INT_ADD", "register:40f0:8", ["const:c355e4:8", "const:4:8"]]
- 00c355e4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c365d8 ["INT_ADD", "register:40f0:8", ["const:c365d8:8", "const:4:8"]]
+ 00c365d8 ["CALL", null, ["callee:00c58f50:8"]]
- 00c355e4 bytes 678a0094
+ 00c365d8 bytes 5e8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a31efc65a222aef9fa0f010d93f61b8"></a>

### [`00c3565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md) → [`00c36650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36650.md) FUN_00c36650

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c356f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c356f0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 1件 [`00c366e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c366e4.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c36670",
      "incomplete_value": true,
      "site": "00c36674",
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
      "definition_site": "00c3567c",
      "incomplete_value": true,
      "site": "00c35680",
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
      "00c36668",
      "READ",
      [
        "storage",
        "00c9be78",
        null,
        "pointer"
      ]
    ],
    [
      "00c36674",
      "DATA",
      [
        "storage",
        "00c955e0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c36668",
      "READ",
      [
        "storage",
        "00c9ce48",
        null,
        "pointer"
      ]
    ],
    [
      "00c36674",
      "DATA",
      [
        "storage",
        "00c965b0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3566c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md#insn-00c3566c) · [`00c35674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md#insn-00c35674) · [`00c356a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3565c.md#insn-00c356a4)
- 新版 [`00c36660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36650.md#insn-00c36660) · [`00c36668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36650.md#insn-00c36668) · [`00c36698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36650.md#insn-00c36698)

~~~diff
- 00c3566c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c36660 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c3566c bytes 280300d0
+ 00c36660 bytes 280300d0
- 00c35674 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00c35674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c36668 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
+ 00c36668 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c35674 bytes 083d47f9
+ 00c36668 bytes 082547f9
- 00c356a4 ["INT_ADD", "register:40f0:8", ["const:c356a4:8", "const:4:8"]]
- 00c356a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00c36698 ["INT_ADD", "register:40f0:8", ["const:c36698:8", "const:4:8"]]
+ 00c36698 ["CALL", null, ["callee:00c58f50:8"]]
- 00c356a4 bytes 378a0094
+ 00c36698 bytes 2e8a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e86e798354be10b10b7bbcb5653d44a9"></a>

### [`00c3596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md) → [`00c36960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md) FUN_00c36960

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c24970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c24/00c24970.md) [`00c35984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35984.md) [`00c35ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c35ae0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`00c25964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c25/00c25964.md) [`00c36978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36978.md) [`00c36ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36ad4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c36970",
      "incomplete_value": false,
      "site": "00c36974",
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
      "definition_site": "00c3597c",
      "incomplete_value": false,
      "site": "00c35980",
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
      "00c36970",
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
      "00c36970",
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

- 旧版 [`00c35980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md#insn-00c35980) · [`00c35978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md#insn-00c35978) · [`00c3597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c35/00c3596c.md#insn-00c3597c)
- 新版 [`00c36974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md#insn-00c36974) · [`00c3696c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md#insn-00c3696c) · [`00c36970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c36/00c36960.md#insn-00c36970)

~~~diff
- 00c35980 ["INT_ADD", "register:40f0:8", ["const:c35980:8", "const:4:8"]]
- 00c35980 ["CALL", null, ["callee:0043bad8:8"]]
+ 00c36974 ["INT_ADD", "register:40f0:8", ["const:c36974:8", "const:4:8"]]
+ 00c36974 ["CALL", null, ["callee:0043bad8:8"]]
- 00c35980 bytes 8e17e097
+ 00c36974 bytes 5914e097
- 00c35978 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00c3696c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00c35978 bytes 00b4ffd0
+ 00c3696c bytes 00b4ffd0
- 00c3597c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00c3597c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c3597c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c3597c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c36970 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00c36970 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c36970 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c36970 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c3597c bytes 00303e91
+ 00c36970 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2434901210789f0a9107e1a4ab36cf1b"></a>

### [`00c36054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md) → [`00c37048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md) FUN_00c37048

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 96件 [`00c07928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c07/00c07928.md) [`00c0a5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a5d0.md) [`00c0ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0ae00.md) [`00c0da44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0da44.md) [`00c0e128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0e/00c0e128.md) · 呼出先 1件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md)
- 新版 呼出元 96件 [`00c0891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c08/00c0891c.md) [`00c0b5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b5c4.md) [`00c0bdf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0bdf4.md) [`00c0ea38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0ea38.md) [`00c0f11c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0f/00c0f11c.md) · 呼出先 1件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3706c",
      "incomplete_value": true,
      "site": "00c37070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36078",
      "incomplete_value": true,
      "site": "00c3607c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
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
      "00c3706c",
      "READ",
      [
        "storage",
        "00c9bed8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3706c",
      "PARAM",
      [
        "storage",
        "01127f00",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00c3706c",
      "READ",
      [
        "storage",
        "00c9cea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3706c",
      "PARAM",
      [
        "storage",
        "01128ec0",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md#insn-00c3607c) · [`00c36068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md#insn-00c36068) · [`00c36078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36054.md#insn-00c36078)
- 新版 [`00c37070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md#insn-00c37070) · [`00c3705c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md#insn-00c3705c) · [`00c3706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37048.md#insn-00c3706c)

~~~diff
- 00c3607c ["INT_ADD", "register:40f0:8", ["const:c3607c:8", "const:4:8"]]
- 00c3607c ["CALL", null, ["callee:00c54d30:8"]]
+ 00c37070 ["INT_ADD", "register:40f0:8", ["const:c37070:8", "const:4:8"]]
+ 00c37070 ["CALL", null, ["callee:00c54d30:8"]]
- 00c3607c bytes 31770094
+ 00c37070 bytes 30770094
- 00c36068 ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 00c3705c ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00c36068 bytes 210300b0
+ 00c3705c bytes 210300b0
- 00c36078 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed8:8"]]
- 00c36078 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c3706c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ea8:8"]]
+ 00c3706c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00c36078 bytes 216c47f9
+ 00c3706c bytes 215447f9
~~~


<a id="compare-a4effa9ab29930d233705fa7c9b514bc"></a>

### [`00c36098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36098.md) → [`00c3708c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3708c.md) FUN_00c3708c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "definition_site": "00c370ac",
      "incomplete_value": true,
      "site": "00c370b0",
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
      "definition_site": "00c360b8",
      "incomplete_value": true,
      "site": "00c360bc",
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
      "definition_site": "00c370c4",
      "incomplete_value": true,
      "site": "00c370c8",
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
      "definition_site": "00c360d0",
      "incomplete_value": true,
      "site": "00c360d4",
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
      "00c370a4",
      "READ",
      [
        "storage",
        "00c9bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00c370b0",
      "DATA",
      [
        "storage",
        "00c938a0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c370bc",
      "READ",
      [
        "storage",
        "00c9be98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c370a4",
      "READ",
      [
        "storage",
        "00c9ce70",
        null,
        "pointer"
      ]
    ],
    [
      "00c370b0",
      "DATA",
      [
        "storage",
        "00c94870",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c370bc",
      "READ",
      [
        "storage",
        "00c9ce68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c360a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36098.md#insn-00c360a8) · [`00c360b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36098.md#insn-00c360b0) · [`00c360c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36098.md#insn-00c360c0)
- 新版 [`00c3709c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3708c.md#insn-00c3709c) · [`00c370a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3708c.md#insn-00c370a4) · [`00c370b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3708c.md#insn-00c370b4)

~~~diff
- 00c360a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c3709c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c360a8 bytes 280300b0
+ 00c3709c bytes 280300b0
- 00c360b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00c360b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c370a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00c370a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c360b0 bytes 085147f9
+ 00c370a4 bytes 083947f9
- 00c360c0 ["INT_ADD", "register:40f0:8", ["const:c360c0:8", "const:4:8"]]
- 00c360c0 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c370b4 ["INT_ADD", "register:40f0:8", ["const:c370b4:8", "const:4:8"]]
+ 00c370b4 ["CALL", null, ["callee:00c5e270:8"]]
- 00c360c0 bytes 789c0094
+ 00c370b4 bytes 6f9c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c83502cd7630a526996d5ea3424800"></a>

### [`00c36108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36108.md) → [`00c370fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c370fc.md) FUN_00c370fc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2a0.md) [`00c5ead0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ead0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e270.md) [`00c5faa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5faa0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3711c",
      "incomplete_value": true,
      "site": "00c37120",
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
      "definition_site": "00c36128",
      "incomplete_value": true,
      "site": "00c3612c",
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
      "00c37114",
      "READ",
      [
        "storage",
        "00c9bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00c37120",
      "DATA",
      [
        "storage",
        "00c93908",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00c37114",
      "READ",
      [
        "storage",
        "00c9ce78",
        null,
        "pointer"
      ]
    ],
    [
      "00c37120",
      "DATA",
      [
        "storage",
        "00c948d8",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36108.md#insn-00c36118) · [`00c36120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36108.md#insn-00c36120) · [`00c36130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36108.md#insn-00c36130)
- 新版 [`00c3710c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c370fc.md#insn-00c3710c) · [`00c37114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c370fc.md#insn-00c37114) · [`00c37124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c370fc.md#insn-00c37124)

~~~diff
- 00c36118 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c3710c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c36118 bytes 280300b0
+ 00c3710c bytes 280300b0
- 00c36120 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00c36120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c37114 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
+ 00c37114 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c36120 bytes 085547f9
+ 00c37114 bytes 083d47f9
- 00c36130 ["INT_ADD", "register:40f0:8", ["const:c36130:8", "const:4:8"]]
- 00c36130 ["CALL", null, ["callee:00c5e270:8"]]
+ 00c37124 ["INT_ADD", "register:40f0:8", ["const:c37124:8", "const:4:8"]]
+ 00c37124 ["CALL", null, ["callee:00c5e270:8"]]
- 00c36130 bytes 5c9c0094
+ 00c37124 bytes 539c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc70db9d03d5038423588fcb84ab74ae"></a>

### [`00c36208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md) → [`00c371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md) FUN_00c371fc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08028.md) [`00c0b508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b508.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d220.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c0901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c0901c.md) [`00c0c4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c4fc.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1f0.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c372f8",
      "incomplete_value": true,
      "site": "00c372f8",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36304",
      "incomplete_value": true,
      "site": "00c36304",
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
            "const:d98:8"
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
      "definition_site": "00c37254",
      "incomplete_value": true,
      "site": "00c37264",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36260",
      "incomplete_value": true,
      "site": "00c36270",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:d98:8"
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
      "definition_site": "00c372d8",
      "incomplete_value": false,
      "site": "00c372dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c362e4",
      "incomplete_value": false,
      "site": "00c362e8",
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
            "const:da0:8"
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
      "00c3724c",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37254",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c372d8",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c3724c",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37254",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c372d8",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md#insn-00c36270) · [`00c362e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md#insn-00c362e8) · [`00c36300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36208.md#insn-00c36300)
- 新版 [`00c37264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md#insn-00c37264) · [`00c372dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md#insn-00c372dc) · [`00c372f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371fc.md#insn-00c372f4)

~~~diff
- 00c36270 ["INT_ADD", "register:40f0:8", ["const:c36270:8", "const:4:8"]]
- 00c36270 ["CALL", null, ["callee:00c5e1f0:8"]]
+ 00c37264 ["INT_ADD", "register:40f0:8", ["const:c37264:8", "const:4:8"]]
+ 00c37264 ["CALL", null, ["callee:00c5e1f0:8"]]
- 00c36270 bytes ec9b0094
+ 00c37264 bytes e39b0094
- 00c362e8 ["INT_ADD", "register:40f0:8", ["const:c362e8:8", "const:4:8"]]
- 00c362e8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c372dc ["INT_ADD", "register:40f0:8", ["const:c372dc:8", "const:4:8"]]
+ 00c372dc ["CALL", null, ["callee:00c58ef0:8"]]
- 00c362e8 bytes 0e870094
+ 00c372dc bytes 05870094
- 00c36300 ["INT_ADD", "register:40f0:8", ["const:c36300:8", "const:4:8"]]
- 00c36300 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c372f4 ["INT_ADD", "register:40f0:8", ["const:c372f4:8", "const:4:8"]]
+ 00c372f4 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36300 bytes fc9b0094
+ 00c372f4 bytes f39b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fac56d6bbffc95c65c803002172b58e"></a>

### [`00c36330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md) → [`00c37324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md) FUN_00c37324

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08464.md) [`00c0b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0b938.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d220.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c09458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09458.md) [`00c0c92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0c92c.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e1f0.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37420",
      "incomplete_value": true,
      "site": "00c37420",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3642c",
      "incomplete_value": true,
      "site": "00c3642c",
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
            "const:d98:8"
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
      "definition_site": "00c3737c",
      "incomplete_value": true,
      "site": "00c3738c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36388",
      "incomplete_value": true,
      "site": "00c36398",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:d98:8"
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
      "definition_site": "00c37400",
      "incomplete_value": false,
      "site": "00c37404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3640c",
      "incomplete_value": false,
      "site": "00c36410",
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
            "const:da0:8"
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
      "00c37374",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3737c",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37400",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c37374",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3737c",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37400",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md#insn-00c36398) · [`00c36410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md#insn-00c36410) · [`00c36428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36330.md#insn-00c36428)
- 新版 [`00c3738c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md#insn-00c3738c) · [`00c37404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md#insn-00c37404) · [`00c3741c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37324.md#insn-00c3741c)

~~~diff
- 00c36398 ["INT_ADD", "register:40f0:8", ["const:c36398:8", "const:4:8"]]
- 00c36398 ["CALL", null, ["callee:00c5e1f0:8"]]
+ 00c3738c ["INT_ADD", "register:40f0:8", ["const:c3738c:8", "const:4:8"]]
+ 00c3738c ["CALL", null, ["callee:00c5e1f0:8"]]
- 00c36398 bytes a29b0094
+ 00c3738c bytes 999b0094
- 00c36410 ["INT_ADD", "register:40f0:8", ["const:c36410:8", "const:4:8"]]
- 00c36410 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c37404 ["INT_ADD", "register:40f0:8", ["const:c37404:8", "const:4:8"]]
+ 00c37404 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36410 bytes c4860094
+ 00c37404 bytes bb860094
- 00c36428 ["INT_ADD", "register:40f0:8", ["const:c36428:8", "const:4:8"]]
- 00c36428 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c3741c ["INT_ADD", "register:40f0:8", ["const:c3741c:8", "const:4:8"]]
+ 00c3741c ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36428 bytes b29b0094
+ 00c3741c bytes a99b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6649b02dde216a2ee6c4c258425417b"></a>

### [`00c36458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md) → [`00c3744c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md) FUN_00c3744c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c088a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c088a0.md) [`00c0bd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0b/00c0bd68.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c09894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09894.md) [`00c0cd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0c/00c0cd5c.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e200.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37578",
      "incomplete_value": true,
      "site": "00c37578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36584",
      "incomplete_value": true,
      "site": "00c36584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c374c0",
      "incomplete_value": true,
      "site": "00c374d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c364cc",
      "incomplete_value": true,
      "site": "00c364dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c37558",
      "incomplete_value": false,
      "site": "00c3755c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36564",
      "incomplete_value": false,
      "site": "00c36568",
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
            "const:da0:8"
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
      "00c374b8",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c374c0",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37558",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c374b8",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c374c0",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37558",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c364dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md#insn-00c364dc) · [`00c36568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md#insn-00c36568) · [`00c36580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36458.md#insn-00c36580)
- 新版 [`00c374d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md#insn-00c374d0) · [`00c3755c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md#insn-00c3755c) · [`00c37574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c3744c.md#insn-00c37574)

~~~diff
- 00c364dc ["INT_ADD", "register:40f0:8", ["const:c364dc:8", "const:4:8"]]
- 00c364dc ["CALL", null, ["callee:00c5e200:8"]]
+ 00c374d0 ["INT_ADD", "register:40f0:8", ["const:c374d0:8", "const:4:8"]]
+ 00c374d0 ["CALL", null, ["callee:00c5e200:8"]]
- 00c364dc bytes 559b0094
+ 00c374d0 bytes 4c9b0094
- 00c36568 ["INT_ADD", "register:40f0:8", ["const:c36568:8", "const:4:8"]]
- 00c36568 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c3755c ["INT_ADD", "register:40f0:8", ["const:c3755c:8", "const:4:8"]]
+ 00c3755c ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36568 bytes 6e860094
+ 00c3755c bytes 65860094
- 00c36580 ["INT_ADD", "register:40f0:8", ["const:c36580:8", "const:4:8"]]
- 00c36580 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37574 ["INT_ADD", "register:40f0:8", ["const:c37574:8", "const:4:8"]]
+ 00c37574 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36580 bytes 5c9b0094
+ 00c37574 bytes 539b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0040261531d9d6ddded8f3a297cc509"></a>

### [`00c365b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md) → [`00c375a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md) FUN_00c375a4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c08cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c08/00c08cdc.md) [`00c0c198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c198.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c09cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c09/00c09cd0.md) [`00c0d18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d18c.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e200.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c376cc",
      "incomplete_value": true,
      "site": "00c376cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366d8",
      "incomplete_value": true,
      "site": "00c366d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c37618",
      "incomplete_value": true,
      "site": "00c37628",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36624",
      "incomplete_value": true,
      "site": "00c36634",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c376ac",
      "incomplete_value": false,
      "site": "00c376b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c366b8",
      "incomplete_value": false,
      "site": "00c366bc",
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
            "const:da0:8"
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
      "00c37610",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37618",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c376ac",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c37610",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37618",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c376ac",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md#insn-00c36634) · [`00c366bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md#insn-00c366bc) · [`00c366d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c365b0.md#insn-00c366d4)
- 新版 [`00c37628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md#insn-00c37628) · [`00c376b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md#insn-00c376b0) · [`00c376c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c375a4.md#insn-00c376c8)

~~~diff
- 00c36634 ["INT_ADD", "register:40f0:8", ["const:c36634:8", "const:4:8"]]
- 00c36634 ["CALL", null, ["callee:00c5e200:8"]]
+ 00c37628 ["INT_ADD", "register:40f0:8", ["const:c37628:8", "const:4:8"]]
+ 00c37628 ["CALL", null, ["callee:00c5e200:8"]]
- 00c36634 bytes ff9a0094
+ 00c37628 bytes f69a0094
- 00c366bc ["INT_ADD", "register:40f0:8", ["const:c366bc:8", "const:4:8"]]
- 00c366bc ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c376b0 ["INT_ADD", "register:40f0:8", ["const:c376b0:8", "const:4:8"]]
+ 00c376b0 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c366bc bytes 19860094
+ 00c376b0 bytes 10860094
- 00c366d4 ["INT_ADD", "register:40f0:8", ["const:c366d4:8", "const:4:8"]]
- 00c366d4 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c376c8 ["INT_ADD", "register:40f0:8", ["const:c376c8:8", "const:4:8"]]
+ 00c376c8 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c366d4 bytes 079b0094
+ 00c376c8 bytes fe9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7086bb36c546ae55a6a8031894232147"></a>

### [`00c36704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md) → [`00c376f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md) FUN_00c376f8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09118.md) [`00c0c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c5c8.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c0a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a10c.md) [`00c0d5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d5bc.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e200.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37814",
      "incomplete_value": true,
      "site": "00c37814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36820",
      "incomplete_value": true,
      "site": "00c36820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c3776c",
      "incomplete_value": true,
      "site": "00c3777c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36778",
      "incomplete_value": true,
      "site": "00c36788",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c377f4",
      "incomplete_value": false,
      "site": "00c377f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36800",
      "incomplete_value": false,
      "site": "00c36804",
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
            "const:da0:8"
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
      "00c37764",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3776c",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c377f4",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c37764",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c3776c",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c377f4",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md#insn-00c36788) · [`00c36804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md#insn-00c36804) · [`00c3681c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36704.md#insn-00c3681c)
- 新版 [`00c3777c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md#insn-00c3777c) · [`00c377f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md#insn-00c377f8) · [`00c37810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c376f8.md#insn-00c37810)

~~~diff
- 00c36788 ["INT_ADD", "register:40f0:8", ["const:c36788:8", "const:4:8"]]
- 00c36788 ["CALL", null, ["callee:00c5e200:8"]]
+ 00c3777c ["INT_ADD", "register:40f0:8", ["const:c3777c:8", "const:4:8"]]
+ 00c3777c ["CALL", null, ["callee:00c5e200:8"]]
- 00c36788 bytes aa9a0094
+ 00c3777c bytes a19a0094
- 00c36804 ["INT_ADD", "register:40f0:8", ["const:c36804:8", "const:4:8"]]
- 00c36804 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c377f8 ["INT_ADD", "register:40f0:8", ["const:c377f8:8", "const:4:8"]]
+ 00c377f8 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36804 bytes c7850094
+ 00c377f8 bytes be850094
- 00c3681c ["INT_ADD", "register:40f0:8", ["const:c3681c:8", "const:4:8"]]
- 00c3681c ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37810 ["INT_ADD", "register:40f0:8", ["const:c37810:8", "const:4:8"]]
+ 00c37810 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c3681c bytes b59a0094
+ 00c37810 bytes ac9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e43adb83da8b5fa973f583f015a75d"></a>

### [`00c3684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md) → [`00c37840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md) FUN_00c37840

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09554.md) [`00c0c9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0c9f8.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c0a548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a548.md) [`00c0d9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0d9ec.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e200.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c3795c",
      "incomplete_value": true,
      "site": "00c3795c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36968",
      "incomplete_value": true,
      "site": "00c36968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00c378b4",
      "incomplete_value": true,
      "site": "00c378c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c368c0",
      "incomplete_value": true,
      "site": "00c368d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "definition_site": "00c3793c",
      "incomplete_value": false,
      "site": "00c37940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36948",
      "incomplete_value": false,
      "site": "00c3694c",
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
            "const:da0:8"
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
      "00c378ac",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c378b4",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3793c",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c378ac",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c378b4",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c3793c",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c368d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md#insn-00c368d0) · [`00c3694c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md#insn-00c3694c) · [`00c36964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c3684c.md#insn-00c36964)
- 新版 [`00c378c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md#insn-00c378c4) · [`00c37940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md#insn-00c37940) · [`00c37958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37840.md#insn-00c37958)

~~~diff
- 00c368d0 ["INT_ADD", "register:40f0:8", ["const:c368d0:8", "const:4:8"]]
- 00c368d0 ["CALL", null, ["callee:00c5e200:8"]]
+ 00c378c4 ["INT_ADD", "register:40f0:8", ["const:c378c4:8", "const:4:8"]]
+ 00c378c4 ["CALL", null, ["callee:00c5e200:8"]]
- 00c368d0 bytes 589a0094
+ 00c378c4 bytes 4f9a0094
- 00c3694c ["INT_ADD", "register:40f0:8", ["const:c3694c:8", "const:4:8"]]
- 00c3694c ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c37940 ["INT_ADD", "register:40f0:8", ["const:c37940:8", "const:4:8"]]
+ 00c37940 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c3694c bytes 75850094
+ 00c37940 bytes 6c850094
- 00c36964 ["INT_ADD", "register:40f0:8", ["const:c36964:8", "const:4:8"]]
- 00c36964 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37958 ["INT_ADD", "register:40f0:8", ["const:c37958:8", "const:4:8"]]
+ 00c37958 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36964 bytes 639a0094
+ 00c37958 bytes 5a9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db838c901bb5137fd3521dbdf1b4f67"></a>

### [`00c36994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md) → [`00c37988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md) FUN_00c37988

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c09990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09990.md) [`00c0ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0c/00c0ce28.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58680.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c0a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0a984.md) [`00c0de1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0d/00c0de1c.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59650.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37a74",
      "incomplete_value": false,
      "site": "00c37a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36a80",
      "incomplete_value": false,
      "site": "00c36a80",
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
            "const:d98:8"
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
      "definition_site": "00c37a50",
      "incomplete_value": false,
      "site": "00c37a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36a5c",
      "incomplete_value": false,
      "site": "00c36a60",
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
            "const:da0:8"
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
      "definition_site": "00c37a60",
      "incomplete_value": false,
      "site": "00c37a6c",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36a6c",
      "incomplete_value": false,
      "site": "00c36a78",
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
            "const:1bc:8"
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
      "00c379cc",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37a50",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37a60",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c379cc",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37a50",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37a60",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md#insn-00c36a60) · [`00c36a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md#insn-00c36a78) · [`00c36a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36994.md#insn-00c36a80)
- 新版 [`00c37a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md#insn-00c37a54) · [`00c37a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md#insn-00c37a6c) · [`00c37a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37988.md#insn-00c37a74)

~~~diff
- 00c36a60 ["INT_ADD", "register:40f0:8", ["const:c36a60:8", "const:4:8"]]
- 00c36a60 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c37a54 ["INT_ADD", "register:40f0:8", ["const:c37a54:8", "const:4:8"]]
+ 00c37a54 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36a60 bytes 30850094
+ 00c37a54 bytes 27850094
- 00c36a78 ["INT_ADD", "register:40f0:8", ["const:c36a78:8", "const:4:8"]]
- 00c36a78 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37a6c ["INT_ADD", "register:40f0:8", ["const:c37a6c:8", "const:4:8"]]
+ 00c37a6c ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36a78 bytes 1e9a0094
+ 00c37a6c bytes 159a0094
- 00c36a80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c36a80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c37a74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c37a74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c36a80 bytes 00cd06f9
+ 00c37a74 bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243d296265657c213e7c8cefdae499f2"></a>

### [`00c36aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md) → [`00c37aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md) FUN_00c37aa0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c09da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c09/00c09da8.md) [`00c0d234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d234.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 2件 [`00c0ad9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0a/00c0ad9c.md) [`00c0e228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e228.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c59660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59660.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37b8c",
      "incomplete_value": false,
      "site": "00c37b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36b98",
      "incomplete_value": false,
      "site": "00c36b98",
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
            "const:d98:8"
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
      "definition_site": "00c37b68",
      "incomplete_value": false,
      "site": "00c37b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36b74",
      "incomplete_value": false,
      "site": "00c36b78",
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
            "const:da0:8"
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
      "definition_site": "00c37b78",
      "incomplete_value": false,
      "site": "00c37b84",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36b84",
      "incomplete_value": false,
      "site": "00c36b90",
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
            "const:1bc:8"
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
      "00c37ae4",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37b68",
      "PARAM",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37b78",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37ae4",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37b68",
      "PARAM",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37b78",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md#insn-00c36b78) · [`00c36b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md#insn-00c36b90) · [`00c36b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36aac.md#insn-00c36b98)
- 新版 [`00c37b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md#insn-00c37b6c) · [`00c37b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md#insn-00c37b84) · [`00c37b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37aa0.md#insn-00c37b8c)

~~~diff
- 00c36b78 ["INT_ADD", "register:40f0:8", ["const:c36b78:8", "const:4:8"]]
- 00c36b78 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c37b6c ["INT_ADD", "register:40f0:8", ["const:c37b6c:8", "const:4:8"]]
+ 00c37b6c ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36b78 bytes ea840094
+ 00c37b6c bytes e1840094
- 00c36b90 ["INT_ADD", "register:40f0:8", ["const:c36b90:8", "const:4:8"]]
- 00c36b90 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37b84 ["INT_ADD", "register:40f0:8", ["const:c37b84:8", "const:4:8"]]
+ 00c37b84 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36b90 bytes d8990094
+ 00c37b84 bytes cf990094
- 00c36b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c36b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c37b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 00c37b8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c36b98 bytes 00cd06f9
+ 00c37b8c bytes 00ad06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05901c70808fb1c0fa334403630b84e5"></a>

### [`00c36bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md) → [`00c37bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md) FUN_00c37bb8

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c0a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0a/00c0a1c0.md) [`00c0d640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0d/00c0d640.md) · 呼出先 5件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md) [`00c5ee30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee30.md)
- 新版 呼出元 2件 [`00c0b1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0b/00c0b1b4.md) [`00c0e634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c0e/00c0e634.md) · 呼出先 5件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md) [`00c5fe00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.07% / 新版 85.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c37cb0",
      "incomplete_value": true,
      "site": "00c37cb0",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36cbc",
      "incomplete_value": true,
      "site": "00c36cbc",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37c90",
      "incomplete_value": false,
      "site": "00c37c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36c9c",
      "incomplete_value": false,
      "site": "00c36ca0",
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
            "const:da0:8"
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
      "definition_site": "00c37ca0",
      "incomplete_value": false,
      "site": "00c37cac",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c36cac",
      "incomplete_value": false,
      "site": "00c36cb8",
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
            "const:1bc:8"
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
      "00c37c04",
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37c0c",
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37c44",
      "READ",
      [
        "storage",
        "002c2f80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37c04",
      "READ",
      [
        "storage",
        "01128d60",
        null,
        "undefined1"
      ]
    ],
    [
      "00c37c0c",
      "READ",
      [
        "storage",
        "01128d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00c37c44",
      "READ",
      [
        "storage",
        "002c2fd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c36ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md#insn-00c36ca0) · [`00c36cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md#insn-00c36cb8) · [`00c36cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36bc4.md#insn-00c36cbc)
- 新版 [`00c37c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md#insn-00c37c94) · [`00c37cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md#insn-00c37cac) · [`00c37cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37bb8.md#insn-00c37cb0)

~~~diff
- 00c36ca0 ["INT_ADD", "register:40f0:8", ["const:c36ca0:8", "const:4:8"]]
- 00c36ca0 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00c37c94 ["INT_ADD", "register:40f0:8", ["const:c37c94:8", "const:4:8"]]
+ 00c37c94 ["CALL", null, ["callee:00c58ef0:8"]]
- 00c36ca0 bytes a0840094
+ 00c37c94 bytes 97840094
- 00c36cb8 ["INT_ADD", "register:40f0:8", ["const:c36cb8:8", "const:4:8"]]
- 00c36cb8 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c37cac ["INT_ADD", "register:40f0:8", ["const:c37cac:8", "const:4:8"]]
+ 00c37cac ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c36cb8 bytes 8e990094
+ 00c37cac bytes 85990094
- 00c36cbc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d98:8"]]
- 00c36cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c37cb0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d58:8"]]
+ 00c37cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c36cbc bytes 00cf06f9
+ 00c37cb0 bytes 00af06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861e4bb2303d857cba9e00029c1a1bed"></a>

### [`00c37148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37148.md) → [`00c3813c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3813c.md) _ZNSt6__ndk111__call_onceERVmPvPFvS2_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfb0.md) · 呼出先 4件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md) [`00c5e2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2a0.md)
- 新版 呼出元 1件 [`00c5ef80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef80.md) · 呼出先 4件 [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f260.md) [`00c5f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38160",
      "incomplete_value": false,
      "site": "00c3816c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3716c",
      "incomplete_value": false,
      "site": "00c37178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00c381e4",
      "incomplete_value": false,
      "site": "00c381e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c371f0",
      "incomplete_value": false,
      "site": "00c371f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00c381f8",
      "incomplete_value": false,
      "site": "00c381fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37204",
      "incomplete_value": false,
      "site": "00c37208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "00c38160",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c3818c",
      "PARAM",
      [
        "storage",
        "01128ad8",
        null,
        null
      ]
    ],
    [
      "00c38190",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38160",
      "PARAM",
      [
        "storage",
        "01129a70",
        null,
        null
      ]
    ],
    [
      "00c3818c",
      "PARAM",
      [
        "storage",
        "01129a98",
        null,
        null
      ]
    ],
    [
      "00c38190",
      "PARAM",
      [
        "storage",
        "01129a70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37148.md#insn-00c37178) · [`00c371f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37148.md#insn-00c371f4) · [`00c37208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37148.md#insn-00c37208)
- 新版 [`00c3816c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3813c.md#insn-00c3816c) · [`00c381e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3813c.md#insn-00c381e8) · [`00c381fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3813c.md#insn-00c381fc)

~~~diff
- 00c37178 ["INT_ADD", "register:40f0:8", ["const:c37178:8", "const:4:8"]]
- 00c37178 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c3816c ["INT_ADD", "register:40f0:8", ["const:c3816c:8", "const:4:8"]]
+ 00c3816c ["CALL", null, ["callee:00c5c740:8"]]
- 00c37178 bytes 7e910094
+ 00c3816c bytes 75910094
- 00c371f4 ["INT_ADD", "register:40f0:8", ["const:c371f4:8", "const:4:8"]]
- 00c371f4 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c381e8 ["INT_ADD", "register:40f0:8", ["const:c381e8:8", "const:4:8"]]
+ 00c381e8 ["CALL", null, ["callee:00c5c750:8"]]
- 00c371f4 bytes 63910094
+ 00c381e8 bytes 5a910094
- 00c37208 ["INT_ADD", "register:40f0:8", ["const:c37208:8", "const:4:8"]]
- 00c37208 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c381fc ["INT_ADD", "register:40f0:8", ["const:c381fc:8", "const:4:8"]]
+ 00c381fc ["CALL", null, ["callee:00c5c740:8"]]
- 00c37208 bytes 5a910094
+ 00c381fc bytes 51910094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e28b0f4d8a1911e28a7664b092fc2df3"></a>

### [`00c3725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3725c.md) → [`00c38250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38250.md) FUN_00c38250

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38270",
      "incomplete_value": false,
      "site": "00c38274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3727c",
      "incomplete_value": false,
      "site": "00c37280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00c38284",
      "incomplete_value": false,
      "site": "00c38288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37290",
      "incomplete_value": false,
      "site": "00c37294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00c38290",
      "incomplete_value": false,
      "site": "00c38294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3729c",
      "incomplete_value": false,
      "site": "00c372a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00c38270",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c38284",
      "PARAM",
      [
        "storage",
        "01128ab0",
        null,
        null
      ]
    ],
    [
      "00c38290",
      "PARAM",
      [
        "storage",
        "01128ad8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38270",
      "PARAM",
      [
        "storage",
        "01129a70",
        null,
        null
      ]
    ],
    [
      "00c38284",
      "PARAM",
      [
        "storage",
        "01129a70",
        null,
        null
      ]
    ],
    [
      "00c38290",
      "PARAM",
      [
        "storage",
        "01129a98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3725c.md#insn-00c37280) · [`00c37294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3725c.md#insn-00c37294) · [`00c372a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3725c.md#insn-00c372a0)
- 新版 [`00c38274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38250.md#insn-00c38274) · [`00c38288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38250.md#insn-00c38288) · [`00c38294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38250.md#insn-00c38294)

~~~diff
- 00c37280 ["INT_ADD", "register:40f0:8", ["const:c37280:8", "const:4:8"]]
- 00c37280 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c38274 ["INT_ADD", "register:40f0:8", ["const:c38274:8", "const:4:8"]]
+ 00c38274 ["CALL", null, ["callee:00c5c740:8"]]
- 00c37280 bytes 3c910094
+ 00c38274 bytes 33910094
- 00c37294 ["INT_ADD", "register:40f0:8", ["const:c37294:8", "const:4:8"]]
- 00c37294 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c38288 ["INT_ADD", "register:40f0:8", ["const:c38288:8", "const:4:8"]]
+ 00c38288 ["CALL", null, ["callee:00c5c750:8"]]
- 00c37294 bytes 3b910094
+ 00c38288 bytes 32910094
- 00c372a0 ["INT_ADD", "register:40f0:8", ["const:c372a0:8", "const:4:8"]]
- 00c372a0 ["CALL", null, ["callee:00c5f260:8"]]
+ 00c38294 ["INT_ADD", "register:40f0:8", ["const:c38294:8", "const:4:8"]]
+ 00c38294 ["CALL", null, ["callee:00c5f260:8"]]
- 00c372a0 bytes fc9b0094
+ 00c38294 bytes f39b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb48d1008b476f9428651784bef24950"></a>

### [`00c37358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37358.md) → [`00c3834c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3834c.md) _ZNSt6__ndk120__get_collation_nameEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8d0.md) · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 1件 [`00c5b8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8a0.md) · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c383b0",
      "incomplete_value": true,
      "site": "00c383b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c373bc",
      "incomplete_value": true,
      "site": "00c373c4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "00c38384",
      "READ",
      [
        "storage",
        "00c96218",
        null,
        "pointer"
      ]
    ],
    [
      "00c38384",
      "PARAM",
      [
        "storage",
        "002b704d",
        null,
        "string"
      ]
    ],
    [
      "00c38384",
      "READ",
      [
        "storage",
        "00c96058",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c38384",
      "READ",
      [
        "storage",
        "00c971e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c38384",
      "PARAM",
      [
        "storage",
        "002b711c",
        null,
        "string"
      ]
    ],
    [
      "00c38384",
      "READ",
      [
        "storage",
        "00c97028",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37358.md#insn-00c37380) · [`00c37394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37358.md#insn-00c37394) · [`00c373b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37358.md#insn-00c373b0)
- 新版 [`00c38374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3834c.md#insn-00c38374) · [`00c38388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3834c.md#insn-00c38388) · [`00c383a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3834c.md#insn-00c383a4)

~~~diff
- 00c37380 ["COPY", "register:40a8:8", ["const:c95ea8:8"]]
+ 00c38374 ["COPY", "register:40a8:8", ["const:c96e78:8"]]
- 00c37380 bytes 55592f10
+ 00c38374 bytes 35582f10
- 00c37394 ["INT_ADD", "register:40f0:8", ["const:c37394:8", "const:4:8"]]
- 00c37394 ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c38388 ["INT_ADD", "register:40f0:8", ["const:c38388:8", "const:4:8"]]
+ 00c38388 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c37394 bytes 63910094
+ 00c38388 bytes 5a910094
- 00c373b0 ["COPY", "register:4040:8", ["const:c96000:8"]]
+ 00c383a4 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c373b0 bytes e80200f0
+ 00c383a4 bytes e80200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d79c60df783b1e1a4ad0ee49670f4e"></a>

### [`00c37400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37400.md) → [`00c383f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c383f4.md) _ZNSt6__ndk115__get_classnameEPKcb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8e0.md) · 呼出先 1件 [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 1件 [`00c5b8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8b0.md) · 呼出先 1件 [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c38454",
      "incomplete_value": true,
      "site": "00c38458",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37460",
      "incomplete_value": true,
      "site": "00c37464",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_ADD"
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
      "00c3842c",
      "READ",
      [
        "storage",
        "00c96608",
        null,
        "pointer"
      ]
    ],
    [
      "00c3842c",
      "PARAM",
      [
        "storage",
        "002b3830",
        null,
        "string"
      ]
    ],
    [
      "00c3842c",
      "READ",
      [
        "storage",
        "00c965c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3842c",
      "READ",
      [
        "storage",
        "00c975d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3842c",
      "PARAM",
      [
        "storage",
        "002b387a",
        null,
        "string"
      ]
    ],
    [
      "00c3842c",
      "READ",
      [
        "storage",
        "00c97598",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37400.md#insn-00c37428) · [`00c3743c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37400.md#insn-00c3743c) · [`00c37458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37400.md#insn-00c37458)
- 新版 [`00c3841c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c383f4.md#insn-00c3841c) · [`00c38430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c383f4.md#insn-00c38430) · [`00c3844c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c383f4.md#insn-00c3844c)

~~~diff
- 00c37428 ["COPY", "register:40a8:8", ["const:c96598:8"]]
+ 00c3841c ["COPY", "register:40a8:8", ["const:c97568:8"]]
- 00c37428 bytes 958b2f10
+ 00c3841c bytes 758a2f10
- 00c3743c ["INT_ADD", "register:40f0:8", ["const:c3743c:8", "const:4:8"]]
- 00c3743c ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c38430 ["INT_ADD", "register:40f0:8", ["const:c38430:8", "const:4:8"]]
+ 00c38430 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c3743c bytes 39910094
+ 00c38430 bytes 30910094
- 00c37458 ["COPY", "register:4040:8", ["const:c96000:8"]]
+ 00c3844c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c37458 bytes e80200f0
+ 00c3844c bytes e80200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56eaaa2adf652694d04a337176c0c357"></a>

### [`00c37564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37564.md) → [`00c38558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38558.md) __cxa_bad_cast

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59db0.md) · 呼出先 4件 [`00c38008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38008.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5e550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e550.md)
- 新版 呼出元 1件 [`00c5ad80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad80.md) · 呼出先 4件 [`00c38ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ffc.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5f520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38584",
      "incomplete_value": true,
      "site": "00c3858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37590",
      "incomplete_value": true,
      "site": "00c37598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
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
      "definition_site": "00c38588",
      "incomplete_value": true,
      "site": "00c3858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37594",
      "incomplete_value": true,
      "site": "00c37598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
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
      "00c38584",
      "READ",
      [
        "storage",
        "00c9bc30",
        null,
        "pointer"
      ]
    ],
    [
      "00c38584",
      "PARAM",
      [
        "storage",
        "00c96a58",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c38588",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c38584",
      "READ",
      [
        "storage",
        "00c9cc00",
        null,
        "pointer"
      ]
    ],
    [
      "00c38584",
      "PARAM",
      [
        "storage",
        "00c97a28",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c38588",
      "READ",
      [
        "storage",
        "00c9cc08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37564.md#insn-00c37598) · [`00c37578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37564.md#insn-00c37578) · [`00c37580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37564.md#insn-00c37580)
- 新版 [`00c3858c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38558.md#insn-00c3858c) · [`00c3856c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38558.md#insn-00c3856c) · [`00c38574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38558.md#insn-00c38574)

~~~diff
- 00c37598 ["INT_ADD", "register:40f0:8", ["const:c37598:8", "const:4:8"]]
- 00c37598 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c3858c ["INT_ADD", "register:40f0:8", ["const:c3858c:8", "const:4:8"]]
+ 00c3858c ["CALL", null, ["callee:00c58fb0:8"]]
- 00c37598 bytes 92820094
+ 00c3858c bytes 89820094
- 00c37578 ["INT_ADD", "register:40f0:8", ["const:c37578:8", "const:4:8"]]
- 00c37578 ["CALL", null, ["callee:00c58f90:8"]]
+ 00c3856c ["INT_ADD", "register:40f0:8", ["const:c3856c:8", "const:4:8"]]
+ 00c3856c ["CALL", null, ["callee:00c58f90:8"]]
- 00c37578 bytes 92820094
+ 00c3856c bytes 89820094
- 00c37580 ["INT_ADD", "register:40f0:8", ["const:c37580:8", "const:4:8"]]
- 00c37580 ["CALL", null, ["callee:00c5f520:8"]]
+ 00c38574 ["INT_ADD", "register:40f0:8", ["const:c38574:8", "const:4:8"]]
+ 00c38574 ["CALL", null, ["callee:00c5f520:8"]]
- 00c37580 bytes f49b0094
+ 00c38574 bytes eb9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582d748ed6f278f0ad564c7a6ca42ed5"></a>

### [`00c3759c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3759c.md) → [`00c38590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38590.md) __cxa_bad_typeid

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c38064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38064.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5ee40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c39058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39058.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5fe10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c385bc",
      "incomplete_value": true,
      "site": "00c385c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c375c8",
      "incomplete_value": true,
      "site": "00c375d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
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
      "definition_site": "00c385c0",
      "incomplete_value": true,
      "site": "00c385c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c375cc",
      "incomplete_value": true,
      "site": "00c375d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
      "00c385bc",
      "READ",
      [
        "storage",
        "00c9bee8",
        null,
        "pointer"
      ]
    ],
    [
      "00c385bc",
      "PARAM",
      [
        "storage",
        "00c96a70",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c385c0",
      "READ",
      [
        "storage",
        "00c9bef0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c385bc",
      "READ",
      [
        "storage",
        "00c9ceb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c385bc",
      "PARAM",
      [
        "storage",
        "00c97a40",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c385c0",
      "READ",
      [
        "storage",
        "00c9cec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c375d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3759c.md#insn-00c375d0) · [`00c375b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3759c.md#insn-00c375b0) · [`00c375b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3759c.md#insn-00c375b8)
- 新版 [`00c385c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38590.md#insn-00c385c4) · [`00c385a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38590.md#insn-00c385a4) · [`00c385ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38590.md#insn-00c385ac)

~~~diff
- 00c375d0 ["INT_ADD", "register:40f0:8", ["const:c375d0:8", "const:4:8"]]
- 00c375d0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c385c4 ["INT_ADD", "register:40f0:8", ["const:c385c4:8", "const:4:8"]]
+ 00c385c4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00c375d0 bytes 84820094
+ 00c385c4 bytes 7b820094
- 00c375b0 ["INT_ADD", "register:40f0:8", ["const:c375b0:8", "const:4:8"]]
- 00c375b0 ["CALL", null, ["callee:00c58f90:8"]]
+ 00c385a4 ["INT_ADD", "register:40f0:8", ["const:c385a4:8", "const:4:8"]]
+ 00c385a4 ["CALL", null, ["callee:00c58f90:8"]]
- 00c375b0 bytes 84820094
+ 00c385a4 bytes 7b820094
- 00c375b8 ["INT_ADD", "register:40f0:8", ["const:c375b8:8", "const:4:8"]]
- 00c375b8 ["CALL", null, ["callee:00c5fe10:8"]]
+ 00c385ac ["INT_ADD", "register:40f0:8", ["const:c385ac:8", "const:4:8"]]
+ 00c385ac ["CALL", null, ["callee:00c5fe10:8"]]
- 00c375b8 bytes 229e0094
+ 00c385ac bytes 199e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67187b2229ea5948a9c18b61456c8704"></a>

### [`00c375d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c375d4.md) → [`00c385c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c385c8.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c590d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c385f4",
      "incomplete_value": true,
      "site": "00c385fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37600",
      "incomplete_value": true,
      "site": "00c37608",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c385f8",
      "incomplete_value": true,
      "site": "00c385fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37604",
      "incomplete_value": true,
      "site": "00c37608",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:ca8:8"
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
      "00c385f4",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00c385f4",
      "PARAM",
      [
        "storage",
        "00c96780",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c385f8",
      "READ",
      [
        "storage",
        "00c9aca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c385f4",
      "READ",
      [
        "storage",
        "00c9bc70",
        null,
        "pointer"
      ]
    ],
    [
      "00c385f4",
      "PARAM",
      [
        "storage",
        "00c97750",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c385f8",
      "READ",
      [
        "storage",
        "00c9bc78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c375d4.md#insn-00c37608) · [`00c375e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c375d4.md#insn-00c375e8) · [`00c375f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c375d4.md#insn-00c375f0)
- 新版 [`00c385fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c385c8.md#insn-00c385fc) · [`00c385dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c385c8.md#insn-00c385dc) · [`00c385e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c385c8.md#insn-00c385e4)

~~~diff
- 00c37608 ["INT_ADD", "register:40f0:8", ["const:c37608:8", "const:4:8"]]
- 00c37608 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00c385fc ["INT_ADD", "register:40f0:8", ["const:c385fc:8", "const:4:8"]]
+ 00c385fc ["CALL", null, ["callee:00c58fb0:8"]]
- 00c37608 bytes 76820094
+ 00c385fc bytes 6d820094
- 00c375e8 ["INT_ADD", "register:40f0:8", ["const:c375e8:8", "const:4:8"]]
- 00c375e8 ["CALL", null, ["callee:00c58f90:8"]]
+ 00c385dc ["INT_ADD", "register:40f0:8", ["const:c385dc:8", "const:4:8"]]
+ 00c385dc ["CALL", null, ["callee:00c58f90:8"]]
- 00c375e8 bytes 76820094
+ 00c385dc bytes 6d820094
- 00c375f0 ["INT_ADD", "register:40f0:8", ["const:c375f0:8", "const:4:8"]]
- 00c375f0 ["CALL", null, ["callee:00c590d0:8"]]
+ 00c385e4 ["INT_ADD", "register:40f0:8", ["const:c385e4:8", "const:4:8"]]
+ 00c385e4 ["CALL", null, ["callee:00c590d0:8"]]
- 00c375f0 bytes c4820094
+ 00c385e4 bytes bb820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3809bb0611107a993546b529a0e96398"></a>

### [`00c3760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md) → [`00c38600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38600.md) __cxa_guard_acquire

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) · 呼出先 5件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e2a0.md) [`00c5ee80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee80.md)
- 新版 呼出元 1件 [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) · 呼出先 5件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f270.md) [`00c5fe50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c38634",
      "incomplete_value": false,
      "site": "00c38640",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37640",
      "incomplete_value": false,
      "site": "00c3764c",
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
            "const:eb6:8"
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
      "definition_site": "00c3863c",
      "incomplete_value": false,
      "site": "00c38644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37648",
      "incomplete_value": false,
      "site": "00c37650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "00c386c4",
      "incomplete_value": false,
      "site": "00c386c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c376d0",
      "incomplete_value": false,
      "site": "00c376d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00c3863c",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c38640",
      "DATA",
      [
        "storage",
        "002b7eb6",
        null,
        "string"
      ]
    ],
    [
      "00c3868c",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3863c",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c38640",
      "DATA",
      [
        "storage",
        "002b7f85",
        null,
        "string"
      ]
    ],
    [
      "00c3868c",
      "PARAM",
      [
        "storage",
        "01129af0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md#insn-00c37650) · [`00c376d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md#insn-00c376d4) · [`00c37724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md#insn-00c37724)
- 新版 [`00c38644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38600.md#insn-00c38644) · [`00c386c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38600.md#insn-00c386c8) · [`00c38718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38600.md#insn-00c38718)

~~~diff
- 00c37650 ["INT_ADD", "register:40f0:8", ["const:c37650:8", "const:4:8"]]
- 00c37650 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c38644 ["INT_ADD", "register:40f0:8", ["const:c38644:8", "const:4:8"]]
+ 00c38644 ["CALL", null, ["callee:00c5c740:8"]]
- 00c37650 bytes 48900094
+ 00c38644 bytes 3f900094
- 00c376d4 ["INT_ADD", "register:40f0:8", ["const:c376d4:8", "const:4:8"]]
- 00c376d4 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c386c8 ["INT_ADD", "register:40f0:8", ["const:c386c8:8", "const:4:8"]]
+ 00c386c8 ["CALL", null, ["callee:00c5c750:8"]]
- 00c376d4 bytes 2b900094
+ 00c386c8 bytes 22900094
- 00c37724 ["INT_ADD", "register:40f0:8", ["const:c37724:8", "const:4:8"]]
- 00c37724 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c38718 ["INT_ADD", "register:40f0:8", ["const:c38718:8", "const:4:8"]]
+ 00c38718 ["CALL", null, ["callee:00c3909c:8"]]
- 00c37724 bytes 61020094
+ 00c38718 bytes 61020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df3e8cebcca686a6427f18a7b053d4f1"></a>

### [`00c37750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md) → [`00c38744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38744.md) __cxa_guard_release

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)
- 新版 呼出元 1件 [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md) · 呼出先 4件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38768",
      "incomplete_value": false,
      "site": "00c3876c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37774",
      "incomplete_value": false,
      "site": "00c37778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "00c38780",
      "incomplete_value": false,
      "site": "00c38784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3778c",
      "incomplete_value": false,
      "site": "00c37790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "00c38794",
      "incomplete_value": false,
      "site": "00c38798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1129000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c377a0",
      "incomplete_value": false,
      "site": "00c377a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00c38768",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c38780",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c38794",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38768",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c38780",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c38794",
      "PARAM",
      [
        "storage",
        "01129af0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md#insn-00c37778) · [`00c37790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md#insn-00c37790) · [`00c377a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md#insn-00c377a4)
- 新版 [`00c3876c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38744.md#insn-00c3876c) · [`00c38784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38744.md#insn-00c38784) · [`00c38798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38744.md#insn-00c38798)

~~~diff
- 00c37778 ["INT_ADD", "register:40f0:8", ["const:c37778:8", "const:4:8"]]
- 00c37778 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c3876c ["INT_ADD", "register:40f0:8", ["const:c3876c:8", "const:4:8"]]
+ 00c3876c ["CALL", null, ["callee:00c5c740:8"]]
- 00c37778 bytes fe8f0094
+ 00c3876c bytes f58f0094
- 00c37790 ["INT_ADD", "register:40f0:8", ["const:c37790:8", "const:4:8"]]
- 00c37790 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c38784 ["INT_ADD", "register:40f0:8", ["const:c38784:8", "const:4:8"]]
+ 00c38784 ["CALL", null, ["callee:00c5c750:8"]]
- 00c37790 bytes fc8f0094
+ 00c38784 bytes f38f0094
- 00c377a4 ["INT_ADD", "register:40f0:8", ["const:c377a4:8", "const:4:8"]]
- 00c377a4 ["CALL", null, ["callee:00c5f260:8"]]
+ 00c38798 ["INT_ADD", "register:40f0:8", ["const:c38798:8", "const:4:8"]]
+ 00c38798 ["CALL", null, ["callee:00c5f260:8"]]
- 00c377a4 bytes bb9a0094
+ 00c38798 bytes b29a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

