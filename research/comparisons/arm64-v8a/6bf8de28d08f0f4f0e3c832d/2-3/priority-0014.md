# v16.0.2 → v16.0.3 · 最優先の変更候補 (14)

[一覧の目次](README.md)

<a id="compare-3fe3d5a58c55ef58cbe6666e80cc9dd1"></a>

### [`00537598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md) → [`005378b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005378b8.md) FUN_005378b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00536edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`005371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c599d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599d0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005379c8",
      "incomplete_value": true,
      "site": "005379c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005376a8",
      "incomplete_value": true,
      "site": "005376a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005379f4",
      "incomplete_value": true,
      "site": "005379f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005376d4",
      "incomplete_value": true,
      "site": "005376d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
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
      "005379b8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005379e4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005379b8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005379e4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005376a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md#insn-005376a8) · [`005376d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md#insn-005376d4) · [`005375c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md#insn-005375c8)
- 新版 [`005379c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005378b8.md#insn-005379c8) · [`005379f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005378b8.md#insn-005379f4) · [`005378e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005378b8.md#insn-005378e8)

~~~diff
- 005376a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005376a8 ["INT_ADD", "register:40f0:8", ["const:5376a8:8", "const:4:8"]]
- 005376a8 ["CALLIND", null, ["register:0:8"]]
+ 005379c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005379c8 ["INT_ADD", "register:40f0:8", ["const:5379c8:8", "const:4:8"]]
+ 005379c8 ["CALLIND", null, ["register:0:8"]]
- 005376a8 bytes 20013fd6
+ 005379c8 bytes 20013fd6
- 005376d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005376d4 ["INT_ADD", "register:40f0:8", ["const:5376d4:8", "const:4:8"]]
- 005376d4 ["CALLIND", null, ["register:0:8"]]
+ 005379f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005379f4 ["INT_ADD", "register:40f0:8", ["const:5379f4:8", "const:4:8"]]
+ 005379f4 ["CALLIND", null, ["register:0:8"]]
- 005376d4 bytes 20013fd6
+ 005379f4 bytes 20013fd6
- 005375c8 ["INT_ADD", "register:40f0:8", ["const:5375c8:8", "const:4:8"]]
- 005375c8 ["CALL", null, ["callee:00c599d0:8"]]
+ 005378e8 ["INT_ADD", "register:40f0:8", ["const:5378e8:8", "const:4:8"]]
+ 005378e8 ["CALL", null, ["callee:00c599d0:8"]]
- 005375c8 bytes 0e851c94
+ 005378e8 bytes 3a881c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-745be01540a6d730e281e27df894f461"></a>

### [`00537754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537754.md) → [`00537a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537a74.md) FUN_00537a74

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004f5748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5748.md) [`004f5910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5910.md) · 呼出先 8件 [`005379f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379f8.md) [`005379fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379fc.md) [`00537aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aa8.md) [`00537aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`004f5a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f5/004f5a68.md) [`004f5c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f5/004f5c30.md) · 呼出先 8件 [`00537d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d18.md) [`00537d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d1c.md) [`00537dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537dc8.md) [`00537dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537dcc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00537b08",
      "incomplete_value": false,
      "site": "00537b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005377e8",
      "incomplete_value": false,
      "site": "005377e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00537b28",
      "incomplete_value": false,
      "site": "00537b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537808",
      "incomplete_value": false,
      "site": "00537808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00537b08",
      "DATA",
      [
        "storage",
        "00c6a0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00537b28",
      "DATA",
      [
        "storage",
        "00c6a158",
        null,
        "undefined *"
      ]
    ],
    [
      "00537b60",
      "READ",
      [
        "storage",
        "00c6a178",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00537b08",
      "DATA",
      [
        "storage",
        "00c6b098",
        null,
        "undefined *"
      ]
    ],
    [
      "00537b28",
      "DATA",
      [
        "storage",
        "00c6b128",
        null,
        "undefined *"
      ]
    ],
    [
      "00537b60",
      "READ",
      [
        "storage",
        "00c6b148",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537754.md#insn-005377a4) · [`005377b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537754.md#insn-005377b8) · [`005377cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537754.md#insn-005377cc)
- 新版 [`00537ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537a74.md#insn-00537ac4) · [`00537ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537a74.md#insn-00537ad8) · [`00537aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537a74.md#insn-00537aec)

~~~diff
- 005377a4 ["INT_ADD", "register:40f0:8", ["const:5377a4:8", "const:4:8"]]
- 005377a4 ["CALL", null, ["callee:00c5a370:8"]]
+ 00537ac4 ["INT_ADD", "register:40f0:8", ["const:537ac4:8", "const:4:8"]]
+ 00537ac4 ["CALL", null, ["callee:00c5a370:8"]]
- 005377a4 bytes ff861c94
+ 00537ac4 bytes 2b8a1c94
- 005377b8 ["INT_ADD", "register:40f0:8", ["const:5377b8:8", "const:4:8"]]
- 005377b8 ["CALL", null, ["callee:00c5a370:8"]]
+ 00537ad8 ["INT_ADD", "register:40f0:8", ["const:537ad8:8", "const:4:8"]]
+ 00537ad8 ["CALL", null, ["callee:00c5a370:8"]]
- 005377b8 bytes fa861c94
+ 00537ad8 bytes 268a1c94
- 005377cc ["INT_ADD", "register:40f0:8", ["const:5377cc:8", "const:4:8"]]
- 005377cc ["CALL", null, ["callee:00c5a370:8"]]
+ 00537aec ["INT_ADD", "register:40f0:8", ["const:537aec:8", "const:4:8"]]
+ 00537aec ["CALL", null, ["callee:00c5a370:8"]]
- 005377cc bytes f5861c94
+ 00537aec bytes 218a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b88f88e342d01e958cd5ab7677b6801"></a>

### [`005379b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379b0.md) → [`00537cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537cd0.md) FUN_00537cd0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00537cf4",
      "incomplete_value": false,
      "site": "00537cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005379d4",
      "incomplete_value": false,
      "site": "005379d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00537cf4",
      "DATA",
      [
        "storage",
        "00c6a0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537cf4",
      "DATA",
      [
        "storage",
        "00c6b098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005379c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379b0.md#insn-005379c4) · [`005379cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379b0.md#insn-005379cc) · [`005379d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379b0.md#insn-005379d0)
- 新版 [`00537ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537cd0.md#insn-00537ce4) · [`00537cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537cd0.md#insn-00537cec) · [`00537cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537cd0.md#insn-00537cf0)

~~~diff
- 005379c4 ["INT_ADD", "register:40f0:8", ["const:5379c4:8", "const:4:8"]]
- 005379c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00537ce4 ["INT_ADD", "register:40f0:8", ["const:537ce4:8", "const:4:8"]]
+ 00537ce4 ["CALL", null, ["callee:00c58f30:8"]]
- 005379c4 bytes 67811c94
+ 00537ce4 bytes 93841c94
- 005379cc ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00537cec ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 005379cc bytes 883900f0
+ 00537cec bytes a8390090
- 005379d0 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 005379d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005379d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005379d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537cf0 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00537cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005379d0 bytes 08210391
+ 00537cf0 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3af081a3d30281e7e9ae76bc59d60ff1"></a>

### [`005379e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379e4.md) → [`00537d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d04.md) FUN_00537d04

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00537d10",
      "incomplete_value": false,
      "site": "00537d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005379f0",
      "incomplete_value": false,
      "site": "005379f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00537d10",
      "DATA",
      [
        "storage",
        "00c6a0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537d10",
      "DATA",
      [
        "storage",
        "00c6b098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005379e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379e4.md#insn-005379e8) · [`005379ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005379e4.md#insn-005379ec)
- 新版 [`00537d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d04.md#insn-00537d08) · [`00537d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d04.md#insn-00537d0c)

~~~diff
- 005379e8 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00537d08 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005379e8 bytes 893900f0
+ 00537d08 bytes a9390090
- 005379ec ["COPY", "tmp:0:8", ["const:c8:8"]]
- 005379ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005379ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005379ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00537d0c ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00537d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00537d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00537d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005379ec bytes 29210391
+ 00537d0c bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0962fdba66c4e03801bd3574ff15097a"></a>

### [`00537a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a60.md) → [`00537d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d80.md) FUN_00537d80

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00537da4",
      "incomplete_value": false,
      "site": "00537da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537a84",
      "incomplete_value": false,
      "site": "00537a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00537da4",
      "DATA",
      [
        "storage",
        "00c6a158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537da4",
      "DATA",
      [
        "storage",
        "00c6b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a60.md#insn-00537a74) · [`00537a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a60.md#insn-00537a7c) · [`00537a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a60.md#insn-00537a80)
- 新版 [`00537d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d80.md#insn-00537d94) · [`00537d9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d80.md#insn-00537d9c) · [`00537da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537d80.md#insn-00537da0)

~~~diff
- 00537a74 ["INT_ADD", "register:40f0:8", ["const:537a74:8", "const:4:8"]]
- 00537a74 ["CALL", null, ["callee:00c58f30:8"]]
+ 00537d94 ["INT_ADD", "register:40f0:8", ["const:537d94:8", "const:4:8"]]
+ 00537d94 ["CALL", null, ["callee:00c58f30:8"]]
- 00537a74 bytes 3b811c94
+ 00537d94 bytes 67841c94
- 00537a7c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00537d9c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00537a7c bytes 883900f0
+ 00537d9c bytes a8390090
- 00537a80 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00537a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537da0 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 00537da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537a80 bytes 08610591
+ 00537da0 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7569e34c15170e9a3d661b0f6c2dbbbd"></a>

### [`00537a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a94.md) → [`00537db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537db4.md) FUN_00537db4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00537dc0",
      "incomplete_value": false,
      "site": "00537dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537aa0",
      "incomplete_value": false,
      "site": "00537aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00537dc0",
      "DATA",
      [
        "storage",
        "00c6a158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537dc0",
      "DATA",
      [
        "storage",
        "00c6b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a94.md#insn-00537a98) · [`00537a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537a94.md#insn-00537a9c)
- 新版 [`00537db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537db4.md#insn-00537db8) · [`00537dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537db4.md#insn-00537dbc)

~~~diff
- 00537a98 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00537db8 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00537a98 bytes 893900f0
+ 00537db8 bytes a9390090
- 00537a9c ["COPY", "tmp:0:8", ["const:158:8"]]
- 00537a9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00537a9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00537a9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00537dbc ["COPY", "tmp:0:8", ["const:128:8"]]
+ 00537dbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00537dbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00537dbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00537a9c bytes 29610591
+ 00537dbc bytes 29a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-440c1ab1065d12b6cdb0deb883186395"></a>

### [`00537aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md) → [`00537e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md) FUN_00537e0c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00539214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539214.md) [`005392cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005392cc.md) [`005395e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005395e0.md) [`005396ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005396ac.md) · 呼出先 3件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 4件 [`00539534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539534.md) [`005395ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005395ec.md) [`00539900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539900.md) [`005399cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005399cc.md) · 呼出先 3件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00537e44",
      "incomplete_value": true,
      "site": "00537e44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537b24",
      "incomplete_value": true,
      "site": "00537b24",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00537e70",
      "incomplete_value": true,
      "site": "00537e70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537b50",
      "incomplete_value": true,
      "site": "00537b50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
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
      "00537e34",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00537e60",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00537e34",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00537e60",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md#insn-00537b24) · [`00537b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md#insn-00537b50) · [`00537b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md#insn-00537b04)
- 新版 [`00537e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md#insn-00537e44) · [`00537e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md#insn-00537e70) · [`00537e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md#insn-00537e24)

~~~diff
- 00537b24 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537b24 ["INT_ADD", "register:40f0:8", ["const:537b24:8", "const:4:8"]]
- 00537b24 ["CALLIND", null, ["register:0:8"]]
+ 00537e44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00537e44 ["INT_ADD", "register:40f0:8", ["const:537e44:8", "const:4:8"]]
+ 00537e44 ["CALLIND", null, ["register:0:8"]]
- 00537b24 bytes 20013fd6
+ 00537e44 bytes 20013fd6
- 00537b50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537b50 ["INT_ADD", "register:40f0:8", ["const:537b50:8", "const:4:8"]]
- 00537b50 ["CALLIND", null, ["register:0:8"]]
+ 00537e70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00537e70 ["INT_ADD", "register:40f0:8", ["const:537e70:8", "const:4:8"]]
+ 00537e70 ["CALLIND", null, ["register:0:8"]]
- 00537b50 bytes 20013fd6
+ 00537e70 bytes 20013fd6
- 00537b04 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00537e24 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00537b04 bytes 95390090
+ 00537e24 bytes 953900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c37da854d1d52988196886837eee1f"></a>

### [`00537bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md) → [`00537ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md) FUN_00537ef8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0053937c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/0053937c.md) [`005397f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005397f0.md) · 呼出先 19件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00537fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md) [`005390ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005390ec.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`0053969c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053969c.md) [`00539b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539b10.md) · 呼出先 19件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`005382e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md) [`0053940c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053940c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00538024",
      "incomplete_value": true,
      "site": "00538024",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537d04",
      "incomplete_value": true,
      "site": "00537d04",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00538050",
      "incomplete_value": true,
      "site": "00538050",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537d30",
      "incomplete_value": true,
      "site": "00537d30",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00538090",
      "incomplete_value": true,
      "site": "00538090",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537d70",
      "incomplete_value": true,
      "site": "00537d70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00538018",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00538040",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00538080",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00538018",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538040",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538080",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md#insn-00537d04) · [`00537d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md#insn-00537d30) · [`00537d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md#insn-00537d70)
- 新版 [`00538024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md#insn-00538024) · [`00538050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md#insn-00538050) · [`00538090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md#insn-00538090)

~~~diff
- 00537d04 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537d04 ["INT_ADD", "register:40f0:8", ["const:537d04:8", "const:4:8"]]
- 00537d04 ["CALLIND", null, ["register:0:8"]]
+ 00538024 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538024 ["INT_ADD", "register:40f0:8", ["const:538024:8", "const:4:8"]]
+ 00538024 ["CALLIND", null, ["register:0:8"]]
- 00537d04 bytes 20013fd6
+ 00538024 bytes 20013fd6
- 00537d30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537d30 ["INT_ADD", "register:40f0:8", ["const:537d30:8", "const:4:8"]]
- 00537d30 ["CALLIND", null, ["register:0:8"]]
+ 00538050 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538050 ["INT_ADD", "register:40f0:8", ["const:538050:8", "const:4:8"]]
+ 00538050 ["CALLIND", null, ["register:0:8"]]
- 00537d30 bytes 20013fd6
+ 00538050 bytes 20013fd6
- 00537d70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537d70 ["INT_ADD", "register:40f0:8", ["const:537d70:8", "const:4:8"]]
- 00537d70 ["CALLIND", null, ["register:0:8"]]
+ 00538090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538090 ["INT_ADD", "register:40f0:8", ["const:538090:8", "const:4:8"]]
+ 00538090 ["CALLIND", null, ["register:0:8"]]
- 00537d70 bytes 20013fd6
+ 00538090 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be1468a432a6d29076f263dc222ca28c"></a>

### [`00537fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md) → [`005382e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md) FUN_005382e4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md) · 呼出先 6件 [`00538380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md) [`00538630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)
- 新版 呼出元 1件 [`00537ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md) · 呼出先 6件 [`005386a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md) [`00538950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00538364",
      "incomplete_value": true,
      "site": "00538364",
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
      "definition_site": "00538044",
      "incomplete_value": true,
      "site": "00538044",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005383ac",
      "incomplete_value": true,
      "site": "005383b4",
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
      "definition_site": "0053808c",
      "incomplete_value": true,
      "site": "00538094",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00538500",
      "incomplete_value": true,
      "site": "00538500",
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
      "definition_site": "005381e0",
      "incomplete_value": true,
      "site": "005381e0",
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
      "0053835c",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00538364",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053839c",
      "READ",
      [
        "storage",
        "00c9b088",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053835c",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00538364",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053839c",
      "READ",
      [
        "storage",
        "00c9c058",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005380e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md#insn-005380e0) · [`00538128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md#insn-00538128) · [`00538264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md#insn-00538264)
- 新版 [`00538400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md#insn-00538400) · [`00538448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md#insn-00538448) · [`00538584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md#insn-00538584)

~~~diff
- 005380e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005380e0 ["INT_ADD", "register:40f0:8", ["const:5380e0:8", "const:4:8"]]
- 005380e0 ["CALLIND", null, ["register:0:8"]]
+ 00538400 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538400 ["INT_ADD", "register:40f0:8", ["const:538400:8", "const:4:8"]]
+ 00538400 ["CALLIND", null, ["register:0:8"]]
- 005380e0 bytes 20013fd6
+ 00538400 bytes 20013fd6
- 00538128 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538128 ["INT_ADD", "register:40f0:8", ["const:538128:8", "const:4:8"]]
- 00538128 ["CALLIND", null, ["register:0:8"]]
+ 00538448 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538448 ["INT_ADD", "register:40f0:8", ["const:538448:8", "const:4:8"]]
+ 00538448 ["CALLIND", null, ["register:0:8"]]
- 00538128 bytes 20013fd6
+ 00538448 bytes 20013fd6
- 00538264 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538264 ["INT_ADD", "register:40f0:8", ["const:538264:8", "const:4:8"]]
- 00538264 ["CALLIND", null, ["register:0:8"]]
+ 00538584 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538584 ["INT_ADD", "register:40f0:8", ["const:538584:8", "const:4:8"]]
+ 00538584 ["CALLIND", null, ["register:0:8"]]
- 00538264 bytes 20013fd6
+ 00538584 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7522a457a158c99ec374b6eb37d94d9"></a>

### [`00538380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md) → [`005386a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md) FUN_005386a0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md) · 呼出先 11件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`005387ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005387ec.md) [`00538a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538a60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`005382e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md) · 呼出先 11件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00538b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538b0c.md) [`00538d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538d80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005386e4",
      "incomplete_value": false,
      "site": "0053870c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383c4",
      "incomplete_value": false,
      "site": "005383ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "definition_site": "00538718",
      "incomplete_value": true,
      "site": "00538718",
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
      "definition_site": "005383f8",
      "incomplete_value": true,
      "site": "005383f8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00538760",
      "incomplete_value": true,
      "site": "00538768",
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
      "definition_site": "00538440",
      "incomplete_value": true,
      "site": "00538448",
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
      "00538704",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "0053870c",
      "DATA",
      [
        "storage",
        "00c6a1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538718",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00538704",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "0053870c",
      "DATA",
      [
        "storage",
        "00c6b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00538718",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005383b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md#insn-005383b0) · [`005383bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md#insn-005383bc) · [`005383c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md#insn-005383c0)
- 新版 [`005386d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md#insn-005386d0) · [`005386dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md#insn-005386dc) · [`005386e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md#insn-005386e0)

~~~diff
- 005383b0 ["INT_ADD", "register:40f0:8", ["const:5383b0:8", "const:4:8"]]
- 005383b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 005386d0 ["INT_ADD", "register:40f0:8", ["const:5386d0:8", "const:4:8"]]
+ 005386d0 ["CALL", null, ["callee:00c58f30:8"]]
- 005383b0 bytes ec7e1c94
+ 005386d0 bytes 18821c94
- 005383bc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005386dc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005383bc bytes 083b00f0
+ 005386dc bytes 283b0090
- 005383c0 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 005386e0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005383c0 bytes 893900d0
+ 005386e0 bytes 893900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a9fb64d73bb0c578d57ac51c968913"></a>

### [`00538630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md) → [`00538950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md) FUN_00538950

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537fc4.md) · 呼出先 7件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`00538bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538bdc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005382e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005382e4.md) · 呼出先 7件 [`0045aa34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa34.md) [`00538efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538efc.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00538980",
      "incomplete_value": false,
      "site": "005389a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538660",
      "incomplete_value": false,
      "site": "00538688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "definition_site": "005389b4",
      "incomplete_value": true,
      "site": "005389b4",
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
      "definition_site": "00538694",
      "incomplete_value": true,
      "site": "00538694",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00538a00",
      "incomplete_value": true,
      "site": "00538a08",
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
      "definition_site": "005386e0",
      "incomplete_value": true,
      "site": "005386e8",
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
      "005389a0",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "005389a8",
      "DATA",
      [
        "storage",
        "00c6a238",
        null,
        "pointer"
      ]
    ],
    [
      "005389b4",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005389a0",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "005389a8",
      "DATA",
      [
        "storage",
        "00c6b208",
        null,
        "pointer"
      ]
    ],
    [
      "005389b4",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053864c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md#insn-0053864c) · [`00538658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md#insn-00538658) · [`0053865c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md#insn-0053865c)
- 新版 [`0053896c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md#insn-0053896c) · [`00538978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md#insn-00538978) · [`0053897c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md#insn-0053897c)

~~~diff
- 0053864c ["INT_ADD", "register:40f0:8", ["const:53864c:8", "const:4:8"]]
- 0053864c ["CALL", null, ["callee:00c58f30:8"]]
+ 0053896c ["INT_ADD", "register:40f0:8", ["const:53896c:8", "const:4:8"]]
+ 0053896c ["CALL", null, ["callee:00c58f30:8"]]
- 0053864c bytes 457e1c94
+ 0053896c bytes 71811c94
- 00538658 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00538978 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00538658 bytes 083b00f0
+ 00538978 bytes 283b0090
- 0053865c ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 0053897c ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 0053865c bytes 893900d0
+ 0053897c bytes 893900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-695c6820e8d0e1fc4f1d9be90a708429"></a>

### [`005387ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005387ec.md) → [`00538b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538b0c.md) FUN_00538b0c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00538380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md) · 呼出先 6件 [`00538d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538d58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) [`00c581e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581e0.md)
- 新版 呼出元 1件 [`005386a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/005386a0.md) · 呼出先 6件 [`00539078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539078.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c591a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591a0.md) [`00c591b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c591b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

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
      "definition_site": "00538b78",
      "incomplete_value": false,
      "site": "00538b84",
      "value": [
        "leaf",
        "const:539078:8"
      ]
    },
    "old": {
      "definition_site": "00538858",
      "incomplete_value": false,
      "site": "00538864",
      "value": [
        "leaf",
        "const:538d58:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00538bc8",
      "incomplete_value": false,
      "site": "00538bcc",
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
            "const:fa5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005388a8",
      "incomplete_value": false,
      "site": "005388ac",
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
            "const:eda:8"
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
      "00538b78",
      "PARAM",
      [
        "storage",
        "00538d58",
        null,
        null
      ]
    ],
    [
      "00538bc8",
      "PARAM",
      [
        "storage",
        "002a3eda",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00538b78",
      "PARAM",
      [
        "storage",
        "00539078",
        null,
        null
      ]
    ],
    [
      "00538bc8",
      "PARAM",
      [
        "storage",
        "002a3fa5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005387ec.md#insn-00538864) · [`005388ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005387ec.md#insn-005388ac) · [`00538820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005387ec.md#insn-00538820)
- 新版 [`00538b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538b0c.md#insn-00538b84) · [`00538bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538b0c.md#insn-00538bcc) · [`00538b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538b0c.md#insn-00538b40)

~~~diff
- 00538864 ["INT_ADD", "register:40f0:8", ["const:538864:8", "const:4:8"]]
- 00538864 ["CALL", null, ["callee:00c591b0:8"]]
+ 00538b84 ["INT_ADD", "register:40f0:8", ["const:538b84:8", "const:4:8"]]
+ 00538b84 ["CALL", null, ["callee:00c591b0:8"]]
- 00538864 bytes 5f7e1c94
+ 00538b84 bytes 8b811c94
- 005388ac ["INT_ADD", "register:40f0:8", ["const:5388ac:8", "const:4:8"]]
- 005388ac ["CALL", null, ["callee:00c591c0:8"]]
+ 00538bcc ["INT_ADD", "register:40f0:8", ["const:538bcc:8", "const:4:8"]]
+ 00538bcc ["CALL", null, ["callee:00c591c0:8"]]
- 005388ac bytes 517e1c94
+ 00538bcc bytes 7d811c94
- 00538820 ["INT_ADD", "register:40f0:8", ["const:538820:8", "const:4:8"]]
- 00538820 ["CALL", null, ["callee:00c58f30:8"]]
+ 00538b40 ["INT_ADD", "register:40f0:8", ["const:538b40:8", "const:4:8"]]
+ 00538b40 ["CALL", null, ["callee:00c58f30:8"]]
- 00538820 bytes d07d1c94
+ 00538b40 bytes fc801c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4beed374bd47acaa6354aae67911e44b"></a>

### [`005388f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005388f8.md) → [`00538c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538c18.md) FUN_00538c18

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00538c30",
      "incomplete_value": false,
      "site": "00538c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538910",
      "incomplete_value": false,
      "site": "00538914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "definition_site": "00538c74",
      "incomplete_value": true,
      "site": "00538c74",
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
      "definition_site": "00538954",
      "incomplete_value": true,
      "site": "00538954",
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
      "definition_site": "00538c9c",
      "incomplete_value": true,
      "site": "00538c9c",
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
      "definition_site": "0053897c",
      "incomplete_value": true,
      "site": "0053897c",
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
      "00538c34",
      "DATA",
      [
        "storage",
        "00c6a1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538c48",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00538c68",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00538c34",
      "DATA",
      [
        "storage",
        "00c6b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00538c48",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538c68",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005388f8.md#insn-00538938) · [`0053890c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005388f8.md#insn-0053890c) · [`00538910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005388f8.md#insn-00538910)
- 新版 [`00538c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538c18.md#insn-00538c58) · [`00538c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538c18.md#insn-00538c2c) · [`00538c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538c18.md#insn-00538c30)

~~~diff
- 00538938 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538938 ["INT_ADD", "register:40f0:8", ["const:538938:8", "const:4:8"]]
- 00538938 ["CALLIND", null, ["register:0:8"]]
+ 00538c58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538c58 ["INT_ADD", "register:40f0:8", ["const:538c58:8", "const:4:8"]]
+ 00538c58 ["CALLIND", null, ["register:0:8"]]
- 00538938 bytes 20013fd6
+ 00538c58 bytes 20013fd6
- 0053890c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00538c2c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0053890c bytes 883900d0
+ 00538c2c bytes 883900f0
- 00538910 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00538910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00538910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00538910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00538c30 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00538c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00538c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00538c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00538910 bytes 08610791
+ 00538c30 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae610c7c08aef5df4ee5d1c5c119e54e"></a>

### [`005389a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005389a8.md) → [`00538cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538cc8.md) FUN_00538cc8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00538ce0",
      "incomplete_value": false,
      "site": "00538ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005389c0",
      "incomplete_value": false,
      "site": "005389c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "definition_site": "00538d24",
      "incomplete_value": true,
      "site": "00538d24",
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
      "definition_site": "00538a04",
      "incomplete_value": true,
      "site": "00538a04",
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
      "definition_site": "00538d4c",
      "incomplete_value": true,
      "site": "00538d4c",
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
      "definition_site": "00538a2c",
      "incomplete_value": true,
      "site": "00538a2c",
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
      "00538ce4",
      "DATA",
      [
        "storage",
        "00c6a1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538cf8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00538d18",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00538ce4",
      "DATA",
      [
        "storage",
        "00c6b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "00538cf8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00538d18",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005389e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005389a8.md#insn-005389e8) · [`005389bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005389a8.md#insn-005389bc) · [`005389c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/005389a8.md#insn-005389c0)
- 新版 [`00538d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538cc8.md#insn-00538d08) · [`00538cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538cc8.md#insn-00538cdc) · [`00538ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538cc8.md#insn-00538ce0)

~~~diff
- 005389e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005389e8 ["INT_ADD", "register:40f0:8", ["const:5389e8:8", "const:4:8"]]
- 005389e8 ["CALLIND", null, ["register:0:8"]]
+ 00538d08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538d08 ["INT_ADD", "register:40f0:8", ["const:538d08:8", "const:4:8"]]
+ 00538d08 ["CALLIND", null, ["register:0:8"]]
- 005389e8 bytes 20013fd6
+ 00538d08 bytes 20013fd6
- 005389bc ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00538cdc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 005389bc bytes 883900d0
+ 00538cdc bytes 883900f0
- 005389c0 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 005389c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005389c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005389c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00538ce0 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00538ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00538ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00538ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005389c0 bytes 08610791
+ 00538ce0 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41745f843b016720db0727411ce29089"></a>

### [`00538bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538bdc.md) → [`00538efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538efc.md) FUN_00538efc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00538630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00538950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538950.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00538f38",
      "incomplete_value": true,
      "site": "00538f38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538c18",
      "incomplete_value": true,
      "site": "00538c18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
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
      "00538f28",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00538f28",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538bdc.md#insn-00538c18) · [`00538c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538bdc.md#insn-00538c00) · [`00538c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538bdc.md#insn-00538c08)
- 新版 [`00538f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538efc.md#insn-00538f38) · [`00538f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538efc.md#insn-00538f20) · [`00538f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00538/00538efc.md#insn-00538f28)

~~~diff
- 00538c18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538c18 ["INT_ADD", "register:40f0:8", ["const:538c18:8", "const:4:8"]]
- 00538c18 ["CALLIND", null, ["register:0:8"]]
+ 00538f38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00538f38 ["INT_ADD", "register:40f0:8", ["const:538f38:8", "const:4:8"]]
+ 00538f38 ["CALLIND", null, ["register:0:8"]]
- 00538c18 bytes 20013fd6
+ 00538f38 bytes 20013fd6
- 00538c00 ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 00538f20 ["COPY", "register:4048:8", ["const:c68000:8"]]
- 00538c00 bytes 693900f0
+ 00538f20 bytes 89390090
- 00538c08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
- 00538c08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00538f28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d8:8"]]
+ 00538f28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00538c08 bytes 290544f9
+ 00538f28 bytes 29ed43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3acc0bc4d873778a3aaa27bcb27eaa35"></a>

### [`00538e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538e74.md) → [`00539194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539194.md) FUN_00539194

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005391ac",
      "incomplete_value": false,
      "site": "005391b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538e8c",
      "incomplete_value": false,
      "site": "00538e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "definition_site": "005391f0",
      "incomplete_value": true,
      "site": "005391f0",
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
      "definition_site": "00538ed0",
      "incomplete_value": true,
      "site": "00538ed0",
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
      "definition_site": "00539218",
      "incomplete_value": true,
      "site": "00539218",
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
      "definition_site": "00538ef8",
      "incomplete_value": true,
      "site": "00538ef8",
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
      "005391b0",
      "DATA",
      [
        "storage",
        "00c6a238",
        null,
        "pointer"
      ]
    ],
    [
      "005391c4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005391e4",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005391b0",
      "DATA",
      [
        "storage",
        "00c6b208",
        null,
        "pointer"
      ]
    ],
    [
      "005391c4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005391e4",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538e74.md#insn-00538eb4) · [`00538e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538e74.md#insn-00538e88) · [`00538e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538e74.md#insn-00538e8c)
- 新版 [`005391d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539194.md#insn-005391d4) · [`005391a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539194.md#insn-005391a8) · [`005391ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539194.md#insn-005391ac)

~~~diff
- 00538eb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538eb4 ["INT_ADD", "register:40f0:8", ["const:538eb4:8", "const:4:8"]]
- 00538eb4 ["CALLIND", null, ["register:0:8"]]
+ 005391d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005391d4 ["INT_ADD", "register:40f0:8", ["const:5391d4:8", "const:4:8"]]
+ 005391d4 ["CALLIND", null, ["register:0:8"]]
- 00538eb4 bytes 20013fd6
+ 005391d4 bytes 20013fd6
- 00538e88 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 005391a8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00538e88 bytes 883900d0
+ 005391a8 bytes 883900d0
- 00538e8c ["COPY", "tmp:0:8", ["const:238:8"]]
- 00538e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00538e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00538e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005391ac ["COPY", "tmp:0:8", ["const:208:8"]]
+ 005391ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005391ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005391ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00538e8c bytes 08e10891
+ 005391ac bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ba3757fbc9e2f26d6e60ca464af4b9"></a>

### [`00538f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538f24.md) → [`00539244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539244.md) FUN_00539244

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053925c",
      "incomplete_value": false,
      "site": "00539260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538f3c",
      "incomplete_value": false,
      "site": "00538f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "definition_site": "005392a0",
      "incomplete_value": true,
      "site": "005392a0",
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
      "definition_site": "00538f80",
      "incomplete_value": true,
      "site": "00538f80",
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
      "definition_site": "005392c8",
      "incomplete_value": true,
      "site": "005392c8",
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
      "definition_site": "00538fa8",
      "incomplete_value": true,
      "site": "00538fa8",
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
      "00539260",
      "DATA",
      [
        "storage",
        "00c6a238",
        null,
        "pointer"
      ]
    ],
    [
      "00539274",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00539294",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00539260",
      "DATA",
      [
        "storage",
        "00c6b208",
        null,
        "pointer"
      ]
    ],
    [
      "00539274",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00539294",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538f24.md#insn-00538f64) · [`00538f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538f24.md#insn-00538f38) · [`00538f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538f24.md#insn-00538f3c)
- 新版 [`00539284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539244.md#insn-00539284) · [`00539258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539244.md#insn-00539258) · [`0053925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539244.md#insn-0053925c)

~~~diff
- 00538f64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00538f64 ["INT_ADD", "register:40f0:8", ["const:538f64:8", "const:4:8"]]
- 00538f64 ["CALLIND", null, ["register:0:8"]]
+ 00539284 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539284 ["INT_ADD", "register:40f0:8", ["const:539284:8", "const:4:8"]]
+ 00539284 ["CALLIND", null, ["register:0:8"]]
- 00538f64 bytes 20013fd6
+ 00539284 bytes 20013fd6
- 00538f38 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00539258 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00538f38 bytes 883900d0
+ 00539258 bytes 883900d0
- 00538f3c ["COPY", "tmp:0:8", ["const:238:8"]]
- 00538f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00538f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00538f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053925c ["COPY", "tmp:0:8", ["const:208:8"]]
+ 0053925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00538f3c bytes 08e10891
+ 0053925c bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf65d1ec48d791440d23a61eb092a90"></a>

### [`00539214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539214.md) → [`00539534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539534.md) FUN_00539534

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00537aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00537e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "00539568",
      "incomplete_value": true,
      "site": "00539568",
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
      "definition_site": "00539248",
      "incomplete_value": true,
      "site": "00539248",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005395bc",
      "incomplete_value": false,
      "site": "005395bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053929c",
      "incomplete_value": false,
      "site": "0053929c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "0053955c",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00539568",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539580",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "0053955c",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00539568",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539580",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053922c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539214.md#insn-0053922c) · [`00539234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539214.md#insn-00539234) · [`00539238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539214.md#insn-00539238)
- 新版 [`0053954c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539534.md#insn-0053954c) · [`00539554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539534.md#insn-00539554) · [`00539558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539534.md#insn-00539558)

~~~diff
- 0053922c ["INT_ADD", "register:40f0:8", ["const:53922c:8", "const:4:8"]]
- 0053922c ["CALL", null, ["callee:00537e0c:8"]]
+ 0053954c ["INT_ADD", "register:40f0:8", ["const:53954c:8", "const:4:8"]]
+ 0053954c ["CALL", null, ["callee:00537e0c:8"]]
- 0053922c bytes 30faff97
+ 0053954c bytes 30faff97
- 00539234 ["INT_ADD", "register:40f0:8", ["const:539234:8", "const:4:8"]]
- 00539234 ["CALL", null, ["callee:004dea48:8"]]
+ 00539554 ["INT_ADD", "register:40f0:8", ["const:539554:8", "const:4:8"]]
+ 00539554 ["CALL", null, ["callee:004dea48:8"]]
- 00539234 bytes 3d95fe97
+ 00539554 bytes 3d95fe97
- 00539238 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00539558 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00539238 bytes 143b00d0
+ 00539558 bytes 143b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a290a437ece88c5168e815ada98eca"></a>

### [`005392cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005392cc.md) → [`005395ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005395ec.md) FUN_005395ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00537aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00537e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00539620",
      "incomplete_value": true,
      "site": "00539620",
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
      "definition_site": "00539300",
      "incomplete_value": true,
      "site": "00539300",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539354",
      "incomplete_value": false,
      "site": "00539354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00539614",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00539620",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539638",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00539614",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00539620",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539638",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005392e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005392cc.md#insn-005392e4) · [`005392ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005392cc.md#insn-005392ec) · [`005392f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005392cc.md#insn-005392f0)
- 新版 [`00539604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005395ec.md#insn-00539604) · [`0053960c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005395ec.md#insn-0053960c) · [`00539610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005395ec.md#insn-00539610)

~~~diff
- 005392e4 ["INT_ADD", "register:40f0:8", ["const:5392e4:8", "const:4:8"]]
- 005392e4 ["CALL", null, ["callee:00537e0c:8"]]
+ 00539604 ["INT_ADD", "register:40f0:8", ["const:539604:8", "const:4:8"]]
+ 00539604 ["CALL", null, ["callee:00537e0c:8"]]
- 005392e4 bytes 02faff97
+ 00539604 bytes 02faff97
- 005392ec ["INT_ADD", "register:40f0:8", ["const:5392ec:8", "const:4:8"]]
- 005392ec ["CALL", null, ["callee:004dea48:8"]]
+ 0053960c ["INT_ADD", "register:40f0:8", ["const:53960c:8", "const:4:8"]]
+ 0053960c ["CALL", null, ["callee:004dea48:8"]]
- 005392ec bytes 0f95fe97
+ 0053960c bytes 0f95fe97
- 005392f0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00539610 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 005392f0 bytes 143b00d0
+ 00539610 bytes 143b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9501f1e8b0934c002a4ccef42b5c51e"></a>

### [`0053937c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/0053937c.md) → [`0053969c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053969c.md) FUN_0053969c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00537bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00537ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.25% / 新版 92.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005397dc",
      "incomplete_value": true,
      "site": "005397dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005394bc",
      "incomplete_value": true,
      "site": "005394bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00539808",
      "incomplete_value": true,
      "site": "00539808",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005394e8",
      "incomplete_value": true,
      "site": "005394e8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00539834",
      "incomplete_value": true,
      "site": "00539834",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539514",
      "incomplete_value": true,
      "site": "00539514",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005397cc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005397f8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00539824",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005397cc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005397f8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00539824",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005394bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/0053937c.md#insn-005394bc) · [`005394e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/0053937c.md#insn-005394e8) · [`00539514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/0053937c.md#insn-00539514)
- 新版 [`005397dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053969c.md#insn-005397dc) · [`00539808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053969c.md#insn-00539808) · [`00539834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/0053969c.md#insn-00539834)

~~~diff
- 005394bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005394bc ["INT_ADD", "register:40f0:8", ["const:5394bc:8", "const:4:8"]]
- 005394bc ["CALLIND", null, ["register:0:8"]]
+ 005397dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005397dc ["INT_ADD", "register:40f0:8", ["const:5397dc:8", "const:4:8"]]
+ 005397dc ["CALLIND", null, ["register:0:8"]]
- 005394bc bytes 20013fd6
+ 005397dc bytes 20013fd6
- 005394e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005394e8 ["INT_ADD", "register:40f0:8", ["const:5394e8:8", "const:4:8"]]
- 005394e8 ["CALLIND", null, ["register:0:8"]]
+ 00539808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539808 ["INT_ADD", "register:40f0:8", ["const:539808:8", "const:4:8"]]
+ 00539808 ["CALLIND", null, ["register:0:8"]]
- 005394e8 bytes 20013fd6
+ 00539808 bytes 20013fd6
- 00539514 ["COPY", "register:0:8", ["register:4048:8"]]
- 00539514 ["INT_ADD", "register:40f0:8", ["const:539514:8", "const:4:8"]]
- 00539514 ["CALLIND", null, ["register:0:8"]]
+ 00539834 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539834 ["INT_ADD", "register:40f0:8", ["const:539834:8", "const:4:8"]]
+ 00539834 ["CALLIND", null, ["register:0:8"]]
- 00539514 bytes 20013fd6
+ 00539834 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b13495a9e351c683d25dbd9c8d4de7"></a>

### [`005395e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005395e0.md) → [`00539900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539900.md) FUN_00539900

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00537aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00537e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "00539934",
      "incomplete_value": true,
      "site": "00539934",
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
      "definition_site": "00539614",
      "incomplete_value": true,
      "site": "00539614",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539984",
      "incomplete_value": false,
      "site": "00539988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539664",
      "incomplete_value": false,
      "site": "00539668",
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
            "const:f38:8"
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
      "00539928",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00539934",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053994c",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00539928",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00539934",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053994c",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005395f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005395e0.md#insn-005395f8) · [`00539600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005395e0.md#insn-00539600) · [`00539604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005395e0.md#insn-00539604)
- 新版 [`00539918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539900.md#insn-00539918) · [`00539920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539900.md#insn-00539920) · [`00539924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539900.md#insn-00539924)

~~~diff
- 005395f8 ["INT_ADD", "register:40f0:8", ["const:5395f8:8", "const:4:8"]]
- 005395f8 ["CALL", null, ["callee:00537e0c:8"]]
+ 00539918 ["INT_ADD", "register:40f0:8", ["const:539918:8", "const:4:8"]]
+ 00539918 ["CALL", null, ["callee:00537e0c:8"]]
- 005395f8 bytes 3df9ff97
+ 00539918 bytes 3df9ff97
- 00539600 ["INT_ADD", "register:40f0:8", ["const:539600:8", "const:4:8"]]
- 00539600 ["CALL", null, ["callee:004dea48:8"]]
+ 00539920 ["INT_ADD", "register:40f0:8", ["const:539920:8", "const:4:8"]]
+ 00539920 ["CALL", null, ["callee:004dea48:8"]]
- 00539600 bytes 4a94fe97
+ 00539920 bytes 4a94fe97
- 00539604 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 00539924 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 00539604 bytes 143b00d0
+ 00539924 bytes 143b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-543faef07cfbf11d2874e46a1fd00770"></a>

### [`005396ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005396ac.md) → [`005399cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005399cc.md) FUN_005399cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00537aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537aec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00537e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537e0c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

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
      "definition_site": "00539a00",
      "incomplete_value": true,
      "site": "00539a00",
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
      "definition_site": "005396e0",
      "incomplete_value": true,
      "site": "005396e0",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539a50",
      "incomplete_value": false,
      "site": "00539a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539730",
      "incomplete_value": false,
      "site": "00539734",
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
            "const:f38:8"
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
      "005399f4",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00539a00",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539a18",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "005399f4",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00539a00",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00539a18",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005396c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005396ac.md#insn-005396c4) · [`005396cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005396ac.md#insn-005396cc) · [`005396d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005396ac.md#insn-005396d0)
- 新版 [`005399e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005399cc.md#insn-005399e4) · [`005399ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005399cc.md#insn-005399ec) · [`005399f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/005399cc.md#insn-005399f0)

~~~diff
- 005396c4 ["INT_ADD", "register:40f0:8", ["const:5396c4:8", "const:4:8"]]
- 005396c4 ["CALL", null, ["callee:00537e0c:8"]]
+ 005399e4 ["INT_ADD", "register:40f0:8", ["const:5399e4:8", "const:4:8"]]
+ 005399e4 ["CALL", null, ["callee:00537e0c:8"]]
- 005396c4 bytes 0af9ff97
+ 005399e4 bytes 0af9ff97
- 005396cc ["INT_ADD", "register:40f0:8", ["const:5396cc:8", "const:4:8"]]
- 005396cc ["CALL", null, ["callee:004dea48:8"]]
+ 005399ec ["INT_ADD", "register:40f0:8", ["const:5399ec:8", "const:4:8"]]
+ 005399ec ["CALL", null, ["callee:004dea48:8"]]
- 005396cc bytes 1794fe97
+ 005399ec bytes 1794fe97
- 005396d0 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 005399f0 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 005396d0 bytes 143b00d0
+ 005399f0 bytes 143b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7b11d43b9b821683016e17076f512d"></a>

### [`005397f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005397f0.md) → [`00539b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539b10.md) FUN_00539b10

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00537bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537bd8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00537ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537ef8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.25% / 新版 92.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00539c50",
      "incomplete_value": true,
      "site": "00539c50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539930",
      "incomplete_value": true,
      "site": "00539930",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00539c7c",
      "incomplete_value": true,
      "site": "00539c7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053995c",
      "incomplete_value": true,
      "site": "0053995c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00539ca8",
      "incomplete_value": true,
      "site": "00539ca8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539988",
      "incomplete_value": true,
      "site": "00539988",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00539c40",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00539c6c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00539c98",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00539c40",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00539c6c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00539c98",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005397f0.md#insn-00539930) · [`0053995c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005397f0.md#insn-0053995c) · [`00539988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/005397f0.md#insn-00539988)
- 新版 [`00539c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539b10.md#insn-00539c50) · [`00539c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539b10.md#insn-00539c7c) · [`00539ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539b10.md#insn-00539ca8)

~~~diff
- 00539930 ["COPY", "register:0:8", ["register:4048:8"]]
- 00539930 ["INT_ADD", "register:40f0:8", ["const:539930:8", "const:4:8"]]
- 00539930 ["CALLIND", null, ["register:0:8"]]
+ 00539c50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539c50 ["INT_ADD", "register:40f0:8", ["const:539c50:8", "const:4:8"]]
+ 00539c50 ["CALLIND", null, ["register:0:8"]]
- 00539930 bytes 20013fd6
+ 00539c50 bytes 20013fd6
- 0053995c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053995c ["INT_ADD", "register:40f0:8", ["const:53995c:8", "const:4:8"]]
- 0053995c ["CALLIND", null, ["register:0:8"]]
+ 00539c7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539c7c ["INT_ADD", "register:40f0:8", ["const:539c7c:8", "const:4:8"]]
+ 00539c7c ["CALLIND", null, ["register:0:8"]]
- 0053995c bytes 20013fd6
+ 00539c7c bytes 20013fd6
- 00539988 ["COPY", "register:0:8", ["register:4048:8"]]
- 00539988 ["INT_ADD", "register:40f0:8", ["const:539988:8", "const:4:8"]]
- 00539988 ["CALLIND", null, ["register:0:8"]]
+ 00539ca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00539ca8 ["INT_ADD", "register:40f0:8", ["const:539ca8:8", "const:4:8"]]
+ 00539ca8 ["CALLIND", null, ["register:0:8"]]
- 00539988 bytes 20013fd6
+ 00539ca8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db13b3dddf617e0d7510c08664795e0"></a>

### [`00539a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539a80.md) → [`00539da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539da0.md) FUN_00539da0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00539e44",
      "incomplete_value": false,
      "site": "00539e4c",
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
            "const:9ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b24",
      "incomplete_value": false,
      "site": "00539b2c",
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
            "const:8a7:8"
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
      "definition_site": "00539e7c",
      "incomplete_value": true,
      "site": "00539e88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b5c",
      "incomplete_value": true,
      "site": "00539b68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00539e78",
      "incomplete_value": false,
      "site": "00539e88",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00539b58",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00539e44",
      "PARAM",
      [
        "storage",
        "002a78a7",
        null,
        "string"
      ]
    ],
    [
      "00539e78",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00539e7c",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00539e44",
      "PARAM",
      [
        "storage",
        "002a79ff",
        null,
        "string"
      ]
    ],
    [
      "00539e78",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00539e7c",
      "READ",
      [
        "storage",
        "00c9be28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539a80.md#insn-00539b2c) · [`00539b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539a80.md#insn-00539b68) · [`00539ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539a80.md#insn-00539ba0)
- 新版 [`00539e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539da0.md#insn-00539e4c) · [`00539e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539da0.md#insn-00539e88) · [`00539ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539da0.md#insn-00539ec0)

~~~diff
- 00539b2c ["INT_ADD", "register:40f0:8", ["const:539b2c:8", "const:4:8"]]
- 00539b2c ["CALL", null, ["callee:0043e138:8"]]
+ 00539e4c ["INT_ADD", "register:40f0:8", ["const:539e4c:8", "const:4:8"]]
+ 00539e4c ["CALL", null, ["callee:0043e138:8"]]
- 00539b2c bytes bb10fc97
+ 00539e4c bytes bb10fc97
- 00539b68 ["INT_ADD", "register:40f0:8", ["const:539b68:8", "const:4:8"]]
- 00539b68 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00539e88 ["INT_ADD", "register:40f0:8", ["const:539e88:8", "const:4:8"]]
+ 00539e88 ["CALL", null, ["callee:00c58fb0:8"]]
- 00539b68 bytes 1e791c94
+ 00539e88 bytes 4a7c1c94
- 00539ba0 ["INT_ADD", "register:40f0:8", ["const:539ba0:8", "const:4:8"]]
- 00539ba0 ["CALL", null, ["callee:00c59000:8"]]
+ 00539ec0 ["INT_ADD", "register:40f0:8", ["const:539ec0:8", "const:4:8"]]
+ 00539ec0 ["CALL", null, ["callee:00c59000:8"]]
- 00539ba0 bytes 24791c94
+ 00539ec0 bytes 507c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dab4bf8f6dc073715d2c58c239c1be25"></a>

### [`00539c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539c90.md) → [`00539fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539fb0.md) FUN_00539fb0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c58ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

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
      "definition_site": "0053a070",
      "incomplete_value": false,
      "site": "0053a07c",
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
            "const:95c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539d50",
      "incomplete_value": false,
      "site": "00539d5c",
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
            "const:88f:8"
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
      "definition_site": "0053a0c4",
      "incomplete_value": true,
      "site": "0053a0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539da4",
      "incomplete_value": true,
      "site": "00539db0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "definition_site": "0053a0c0",
      "incomplete_value": false,
      "site": "0053a0d0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00539da0",
      "incomplete_value": false,
      "site": "00539db0",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0053a070",
      "PARAM",
      [
        "storage",
        "002ac88f",
        null,
        "string"
      ]
    ],
    [
      "0053a0c0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0053a0c4",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053a070",
      "PARAM",
      [
        "storage",
        "002ac95c",
        null,
        "string"
      ]
    ],
    [
      "0053a0c0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0053a0c4",
      "READ",
      [
        "storage",
        "00c9be28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539c90.md#insn-00539d5c) · [`00539db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539c90.md#insn-00539db0) · [`00539ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539c90.md#insn-00539ce0)
- 新版 [`0053a07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539fb0.md#insn-0053a07c) · [`0053a0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539fb0.md#insn-0053a0d0) · [`0053a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00539/00539fb0.md#insn-0053a000)

~~~diff
- 00539d5c ["INT_ADD", "register:40f0:8", ["const:539d5c:8", "const:4:8"]]
- 00539d5c ["CALL", null, ["callee:00c59000:8"]]
+ 0053a07c ["INT_ADD", "register:40f0:8", ["const:53a07c:8", "const:4:8"]]
+ 0053a07c ["CALL", null, ["callee:00c59000:8"]]
- 00539d5c bytes b5781c94
+ 0053a07c bytes e17b1c94
- 00539db0 ["INT_ADD", "register:40f0:8", ["const:539db0:8", "const:4:8"]]
- 00539db0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053a0d0 ["INT_ADD", "register:40f0:8", ["const:53a0d0:8", "const:4:8"]]
+ 0053a0d0 ["CALL", null, ["callee:00c58fb0:8"]]
- 00539db0 bytes 8c781c94
+ 0053a0d0 bytes b87b1c94
- 00539ce0 ["INT_ADD", "register:40f0:8", ["const:539ce0:8", "const:4:8"]]
- 00539ce0 ["CALL", null, ["callee:00c5b050:8"]]
+ 0053a000 ["INT_ADD", "register:40f0:8", ["const:53a000:8", "const:4:8"]]
+ 0053a000 ["CALL", null, ["callee:00c5b050:8"]]
- 00539ce0 bytes e8801c94
+ 0053a000 bytes 14841c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb931ded9be377ad1d5b9eb08b9b4f5"></a>

### [`00539e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e28.md) → [`0053a148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a148.md) FUN_0053a148

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0053a16c",
      "incomplete_value": true,
      "site": "0053a16c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539e4c",
      "incomplete_value": true,
      "site": "00539e4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc9:8"
              ]
            ]
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
      "0053a15c",
      "READ",
      [
        "storage",
        "002b8dc9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053a15c",
      "READ",
      [
        "storage",
        "002b8e98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e28.md#insn-00539e30)
- 新版 [`0053a150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a148.md#insn-0053a150)

~~~diff
- 00539e30 ["COPY", "tmp:0:8", ["const:dc9:8"]]
- 00539e30 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00539e30 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00539e30 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053a150 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0053a150 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053a150 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053a150 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00539e30 bytes 4a253791
+ 0053a150 bytes 4a613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbd9b73a0e21333367f31c09a9885a6e"></a>

### [`00539e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e60.md) → [`0053a180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a180.md) FUN_0053a180

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59380.md)

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
      "definition_site": "0053a19c",
      "incomplete_value": true,
      "site": "0053a1a0",
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
      "definition_site": "00539e7c",
      "incomplete_value": true,
      "site": "00539e80",
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
      "0053a194",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "0053a1a0",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053a194",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "0053a1a0",
      "DATA",
      [
        "storage",
        "00c684c8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e60.md#insn-00539e6c) · [`00539e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e60.md#insn-00539e74) · [`00539e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00539/00539e60.md#insn-00539e8c)
- 新版 [`0053a18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a180.md#insn-0053a18c) · [`0053a194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a180.md#insn-0053a194) · [`0053a1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053a180.md#insn-0053a1ac)

~~~diff
- 00539e6c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053a18c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00539e6c bytes 083b00b0
+ 0053a18c bytes 083b00b0
- 00539e74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00539e74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053a194 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053a194 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00539e74 bytes 085147f9
+ 0053a194 bytes 083947f9
- 00539e8c ["INT_ADD", "register:40f0:8", ["const:539e8c:8", "const:4:8"]]
- 00539e8c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053a1ac ["INT_ADD", "register:40f0:8", ["const:53a1ac:8", "const:4:8"]]
+ 0053a1ac ["CALL", null, ["callee:00c58f50:8"]]
- 00539e8c bytes 3d781c94
+ 0053a1ac bytes 697b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40f877f78bde8ea16dd37235eeb0c13b"></a>

### [`0053aa5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa5c.md) → [`0053ad7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ad7c.md) FUN_0053ad7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0053ada0",
      "incomplete_value": false,
      "site": "0053ada0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053aa80",
      "incomplete_value": false,
      "site": "0053aa80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "0053ada0",
      "DATA",
      [
        "storage",
        "00c6a418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053ada0",
      "DATA",
      [
        "storage",
        "00c6b3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053aa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa5c.md#insn-0053aa70) · [`0053aa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa5c.md#insn-0053aa78) · [`0053aa7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa5c.md#insn-0053aa7c)
- 新版 [`0053ad90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ad7c.md#insn-0053ad90) · [`0053ad98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ad7c.md#insn-0053ad98) · [`0053ad9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ad7c.md#insn-0053ad9c)

~~~diff
- 0053aa70 ["INT_ADD", "register:40f0:8", ["const:53aa70:8", "const:4:8"]]
- 0053aa70 ["CALL", null, ["callee:00c58f30:8"]]
+ 0053ad90 ["INT_ADD", "register:40f0:8", ["const:53ad90:8", "const:4:8"]]
+ 0053ad90 ["CALL", null, ["callee:00c58f30:8"]]
- 0053aa70 bytes 3c751c94
+ 0053ad90 bytes 68781c94
- 0053aa78 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0053ad98 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0053aa78 bytes 88390090
+ 0053ad98 bytes 883900b0
- 0053aa7c ["COPY", "tmp:0:8", ["const:418:8"]]
- 0053aa7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053aa7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053aa7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ad9c ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0053ad9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ad9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ad9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053aa7c bytes 08611091
+ 0053ad9c bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea06be173ec3f50cfd232e602b97797"></a>

### [`0053aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa90.md) → [`0053adb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053adb0.md) FUN_0053adb0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0053adbc",
      "incomplete_value": false,
      "site": "0053adbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053aa9c",
      "incomplete_value": false,
      "site": "0053aa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
      "0053adbc",
      "DATA",
      [
        "storage",
        "00c6a418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053adbc",
      "DATA",
      [
        "storage",
        "00c6b3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053aa94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa90.md#insn-0053aa94) · [`0053aa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aa90.md#insn-0053aa98)
- 新版 [`0053adb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053adb0.md#insn-0053adb4) · [`0053adb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053adb0.md#insn-0053adb8)

~~~diff
- 0053aa94 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 0053adb4 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 0053aa94 bytes 89390090
+ 0053adb4 bytes 893900b0
- 0053aa98 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0053aa98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053aa98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053aa98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053adb8 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0053adb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053adb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053adb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053aa98 bytes 29611091
+ 0053adb8 bytes 29a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31c78c4a4baeef15dae8161fdfd5e382"></a>

### [`0053ae64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053ae64.md) → [`0053b184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b184.md) FUN_0053b184

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`0053c2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c2e8.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`0053ae04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ae04.md) [`0053c608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053c608.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053b1c0",
      "incomplete_value": true,
      "site": "0053b1c4",
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
      "definition_site": "0053aea0",
      "incomplete_value": true,
      "site": "0053aea4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053b218",
      "incomplete_value": true,
      "site": "0053b218",
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
      "definition_site": "0053aef8",
      "incomplete_value": true,
      "site": "0053aef8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053b1b0",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0053b1c4",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053b208",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053b1b0",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "0053b1c4",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053b208",
      "READ",
      [
        "storage",
        "00c9be58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ae84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053ae64.md#insn-0053ae84) · [`0053ae90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053ae64.md#insn-0053ae90) · [`0053aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053ae64.md#insn-0053aeb8)
- 新版 [`0053b1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b184.md#insn-0053b1a4) · [`0053b1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b184.md#insn-0053b1b0) · [`0053b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b184.md#insn-0053b1d8)

~~~diff
- 0053ae84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053b1a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053ae84 bytes 083b0090
+ 0053b1a4 bytes 083b0090
- 0053ae90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 0053ae90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053b1b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 0053b1b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ae90 bytes 080947f9
+ 0053b1b0 bytes 08f146f9
- 0053aeb8 ["INT_ADD", "register:40f0:8", ["const:53aeb8:8", "const:4:8"]]
- 0053aeb8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0053b1d8 ["INT_ADD", "register:40f0:8", ["const:53b1d8:8", "const:4:8"]]
+ 0053b1d8 ["CALL", null, ["callee:00c58f30:8"]]
- 0053aeb8 bytes 2a741c94
+ 0053b1d8 bytes 56771c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41181c5512f0d3ad64d3bf3187699cc9"></a>

### [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) → [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) FUN_0053b360

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`005013c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md) [`005024c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md) [`005095e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md) [`00509948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509948.md) [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005366f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 12件 [`005016e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005016e8.md) [`005027e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027e8.md) [`00509908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509908.md) [`00509c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509c68.md) [`00509f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md) · 呼出先 4件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00536a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536a14.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053b394",
      "incomplete_value": true,
      "site": "0053b394",
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
      "definition_site": "0053b074",
      "incomplete_value": true,
      "site": "0053b074",
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
      "0053b384",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0053b394",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0053b384",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "0053b394",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md#insn-0053b058) · [`0053b064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md#insn-0053b064) · [`0053b068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md#insn-0053b068)
- 新版 [`0053b378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md#insn-0053b378) · [`0053b384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md#insn-0053b384)

~~~diff
- 0053b058 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053b378 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053b058 bytes 083b0090
+ 0053b378 bytes 083b00b0
- 0053b064 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 0053b064 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053b384 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 0053b384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053b064 bytes 081541f9
+ 0053b384 bytes 08fd40f9
- 0053b068 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0053b068 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d11481392358b9e4300d2db258cadc"></a>

### [`0053b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b450.md) → [`0053b770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b770.md) FUN_0053b770

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053b174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b174.md) [`0054ef50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054ef50.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`0053b494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b494.md) [`0054f270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054f/0054f270.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0053b77c",
      "incomplete_value": false,
      "site": "0053b780",
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
      "definition_site": "0053b45c",
      "incomplete_value": false,
      "site": "0053b460",
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
      "0053b77c",
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
      "0053b77c",
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

- 旧版 [`0053b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b450.md#insn-0053b460) · [`0053b458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b450.md#insn-0053b458) · [`0053b45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b450.md#insn-0053b45c)
- 新版 [`0053b780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b770.md#insn-0053b780) · [`0053b778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b770.md#insn-0053b778) · [`0053b77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b770.md#insn-0053b77c)

~~~diff
- 0053b460 ["INT_ADD", "register:40f0:8", ["const:53b460:8", "const:4:8"]]
- 0053b460 ["CALL", null, ["callee:0043bad8:8"]]
+ 0053b780 ["INT_ADD", "register:40f0:8", ["const:53b780:8", "const:4:8"]]
+ 0053b780 ["CALL", null, ["callee:0043bad8:8"]]
- 0053b460 bytes d600fc97
+ 0053b780 bytes d600fc97
- 0053b458 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0053b778 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053b458 bytes e0ebff90
+ 0053b778 bytes e0ebffb0
- 0053b45c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053b45c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053b45c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053b45c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053b77c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0053b77c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053b77c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053b77c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053b45c bytes 00303e91
+ 0053b77c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88fbc1cbc0bcc9c0902aad0e794bad28"></a>

### [`0053b4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b4f4.md) → [`0053b814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b814.md) FUN_0053b814

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050e084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59be0.md)
- 新版 呼出元 1件 [`0050e3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5abb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053b854",
      "incomplete_value": true,
      "site": "0053b854",
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
      "definition_site": "0053b534",
      "incomplete_value": true,
      "site": "0053b534",
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
      "0053b838",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "0053b854",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053b8b8",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053b838",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "0053b854",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053b8b8",
      "READ",
      [
        "storage",
        "00c9c1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b4f4.md#insn-0053b50c) · [`0053b518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b4f4.md#insn-0053b518) · [`0053b564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b4f4.md#insn-0053b564)
- 新版 [`0053b82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b814.md#insn-0053b82c) · [`0053b838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b814.md#insn-0053b838) · [`0053b884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b814.md#insn-0053b884)

~~~diff
- 0053b50c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 0053b82c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 0053b50c bytes 093b0090
+ 0053b82c bytes 093b00b0
- 0053b518 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1a0:8"]]
- 0053b518 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053b838 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:170:8"]]
+ 0053b838 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053b518 bytes 29d140f9
+ 0053b838 bytes 29b940f9
- 0053b564 ["INT_ADD", "register:40f0:8", ["const:53b564:8", "const:4:8"]]
- 0053b564 ["CALL", null, ["callee:00c5abb0:8"]]
+ 0053b884 ["INT_ADD", "register:40f0:8", ["const:53b884:8", "const:4:8"]]
+ 0053b884 ["CALL", null, ["callee:00c5abb0:8"]]
- 0053b564 bytes 9f791c94
+ 0053b884 bytes cb7c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba2bd346bd309095e8f4f88941f54d4"></a>

### [`0053b6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b6a8.md) → [`0053b9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b9c8.md) FUN_0053b9c8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0050e084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`0050e3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md) [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053ba04",
      "incomplete_value": true,
      "site": "0053ba04",
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
      "definition_site": "0053b6e4",
      "incomplete_value": true,
      "site": "0053b6e4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053ba40",
      "incomplete_value": false,
      "site": "0053ba48",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b720",
      "incomplete_value": false,
      "site": "0053b728",
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
            "const:2c3:8"
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
      "definition_site": "0053ba7c",
      "incomplete_value": true,
      "site": "0053ba88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b75c",
      "incomplete_value": true,
      "site": "0053b768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053b9f4",
      "READ",
      [
        "storage",
        "00c9b268",
        null,
        "pointer"
      ]
    ],
    [
      "0053ba40",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053ba78",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053b9f4",
      "READ",
      [
        "storage",
        "00c9c238",
        null,
        "pointer"
      ]
    ],
    [
      "0053ba40",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053ba78",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b6a8.md#insn-0053b728) · [`0053b768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b6a8.md#insn-0053b768) · [`0053b6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b6a8.md#insn-0053b6c8)
- 新版 [`0053ba48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b9c8.md#insn-0053ba48) · [`0053ba88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b9c8.md#insn-0053ba88) · [`0053b9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b9c8.md#insn-0053b9e8)

~~~diff
- 0053b728 ["INT_ADD", "register:40f0:8", ["const:53b728:8", "const:4:8"]]
- 0053b728 ["CALL", null, ["callee:0043e138:8"]]
+ 0053ba48 ["INT_ADD", "register:40f0:8", ["const:53ba48:8", "const:4:8"]]
+ 0053ba48 ["CALL", null, ["callee:0043e138:8"]]
- 0053b728 bytes bc09fc97
+ 0053ba48 bytes bc09fc97
- 0053b768 ["INT_ADD", "register:40f0:8", ["const:53b768:8", "const:4:8"]]
- 0053b768 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053ba88 ["INT_ADD", "register:40f0:8", ["const:53ba88:8", "const:4:8"]]
+ 0053ba88 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053b768 bytes 1e721c94
+ 0053ba88 bytes 4a751c94
- 0053b6c8 ["INT_ADD", "register:40f0:8", ["const:53b6c8:8", "const:4:8"]]
- 0053b6c8 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053b9e8 ["INT_ADD", "register:40f0:8", ["const:53b9e8:8", "const:4:8"]]
+ 0053b9e8 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053b6c8 bytes 32791c94
+ 0053b9e8 bytes 5e7c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65ef64ab9d6be9dc730a171486fb51df"></a>

### [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) → [`0053cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md) FUN_0053cca0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) [`0053168c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md) [`0053185c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md) [`00532a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md) [`0053fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fb18.md) · 呼出先 2件 [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`0053cac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cac8.md)
- 新版 呼出元 6件 [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) [`005319ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005319ac.md) [`00531b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531b7c.md) [`00532d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d20.md) [`0053fe38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fe38.md) · 呼出先 2件 [`0053ae04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ae04.md) [`0053cde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cde8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053cce0",
      "incomplete_value": true,
      "site": "0053cce8",
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
      "definition_site": "0053c9c0",
      "incomplete_value": true,
      "site": "0053c9c8",
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
      "0053ccd0",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "0053cce8",
      "DATA",
      [
        "storage",
        "00c67838",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0053ccd0",
      "READ",
      [
        "storage",
        "00c9c168",
        null,
        "pointer"
      ]
    ],
    [
      "0053cce8",
      "DATA",
      [
        "storage",
        "00c68808",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md#insn-0053c9a4) · [`0053c9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md#insn-0053c9b0) · [`0053ca1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md#insn-0053ca1c)
- 新版 [`0053ccc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md#insn-0053ccc4) · [`0053ccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md#insn-0053ccd0) · [`0053cd3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md#insn-0053cd3c)

~~~diff
- 0053c9a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053ccc4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053c9a4 bytes e83a00f0
+ 0053ccc4 bytes 083b0090
- 0053c9b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
- 0053c9b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ccd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:168:8"]]
+ 0053ccd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c9b0 bytes 08cd40f9
+ 0053ccd0 bytes 08b540f9
- 0053ca1c ["INT_ADD", "register:40f0:8", ["const:53ca1c:8", "const:4:8"]]
- 0053ca1c ["CALL", null, ["callee:0053cde8:8"]]
+ 0053cd3c ["INT_ADD", "register:40f0:8", ["const:53cd3c:8", "const:4:8"]]
+ 0053cd3c ["CALL", null, ["callee:0053cde8:8"]]
- 0053ca1c bytes 2b000094
+ 0053cd3c bytes 2b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b24fa054bab4a781f806844a5781789"></a>

### [`0053cdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cdd0.md) → [`0053d0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d0f0.md) FUN_0053d0f0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 1件 [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d138",
      "incomplete_value": true,
      "site": "0053d138",
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
      "definition_site": "0053ce18",
      "incomplete_value": true,
      "site": "0053ce18",
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
      "definition_site": "0053d174",
      "incomplete_value": true,
      "site": "0053d178",
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
      "definition_site": "0053ce54",
      "incomplete_value": true,
      "site": "0053ce58",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d110",
      "incomplete_value": false,
      "site": "0053d120",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053cdf0",
      "incomplete_value": false,
      "site": "0053ce00",
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
            "const:218:8"
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
      "0053d110",
      "PARAM",
      [
        "storage",
        "002a3218",
        null,
        "string"
      ]
    ],
    [
      "0053d12c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "0053d138",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "0053d110",
      "PARAM",
      [
        "storage",
        "002a32e3",
        null,
        "string"
      ]
    ],
    [
      "0053d12c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "0053d138",
      "DATA",
      [
        "storage",
        "00c684c8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ce00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cdd0.md#insn-0053ce00) · [`0053cdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cdd0.md#insn-0053cdf0) · [`0053ce04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cdd0.md#insn-0053ce04)
- 新版 [`0053d120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d0f0.md#insn-0053d120) · [`0053d110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d0f0.md#insn-0053d110) · [`0053d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d0f0.md#insn-0053d124)

~~~diff
- 0053ce00 ["INT_ADD", "register:40f0:8", ["const:53ce00:8", "const:4:8"]]
- 0053ce00 ["CALL", null, ["callee:00c59150:8"]]
+ 0053d120 ["INT_ADD", "register:40f0:8", ["const:53d120:8", "const:4:8"]]
+ 0053d120 ["CALL", null, ["callee:00c59150:8"]]
- 0053ce00 bytes e06c1c94
+ 0053d120 bytes 0c701c94
- 0053cdf0 ["COPY", "tmp:0:8", ["const:218:8"]]
- 0053cdf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053cdf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053cdf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053d110 ["COPY", "tmp:0:8", ["const:2e3:8"]]
+ 0053d110 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d110 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d110 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053cdf0 bytes 00600891
+ 0053d110 bytes 008c0b91
- 0053ce04 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053d124 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053ce04 bytes e83a00d0
+ 0053d124 bytes e83a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18a6b28201851f65093dc3d2b9dd384"></a>

### [`0053ceb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053ceb8.md) → [`0053d1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d1d8.md) FUN_0053d1d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053d214",
      "incomplete_value": true,
      "site": "0053d214",
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
      "definition_site": "0053cef4",
      "incomplete_value": true,
      "site": "0053cef4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d250",
      "incomplete_value": false,
      "site": "0053d258",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053cf30",
      "incomplete_value": false,
      "site": "0053cf38",
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
            "const:2c3:8"
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
      "definition_site": "0053d28c",
      "incomplete_value": true,
      "site": "0053d298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053cf6c",
      "incomplete_value": true,
      "site": "0053cf78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053d204",
      "READ",
      [
        "storage",
        "00c9b270",
        null,
        "pointer"
      ]
    ],
    [
      "0053d250",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053d288",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053d204",
      "READ",
      [
        "storage",
        "00c9c240",
        null,
        "pointer"
      ]
    ],
    [
      "0053d250",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053d288",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053cf38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053ceb8.md#insn-0053cf38) · [`0053cf78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053ceb8.md#insn-0053cf78) · [`0053ced8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053ceb8.md#insn-0053ced8)
- 新版 [`0053d258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d1d8.md#insn-0053d258) · [`0053d298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d1d8.md#insn-0053d298) · [`0053d1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d1d8.md#insn-0053d1f8)

~~~diff
- 0053cf38 ["INT_ADD", "register:40f0:8", ["const:53cf38:8", "const:4:8"]]
- 0053cf38 ["CALL", null, ["callee:0043e138:8"]]
+ 0053d258 ["INT_ADD", "register:40f0:8", ["const:53d258:8", "const:4:8"]]
+ 0053d258 ["CALL", null, ["callee:0043e138:8"]]
- 0053cf38 bytes b803fc97
+ 0053d258 bytes b803fc97
- 0053cf78 ["INT_ADD", "register:40f0:8", ["const:53cf78:8", "const:4:8"]]
- 0053cf78 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053d298 ["INT_ADD", "register:40f0:8", ["const:53d298:8", "const:4:8"]]
+ 0053d298 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053cf78 bytes 1a6c1c94
+ 0053d298 bytes 466f1c94
- 0053ced8 ["INT_ADD", "register:40f0:8", ["const:53ced8:8", "const:4:8"]]
- 0053ced8 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053d1f8 ["INT_ADD", "register:40f0:8", ["const:53d1f8:8", "const:4:8"]]
+ 0053d1f8 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053ced8 bytes 2e731c94
+ 0053d1f8 bytes 5a761c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdfa1504e549300feff2947110334e7c"></a>

### [`0053cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cfcc.md) → [`0053d2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d2ec.md) FUN_0053d2ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053d328",
      "incomplete_value": true,
      "site": "0053d328",
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
      "definition_site": "0053d008",
      "incomplete_value": true,
      "site": "0053d008",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d364",
      "incomplete_value": false,
      "site": "0053d36c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d044",
      "incomplete_value": false,
      "site": "0053d04c",
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
            "const:2c3:8"
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
      "definition_site": "0053d3a0",
      "incomplete_value": true,
      "site": "0053d3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d080",
      "incomplete_value": true,
      "site": "0053d08c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053d318",
      "READ",
      [
        "storage",
        "00c9b260",
        null,
        "pointer"
      ]
    ],
    [
      "0053d364",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053d39c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053d318",
      "READ",
      [
        "storage",
        "00c9c230",
        null,
        "pointer"
      ]
    ],
    [
      "0053d364",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053d39c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cfcc.md#insn-0053d04c) · [`0053d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cfcc.md#insn-0053d08c) · [`0053cfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cfcc.md#insn-0053cfec)
- 新版 [`0053d36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d2ec.md#insn-0053d36c) · [`0053d3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d2ec.md#insn-0053d3ac) · [`0053d30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d2ec.md#insn-0053d30c)

~~~diff
- 0053d04c ["INT_ADD", "register:40f0:8", ["const:53d04c:8", "const:4:8"]]
- 0053d04c ["CALL", null, ["callee:0043e138:8"]]
+ 0053d36c ["INT_ADD", "register:40f0:8", ["const:53d36c:8", "const:4:8"]]
+ 0053d36c ["CALL", null, ["callee:0043e138:8"]]
- 0053d04c bytes 7303fc97
+ 0053d36c bytes 7303fc97
- 0053d08c ["INT_ADD", "register:40f0:8", ["const:53d08c:8", "const:4:8"]]
- 0053d08c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053d3ac ["INT_ADD", "register:40f0:8", ["const:53d3ac:8", "const:4:8"]]
+ 0053d3ac ["CALL", null, ["callee:00c58fb0:8"]]
- 0053d08c bytes d56b1c94
+ 0053d3ac bytes 016f1c94
- 0053cfec ["INT_ADD", "register:40f0:8", ["const:53cfec:8", "const:4:8"]]
- 0053cfec ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053d30c ["INT_ADD", "register:40f0:8", ["const:53d30c:8", "const:4:8"]]
+ 0053d30c ["CALL", null, ["callee:00c5ab60:8"]]
- 0053cfec bytes e9721c94
+ 0053d30c bytes 15761c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c80926049eaeda546b487358993011"></a>

### [`0053d0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d0e0.md) → [`0053d400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d400.md) FUN_0053d400

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053d438",
      "incomplete_value": true,
      "site": "0053d438",
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
      "definition_site": "0053d118",
      "incomplete_value": true,
      "site": "0053d118",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d474",
      "incomplete_value": false,
      "site": "0053d47c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d154",
      "incomplete_value": false,
      "site": "0053d15c",
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
            "const:2c3:8"
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
      "definition_site": "0053d4b0",
      "incomplete_value": true,
      "site": "0053d4bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d190",
      "incomplete_value": true,
      "site": "0053d19c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053d474",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053d4ac",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0053d4b0",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053d474",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053d4ac",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0053d4b0",
      "READ",
      [
        "storage",
        "00c9be28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d0e0.md#insn-0053d15c) · [`0053d19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d0e0.md#insn-0053d19c) · [`0053d100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d0e0.md#insn-0053d100)
- 新版 [`0053d47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d400.md#insn-0053d47c) · [`0053d4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d400.md#insn-0053d4bc) · [`0053d420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053d400.md#insn-0053d420)

~~~diff
- 0053d15c ["INT_ADD", "register:40f0:8", ["const:53d15c:8", "const:4:8"]]
- 0053d15c ["CALL", null, ["callee:0043e138:8"]]
+ 0053d47c ["INT_ADD", "register:40f0:8", ["const:53d47c:8", "const:4:8"]]
+ 0053d47c ["CALL", null, ["callee:0043e138:8"]]
- 0053d15c bytes 2f03fc97
+ 0053d47c bytes 2f03fc97
- 0053d19c ["INT_ADD", "register:40f0:8", ["const:53d19c:8", "const:4:8"]]
- 0053d19c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053d4bc ["INT_ADD", "register:40f0:8", ["const:53d4bc:8", "const:4:8"]]
+ 0053d4bc ["CALL", null, ["callee:00c58fb0:8"]]
- 0053d19c bytes 916b1c94
+ 0053d4bc bytes bd6e1c94
- 0053d100 ["INT_ADD", "register:40f0:8", ["const:53d100:8", "const:4:8"]]
- 0053d100 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053d420 ["INT_ADD", "register:40f0:8", ["const:53d420:8", "const:4:8"]]
+ 0053d420 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053d100 bytes a4721c94
+ 0053d420 bytes d0751c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b5c1697238b28eb2afebd0d8cf1c6ff"></a>

### [`0053d838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md) → [`0053db58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db58.md) FUN_0053db58

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) [`0053ea4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053ea4c.md) [`0053f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f950.md) [`0054c8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054c8bc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 4件 [`0051ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051a/0051ad34.md) [`0053ed6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ed6c.md) [`0053fc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc70.md) [`0054cbdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054c/0054cbdc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0053db64",
      "incomplete_value": false,
      "site": "0053db68",
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
      "definition_site": "0053d844",
      "incomplete_value": false,
      "site": "0053d848",
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
      "0053db64",
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
      "0053db64",
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

- 旧版 [`0053d848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md#insn-0053d848) · [`0053d840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md#insn-0053d840) · [`0053d844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d838.md#insn-0053d844)
- 新版 [`0053db68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db58.md#insn-0053db68) · [`0053db60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db58.md#insn-0053db60) · [`0053db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053db58.md#insn-0053db64)

~~~diff
- 0053d848 ["INT_ADD", "register:40f0:8", ["const:53d848:8", "const:4:8"]]
- 0053d848 ["CALL", null, ["callee:0043bad8:8"]]
+ 0053db68 ["INT_ADD", "register:40f0:8", ["const:53db68:8", "const:4:8"]]
+ 0053db68 ["CALL", null, ["callee:0043bad8:8"]]
- 0053d848 bytes dcf7fb97
+ 0053db68 bytes dcf7fb97
- 0053d840 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0053db60 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053d840 bytes c0ebffd0
+ 0053db60 bytes c0ebfff0
- 0053d844 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053d844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053db64 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0053db64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053db64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053db64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d844 bytes 00303e91
+ 0053db64 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cf416dd2dc35d917f9a6b3b42ca4287"></a>

### [`0053db84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053db84.md) → [`0053dea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dea4.md) FUN_0053dea4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59be0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5abb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.71% / 新版 91.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053deec",
      "incomplete_value": true,
      "site": "0053deec",
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
      "definition_site": "0053dbcc",
      "incomplete_value": true,
      "site": "0053dbcc",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053df20",
      "incomplete_value": true,
      "site": "0053df20",
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
      "definition_site": "0053dc00",
      "incomplete_value": true,
      "site": "0053dc00",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053df28",
      "incomplete_value": true,
      "site": "0053df28",
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
      "definition_site": "0053dc08",
      "incomplete_value": true,
      "site": "0053dc08",
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
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053ded8",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0053deec",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053df18",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053ded8",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0053deec",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053df18",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053db84.md#insn-0053dba4) · [`0053dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053db84.md#insn-0053dbb8) · [`0053dbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053db84.md#insn-0053dbd8)
- 新版 [`0053dec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dea4.md#insn-0053dec4) · [`0053ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dea4.md#insn-0053ded8) · [`0053def8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053dea4.md#insn-0053def8)

~~~diff
- 0053dba4 ["COPY", "register:40b8:8", ["const:c9a000:8"]]
+ 0053dec4 ["COPY", "register:40b8:8", ["const:c9b000:8"]]
- 0053dba4 bytes f73a00b0
+ 0053dec4 bytes f73a00d0
- 0053dbb8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e08:8"]]
- 0053dbb8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ded8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:dd8:8"]]
+ 0053ded8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053dbb8 bytes f70647f9
+ 0053ded8 bytes f7ee46f9
- 0053dbd8 ["INT_ADD", "register:40f0:8", ["const:53dbd8:8", "const:4:8"]]
- 0053dbd8 ["CALL", null, ["callee:00c59730:8"]]
+ 0053def8 ["INT_ADD", "register:40f0:8", ["const:53def8:8", "const:4:8"]]
+ 0053def8 ["CALL", null, ["callee:00c59730:8"]]
- 0053dbd8 bytes e26a1c94
+ 0053def8 bytes 0e6e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3f112b06e07bc8b7a9a10eb0e0bbd73"></a>

### [`0053e098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e098.md) → [`0053e3b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e3b8.md) FUN_0053e3b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "definition_site": "0053e430",
      "incomplete_value": false,
      "site": "0053e438",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e110",
      "incomplete_value": false,
      "site": "0053e118",
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
            "const:2c3:8"
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
      "definition_site": "0053e46c",
      "incomplete_value": true,
      "site": "0053e478",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e14c",
      "incomplete_value": true,
      "site": "0053e158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "definition_site": "0053e468",
      "incomplete_value": false,
      "site": "0053e478",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0053e148",
      "incomplete_value": false,
      "site": "0053e158",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0053e3e4",
      "READ",
      [
        "storage",
        "00c9b248",
        null,
        "pointer"
      ]
    ],
    [
      "0053e430",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053e468",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e3e4",
      "READ",
      [
        "storage",
        "00c9c218",
        null,
        "pointer"
      ]
    ],
    [
      "0053e430",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053e468",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e098.md#insn-0053e118) · [`0053e158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e098.md#insn-0053e158) · [`0053e0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e098.md#insn-0053e0b8)
- 新版 [`0053e438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e3b8.md#insn-0053e438) · [`0053e478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e3b8.md#insn-0053e478) · [`0053e3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e3b8.md#insn-0053e3d8)

~~~diff
- 0053e118 ["INT_ADD", "register:40f0:8", ["const:53e118:8", "const:4:8"]]
- 0053e118 ["CALL", null, ["callee:0043e138:8"]]
+ 0053e438 ["INT_ADD", "register:40f0:8", ["const:53e438:8", "const:4:8"]]
+ 0053e438 ["CALL", null, ["callee:0043e138:8"]]
- 0053e118 bytes 40fffb97
+ 0053e438 bytes 40fffb97
- 0053e158 ["INT_ADD", "register:40f0:8", ["const:53e158:8", "const:4:8"]]
- 0053e158 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053e478 ["INT_ADD", "register:40f0:8", ["const:53e478:8", "const:4:8"]]
+ 0053e478 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e158 bytes a2671c94
+ 0053e478 bytes ce6a1c94
- 0053e0b8 ["INT_ADD", "register:40f0:8", ["const:53e0b8:8", "const:4:8"]]
- 0053e0b8 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053e3d8 ["INT_ADD", "register:40f0:8", ["const:53e3d8:8", "const:4:8"]]
+ 0053e3d8 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e0b8 bytes b66e1c94
+ 0053e3d8 bytes e2711c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63bc4ef435fe16a0bb929494330352eb"></a>

### [`0053e1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e1ac.md) → [`0053e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e4cc.md) FUN_0053e4cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053e508",
      "incomplete_value": true,
      "site": "0053e508",
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
      "definition_site": "0053e1e8",
      "incomplete_value": true,
      "site": "0053e1e8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e580",
      "incomplete_value": true,
      "site": "0053e58c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e260",
      "incomplete_value": true,
      "site": "0053e26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "definition_site": "0053e57c",
      "incomplete_value": false,
      "site": "0053e58c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0053e25c",
      "incomplete_value": false,
      "site": "0053e26c",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0053e4f8",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "0053e544",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053e57c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e4f8",
      "READ",
      [
        "storage",
        "00c9c250",
        null,
        "pointer"
      ]
    ],
    [
      "0053e544",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053e57c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e1ac.md#insn-0053e26c) · [`0053e1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e1ac.md#insn-0053e1cc) · [`0053e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e1ac.md#insn-0053e1d4)
- 新版 [`0053e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e4cc.md#insn-0053e58c) · [`0053e4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e4cc.md#insn-0053e4ec) · [`0053e4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e4cc.md#insn-0053e4f4)

~~~diff
- 0053e26c ["INT_ADD", "register:40f0:8", ["const:53e26c:8", "const:4:8"]]
- 0053e26c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053e58c ["INT_ADD", "register:40f0:8", ["const:53e58c:8", "const:4:8"]]
+ 0053e58c ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e26c bytes 5d671c94
+ 0053e58c bytes 896a1c94
- 0053e1cc ["INT_ADD", "register:40f0:8", ["const:53e1cc:8", "const:4:8"]]
- 0053e1cc ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053e4ec ["INT_ADD", "register:40f0:8", ["const:53e4ec:8", "const:4:8"]]
+ 0053e4ec ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e1cc bytes 716e1c94
+ 0053e4ec bytes 9d711c94
- 0053e1d4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053e4f4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053e1d4 bytes e83a00b0
+ 0053e4f4 bytes e83a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d2e8ec0ab2a513938d3bec474f904d4"></a>

### [`0053e2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e2c0.md) → [`0053e5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e5e0.md) FUN_0053e5e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053e61c",
      "incomplete_value": true,
      "site": "0053e61c",
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
      "definition_site": "0053e2fc",
      "incomplete_value": true,
      "site": "0053e2fc",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e658",
      "incomplete_value": false,
      "site": "0053e660",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e338",
      "incomplete_value": false,
      "site": "0053e340",
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
            "const:2c3:8"
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
      "definition_site": "0053e694",
      "incomplete_value": true,
      "site": "0053e6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e374",
      "incomplete_value": true,
      "site": "0053e380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053e60c",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "0053e658",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053e690",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e60c",
      "READ",
      [
        "storage",
        "00c9c260",
        null,
        "pointer"
      ]
    ],
    [
      "0053e658",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053e690",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e2c0.md#insn-0053e340) · [`0053e380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e2c0.md#insn-0053e380) · [`0053e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e2c0.md#insn-0053e2e0)
- 新版 [`0053e660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e5e0.md#insn-0053e660) · [`0053e6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e5e0.md#insn-0053e6a0) · [`0053e600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e5e0.md#insn-0053e600)

~~~diff
- 0053e340 ["INT_ADD", "register:40f0:8", ["const:53e340:8", "const:4:8"]]
- 0053e340 ["CALL", null, ["callee:0043e138:8"]]
+ 0053e660 ["INT_ADD", "register:40f0:8", ["const:53e660:8", "const:4:8"]]
+ 0053e660 ["CALL", null, ["callee:0043e138:8"]]
- 0053e340 bytes b6fefb97
+ 0053e660 bytes b6fefb97
- 0053e380 ["INT_ADD", "register:40f0:8", ["const:53e380:8", "const:4:8"]]
- 0053e380 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053e6a0 ["INT_ADD", "register:40f0:8", ["const:53e6a0:8", "const:4:8"]]
+ 0053e6a0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e380 bytes 18671c94
+ 0053e6a0 bytes 446a1c94
- 0053e2e0 ["INT_ADD", "register:40f0:8", ["const:53e2e0:8", "const:4:8"]]
- 0053e2e0 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053e600 ["INT_ADD", "register:40f0:8", ["const:53e600:8", "const:4:8"]]
+ 0053e600 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e2e0 bytes 2c6e1c94
+ 0053e600 bytes 58711c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af92da9d2be88ffea3aa4a9d8272f67d"></a>

### [`0053e4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e4e8.md) → [`0053e808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e808.md) FUN_0053e808

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053e844",
      "incomplete_value": true,
      "site": "0053e844",
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
      "definition_site": "0053e524",
      "incomplete_value": true,
      "site": "0053e524",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e8bc",
      "incomplete_value": true,
      "site": "0053e8c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e59c",
      "incomplete_value": true,
      "site": "0053e5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "definition_site": "0053e8b8",
      "incomplete_value": false,
      "site": "0053e8c8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0053e598",
      "incomplete_value": false,
      "site": "0053e5a8",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0053e834",
      "READ",
      [
        "storage",
        "00c9b288",
        null,
        "pointer"
      ]
    ],
    [
      "0053e880",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053e8b8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e834",
      "READ",
      [
        "storage",
        "00c9c258",
        null,
        "pointer"
      ]
    ],
    [
      "0053e880",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053e8b8",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e4e8.md#insn-0053e5a8) · [`0053e508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e4e8.md#insn-0053e508) · [`0053e510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e4e8.md#insn-0053e510)
- 新版 [`0053e8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e808.md#insn-0053e8c8) · [`0053e828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e808.md#insn-0053e828) · [`0053e830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e808.md#insn-0053e830)

~~~diff
- 0053e5a8 ["INT_ADD", "register:40f0:8", ["const:53e5a8:8", "const:4:8"]]
- 0053e5a8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053e8c8 ["INT_ADD", "register:40f0:8", ["const:53e8c8:8", "const:4:8"]]
+ 0053e8c8 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e5a8 bytes 8e661c94
+ 0053e8c8 bytes ba691c94
- 0053e508 ["INT_ADD", "register:40f0:8", ["const:53e508:8", "const:4:8"]]
- 0053e508 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053e828 ["INT_ADD", "register:40f0:8", ["const:53e828:8", "const:4:8"]]
+ 0053e828 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e508 bytes a26d1c94
+ 0053e828 bytes ce701c94
- 0053e510 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053e830 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053e510 bytes e83a00b0
+ 0053e830 bytes e83a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc3eed7387b3649aace37a4ee06a5f8a"></a>

### [`0053e5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e5fc.md) → [`0053e91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e91c.md) FUN_0053e91c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053e958",
      "incomplete_value": true,
      "site": "0053e958",
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
      "definition_site": "0053e638",
      "incomplete_value": true,
      "site": "0053e638",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e994",
      "incomplete_value": false,
      "site": "0053e99c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e674",
      "incomplete_value": false,
      "site": "0053e67c",
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
            "const:2c3:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "0053e638"
      ],
      [
        "CONDITIONAL_JUMP",
        "0053e958"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0053e958",
      "incomplete_value": true,
      "site": "0053e984",
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
      "definition_site": "0053e638",
      "incomplete_value": true,
      "site": "0053e664",
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
      "0053e948",
      "READ",
      [
        "storage",
        "00c9b250",
        null,
        "pointer"
      ]
    ],
    [
      "0053e994",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053e9cc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e948",
      "READ",
      [
        "storage",
        "00c9c220",
        null,
        "pointer"
      ]
    ],
    [
      "0053e994",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053e9cc",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e5fc.md#insn-0053e67c) · [`0053e61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e5fc.md#insn-0053e61c) · [`0053e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e5fc.md#insn-0053e624)
- 新版 [`0053e99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e91c.md#insn-0053e99c) · [`0053e93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e91c.md#insn-0053e93c) · [`0053e944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053e91c.md#insn-0053e944)

~~~diff
- 0053e67c ["INT_ADD", "register:40f0:8", ["const:53e67c:8", "const:4:8"]]
- 0053e67c ["CALL", null, ["callee:0043e138:8"]]
+ 0053e99c ["INT_ADD", "register:40f0:8", ["const:53e99c:8", "const:4:8"]]
+ 0053e99c ["CALL", null, ["callee:0043e138:8"]]
- 0053e67c bytes e7fdfb97
+ 0053e99c bytes e7fdfb97
- 0053e61c ["INT_ADD", "register:40f0:8", ["const:53e61c:8", "const:4:8"]]
- 0053e61c ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053e93c ["INT_ADD", "register:40f0:8", ["const:53e93c:8", "const:4:8"]]
+ 0053e93c ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e61c bytes 5d6d1c94
+ 0053e93c bytes 89701c94
- 0053e624 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053e944 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053e624 bytes e83a00b0
+ 0053e944 bytes e83a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3a84bbb3e60e232fc22b562eccab840"></a>

### [`0053e710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e710.md) → [`0053ea30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ea30.md) FUN_0053ea30

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053ea6c",
      "incomplete_value": true,
      "site": "0053ea6c",
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
      "definition_site": "0053e74c",
      "incomplete_value": true,
      "site": "0053e74c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053eaa8",
      "incomplete_value": false,
      "site": "0053eab0",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e788",
      "incomplete_value": false,
      "site": "0053e790",
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
            "const:2c3:8"
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
      "definition_site": "0053eae4",
      "incomplete_value": true,
      "site": "0053eaf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e7c4",
      "incomplete_value": true,
      "site": "0053e7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053ea5c",
      "READ",
      [
        "storage",
        "00c9b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "0053eaa8",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053eae0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053ea5c",
      "READ",
      [
        "storage",
        "00c9c270",
        null,
        "pointer"
      ]
    ],
    [
      "0053eaa8",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053eae0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e710.md#insn-0053e790) · [`0053e7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e710.md#insn-0053e7d0) · [`0053e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e710.md#insn-0053e730)
- 新版 [`0053eab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ea30.md#insn-0053eab0) · [`0053eaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ea30.md#insn-0053eaf0) · [`0053ea50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ea30.md#insn-0053ea50)

~~~diff
- 0053e790 ["INT_ADD", "register:40f0:8", ["const:53e790:8", "const:4:8"]]
- 0053e790 ["CALL", null, ["callee:0043e138:8"]]
+ 0053eab0 ["INT_ADD", "register:40f0:8", ["const:53eab0:8", "const:4:8"]]
+ 0053eab0 ["CALL", null, ["callee:0043e138:8"]]
- 0053e790 bytes a2fdfb97
+ 0053eab0 bytes a2fdfb97
- 0053e7d0 ["INT_ADD", "register:40f0:8", ["const:53e7d0:8", "const:4:8"]]
- 0053e7d0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053eaf0 ["INT_ADD", "register:40f0:8", ["const:53eaf0:8", "const:4:8"]]
+ 0053eaf0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e7d0 bytes 04661c94
+ 0053eaf0 bytes 30691c94
- 0053e730 ["INT_ADD", "register:40f0:8", ["const:53e730:8", "const:4:8"]]
- 0053e730 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053ea50 ["INT_ADD", "register:40f0:8", ["const:53ea50:8", "const:4:8"]]
+ 0053ea50 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e730 bytes 186d1c94
+ 0053ea50 bytes 44701c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-766afeb4a464d59e39e3f12415f70a21"></a>

### [`0053e824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e824.md) → [`0053eb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053eb44.md) FUN_0053eb44

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053eb80",
      "incomplete_value": true,
      "site": "0053eb80",
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
      "definition_site": "0053e860",
      "incomplete_value": true,
      "site": "0053e860",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053ebbc",
      "incomplete_value": false,
      "site": "0053ebc4",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e89c",
      "incomplete_value": false,
      "site": "0053e8a4",
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
            "const:2c3:8"
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
      "definition_site": "0053ebf8",
      "incomplete_value": true,
      "site": "0053ec04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e8d8",
      "incomplete_value": true,
      "site": "0053e8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053eb70",
      "READ",
      [
        "storage",
        "00c9b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "0053ebbc",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053ebf4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053eb70",
      "READ",
      [
        "storage",
        "00c9c278",
        null,
        "pointer"
      ]
    ],
    [
      "0053ebbc",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053ebf4",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e824.md#insn-0053e8a4) · [`0053e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e824.md#insn-0053e8e4) · [`0053e844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e824.md#insn-0053e844)
- 新版 [`0053ebc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053eb44.md#insn-0053ebc4) · [`0053ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053eb44.md#insn-0053ec04) · [`0053eb64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053eb44.md#insn-0053eb64)

~~~diff
- 0053e8a4 ["INT_ADD", "register:40f0:8", ["const:53e8a4:8", "const:4:8"]]
- 0053e8a4 ["CALL", null, ["callee:0043e138:8"]]
+ 0053ebc4 ["INT_ADD", "register:40f0:8", ["const:53ebc4:8", "const:4:8"]]
+ 0053ebc4 ["CALL", null, ["callee:0043e138:8"]]
- 0053e8a4 bytes 5dfdfb97
+ 0053ebc4 bytes 5dfdfb97
- 0053e8e4 ["INT_ADD", "register:40f0:8", ["const:53e8e4:8", "const:4:8"]]
- 0053e8e4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053ec04 ["INT_ADD", "register:40f0:8", ["const:53ec04:8", "const:4:8"]]
+ 0053ec04 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e8e4 bytes bf651c94
+ 0053ec04 bytes eb681c94
- 0053e844 ["INT_ADD", "register:40f0:8", ["const:53e844:8", "const:4:8"]]
- 0053e844 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053eb64 ["INT_ADD", "register:40f0:8", ["const:53eb64:8", "const:4:8"]]
+ 0053eb64 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e844 bytes d36c1c94
+ 0053eb64 bytes ff6f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ece199b6fa26cd3870c3c55d1a778ec0"></a>

### [`0053e938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e938.md) → [`0053ec58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ec58.md) FUN_0053ec58

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00521210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00521/00521210.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053ec94",
      "incomplete_value": true,
      "site": "0053ec94",
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
      "definition_site": "0053e974",
      "incomplete_value": true,
      "site": "0053e974",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053ecd0",
      "incomplete_value": false,
      "site": "0053ecd8",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e9b0",
      "incomplete_value": false,
      "site": "0053e9b8",
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
            "const:2c3:8"
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
      "definition_site": "0053ed0c",
      "incomplete_value": true,
      "site": "0053ed18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e9ec",
      "incomplete_value": true,
      "site": "0053e9f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0053ec84",
      "READ",
      [
        "storage",
        "00c9b298",
        null,
        "pointer"
      ]
    ],
    [
      "0053ecd0",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "0053ed08",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053ec84",
      "READ",
      [
        "storage",
        "00c9c268",
        null,
        "pointer"
      ]
    ],
    [
      "0053ecd0",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "0053ed08",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e938.md#insn-0053e9b8) · [`0053e9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e938.md#insn-0053e9f8) · [`0053e958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053e938.md#insn-0053e958)
- 新版 [`0053ecd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ec58.md#insn-0053ecd8) · [`0053ed18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ec58.md#insn-0053ed18) · [`0053ec78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053e/0053ec58.md#insn-0053ec78)

~~~diff
- 0053e9b8 ["INT_ADD", "register:40f0:8", ["const:53e9b8:8", "const:4:8"]]
- 0053e9b8 ["CALL", null, ["callee:0043e138:8"]]
+ 0053ecd8 ["INT_ADD", "register:40f0:8", ["const:53ecd8:8", "const:4:8"]]
+ 0053ecd8 ["CALL", null, ["callee:0043e138:8"]]
- 0053e9b8 bytes 18fdfb97
+ 0053ecd8 bytes 18fdfb97
- 0053e9f8 ["INT_ADD", "register:40f0:8", ["const:53e9f8:8", "const:4:8"]]
- 0053e9f8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053ed18 ["INT_ADD", "register:40f0:8", ["const:53ed18:8", "const:4:8"]]
+ 0053ed18 ["CALL", null, ["callee:00c58fb0:8"]]
- 0053e9f8 bytes 7a651c94
+ 0053ed18 bytes a6681c94
- 0053e958 ["INT_ADD", "register:40f0:8", ["const:53e958:8", "const:4:8"]]
- 0053e958 ["CALL", null, ["callee:00c5ab60:8"]]
+ 0053ec78 ["INT_ADD", "register:40f0:8", ["const:53ec78:8", "const:4:8"]]
+ 0053ec78 ["CALL", null, ["callee:00c5ab60:8"]]
- 0053e958 bytes 8e6c1c94
+ 0053ec78 bytes ba6f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd6df6204ba0d9a69401a1995efe636c"></a>

### [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) → [`0053f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md) FUN_0053f364

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`0050f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md) [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) [`00524a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md) [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 11件 [`0050f74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md) [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) [`00511584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md) [`00524d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00524/00524d40.md) [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0053f370",
      "incomplete_value": false,
      "site": "0053f374",
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
      "definition_site": "0053f050",
      "incomplete_value": false,
      "site": "0053f054",
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
      "0053f370",
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
      "0053f370",
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

- 旧版 [`0053f054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md#insn-0053f054) · [`0053f04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md#insn-0053f04c) · [`0053f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md#insn-0053f050)
- 新版 [`0053f374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md#insn-0053f374) · [`0053f36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md#insn-0053f36c) · [`0053f370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md#insn-0053f370)

~~~diff
- 0053f054 ["INT_ADD", "register:40f0:8", ["const:53f054:8", "const:4:8"]]
- 0053f054 ["CALL", null, ["callee:0043bad8:8"]]
+ 0053f374 ["INT_ADD", "register:40f0:8", ["const:53f374:8", "const:4:8"]]
+ 0053f374 ["CALL", null, ["callee:0043bad8:8"]]
- 0053f054 bytes d9f1fb97
+ 0053f374 bytes d9f1fb97
- 0053f04c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0053f36c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053f04c bytes c0ebff90
+ 0053f36c bytes c0ebffb0
- 0053f050 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053f050 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053f050 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053f050 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053f370 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0053f370 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053f370 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053f370 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053f050 bytes 00303e91
+ 0053f370 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec75a4bc7a3bbedf67a8a3172b6ca0e"></a>

### [`0053f8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f8ec.md) → [`0053fc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc0c.md) FUN_0053fc0c

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) [`005283e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md) [`0053f370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f370.md) [`0054e9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054e/0054e9b8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 6件 [`00526d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md) [`00528188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md) [`00528704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md) [`0053f690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f690.md) [`0054ecd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054e/0054ecd8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0053fc18",
      "incomplete_value": false,
      "site": "0053fc1c",
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
      "definition_site": "0053f8f8",
      "incomplete_value": false,
      "site": "0053f8fc",
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
      "0053fc18",
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
      "0053fc18",
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

- 旧版 [`0053f8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f8ec.md#insn-0053f8fc) · [`0053f8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f8ec.md#insn-0053f8f4) · [`0053f8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f8ec.md#insn-0053f8f8)
- 新版 [`0053fc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc0c.md#insn-0053fc1c) · [`0053fc14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc0c.md#insn-0053fc14) · [`0053fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc0c.md#insn-0053fc18)

~~~diff
- 0053f8fc ["INT_ADD", "register:40f0:8", ["const:53f8fc:8", "const:4:8"]]
- 0053f8fc ["CALL", null, ["callee:0043bad8:8"]]
+ 0053fc1c ["INT_ADD", "register:40f0:8", ["const:53fc1c:8", "const:4:8"]]
+ 0053fc1c ["CALL", null, ["callee:0043bad8:8"]]
- 0053f8fc bytes afeffb97
+ 0053fc1c bytes afeffb97
- 0053f8f4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0053fc14 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053f8f4 bytes c0ebff90
+ 0053fc14 bytes c0ebffb0
- 0053f8f8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053f8f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053f8f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053f8f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053fc18 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0053fc18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fc18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fc18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053f8f8 bytes 00303e91
+ 0053fc18 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73eda5a69d221fdcb9e5a4c1ed80d222"></a>

### [`0053fce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fce0.md) → [`00540000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540000.md) FUN_00540000

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fb18.md) [`0054d17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d17c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`0053fe38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fe38.md) [`0054d49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054d/0054d49c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0054000c",
      "incomplete_value": false,
      "site": "00540010",
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
      "definition_site": "0053fcec",
      "incomplete_value": false,
      "site": "0053fcf0",
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
      "0054000c",
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
      "0054000c",
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

- 旧版 [`0053fcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fce0.md#insn-0053fcf0) · [`0053fce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fce0.md#insn-0053fce8) · [`0053fcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fce0.md#insn-0053fcec)
- 新版 [`00540010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540000.md#insn-00540010) · [`00540008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540000.md#insn-00540008) · [`0054000c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540000.md#insn-0054000c)

~~~diff
- 0053fcf0 ["INT_ADD", "register:40f0:8", ["const:53fcf0:8", "const:4:8"]]
- 0053fcf0 ["CALL", null, ["callee:0043bad8:8"]]
+ 00540010 ["INT_ADD", "register:40f0:8", ["const:540010:8", "const:4:8"]]
+ 00540010 ["CALL", null, ["callee:0043bad8:8"]]
- 0053fcf0 bytes b2eefb97
+ 00540010 bytes b2eefb97
- 0053fce8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00540008 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053fce8 bytes c0ebff90
+ 00540008 bytes c0ebff90
- 0053fcec ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053fcec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053fcec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053fcec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054000c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0054000c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054000c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054000c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053fcec bytes 00303e91
+ 0054000c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a202a04999d2a2688c4c1b3255ad3f"></a>

### [`0053ff44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff44.md) → [`00540264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540264.md) FUN_00540264

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004efe64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ef/004efe64.md) [`0053fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fd58.md) [`00544e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e9c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`004f0184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f0/004f0184.md) [`00540078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540078.md) [`005451bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451bc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00540270",
      "incomplete_value": false,
      "site": "00540274",
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
      "definition_site": "0053ff50",
      "incomplete_value": false,
      "site": "0053ff54",
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
      "00540270",
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
      "00540270",
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

- 旧版 [`0053ff54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff44.md#insn-0053ff54) · [`0053ff4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff44.md#insn-0053ff4c) · [`0053ff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff44.md#insn-0053ff50)
- 新版 [`00540274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540264.md#insn-00540274) · [`0054026c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540264.md#insn-0054026c) · [`00540270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540264.md#insn-00540270)

~~~diff
- 0053ff54 ["INT_ADD", "register:40f0:8", ["const:53ff54:8", "const:4:8"]]
- 0053ff54 ["CALL", null, ["callee:0043bad8:8"]]
+ 00540274 ["INT_ADD", "register:40f0:8", ["const:540274:8", "const:4:8"]]
+ 00540274 ["CALL", null, ["callee:0043bad8:8"]]
- 0053ff54 bytes 19eefb97
+ 00540274 bytes 19eefb97
- 0053ff4c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0054026c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053ff4c bytes c0ebff90
+ 0054026c bytes c0ebff90
- 0053ff50 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0053ff50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053ff50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053ff50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00540270 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00540270 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00540270 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00540270 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053ff50 bytes 00303e91
+ 00540270 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f994bf64d45f0cda22780c349ea5d1"></a>

### [`0053ff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff58.md) → [`00540278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540278.md) FUN_00540278

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005402ec",
      "incomplete_value": true,
      "site": "005402ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ffcc",
      "incomplete_value": true,
      "site": "0053ffcc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
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
      "005402dc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005402dc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ffcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff58.md#insn-0053ffcc) · [`0053ff94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff58.md#insn-0053ff94) · [`0053ffbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ff58.md#insn-0053ffbc)
- 新版 [`005402ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540278.md#insn-005402ec) · [`005402b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540278.md#insn-005402b4) · [`005402dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540278.md#insn-005402dc)

~~~diff
- 0053ffcc ["COPY", "register:0:8", ["register:4048:8"]]
- 0053ffcc ["INT_ADD", "register:40f0:8", ["const:53ffcc:8", "const:4:8"]]
- 0053ffcc ["CALLIND", null, ["register:0:8"]]
+ 005402ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005402ec ["INT_ADD", "register:40f0:8", ["const:5402ec:8", "const:4:8"]]
+ 005402ec ["CALLIND", null, ["register:0:8"]]
- 0053ffcc bytes 20013fd6
+ 005402ec bytes 20013fd6
- 0053ff94 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 005402b4 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 0053ff94 bytes 55390090
+ 005402b4 bytes 55390090
- 0053ffbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
- 0053ffbc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005402dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d8:8"]]
+ 005402dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ffbc bytes a90644f9
+ 005402dc bytes a9ee43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99eb078617ce5835d77ab441a8418c70"></a>

### [`0053ffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md) → [`00540300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540300.md) FUN_00540300

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00532fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532fb0.md) · 呼出先 2件 [`0053fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fd58.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)
- 新版 呼出元 1件 [`005332d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332d0.md) · 呼出先 2件 [`00540078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540078.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0054032c",
      "incomplete_value": false,
      "site": "0054032c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c67000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054000c",
      "incomplete_value": false,
      "site": "0054000c",
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
            "const:ec8:8"
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
      "0054032c",
      "DATA",
      [
        "storage",
        "00c66ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054032c",
      "DATA",
      [
        "storage",
        "00c67e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053fff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md#insn-0053fff8) · [`0053fffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md#insn-0053fffc) · [`00540010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053ffe0.md#insn-00540010)
- 新版 [`00540318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540300.md#insn-00540318) · [`0054031c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540300.md#insn-0054031c) · [`00540330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540300.md#insn-00540330)

~~~diff
- 0053fff8 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00540318 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 0053fff8 bytes 283900f0
+ 00540318 bytes 283900f0
- 0053fffc ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 0053fffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053fffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053fffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054031c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0054031c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054031c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054031c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053fffc bytes 08213b91
+ 0054031c bytes 08613a91
- 00540010 ["INT_ADD", "register:40f0:8", ["const:540010:8", "const:4:8"]]
- 00540010 ["CALL", null, ["callee:00c59be0:8"]]
+ 00540330 ["INT_ADD", "register:40f0:8", ["const:540330:8", "const:4:8"]]
+ 00540330 ["CALL", null, ["callee:00c59be0:8"]]
- 00540010 bytes 00631c94
+ 00540330 bytes 2c661c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a9f2d68e740555c7918634e4fd712bb"></a>

### [`00540114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md) → [`00540434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md) FUN_00540434

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0053462c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053462c.md) [`00534638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md) [`00534664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534664.md) [`00534674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 4件 [`0053494c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053494c.md) [`00534958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534958.md) [`00534984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534984.md) [`00534994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534994.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00540470",
      "incomplete_value": true,
      "site": "00540470",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540150",
      "incomplete_value": true,
      "site": "00540150",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0054049c",
      "incomplete_value": true,
      "site": "0054049c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054017c",
      "incomplete_value": true,
      "site": "0054017c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005404c8",
      "incomplete_value": true,
      "site": "005404c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005401a8",
      "incomplete_value": true,
      "site": "005401a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00540460",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0054048c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005404b8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00540460",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0054048c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005404b8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md#insn-00540150) · [`0054017c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md#insn-0054017c) · [`005401a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md#insn-005401a8)
- 新版 [`00540470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md#insn-00540470) · [`0054049c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md#insn-0054049c) · [`005404c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md#insn-005404c8)

~~~diff
- 00540150 ["COPY", "register:0:8", ["register:4048:8"]]
- 00540150 ["INT_ADD", "register:40f0:8", ["const:540150:8", "const:4:8"]]
- 00540150 ["CALLIND", null, ["register:0:8"]]
+ 00540470 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00540470 ["INT_ADD", "register:40f0:8", ["const:540470:8", "const:4:8"]]
+ 00540470 ["CALLIND", null, ["register:0:8"]]
- 00540150 bytes 20013fd6
+ 00540470 bytes 20013fd6
- 0054017c ["COPY", "register:0:8", ["register:4048:8"]]
- 0054017c ["INT_ADD", "register:40f0:8", ["const:54017c:8", "const:4:8"]]
- 0054017c ["CALLIND", null, ["register:0:8"]]
+ 0054049c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0054049c ["INT_ADD", "register:40f0:8", ["const:54049c:8", "const:4:8"]]
+ 0054049c ["CALLIND", null, ["register:0:8"]]
- 0054017c bytes 20013fd6
+ 0054049c bytes 20013fd6
- 005401a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005401a8 ["INT_ADD", "register:40f0:8", ["const:5401a8:8", "const:4:8"]]
- 005401a8 ["CALLIND", null, ["register:0:8"]]
+ 005404c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005404c8 ["INT_ADD", "register:40f0:8", ["const:5404c8:8", "const:4:8"]]
+ 005404c8 ["CALLIND", null, ["register:0:8"]]
- 005401a8 bytes 20013fd6
+ 005404c8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c22ad4f33d67f29d7436a5defb0c36b"></a>

### [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) → [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md) FUN_00540604

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 20件 [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) [`004b0678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0678.md) [`004b5398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5398.md) [`004b5500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5500.md) [`004b571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b571c.md) · 呼出先 8件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 20件 [`004aff70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004aff70.md) [`004b0998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b0/004b0998.md) [`004b56b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b56b8.md) [`004b5820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5820.md) [`004b5a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5a3c.md) · 呼出先 8件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005406f4",
      "incomplete_value": true,
      "site": "005406fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005403d4",
      "incomplete_value": true,
      "site": "005403dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005406f8",
      "incomplete_value": true,
      "site": "005406fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005403d8",
      "incomplete_value": true,
      "site": "005403dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005406f4",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "005406f4",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005406f8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005406f4",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "005406f4",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005406f8",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005403dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md#insn-005403dc) · [`00540330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md#insn-00540330) · [`0054035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md#insn-0054035c)
- 新版 [`005406fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md#insn-005406fc) · [`00540650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md#insn-00540650) · [`0054067c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md#insn-0054067c)

~~~diff
- 005403dc ["INT_ADD", "register:40f0:8", ["const:5403dc:8", "const:4:8"]]
- 005403dc ["CALL", null, ["callee:00c58fb0:8"]]
+ 005406fc ["INT_ADD", "register:40f0:8", ["const:5406fc:8", "const:4:8"]]
+ 005406fc ["CALL", null, ["callee:00c58fb0:8"]]
- 005403dc bytes 015f1c94
+ 005406fc bytes 2d621c94
- 00540330 ["INT_ADD", "register:40f0:8", ["const:540330:8", "const:4:8"]]
- 00540330 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00540650 ["INT_ADD", "register:40f0:8", ["const:540650:8", "const:4:8"]]
+ 00540650 ["CALL", null, ["callee:00c59ad0:8"]]
- 00540330 bytes f4611c94
+ 00540650 bytes 20651c94
- 0054035c ["INT_ADD", "register:40f0:8", ["const:54035c:8", "const:4:8"]]
- 0054035c ["CALL", null, ["callee:00c590a0:8"]]
+ 0054067c ["INT_ADD", "register:40f0:8", ["const:54067c:8", "const:4:8"]]
+ 0054067c ["CALL", null, ["callee:00c590a0:8"]]
- 0054035c bytes 5d5f1c94
+ 0054067c bytes 89621c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f70602902318b81753ceabdef68e6ef"></a>

### [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) → [`00540728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md) FUN_00540728

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`004b059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b059c.md) [`004b074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b074c.md) [`004b2774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2774.md) [`004c6108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6108.md) [`004f9b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9b48.md) · 呼出先 8件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 8件 [`004b08bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b0/004b08bc.md) [`004b0a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b0/004b0a6c.md) [`004b2a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2a94.md) [`004c6428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6428.md) [`004f9e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f9/004f9e68.md) · 呼出先 8件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00540818",
      "incomplete_value": true,
      "site": "00540820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005404f8",
      "incomplete_value": true,
      "site": "00540500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054081c",
      "incomplete_value": true,
      "site": "00540820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005404fc",
      "incomplete_value": true,
      "site": "00540500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00540818",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00540818",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0054081c",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00540818",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00540818",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0054081c",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md#insn-00540500) · [`00540454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md#insn-00540454) · [`00540480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md#insn-00540480)
- 新版 [`00540820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md#insn-00540820) · [`00540774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md#insn-00540774) · [`005407a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md#insn-005407a0)

~~~diff
- 00540500 ["INT_ADD", "register:40f0:8", ["const:540500:8", "const:4:8"]]
- 00540500 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00540820 ["INT_ADD", "register:40f0:8", ["const:540820:8", "const:4:8"]]
+ 00540820 ["CALL", null, ["callee:00c58fb0:8"]]
- 00540500 bytes b85e1c94
+ 00540820 bytes e4611c94
- 00540454 ["INT_ADD", "register:40f0:8", ["const:540454:8", "const:4:8"]]
- 00540454 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00540774 ["INT_ADD", "register:40f0:8", ["const:540774:8", "const:4:8"]]
+ 00540774 ["CALL", null, ["callee:00c59ad0:8"]]
- 00540454 bytes ab611c94
+ 00540774 bytes d7641c94
- 00540480 ["INT_ADD", "register:40f0:8", ["const:540480:8", "const:4:8"]]
- 00540480 ["CALL", null, ["callee:00c590a0:8"]]
+ 005407a0 ["INT_ADD", "register:40f0:8", ["const:5407a0:8", "const:4:8"]]
+ 005407a0 ["CALL", null, ["callee:00c590a0:8"]]
- 00540480 bytes 145f1c94
+ 005407a0 bytes 40621c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e7fbc91f1db8534c1b45eec2091896b"></a>

### [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) → [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) FUN_0054084c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 44件 [`004a1394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1394.md) [`004a5348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5348.md) [`004a55dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) [`004a5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5efc.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) · 呼出先 11件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 44件 [`004a16b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a16b4.md) [`004a5668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5668.md) [`004a58fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a58fc.md) [`004a621c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a621c.md) [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md) · 呼出先 11件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005408e0",
      "incomplete_value": true,
      "site": "005408e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405c0",
      "incomplete_value": true,
      "site": "005405c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405c4",
      "incomplete_value": true,
      "site": "005405c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
      "005408e0",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "005408e0",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005408e4",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005408e0",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "005408e0",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005408e4",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005405c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md#insn-005405c8) · [`00540598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md#insn-00540598) · [`005405a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md#insn-005405a8)
- 新版 [`005408e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md#insn-005408e8) · [`005408b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md#insn-005408b8) · [`005408c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md#insn-005408c8)

~~~diff
- 005405c8 ["INT_ADD", "register:40f0:8", ["const:5405c8:8", "const:4:8"]]
- 005405c8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005408e8 ["INT_ADD", "register:40f0:8", ["const:5408e8:8", "const:4:8"]]
+ 005408e8 ["CALL", null, ["callee:00c58fb0:8"]]
- 005405c8 bytes 865e1c94
+ 005408e8 bytes b2611c94
- 00540598 ["INT_ADD", "register:40f0:8", ["const:540598:8", "const:4:8"]]
- 00540598 ["CALL", null, ["callee:00c59ad0:8"]]
+ 005408b8 ["INT_ADD", "register:40f0:8", ["const:5408b8:8", "const:4:8"]]
+ 005408b8 ["CALL", null, ["callee:00c59ad0:8"]]
- 00540598 bytes 5a611c94
+ 005408b8 bytes 86641c94
- 005405a8 ["INT_ADD", "register:40f0:8", ["const:5405a8:8", "const:4:8"]]
- 005405a8 ["CALL", null, ["callee:00c58f90:8"]]
+ 005408c8 ["INT_ADD", "register:40f0:8", ["const:5408c8:8", "const:4:8"]]
+ 005408c8 ["CALL", null, ["callee:00c58f90:8"]]
- 005405a8 bytes 865e1c94
+ 005408c8 bytes b2611c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f6af295953e082a3eb75393412e3e7"></a>

### [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) → [`00540c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md) FUN_00540c1c

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0051b15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md) [`0051c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c84c.md) [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) [`005283e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 6件 [`0051b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b47c.md) [`0051cb6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051c/0051cb6c.md) [`00526d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md) [`00528188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528188.md) [`00528704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00528/00528704.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00540c28",
      "incomplete_value": true,
      "site": "00540c2c",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540908",
      "incomplete_value": true,
      "site": "0054090c",
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
      "00540c28",
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
      "00540c28",
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

- 旧版 [`0054090c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md#insn-0054090c) · [`00540904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md#insn-00540904) · [`00540908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md#insn-00540908)
- 新版 [`00540c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md#insn-00540c2c) · [`00540c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md#insn-00540c24) · [`00540c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c1c.md#insn-00540c28)

~~~diff
- 0054090c ["INT_ADD", "register:40f0:8", ["const:54090c:8", "const:4:8"]]
- 0054090c ["CALL", null, ["callee:00442c90:8"]]
+ 00540c2c ["INT_ADD", "register:40f0:8", ["const:540c2c:8", "const:4:8"]]
+ 00540c2c ["CALL", null, ["callee:00442c90:8"]]
- 0054090c bytes 1908fc97
+ 00540c2c bytes 1908fc97
- 00540904 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00540c24 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00540904 bytes a0ebfff0
+ 00540c24 bytes c0ebff90
- 00540908 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00540908 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00540908 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00540908 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00540c28 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00540c28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00540c28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00540c28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00540908 bytes 00303e91
+ 00540c28 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95a1f6d707f2d1cfc8f40d9f39b58bfa"></a>

### [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) → [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md) FUN_00540c80

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 24件 [`004a1394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1394.md) [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) [`004b7758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7758.md) [`004b7c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7c50.md) [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) · 呼出先 11件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 24件 [`004a16b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a16b4.md) [`004b6a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b6a88.md) [`004b7a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7a78.md) [`004b7f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b7/004b7f70.md) [`004b8328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8328.md) · 呼出先 11件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00536694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00540d24",
      "incomplete_value": true,
      "site": "00540d28",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540a04",
      "incomplete_value": true,
      "site": "00540a08",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00540da4",
      "incomplete_value": true,
      "site": "00540da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540a84",
      "incomplete_value": true,
      "site": "00540a84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
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
      "00540d20",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00540d20",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540d24",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00540d20",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00540d20",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540d24",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md#insn-00540a08) · [`00540a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md#insn-00540a84) · [`005409d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md#insn-005409d4)
- 新版 [`00540d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md#insn-00540d28) · [`00540da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md#insn-00540da4) · [`00540cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md#insn-00540cf4)

~~~diff
- 00540a08 ["INT_ADD", "register:40f0:8", ["const:540a08:8", "const:4:8"]]
- 00540a08 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00540d28 ["INT_ADD", "register:40f0:8", ["const:540d28:8", "const:4:8"]]
+ 00540d28 ["CALL", null, ["callee:00c58fb0:8"]]
- 00540a08 bytes 765d1c94
+ 00540d28 bytes a2601c94
- 00540a84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00540a84 ["INT_ADD", "register:40f0:8", ["const:540a84:8", "const:4:8"]]
- 00540a84 ["CALLIND", null, ["register:0:8"]]
+ 00540da4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00540da4 ["INT_ADD", "register:40f0:8", ["const:540da4:8", "const:4:8"]]
+ 00540da4 ["CALLIND", null, ["register:0:8"]]
- 00540a84 bytes 00013fd6
+ 00540da4 bytes 00013fd6
- 005409d4 ["INT_ADD", "register:40f0:8", ["const:5409d4:8", "const:4:8"]]
- 005409d4 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00540cf4 ["INT_ADD", "register:40f0:8", ["const:540cf4:8", "const:4:8"]]
+ 00540cf4 ["CALL", null, ["callee:00c59ad0:8"]]
- 005409d4 bytes 4b601c94
+ 00540cf4 bytes 77631c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbf14e3af97fa724ab7dc420efa58b4e"></a>

### [`00540ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md) → [`00540de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md) FUN_00540de8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004a1af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md) [`004a1e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md) [`004a212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md) · 呼出先 8件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 3件 [`004a1e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md) [`004a2130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md) [`004a244c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md) · 呼出先 8件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00540e54",
      "incomplete_value": true,
      "site": "00540e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540b34",
      "incomplete_value": true,
      "site": "00540b3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "00540e58",
      "incomplete_value": true,
      "site": "00540e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540b38",
      "incomplete_value": true,
      "site": "00540b3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00540e98",
      "incomplete_value": true,
      "site": "00540e98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540b78",
      "incomplete_value": true,
      "site": "00540b78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00540e54",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00540e54",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540e58",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00540e54",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00540e54",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540e58",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md#insn-00540b3c) · [`00540b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md#insn-00540b78) · [`00540b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540ac8.md#insn-00540b0c)
- 新版 [`00540e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md#insn-00540e5c) · [`00540e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md#insn-00540e98) · [`00540e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540de8.md#insn-00540e2c)

~~~diff
- 00540b3c ["INT_ADD", "register:40f0:8", ["const:540b3c:8", "const:4:8"]]
- 00540b3c ["CALL", null, ["callee:00c58fb0:8"]]
+ 00540e5c ["INT_ADD", "register:40f0:8", ["const:540e5c:8", "const:4:8"]]
+ 00540e5c ["CALL", null, ["callee:00c58fb0:8"]]
- 00540b3c bytes 295d1c94
+ 00540e5c bytes 55601c94
- 00540b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00540b78 ["INT_ADD", "register:40f0:8", ["const:540b78:8", "const:4:8"]]
- 00540b78 ["CALLIND", null, ["register:0:8"]]
+ 00540e98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00540e98 ["INT_ADD", "register:40f0:8", ["const:540e98:8", "const:4:8"]]
+ 00540e98 ["CALLIND", null, ["register:0:8"]]
- 00540b78 bytes 00013fd6
+ 00540e98 bytes 00013fd6
- 00540b0c ["INT_ADD", "register:40f0:8", ["const:540b0c:8", "const:4:8"]]
- 00540b0c ["CALL", null, ["callee:00c59ad0:8"]]
+ 00540e2c ["INT_ADD", "register:40f0:8", ["const:540e2c:8", "const:4:8"]]
+ 00540e2c ["CALL", null, ["callee:00c59ad0:8"]]
- 00540b0c bytes fd5f1c94
+ 00540e2c bytes 29631c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9bcf13496c0e21e5dcace6e57244c83"></a>

### [`00540bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md) → [`00540ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md) FUN_00540ed8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004a1af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1af4.md) [`004a1e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1e10.md) [`004a212c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a212c.md) [`004cd180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cd/004cd180.md) · 呼出先 8件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 4件 [`004a1e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a1/004a1e14.md) [`004a2130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2130.md) [`004a244c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a244c.md) [`004cd4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cd/004cd4a0.md) · 呼出先 8件 [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00540f40",
      "incomplete_value": true,
      "site": "00540f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540c20",
      "incomplete_value": true,
      "site": "00540c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "00540f44",
      "incomplete_value": true,
      "site": "00540f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540c24",
      "incomplete_value": true,
      "site": "00540c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00540f84",
      "incomplete_value": true,
      "site": "00540f84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540c64",
      "incomplete_value": true,
      "site": "00540c64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00540f40",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00540f40",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540f44",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00540f40",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00540f40",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00540f44",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md#insn-00540c28) · [`00540c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md#insn-00540c64) · [`00540bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540bb8.md#insn-00540bf8)
- 新版 [`00540f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md#insn-00540f48) · [`00540f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md#insn-00540f84) · [`00540f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540ed8.md#insn-00540f18)

~~~diff
- 00540c28 ["INT_ADD", "register:40f0:8", ["const:540c28:8", "const:4:8"]]
- 00540c28 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00540f48 ["INT_ADD", "register:40f0:8", ["const:540f48:8", "const:4:8"]]
+ 00540f48 ["CALL", null, ["callee:00c58fb0:8"]]
- 00540c28 bytes ee5c1c94
+ 00540f48 bytes 1a601c94
- 00540c64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00540c64 ["INT_ADD", "register:40f0:8", ["const:540c64:8", "const:4:8"]]
- 00540c64 ["CALLIND", null, ["register:0:8"]]
+ 00540f84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00540f84 ["INT_ADD", "register:40f0:8", ["const:540f84:8", "const:4:8"]]
+ 00540f84 ["CALLIND", null, ["register:0:8"]]
- 00540c64 bytes 00013fd6
+ 00540f84 bytes 00013fd6
- 00540bf8 ["INT_ADD", "register:40f0:8", ["const:540bf8:8", "const:4:8"]]
- 00540bf8 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00540f18 ["INT_ADD", "register:40f0:8", ["const:540f18:8", "const:4:8"]]
+ 00540f18 ["CALL", null, ["callee:00c59ad0:8"]]
- 00540bf8 bytes c25f1c94
+ 00540f18 bytes ee621c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec8ed634071bba68fcca8d9c14bd558"></a>

### [`00540f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md) → [`0054128c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/0054128c.md) FUN_0054128c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004b18ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b18ac.md) · 呼出先 9件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`004b1bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b1/004b1bcc.md) · 呼出先 9件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.25% / 新版 94.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005412dc",
      "incomplete_value": true,
      "site": "005412dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540fbc",
      "incomplete_value": true,
      "site": "00540fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005413dc",
      "incomplete_value": true,
      "site": "005413e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005410bc",
      "incomplete_value": true,
      "site": "005410c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "005413e0",
      "incomplete_value": true,
      "site": "005413e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005410c0",
      "incomplete_value": true,
      "site": "005410c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005412d0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005413dc",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "005413dc",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005412d0",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005413dc",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "005413dc",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md#insn-00540fbc) · [`005410c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md#insn-005410c4) · [`00540fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md#insn-00540fa8)
- 新版 [`005412dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/0054128c.md#insn-005412dc) · [`005413e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/0054128c.md#insn-005413e4) · [`005412c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/0054128c.md#insn-005412c8)

~~~diff
- 00540fbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00540fbc ["INT_ADD", "register:40f0:8", ["const:540fbc:8", "const:4:8"]]
- 00540fbc ["CALLIND", null, ["register:0:8"]]
+ 005412dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005412dc ["INT_ADD", "register:40f0:8", ["const:5412dc:8", "const:4:8"]]
+ 005412dc ["CALLIND", null, ["register:0:8"]]
- 00540fbc bytes 00013fd6
+ 005412dc bytes 00013fd6
- 005410c4 ["INT_ADD", "register:40f0:8", ["const:5410c4:8", "const:4:8"]]
- 005410c4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005413e4 ["INT_ADD", "register:40f0:8", ["const:5413e4:8", "const:4:8"]]
+ 005413e4 ["CALL", null, ["callee:00c58fb0:8"]]
- 005410c4 bytes c75b1c94
+ 005413e4 bytes f35e1c94
- 00540fa8 ["COPY", "register:4040:8", ["const:c67000:8"]]
+ 005412c8 ["COPY", "register:4040:8", ["const:c68000:8"]]
- 00540fa8 bytes 283900f0
+ 005412c8 bytes 283900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e185d773e9b82f62fc8d599937e9a46b"></a>

### [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) → [`00541504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541504.md) FUN_00541504

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004b2294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) [`004b2600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) [`004b318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b318c.md) [`004d02cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md) [`004d0794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0794.md) · 呼出先 10件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 6件 [`004b25b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b25b4.md) [`004b2920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2920.md) [`004b34ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b34ac.md) [`004d05ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d0/004d05ec.md) [`004d0ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d0/004d0ab4.md) · 呼出先 10件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054158c",
      "incomplete_value": true,
      "site": "00541594",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054126c",
      "incomplete_value": true,
      "site": "00541274",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00541590",
      "incomplete_value": true,
      "site": "00541594",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541270",
      "incomplete_value": true,
      "site": "00541274",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
      "0054158c",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "0054158c",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00541590",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054158c",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "0054158c",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00541590",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md#insn-00541274) · [`00541244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md#insn-00541244) · [`00541254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md#insn-00541254)
- 新版 [`00541594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541504.md#insn-00541594) · [`00541564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541504.md#insn-00541564) · [`00541574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541504.md#insn-00541574)

~~~diff
- 00541274 ["INT_ADD", "register:40f0:8", ["const:541274:8", "const:4:8"]]
- 00541274 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00541594 ["INT_ADD", "register:40f0:8", ["const:541594:8", "const:4:8"]]
+ 00541594 ["CALL", null, ["callee:00c58fb0:8"]]
- 00541274 bytes 5b5b1c94
+ 00541594 bytes 875e1c94
- 00541244 ["INT_ADD", "register:40f0:8", ["const:541244:8", "const:4:8"]]
- 00541244 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00541564 ["INT_ADD", "register:40f0:8", ["const:541564:8", "const:4:8"]]
+ 00541564 ["CALL", null, ["callee:00c59ad0:8"]]
- 00541244 bytes 2f5e1c94
+ 00541564 bytes 5b611c94
- 00541254 ["INT_ADD", "register:40f0:8", ["const:541254:8", "const:4:8"]]
- 00541254 ["CALL", null, ["callee:00c58f90:8"]]
+ 00541574 ["INT_ADD", "register:40f0:8", ["const:541574:8", "const:4:8"]]
+ 00541574 ["CALL", null, ["callee:00c58f90:8"]]
- 00541254 bytes 5b5b1c94
+ 00541574 bytes 875e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b803e653a0a06d25674aa5207c72bb"></a>

### [`00541b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541b68.md) → [`00541e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541e88.md) FUN_00541e88

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005412f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005412f0.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00541610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541610.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00542134",
      "incomplete_value": true,
      "site": "00542134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541e14",
      "incomplete_value": true,
      "site": "00541e14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00542184",
      "incomplete_value": true,
      "site": "00542184",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541e64",
      "incomplete_value": true,
      "site": "00541e64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00542124",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00542174",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00542124",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00542174",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541b68.md#insn-00541e14) · [`00541e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541b68.md#insn-00541e64) · [`00541dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541b68.md#insn-00541dfc)
- 新版 [`00542134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541e88.md#insn-00542134) · [`00542184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541e88.md#insn-00542184) · [`0054211c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541e88.md#insn-0054211c)

~~~diff
- 00541e14 ["COPY", "register:0:8", ["register:4048:8"]]
- 00541e14 ["INT_ADD", "register:40f0:8", ["const:541e14:8", "const:4:8"]]
- 00541e14 ["CALLIND", null, ["register:0:8"]]
+ 00542134 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00542134 ["INT_ADD", "register:40f0:8", ["const:542134:8", "const:4:8"]]
+ 00542134 ["CALLIND", null, ["register:0:8"]]
- 00541e14 bytes 20013fd6
+ 00542134 bytes 20013fd6
- 00541e64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00541e64 ["INT_ADD", "register:40f0:8", ["const:541e64:8", "const:4:8"]]
- 00541e64 ["CALLIND", null, ["register:0:8"]]
+ 00542184 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00542184 ["INT_ADD", "register:40f0:8", ["const:542184:8", "const:4:8"]]
+ 00542184 ["CALLIND", null, ["register:0:8"]]
- 00541e64 bytes 20013fd6
+ 00542184 bytes 20013fd6
- 00541dfc ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 0054211c ["COPY", "register:4048:8", ["const:c68000:8"]]
- 00541dfc bytes 293900d0
+ 0054211c bytes 293900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a6a02ca5b2178a8d174376ceaff6dbf"></a>

### [`00541e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541e9c.md) → [`005421bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/005421bc.md) FUN_005421bc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005412f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005412f0.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00541610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/00541610.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00542454",
      "incomplete_value": true,
      "site": "00542454",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542134",
      "incomplete_value": true,
      "site": "00542134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005424a4",
      "incomplete_value": true,
      "site": "005424a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542184",
      "incomplete_value": true,
      "site": "00542184",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00542444",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00542494",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00542444",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00542494",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541e9c.md#insn-00542134) · [`00542184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541e9c.md#insn-00542184) · [`0054211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/00541e9c.md#insn-0054211c)
- 新版 [`00542454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/005421bc.md#insn-00542454) · [`005424a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/005421bc.md#insn-005424a4) · [`0054243c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/005421bc.md#insn-0054243c)

~~~diff
- 00542134 ["COPY", "register:0:8", ["register:4048:8"]]
- 00542134 ["INT_ADD", "register:40f0:8", ["const:542134:8", "const:4:8"]]
- 00542134 ["CALLIND", null, ["register:0:8"]]
+ 00542454 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00542454 ["INT_ADD", "register:40f0:8", ["const:542454:8", "const:4:8"]]
+ 00542454 ["CALLIND", null, ["register:0:8"]]
- 00542134 bytes 20013fd6
+ 00542454 bytes 20013fd6
- 00542184 ["COPY", "register:0:8", ["register:4048:8"]]
- 00542184 ["INT_ADD", "register:40f0:8", ["const:542184:8", "const:4:8"]]
- 00542184 ["CALLIND", null, ["register:0:8"]]
+ 005424a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005424a4 ["INT_ADD", "register:40f0:8", ["const:5424a4:8", "const:4:8"]]
+ 005424a4 ["CALLIND", null, ["register:0:8"]]
- 00542184 bytes 20013fd6
+ 005424a4 bytes 20013fd6
- 0054211c ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 0054243c ["COPY", "register:4048:8", ["const:c68000:8"]]
- 0054211c bytes 293900b0
+ 0054243c bytes 293900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2ad96a33d14e89f5bee5225d3901fe"></a>

### [`00542cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542cc4.md) → [`00542fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/00542fe4.md) FUN_00542fe4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00542a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542a10.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00542d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/00542d30.md) · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005430e0",
      "incomplete_value": true,
      "site": "005430e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542dc0",
      "incomplete_value": true,
      "site": "00542dc0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
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
      "005430d0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005430d0",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542cc4.md#insn-00542dc0) · [`00542cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542cc4.md#insn-00542cfc) · [`00542db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542cc4.md#insn-00542db0)
- 新版 [`005430e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/00542fe4.md#insn-005430e0) · [`0054301c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/00542fe4.md#insn-0054301c) · [`005430d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00542/00542fe4.md#insn-005430d0)

~~~diff
- 00542dc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00542dc0 ["INT_ADD", "register:40f0:8", ["const:542dc0:8", "const:4:8"]]
- 00542dc0 ["CALLIND", null, ["register:0:8"]]
+ 005430e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005430e0 ["INT_ADD", "register:40f0:8", ["const:5430e0:8", "const:4:8"]]
+ 005430e0 ["CALLIND", null, ["register:0:8"]]
- 00542dc0 bytes 20013fd6
+ 005430e0 bytes 20013fd6
- 00542cfc ["COPY", "register:40d0:8", ["const:c67000:8"]]
+ 0054301c ["COPY", "register:40d0:8", ["const:c68000:8"]]
- 00542cfc bytes 3a3900b0
+ 0054301c bytes 3a3900b0
- 00542db0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:808:8"]]
- 00542db0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005430d0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:7d8:8"]]
+ 005430d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00542db0 bytes 490744f9
+ 005430d0 bytes 49ef43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a0090f6bc1af338103c83f1f2efa3aa"></a>

### [`00542df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542df8.md) → [`00543118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543118.md) FUN_00543118

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b2774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2774.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00542fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fb4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 1件 [`004b2a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b2/004b2a94.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005432d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432d4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00543274",
      "incomplete_value": true,
      "site": "00543274",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542f54",
      "incomplete_value": true,
      "site": "00542f54",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "00543264",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00543264",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542df8.md#insn-00542f54) · [`00542e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542df8.md#insn-00542e88) · [`00542f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542df8.md#insn-00542f18)
- 新版 [`00543274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543118.md#insn-00543274) · [`005431a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543118.md#insn-005431a8) · [`00543238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543118.md#insn-00543238)

~~~diff
- 00542f54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00542f54 ["INT_ADD", "register:40f0:8", ["const:542f54:8", "const:4:8"]]
- 00542f54 ["CALLIND", null, ["register:0:8"]]
+ 00543274 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00543274 ["INT_ADD", "register:40f0:8", ["const:543274:8", "const:4:8"]]
+ 00543274 ["CALLIND", null, ["register:0:8"]]
- 00542f54 bytes 20013fd6
+ 00543274 bytes 20013fd6
- 00542e88 ["INT_ADD", "register:40f0:8", ["const:542e88:8", "const:4:8"]]
- 00542e88 ["CALL", null, ["callee:00c58f30:8"]]
+ 005431a8 ["INT_ADD", "register:40f0:8", ["const:5431a8:8", "const:4:8"]]
+ 005431a8 ["CALL", null, ["callee:00c58f30:8"]]
- 00542e88 bytes 36541c94
+ 005431a8 bytes 62571c94
- 00542f18 ["COPY", "register:40e0:8", ["const:c67000:8"]]
+ 00543238 ["COPY", "register:40e0:8", ["const:c68000:8"]]
- 00542f18 bytes 3c3900b0
+ 00543238 bytes 3c3900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cac4eb0fc46aa4d3be44e69d9f28012d"></a>

### [`00542fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fb4.md) → [`005432d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432d4.md) FUN_005432d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00542df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542df8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00543118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543118.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005432e0",
      "incomplete_value": false,
      "site": "005432e4",
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
      "definition_site": "00542fc0",
      "incomplete_value": false,
      "site": "00542fc4",
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
      "005432e0",
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
      "005432e0",
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

- 旧版 [`00542fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fb4.md#insn-00542fc4) · [`00542fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fb4.md#insn-00542fbc) · [`00542fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fb4.md#insn-00542fc0)
- 新版 [`005432e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432d4.md#insn-005432e4) · [`005432dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432d4.md#insn-005432dc) · [`005432e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432d4.md#insn-005432e0)

~~~diff
- 00542fc4 ["INT_ADD", "register:40f0:8", ["const:542fc4:8", "const:4:8"]]
- 00542fc4 ["CALL", null, ["callee:0043bad8:8"]]
+ 005432e4 ["INT_ADD", "register:40f0:8", ["const:5432e4:8", "const:4:8"]]
+ 005432e4 ["CALL", null, ["callee:0043bad8:8"]]
- 00542fc4 bytes fde1fb97
+ 005432e4 bytes fde1fb97
- 00542fbc ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005432dc ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00542fbc bytes a0ebffb0
+ 005432dc bytes a0ebffb0
- 00542fc0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00542fc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00542fc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00542fc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005432e0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005432e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005432e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005432e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00542fc0 bytes 00303e91
+ 005432e0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf311df59a42d87baacf0c12072dbf9"></a>

### [`0054317c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054317c.md) → [`0054349c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054349c.md) FUN_0054349c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00542fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fc8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005432e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005432e8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005434a8",
      "incomplete_value": false,
      "site": "005434ac",
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
      "definition_site": "00543188",
      "incomplete_value": false,
      "site": "0054318c",
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
      "005434a8",
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
      "005434a8",
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

- 旧版 [`0054318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054317c.md#insn-0054318c) · [`00543184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054317c.md#insn-00543184) · [`00543188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054317c.md#insn-00543188)
- 新版 [`005434ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054349c.md#insn-005434ac) · [`005434a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054349c.md#insn-005434a4) · [`005434a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054349c.md#insn-005434a8)

~~~diff
- 0054318c ["INT_ADD", "register:40f0:8", ["const:54318c:8", "const:4:8"]]
- 0054318c ["CALL", null, ["callee:0043bad8:8"]]
+ 005434ac ["INT_ADD", "register:40f0:8", ["const:5434ac:8", "const:4:8"]]
+ 005434ac ["CALL", null, ["callee:0043bad8:8"]]
- 0054318c bytes 8be1fb97
+ 005434ac bytes 8be1fb97
- 00543184 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005434a4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00543184 bytes a0ebff90
+ 005434a4 bytes a0ebffb0
- 00543188 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00543188 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00543188 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00543188 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005434a8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005434a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005434a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005434a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00543188 bytes 00303e91
+ 005434a8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b658805ab794188950777c9ec12f3905"></a>

### [`005433ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/005433ec.md) → [`0054370c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054370c.md) FUN_0054370c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00543190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543190.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005434b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/005434b0.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00543718",
      "incomplete_value": false,
      "site": "0054371c",
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
      "definition_site": "005433f8",
      "incomplete_value": false,
      "site": "005433fc",
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
      "00543718",
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
      "00543718",
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

- 旧版 [`005433fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/005433ec.md#insn-005433fc) · [`005433f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/005433ec.md#insn-005433f4) · [`005433f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/005433ec.md#insn-005433f8)
- 新版 [`0054371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054370c.md#insn-0054371c) · [`00543714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054370c.md#insn-00543714) · [`00543718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/0054370c.md#insn-00543718)

~~~diff
- 005433fc ["INT_ADD", "register:40f0:8", ["const:5433fc:8", "const:4:8"]]
- 005433fc ["CALL", null, ["callee:0043bad8:8"]]
+ 0054371c ["INT_ADD", "register:40f0:8", ["const:54371c:8", "const:4:8"]]
+ 0054371c ["CALL", null, ["callee:0043bad8:8"]]
- 005433fc bytes efe0fb97
+ 0054371c bytes efe0fb97
- 005433f4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00543714 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005433f4 bytes a0ebff90
+ 00543714 bytes a0ebffb0
- 005433f8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005433f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005433f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005433f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00543718 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00543718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00543718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00543718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005433f8 bytes 00303e91
+ 00543718 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5af1aeef929d234b23d76a53bdf31af"></a>

### [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md) → [`00543720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md) FUN_00543720

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004b5010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5010.md) [`004bcb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md) [`004c602c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c602c.md) · 呼出先 10件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 3件 [`004b5330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b5/004b5330.md) [`004bceb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bc/004bceb4.md) [`004c634c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c634c.md) · 呼出先 10件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00543770",
      "incomplete_value": true,
      "site": "00543770",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543450",
      "incomplete_value": true,
      "site": "00543450",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543878",
      "incomplete_value": true,
      "site": "00543880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543558",
      "incomplete_value": true,
      "site": "00543560",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054387c",
      "incomplete_value": true,
      "site": "00543880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054355c",
      "incomplete_value": true,
      "site": "00543560",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
      "00543764",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00543878",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00543878",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00543764",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00543878",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00543878",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00543450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md#insn-00543450) · [`00543560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md#insn-00543560) · [`0054343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md#insn-0054343c)
- 新版 [`00543770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md#insn-00543770) · [`00543880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md#insn-00543880) · [`0054375c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543720.md#insn-0054375c)

~~~diff
- 00543450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00543450 ["INT_ADD", "register:40f0:8", ["const:543450:8", "const:4:8"]]
- 00543450 ["CALLIND", null, ["register:0:8"]]
+ 00543770 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00543770 ["INT_ADD", "register:40f0:8", ["const:543770:8", "const:4:8"]]
+ 00543770 ["CALLIND", null, ["register:0:8"]]
- 00543450 bytes 00013fd6
+ 00543770 bytes 00013fd6
- 00543560 ["INT_ADD", "register:40f0:8", ["const:543560:8", "const:4:8"]]
- 00543560 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00543880 ["INT_ADD", "register:40f0:8", ["const:543880:8", "const:4:8"]]
+ 00543880 ["CALL", null, ["callee:00c58fb0:8"]]
- 00543560 bytes a0521c94
+ 00543880 bytes cc551c94
- 0054343c ["COPY", "register:4040:8", ["const:c67000:8"]]
+ 0054375c ["COPY", "register:4040:8", ["const:c68000:8"]]
- 0054343c bytes 28390090
+ 0054375c bytes 283900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27022fac9e72ffb85cbdee4732e82eb"></a>

### [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md) → [`00543a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md) FUN_00543a3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) [`004bace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bace0.md) [`004def44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004def44.md) [`004def88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004def88.md) [`004df660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004df/004df660.md) · 呼出先 10件 [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 12件 [`004b6a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b6/004b6a88.md) [`004bb000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bb000.md) [`004df264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004df/004df264.md) [`004df2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004df/004df2a8.md) [`004df980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004df/004df980.md) · 呼出先 10件 [`00536694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543ba8",
      "incomplete_value": true,
      "site": "00543bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543888",
      "incomplete_value": true,
      "site": "00543890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543bac",
      "incomplete_value": true,
      "site": "00543bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054388c",
      "incomplete_value": true,
      "site": "00543890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
      "00543a80",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00543ba8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00543ba8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00543a80",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00543ba8",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00543ba8",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00543890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md#insn-00543890) · [`00543758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md#insn-00543758) · [`00543760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md#insn-00543760)
- 新版 [`00543bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md#insn-00543bb0) · [`00543a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md#insn-00543a78) · [`00543a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md#insn-00543a80)

~~~diff
- 00543890 ["INT_ADD", "register:40f0:8", ["const:543890:8", "const:4:8"]]
- 00543890 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00543bb0 ["INT_ADD", "register:40f0:8", ["const:543bb0:8", "const:4:8"]]
+ 00543bb0 ["CALL", null, ["callee:00c58fb0:8"]]
- 00543890 bytes d4511c94
+ 00543bb0 bytes 00551c94
- 00543758 ["COPY", "register:4040:8", ["const:c67000:8"]]
+ 00543a78 ["COPY", "register:4040:8", ["const:c68000:8"]]
- 00543758 bytes 28390090
+ 00543a78 bytes 283900b0
- 00543760 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
- 00543760 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00543a80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d8:8"]]
+ 00543a80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00543760 bytes 080544f9
+ 00543a80 bytes 08ed43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe176c9fbce73e6fc57ae36e704a4532"></a>

### [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md) → [`00543bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md) FUN_00543bb8

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`004a8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) [`004b0430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0430.md) [`004bcd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md) [`004c1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md) [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) · 呼出先 10件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 5件 [`004a8c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a8/004a8c48.md) [`004b0750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b0/004b0750.md) [`004bd06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bd/004bd06c.md) [`004c21a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c21a4.md) [`004ed070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ed/004ed070.md) · 呼出先 10件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00543c08",
      "incomplete_value": true,
      "site": "00543c08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005438e8",
      "incomplete_value": true,
      "site": "005438e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543d10",
      "incomplete_value": true,
      "site": "00543d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005439f0",
      "incomplete_value": true,
      "site": "005439f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543d14",
      "incomplete_value": true,
      "site": "00543d18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005439f4",
      "incomplete_value": true,
      "site": "005439f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
      "00543bfc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00543d10",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00543d10",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00543bfc",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00543d10",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00543d10",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005438e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md#insn-005438e8) · [`005439f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md#insn-005439f8) · [`005438d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md#insn-005438d4)
- 新版 [`00543c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md#insn-00543c08) · [`00543d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md#insn-00543d18) · [`00543bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543bb8.md#insn-00543bf4)

~~~diff
- 005438e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005438e8 ["INT_ADD", "register:40f0:8", ["const:5438e8:8", "const:4:8"]]
- 005438e8 ["CALLIND", null, ["register:0:8"]]
+ 00543c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00543c08 ["INT_ADD", "register:40f0:8", ["const:543c08:8", "const:4:8"]]
+ 00543c08 ["CALLIND", null, ["register:0:8"]]
- 005438e8 bytes 00013fd6
+ 00543c08 bytes 00013fd6
- 005439f8 ["INT_ADD", "register:40f0:8", ["const:5439f8:8", "const:4:8"]]
- 005439f8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00543d18 ["INT_ADD", "register:40f0:8", ["const:543d18:8", "const:4:8"]]
+ 00543d18 ["CALL", null, ["callee:00c58fb0:8"]]
- 005439f8 bytes 7a511c94
+ 00543d18 bytes a6541c94
- 005438d4 ["COPY", "register:4040:8", ["const:c67000:8"]]
+ 00543bf4 ["COPY", "register:4040:8", ["const:c68000:8"]]
- 005438d4 bytes 28390090
+ 00543bf4 bytes 283900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b96d822fe081ea1ad98da799e473589"></a>

### [`00543a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md) → [`00543d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d20.md) FUN_00543d20

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004beee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004beee0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`004bf200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bf/004bf200.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00543d2c",
      "incomplete_value": false,
      "site": "00543d30",
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
      "definition_site": "00543a0c",
      "incomplete_value": false,
      "site": "00543a10",
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
      "00543d2c",
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
      "00543d2c",
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

- 旧版 [`00543a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md#insn-00543a10) · [`00543a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md#insn-00543a08) · [`00543a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a00.md#insn-00543a0c)
- 新版 [`00543d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d20.md#insn-00543d30) · [`00543d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d20.md#insn-00543d28) · [`00543d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d20.md#insn-00543d2c)

~~~diff
- 00543a10 ["INT_ADD", "register:40f0:8", ["const:543a10:8", "const:4:8"]]
- 00543a10 ["CALL", null, ["callee:0043bad8:8"]]
+ 00543d30 ["INT_ADD", "register:40f0:8", ["const:543d30:8", "const:4:8"]]
+ 00543d30 ["CALL", null, ["callee:0043bad8:8"]]
- 00543a10 bytes 6adffb97
+ 00543d30 bytes 6adffb97
- 00543a08 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00543d28 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00543a08 bytes a0ebff90
+ 00543d28 bytes a0ebffb0
- 00543a0c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00543a0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00543a0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00543a0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00543d2c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00543d2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00543d2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00543d2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00543a0c bytes 00303e91
+ 00543d2c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-983bf42030a2af59c7797396096742d0"></a>

### [`00543a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a14.md) → [`00543d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d34.md) FUN_00543d34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d7c.md) · 呼出先 11件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`004c309c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c309c.md) · 呼出先 11件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00543de8",
      "incomplete_value": true,
      "site": "00543df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543ac8",
      "incomplete_value": true,
      "site": "00543ad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "00543dec",
      "incomplete_value": true,
      "site": "00543df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543acc",
      "incomplete_value": true,
      "site": "00543ad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00543ed4",
      "incomplete_value": true,
      "site": "00543ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00543bb4",
      "incomplete_value": true,
      "site": "00543bb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00543de8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00543de8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00543dec",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00543de8",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00543de8",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00543dec",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00543ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a14.md#insn-00543ad0) · [`00543bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a14.md#insn-00543bb4) · [`00543aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543a14.md#insn-00543aa0)
- 新版 [`00543df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d34.md#insn-00543df0) · [`00543ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d34.md#insn-00543ed4) · [`00543dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543d34.md#insn-00543dc0)

~~~diff
- 00543ad0 ["INT_ADD", "register:40f0:8", ["const:543ad0:8", "const:4:8"]]
- 00543ad0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00543df0 ["INT_ADD", "register:40f0:8", ["const:543df0:8", "const:4:8"]]
+ 00543df0 ["CALL", null, ["callee:00c58fb0:8"]]
- 00543ad0 bytes 44511c94
+ 00543df0 bytes 70541c94
- 00543bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00543bb4 ["INT_ADD", "register:40f0:8", ["const:543bb4:8", "const:4:8"]]
- 00543bb4 ["CALLIND", null, ["register:0:8"]]
+ 00543ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00543ed4 ["INT_ADD", "register:40f0:8", ["const:543ed4:8", "const:4:8"]]
+ 00543ed4 ["CALLIND", null, ["register:0:8"]]
- 00543bb4 bytes 00013fd6
+ 00543ed4 bytes 00013fd6
- 00543aa0 ["INT_ADD", "register:40f0:8", ["const:543aa0:8", "const:4:8"]]
- 00543aa0 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00543dc0 ["INT_ADD", "register:40f0:8", ["const:543dc0:8", "const:4:8"]]
+ 00543dc0 ["CALL", null, ["callee:00c59ad0:8"]]
- 00543aa0 bytes 18541c94
+ 00543dc0 bytes 44571c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d8db1bd241c79fdce78e1097f53492"></a>

### [`00543c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md) → [`00543fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fa8.md) FUN_00543fa8

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c332c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c332c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`004c364c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c3/004c364c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00543fb4",
      "incomplete_value": false,
      "site": "00543fb8",
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
      "definition_site": "00543c94",
      "incomplete_value": false,
      "site": "00543c98",
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
      "00543fb4",
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
      "00543fb4",
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

- 旧版 [`00543c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md#insn-00543c98) · [`00543c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md#insn-00543c90) · [`00543c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c88.md#insn-00543c94)
- 新版 [`00543fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fa8.md#insn-00543fb8) · [`00543fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fa8.md#insn-00543fb0) · [`00543fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fa8.md#insn-00543fb4)

~~~diff
- 00543c98 ["INT_ADD", "register:40f0:8", ["const:543c98:8", "const:4:8"]]
- 00543c98 ["CALL", null, ["callee:0043bad8:8"]]
+ 00543fb8 ["INT_ADD", "register:40f0:8", ["const:543fb8:8", "const:4:8"]]
+ 00543fb8 ["CALL", null, ["callee:0043bad8:8"]]
- 00543c98 bytes c8defb97
+ 00543fb8 bytes c8defb97
- 00543c90 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00543fb0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00543c90 bytes a0ebff90
+ 00543fb0 bytes a0ebffb0
- 00543c94 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00543c94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00543c94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00543c94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00543fb4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00543fb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00543fb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00543fb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00543c94 bytes 00303e91
+ 00543fb4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dae937d5a13780513179e6eaf8f16a0"></a>

### [`00543dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543dc8.md) → [`005440e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440e8.md) FUN_005440e8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00543ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543ddc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00543fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543fbc.md) [`005440fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440fc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005440f4",
      "incomplete_value": false,
      "site": "005440f8",
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
      "definition_site": "00543dd4",
      "incomplete_value": false,
      "site": "00543dd8",
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
      "005440f4",
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
      "005440f4",
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

- 旧版 [`00543dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543dc8.md#insn-00543dd8) · [`00543dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543dc8.md#insn-00543dd0) · [`00543dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543dc8.md#insn-00543dd4)
- 新版 [`005440f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440e8.md#insn-005440f8) · [`005440f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440e8.md#insn-005440f0) · [`005440f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/005440e8.md#insn-005440f4)

~~~diff
- 00543dd8 ["INT_ADD", "register:40f0:8", ["const:543dd8:8", "const:4:8"]]
- 00543dd8 ["CALL", null, ["callee:0043bad8:8"]]
+ 005440f8 ["INT_ADD", "register:40f0:8", ["const:5440f8:8", "const:4:8"]]
+ 005440f8 ["CALL", null, ["callee:0043bad8:8"]]
- 00543dd8 bytes 78defb97
+ 005440f8 bytes 78defb97
- 00543dd0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005440f0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00543dd0 bytes a0ebff90
+ 005440f0 bytes a0ebff90
- 00543dd4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00543dd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00543dd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00543dd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005440f4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005440f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005440f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005440f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00543dd4 bytes 00303e91
+ 005440f4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db22f704c2788077afbb375ea265da1"></a>

### [`005449f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md) → [`00544d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544d10.md) FUN_00544d10

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004cafe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ca/004cafe0.md) [`00544bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544bdc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`004cb300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cb300.md) [`00544efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544efc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00544d1c",
      "incomplete_value": false,
      "site": "00544d20",
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
      "definition_site": "005449fc",
      "incomplete_value": false,
      "site": "00544a00",
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
      "00544d1c",
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
      "00544d1c",
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

- 旧版 [`00544a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md#insn-00544a00) · [`005449f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md#insn-005449f8) · [`005449fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/005449f0.md#insn-005449fc)
- 新版 [`00544d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544d10.md#insn-00544d20) · [`00544d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544d10.md#insn-00544d18) · [`00544d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00544/00544d10.md#insn-00544d1c)

~~~diff
- 00544a00 ["INT_ADD", "register:40f0:8", ["const:544a00:8", "const:4:8"]]
- 00544a00 ["CALL", null, ["callee:0043bad8:8"]]
+ 00544d20 ["INT_ADD", "register:40f0:8", ["const:544d20:8", "const:4:8"]]
+ 00544d20 ["CALL", null, ["callee:0043bad8:8"]]
- 00544a00 bytes 6edbfb97
+ 00544d20 bytes 6edbfb97
- 005449f8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00544d18 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005449f8 bytes 80ebfff0
+ 00544d18 bytes a0ebff90
- 005449fc ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005449fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005449fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005449fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00544d1c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00544d1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00544d1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00544d1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005449fc bytes 00303e91
+ 00544d1c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941626aaee8d99f0ebcb36d3d70b168b"></a>

### [`00544d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md) → [`0054503c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054503c.md) FUN_0054503c

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004cfe08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfe08.md) [`004d02cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d02cc.md) [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) · 呼出先 10件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 3件 [`004d0128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d0/004d0128.md) [`004d05ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004d0/004d05ec.md) [`004ed070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ed/004ed070.md) · 呼出先 10件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005450c4",
      "incomplete_value": true,
      "site": "005450cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00544da4",
      "incomplete_value": true,
      "site": "00544dac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "005450c8",
      "incomplete_value": true,
      "site": "005450cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00544da8",
      "incomplete_value": true,
      "site": "00544dac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00545114",
      "incomplete_value": true,
      "site": "00545114",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00544df4",
      "incomplete_value": true,
      "site": "00544df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
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
      "005450c4",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "005450c4",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005450c8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005450c4",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "005450c4",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005450c8",
      "READ",
      [
        "storage",
        "00c9be90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00544dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md#insn-00544dac) · [`00544df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md#insn-00544df4) · [`00544d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544d1c.md#insn-00544d7c)
- 新版 [`005450cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054503c.md#insn-005450cc) · [`00545114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054503c.md#insn-00545114) · [`0054509c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054503c.md#insn-0054509c)

~~~diff
- 00544dac ["INT_ADD", "register:40f0:8", ["const:544dac:8", "const:4:8"]]
- 00544dac ["CALL", null, ["callee:00c58fb0:8"]]
+ 005450cc ["INT_ADD", "register:40f0:8", ["const:5450cc:8", "const:4:8"]]
+ 005450cc ["CALL", null, ["callee:00c58fb0:8"]]
- 00544dac bytes 8d4c1c94
+ 005450cc bytes b94f1c94
- 00544df4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00544df4 ["INT_ADD", "register:40f0:8", ["const:544df4:8", "const:4:8"]]
- 00544df4 ["CALLIND", null, ["register:0:8"]]
+ 00545114 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00545114 ["INT_ADD", "register:40f0:8", ["const:545114:8", "const:4:8"]]
+ 00545114 ["CALLIND", null, ["register:0:8"]]
- 00544df4 bytes 00013fd6
+ 00545114 bytes 00013fd6
- 00544d7c ["INT_ADD", "register:40f0:8", ["const:544d7c:8", "const:4:8"]]
- 00544d7c ["CALL", null, ["callee:00c59ad0:8"]]
+ 0054509c ["INT_ADD", "register:40f0:8", ["const:54509c:8", "const:4:8"]]
+ 0054509c ["CALL", null, ["callee:00c59ad0:8"]]
- 00544d7c bytes 614f1c94
+ 0054509c bytes 8d521c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d914549bbd33d4404d32bca50229a35c"></a>

### [`00544e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e28.md) → [`00545148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545148.md) FUN_00545148

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00545190",
      "incomplete_value": true,
      "site": "00545190",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00544e70",
      "incomplete_value": true,
      "site": "00544e70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
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
      "00545180",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545180",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00544e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e28.md#insn-00544e70) · [`00544e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e28.md#insn-00544e5c) · [`00544e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e28.md#insn-00544e60)
- 新版 [`00545190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545148.md#insn-00545190) · [`0054517c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545148.md#insn-0054517c) · [`00545180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545148.md#insn-00545180)

~~~diff
- 00544e70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00544e70 ["INT_ADD", "register:40f0:8", ["const:544e70:8", "const:4:8"]]
- 00544e70 ["CALLIND", null, ["register:0:8"]]
+ 00545190 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00545190 ["INT_ADD", "register:40f0:8", ["const:545190:8", "const:4:8"]]
+ 00545190 ["CALLIND", null, ["register:0:8"]]
- 00544e70 bytes 20013fd6
+ 00545190 bytes 20013fd6
- 00544e5c ["COPY", "register:4048:8", ["const:c67000:8"]]
+ 0054517c ["COPY", "register:4048:8", ["const:c68000:8"]]
- 00544e5c bytes 093900f0
+ 0054517c bytes 093900f0
- 00544e60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
- 00544e60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00545180 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d8:8"]]
+ 00545180 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00544e60 bytes 290544f9
+ 00545180 bytes 29ed43f9
~~~


<a id="compare-925eac53947e0f1ec6bfd544574f35e2"></a>

### [`00544e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e88.md) → [`005451a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451a8.md) FUN_005451a8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004da5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004da/004da5f0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`004da910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004da/004da910.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005451b4",
      "incomplete_value": false,
      "site": "005451b8",
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
      "definition_site": "00544e94",
      "incomplete_value": false,
      "site": "00544e98",
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
      "005451b4",
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
      "005451b4",
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

- 旧版 [`00544e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e88.md#insn-00544e98) · [`00544e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e88.md#insn-00544e90) · [`00544e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e88.md#insn-00544e94)
- 新版 [`005451b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451a8.md#insn-005451b8) · [`005451b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451a8.md#insn-005451b0) · [`005451b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451a8.md#insn-005451b4)

~~~diff
- 00544e98 ["INT_ADD", "register:40f0:8", ["const:544e98:8", "const:4:8"]]
- 00544e98 ["CALL", null, ["callee:0043bad8:8"]]
+ 005451b8 ["INT_ADD", "register:40f0:8", ["const:5451b8:8", "const:4:8"]]
+ 005451b8 ["CALL", null, ["callee:0043bad8:8"]]
- 00544e98 bytes 48dafb97
+ 005451b8 bytes 48dafb97
- 00544e90 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005451b0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00544e90 bytes 80ebfff0
+ 005451b0 bytes 80ebfff0
- 00544e94 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00544e94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00544e94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00544e94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005451b4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005451b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005451b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005451b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00544e94 bytes 00303e91
+ 005451b4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1859afd4860d67d1c1f047fbe877918a"></a>

### [`0054505c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054505c.md) → [`0054537c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054537c.md) FUN_0054537c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005453d8",
      "incomplete_value": true,
      "site": "005453d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005450b8",
      "incomplete_value": true,
      "site": "005450b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
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
      "005453c8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005453c8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005450b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054505c.md#insn-005450b8) · [`0054507c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054505c.md#insn-0054507c) · [`005450a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054505c.md#insn-005450a8)
- 新版 [`005453d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054537c.md#insn-005453d8) · [`0054539c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054537c.md#insn-0054539c) · [`005453c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054537c.md#insn-005453c8)

~~~diff
- 005450b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005450b8 ["INT_ADD", "register:40f0:8", ["const:5450b8:8", "const:4:8"]]
- 005450b8 ["CALLIND", null, ["register:0:8"]]
+ 005453d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005453d8 ["INT_ADD", "register:40f0:8", ["const:5453d8:8", "const:4:8"]]
+ 005453d8 ["CALLIND", null, ["register:0:8"]]
- 005450b8 bytes 20013fd6
+ 005453d8 bytes 20013fd6
- 0054507c ["COPY", "register:40b0:8", ["const:c67000:8"]]
+ 0054539c ["COPY", "register:40b0:8", ["const:c68000:8"]]
- 0054507c bytes 163900d0
+ 0054539c bytes 163900f0
- 005450a8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:808:8"]]
- 005450a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005453c8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7d8:8"]]
+ 005453c8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005450a8 bytes c90644f9
+ 005453c8 bytes c9ee43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754a69108ff6c30c9b8783014d0fea8f"></a>

### [`005450fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005450fc.md) → [`0054541c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054541c.md) FUN_0054541c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00544e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00544/00544e9c.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`005451bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/005451bc.md) · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005454d4",
      "incomplete_value": true,
      "site": "005454d4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005451b4",
      "incomplete_value": true,
      "site": "005451b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
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
      "005454c4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005454c4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005451b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005450fc.md#insn-005451b4) · [`00545154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005450fc.md#insn-00545154) · [`00545180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005450fc.md#insn-00545180)
- 新版 [`005454d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054541c.md#insn-005454d4) · [`00545474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054541c.md#insn-00545474) · [`005454a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/0054541c.md#insn-005454a0)

~~~diff
- 005451b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005451b4 ["INT_ADD", "register:40f0:8", ["const:5451b4:8", "const:4:8"]]
- 005451b4 ["CALLIND", null, ["register:0:8"]]
+ 005454d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005454d4 ["INT_ADD", "register:40f0:8", ["const:5454d4:8", "const:4:8"]]
+ 005454d4 ["CALLIND", null, ["register:0:8"]]
- 005451b4 bytes 20013fd6
+ 005454d4 bytes 20013fd6
- 00545154 ["INT_ADD", "register:40f0:8", ["const:545154:8", "const:4:8"]]
- 00545154 ["CALL", null, ["callee:00c59be0:8"]]
+ 00545474 ["INT_ADD", "register:40f0:8", ["const:545474:8", "const:4:8"]]
+ 00545474 ["CALL", null, ["callee:00c59be0:8"]]
- 00545154 bytes af4e1c94
+ 00545474 bytes db511c94
- 00545180 ["COPY", "register:40b8:8", ["const:c67000:8"]]
+ 005454a0 ["COPY", "register:40b8:8", ["const:c68000:8"]]
- 00545180 bytes 173900d0
+ 005454a0 bytes 173900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d2e1326c08c28fe321227771eb6ca4c"></a>

### [`005457c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457c8.md) → [`00545ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ae8.md) FUN_00545ae8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00545af0",
      "incomplete_value": false,
      "site": "00545af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005457d0",
      "incomplete_value": false,
      "site": "005457d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00545af4",
      "DATA",
      [
        "storage",
        "00c6a5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545af4",
      "DATA",
      [
        "storage",
        "00c6b5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005457cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457c8.md#insn-005457cc) · [`005457d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457c8.md#insn-005457d0)
- 新版 [`00545aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ae8.md#insn-00545aec) · [`00545af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ae8.md#insn-00545af0)

~~~diff
- 005457cc ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00545aec ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005457cc bytes 293900b0
+ 00545aec bytes 293900d0
- 005457d0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005457d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005457d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005457d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545af0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00545af0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545af0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545af0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005457d0 bytes 29c11791
+ 00545af0 bytes 29011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f249ff23a71f61be4e8304a765dbd35"></a>

### [`005457e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457e8.md) → [`00545b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b08.md) FUN_00545b08

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00545b10",
      "incomplete_value": false,
      "site": "00545b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005457f0",
      "incomplete_value": false,
      "site": "005457f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00545b14",
      "DATA",
      [
        "storage",
        "00c6a5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545b14",
      "DATA",
      [
        "storage",
        "00c6b5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005457ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457e8.md#insn-005457ec) · [`005457f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457e8.md#insn-005457f0) · [`00545814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005457e8.md#insn-00545814)
- 新版 [`00545b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b08.md#insn-00545b0c) · [`00545b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b08.md#insn-00545b10) · [`00545b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b08.md#insn-00545b34)

~~~diff
- 005457ec ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00545b0c ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005457ec bytes 293900b0
+ 00545b0c bytes 293900d0
- 005457f0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005457f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005457f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005457f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545b10 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00545b10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545b10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545b10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005457f0 bytes 29c11791
+ 00545b10 bytes 29011791
- 00545814 ["INT_ADD", "register:40f0:8", ["const:545814:8", "const:4:8"]]
- 00545814 ["CALL", null, ["callee:00c58f50:8"]]
+ 00545b34 ["INT_ADD", "register:40f0:8", ["const:545b34:8", "const:4:8"]]
+ 00545b34 ["CALL", null, ["callee:00c58f50:8"]]
- 00545814 bytes db491c94
+ 00545b34 bytes 074d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bbd7f1ee4c9128790af3869cb84940a"></a>

### [`00545828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545828.md) → [`00545b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b48.md) FUN_00545b48

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00545b74",
      "incomplete_value": false,
      "site": "00545b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545854",
      "incomplete_value": false,
      "site": "00545854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00545b74",
      "DATA",
      [
        "storage",
        "00c6a5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545b74",
      "DATA",
      [
        "storage",
        "00c6b5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054583c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545828.md#insn-0054583c) · [`00545848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545828.md#insn-00545848) · [`0054584c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545828.md#insn-0054584c)
- 新版 [`00545b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b48.md#insn-00545b5c) · [`00545b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b48.md#insn-00545b68) · [`00545b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545b48.md#insn-00545b6c)

~~~diff
- 0054583c ["INT_ADD", "register:40f0:8", ["const:54583c:8", "const:4:8"]]
- 0054583c ["CALL", null, ["callee:00c58f30:8"]]
+ 00545b5c ["INT_ADD", "register:40f0:8", ["const:545b5c:8", "const:4:8"]]
+ 00545b5c ["CALL", null, ["callee:00c58f30:8"]]
- 0054583c bytes c9491c94
+ 00545b5c bytes f54c1c94
- 00545848 ["COPY", "register:4050:8", ["const:c6a000:8"]]
+ 00545b68 ["COPY", "register:4050:8", ["const:c6b000:8"]]
- 00545848 bytes 2a3900b0
+ 00545b68 bytes 2a3900d0
- 0054584c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 0054584c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0054584c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0054584c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00545b6c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00545b6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00545b6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00545b6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0054584c bytes 4ac11791
+ 00545b6c bytes 4a011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261b9b9df7064b6dee8ed0d3c620ffc0"></a>

### [`0054589c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054589c.md) → [`00545bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545bbc.md) FUN_00545bbc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00545bc4",
      "incomplete_value": false,
      "site": "00545bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005458a4",
      "incomplete_value": false,
      "site": "005458a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00545bc4",
      "DATA",
      [
        "storage",
        "00c6a5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545bc4",
      "DATA",
      [
        "storage",
        "00c6b5c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054589c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054589c.md#insn-0054589c) · [`005458a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054589c.md#insn-005458a0)
- 新版 [`00545bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545bbc.md#insn-00545bbc) · [`00545bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545bbc.md#insn-00545bc0)

~~~diff
- 0054589c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00545bbc ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0054589c bytes 283900b0
+ 00545bbc bytes 283900d0
- 005458a0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005458a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005458a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005458a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00545bc0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00545bc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00545bc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00545bc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005458a0 bytes 08c11791
+ 00545bc0 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d741926d92a348b83ba342705838fcf5"></a>

### [`0054597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054597c.md) → [`00545c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545c9c.md) FUN_00545c9c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00545cb0",
      "incomplete_value": false,
      "site": "00545cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545990",
      "incomplete_value": false,
      "site": "00545994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "00545cb4",
      "DATA",
      [
        "storage",
        "00c6a680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545cb4",
      "DATA",
      [
        "storage",
        "00c6b650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054597c.md#insn-00545988) · [`0054598c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054597c.md#insn-0054598c) · [`00545990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/0054597c.md#insn-00545990)
- 新版 [`00545ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545c9c.md#insn-00545ca8) · [`00545cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545c9c.md#insn-00545cac) · [`00545cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545c9c.md#insn-00545cb0)

~~~diff
- 00545988 ["INT_ADD", "register:40f0:8", ["const:545988:8", "const:4:8"]]
- 00545988 ["CALL", null, ["callee:00c58f30:8"]]
+ 00545ca8 ["INT_ADD", "register:40f0:8", ["const:545ca8:8", "const:4:8"]]
+ 00545ca8 ["CALL", null, ["callee:00c58f30:8"]]
- 00545988 bytes 76491c94
+ 00545ca8 bytes a24c1c94
- 0054598c ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00545cac ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0054598c bytes 283900b0
+ 00545cac bytes 283900d0
- 00545990 ["COPY", "tmp:0:8", ["const:680:8"]]
- 00545990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00545990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00545990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00545cb0 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00545cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00545cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00545cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00545990 bytes 08011a91
+ 00545cb0 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48c0dd8b967c192ca4db8152e87b4ad5"></a>

### [`005459a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459a0.md) → [`00545cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cc0.md) FUN_00545cc0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00545cc4",
      "incomplete_value": false,
      "site": "00545cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005459a4",
      "incomplete_value": false,
      "site": "005459a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "00545cc8",
      "DATA",
      [
        "storage",
        "00c6a680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545cc8",
      "DATA",
      [
        "storage",
        "00c6b650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005459a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459a0.md#insn-005459a0) · [`005459a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459a0.md#insn-005459a4)
- 新版 [`00545cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cc0.md#insn-00545cc0) · [`00545cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cc0.md#insn-00545cc4)

~~~diff
- 005459a0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00545cc0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 005459a0 bytes 283900b0
+ 00545cc0 bytes 283900d0
- 005459a4 ["COPY", "tmp:0:8", ["const:680:8"]]
- 005459a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005459a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005459a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00545cc4 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00545cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00545cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00545cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005459a4 bytes 08011a91
+ 00545cc4 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dcf8b9a632794ad004b2cd1499f9297"></a>

### [`005459b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md) → [`00545cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cd8.md) FUN_00545cd8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00536a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00536d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536d88.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00545d30",
      "incomplete_value": true,
      "site": "00545d38",
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545a10",
      "incomplete_value": true,
      "site": "00545a18",
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
                "const:ce0:8"
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
      "definition_site": "00545d6c",
      "incomplete_value": true,
      "site": "00545d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545a4c",
      "incomplete_value": true,
      "site": "00545a58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0:8"
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
      "definition_site": "00545d68",
      "incomplete_value": false,
      "site": "00545d78",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00545a48",
      "incomplete_value": false,
      "site": "00545a58",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "00545d18",
      "READ",
      [
        "storage",
        "002bfee6",
        null,
        "string"
      ]
    ],
    [
      "00545d18",
      "READ",
      [
        "storage",
        "002bfef6",
        null,
        "string"
      ]
    ],
    [
      "00545d1c",
      "READ",
      [
        "storage",
        "002bff06",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00545d18",
      "READ",
      [
        "storage",
        "002bff30",
        null,
        "string"
      ]
    ],
    [
      "00545d18",
      "READ",
      [
        "storage",
        "002bff40",
        null,
        "string"
      ]
    ],
    [
      "00545d1c",
      "READ",
      [
        "storage",
        "002bff50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md#insn-00545a58) · [`005459dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md#insn-005459dc) · [`005459e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md#insn-005459e8)
- 新版 [`00545d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cd8.md#insn-00545d78) · [`00545cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cd8.md#insn-00545cfc) · [`00545d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cd8.md#insn-00545d08)

~~~diff
- 00545a58 ["INT_ADD", "register:40f0:8", ["const:545a58:8", "const:4:8"]]
- 00545a58 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00545d78 ["INT_ADD", "register:40f0:8", ["const:545d78:8", "const:4:8"]]
+ 00545d78 ["CALL", null, ["callee:00c58fb0:8"]]
- 00545a58 bytes 62491c94
+ 00545d78 bytes 8e4c1c94
- 005459dc ["INT_ADD", "register:40f0:8", ["const:5459dc:8", "const:4:8"]]
- 005459dc ["CALL", null, ["callee:00c58f90:8"]]
+ 00545cfc ["INT_ADD", "register:40f0:8", ["const:545cfc:8", "const:4:8"]]
+ 00545cfc ["CALL", null, ["callee:00c58f90:8"]]
- 005459dc bytes 79491c94
+ 00545cfc bytes a54c1c94
- 005459e8 ["INT_ADD", "register:40f0:8", ["const:5459e8:8", "const:4:8"]]
- 005459e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00545d08 ["INT_ADD", "register:40f0:8", ["const:545d08:8", "const:4:8"]]
+ 00545d08 ["CALL", null, ["callee:00c58f30:8"]]
- 005459e8 bytes 5e491c94
+ 00545d08 bytes 8a4c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012ce8b5d92a92ce68cb93f980ab6e1a"></a>

### [`00545ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ad0.md) → [`00545df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545df0.md) FUN_00545df0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00545df8",
      "incomplete_value": false,
      "site": "00545dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545ad8",
      "incomplete_value": false,
      "site": "00545adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00545dfc",
      "DATA",
      [
        "storage",
        "00c6a700",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545dfc",
      "DATA",
      [
        "storage",
        "00c6b6d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ad0.md#insn-00545ad4) · [`00545ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ad0.md#insn-00545ad8)
- 新版 [`00545df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545df0.md#insn-00545df4) · [`00545df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545df0.md#insn-00545df8)

~~~diff
- 00545ad4 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00545df4 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00545ad4 bytes 293900b0
+ 00545df4 bytes 293900d0
- 00545ad8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00545ad8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00545ad8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00545ad8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545df8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00545df8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545df8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545df8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00545ad8 bytes 29011c91
+ 00545df8 bytes 29411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11987df36ec0b54fb21ae4abd538c423"></a>

### [`00545af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545af0.md) → [`00545e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e10.md) FUN_00545e10

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00545e18",
      "incomplete_value": false,
      "site": "00545e1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545af8",
      "incomplete_value": false,
      "site": "00545afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00545e1c",
      "DATA",
      [
        "storage",
        "00c6a700",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545e1c",
      "DATA",
      [
        "storage",
        "00c6b6d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545af0.md#insn-00545af4) · [`00545af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545af0.md#insn-00545af8) · [`00545b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545af0.md#insn-00545b1c)
- 新版 [`00545e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e10.md#insn-00545e14) · [`00545e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e10.md#insn-00545e18) · [`00545e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e10.md#insn-00545e3c)

~~~diff
- 00545af4 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00545e14 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00545af4 bytes 293900b0
+ 00545e14 bytes 293900d0
- 00545af8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00545af8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00545af8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00545af8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00545e18 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00545e18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00545e18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00545e18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00545af8 bytes 29011c91
+ 00545e18 bytes 29411b91
- 00545b1c ["INT_ADD", "register:40f0:8", ["const:545b1c:8", "const:4:8"]]
- 00545b1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00545e3c ["INT_ADD", "register:40f0:8", ["const:545e3c:8", "const:4:8"]]
+ 00545e3c ["CALL", null, ["callee:00c58f50:8"]]
- 00545b1c bytes 19491c94
+ 00545e3c bytes 454c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-accb8f66757415246bfff8295c9511ea"></a>

### [`00545b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545b30.md) → [`00545e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e50.md) FUN_00545e50

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`004ee574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ee/004ee574.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`004ee894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ee/004ee894.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00545e7c",
      "incomplete_value": false,
      "site": "00545e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545b5c",
      "incomplete_value": false,
      "site": "00545b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00545e7c",
      "DATA",
      [
        "storage",
        "00c6a700",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545e7c",
      "DATA",
      [
        "storage",
        "00c6b6d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545b30.md#insn-00545b44) · [`00545b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545b30.md#insn-00545b50) · [`00545b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545b30.md#insn-00545b54)
- 新版 [`00545e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e50.md#insn-00545e64) · [`00545e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e50.md#insn-00545e70) · [`00545e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545e50.md#insn-00545e74)

~~~diff
- 00545b44 ["INT_ADD", "register:40f0:8", ["const:545b44:8", "const:4:8"]]
- 00545b44 ["CALL", null, ["callee:00c58f30:8"]]
+ 00545e64 ["INT_ADD", "register:40f0:8", ["const:545e64:8", "const:4:8"]]
+ 00545e64 ["CALL", null, ["callee:00c58f30:8"]]
- 00545b44 bytes 07491c94
+ 00545e64 bytes 334c1c94
- 00545b50 ["COPY", "register:4050:8", ["const:c6a000:8"]]
+ 00545e70 ["COPY", "register:4050:8", ["const:c6b000:8"]]
- 00545b50 bytes 2a3900b0
+ 00545e70 bytes 2a3900d0
- 00545b54 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00545b54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00545b54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00545b54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00545e74 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00545e74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00545e74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00545e74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00545b54 bytes 4a011c91
+ 00545e74 bytes 4a411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75c37715704e568b7723bf338dcc3c8"></a>

### [`00545ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ba4.md) → [`00545ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ec4.md) FUN_00545ec4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00545ecc",
      "incomplete_value": false,
      "site": "00545ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00545bac",
      "incomplete_value": false,
      "site": "00545bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "00545ecc",
      "DATA",
      [
        "storage",
        "00c6a700",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545ecc",
      "DATA",
      [
        "storage",
        "00c6b6d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00545ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ba4.md#insn-00545ba4) · [`00545ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/00545ba4.md#insn-00545ba8)
- 新版 [`00545ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ec4.md#insn-00545ec4) · [`00545ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545ec4.md#insn-00545ec8)

~~~diff
- 00545ba4 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00545ec4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00545ba4 bytes 283900b0
+ 00545ec4 bytes 283900d0
- 00545ba8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00545ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00545ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00545ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00545ec8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00545ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00545ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00545ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00545ba8 bytes 08011c91
+ 00545ec8 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c98fd0d7eb6222fe8fd6e3f59c207bd2"></a>

### [`00547b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b5c.md) → [`00547e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e7c.md) FUN_00547e7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00547e9c",
      "incomplete_value": false,
      "site": "00547ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547b7c",
      "incomplete_value": false,
      "site": "00547b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00547ea0",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00547ea0",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b5c.md#insn-00547b70) · [`00547b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b5c.md#insn-00547b78) · [`00547b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b5c.md#insn-00547b7c)
- 新版 [`00547e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e7c.md#insn-00547e90) · [`00547e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e7c.md#insn-00547e98) · [`00547e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e7c.md#insn-00547e9c)

~~~diff
- 00547b70 ["INT_ADD", "register:40f0:8", ["const:547b70:8", "const:4:8"]]
- 00547b70 ["CALL", null, ["callee:00c58f30:8"]]
+ 00547e90 ["INT_ADD", "register:40f0:8", ["const:547e90:8", "const:4:8"]]
+ 00547e90 ["CALL", null, ["callee:00c58f30:8"]]
- 00547b70 bytes fc401c94
+ 00547e90 bytes 28441c94
- 00547b78 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 00547e98 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00547b78 bytes 083900f0
+ 00547e98 bytes 28390090
- 00547b7c ["COPY", "tmp:0:8", ["const:780:8"]]
- 00547b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00547b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00547b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00547e9c ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00547e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00547e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00547e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00547b7c bytes 08011e91
+ 00547e9c bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b893d2f43d5303a2b09ae47e231d89e"></a>

### [`00547b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b94.md) → [`00547eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547eb4.md) FUN_00547eb4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00547ebc",
      "incomplete_value": false,
      "site": "00547ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00547b9c",
      "incomplete_value": false,
      "site": "00547ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00547ec0",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00547ec0",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b94.md#insn-00547b98) · [`00547b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b94.md#insn-00547b9c)
- 新版 [`00547eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547eb4.md#insn-00547eb8) · [`00547ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547eb4.md#insn-00547ebc)

~~~diff
- 00547b98 ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 00547eb8 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00547b98 bytes 093900f0
+ 00547eb8 bytes 29390090
- 00547b9c ["COPY", "tmp:0:8", ["const:780:8"]]
- 00547b9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00547b9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00547b9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00547ebc ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00547ebc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00547ebc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00547ebc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00547b9c bytes 29011e91
+ 00547ebc bytes 29411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f26ec8e330e4b7f2d83199e205bed1e8"></a>

### [`00547e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547e04.md) → [`00548124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548124.md) FUN_00548124

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`004ff6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff6dc.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00548160",
      "incomplete_value": true,
      "site": "00548160",
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
      "definition_site": "00547e40",
      "incomplete_value": true,
      "site": "00547e40",
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
      "0054814c",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00548160",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00548168",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0054814c",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00548160",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00548168",
      "READ",
      [
        "storage",
        "00c9be58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547e04.md#insn-00547e20) · [`00547e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547e04.md#insn-00547e24) · [`00547e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547e04.md#insn-00547e2c)
- 新版 [`00548140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548124.md#insn-00548140) · [`00548144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548124.md#insn-00548144) · [`0054814c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548124.md#insn-0054814c)

~~~diff
- 00547e20 ["INT_ADD", "register:40f0:8", ["const:547e20:8", "const:4:8"]]
- 00547e20 ["CALL", null, ["callee:00c58f30:8"]]
+ 00548140 ["INT_ADD", "register:40f0:8", ["const:548140:8", "const:4:8"]]
+ 00548140 ["CALL", null, ["callee:00c58f30:8"]]
- 00547e20 bytes 50401c94
+ 00548140 bytes 7c431c94
- 00547e24 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00548144 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00547e24 bytes 893a00f0
+ 00548144 bytes 893a00f0
- 00547e2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 00547e2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0054814c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 0054814c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00547e2c bytes 290947f9
+ 0054814c bytes 29f146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0632fbf202bd5a4ebf48ef5428fee696"></a>

### [`00547f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547f6c.md) → [`0054828c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/0054828c.md) FUN_0054828c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`004ff6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff6dc.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005482c8",
      "incomplete_value": true,
      "site": "005482cc",
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
      "definition_site": "00547fa8",
      "incomplete_value": true,
      "site": "00547fac",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00548320",
      "incomplete_value": true,
      "site": "00548320",
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
      "definition_site": "00548000",
      "incomplete_value": true,
      "site": "00548000",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005482b8",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "005482cc",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00548310",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005482b8",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "005482cc",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00548310",
      "READ",
      [
        "storage",
        "00c9be58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00547f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547f6c.md#insn-00547f8c) · [`00547f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547f6c.md#insn-00547f98) · [`00547fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547f6c.md#insn-00547fc0)
- 新版 [`005482ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/0054828c.md#insn-005482ac) · [`005482b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/0054828c.md#insn-005482b8) · [`005482e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/0054828c.md#insn-005482e0)

~~~diff
- 00547f8c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005482ac ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00547f8c bytes 883a00f0
+ 005482ac bytes 883a00f0
- 00547f98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00547f98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005482b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 005482b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00547f98 bytes 080947f9
+ 005482b8 bytes 08f146f9
- 00547fc0 ["INT_ADD", "register:40f0:8", ["const:547fc0:8", "const:4:8"]]
- 00547fc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 005482e0 ["INT_ADD", "register:40f0:8", ["const:5482e0:8", "const:4:8"]]
+ 005482e0 ["CALL", null, ["callee:00c58f30:8"]]
- 00547fc0 bytes e83f1c94
+ 005482e0 bytes 14431c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

