# v16.0.2 → v16.0.3 · 最優先の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-97c8569937890754973863e258f6471b"></a>

### [`00531244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md) → [`00531564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531564.md) FUN_00531564

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531598",
      "incomplete_value": true,
      "site": "005315a4",
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
      "definition_site": "00531278",
      "incomplete_value": true,
      "site": "00531284",
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
      "00531588",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "005315a4",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531588",
      "READ",
      [
        "storage",
        "00c9c250",
        null,
        "pointer"
      ]
    ],
    [
      "005315a4",
      "DATA",
      [
        "storage",
        "00c68ac8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053125c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-0053125c) · [`00531260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-00531260) · [`00531268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531244.md#insn-00531268)
- 新版 [`0053157c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531564.md#insn-0053157c) · [`00531580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531564.md#insn-00531580) · [`00531588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531564.md#insn-00531588)

~~~diff
- 0053125c ["INT_ADD", "register:40f0:8", ["const:53125c:8", "const:4:8"]]
- 0053125c ["CALL", null, ["callee:00c58f30:8"]]
+ 0053157c ["INT_ADD", "register:40f0:8", ["const:53157c:8", "const:4:8"]]
+ 0053157c ["CALL", null, ["callee:00c58f30:8"]]
- 0053125c bytes 419b1c94
+ 0053157c bytes 6d9e1c94
- 00531260 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00531580 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531260 bytes 483b00d0
+ 00531580 bytes 483b00f0
- 00531268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
- 00531268 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531588 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:250:8"]]
+ 00531588 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531268 bytes 084141f9
+ 00531588 bytes 082941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee5d75dc854652c95b9933f2a037235"></a>

### [`00531354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md) → [`00531674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531674.md) FUN_00531674

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005316ac",
      "incomplete_value": true,
      "site": "005316ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:181:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053138c",
      "incomplete_value": true,
      "site": "0053138c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:b6:8"
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
      "0053169c",
      "READ",
      [
        "storage",
        "002a40b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053169c",
      "READ",
      [
        "storage",
        "002a4181",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-00531370) · [`00531398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-00531398) · [`005313a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531354.md#insn-005313a8)
- 新版 [`00531690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531674.md#insn-00531690) · [`005316b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531674.md#insn-005316b8) · [`005316c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531674.md#insn-005316c8)

~~~diff
- 00531370 ["COPY", "tmp:0:8", ["const:b6:8"]]
- 00531370 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531370 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531370 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531690 ["COPY", "tmp:0:8", ["const:181:8"]]
+ 00531690 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531690 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531690 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531370 bytes 29d90291
+ 00531690 bytes 29050691
- 00531398 ["INT_ADD", "register:40f0:8", ["const:531398:8", "const:4:8"]]
- 00531398 ["CALL", null, ["callee:00c59730:8"]]
+ 005316b8 ["INT_ADD", "register:40f0:8", ["const:5316b8:8", "const:4:8"]]
+ 005316b8 ["CALL", null, ["callee:00c59730:8"]]
- 00531398 bytes f29c1c94
+ 005316b8 bytes 1ea01c94
- 005313a8 ["INT_ADD", "register:40f0:8", ["const:5313a8:8", "const:4:8"]]
- 005313a8 ["CALL", null, ["callee:00c58f50:8"]]
+ 005316c8 ["INT_ADD", "register:40f0:8", ["const:5316c8:8", "const:4:8"]]
+ 005316c8 ["CALL", null, ["callee:00c58f50:8"]]
- 005313a8 bytes f69a1c94
+ 005316c8 bytes 229e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8501a9c7afabfb179ab5e53588b11033"></a>

### [`0053144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md) → [`0053176c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053176c.md) FUN_0053176c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005317a0",
      "incomplete_value": true,
      "site": "005317ac",
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
      "definition_site": "00531480",
      "incomplete_value": true,
      "site": "0053148c",
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
      "00531790",
      "READ",
      [
        "storage",
        "00c9b260",
        null,
        "pointer"
      ]
    ],
    [
      "005317ac",
      "DATA",
      [
        "storage",
        "00c68a90",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531790",
      "READ",
      [
        "storage",
        "00c9c230",
        null,
        "pointer"
      ]
    ],
    [
      "005317ac",
      "DATA",
      [
        "storage",
        "00c69a60",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-00531464) · [`00531468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-00531468) · [`00531470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053144c.md#insn-00531470)
- 新版 [`00531784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053176c.md#insn-00531784) · [`00531788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053176c.md#insn-00531788) · [`00531790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/0053176c.md#insn-00531790)

~~~diff
- 00531464 ["INT_ADD", "register:40f0:8", ["const:531464:8", "const:4:8"]]
- 00531464 ["CALL", null, ["callee:00c58f30:8"]]
+ 00531784 ["INT_ADD", "register:40f0:8", ["const:531784:8", "const:4:8"]]
+ 00531784 ["CALL", null, ["callee:00c58f30:8"]]
- 00531464 bytes bf9a1c94
+ 00531784 bytes eb9d1c94
- 00531468 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00531788 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531468 bytes 483b00d0
+ 00531788 bytes 483b00f0
- 00531470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
- 00531470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531790 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
+ 00531790 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531470 bytes 083141f9
+ 00531790 bytes 081941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d7114a3b400b8f3cfbefde1733b9013"></a>

### [`00531594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md) → [`005318b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005318b4.md) FUN_005318b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005318ec",
      "incomplete_value": true,
      "site": "005318ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:3aa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005315cc",
      "incomplete_value": true,
      "site": "005315cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:2cc:8"
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
      "005318dc",
      "READ",
      [
        "storage",
        "002bb2cc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005318dc",
      "READ",
      [
        "storage",
        "002bb3aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005315b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315b0) · [`005315d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315d8) · [`005315e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531594.md#insn-005315e8)
- 新版 [`005318d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005318b4.md#insn-005318d0) · [`005318f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005318b4.md#insn-005318f8) · [`00531908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005318b4.md#insn-00531908)

~~~diff
- 005315b0 ["COPY", "tmp:0:8", ["const:2cc:8"]]
- 005315b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005315b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005315b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["COPY", "tmp:0:8", ["const:3aa:8"]]
+ 005318d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005318d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005315b0 bytes 29310b91
+ 005318d0 bytes 29a90e91
- 005315d8 ["INT_ADD", "register:40f0:8", ["const:5315d8:8", "const:4:8"]]
- 005315d8 ["CALL", null, ["callee:00c59730:8"]]
+ 005318f8 ["INT_ADD", "register:40f0:8", ["const:5318f8:8", "const:4:8"]]
+ 005318f8 ["CALL", null, ["callee:00c59730:8"]]
- 005315d8 bytes 629c1c94
+ 005318f8 bytes 8e9f1c94
- 005315e8 ["INT_ADD", "register:40f0:8", ["const:5315e8:8", "const:4:8"]]
- 005315e8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531908 ["INT_ADD", "register:40f0:8", ["const:531908:8", "const:4:8"]]
+ 00531908 ["CALL", null, ["callee:00c58f50:8"]]
- 005315e8 bytes 669a1c94
+ 00531908 bytes 929d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f601692405c3b84aa1789ab105322c4b"></a>

### [`0053168c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md) → [`005319ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005319ac.md) FUN_005319ac

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005319d4",
      "incomplete_value": true,
      "site": "005319d4",
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
      "definition_site": "005316b4",
      "incomplete_value": true,
      "site": "005316b4",
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
      "005319cc",
      "READ",
      [
        "storage",
        "00c9b268",
        null,
        "pointer"
      ]
    ],
    [
      "005319d4",
      "DATA",
      [
        "storage",
        "00c68b20",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005319cc",
      "READ",
      [
        "storage",
        "00c9c238",
        null,
        "pointer"
      ]
    ],
    [
      "005319d4",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005316a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316a0) · [`005316a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316a4) · [`005316ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053168c.md#insn-005316ac)
- 新版 [`005319c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005319ac.md#insn-005319c0) · [`005319c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005319ac.md#insn-005319c4) · [`005319cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/005319ac.md#insn-005319cc)

~~~diff
- 005316a0 ["INT_ADD", "register:40f0:8", ["const:5316a0:8", "const:4:8"]]
- 005316a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 005319c0 ["INT_ADD", "register:40f0:8", ["const:5319c0:8", "const:4:8"]]
+ 005319c0 ["CALL", null, ["callee:00c58f30:8"]]
- 005316a0 bytes 309a1c94
+ 005319c0 bytes 5c9d1c94
- 005316a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005319c4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005316a4 bytes 483b00d0
+ 005319c4 bytes 483b00f0
- 005316ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
- 005316ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005319cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
+ 005319cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005316ac bytes 083541f9
+ 005319cc bytes 081d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5da19d9b5edef4065bb88f32db48ec7"></a>

### [`00531764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531764.md) → [`00531a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a84.md) FUN_00531a84

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531abc",
      "incomplete_value": true,
      "site": "00531abc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f4f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053179c",
      "incomplete_value": true,
      "site": "0053179c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f0f:8"
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
      "00531aac",
      "READ",
      [
        "storage",
        "002a1f0f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00531aac",
      "READ",
      [
        "storage",
        "002a1f4f",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531764.md#insn-00531780) · [`005317a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531764.md#insn-005317a8) · [`005317b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531764.md#insn-005317b8)
- 新版 [`00531aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a84.md#insn-00531aa0) · [`00531ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a84.md#insn-00531ac8) · [`00531ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531a84.md#insn-00531ad8)

~~~diff
- 00531780 ["COPY", "tmp:0:8", ["const:f0f:8"]]
- 00531780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531aa0 ["COPY", "tmp:0:8", ["const:f4f:8"]]
+ 00531aa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531aa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531aa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531780 bytes 293d3c91
+ 00531aa0 bytes 293d3d91
- 005317a8 ["INT_ADD", "register:40f0:8", ["const:5317a8:8", "const:4:8"]]
- 005317a8 ["CALL", null, ["callee:00c59730:8"]]
+ 00531ac8 ["INT_ADD", "register:40f0:8", ["const:531ac8:8", "const:4:8"]]
+ 00531ac8 ["CALL", null, ["callee:00c59730:8"]]
- 005317a8 bytes ee9b1c94
+ 00531ac8 bytes 1a9f1c94
- 005317b8 ["INT_ADD", "register:40f0:8", ["const:5317b8:8", "const:4:8"]]
- 005317b8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531ad8 ["INT_ADD", "register:40f0:8", ["const:531ad8:8", "const:4:8"]]
+ 00531ad8 ["CALL", null, ["callee:00c58f50:8"]]
- 005317b8 bytes f2991c94
+ 00531ad8 bytes 1e9d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce91b95d9cf74d02414ef85e7a1e115"></a>

### [`0053185c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md) → [`00531b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531b7c.md) FUN_00531b7c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531ba4",
      "incomplete_value": true,
      "site": "00531ba4",
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
      "definition_site": "00531884",
      "incomplete_value": true,
      "site": "00531884",
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
      "00531b9c",
      "READ",
      [
        "storage",
        "00c9b288",
        null,
        "pointer"
      ]
    ],
    [
      "00531ba4",
      "DATA",
      [
        "storage",
        "00c68b98",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531b9c",
      "READ",
      [
        "storage",
        "00c9c258",
        null,
        "pointer"
      ]
    ],
    [
      "00531ba4",
      "DATA",
      [
        "storage",
        "00c69b68",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-00531870) · [`00531874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-00531874) · [`0053187c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/0053185c.md#insn-0053187c)
- 新版 [`00531b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531b7c.md#insn-00531b90) · [`00531b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531b7c.md#insn-00531b94) · [`00531b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531b7c.md#insn-00531b9c)

~~~diff
- 00531870 ["INT_ADD", "register:40f0:8", ["const:531870:8", "const:4:8"]]
- 00531870 ["CALL", null, ["callee:00c58f30:8"]]
+ 00531b90 ["INT_ADD", "register:40f0:8", ["const:531b90:8", "const:4:8"]]
+ 00531b90 ["CALL", null, ["callee:00c58f30:8"]]
- 00531870 bytes bc991c94
+ 00531b90 bytes e89c1c94
- 00531874 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00531b94 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531874 bytes 483b00d0
+ 00531b94 bytes 483b00f0
- 0053187c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 0053187c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531b9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:258:8"]]
+ 00531b9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053187c bytes 084541f9
+ 00531b9c bytes 082d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0539f169af2bfd7875b1d7120d383a"></a>

### [`00531934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md) → [`00531c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c54.md) FUN_00531c54

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531c8c",
      "incomplete_value": true,
      "site": "00531c8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
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
    "old": {
      "definition_site": "0053196c",
      "incomplete_value": true,
      "site": "0053196c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3bb:8"
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
      "00531c7c",
      "READ",
      [
        "storage",
        "002ab3bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531c7c",
      "READ",
      [
        "storage",
        "002ab488",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531950) · [`00531978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531978) · [`00531988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531934.md#insn-00531988)
- 新版 [`00531c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c54.md#insn-00531c70) · [`00531c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c54.md#insn-00531c98) · [`00531ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531c54.md#insn-00531ca8)

~~~diff
- 00531950 ["COPY", "tmp:0:8", ["const:3bb:8"]]
- 00531950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531c70 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00531c70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531c70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531950 bytes 29ed0e91
+ 00531c70 bytes 29211291
- 00531978 ["INT_ADD", "register:40f0:8", ["const:531978:8", "const:4:8"]]
- 00531978 ["CALL", null, ["callee:00c59730:8"]]
+ 00531c98 ["INT_ADD", "register:40f0:8", ["const:531c98:8", "const:4:8"]]
+ 00531c98 ["CALL", null, ["callee:00c59730:8"]]
- 00531978 bytes 7a9b1c94
+ 00531c98 bytes a69e1c94
- 00531988 ["INT_ADD", "register:40f0:8", ["const:531988:8", "const:4:8"]]
- 00531988 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531ca8 ["INT_ADD", "register:40f0:8", ["const:531ca8:8", "const:4:8"]]
+ 00531ca8 ["CALL", null, ["callee:00c58f50:8"]]
- 00531988 bytes 7e991c94
+ 00531ca8 bytes aa9c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64181652e82ecc8b25108f7079bb632a"></a>

### [`00531a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md) → [`00531d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531d4c.md) FUN_00531d4c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f1d0.md) [`0053f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md) [`00540a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540a34.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00531d98",
      "incomplete_value": true,
      "site": "00531da4",
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
      "definition_site": "00531a78",
      "incomplete_value": true,
      "site": "00531a84",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00531d8c",
      "READ",
      [
        "storage",
        "00c9b250",
        null,
        "pointer"
      ]
    ],
    [
      "00531da4",
      "DATA",
      [
        "storage",
        "00c679c0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00531d8c",
      "READ",
      [
        "storage",
        "00c9c220",
        null,
        "pointer"
      ]
    ],
    [
      "00531da4",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531a5c) · [`00531a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531a60) · [`00531a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531a2c.md#insn-00531a6c)
- 新版 [`00531d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531d4c.md#insn-00531d7c) · [`00531d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531d4c.md#insn-00531d80) · [`00531d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531d4c.md#insn-00531d8c)

~~~diff
- 00531a5c ["INT_ADD", "register:40f0:8", ["const:531a5c:8", "const:4:8"]]
- 00531a5c ["CALL", null, ["callee:00c58f30:8"]]
+ 00531d7c ["INT_ADD", "register:40f0:8", ["const:531d7c:8", "const:4:8"]]
+ 00531d7c ["CALL", null, ["callee:00c58f30:8"]]
- 00531a5c bytes 41991c94
+ 00531d7c bytes 6d9c1c94
- 00531a60 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00531d80 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531a60 bytes 483b00d0
+ 00531d80 bytes 483b00f0
- 00531a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:250:8"]]
- 00531a6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00531d8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
+ 00531d8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531a6c bytes 082941f9
+ 00531d8c bytes 081141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-499d3800a9288fb7d04c18636a3cdbb1"></a>

### [`00531c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md) → [`00531f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531f64.md) FUN_00531f64

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00531f9c",
      "incomplete_value": true,
      "site": "00531f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531c7c",
      "incomplete_value": true,
      "site": "00531c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:f20:8"
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
      "00531f8c",
      "READ",
      [
        "storage",
        "0029ef20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00531f8c",
      "READ",
      [
        "storage",
        "0029ef60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c60) · [`00531c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c88) · [`00531c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531c44.md#insn-00531c98)
- 新版 [`00531f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531f64.md#insn-00531f80) · [`00531fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531f64.md#insn-00531fa8) · [`00531fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531f64.md#insn-00531fb8)

~~~diff
- 00531c60 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00531c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00531f80 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00531f80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00531f80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00531f80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531c60 bytes 29813c91
+ 00531f80 bytes 29813d91
- 00531c88 ["INT_ADD", "register:40f0:8", ["const:531c88:8", "const:4:8"]]
- 00531c88 ["CALL", null, ["callee:00c59730:8"]]
+ 00531fa8 ["INT_ADD", "register:40f0:8", ["const:531fa8:8", "const:4:8"]]
+ 00531fa8 ["CALL", null, ["callee:00c59730:8"]]
- 00531c88 bytes b69a1c94
+ 00531fa8 bytes e29d1c94
- 00531c98 ["INT_ADD", "register:40f0:8", ["const:531c98:8", "const:4:8"]]
- 00531c98 ["CALL", null, ["callee:00c58f50:8"]]
+ 00531fb8 ["INT_ADD", "register:40f0:8", ["const:531fb8:8", "const:4:8"]]
+ 00531fb8 ["CALL", null, ["callee:00c58f50:8"]]
- 00531c98 bytes ba981c94
+ 00531fb8 bytes e69b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc25216992441046aeaff81227a56765"></a>

### [`00531cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531cec.md) → [`0053200c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/0053200c.md) FUN_0053200c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532018",
      "incomplete_value": true,
      "site": "00532028",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:58b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531cf8",
      "incomplete_value": true,
      "site": "00531d08",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:433:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0053202c",
      "incomplete_value": true,
      "site": "0053202c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00531d0c",
      "incomplete_value": true,
      "site": "00531d0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00532018",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ],
    [
      "00532020",
      "READ",
      [
        "storage",
        "002a5441",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532018",
      "READ",
      [
        "storage",
        "002a558b",
        null,
        "string"
      ]
    ],
    [
      "00532020",
      "READ",
      [
        "storage",
        "002a5599",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531cec.md#insn-00531cf4)
- 新版 [`00532014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/0053200c.md#insn-00532014)

~~~diff
- 00531cf4 ["COPY", "tmp:0:8", ["const:433:8"]]
- 00531cf4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00531cf4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00531cf4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532014 ["COPY", "tmp:0:8", ["const:58b:8"]]
+ 00532014 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532014 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532014 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00531cf4 bytes 4acd1091
+ 00532014 bytes 4a2d1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5803de5eeb46ba14647c536a33fb7949"></a>

### [`00531d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md) → [`00532034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532034.md) FUN_00532034

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f950.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fc70.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053205c",
      "incomplete_value": true,
      "site": "0053205c",
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
      "definition_site": "00531d3c",
      "incomplete_value": true,
      "site": "00531d3c",
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
      "00532054",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "0053205c",
      "DATA",
      [
        "storage",
        "00c68c28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532054",
      "READ",
      [
        "storage",
        "00c9c260",
        null,
        "pointer"
      ]
    ],
    [
      "0053205c",
      "DATA",
      [
        "storage",
        "00c69bf8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d28) · [`00531d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d2c) · [`00531d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531d14.md#insn-00531d34)
- 新版 [`00532048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532034.md#insn-00532048) · [`0053204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532034.md#insn-0053204c) · [`00532054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532034.md#insn-00532054)

~~~diff
- 00531d28 ["INT_ADD", "register:40f0:8", ["const:531d28:8", "const:4:8"]]
- 00531d28 ["CALL", null, ["callee:00c58f30:8"]]
+ 00532048 ["INT_ADD", "register:40f0:8", ["const:532048:8", "const:4:8"]]
+ 00532048 ["CALL", null, ["callee:00c58f30:8"]]
- 00531d28 bytes 8e981c94
+ 00532048 bytes ba9b1c94
- 00531d2c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053204c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531d2c bytes 483b00d0
+ 0053204c bytes 483b00d0
- 00531d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 00531d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00532054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 00532054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531d34 bytes 084941f9
+ 00532054 bytes 083141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-987959dd79f014119790fd582024f2e7"></a>

### [`00531da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md) → [`005320c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005320c4.md) FUN_005320c4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005320fc",
      "incomplete_value": true,
      "site": "005320fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531ddc",
      "incomplete_value": true,
      "site": "00531ddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e5:8"
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
      "005320ec",
      "READ",
      [
        "storage",
        "002ad6e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005320ec",
      "READ",
      [
        "storage",
        "002ad7b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531dc0) · [`00531de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531de8) · [`00531df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531da4.md#insn-00531df8)
- 新版 [`005320e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005320c4.md#insn-005320e0) · [`00532108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005320c4.md#insn-00532108) · [`00532118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005320c4.md#insn-00532118)

~~~diff
- 00531dc0 ["COPY", "tmp:0:8", ["const:6e5:8"]]
- 00531dc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00531dc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00531dc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005320e0 ["COPY", "tmp:0:8", ["const:7b2:8"]]
+ 005320e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005320e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005320e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00531dc0 bytes 29951b91
+ 005320e0 bytes 29c91e91
- 00531de8 ["INT_ADD", "register:40f0:8", ["const:531de8:8", "const:4:8"]]
- 00531de8 ["CALL", null, ["callee:00c59730:8"]]
+ 00532108 ["INT_ADD", "register:40f0:8", ["const:532108:8", "const:4:8"]]
+ 00532108 ["CALL", null, ["callee:00c59730:8"]]
- 00531de8 bytes 5e9a1c94
+ 00532108 bytes 8a9d1c94
- 00531df8 ["INT_ADD", "register:40f0:8", ["const:531df8:8", "const:4:8"]]
- 00531df8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532118 ["INT_ADD", "register:40f0:8", ["const:532118:8", "const:4:8"]]
+ 00532118 ["CALL", null, ["callee:00c58f50:8"]]
- 00531df8 bytes 62981c94
+ 00532118 bytes 8e9b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89526f203079f07ed603f470f2043c87"></a>

### [`00531e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md) → [`005321bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005321bc.md) FUN_005321bc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f1d0.md) [`0053f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md) [`00540a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540a34.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00532208",
      "incomplete_value": true,
      "site": "00532214",
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
      "definition_site": "00531ee8",
      "incomplete_value": true,
      "site": "00531ef4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005321fc",
      "READ",
      [
        "storage",
        "00c9b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00532214",
      "DATA",
      [
        "storage",
        "00c68ca0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005321fc",
      "READ",
      [
        "storage",
        "00c9c270",
        null,
        "pointer"
      ]
    ],
    [
      "00532214",
      "DATA",
      [
        "storage",
        "00c69c70",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531ecc) · [`00531ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531ed0) · [`00531edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531e9c.md#insn-00531edc)
- 新版 [`005321ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005321bc.md#insn-005321ec) · [`005321f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005321bc.md#insn-005321f0) · [`005321fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005321bc.md#insn-005321fc)

~~~diff
- 00531ecc ["INT_ADD", "register:40f0:8", ["const:531ecc:8", "const:4:8"]]
- 00531ecc ["CALL", null, ["callee:00c58f30:8"]]
+ 005321ec ["INT_ADD", "register:40f0:8", ["const:5321ec:8", "const:4:8"]]
+ 005321ec ["CALL", null, ["callee:00c58f30:8"]]
- 00531ecc bytes 25981c94
+ 005321ec bytes 519b1c94
- 00531ed0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005321f0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00531ed0 bytes 483b00d0
+ 005321f0 bytes 483b00d0
- 00531edc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 00531edc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005321fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:270:8"]]
+ 005321fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00531edc bytes 085141f9
+ 005321fc bytes 083941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e3421367ab3e7a47c7d05a26612a69"></a>

### [`005320b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md) → [`005323d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005323d4.md) FUN_005323d4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005323fc",
      "incomplete_value": true,
      "site": "0053240c",
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
                "const:b12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005320dc",
      "incomplete_value": true,
      "site": "005320ec",
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
                "const:a3b:8"
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
      "005323fc",
      "READ",
      [
        "storage",
        "002b0a3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005323fc",
      "READ",
      [
        "storage",
        "002b0b12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005320d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-005320d0) · [`005320f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-005320f8) · [`00532108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005320b4.md#insn-00532108)
- 新版 [`005323f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005323d4.md#insn-005323f0) · [`00532418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005323d4.md#insn-00532418) · [`00532428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005323d4.md#insn-00532428)

~~~diff
- 005320d0 ["COPY", "tmp:0:8", ["const:a3b:8"]]
- 005320d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005320d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005320d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005323f0 ["COPY", "tmp:0:8", ["const:b12:8"]]
+ 005323f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005323f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005323f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005320d0 bytes 29ed2891
+ 005323f0 bytes 29492c91
- 005320f8 ["INT_ADD", "register:40f0:8", ["const:5320f8:8", "const:4:8"]]
- 005320f8 ["CALL", null, ["callee:00c59730:8"]]
+ 00532418 ["INT_ADD", "register:40f0:8", ["const:532418:8", "const:4:8"]]
+ 00532418 ["CALL", null, ["callee:00c59730:8"]]
- 005320f8 bytes 9a991c94
+ 00532418 bytes c69c1c94
- 00532108 ["INT_ADD", "register:40f0:8", ["const:532108:8", "const:4:8"]]
- 00532108 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532428 ["INT_ADD", "register:40f0:8", ["const:532428:8", "const:4:8"]]
+ 00532428 ["CALL", null, ["callee:00c58f50:8"]]
- 00532108 bytes 9e971c94
+ 00532428 bytes ca9a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69371b6d0ea2c1c0169438bc499eb0ef"></a>

### [`005321ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md) → [`005324cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005324cc.md) FUN_005324cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532504",
      "incomplete_value": true,
      "site": "00532504",
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
      "definition_site": "005321e4",
      "incomplete_value": true,
      "site": "005321e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005324f4",
      "READ",
      [
        "storage",
        "00c9b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "00532504",
      "DATA",
      [
        "storage",
        "00c68d18",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005324f4",
      "READ",
      [
        "storage",
        "00c9c278",
        null,
        "pointer"
      ]
    ],
    [
      "00532504",
      "DATA",
      [
        "storage",
        "00c69ce8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005321c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md#insn-005321c4) · [`005321c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md#insn-005321c8) · [`005321d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005321ac.md#insn-005321d4)
- 新版 [`005324e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005324cc.md#insn-005324e4) · [`005324e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005324cc.md#insn-005324e8) · [`005324f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005324cc.md#insn-005324f4)

~~~diff
- 005321c4 ["INT_ADD", "register:40f0:8", ["const:5321c4:8", "const:4:8"]]
- 005321c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005324e4 ["INT_ADD", "register:40f0:8", ["const:5324e4:8", "const:4:8"]]
+ 005324e4 ["CALL", null, ["callee:00c58f30:8"]]
- 005321c4 bytes 67971c94
+ 005324e4 bytes 939a1c94
- 005321c8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005324e8 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005321c8 bytes 493b00b0
+ 005324e8 bytes 493b00d0
- 005321d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2a8:8"]]
- 005321d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005324f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:278:8"]]
+ 005324f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005321d4 bytes 295541f9
+ 005324f4 bytes 293d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd01d755721081ff4f9a8de750ab17ae"></a>

### [`005323a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md) → [`005326c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005326c4.md) FUN_005326c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005326fc",
      "incomplete_value": true,
      "site": "005326fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
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
      "definition_site": "005323dc",
      "incomplete_value": true,
      "site": "005323dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:c4a:8"
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
      "005326ec",
      "READ",
      [
        "storage",
        "002bec4a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005326ec",
      "READ",
      [
        "storage",
        "002bed28",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005323c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323c0) · [`005323e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323e8) · [`005323f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/005323a4.md#insn-005323f8)
- 新版 [`005326e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005326c4.md#insn-005326e0) · [`00532708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005326c4.md#insn-00532708) · [`00532718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005326c4.md#insn-00532718)

~~~diff
- 005323c0 ["COPY", "tmp:0:8", ["const:c4a:8"]]
- 005323c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005323c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005323c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005326e0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 005326e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005326e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005326e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005323c0 bytes 29293191
+ 005326e0 bytes 29a13491
- 005323e8 ["INT_ADD", "register:40f0:8", ["const:5323e8:8", "const:4:8"]]
- 005323e8 ["CALL", null, ["callee:00c59730:8"]]
+ 00532708 ["INT_ADD", "register:40f0:8", ["const:532708:8", "const:4:8"]]
+ 00532708 ["CALL", null, ["callee:00c59730:8"]]
- 005323e8 bytes de981c94
+ 00532708 bytes 0a9c1c94
- 005323f8 ["INT_ADD", "register:40f0:8", ["const:5323f8:8", "const:4:8"]]
- 005323f8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00532718 ["INT_ADD", "register:40f0:8", ["const:532718:8", "const:4:8"]]
+ 00532718 ["CALL", null, ["callee:00c58f50:8"]]
- 005323f8 bytes e2961c94
+ 00532718 bytes 0e9a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78789128028a1dedf1af06521461c3cc"></a>

### [`0053244c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/0053244c.md) → [`0053276c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/0053276c.md) FUN_0053276c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532778",
      "incomplete_value": true,
      "site": "00532784",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:46d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532458",
      "incomplete_value": true,
      "site": "00532464",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3a0:8"
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
      "00532778",
      "READ",
      [
        "storage",
        "002ab3a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532778",
      "READ",
      [
        "storage",
        "002ab46d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/0053244c.md#insn-00532450)
- 新版 [`00532770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/0053276c.md#insn-00532770)

~~~diff
- 00532450 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00532450 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00532450 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00532450 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532770 ["COPY", "tmp:0:8", ["const:46d:8"]]
+ 00532770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00532450 bytes 4a810e91
+ 00532770 bytes 4ab51191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a71da4ed475e9e0ab64e46354308976"></a>

### [`00532520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532520.md) → [`00532840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532840.md) FUN_00532840

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0053284c",
      "incomplete_value": true,
      "site": "0053285c",
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
                "const:fc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053252c",
      "incomplete_value": true,
      "site": "0053253c",
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
                "const:ef9:8"
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
      "0053284c",
      "READ",
      [
        "storage",
        "002b8ef9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053284c",
      "READ",
      [
        "storage",
        "002b8fc8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532520.md#insn-00532524)
- 新版 [`00532844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532840.md#insn-00532844)

~~~diff
- 00532524 ["COPY", "tmp:0:8", ["const:ef9:8"]]
- 00532524 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00532524 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00532524 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00532844 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00532844 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00532844 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00532844 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00532524 bytes 4ae53b91
+ 00532844 bytes 4a213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97413b713cd73c426ede26a71147c0a5"></a>

### [`00532598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md) → [`005328b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005328b8.md) FUN_005328b8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005328f0",
      "incomplete_value": true,
      "site": "005328f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:885:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005325d0",
      "incomplete_value": true,
      "site": "005325d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:72d:8"
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
      "005328e0",
      "READ",
      [
        "storage",
        "002a772d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005328e0",
      "READ",
      [
        "storage",
        "002a7885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005325b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325b4) · [`005325dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325dc) · [`005325ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532598.md#insn-005325ec)
- 新版 [`005328d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005328b8.md#insn-005328d4) · [`005328fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005328b8.md#insn-005328fc) · [`0053290c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005328b8.md#insn-0053290c)

~~~diff
- 005325b4 ["COPY", "tmp:0:8", ["const:72d:8"]]
- 005325b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005325b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005325b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005328d4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 005328d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005328d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005328d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005325b4 bytes 29b51c91
+ 005328d4 bytes 29152291
- 005325dc ["INT_ADD", "register:40f0:8", ["const:5325dc:8", "const:4:8"]]
- 005325dc ["CALL", null, ["callee:00c59730:8"]]
+ 005328fc ["INT_ADD", "register:40f0:8", ["const:5328fc:8", "const:4:8"]]
+ 005328fc ["CALL", null, ["callee:00c59730:8"]]
- 005325dc bytes 61981c94
+ 005328fc bytes 8d9b1c94
- 005325ec ["INT_ADD", "register:40f0:8", ["const:5325ec:8", "const:4:8"]]
- 005325ec ["CALL", null, ["callee:00c58f50:8"]]
+ 0053290c ["INT_ADD", "register:40f0:8", ["const:53290c:8", "const:4:8"]]
+ 0053290c ["CALL", null, ["callee:00c58f50:8"]]
- 005325ec bytes 65961c94
+ 0053290c bytes 91991c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb09bf0d77155dbf6ac82a832f7c92a3"></a>

### [`00532690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md) → [`005329b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005329b0.md) FUN_005329b0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fb18.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053fe38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053fe38.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "005329dc",
      "incomplete_value": true,
      "site": "005329e0",
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
      "definition_site": "005326bc",
      "incomplete_value": true,
      "site": "005326c0",
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
      "005329d0",
      "READ",
      [
        "storage",
        "00c9b298",
        null,
        "pointer"
      ]
    ],
    [
      "005329e0",
      "DATA",
      [
        "storage",
        "00c68e80",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "005329d0",
      "READ",
      [
        "storage",
        "00c9c268",
        null,
        "pointer"
      ]
    ],
    [
      "005329e0",
      "DATA",
      [
        "storage",
        "00c69e50",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005326a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326a4) · [`005326a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326a8) · [`005326b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532690.md#insn-005326b0)
- 新版 [`005329c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005329b0.md#insn-005329c4) · [`005329c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005329b0.md#insn-005329c8) · [`005329d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/005329b0.md#insn-005329d0)

~~~diff
- 005326a4 ["INT_ADD", "register:40f0:8", ["const:5326a4:8", "const:4:8"]]
- 005326a4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005329c4 ["INT_ADD", "register:40f0:8", ["const:5329c4:8", "const:4:8"]]
+ 005329c4 ["CALL", null, ["callee:00c58f30:8"]]
- 005326a4 bytes 2f961c94
+ 005329c4 bytes 5b991c94
- 005326a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005329c8 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005326a8 bytes 483b00b0
+ 005329c8 bytes 483b00d0
- 005326b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:298:8"]]
- 005326b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005329d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:268:8"]]
+ 005329d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005326b0 bytes 084d41f9
+ 005329d0 bytes 083541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cab2959fe4f6e2cece15c06cfcd7753"></a>

### [`00532908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md) → [`00532c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532c28.md) FUN_00532c28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532c60",
      "incomplete_value": true,
      "site": "00532c60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:567:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532940",
      "incomplete_value": true,
      "site": "00532940",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:489:8"
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
      "00532c50",
      "READ",
      [
        "storage",
        "002bc489",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00532c50",
      "READ",
      [
        "storage",
        "002bc567",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-00532924) · [`0053294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-0053294c) · [`0053295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532908.md#insn-0053295c)
- 新版 [`00532c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532c28.md#insn-00532c44) · [`00532c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532c28.md#insn-00532c6c) · [`00532c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532c28.md#insn-00532c7c)

~~~diff
- 00532924 ["COPY", "tmp:0:8", ["const:489:8"]]
- 00532924 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00532924 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00532924 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00532c44 ["COPY", "tmp:0:8", ["const:567:8"]]
+ 00532c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00532c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00532c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00532924 bytes 29251291
+ 00532c44 bytes 299d1591
- 0053294c ["INT_ADD", "register:40f0:8", ["const:53294c:8", "const:4:8"]]
- 0053294c ["CALL", null, ["callee:00c59730:8"]]
+ 00532c6c ["INT_ADD", "register:40f0:8", ["const:532c6c:8", "const:4:8"]]
+ 00532c6c ["CALL", null, ["callee:00c59730:8"]]
- 0053294c bytes 85971c94
+ 00532c6c bytes b19a1c94
- 0053295c ["INT_ADD", "register:40f0:8", ["const:53295c:8", "const:4:8"]]
- 0053295c ["CALL", null, ["callee:00c58f50:8"]]
+ 00532c7c ["INT_ADD", "register:40f0:8", ["const:532c7c:8", "const:4:8"]]
+ 00532c7c ["CALL", null, ["callee:00c58f50:8"]]
- 0053295c bytes 89951c94
+ 00532c7c bytes b5981c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a95e1b920301f22f299a363bb57079f1"></a>

### [`00532a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md) → [`00532d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d20.md) FUN_00532d20

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0053c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c980.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053cca0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00532d50",
      "incomplete_value": false,
      "site": "00532d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532a30",
      "incomplete_value": false,
      "site": "00532a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c68000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "definition_site": "00532d50",
      "incomplete_value": true,
      "site": "00532d50",
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
      "definition_site": "00532a30",
      "incomplete_value": true,
      "site": "00532a30",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00532d48",
      "READ",
      [
        "storage",
        "00c9b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "00532d50",
      "DATA",
      [
        "storage",
        "00c68f40",
        null,
        "undefined *"
      ]
    ],
    [
      "00532d50",
      "DATA",
      [
        "storage",
        "00c68ef8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00532d48",
      "READ",
      [
        "storage",
        "00c9c288",
        null,
        "pointer"
      ]
    ],
    [
      "00532d50",
      "DATA",
      [
        "storage",
        "00c69f10",
        null,
        "undefined *"
      ]
    ],
    [
      "00532d50",
      "DATA",
      [
        "storage",
        "00c69ec8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a14) · [`00532a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a18) · [`00532a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532a00.md#insn-00532a20)
- 新版 [`00532d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d20.md#insn-00532d34) · [`00532d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d20.md#insn-00532d38) · [`00532d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532d20.md#insn-00532d40)

~~~diff
- 00532a14 ["INT_ADD", "register:40f0:8", ["const:532a14:8", "const:4:8"]]
- 00532a14 ["CALL", null, ["callee:00c58f30:8"]]
+ 00532d34 ["INT_ADD", "register:40f0:8", ["const:532d34:8", "const:4:8"]]
+ 00532d34 ["CALL", null, ["callee:00c58f30:8"]]
- 00532a14 bytes 53951c94
+ 00532d34 bytes 7f981c94
- 00532a18 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00532d38 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00532a18 bytes 483b00b0
+ 00532d38 bytes 483b00d0
- 00532a20 ["COPY", "register:4048:8", ["const:c68000:8"]]
+ 00532d40 ["COPY", "register:4048:8", ["const:c69000:8"]]
- 00532a20 bytes a93900d0
+ 00532d40 bytes a93900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-387071b365cd26dd740089a043fe2cec"></a>

### [`00532b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md) → [`00532e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532e94.md) FUN_00532e94

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00532edc",
      "incomplete_value": true,
      "site": "00532edc",
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
      "definition_site": "00532bbc",
      "incomplete_value": true,
      "site": "00532bbc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00532edc",
      "incomplete_value": true,
      "site": "00532edc",
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
      "definition_site": "00532bbc",
      "incomplete_value": true,
      "site": "00532bbc",
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
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00532ec0",
      "READ",
      [
        "storage",
        "00c9b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00532ec4",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00532edc",
      "DATA",
      [
        "storage",
        "00c68fb8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00532ec0",
      "READ",
      [
        "storage",
        "00c9c280",
        null,
        "pointer"
      ]
    ],
    [
      "00532ec4",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00532edc",
      "DATA",
      [
        "storage",
        "00c69f88",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532b90) · [`00532b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532b94) · [`00532b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532b74.md#insn-00532b98)
- 新版 [`00532eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532e94.md#insn-00532eb0) · [`00532eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532e94.md#insn-00532eb4) · [`00532eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00532/00532e94.md#insn-00532eb8)

~~~diff
- 00532b90 ["INT_ADD", "register:40f0:8", ["const:532b90:8", "const:4:8"]]
- 00532b90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00532eb0 ["INT_ADD", "register:40f0:8", ["const:532eb0:8", "const:4:8"]]
+ 00532eb0 ["CALL", null, ["callee:00c58f30:8"]]
- 00532b90 bytes f4941c94
+ 00532eb0 bytes 20981c94
- 00532b94 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00532eb4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00532b94 bytes 483b00b0
+ 00532eb4 bytes 483b00d0
- 00532b98 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00532eb8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00532b98 bytes 493b0090
+ 00532eb8 bytes 493b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1174a6511eff9994d039f3019b92fa8e"></a>

### [`00532dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md) → [`005330e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005330e0.md) FUN_005330e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053fd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053fd58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00540078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540078.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59be0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053310c",
      "incomplete_value": false,
      "site": "0053310c",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532dec",
      "incomplete_value": false,
      "site": "00532dec",
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
            "const:e88:8"
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
      "0053310c",
      "DATA",
      [
        "storage",
        "00c66e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053310c",
      "DATA",
      [
        "storage",
        "00c67e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md#insn-00532dd8) · [`00532de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md#insn-00532de0) · [`00532de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532dc0.md#insn-00532de4)
- 新版 [`005330f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005330e0.md#insn-005330f8) · [`00533100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005330e0.md#insn-00533100) · [`00533104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005330e0.md#insn-00533104)

~~~diff
- 00532dd8 ["INT_ADD", "register:40f0:8", ["const:532dd8:8", "const:4:8"]]
- 00532dd8 ["CALL", null, ["callee:00c58f30:8"]]
+ 005330f8 ["INT_ADD", "register:40f0:8", ["const:5330f8:8", "const:4:8"]]
+ 005330f8 ["CALL", null, ["callee:00c58f30:8"]]
- 00532dd8 bytes 62941c94
+ 005330f8 bytes 8e971c94
- 00532de0 ["COPY", "register:4040:8", ["const:c66000:8"]]
+ 00533100 ["COPY", "register:4040:8", ["const:c67000:8"]]
- 00532de0 bytes a8390090
+ 00533100 bytes a8390090
- 00532de4 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00532de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00533104 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00533104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00533104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00533104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532de4 bytes 08213a91
+ 00533104 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293fa0de22052cd63f39faddea1eadc1"></a>

### [`00532ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md) → [`005331dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005331dc.md) FUN_005331dc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00532f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532f8c.md) · 呼出先 4件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`005332ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005332ac.md) · 呼出先 4件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533244",
      "incomplete_value": true,
      "site": "00533244",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00532f24",
      "incomplete_value": true,
      "site": "00532f24",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533280",
      "incomplete_value": true,
      "site": "00533280",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00532f60",
      "incomplete_value": true,
      "site": "00532f60",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533234",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533270",
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
      "00533234",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00533270",
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

- 旧版 [`00532f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532f24) · [`00532f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532f60) · [`00532ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ebc.md#insn-00532ed8)
- 新版 [`00533244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005331dc.md#insn-00533244) · [`00533280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005331dc.md#insn-00533280) · [`005331f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005331dc.md#insn-005331f8)

~~~diff
- 00532f24 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532f24 ["INT_ADD", "register:40f0:8", ["const:532f24:8", "const:4:8"]]
- 00532f24 ["CALLIND", null, ["register:0:8"]]
+ 00533244 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533244 ["INT_ADD", "register:40f0:8", ["const:533244:8", "const:4:8"]]
+ 00533244 ["CALLIND", null, ["register:0:8"]]
- 00532f24 bytes 20013fd6
+ 00533244 bytes 20013fd6
- 00532f60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00532f60 ["INT_ADD", "register:40f0:8", ["const:532f60:8", "const:4:8"]]
- 00532f60 ["CALLIND", null, ["register:0:8"]]
+ 00533280 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533280 ["INT_ADD", "register:40f0:8", ["const:533280:8", "const:4:8"]]
+ 00533280 ["CALLIND", null, ["register:0:8"]]
- 00532f60 bytes 20013fd6
+ 00533280 bytes 20013fd6
- 00532ed8 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 005331f8 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00532ed8 bytes b53900b0
+ 005331f8 bytes b53900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c62059005865a2654f3ddfdb07ddcb"></a>

### [`00532ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md) → [`00533318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533318.md) FUN_00533318

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/0053316c.md) · 呼出先 4件 [`004de728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004de/004de728.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0053348c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/0053348c.md) · 呼出先 4件 [`004dea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004de/004dea48.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533380",
      "incomplete_value": true,
      "site": "00533380",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533060",
      "incomplete_value": true,
      "site": "00533060",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005333c4",
      "incomplete_value": true,
      "site": "005333c4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005330a4",
      "incomplete_value": true,
      "site": "005330a4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005333f0",
      "incomplete_value": true,
      "site": "005333f0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005330d0",
      "incomplete_value": true,
      "site": "005330d0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533370",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005333b4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005333e0",
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
      "00533370",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005333b4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005333e0",
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

- 旧版 [`00533060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-00533060) · [`005330a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-005330a4) · [`005330d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00532/00532ff8.md#insn-005330d0)
- 新版 [`00533380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533318.md#insn-00533380) · [`005333c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533318.md#insn-005333c4) · [`005333f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533318.md#insn-005333f0)

~~~diff
- 00533060 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533060 ["INT_ADD", "register:40f0:8", ["const:533060:8", "const:4:8"]]
- 00533060 ["CALLIND", null, ["register:0:8"]]
+ 00533380 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533380 ["INT_ADD", "register:40f0:8", ["const:533380:8", "const:4:8"]]
+ 00533380 ["CALLIND", null, ["register:0:8"]]
- 00533060 bytes 20013fd6
+ 00533380 bytes 20013fd6
- 005330a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005330a4 ["INT_ADD", "register:40f0:8", ["const:5330a4:8", "const:4:8"]]
- 005330a4 ["CALLIND", null, ["register:0:8"]]
+ 005333c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005333c4 ["INT_ADD", "register:40f0:8", ["const:5333c4:8", "const:4:8"]]
+ 005333c4 ["CALLIND", null, ["register:0:8"]]
- 005330a4 bytes 20013fd6
+ 005333c4 bytes 20013fd6
- 005330d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005330d0 ["INT_ADD", "register:40f0:8", ["const:5330d0:8", "const:4:8"]]
- 005330d0 ["CALLIND", null, ["register:0:8"]]
+ 005333f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005333f0 ["INT_ADD", "register:40f0:8", ["const:5333f0:8", "const:4:8"]]
+ 005333f0 ["CALLIND", null, ["register:0:8"]]
- 005330d0 bytes 20013fd6
+ 005333f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8fbaffb2138772e1528fcb5b9e78a9b"></a>

### [`005334a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md) → [`005337c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005337c0.md) FUN_005337c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533864",
      "incomplete_value": true,
      "site": "00533864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533544",
      "incomplete_value": true,
      "site": "00533544",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da6:8"
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
      "definition_site": "00533800",
      "incomplete_value": false,
      "site": "00533808",
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
            "const:f25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005334e0",
      "incomplete_value": false,
      "site": "005334e8",
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
            "const:edb:8"
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
      "definition_site": "00533810",
      "incomplete_value": false,
      "site": "00533818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:3a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005334f0",
      "incomplete_value": false,
      "site": "005334f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:2d6:8"
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
      "00533800",
      "PARAM",
      [
        "storage",
        "002bfedb",
        null,
        "string"
      ]
    ],
    [
      "00533810",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ],
    [
      "00533854",
      "READ",
      [
        "storage",
        "002a8da6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00533800",
      "PARAM",
      [
        "storage",
        "002bff25",
        null,
        "string"
      ]
    ],
    [
      "00533810",
      "PARAM",
      [
        "storage",
        "002ab3a3",
        null,
        null
      ]
    ],
    [
      "00533854",
      "READ",
      [
        "storage",
        "002a8e73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005334e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334e8) · [`005334f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334f8) · [`005334e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005334a0.md#insn-005334e0)
- 新版 [`00533808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005337c0.md#insn-00533808) · [`00533818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005337c0.md#insn-00533818) · [`00533800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/005337c0.md#insn-00533800)

~~~diff
- 005334e8 ["INT_ADD", "register:40f0:8", ["const:5334e8:8", "const:4:8"]]
- 005334e8 ["CALL", null, ["callee:00c59150:8"]]
+ 00533808 ["INT_ADD", "register:40f0:8", ["const:533808:8", "const:4:8"]]
+ 00533808 ["CALL", null, ["callee:00c59150:8"]]
- 005334e8 bytes 26931c94
+ 00533808 bytes 52961c94
- 005334f8 ["INT_ADD", "register:40f0:8", ["const:5334f8:8", "const:4:8"]]
- 005334f8 ["CALL", null, ["callee:00c59010:8"]]
+ 00533818 ["INT_ADD", "register:40f0:8", ["const:533818:8", "const:4:8"]]
+ 00533818 ["CALL", null, ["callee:00c59010:8"]]
- 005334f8 bytes d2921c94
+ 00533818 bytes fe951c94
- 005334e0 ["COPY", "tmp:0:8", ["const:edb:8"]]
- 005334e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005334e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005334e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00533800 ["COPY", "tmp:0:8", ["const:f25:8"]]
+ 00533800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00533800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00533800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005334e0 bytes 006c3b91
+ 00533800 bytes 00943c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af9071c3d48229283821778c38649b5"></a>

### [`005337ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md) → [`00533acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533acc.md) FUN_00533acc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00533878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533878.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00533b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533b98.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533b34",
      "incomplete_value": true,
      "site": "00533b38",
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
      "definition_site": "00533814",
      "incomplete_value": true,
      "site": "00533818",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533b1c",
      "incomplete_value": true,
      "site": "00533b1c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005337fc",
      "incomplete_value": true,
      "site": "005337fc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533b68",
      "incomplete_value": true,
      "site": "00533b68",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533848",
      "incomplete_value": true,
      "site": "00533848",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533b0c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533b2c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533b38",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00533b0c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00533b2c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "00533b38",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005337fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-005337fc) · [`00533848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-00533848) · [`005337d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005337ac.md#insn-005337d4)
- 新版 [`00533b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533acc.md#insn-00533b1c) · [`00533b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533acc.md#insn-00533b68) · [`00533af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533acc.md#insn-00533af4)

~~~diff
- 005337fc ["COPY", "register:0:8", ["register:4048:8"]]
- 005337fc ["INT_ADD", "register:40f0:8", ["const:5337fc:8", "const:4:8"]]
- 005337fc ["CALLIND", null, ["register:0:8"]]
+ 00533b1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533b1c ["INT_ADD", "register:40f0:8", ["const:533b1c:8", "const:4:8"]]
+ 00533b1c ["CALLIND", null, ["register:0:8"]]
- 005337fc bytes 20013fd6
+ 00533b1c bytes 20013fd6
- 00533848 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533848 ["INT_ADD", "register:40f0:8", ["const:533848:8", "const:4:8"]]
- 00533848 ["CALLIND", null, ["register:0:8"]]
+ 00533b68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533b68 ["INT_ADD", "register:40f0:8", ["const:533b68:8", "const:4:8"]]
+ 00533b68 ["CALLIND", null, ["register:0:8"]]
- 00533848 bytes 20013fd6
+ 00533b68 bytes 20013fd6
- 005337d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005337d4 ["INT_ADD", "register:40f0:8", ["const:5337d4:8", "const:4:8"]]
- 005337d4 ["CALLIND", null, ["register:0:8"]]
+ 00533af4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00533af4 ["INT_ADD", "register:40f0:8", ["const:533af4:8", "const:4:8"]]
+ 00533af4 ["CALLIND", null, ["register:0:8"]]
- 005337d4 bytes 00013fd6
+ 00533af4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-990b37fd2ba121a08c301c0dc06465d3"></a>

### [`005338f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md) → [`00533c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c10.md) FUN_00533c10

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533c2c",
      "incomplete_value": true,
      "site": "00533c30",
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
      "definition_site": "0053390c",
      "incomplete_value": true,
      "site": "00533910",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533c64",
      "incomplete_value": true,
      "site": "00533c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00533944",
      "incomplete_value": true,
      "site": "00533944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00533c24",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533c30",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533c54",
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
      "00533c24",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "00533c30",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533c54",
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

- 旧版 [`00533944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-00533944) · [`005338fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-005338fc) · [`00533904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005338f0.md#insn-00533904)
- 新版 [`00533c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c10.md#insn-00533c64) · [`00533c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c10.md#insn-00533c1c) · [`00533c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c10.md#insn-00533c24)

~~~diff
- 00533944 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533944 ["INT_ADD", "register:40f0:8", ["const:533944:8", "const:4:8"]]
- 00533944 ["CALLIND", null, ["register:0:8"]]
+ 00533c64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533c64 ["INT_ADD", "register:40f0:8", ["const:533c64:8", "const:4:8"]]
+ 00533c64 ["CALLIND", null, ["register:0:8"]]
- 00533944 bytes 20013fd6
+ 00533c64 bytes 20013fd6
- 005338fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00533c1c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005338fc bytes 283b00f0
+ 00533c1c bytes 483b0090
- 00533904 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00533904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533c24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 00533c24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00533904 bytes 08a147f9
+ 00533c24 bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313428dd868b123a294174be2e9f0e13"></a>

### [`00533970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md) → [`00533c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c90.md) FUN_00533c90

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533cac",
      "incomplete_value": true,
      "site": "00533cb0",
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
      "definition_site": "0053398c",
      "incomplete_value": true,
      "site": "00533990",
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
    "kind": "call_target",
    "new": {
      "definition_site": "00533ce4",
      "incomplete_value": true,
      "site": "00533ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005339c4",
      "incomplete_value": true,
      "site": "005339c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00533ca4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00533cb0",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533cd4",
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
      "00533ca4",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "00533cb0",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00533cd4",
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

- 旧版 [`005339c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-005339c4) · [`0053397c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-0053397c) · [`00533984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533970.md#insn-00533984)
- 新版 [`00533ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c90.md#insn-00533ce4) · [`00533c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c90.md#insn-00533c9c) · [`00533ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533c90.md#insn-00533ca4)

~~~diff
- 005339c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005339c4 ["INT_ADD", "register:40f0:8", ["const:5339c4:8", "const:4:8"]]
- 005339c4 ["CALLIND", null, ["register:0:8"]]
+ 00533ce4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533ce4 ["INT_ADD", "register:40f0:8", ["const:533ce4:8", "const:4:8"]]
+ 00533ce4 ["CALLIND", null, ["register:0:8"]]
- 005339c4 bytes 20013fd6
+ 00533ce4 bytes 20013fd6
- 0053397c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00533c9c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053397c bytes 283b00f0
+ 00533c9c bytes 483b0090
- 00533984 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00533984 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00533ca4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 00533ca4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00533984 bytes 08a147f9
+ 00533ca4 bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d112280cd4d14dc424247ac00411d299"></a>

### [`005339e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md) → [`00533d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533d04.md) FUN_00533d04

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00533b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b00.md) [`00533b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b24.md) [`00533b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b2c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 3件 [`00533e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533e20.md) [`00533e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533e44.md) [`00533e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533e4c.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533d7c",
      "incomplete_value": true,
      "site": "00533d80",
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
      "definition_site": "00533a5c",
      "incomplete_value": true,
      "site": "00533a60",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00533db8",
      "incomplete_value": true,
      "site": "00533dbc",
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
      "definition_site": "00533a98",
      "incomplete_value": true,
      "site": "00533a9c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533d3c",
      "incomplete_value": true,
      "site": "00533d3c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533a1c",
      "incomplete_value": true,
      "site": "00533a1c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533d2c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533d74",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ],
    [
      "00533d80",
      "DATA",
      [
        "storage",
        "00c66978",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00533d2c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00533d74",
      "READ",
      [
        "storage",
        "00c9bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00533d80",
      "DATA",
      [
        "storage",
        "00c67948",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533a1c) · [`00533a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533a80) · [`00533acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/005339e4.md#insn-00533acc)
- 新版 [`00533d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533d04.md#insn-00533d3c) · [`00533da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533d04.md#insn-00533da0) · [`00533dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533d04.md#insn-00533dec)

~~~diff
- 00533a1c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a1c ["INT_ADD", "register:40f0:8", ["const:533a1c:8", "const:4:8"]]
- 00533a1c ["CALLIND", null, ["register:0:8"]]
+ 00533d3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533d3c ["INT_ADD", "register:40f0:8", ["const:533d3c:8", "const:4:8"]]
+ 00533d3c ["CALLIND", null, ["register:0:8"]]
- 00533a1c bytes 20013fd6
+ 00533d3c bytes 20013fd6
- 00533a80 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533a80 ["INT_ADD", "register:40f0:8", ["const:533a80:8", "const:4:8"]]
- 00533a80 ["CALLIND", null, ["register:0:8"]]
+ 00533da0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533da0 ["INT_ADD", "register:40f0:8", ["const:533da0:8", "const:4:8"]]
+ 00533da0 ["CALLIND", null, ["register:0:8"]]
- 00533a80 bytes 20013fd6
+ 00533da0 bytes 20013fd6
- 00533acc ["COPY", "register:0:8", ["register:4048:8"]]
- 00533acc ["INT_ADD", "register:40f0:8", ["const:533acc:8", "const:4:8"]]
- 00533acc ["CALLIND", null, ["register:0:8"]]
+ 00533dec ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533dec ["INT_ADD", "register:40f0:8", ["const:533dec:8", "const:4:8"]]
+ 00533dec ["CALLIND", null, ["register:0:8"]]
- 00533acc bytes 20013fd6
+ 00533dec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1dc8813df5bcdf04e4d4d099193c71"></a>

### [`00533b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md) → [`00533ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ea8.md) FUN_00533ea8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533ee0",
      "incomplete_value": true,
      "site": "00533ee0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533bc0",
      "incomplete_value": true,
      "site": "00533bc0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533f0c",
      "incomplete_value": true,
      "site": "00533f0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533bec",
      "incomplete_value": true,
      "site": "00533bec",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533ed0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533efc",
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
      "00533ed0",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00533efc",
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

- 旧版 [`00533bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533bc0) · [`00533bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533bec) · [`00533ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533b88.md#insn-00533ba0)
- 新版 [`00533ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ea8.md#insn-00533ee0) · [`00533f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ea8.md#insn-00533f0c) · [`00533ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ea8.md#insn-00533ec0)

~~~diff
- 00533bc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533bc0 ["INT_ADD", "register:40f0:8", ["const:533bc0:8", "const:4:8"]]
- 00533bc0 ["CALLIND", null, ["register:0:8"]]
+ 00533ee0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533ee0 ["INT_ADD", "register:40f0:8", ["const:533ee0:8", "const:4:8"]]
+ 00533ee0 ["CALLIND", null, ["register:0:8"]]
- 00533bc0 bytes 20013fd6
+ 00533ee0 bytes 20013fd6
- 00533bec ["COPY", "register:0:8", ["register:4048:8"]]
- 00533bec ["INT_ADD", "register:40f0:8", ["const:533bec:8", "const:4:8"]]
- 00533bec ["CALLIND", null, ["register:0:8"]]
+ 00533f0c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533f0c ["INT_ADD", "register:40f0:8", ["const:533f0c:8", "const:4:8"]]
+ 00533f0c ["CALLIND", null, ["register:0:8"]]
- 00533bec bytes 20013fd6
+ 00533f0c bytes 20013fd6
- 00533ba0 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00533ec0 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00533ba0 bytes b5390090
+ 00533ec0 bytes b53900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead6182b0d42da9e08f6f9c2b21ea229"></a>

### [`00533c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md) → [`00533f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533f54.md) FUN_00533f54

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00533f8c",
      "incomplete_value": true,
      "site": "00533f8c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533c6c",
      "incomplete_value": true,
      "site": "00533c6c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533fb8",
      "incomplete_value": true,
      "site": "00533fb8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533c98",
      "incomplete_value": true,
      "site": "00533c98",
      "value": [
        "LOAD",
        "8",
        [
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
      "00533f7c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00533fa8",
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
      "00533f7c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00533fa8",
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

- 旧版 [`00533c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c6c) · [`00533c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c98) · [`00533c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533c34.md#insn-00533c4c)
- 新版 [`00533f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533f54.md#insn-00533f8c) · [`00533fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533f54.md#insn-00533fb8) · [`00533f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533f54.md#insn-00533f6c)

~~~diff
- 00533c6c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533c6c ["INT_ADD", "register:40f0:8", ["const:533c6c:8", "const:4:8"]]
- 00533c6c ["CALLIND", null, ["register:0:8"]]
+ 00533f8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533f8c ["INT_ADD", "register:40f0:8", ["const:533f8c:8", "const:4:8"]]
+ 00533f8c ["CALLIND", null, ["register:0:8"]]
- 00533c6c bytes 20013fd6
+ 00533f8c bytes 20013fd6
- 00533c98 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533c98 ["INT_ADD", "register:40f0:8", ["const:533c98:8", "const:4:8"]]
- 00533c98 ["CALLIND", null, ["register:0:8"]]
+ 00533fb8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00533fb8 ["INT_ADD", "register:40f0:8", ["const:533fb8:8", "const:4:8"]]
+ 00533fb8 ["CALLIND", null, ["register:0:8"]]
- 00533c98 bytes 20013fd6
+ 00533fb8 bytes 20013fd6
- 00533c4c ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00533f6c ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00533c4c bytes b5390090
+ 00533f6c bytes b53900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de7f6f2d0c33c2ca3ab1a358c0763510"></a>

### [`00533cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md) → [`00533ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ff8.md) FUN_00533ff8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "definition_site": "005340a0",
      "incomplete_value": true,
      "site": "005340ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00533d80",
      "incomplete_value": true,
      "site": "00533d8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "0053409c",
      "incomplete_value": false,
      "site": "005340ac",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00533d7c",
      "incomplete_value": false,
      "site": "00533d8c",
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
      "0053409c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "005340a0",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "005340a0",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0053409c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "005340a0",
      "READ",
      [
        "storage",
        "00c9bee0",
        null,
        "pointer"
      ]
    ],
    [
      "005340a0",
      "PARAM",
      [
        "storage",
        "00c67550",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00533d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d8c) · [`00533d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d30) · [`00533d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533cd8.md#insn-00533d48)
- 新版 [`005340ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ff8.md#insn-005340ac) · [`00534050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ff8.md#insn-00534050) · [`00534068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00533/00533ff8.md#insn-00534068)

~~~diff
- 00533d8c ["INT_ADD", "register:40f0:8", ["const:533d8c:8", "const:4:8"]]
- 00533d8c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005340ac ["INT_ADD", "register:40f0:8", ["const:5340ac:8", "const:4:8"]]
+ 005340ac ["CALL", null, ["callee:00c58fb0:8"]]
- 00533d8c bytes 95901c94
+ 005340ac bytes c1931c94
- 00533d30 ["INT_ADD", "register:40f0:8", ["const:533d30:8", "const:4:8"]]
- 00533d30 ["CALL", null, ["callee:00c58f90:8"]]
+ 00534050 ["INT_ADD", "register:40f0:8", ["const:534050:8", "const:4:8"]]
+ 00534050 ["CALL", null, ["callee:00c58f90:8"]]
- 00533d30 bytes a4901c94
+ 00534050 bytes d0931c94
- 00533d48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533d48 ["INT_ADD", "register:40f0:8", ["const:533d48:8", "const:4:8"]]
- 00533d48 ["CALLIND", null, ["register:0:8"]]
+ 00534068 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534068 ["INT_ADD", "register:40f0:8", ["const:534068:8", "const:4:8"]]
+ 00534068 ["CALLIND", null, ["register:0:8"]]
- 00533d48 bytes 20013fd6
+ 00534068 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-262409bf73ea022dab3652d6c57ec8d5"></a>

### [`00533e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md) → [`0053414c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053414c.md) FUN_0053414c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534184",
      "incomplete_value": true,
      "site": "00534184",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533e64",
      "incomplete_value": true,
      "site": "00533e64",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005341b0",
      "incomplete_value": true,
      "site": "005341b0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533e90",
      "incomplete_value": true,
      "site": "00533e90",
      "value": [
        "LOAD",
        "8",
        [
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
      "00534174",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005341a0",
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
      "00534174",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005341a0",
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

- 旧版 [`00533e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e64) · [`00533e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e90) · [`00533e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533e2c.md#insn-00533e44)
- 新版 [`00534184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053414c.md#insn-00534184) · [`005341b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053414c.md#insn-005341b0) · [`00534164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053414c.md#insn-00534164)

~~~diff
- 00533e64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e64 ["INT_ADD", "register:40f0:8", ["const:533e64:8", "const:4:8"]]
- 00533e64 ["CALLIND", null, ["register:0:8"]]
+ 00534184 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534184 ["INT_ADD", "register:40f0:8", ["const:534184:8", "const:4:8"]]
+ 00534184 ["CALLIND", null, ["register:0:8"]]
- 00533e64 bytes 20013fd6
+ 00534184 bytes 20013fd6
- 00533e90 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533e90 ["INT_ADD", "register:40f0:8", ["const:533e90:8", "const:4:8"]]
- 00533e90 ["CALLIND", null, ["register:0:8"]]
+ 005341b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005341b0 ["INT_ADD", "register:40f0:8", ["const:5341b0:8", "const:4:8"]]
+ 005341b0 ["CALLIND", null, ["register:0:8"]]
- 00533e90 bytes 20013fd6
+ 005341b0 bytes 20013fd6
- 00533e44 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00534164 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00533e44 bytes b5390090
+ 00534164 bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3580f581edb2975fc76ae69d97a5290"></a>

### [`00533ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md) → [`005341f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005341f8.md) FUN_005341f8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534230",
      "incomplete_value": true,
      "site": "00534230",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533f10",
      "incomplete_value": true,
      "site": "00533f10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053425c",
      "incomplete_value": true,
      "site": "0053425c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00533f3c",
      "incomplete_value": true,
      "site": "00533f3c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00534220",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053424c",
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
      "00534220",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0053424c",
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

- 旧版 [`00533f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533f10) · [`00533f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533f3c) · [`00533ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00533/00533ed8.md#insn-00533ef0)
- 新版 [`00534230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005341f8.md#insn-00534230) · [`0053425c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005341f8.md#insn-0053425c) · [`00534210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005341f8.md#insn-00534210)

~~~diff
- 00533f10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00533f10 ["INT_ADD", "register:40f0:8", ["const:533f10:8", "const:4:8"]]
- 00533f10 ["CALLIND", null, ["register:0:8"]]
+ 00534230 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534230 ["INT_ADD", "register:40f0:8", ["const:534230:8", "const:4:8"]]
+ 00534230 ["CALLIND", null, ["register:0:8"]]
- 00533f10 bytes 20013fd6
+ 00534230 bytes 20013fd6
- 00533f3c ["COPY", "register:0:8", ["register:4048:8"]]
- 00533f3c ["INT_ADD", "register:40f0:8", ["const:533f3c:8", "const:4:8"]]
- 00533f3c ["CALLIND", null, ["register:0:8"]]
+ 0053425c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053425c ["INT_ADD", "register:40f0:8", ["const:53425c:8", "const:4:8"]]
+ 0053425c ["CALLIND", null, ["register:0:8"]]
- 00533f3c bytes 20013fd6
+ 0053425c bytes 20013fd6
- 00533ef0 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00534210 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00533ef0 bytes b5390090
+ 00534210 bytes b5390090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed8f64b045b29f0547926cca7fba7f8"></a>

### [`0053407c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md) → [`0053439c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053439c.md) FUN_0053439c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005343b4",
      "incomplete_value": false,
      "site": "005343b8",
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
      "definition_site": "00534094",
      "incomplete_value": false,
      "site": "00534098",
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
      "005343b8",
      "DATA",
      [
        "storage",
        "00c66f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005343b8",
      "DATA",
      [
        "storage",
        "00c67f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md#insn-00534090) · [`00534094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md#insn-00534094) · [`005340a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053407c.md#insn-005340a4)
- 新版 [`005343b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053439c.md#insn-005343b0) · [`005343b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053439c.md#insn-005343b4) · [`005343c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053439c.md#insn-005343c4)

~~~diff
- 00534090 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 005343b0 ["COPY", "register:4048:8", ["const:c67000:8"]]
- 00534090 bytes 893900d0
+ 005343b0 bytes 893900f0
- 00534094 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00534094 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534094 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534094 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005343b4 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 005343b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005343b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005343b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534094 bytes 29e13c91
+ 005343b4 bytes 29213c91
- 005340a4 ["INT_ADD", "register:40f0:8", ["const:5340a4:8", "const:4:8"]]
- 005340a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 005343c4 ["INT_ADD", "register:40f0:8", ["const:5343c4:8", "const:4:8"]]
+ 005343c4 ["CALL", null, ["callee:00c58f50:8"]]
- 005340a4 bytes b78f1c94
+ 005343c4 bytes e3921c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33df9fbe0d23eb950d85d792ac18a8fc"></a>

### [`005340e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md) → [`00534400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534400.md) FUN_00534400

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58890.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59860.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00534448",
      "incomplete_value": true,
      "site": "00534448",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:531:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534128",
      "incomplete_value": true,
      "site": "00534128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:462:8"
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
      "definition_site": "00534474",
      "incomplete_value": true,
      "site": "00534480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00534154",
      "incomplete_value": true,
      "site": "00534160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00534470",
      "incomplete_value": false,
      "site": "00534480",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00534150",
      "incomplete_value": false,
      "site": "00534160",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "00534434",
      "READ",
      [
        "storage",
        "002b7462",
        null,
        "string"
      ]
    ],
    [
      "00534470",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00534474",
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
      "00534434",
      "READ",
      [
        "storage",
        "002b7531",
        null,
        "string"
      ]
    ],
    [
      "00534470",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00534474",
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

- 旧版 [`00534160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-00534160) · [`00534104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-00534104) · [`0053410c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005340e0.md#insn-0053410c)
- 新版 [`00534480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534400.md#insn-00534480) · [`00534424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534400.md#insn-00534424) · [`0053442c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534400.md#insn-0053442c)

~~~diff
- 00534160 ["INT_ADD", "register:40f0:8", ["const:534160:8", "const:4:8"]]
- 00534160 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00534480 ["INT_ADD", "register:40f0:8", ["const:534480:8", "const:4:8"]]
+ 00534480 ["CALL", null, ["callee:00c58fb0:8"]]
- 00534160 bytes a08f1c94
+ 00534480 bytes cc921c94
- 00534104 ["INT_ADD", "register:40f0:8", ["const:534104:8", "const:4:8"]]
- 00534104 ["CALL", null, ["callee:00c58f90:8"]]
+ 00534424 ["INT_ADD", "register:40f0:8", ["const:534424:8", "const:4:8"]]
+ 00534424 ["CALL", null, ["callee:00c58f90:8"]]
- 00534104 bytes af8f1c94
+ 00534424 bytes db921c94
- 0053410c ["COPY", "tmp:0:8", ["const:462:8"]]
- 0053410c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053410c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053410c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053442c ["COPY", "tmp:0:8", ["const:531:8"]]
+ 0053442c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053442c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053442c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053410c bytes 29891191
+ 0053442c bytes 29c51491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823f60d5915f40f58dc1c28f486917ff"></a>

### [`005341a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md) → [`005344c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005344c8.md) FUN_005344c8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005344e0",
      "incomplete_value": false,
      "site": "005344e4",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005341c0",
      "incomplete_value": false,
      "site": "005341c4",
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
            "const:f88:8"
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
      "005344e4",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005344e4",
      "DATA",
      [
        "storage",
        "00c67f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005341bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md#insn-005341bc) · [`005341c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md#insn-005341c0) · [`005341d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005341a8.md#insn-005341d0)
- 新版 [`005344dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005344c8.md#insn-005344dc) · [`005344e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005344c8.md#insn-005344e0) · [`005344f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005344c8.md#insn-005344f0)

~~~diff
- 005341bc ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 005344dc ["COPY", "register:4048:8", ["const:c67000:8"]]
- 005341bc bytes 893900d0
+ 005344dc bytes 893900f0
- 005341c0 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 005341c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005341c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005341c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005344e0 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 005344e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005344e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005344e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005341c0 bytes 29213e91
+ 005344e0 bytes 29613d91
- 005341d0 ["INT_ADD", "register:40f0:8", ["const:5341d0:8", "const:4:8"]]
- 005341d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005344f0 ["INT_ADD", "register:40f0:8", ["const:5344f0:8", "const:4:8"]]
+ 005344f0 ["CALL", null, ["callee:00c58f50:8"]]
- 005341d0 bytes 6c8f1c94
+ 005344f0 bytes 98921c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811747c20aac6640de59a5375ddcc1b0"></a>

### [`0053420c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md) → [`0053452c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053452c.md) FUN_0053452c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58890.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59860.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00534574",
      "incomplete_value": true,
      "site": "00534574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:531:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534254",
      "incomplete_value": true,
      "site": "00534254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:462:8"
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
      "definition_site": "005345a0",
      "incomplete_value": true,
      "site": "005345ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00534280",
      "incomplete_value": true,
      "site": "0053428c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053459c",
      "incomplete_value": false,
      "site": "005345ac",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0053427c",
      "incomplete_value": false,
      "site": "0053428c",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "00534560",
      "READ",
      [
        "storage",
        "002b7462",
        null,
        "string"
      ]
    ],
    [
      "0053459c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "005345a0",
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
      "00534560",
      "READ",
      [
        "storage",
        "002b7531",
        null,
        "string"
      ]
    ],
    [
      "0053459c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "005345a0",
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

- 旧版 [`0053428c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-0053428c) · [`00534230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-00534230) · [`00534238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053420c.md#insn-00534238)
- 新版 [`005345ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053452c.md#insn-005345ac) · [`00534550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053452c.md#insn-00534550) · [`00534558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053452c.md#insn-00534558)

~~~diff
- 0053428c ["INT_ADD", "register:40f0:8", ["const:53428c:8", "const:4:8"]]
- 0053428c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005345ac ["INT_ADD", "register:40f0:8", ["const:5345ac:8", "const:4:8"]]
+ 005345ac ["CALL", null, ["callee:00c58fb0:8"]]
- 0053428c bytes 558f1c94
+ 005345ac bytes 81921c94
- 00534230 ["INT_ADD", "register:40f0:8", ["const:534230:8", "const:4:8"]]
- 00534230 ["CALL", null, ["callee:00c58f90:8"]]
+ 00534550 ["INT_ADD", "register:40f0:8", ["const:534550:8", "const:4:8"]]
+ 00534550 ["CALL", null, ["callee:00c58f90:8"]]
- 00534230 bytes 648f1c94
+ 00534550 bytes 90921c94
- 00534238 ["COPY", "tmp:0:8", ["const:462:8"]]
- 00534238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534558 ["COPY", "tmp:0:8", ["const:531:8"]]
+ 00534558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534238 bytes 29891191
+ 00534558 bytes 29c51491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc217e904a9317c630065c6cdf04f18"></a>

### [`005342d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md) → [`005345f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005345f4.md) FUN_005345f4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534624",
      "incomplete_value": true,
      "site": "00534638",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:e4b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534304",
      "incomplete_value": true,
      "site": "00534318",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:e01:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00534628",
      "incomplete_value": true,
      "site": "0053463c",
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
      "definition_site": "00534308",
      "incomplete_value": true,
      "site": "0053431c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534648",
      "incomplete_value": true,
      "site": "00534648",
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
      "definition_site": "00534328",
      "incomplete_value": true,
      "site": "00534328",
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
      "00534624",
      "READ",
      [
        "storage",
        "002b1e01",
        null,
        "string"
      ]
    ],
    [
      "00534628",
      "READ",
      [
        "storage",
        "002b1e0a",
        null,
        "string"
      ]
    ],
    [
      "00534630",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534624",
      "READ",
      [
        "storage",
        "002b1e4b",
        null,
        "string"
      ]
    ],
    [
      "00534628",
      "READ",
      [
        "storage",
        "002b1e54",
        null,
        "string"
      ]
    ],
    [
      "00534630",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md#insn-0053435c) · [`005342e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md#insn-005342e8) · [`005342f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005342d4.md#insn-005342f4)
- 新版 [`0053467c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005345f4.md#insn-0053467c) · [`00534608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005345f4.md#insn-00534608) · [`00534614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005345f4.md#insn-00534614)

~~~diff
- 0053435c ["INT_ADD", "register:40f0:8", ["const:53435c:8", "const:4:8"]]
- 0053435c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053467c ["INT_ADD", "register:40f0:8", ["const:53467c:8", "const:4:8"]]
+ 0053467c ["CALL", null, ["callee:00c58fb0:8"]]
- 0053435c bytes 218f1c94
+ 0053467c bytes 4d921c94
- 005342e8 ["INT_ADD", "register:40f0:8", ["const:5342e8:8", "const:4:8"]]
- 005342e8 ["CALL", null, ["callee:00c58f90:8"]]
+ 00534608 ["INT_ADD", "register:40f0:8", ["const:534608:8", "const:4:8"]]
+ 00534608 ["CALL", null, ["callee:00c58f90:8"]]
- 005342e8 bytes 368f1c94
+ 00534608 bytes 62921c94
- 005342f4 ["INT_ADD", "register:40f0:8", ["const:5342f4:8", "const:4:8"]]
- 005342f4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00534614 ["INT_ADD", "register:40f0:8", ["const:534614:8", "const:4:8"]]
+ 00534614 ["CALL", null, ["callee:00c58f30:8"]]
- 005342f4 bytes 1b8f1c94
+ 00534614 bytes 47921c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6240b0dbd3d826fce768a1079feeab39"></a>

### [`005343a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md) → [`005346c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005346c0.md) FUN_005346c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005346f0",
      "incomplete_value": true,
      "site": "00534704",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:8a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005343d0",
      "incomplete_value": true,
      "site": "005343e4",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:748:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005346f4",
      "incomplete_value": true,
      "site": "00534708",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005343d4",
      "incomplete_value": true,
      "site": "005343e8",
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
                "const:e:8"
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
      "definition_site": "00534714",
      "incomplete_value": true,
      "site": "00534714",
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
      "definition_site": "005343f4",
      "incomplete_value": true,
      "site": "005343f4",
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
      "005346f0",
      "READ",
      [
        "storage",
        "002a6748",
        null,
        "string"
      ]
    ],
    [
      "005346f4",
      "READ",
      [
        "storage",
        "002a6756",
        null,
        "string"
      ]
    ],
    [
      "005346fc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005346f0",
      "READ",
      [
        "storage",
        "002a68a0",
        null,
        "string"
      ]
    ],
    [
      "005346f4",
      "READ",
      [
        "storage",
        "002a68ae",
        null,
        "string"
      ]
    ],
    [
      "005346fc",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md#insn-00534428) · [`005343b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md#insn-005343b4) · [`005343c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005343a0.md#insn-005343c0)
- 新版 [`00534748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005346c0.md#insn-00534748) · [`005346d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005346c0.md#insn-005346d4) · [`005346e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005346c0.md#insn-005346e0)

~~~diff
- 00534428 ["INT_ADD", "register:40f0:8", ["const:534428:8", "const:4:8"]]
- 00534428 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00534748 ["INT_ADD", "register:40f0:8", ["const:534748:8", "const:4:8"]]
+ 00534748 ["CALL", null, ["callee:00c58fb0:8"]]
- 00534428 bytes ee8e1c94
+ 00534748 bytes 1a921c94
- 005343b4 ["INT_ADD", "register:40f0:8", ["const:5343b4:8", "const:4:8"]]
- 005343b4 ["CALL", null, ["callee:00c58f90:8"]]
+ 005346d4 ["INT_ADD", "register:40f0:8", ["const:5346d4:8", "const:4:8"]]
+ 005346d4 ["CALL", null, ["callee:00c58f90:8"]]
- 005343b4 bytes 038f1c94
+ 005346d4 bytes 2f921c94
- 005343c0 ["INT_ADD", "register:40f0:8", ["const:5343c0:8", "const:4:8"]]
- 005343c0 ["CALL", null, ["callee:00c58f30:8"]]
+ 005346e0 ["INT_ADD", "register:40f0:8", ["const:5346e0:8", "const:4:8"]]
+ 005346e0 ["CALL", null, ["callee:00c58f30:8"]]
- 005343c0 bytes e88e1c94
+ 005346e0 bytes 14921c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d96d2d6a5a357988df4b8a7d4fe2eb2"></a>

### [`0053446c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053446c.md) → [`0053478c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053478c.md) FUN_0053478c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053479c",
      "incomplete_value": false,
      "site": "0053479c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053447c",
      "incomplete_value": false,
      "site": "0053447c",
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
            "const:fe8:8"
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
      "0053479c",
      "DATA",
      [
        "storage",
        "00c66fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053479c",
      "DATA",
      [
        "storage",
        "00c67fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053446c.md#insn-00534474) · [`00534478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053446c.md#insn-00534478)
- 新版 [`00534794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053478c.md#insn-00534794) · [`00534798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/0053478c.md#insn-00534798)

~~~diff
- 00534474 ["COPY", "register:4048:8", ["const:c66000:8"]]
+ 00534794 ["COPY", "register:4048:8", ["const:c67000:8"]]
- 00534474 bytes 893900d0
+ 00534794 bytes 893900f0
- 00534478 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00534478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00534478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00534478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00534798 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00534798 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00534798 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00534798 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00534478 bytes 29a13f91
+ 00534798 bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c06c9d4ae706c4b6317d853af4636f6"></a>

### [`00534498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534498.md) → [`005347b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347b8.md) FUN_005347b8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005347c8",
      "incomplete_value": false,
      "site": "005347c8",
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
      "definition_site": "005344a8",
      "incomplete_value": false,
      "site": "005344a8",
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
      "005347c8",
      "DATA",
      [
        "storage",
        "00c67018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005347c8",
      "DATA",
      [
        "storage",
        "00c67fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005344a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534498.md#insn-005344a4)
- 新版 [`005347c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347b8.md#insn-005347c4)

~~~diff
- 005344a4 ["COPY", "tmp:0:8", ["const:18:8"]]
- 005344a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005344a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005344a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005347c4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 005347c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005347c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005347c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005344a4 bytes 29610091
+ 005347c4 bytes 29a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a2b44d433f3f23f3b4106f6e2518da6"></a>

### [`005344c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md) → [`005347e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347e4.md) FUN_005347e4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534808",
      "incomplete_value": true,
      "site": "00534814",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005344e8",
      "incomplete_value": true,
      "site": "005344f4",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00534834",
      "incomplete_value": true,
      "site": "00534834",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00534514",
      "incomplete_value": true,
      "site": "00534514",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00534860",
      "incomplete_value": true,
      "site": "00534860",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00534540",
      "incomplete_value": true,
      "site": "00534540",
      "value": [
        "LOAD",
        "8",
        [
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
      "005347fc",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00534814",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534824",
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
      "005347fc",
      "READ",
      [
        "storage",
        "00c9c078",
        null,
        "pointer"
      ]
    ],
    [
      "00534814",
      "DATA",
      [
        "storage",
        "00c68148",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00534824",
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

- 旧版 [`00534514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-00534514) · [`00534540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-00534540) · [`005344d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005344c4.md#insn-005344d4)
- 新版 [`00534834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347e4.md#insn-00534834) · [`00534860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347e4.md#insn-00534860) · [`005347f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/005347e4.md#insn-005347f4)

~~~diff
- 00534514 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534514 ["INT_ADD", "register:40f0:8", ["const:534514:8", "const:4:8"]]
- 00534514 ["CALLIND", null, ["register:0:8"]]
+ 00534834 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534834 ["INT_ADD", "register:40f0:8", ["const:534834:8", "const:4:8"]]
+ 00534834 ["CALLIND", null, ["register:0:8"]]
- 00534514 bytes 20013fd6
+ 00534834 bytes 20013fd6
- 00534540 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534540 ["INT_ADD", "register:40f0:8", ["const:534540:8", "const:4:8"]]
- 00534540 ["CALLIND", null, ["register:0:8"]]
+ 00534860 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00534860 ["INT_ADD", "register:40f0:8", ["const:534860:8", "const:4:8"]]
+ 00534860 ["CALLIND", null, ["register:0:8"]]
- 00534540 bytes 20013fd6
+ 00534860 bytes 20013fd6
- 005344d4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005347f4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005344d4 bytes 283b00f0
+ 005347f4 bytes 483b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49402b8236b56074a6b443a3f0143833"></a>

### [`00534570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md) → [`00534890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534890.md) FUN_00534890

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005348b4",
      "incomplete_value": true,
      "site": "005348c0",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534594",
      "incomplete_value": true,
      "site": "005345a0",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005348e0",
      "incomplete_value": true,
      "site": "005348e0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005345c0",
      "incomplete_value": true,
      "site": "005345c0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0053490c",
      "incomplete_value": true,
      "site": "0053490c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "005345ec",
      "incomplete_value": true,
      "site": "005345ec",
      "value": [
        "LOAD",
        "8",
        [
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
      "005348a8",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "005348c0",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005348d0",
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
      "005348a8",
      "READ",
      [
        "storage",
        "00c9c078",
        null,
        "pointer"
      ]
    ],
    [
      "005348c0",
      "DATA",
      [
        "storage",
        "00c68148",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005348d0",
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

- 旧版 [`005345c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-005345c0) · [`005345ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-005345ec) · [`00534580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534570.md#insn-00534580)
- 新版 [`005348e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534890.md#insn-005348e0) · [`0053490c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534890.md#insn-0053490c) · [`005348a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534890.md#insn-005348a0)

~~~diff
- 005345c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005345c0 ["INT_ADD", "register:40f0:8", ["const:5345c0:8", "const:4:8"]]
- 005345c0 ["CALLIND", null, ["register:0:8"]]
+ 005348e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005348e0 ["INT_ADD", "register:40f0:8", ["const:5348e0:8", "const:4:8"]]
+ 005348e0 ["CALLIND", null, ["register:0:8"]]
- 005345c0 bytes 20013fd6
+ 005348e0 bytes 20013fd6
- 005345ec ["COPY", "register:0:8", ["register:4048:8"]]
- 005345ec ["INT_ADD", "register:40f0:8", ["const:5345ec:8", "const:4:8"]]
- 005345ec ["CALLIND", null, ["register:0:8"]]
+ 0053490c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053490c ["INT_ADD", "register:40f0:8", ["const:53490c:8", "const:4:8"]]
+ 0053490c ["CALLIND", null, ["register:0:8"]]
- 005345ec bytes 20013fd6
+ 0053490c bytes 20013fd6
- 00534580 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005348a0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00534580 bytes 283b00f0
+ 005348a0 bytes 483b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce234231d43486c325be1b7cd87d3a79"></a>

### [`00534638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md) → [`00534958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534958.md) FUN_00534958

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00540114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053496c",
      "incomplete_value": true,
      "site": "00534970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053464c",
      "incomplete_value": true,
      "site": "00534650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8:8"
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
      "0053496c",
      "READ",
      [
        "storage",
        "00c9b0b8",
        null,
        "pointer"
      ]
    ],
    [
      "0053496c",
      "PARAM",
      [
        "storage",
        "00c673f8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "0053496c",
      "READ",
      [
        "storage",
        "00c9c088",
        null,
        "pointer"
      ]
    ],
    [
      "0053496c",
      "PARAM",
      [
        "storage",
        "00c683c8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-00534650) · [`00534644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-00534644) · [`0053464c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534638.md#insn-0053464c)
- 新版 [`00534970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534958.md#insn-00534970) · [`00534964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534958.md#insn-00534964) · [`0053496c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534958.md#insn-0053496c)

~~~diff
- 00534650 ["INT_ADD", "register:40f0:8", ["const:534650:8", "const:4:8"]]
- 00534650 ["CALL", null, ["callee:00540434:8"]]
+ 00534970 ["INT_ADD", "register:40f0:8", ["const:534970:8", "const:4:8"]]
+ 00534970 ["CALL", null, ["callee:00540434:8"]]
- 00534650 bytes b12e0094
+ 00534970 bytes b12e0094
- 00534644 ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 00534964 ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00534644 bytes 213b00f0
+ 00534964 bytes 413b0090
- 0053464c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b8:8"]]
- 0053464c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053496c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:88:8"]]
+ 0053496c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053464c bytes 215c40f9
+ 0053496c bytes 214440f9
~~~


<a id="compare-14fddea8917732bc047fcf942d920452"></a>

### [`00534674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md) → [`00534994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534994.md) FUN_00534994

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00540114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540114.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00540434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540434.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005349a8",
      "incomplete_value": true,
      "site": "005349b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00534688",
      "incomplete_value": true,
      "site": "00534690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8:8"
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
      "005349a8",
      "READ",
      [
        "storage",
        "00c9b0b8",
        null,
        "pointer"
      ]
    ],
    [
      "005349a8",
      "PARAM",
      [
        "storage",
        "00c673f8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ],
  "added": [
    [
      "005349a8",
      "READ",
      [
        "storage",
        "00c9c088",
        null,
        "pointer"
      ]
    ],
    [
      "005349a8",
      "PARAM",
      [
        "storage",
        "00c683c8",
        "_ZTTN5Botan14RSA_PrivateKeyE",
        "pointer __((offset(0x80)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534690) · [`00534680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534680) · [`00534688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534674.md#insn-00534688)
- 新版 [`005349b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534994.md#insn-005349b0) · [`005349a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534994.md#insn-005349a0) · [`005349a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534994.md#insn-005349a8)

~~~diff
- 00534690 ["INT_ADD", "register:40f0:8", ["const:534690:8", "const:4:8"]]
- 00534690 ["CALL", null, ["callee:00540434:8"]]
+ 005349b0 ["INT_ADD", "register:40f0:8", ["const:5349b0:8", "const:4:8"]]
+ 005349b0 ["CALL", null, ["callee:00540434:8"]]
- 00534690 bytes a12e0094
+ 005349b0 bytes a12e0094
- 00534680 ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 005349a0 ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00534680 bytes 213b00f0
+ 005349a0 bytes 413b0090
- 00534688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b8:8"]]
- 00534688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005349a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:88:8"]]
+ 005349a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00534688 bytes 215c40f9
+ 005349a8 bytes 214440f9
~~~


<a id="compare-4870c744116169eed229ba2f91102ce9"></a>

### [`0053484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md) → [`00534b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534b6c.md) FUN_00534b6c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

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
      "definition_site": "00534b88",
      "incomplete_value": true,
      "site": "00534b8c",
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
      "definition_site": "00534868",
      "incomplete_value": true,
      "site": "0053486c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00534bc8",
      "incomplete_value": true,
      "site": "00534bcc",
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
      "definition_site": "005348a8",
      "incomplete_value": true,
      "site": "005348ac",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00534b80",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00534b8c",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534bc0",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00534b80",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ],
    [
      "00534b8c",
      "DATA",
      [
        "storage",
        "00c68b28",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00534bc0",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00534858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-00534858) · [`00534860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-00534860) · [`0053487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/0053484c.md#insn-0053487c)
- 新版 [`00534b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534b6c.md#insn-00534b78) · [`00534b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534b6c.md#insn-00534b80) · [`00534b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534b6c.md#insn-00534b9c)

~~~diff
- 00534858 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00534b78 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00534858 bytes 283b00f0
+ 00534b78 bytes 483b0090
- 00534860 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 00534860 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:180:8"]]
+ 00534b80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534860 bytes 08d940f9
+ 00534b80 bytes 08c140f9
- 0053487c ["INT_ADD", "register:40f0:8", ["const:53487c:8", "const:4:8"]]
- 0053487c ["CALL", null, ["callee:00c54d90:8"]]
+ 00534b9c ["INT_ADD", "register:40f0:8", ["const:534b9c:8", "const:4:8"]]
+ 00534b9c ["CALL", null, ["callee:00c54d90:8"]]
- 0053487c bytes 497d1c94
+ 00534b9c bytes 7d801c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b932abddf658dba92520c2a36d895f7"></a>

### [`005348fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md) → [`00534c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534c1c.md) FUN_00534c1c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00534c38",
      "incomplete_value": true,
      "site": "00534c3c",
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
      "definition_site": "00534918",
      "incomplete_value": true,
      "site": "0053491c",
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
      "00534c30",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00534c3c",
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
      "00534c30",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00534c3c",
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

- 旧版 [`00534908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534908) · [`00534910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534910) · [`00534928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/005348fc.md#insn-00534928)
- 新版 [`00534c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534c1c.md#insn-00534c28) · [`00534c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534c1c.md#insn-00534c30) · [`00534c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00534/00534c1c.md#insn-00534c48)

~~~diff
- 00534908 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00534c28 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00534908 bytes 283b00f0
+ 00534c28 bytes 483b0090
- 00534910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00534910 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00534c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 00534c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534910 bytes 081541f9
+ 00534c30 bytes 08fd40f9
- 00534928 ["INT_ADD", "register:40f0:8", ["const:534928:8", "const:4:8"]]
- 00534928 ["CALL", null, ["callee:00c58f50:8"]]
+ 00534c48 ["INT_ADD", "register:40f0:8", ["const:534c48:8", "const:4:8"]]
+ 00534c48 ["CALL", null, ["callee:00c58f50:8"]]
- 00534928 bytes 968d1c94
+ 00534c48 bytes c2901c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b28af5f9e1c55993474dfe5b23260552"></a>

### [`00534dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md) → [`005350e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005350e8.md) FUN_005350e8

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
      "definition_site": "00535104",
      "incomplete_value": true,
      "site": "00535108",
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
      "definition_site": "00534de4",
      "incomplete_value": true,
      "site": "00534de8",
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
      "005350fc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535108",
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
      "005350fc",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535108",
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

- 旧版 [`00534dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534dd4) · [`00534ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534ddc) · [`00534df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534dc8.md#insn-00534df4)
- 新版 [`005350f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005350e8.md#insn-005350f4) · [`005350fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005350e8.md#insn-005350fc) · [`00535114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005350e8.md#insn-00535114)

~~~diff
- 00534dd4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005350f4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534dd4 bytes 283b00d0
+ 005350f4 bytes 283b00d0
- 00534ddc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00534ddc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005350fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005350fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534ddc bytes 085147f9
+ 005350fc bytes 083947f9
- 00534df4 ["INT_ADD", "register:40f0:8", ["const:534df4:8", "const:4:8"]]
- 00534df4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535114 ["INT_ADD", "register:40f0:8", ["const:535114:8", "const:4:8"]]
+ 00535114 ["CALL", null, ["callee:00c58f50:8"]]
- 00534df4 bytes 638c1c94
+ 00535114 bytes 8f8f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b728975a0d6e9e6a2f08aa0b829237b"></a>

### [`00534e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md) → [`00535148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535148.md) FUN_00535148

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
      "definition_site": "00535164",
      "incomplete_value": true,
      "site": "00535168",
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
      "definition_site": "00534e44",
      "incomplete_value": true,
      "site": "00534e48",
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
      "0053515c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535168",
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
      "0053515c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535168",
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

- 旧版 [`00534e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e34) · [`00534e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e3c) · [`00534e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534e28.md#insn-00534e54)
- 新版 [`00535154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535148.md#insn-00535154) · [`0053515c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535148.md#insn-0053515c) · [`00535174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535148.md#insn-00535174)

~~~diff
- 00534e34 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535154 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534e34 bytes 283b00d0
+ 00535154 bytes 283b00d0
- 00534e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00534e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053515c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053515c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534e3c bytes 085147f9
+ 0053515c bytes 083947f9
- 00534e54 ["INT_ADD", "register:40f0:8", ["const:534e54:8", "const:4:8"]]
- 00534e54 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535174 ["INT_ADD", "register:40f0:8", ["const:535174:8", "const:4:8"]]
+ 00535174 ["CALL", null, ["callee:00c58f50:8"]]
- 00534e54 bytes 4b8c1c94
+ 00535174 bytes 778f1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee6583b04d4434f3bcc53df39019f89e"></a>

### [`00534ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md) → [`00535218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535218.md) FUN_00535218

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00535234",
      "incomplete_value": true,
      "site": "00535238",
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
      "definition_site": "00534f14",
      "incomplete_value": true,
      "site": "00534f18",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0053526c",
      "incomplete_value": true,
      "site": "0053526c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00534f4c",
      "incomplete_value": true,
      "site": "00534f4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0053522c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00535238",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0053525c",
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
      "0053522c",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "00535238",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0053525c",
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

- 旧版 [`00534f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f4c) · [`00534f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f04) · [`00534f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534ef8.md#insn-00534f0c)
- 新版 [`0053526c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535218.md#insn-0053526c) · [`00535224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535218.md#insn-00535224) · [`0053522c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535218.md#insn-0053522c)

~~~diff
- 00534f4c ["COPY", "register:0:8", ["register:4048:8"]]
- 00534f4c ["INT_ADD", "register:40f0:8", ["const:534f4c:8", "const:4:8"]]
- 00534f4c ["CALLIND", null, ["register:0:8"]]
+ 0053526c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053526c ["INT_ADD", "register:40f0:8", ["const:53526c:8", "const:4:8"]]
+ 0053526c ["CALLIND", null, ["register:0:8"]]
- 00534f4c bytes 20013fd6
+ 0053526c bytes 20013fd6
- 00534f04 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535224 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534f04 bytes 283b00d0
+ 00535224 bytes 283b00d0
- 00534f0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00534f0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053522c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 0053522c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534f0c bytes 08a147f9
+ 0053522c bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5fccc2191192815c2142591f2fdfa7a"></a>

### [`00534f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md) → [`00535290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535290.md) FUN_00535290

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005352ac",
      "incomplete_value": true,
      "site": "005352b0",
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
      "definition_site": "00534f8c",
      "incomplete_value": true,
      "site": "00534f90",
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
    "kind": "call_target",
    "new": {
      "definition_site": "005352e4",
      "incomplete_value": true,
      "site": "005352e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00534fc4",
      "incomplete_value": true,
      "site": "00534fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005352a4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "005352b0",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005352d4",
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
      "005352a4",
      "READ",
      [
        "storage",
        "00c9bf10",
        null,
        "pointer"
      ]
    ],
    [
      "005352b0",
      "DATA",
      [
        "storage",
        "00c67a78",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "005352d4",
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

- 旧版 [`00534fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534fc4) · [`00534f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534f7c) · [`00534f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00534/00534f70.md#insn-00534f84)
- 新版 [`005352e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535290.md#insn-005352e4) · [`0053529c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535290.md#insn-0053529c) · [`005352a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535290.md#insn-005352a4)

~~~diff
- 00534fc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00534fc4 ["INT_ADD", "register:40f0:8", ["const:534fc4:8", "const:4:8"]]
- 00534fc4 ["CALLIND", null, ["register:0:8"]]
+ 005352e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005352e4 ["INT_ADD", "register:40f0:8", ["const:5352e4:8", "const:4:8"]]
+ 005352e4 ["CALLIND", null, ["register:0:8"]]
- 00534fc4 bytes 20013fd6
+ 005352e4 bytes 20013fd6
- 00534f7c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053529c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00534f7c bytes 283b00d0
+ 0053529c bytes 283b00d0
- 00534f84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00534f84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005352a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 005352a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00534f84 bytes 08a147f9
+ 005352a4 bytes 088947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e7f8b5c8cf3acaf64c2d3d34050ec40"></a>

### [`00535074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md) → [`00535394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535394.md) FUN_00535394

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005353a8",
      "incomplete_value": true,
      "site": "005353a8",
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
      "definition_site": "00535088",
      "incomplete_value": true,
      "site": "00535088",
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
      "0053539c",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "005353a8",
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
      "0053539c",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "005353a8",
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

- 旧版 [`00535074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md#insn-00535074) · [`0053507c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535074.md#insn-0053507c)
- 新版 [`00535394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535394.md#insn-00535394) · [`0053539c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535394.md#insn-0053539c)

~~~diff
- 00535074 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00535394 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00535074 bytes 293b00d0
+ 00535394 bytes 293b00f0
- 0053507c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 0053507c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053539c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:50:8"]]
+ 0053539c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053507c bytes 294140f9
+ 0053539c bytes 292940f9
~~~


<a id="compare-b4230f0705f322e172354ee120d229ea"></a>

### [`00535398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md) → [`005356b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005356b8.md) FUN_005356b8

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
      "definition_site": "005356d4",
      "incomplete_value": true,
      "site": "005356d8",
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
      "definition_site": "005353b4",
      "incomplete_value": true,
      "site": "005353b8",
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
      "005356cc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005356d8",
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
      "005356cc",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005356d8",
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

- 旧版 [`005353a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353a4) · [`005353ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353ac) · [`005353c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535398.md#insn-005353c4)
- 新版 [`005356c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005356b8.md#insn-005356c4) · [`005356cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005356b8.md#insn-005356cc) · [`005356e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005356b8.md#insn-005356e4)

~~~diff
- 005353a4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005356c4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005353a4 bytes 283b00b0
+ 005356c4 bytes 283b00d0
- 005353ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005353ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005356cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005356cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005353ac bytes 085147f9
+ 005356cc bytes 083947f9
- 005353c4 ["INT_ADD", "register:40f0:8", ["const:5353c4:8", "const:4:8"]]
- 005353c4 ["CALL", null, ["callee:00c58f50:8"]]
+ 005356e4 ["INT_ADD", "register:40f0:8", ["const:5356e4:8", "const:4:8"]]
+ 005356e4 ["CALL", null, ["callee:00c58f50:8"]]
- 005353c4 bytes ef8a1c94
+ 005356e4 bytes 1b8e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-796e942abee24593499a12c443e5f4cd"></a>

### [`005353e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md) → [`00535700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535700.md) FUN_00535700

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
      "definition_site": "0053571c",
      "incomplete_value": true,
      "site": "00535720",
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
      "definition_site": "005353fc",
      "incomplete_value": true,
      "site": "00535400",
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
      "00535714",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535720",
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
      "00535714",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535720",
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

- 旧版 [`005353ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-005353ec) · [`005353f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-005353f4) · [`0053540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005353e0.md#insn-0053540c)
- 新版 [`0053570c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535700.md#insn-0053570c) · [`00535714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535700.md#insn-00535714) · [`0053572c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535700.md#insn-0053572c)

~~~diff
- 005353ec ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053570c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005353ec bytes 283b00b0
+ 0053570c bytes 283b00d0
- 005353f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005353f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005353f4 bytes 085147f9
+ 00535714 bytes 083947f9
- 0053540c ["INT_ADD", "register:40f0:8", ["const:53540c:8", "const:4:8"]]
- 0053540c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053572c ["INT_ADD", "register:40f0:8", ["const:53572c:8", "const:4:8"]]
+ 0053572c ["CALL", null, ["callee:00c58f50:8"]]
- 0053540c bytes dd8a1c94
+ 0053572c bytes 098e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa5ebef6411aee2910a8518a6f71c14"></a>

### [`00535428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md) → [`00535748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535748.md) FUN_00535748

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
      "definition_site": "00535764",
      "incomplete_value": true,
      "site": "00535768",
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
      "definition_site": "00535444",
      "incomplete_value": true,
      "site": "00535448",
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
      "0053575c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535768",
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
      "0053575c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535768",
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

- 旧版 [`00535434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-00535434) · [`0053543c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-0053543c) · [`00535454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535428.md#insn-00535454)
- 新版 [`00535754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535748.md#insn-00535754) · [`0053575c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535748.md#insn-0053575c) · [`00535774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535748.md#insn-00535774)

~~~diff
- 00535434 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535754 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535434 bytes 283b00b0
+ 00535754 bytes 283b00d0
- 0053543c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053543c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053575c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053575c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053543c bytes 085147f9
+ 0053575c bytes 083947f9
- 00535454 ["INT_ADD", "register:40f0:8", ["const:535454:8", "const:4:8"]]
- 00535454 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535774 ["INT_ADD", "register:40f0:8", ["const:535774:8", "const:4:8"]]
+ 00535774 ["CALL", null, ["callee:00c58f50:8"]]
- 00535454 bytes cb8a1c94
+ 00535774 bytes f78d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96cca160c79a8f5483fa29a599af8249"></a>

### [`00535470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md) → [`00535790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535790.md) FUN_00535790

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
      "definition_site": "005357ac",
      "incomplete_value": true,
      "site": "005357b0",
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
      "definition_site": "0053548c",
      "incomplete_value": true,
      "site": "00535490",
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
      "005357a4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005357b0",
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
      "005357a4",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005357b0",
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

- 旧版 [`0053547c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-0053547c) · [`00535484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-00535484) · [`0053549c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535470.md#insn-0053549c)
- 新版 [`0053579c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535790.md#insn-0053579c) · [`005357a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535790.md#insn-005357a4) · [`005357bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535790.md#insn-005357bc)

~~~diff
- 0053547c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053579c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053547c bytes 283b00b0
+ 0053579c bytes 283b00d0
- 00535484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005357a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535484 bytes 085147f9
+ 005357a4 bytes 083947f9
- 0053549c ["INT_ADD", "register:40f0:8", ["const:53549c:8", "const:4:8"]]
- 0053549c ["CALL", null, ["callee:00c58f50:8"]]
+ 005357bc ["INT_ADD", "register:40f0:8", ["const:5357bc:8", "const:4:8"]]
+ 005357bc ["CALL", null, ["callee:00c58f50:8"]]
- 0053549c bytes b98a1c94
+ 005357bc bytes e58d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d80047c9019511ef7ed9b639350366c"></a>

### [`005354b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md) → [`005357d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005357d8.md) FUN_005357d8

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
      "definition_site": "005357f4",
      "incomplete_value": true,
      "site": "005357f8",
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
      "definition_site": "005354d4",
      "incomplete_value": true,
      "site": "005354d8",
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
      "005357ec",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005357f8",
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
      "005357ec",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005357f8",
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

- 旧版 [`005354c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354c4) · [`005354cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354cc) · [`005354e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005354b8.md#insn-005354e4)
- 新版 [`005357e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005357d8.md#insn-005357e4) · [`005357ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005357d8.md#insn-005357ec) · [`00535804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005357d8.md#insn-00535804)

~~~diff
- 005354c4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005357e4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005354c4 bytes 283b00b0
+ 005357e4 bytes 283b00d0
- 005354cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005354cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005357ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005357ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005354cc bytes 085147f9
+ 005357ec bytes 083947f9
- 005354e4 ["INT_ADD", "register:40f0:8", ["const:5354e4:8", "const:4:8"]]
- 005354e4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535804 ["INT_ADD", "register:40f0:8", ["const:535804:8", "const:4:8"]]
+ 00535804 ["CALL", null, ["callee:00c58f50:8"]]
- 005354e4 bytes a78a1c94
+ 00535804 bytes d38d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382def0ae48fdf738631ecd45e038457"></a>

### [`00535500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md) → [`00535820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535820.md) FUN_00535820

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
      "definition_site": "0053583c",
      "incomplete_value": true,
      "site": "00535840",
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
      "definition_site": "0053551c",
      "incomplete_value": true,
      "site": "00535520",
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
      "00535834",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535840",
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
      "00535834",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535840",
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

- 旧版 [`0053550c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-0053550c) · [`00535514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-00535514) · [`0053552c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535500.md#insn-0053552c)
- 新版 [`0053582c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535820.md#insn-0053582c) · [`00535834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535820.md#insn-00535834) · [`0053584c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535820.md#insn-0053584c)

~~~diff
- 0053550c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053582c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053550c bytes 283b00b0
+ 0053582c bytes 283b00d0
- 00535514 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535514 bytes 085147f9
+ 00535834 bytes 083947f9
- 0053552c ["INT_ADD", "register:40f0:8", ["const:53552c:8", "const:4:8"]]
- 0053552c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053584c ["INT_ADD", "register:40f0:8", ["const:53584c:8", "const:4:8"]]
+ 0053584c ["CALL", null, ["callee:00c58f50:8"]]
- 0053552c bytes 958a1c94
+ 0053584c bytes c18d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9378ff70b81e5d235b3f1cecabf9119a"></a>

### [`00535548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md) → [`00535868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535868.md) FUN_00535868

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
      "definition_site": "00535884",
      "incomplete_value": true,
      "site": "00535888",
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
      "definition_site": "00535564",
      "incomplete_value": true,
      "site": "00535568",
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
      "0053587c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535888",
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
      "0053587c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535888",
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

- 旧版 [`00535554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-00535554) · [`0053555c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-0053555c) · [`00535574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535548.md#insn-00535574)
- 新版 [`00535874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535868.md#insn-00535874) · [`0053587c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535868.md#insn-0053587c) · [`00535894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535868.md#insn-00535894)

~~~diff
- 00535554 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535874 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535554 bytes 283b00b0
+ 00535874 bytes 283b00d0
- 0053555c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053555c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053587c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053587c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053555c bytes 085147f9
+ 0053587c bytes 083947f9
- 00535574 ["INT_ADD", "register:40f0:8", ["const:535574:8", "const:4:8"]]
- 00535574 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535894 ["INT_ADD", "register:40f0:8", ["const:535894:8", "const:4:8"]]
+ 00535894 ["CALL", null, ["callee:00c58f50:8"]]
- 00535574 bytes 838a1c94
+ 00535894 bytes af8d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-036b864ac954a43666eb978c386855f2"></a>

### [`00535590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md) → [`005358b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358b0.md) FUN_005358b0

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
      "definition_site": "005358cc",
      "incomplete_value": true,
      "site": "005358d0",
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
      "definition_site": "005355ac",
      "incomplete_value": true,
      "site": "005355b0",
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
      "005358c4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005358d0",
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
      "005358c4",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005358d0",
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

- 旧版 [`0053559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-0053559c) · [`005355a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-005355a4) · [`005355bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535590.md#insn-005355bc)
- 新版 [`005358bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358b0.md#insn-005358bc) · [`005358c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358b0.md#insn-005358c4) · [`005358dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358b0.md#insn-005358dc)

~~~diff
- 0053559c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005358bc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053559c bytes 283b00b0
+ 005358bc bytes 283b00d0
- 005355a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005355a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005358c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005358c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355a4 bytes 085147f9
+ 005358c4 bytes 083947f9
- 005355bc ["INT_ADD", "register:40f0:8", ["const:5355bc:8", "const:4:8"]]
- 005355bc ["CALL", null, ["callee:00c58f50:8"]]
+ 005358dc ["INT_ADD", "register:40f0:8", ["const:5358dc:8", "const:4:8"]]
+ 005358dc ["CALL", null, ["callee:00c58f50:8"]]
- 005355bc bytes 718a1c94
+ 005358dc bytes 9d8d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09900f6d1865a89596b4861f9411ef9"></a>

### [`005355d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md) → [`005358f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358f8.md) FUN_005358f8

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
      "definition_site": "00535914",
      "incomplete_value": true,
      "site": "00535918",
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
      "definition_site": "005355f4",
      "incomplete_value": true,
      "site": "005355f8",
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
      "0053590c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535918",
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
      "0053590c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535918",
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

- 旧版 [`005355e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-005355e4) · [`005355ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-005355ec) · [`00535604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005355d8.md#insn-00535604)
- 新版 [`00535904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358f8.md#insn-00535904) · [`0053590c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358f8.md#insn-0053590c) · [`00535924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005358f8.md#insn-00535924)

~~~diff
- 005355e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535904 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005355e4 bytes 283b00b0
+ 00535904 bytes 283b00d0
- 005355ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005355ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053590c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053590c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005355ec bytes 085147f9
+ 0053590c bytes 083947f9
- 00535604 ["INT_ADD", "register:40f0:8", ["const:535604:8", "const:4:8"]]
- 00535604 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535924 ["INT_ADD", "register:40f0:8", ["const:535924:8", "const:4:8"]]
+ 00535924 ["CALL", null, ["callee:00c58f50:8"]]
- 00535604 bytes 5f8a1c94
+ 00535924 bytes 8b8d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a58140e7f420094f5266b9cb35ddf0f"></a>

### [`00535620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md) → [`00535940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535940.md) FUN_00535940

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
      "definition_site": "0053595c",
      "incomplete_value": true,
      "site": "00535960",
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
      "definition_site": "0053563c",
      "incomplete_value": true,
      "site": "00535640",
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
      "00535954",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535960",
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
      "00535954",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535960",
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

- 旧版 [`0053562c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-0053562c) · [`00535634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-00535634) · [`0053564c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535620.md#insn-0053564c)
- 新版 [`0053594c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535940.md#insn-0053594c) · [`00535954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535940.md#insn-00535954) · [`0053596c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535940.md#insn-0053596c)

~~~diff
- 0053562c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0053594c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053562c bytes 283b00b0
+ 0053594c bytes 283b00d0
- 00535634 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535954 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535954 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535634 bytes 085147f9
+ 00535954 bytes 083947f9
- 0053564c ["INT_ADD", "register:40f0:8", ["const:53564c:8", "const:4:8"]]
- 0053564c ["CALL", null, ["callee:00c58f50:8"]]
+ 0053596c ["INT_ADD", "register:40f0:8", ["const:53596c:8", "const:4:8"]]
+ 0053596c ["CALL", null, ["callee:00c58f50:8"]]
- 0053564c bytes 4d8a1c94
+ 0053596c bytes 798d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef4fac456ddb4f0e73cd7b212d1e070"></a>

### [`00535668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md) → [`00535988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535988.md) FUN_00535988

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
      "definition_site": "005359a4",
      "incomplete_value": true,
      "site": "005359a8",
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
      "definition_site": "00535684",
      "incomplete_value": true,
      "site": "00535688",
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
      "0053599c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005359a8",
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
      "0053599c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005359a8",
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

- 旧版 [`00535674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-00535674) · [`0053567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-0053567c) · [`00535694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535668.md#insn-00535694)
- 新版 [`00535994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535988.md#insn-00535994) · [`0053599c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535988.md#insn-0053599c) · [`005359b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535988.md#insn-005359b4)

~~~diff
- 00535674 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535994 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535674 bytes 283b00b0
+ 00535994 bytes 283b00d0
- 0053567c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053567c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053599c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0053599c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053567c bytes 085147f9
+ 0053599c bytes 083947f9
- 00535694 ["INT_ADD", "register:40f0:8", ["const:535694:8", "const:4:8"]]
- 00535694 ["CALL", null, ["callee:00c58f50:8"]]
+ 005359b4 ["INT_ADD", "register:40f0:8", ["const:5359b4:8", "const:4:8"]]
+ 005359b4 ["CALL", null, ["callee:00c58f50:8"]]
- 00535694 bytes 3b8a1c94
+ 005359b4 bytes 678d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9306ecc3d83c3160b593c0e260567d"></a>

### [`005356b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md) → [`005359d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005359d0.md) FUN_005359d0

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
      "definition_site": "005359ec",
      "incomplete_value": true,
      "site": "005359f0",
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
      "definition_site": "005356cc",
      "incomplete_value": true,
      "site": "005356d0",
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
      "005359e4",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005359f0",
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
      "005359e4",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005359f0",
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

- 旧版 [`005356bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356bc) · [`005356c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356c4) · [`005356dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356b0.md#insn-005356dc)
- 新版 [`005359dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005359d0.md#insn-005359dc) · [`005359e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005359d0.md#insn-005359e4) · [`005359fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/005359d0.md#insn-005359fc)

~~~diff
- 005356bc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005359dc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005356bc bytes 283b00b0
+ 005359dc bytes 283b00d0
- 005356c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005356c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005359e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005359e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005356c4 bytes 085147f9
+ 005359e4 bytes 083947f9
- 005356dc ["INT_ADD", "register:40f0:8", ["const:5356dc:8", "const:4:8"]]
- 005356dc ["CALL", null, ["callee:00c58f50:8"]]
+ 005359fc ["INT_ADD", "register:40f0:8", ["const:5359fc:8", "const:4:8"]]
+ 005359fc ["CALL", null, ["callee:00c58f50:8"]]
- 005356dc bytes 298a1c94
+ 005359fc bytes 558d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217a05c160c7a6343b2d4922fbc72d3f"></a>

### [`005356f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md) → [`00535a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a18.md) FUN_00535a18

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
      "definition_site": "00535a34",
      "incomplete_value": true,
      "site": "00535a38",
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
      "definition_site": "00535714",
      "incomplete_value": true,
      "site": "00535718",
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
      "00535a2c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535a38",
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
      "00535a2c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535a38",
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

- 旧版 [`00535704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-00535704) · [`0053570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-0053570c) · [`00535724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005356f8.md#insn-00535724)
- 新版 [`00535a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a18.md#insn-00535a24) · [`00535a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a18.md#insn-00535a2c) · [`00535a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a18.md#insn-00535a44)

~~~diff
- 00535704 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535a24 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535704 bytes 283b00b0
+ 00535a24 bytes 283b00d0
- 0053570c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053570c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535a2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535a2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053570c bytes 085147f9
+ 00535a2c bytes 083947f9
- 00535724 ["INT_ADD", "register:40f0:8", ["const:535724:8", "const:4:8"]]
- 00535724 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535a44 ["INT_ADD", "register:40f0:8", ["const:535a44:8", "const:4:8"]]
+ 00535a44 ["CALL", null, ["callee:00c58f50:8"]]
- 00535724 bytes 178a1c94
+ 00535a44 bytes 438d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb15dd75ff519c51d514adad24ac6e86"></a>

### [`00535740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md) → [`00535a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a60.md) FUN_00535a60

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
      "definition_site": "00535a7c",
      "incomplete_value": true,
      "site": "00535a80",
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
      "definition_site": "0053575c",
      "incomplete_value": true,
      "site": "00535760",
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
      "00535a74",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535a80",
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
      "00535a74",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535a80",
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

- 旧版 [`0053574c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-0053574c) · [`00535754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-00535754) · [`0053576c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535740.md#insn-0053576c)
- 新版 [`00535a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a60.md#insn-00535a6c) · [`00535a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a60.md#insn-00535a74) · [`00535a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535a60.md#insn-00535a8c)

~~~diff
- 0053574c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535a6c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053574c bytes 283b00b0
+ 00535a6c bytes 283b00d0
- 00535754 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535754 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535a74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535a74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535754 bytes 085147f9
+ 00535a74 bytes 083947f9
- 0053576c ["INT_ADD", "register:40f0:8", ["const:53576c:8", "const:4:8"]]
- 0053576c ["CALL", null, ["callee:00c58f50:8"]]
+ 00535a8c ["INT_ADD", "register:40f0:8", ["const:535a8c:8", "const:4:8"]]
+ 00535a8c ["CALL", null, ["callee:00c58f50:8"]]
- 0053576c bytes 058a1c94
+ 00535a8c bytes 318d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd97c5c0d7b6815d64d5d8dad53c75c"></a>

### [`00535788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md) → [`00535aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535aa8.md) FUN_00535aa8

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
      "definition_site": "00535ac4",
      "incomplete_value": true,
      "site": "00535ac8",
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
      "definition_site": "005357a4",
      "incomplete_value": true,
      "site": "005357a8",
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
      "00535abc",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ac8",
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
      "00535abc",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535ac8",
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

- 旧版 [`00535794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-00535794) · [`0053579c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-0053579c) · [`005357b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535788.md#insn-005357b4)
- 新版 [`00535ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535aa8.md#insn-00535ab4) · [`00535abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535aa8.md#insn-00535abc) · [`00535ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535aa8.md#insn-00535ad4)

~~~diff
- 00535794 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535ab4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535794 bytes 283b00b0
+ 00535ab4 bytes 283b00d0
- 0053579c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053579c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535abc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535abc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053579c bytes 085147f9
+ 00535abc bytes 083947f9
- 005357b4 ["INT_ADD", "register:40f0:8", ["const:5357b4:8", "const:4:8"]]
- 005357b4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535ad4 ["INT_ADD", "register:40f0:8", ["const:535ad4:8", "const:4:8"]]
+ 00535ad4 ["CALL", null, ["callee:00c58f50:8"]]
- 005357b4 bytes f3891c94
+ 00535ad4 bytes 1f8d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51a6fabb69acaec38565924fc4df0e7e"></a>

### [`005357d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md) → [`00535af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535af0.md) FUN_00535af0

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
      "definition_site": "00535b0c",
      "incomplete_value": true,
      "site": "00535b10",
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
      "definition_site": "005357ec",
      "incomplete_value": true,
      "site": "005357f0",
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
      "00535b04",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535b10",
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
      "00535b04",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535b10",
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

- 旧版 [`005357dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-005357dc) · [`005357e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-005357e4) · [`005357fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005357d0.md#insn-005357fc)
- 新版 [`00535afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535af0.md#insn-00535afc) · [`00535b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535af0.md#insn-00535b04) · [`00535b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535af0.md#insn-00535b1c)

~~~diff
- 005357dc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535afc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005357dc bytes 283b00b0
+ 00535afc bytes 283b00d0
- 005357e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005357e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005357e4 bytes 085147f9
+ 00535b04 bytes 083947f9
- 005357fc ["INT_ADD", "register:40f0:8", ["const:5357fc:8", "const:4:8"]]
- 005357fc ["CALL", null, ["callee:00c58f50:8"]]
+ 00535b1c ["INT_ADD", "register:40f0:8", ["const:535b1c:8", "const:4:8"]]
+ 00535b1c ["CALL", null, ["callee:00c58f50:8"]]
- 005357fc bytes e1891c94
+ 00535b1c bytes 0d8d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6aeebbf34b9cd5bb15bb42c577b9dd"></a>

### [`00535818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md) → [`00535b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b38.md) FUN_00535b38

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
      "definition_site": "00535b54",
      "incomplete_value": true,
      "site": "00535b58",
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
      "definition_site": "00535834",
      "incomplete_value": true,
      "site": "00535838",
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
      "00535b4c",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535b58",
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
      "00535b4c",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535b58",
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

- 旧版 [`00535824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-00535824) · [`0053582c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-0053582c) · [`00535844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535818.md#insn-00535844)
- 新版 [`00535b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b38.md#insn-00535b44) · [`00535b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b38.md#insn-00535b4c) · [`00535b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b38.md#insn-00535b64)

~~~diff
- 00535824 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535b44 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535824 bytes 283b00b0
+ 00535b44 bytes 283b00d0
- 0053582c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 0053582c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535b4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053582c bytes 085147f9
+ 00535b4c bytes 083947f9
- 00535844 ["INT_ADD", "register:40f0:8", ["const:535844:8", "const:4:8"]]
- 00535844 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535b64 ["INT_ADD", "register:40f0:8", ["const:535b64:8", "const:4:8"]]
+ 00535b64 ["CALL", null, ["callee:00c58f50:8"]]
- 00535844 bytes cf891c94
+ 00535b64 bytes fb8c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a7ed6b0e34210e9946ffdbc9c2f3df5"></a>

### [`00535860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md) → [`00535b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b80.md) FUN_00535b80

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
      "definition_site": "00535b9c",
      "incomplete_value": true,
      "site": "00535ba0",
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
      "definition_site": "0053587c",
      "incomplete_value": true,
      "site": "00535880",
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
      "00535b94",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535ba0",
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
      "00535b94",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535ba0",
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

- 旧版 [`0053586c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-0053586c) · [`00535874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-00535874) · [`0053588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535860.md#insn-0053588c)
- 新版 [`00535b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b80.md#insn-00535b8c) · [`00535b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b80.md#insn-00535b94) · [`00535bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535b80.md#insn-00535bac)

~~~diff
- 0053586c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535b8c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053586c bytes 283b00b0
+ 00535b8c bytes 283b00d0
- 00535874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535b94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535874 bytes 085147f9
+ 00535b94 bytes 083947f9
- 0053588c ["INT_ADD", "register:40f0:8", ["const:53588c:8", "const:4:8"]]
- 0053588c ["CALL", null, ["callee:00c58f50:8"]]
+ 00535bac ["INT_ADD", "register:40f0:8", ["const:535bac:8", "const:4:8"]]
+ 00535bac ["CALL", null, ["callee:00c58f50:8"]]
- 0053588c bytes bd891c94
+ 00535bac bytes e98c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b2ac3e8542c8c1c9ddd0115a8b13be"></a>

### [`005358ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md) → [`00535c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c0c.md) FUN_00535c0c

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
      "definition_site": "00535c28",
      "incomplete_value": true,
      "site": "00535c2c",
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
      "definition_site": "00535908",
      "incomplete_value": true,
      "site": "0053590c",
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
      "00535c20",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c2c",
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
      "00535c20",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535c2c",
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

- 旧版 [`005358f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-005358f8) · [`00535900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-00535900) · [`00535918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358ec.md#insn-00535918)
- 新版 [`00535c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c0c.md#insn-00535c18) · [`00535c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c0c.md#insn-00535c20) · [`00535c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c0c.md#insn-00535c38)

~~~diff
- 005358f8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535c18 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005358f8 bytes 283b00b0
+ 00535c18 bytes 283b00d0
- 00535900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535900 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535c20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535c20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535900 bytes 085147f9
+ 00535c20 bytes 083947f9
- 00535918 ["INT_ADD", "register:40f0:8", ["const:535918:8", "const:4:8"]]
- 00535918 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535c38 ["INT_ADD", "register:40f0:8", ["const:535c38:8", "const:4:8"]]
+ 00535c38 ["CALL", null, ["callee:00c58f50:8"]]
- 00535918 bytes 9a891c94
+ 00535c38 bytes c68c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d101df3818508b5a859f8da294daf81f"></a>

### [`00535934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md) → [`00535c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c54.md) FUN_00535c54

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
      "definition_site": "00535c70",
      "incomplete_value": true,
      "site": "00535c74",
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
      "definition_site": "00535950",
      "incomplete_value": true,
      "site": "00535954",
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
      "00535c68",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535c74",
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
      "00535c68",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535c74",
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

- 旧版 [`00535940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535940) · [`00535948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535948) · [`00535960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535934.md#insn-00535960)
- 新版 [`00535c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c54.md#insn-00535c60) · [`00535c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c54.md#insn-00535c68) · [`00535c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535c54.md#insn-00535c80)

~~~diff
- 00535940 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535c60 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535940 bytes 283b00b0
+ 00535c60 bytes 283b00d0
- 00535948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535948 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535948 bytes 085147f9
+ 00535c68 bytes 083947f9
- 00535960 ["INT_ADD", "register:40f0:8", ["const:535960:8", "const:4:8"]]
- 00535960 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535c80 ["INT_ADD", "register:40f0:8", ["const:535c80:8", "const:4:8"]]
+ 00535c80 ["CALL", null, ["callee:00c58f50:8"]]
- 00535960 bytes 88891c94
+ 00535c80 bytes b48c1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2458220e31d18ba0701c7d630bfb332e"></a>

### [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) → [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) FUN_00535ecc

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 35件 [`004a21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a21e8.md) [`004a506c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a506c.md) [`004a5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5d0c.md) [`004a766c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a766c.md) [`004a7c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7c48.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 35件 [`004a2508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a2/004a2508.md) [`004a538c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a538c.md) [`004a602c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a602c.md) [`004a798c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a798c.md) [`004a7f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7f68.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00535ed8",
      "incomplete_value": false,
      "site": "00535edc",
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
      "definition_site": "00535bb8",
      "incomplete_value": false,
      "site": "00535bbc",
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
      "00535ed8",
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
      "00535ed8",
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

- 旧版 [`00535bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md#insn-00535bbc) · [`00535bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md#insn-00535bb4) · [`00535bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md#insn-00535bb8)
- 新版 [`00535edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md#insn-00535edc) · [`00535ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md#insn-00535ed4) · [`00535ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md#insn-00535ed8)

~~~diff
- 00535bbc ["INT_ADD", "register:40f0:8", ["const:535bbc:8", "const:4:8"]]
- 00535bbc ["CALL", null, ["callee:0043bad8:8"]]
+ 00535edc ["INT_ADD", "register:40f0:8", ["const:535edc:8", "const:4:8"]]
+ 00535edc ["CALL", null, ["callee:0043bad8:8"]]
- 00535bbc bytes ff16fc97
+ 00535edc bytes ff16fc97
- 00535bb4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00535ed4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00535bb4 bytes 00ecffd0
+ 00535ed4 bytes 00ecfff0
- 00535bb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00535bb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535bb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535bb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00535ed8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00535ed8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00535ed8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00535ed8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535bb8 bytes 00303e91
+ 00535ed8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e0d9bf131357537a338486c81266574"></a>

### [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) → [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) FUN_00535ee0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 32件 [`004a55dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`004a6f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6f3c.md) [`004a8e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8e6c.md) [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)
- 新版 呼出元 32件 [`004a58fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a58fc.md) [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md) [`004a725c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a725c.md) [`004a918c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a9/004a918c.md) [`004c285c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c2/004c285c.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`0112b058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0112b/0112b058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00535f48",
      "incomplete_value": true,
      "site": "00535f48",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00535c28",
      "incomplete_value": true,
      "site": "00535c28",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00535f84",
      "incomplete_value": true,
      "site": "00535f84",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00535c64",
      "incomplete_value": true,
      "site": "00535c64",
      "value": [
        "LOAD",
        "8",
        [
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
      "00535f38",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00535f74",
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
      "00535f38",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00535f74",
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

- 旧版 [`00535c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535c28) · [`00535c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535c64) · [`00535bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md#insn-00535bdc)
- 新版 [`00535f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md#insn-00535f48) · [`00535f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md#insn-00535f84) · [`00535efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md#insn-00535efc)

~~~diff
- 00535c28 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535c28 ["INT_ADD", "register:40f0:8", ["const:535c28:8", "const:4:8"]]
- 00535c28 ["CALLIND", null, ["register:0:8"]]
+ 00535f48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535f48 ["INT_ADD", "register:40f0:8", ["const:535f48:8", "const:4:8"]]
+ 00535f48 ["CALLIND", null, ["register:0:8"]]
- 00535c28 bytes 20013fd6
+ 00535f48 bytes 20013fd6
- 00535c64 ["COPY", "register:0:8", ["register:4048:8"]]
- 00535c64 ["INT_ADD", "register:40f0:8", ["const:535c64:8", "const:4:8"]]
- 00535c64 ["CALLIND", null, ["register:0:8"]]
+ 00535f84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00535f84 ["INT_ADD", "register:40f0:8", ["const:535f84:8", "const:4:8"]]
+ 00535f84 ["CALLIND", null, ["register:0:8"]]
- 00535c64 bytes 20013fd6
+ 00535f84 bytes 20013fd6
- 00535bdc ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 00535efc ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 00535bdc bytes 953900d0
+ 00535efc bytes 953900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a116cc04a771aed7ccd561298b3075d"></a>

### [`00535c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md) → [`00535fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535fbc.md) FUN_00535fbc

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
      "definition_site": "00535fd8",
      "incomplete_value": true,
      "site": "00535fdc",
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
      "definition_site": "00535cb8",
      "incomplete_value": true,
      "site": "00535cbc",
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
      "00535fd0",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00535fdc",
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
      "00535fd0",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00535fdc",
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

- 旧版 [`00535ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535ca8) · [`00535cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535cb0) · [`00535cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535c9c.md#insn-00535cc8)
- 新版 [`00535fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535fbc.md#insn-00535fc8) · [`00535fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535fbc.md#insn-00535fd0) · [`00535fe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535fbc.md#insn-00535fe8)

~~~diff
- 00535ca8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00535fc8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535ca8 bytes 283b00b0
+ 00535fc8 bytes 283b00d0
- 00535cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00535fd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00535fd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535cb0 bytes 085147f9
+ 00535fd0 bytes 083947f9
- 00535cc8 ["INT_ADD", "register:40f0:8", ["const:535cc8:8", "const:4:8"]]
- 00535cc8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00535fe8 ["INT_ADD", "register:40f0:8", ["const:535fe8:8", "const:4:8"]]
+ 00535fe8 ["CALL", null, ["callee:00c58f50:8"]]
- 00535cc8 bytes ae881c94
+ 00535fe8 bytes da8b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd0dbb1ff0e8fdb1149722613f735ea8"></a>

### [`00535ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md) → [`00536004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536004.md) FUN_00536004

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)
- 新版 呼出元 1件 [`004aff70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004af/004aff70.md) · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ff0.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005360c4",
      "incomplete_value": true,
      "site": "005360c4",
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
      "definition_site": "00535da4",
      "incomplete_value": true,
      "site": "00535da4",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00536110",
      "incomplete_value": false,
      "site": "00536114",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535df0",
      "incomplete_value": false,
      "site": "00535df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c69000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536024",
      "incomplete_value": false,
      "site": "00536038",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535d04",
      "incomplete_value": false,
      "site": "00535d18",
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
            "const:28c:8"
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
      "00536024",
      "PARAM",
      [
        "storage",
        "002c128c",
        null,
        "string"
      ]
    ],
    [
      "00536040",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ],
    [
      "005360b0",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00536024",
      "PARAM",
      [
        "storage",
        "002c12d6",
        null,
        "string"
      ]
    ],
    [
      "00536040",
      "PARAM",
      [
        "storage",
        "002b0a42",
        null,
        null
      ]
    ],
    [
      "005360b0",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d18) · [`00535d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d28) · [`00535d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535ce4.md#insn-00535d04)
- 新版 [`00536038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536004.md#insn-00536038) · [`00536048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536004.md#insn-00536048) · [`00536024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536004.md#insn-00536024)

~~~diff
- 00535d18 ["INT_ADD", "register:40f0:8", ["const:535d18:8", "const:4:8"]]
- 00535d18 ["CALL", null, ["callee:00c59150:8"]]
+ 00536038 ["INT_ADD", "register:40f0:8", ["const:536038:8", "const:4:8"]]
+ 00536038 ["CALL", null, ["callee:00c59150:8"]]
- 00535d18 bytes 1a891c94
+ 00536038 bytes 468c1c94
- 00535d28 ["INT_ADD", "register:40f0:8", ["const:535d28:8", "const:4:8"]]
- 00535d28 ["CALL", null, ["callee:00c59010:8"]]
+ 00536048 ["INT_ADD", "register:40f0:8", ["const:536048:8", "const:4:8"]]
+ 00536048 ["CALL", null, ["callee:00c59010:8"]]
- 00535d28 bytes c6881c94
+ 00536048 bytes f28b1c94
- 00535d04 ["COPY", "tmp:0:8", ["const:28c:8"]]
- 00535d04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00535d04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00535d04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00536024 ["COPY", "tmp:0:8", ["const:2d6:8"]]
+ 00536024 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00536024 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00536024 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00535d04 bytes 00300a91
+ 00536024 bytes 00580b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3caa67621dd89b26152dbec37ecd8cb5"></a>

### [`00535eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md) → [`0053620c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053620c.md) FUN_0053620c

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
      "definition_site": "00536228",
      "incomplete_value": true,
      "site": "0053622c",
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
      "definition_site": "00535f08",
      "incomplete_value": true,
      "site": "00535f0c",
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
      "00536220",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "0053622c",
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
      "00536220",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "0053622c",
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

- 旧版 [`00535ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535ef8) · [`00535f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535f00) · [`00535f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535eec.md#insn-00535f18)
- 新版 [`00536218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053620c.md#insn-00536218) · [`00536220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053620c.md#insn-00536220) · [`00536238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053620c.md#insn-00536238)

~~~diff
- 00535ef8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00536218 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535ef8 bytes 283b00b0
+ 00536218 bytes 283b00b0
- 00535f00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535f00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00536220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535f00 bytes 085147f9
+ 00536220 bytes 083947f9
- 00535f18 ["INT_ADD", "register:40f0:8", ["const:535f18:8", "const:4:8"]]
- 00535f18 ["CALL", null, ["callee:00c58f50:8"]]
+ 00536238 ["INT_ADD", "register:40f0:8", ["const:536238:8", "const:4:8"]]
+ 00536238 ["CALL", null, ["callee:00c58f50:8"]]
- 00535f18 bytes 1a881c94
+ 00536238 bytes 468b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47e06c31f5493816a371fbb783a8e48b"></a>

### [`00535f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md) → [`00536254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536254.md) FUN_00536254

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
      "definition_site": "00536270",
      "incomplete_value": true,
      "site": "00536274",
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
      "definition_site": "00535f50",
      "incomplete_value": true,
      "site": "00535f54",
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
      "00536268",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "00536274",
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
      "00536268",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "00536274",
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

- 旧版 [`00535f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f40) · [`00535f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f48) · [`00535f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535f34.md#insn-00535f60)
- 新版 [`00536260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536254.md#insn-00536260) · [`00536268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536254.md#insn-00536268) · [`00536280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536254.md#insn-00536280)

~~~diff
- 00535f40 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00536260 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00535f40 bytes 283b00b0
+ 00536260 bytes 283b00b0
- 00535f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00535f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00536268 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00535f48 bytes 085147f9
+ 00536268 bytes 083947f9
- 00535f60 ["INT_ADD", "register:40f0:8", ["const:535f60:8", "const:4:8"]]
- 00535f60 ["CALL", null, ["callee:00c58f50:8"]]
+ 00536280 ["INT_ADD", "register:40f0:8", ["const:536280:8", "const:4:8"]]
+ 00536280 ["CALL", null, ["callee:00c58f50:8"]]
- 00535f60 bytes 08881c94
+ 00536280 bytes 348b1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3e857be0d9da801f8fc70fcbaf1a39"></a>

### [`00535fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md) → [`005362c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005362c4.md) FUN_005362c4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004f8e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8e70.md) [`004f8fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f8/004f8fac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004f9190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f9/004f9190.md) [`004f92cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f9/004f92cc.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md) [`00c58f10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005362ec",
      "incomplete_value": false,
      "site": "005362fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535fcc",
      "incomplete_value": false,
      "site": "00535fdc",
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
            "const:380:8"
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
      "definition_site": "00536314",
      "incomplete_value": false,
      "site": "00536318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00535ff4",
      "incomplete_value": false,
      "site": "00535ff8",
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
            "const:390:8"
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
      "definition_site": "00536328",
      "incomplete_value": false,
      "site": "0053633c",
      "value": [
        "leaf",
        "const:4f92cc:8"
      ]
    },
    "old": {
      "definition_site": "00536008",
      "incomplete_value": false,
      "site": "0053601c",
      "value": [
        "leaf",
        "const:4f8fac:8"
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
      "005362dc",
      "READ",
      [
        "storage",
        "00ca5390",
        null,
        "undefined1"
      ]
    ],
    [
      "005362ec",
      "PARAM",
      [
        "storage",
        "00ca5380",
        null,
        "undefined8"
      ]
    ],
    [
      "00536314",
      "PARAM",
      [
        "storage",
        "00ca5390",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005362dc",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined1"
      ]
    ],
    [
      "005362ec",
      "PARAM",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00536314",
      "PARAM",
      [
        "storage",
        "00ca6350",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00535fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-00535fdc) · [`00535ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-00535ff8) · [`0053601c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535fa4.md#insn-0053601c)
- 新版 [`005362fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005362c4.md#insn-005362fc) · [`00536318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005362c4.md#insn-00536318) · [`0053633c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005362c4.md#insn-0053633c)

~~~diff
- 00535fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00535fdc ["INT_ADD", "register:40f0:8", ["const:535fdc:8", "const:4:8"]]
- 00535fdc ["CALLIND", null, ["register:0:8"]]
+ 005362fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005362fc ["INT_ADD", "register:40f0:8", ["const:5362fc:8", "const:4:8"]]
+ 005362fc ["CALLIND", null, ["register:0:8"]]
- 00535fdc bytes 00013fd6
+ 005362fc bytes 00013fd6
- 00535ff8 ["INT_ADD", "register:40f0:8", ["const:535ff8:8", "const:4:8"]]
- 00535ff8 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00536318 ["INT_ADD", "register:40f0:8", ["const:536318:8", "const:4:8"]]
+ 00536318 ["CALL", null, ["callee:00c58ef0:8"]]
- 00535ff8 bytes ca871c94
+ 00536318 bytes f68a1c94
- 0053601c ["INT_ADD", "register:40f0:8", ["const:53601c:8", "const:4:8"]]
- 0053601c ["CALL", null, ["callee:00c58ed0:8"]]
+ 0053633c ["INT_ADD", "register:40f0:8", ["const:53633c:8", "const:4:8"]]
+ 0053633c ["CALL", null, ["callee:00c58ed0:8"]]
- 0053601c bytes b9871c94
+ 0053633c bytes e58a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1beff8fe36ea705fbeae0071638d9500"></a>

### [`00536050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md) → [`00536370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536370.md) FUN_00536370

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004c5df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5df4.md) [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`004e3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e3/004e3504.md) · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e50.md)
- 新版 呼出元 3件 [`004c6114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004c6/004c6114.md) [`004e27b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e2/004e27b4.md) [`004e3824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e3/004e3824.md) · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "00536468",
      "incomplete_value": true,
      "site": "00536474",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00536148",
      "incomplete_value": true,
      "site": "00536154",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "definition_site": "00536464",
      "incomplete_value": false,
      "site": "00536474",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00536144",
      "incomplete_value": false,
      "site": "00536154",
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
      "00536464",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00536468",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "00536468",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00536464",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00536468",
      "READ",
      [
        "storage",
        "00c9bed8",
        null,
        "pointer"
      ]
    ],
    [
      "00536468",
      "PARAM",
      [
        "storage",
        "00c67ec8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-00536154) · [`00536088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-00536088) · [`005360c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536050.md#insn-005360c8)
- 新版 [`00536474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536370.md#insn-00536474) · [`005363a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536370.md#insn-005363a8) · [`005363e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536370.md#insn-005363e8)

~~~diff
- 00536154 ["INT_ADD", "register:40f0:8", ["const:536154:8", "const:4:8"]]
- 00536154 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00536474 ["INT_ADD", "register:40f0:8", ["const:536474:8", "const:4:8"]]
+ 00536474 ["CALL", null, ["callee:00c58fb0:8"]]
- 00536154 bytes a3871c94
+ 00536474 bytes cf8a1c94
- 00536088 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536088 ["INT_ADD", "register:40f0:8", ["const:536088:8", "const:4:8"]]
- 00536088 ["CALLIND", null, ["register:0:8"]]
+ 005363a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005363a8 ["INT_ADD", "register:40f0:8", ["const:5363a8:8", "const:4:8"]]
+ 005363a8 ["CALLIND", null, ["register:0:8"]]
- 00536088 bytes 20013fd6
+ 005363a8 bytes 20013fd6
- 005360c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005360c8 ["INT_ADD", "register:40f0:8", ["const:5360c8:8", "const:4:8"]]
- 005360c8 ["CALLIND", null, ["register:0:8"]]
+ 005363e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005363e8 ["INT_ADD", "register:40f0:8", ["const:5363e8:8", "const:4:8"]]
+ 005363e8 ["CALLIND", null, ["register:0:8"]]
- 005360c8 bytes 00013fd6
+ 005363e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac497be6e8f6464c4f6669239dc007c4"></a>

### [`005361a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md) → [`005364c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005364c4.md) FUN_005364c4

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
      "definition_site": "005364e0",
      "incomplete_value": true,
      "site": "005364e4",
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
      "definition_site": "005361c0",
      "incomplete_value": true,
      "site": "005361c4",
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
      "005364d8",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "005364e4",
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
      "005364d8",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "005364e4",
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

- 旧版 [`005361b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361b0) · [`005361b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361b8) · [`005361d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361a4.md#insn-005361d0)
- 新版 [`005364d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005364c4.md#insn-005364d0) · [`005364d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005364c4.md#insn-005364d8) · [`005364f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/005364c4.md#insn-005364f0)

~~~diff
- 005361b0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005364d0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005361b0 bytes 283b0090
+ 005364d0 bytes 283b00b0
- 005361b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 005361b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005364d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 005364d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005361b8 bytes 085147f9
+ 005364d8 bytes 083947f9
- 005361d0 ["INT_ADD", "register:40f0:8", ["const:5361d0:8", "const:4:8"]]
- 005361d0 ["CALL", null, ["callee:00c58f50:8"]]
+ 005364f0 ["INT_ADD", "register:40f0:8", ["const:5364f0:8", "const:4:8"]]
+ 005364f0 ["CALL", null, ["callee:00c58f50:8"]]
- 005361d0 bytes 6c871c94
+ 005364f0 bytes 988a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff375cbc7de4810f7c8a357c4b6b0001"></a>

### [`005361ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md) → [`0053650c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053650c.md) FUN_0053650c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004ce9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ce/004ce9d4.md) [`004f5aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f5/004f5aa4.md) [`004f6a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f6/004f6a04.md) [`004f6ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f6/004f6ab8.md) · 呼出先 8件 [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 4件 [`004cecf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ce/004cecf4.md) [`004f5dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f5/004f5dc4.md) [`004f6d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f6/004f6d24.md) [`004f6dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f6/004f6dd8.md) · 呼出先 8件 [`00536694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536600",
      "incomplete_value": true,
      "site": "00536608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005362e0",
      "incomplete_value": true,
      "site": "005362e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00536604",
      "incomplete_value": true,
      "site": "00536608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005362e4",
      "incomplete_value": true,
      "site": "005362e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00536600",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00536600",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00536604",
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
      "00536600",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00536600",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00536604",
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

- 旧版 [`005362e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-005362e8) · [`0053623c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-0053623c) · [`00536268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md#insn-00536268)
- 新版 [`00536608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053650c.md#insn-00536608) · [`0053655c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053650c.md#insn-0053655c) · [`00536588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053650c.md#insn-00536588)

~~~diff
- 005362e8 ["INT_ADD", "register:40f0:8", ["const:5362e8:8", "const:4:8"]]
- 005362e8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00536608 ["INT_ADD", "register:40f0:8", ["const:536608:8", "const:4:8"]]
+ 00536608 ["CALL", null, ["callee:00c58fb0:8"]]
- 005362e8 bytes 3e871c94
+ 00536608 bytes 6a8a1c94
- 0053623c ["INT_ADD", "register:40f0:8", ["const:53623c:8", "const:4:8"]]
- 0053623c ["CALL", null, ["callee:00c59ad0:8"]]
+ 0053655c ["INT_ADD", "register:40f0:8", ["const:53655c:8", "const:4:8"]]
+ 0053655c ["CALL", null, ["callee:00c59ad0:8"]]
- 0053623c bytes 318a1c94
+ 0053655c bytes 5d8d1c94
- 00536268 ["INT_ADD", "register:40f0:8", ["const:536268:8", "const:4:8"]]
- 00536268 ["CALL", null, ["callee:00c590a0:8"]]
+ 00536588 ["INT_ADD", "register:40f0:8", ["const:536588:8", "const:4:8"]]
+ 00536588 ["CALL", null, ["callee:00c590a0:8"]]
- 00536268 bytes 9a871c94
+ 00536588 bytes c68a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d09e566df372a5b61c42e6104eda9c5"></a>

### [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) → [`00536694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md) FUN_00536694

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`005361ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005361ec.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 4件 [`004b8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b8/004b8bb0.md) [`0053650c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/0053650c.md) [`00540c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c80.md) [`00543a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005366a0",
      "incomplete_value": false,
      "site": "005366a4",
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
      "definition_site": "00536380",
      "incomplete_value": false,
      "site": "00536384",
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
      "005366a0",
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
      "005366a0",
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

- 旧版 [`00536384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md#insn-00536384) · [`0053637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md#insn-0053637c) · [`00536380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md#insn-00536380)
- 新版 [`005366a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md#insn-005366a4) · [`0053669c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md#insn-0053669c) · [`005366a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536694.md#insn-005366a0)

~~~diff
- 00536384 ["INT_ADD", "register:40f0:8", ["const:536384:8", "const:4:8"]]
- 00536384 ["CALL", null, ["callee:0043bad8:8"]]
+ 005366a4 ["INT_ADD", "register:40f0:8", ["const:5366a4:8", "const:4:8"]]
+ 005366a4 ["CALL", null, ["callee:0043bad8:8"]]
- 00536384 bytes 0d15fc97
+ 005366a4 bytes 0d15fc97
- 0053637c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0053669c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0053637c bytes 00ecffb0
+ 0053669c bytes 00ecffd0
- 00536380 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00536380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00536380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00536380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005366a0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005366a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005366a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005366a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00536380 bytes 00303e91
+ 005366a0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8193eedd19d404d65ce20445e37c086"></a>

### [`005366f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md) → [`00536a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536a14.md) FUN_00536a14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004e2494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004e2/004e2494.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00549acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549acc.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 3件 [`004e27b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004e2/004e27b4.md) [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) [`00549dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549dec.md) · 呼出先 4件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536a5c",
      "incomplete_value": true,
      "site": "00536a5c",
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
      "definition_site": "0053673c",
      "incomplete_value": true,
      "site": "0053673c",
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
      "definition_site": "00536a5c",
      "incomplete_value": true,
      "site": "00536a5c",
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
      "definition_site": "0053673c",
      "incomplete_value": true,
      "site": "0053673c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00536a3c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00536a48",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00536a5c",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00536a3c",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00536a48",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00536a5c",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053670c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md#insn-0053670c) · [`00536710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md#insn-00536710) · [`0053671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/005366f4.md#insn-0053671c)
- 新版 [`00536a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536a14.md#insn-00536a2c) · [`00536a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536a14.md#insn-00536a30) · [`00536a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536a14.md#insn-00536a3c)

~~~diff
- 0053670c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00536a2c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0053670c bytes 283b0090
+ 00536a2c bytes 283b00b0
- 00536710 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00536a30 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00536710 bytes 293b0090
+ 00536a30 bytes 293b00b0
- 0053671c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 0053671c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00536a3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 00536a3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053671c bytes 080547f9
+ 00536a3c bytes 08ed46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562389bce151058560a589b1cf8756f1"></a>

### [`0053681c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md) → [`00536b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536b3c.md) FUN_00536b3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a050.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536b88",
      "incomplete_value": true,
      "site": "00536b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:521:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536868",
      "incomplete_value": true,
      "site": "00536868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:452:8"
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
      "definition_site": "00536b78",
      "incomplete_value": true,
      "site": "00536b8c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536858",
      "incomplete_value": true,
      "site": "0053686c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7:8"
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
      "definition_site": "00536bb4",
      "incomplete_value": true,
      "site": "00536bc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536894",
      "incomplete_value": true,
      "site": "005368a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c0:8"
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
      "00536b70",
      "READ",
      [
        "storage",
        "002b7452",
        null,
        "string"
      ]
    ],
    [
      "00536b78",
      "READ",
      [
        "storage",
        "002b7459",
        null,
        "string"
      ]
    ],
    [
      "00536bb0",
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
      "00536b70",
      "READ",
      [
        "storage",
        "002b7521",
        null,
        "string"
      ]
    ],
    [
      "00536b78",
      "READ",
      [
        "storage",
        "002b7528",
        null,
        "string"
      ]
    ],
    [
      "00536bb0",
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

- 旧版 [`005368a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-005368a0) · [`00536840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-00536840) · [`0053684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/0053681c.md#insn-0053684c)
- 新版 [`00536bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536b3c.md#insn-00536bc0) · [`00536b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536b3c.md#insn-00536b60) · [`00536b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536b3c.md#insn-00536b6c)

~~~diff
- 005368a0 ["INT_ADD", "register:40f0:8", ["const:5368a0:8", "const:4:8"]]
- 005368a0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00536bc0 ["INT_ADD", "register:40f0:8", ["const:536bc0:8", "const:4:8"]]
+ 00536bc0 ["CALL", null, ["callee:00c58fb0:8"]]
- 005368a0 bytes d0851c94
+ 00536bc0 bytes fc881c94
- 00536840 ["INT_ADD", "register:40f0:8", ["const:536840:8", "const:4:8"]]
- 00536840 ["CALL", null, ["callee:00c58f90:8"]]
+ 00536b60 ["INT_ADD", "register:40f0:8", ["const:536b60:8", "const:4:8"]]
+ 00536b60 ["CALL", null, ["callee:00c58f90:8"]]
- 00536840 bytes e0851c94
+ 00536b60 bytes 0c891c94
- 0053684c ["COPY", "tmp:0:8", ["const:452:8"]]
- 0053684c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053684c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053684c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00536b6c ["COPY", "tmp:0:8", ["const:521:8"]]
+ 00536b6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00536b6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00536b6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053684c bytes 29491191
+ 00536b6c bytes 29851491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cbec41f043b72ed5e9cd62f22c98700"></a>

### [`00536a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md) → [`00536d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536d88.md) FUN_00536d88

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`005459b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00545/005459b8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)
- 新版 呼出元 2件 [`004ed070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ed/004ed070.md) [`00545cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00545/00545cd8.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59150.md) [`00c59820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59820.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00536dec",
      "incomplete_value": true,
      "site": "00536df0",
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
      "definition_site": "00536acc",
      "incomplete_value": true,
      "site": "00536ad0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00536e0c",
      "incomplete_value": true,
      "site": "00536e10",
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
      "definition_site": "00536aec",
      "incomplete_value": true,
      "site": "00536af0",
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
      "definition_site": "00536e28",
      "incomplete_value": true,
      "site": "00536e2c",
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
      "definition_site": "00536b08",
      "incomplete_value": true,
      "site": "00536b0c",
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
      "00536da4",
      "PARAM",
      [
        "storage",
        "002bc6cf",
        null,
        "string"
      ]
    ],
    [
      "00536dbc",
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      "00536dd0",
      "PARAM",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00536da4",
      "PARAM",
      [
        "storage",
        "002bc7ad",
        null,
        "string"
      ]
    ],
    [
      "00536dbc",
      "PARAM",
      [
        "storage",
        "002bfeae",
        null,
        "string"
      ]
    ],
    [
      "00536dd0",
      "PARAM",
      [
        "storage",
        "002a654a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536a94) · [`00536aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536aa8) · [`00536abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536a68.md#insn-00536abc)
- 新版 [`00536db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536d88.md#insn-00536db4) · [`00536dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536d88.md#insn-00536dc8) · [`00536ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536d88.md#insn-00536ddc)

~~~diff
- 00536a94 ["INT_ADD", "register:40f0:8", ["const:536a94:8", "const:4:8"]]
- 00536a94 ["CALL", null, ["callee:00c59150:8"]]
+ 00536db4 ["INT_ADD", "register:40f0:8", ["const:536db4:8", "const:4:8"]]
+ 00536db4 ["CALL", null, ["callee:00c59150:8"]]
- 00536a94 bytes bb851c94
+ 00536db4 bytes e7881c94
- 00536aa8 ["INT_ADD", "register:40f0:8", ["const:536aa8:8", "const:4:8"]]
- 00536aa8 ["CALL", null, ["callee:00c59150:8"]]
+ 00536dc8 ["INT_ADD", "register:40f0:8", ["const:536dc8:8", "const:4:8"]]
+ 00536dc8 ["CALL", null, ["callee:00c59150:8"]]
- 00536aa8 bytes b6851c94
+ 00536dc8 bytes e2881c94
- 00536abc ["INT_ADD", "register:40f0:8", ["const:536abc:8", "const:4:8"]]
- 00536abc ["CALL", null, ["callee:00c59820:8"]]
+ 00536ddc ["INT_ADD", "register:40f0:8", ["const:536ddc:8", "const:4:8"]]
+ 00536ddc ["CALL", null, ["callee:00c59820:8"]]
- 00536abc bytes 65871c94
+ 00536ddc bytes 918a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d420bf4688df4a90b59d314fe9eb9e"></a>

### [`00536b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md) → [`00536e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536e98.md) FUN_00536e98

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c58af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58af0.md) [`00c58b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md)
- 新版 呼出元 1件 [`004ed070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ed/004ed070.md) · 呼出先 7件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c597a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597a0.md) [`00c59ac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59ac0.md) [`00c59b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59b20.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00536f58",
      "incomplete_value": true,
      "site": "00536f58",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00536c38",
      "incomplete_value": true,
      "site": "00536c38",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00536f9c",
      "incomplete_value": true,
      "site": "00536f9c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00536c7c",
      "incomplete_value": true,
      "site": "00536c7c",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00536f48",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00536f8c",
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
      "00536f48",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00536f8c",
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

- 旧版 [`00536c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536c38) · [`00536c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536c7c) · [`00536bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536b78.md#insn-00536bb0)
- 新版 [`00536f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536e98.md#insn-00536f58) · [`00536f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536e98.md#insn-00536f9c) · [`00536ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00536/00536e98.md#insn-00536ed0)

~~~diff
- 00536c38 ["COPY", "register:0:8", ["register:4048:8"]]
- 00536c38 ["INT_ADD", "register:40f0:8", ["const:536c38:8", "const:4:8"]]
- 00536c38 ["CALLIND", null, ["register:0:8"]]
+ 00536f58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536f58 ["INT_ADD", "register:40f0:8", ["const:536f58:8", "const:4:8"]]
+ 00536f58 ["CALLIND", null, ["register:0:8"]]
- 00536c38 bytes 20013fd6
+ 00536f58 bytes 20013fd6
- 00536c7c ["COPY", "register:0:8", ["register:4048:8"]]
- 00536c7c ["INT_ADD", "register:40f0:8", ["const:536c7c:8", "const:4:8"]]
- 00536c7c ["CALLIND", null, ["register:0:8"]]
+ 00536f9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00536f9c ["INT_ADD", "register:40f0:8", ["const:536f9c:8", "const:4:8"]]
+ 00536f9c ["CALLIND", null, ["register:0:8"]]
- 00536c7c bytes 20013fd6
+ 00536f9c bytes 20013fd6
- 00536bb0 ["INT_ADD", "register:40f0:8", ["const:536bb0:8", "const:4:8"]]
- 00536bb0 ["CALL", null, ["callee:00c5a780:8"]]
+ 00536ed0 ["INT_ADD", "register:40f0:8", ["const:536ed0:8", "const:4:8"]]
+ 00536ed0 ["CALL", null, ["callee:00c5a780:8"]]
- 00536bb0 bytes 008b1c94
+ 00536ed0 bytes 2c8e1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d9bb4e9c45707828a046fc3a7355d3"></a>

### [`00536cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md) → [`0053701c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053701c.md) FUN_0053701c

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
      "definition_site": "00537038",
      "incomplete_value": true,
      "site": "0053703c",
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
      "definition_site": "00536d18",
      "incomplete_value": true,
      "site": "00536d1c",
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
      "00537030",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "0053703c",
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
      "00537030",
      "READ",
      [
        "storage",
        "00c9be70",
        null,
        "pointer"
      ]
    ],
    [
      "0053703c",
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

- 旧版 [`00536d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d08) · [`00536d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d10) · [`00536d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536cfc.md#insn-00536d28)
- 新版 [`00537028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053701c.md#insn-00537028) · [`00537030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053701c.md#insn-00537030) · [`00537048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053701c.md#insn-00537048)

~~~diff
- 00536d08 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00537028 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00536d08 bytes 283b0090
+ 00537028 bytes 283b0090
- 00536d10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00536d10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 00537030 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00536d10 bytes 085147f9
+ 00537030 bytes 083947f9
- 00536d28 ["INT_ADD", "register:40f0:8", ["const:536d28:8", "const:4:8"]]
- 00536d28 ["CALL", null, ["callee:00c58f50:8"]]
+ 00537048 ["INT_ADD", "register:40f0:8", ["const:537048:8", "const:4:8"]]
+ 00537048 ["CALL", null, ["callee:00c58f50:8"]]
- 00536d28 bytes 96841c94
+ 00537048 bytes c2871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-658ac883d771e381ae03747624168d1b"></a>

### [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) → [`00537064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md) FUN_00537064

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004f1614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f1/004f1614.md) [`0050efcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md) · 呼出先 8件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`004f1934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004f1/004f1934.md) [`0050f2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f2ec.md) · 呼出先 8件 [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) [`00c38c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c34.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

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
      "definition_site": "00537154",
      "incomplete_value": true,
      "site": "0053715c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00536e34",
      "incomplete_value": true,
      "site": "00536e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00537158",
      "incomplete_value": true,
      "site": "0053715c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00536e38",
      "incomplete_value": true,
      "site": "00536e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00537154",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00537154",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00537158",
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
      "00537154",
      "READ",
      [
        "storage",
        "00c9be88",
        null,
        "pointer"
      ]
    ],
    [
      "00537154",
      "PARAM",
      [
        "storage",
        "00c97738",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00537158",
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

- 旧版 [`00536e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536e3c) · [`00536d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536d90) · [`00536dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md#insn-00536dbc)
- 新版 [`0053715c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md#insn-0053715c) · [`005370b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md#insn-005370b0) · [`005370dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md#insn-005370dc)

~~~diff
- 00536e3c ["INT_ADD", "register:40f0:8", ["const:536e3c:8", "const:4:8"]]
- 00536e3c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0053715c ["INT_ADD", "register:40f0:8", ["const:53715c:8", "const:4:8"]]
+ 0053715c ["CALL", null, ["callee:00c58fb0:8"]]
- 00536e3c bytes 69841c94
+ 0053715c bytes 95871c94
- 00536d90 ["INT_ADD", "register:40f0:8", ["const:536d90:8", "const:4:8"]]
- 00536d90 ["CALL", null, ["callee:00c59ad0:8"]]
+ 005370b0 ["INT_ADD", "register:40f0:8", ["const:5370b0:8", "const:4:8"]]
+ 005370b0 ["CALL", null, ["callee:00c59ad0:8"]]
- 00536d90 bytes 5c871c94
+ 005370b0 bytes 888a1c94
- 00536dbc ["INT_ADD", "register:40f0:8", ["const:536dbc:8", "const:4:8"]]
- 00536dbc ["CALL", null, ["callee:00c58fe0:8"]]
+ 005370dc ["INT_ADD", "register:40f0:8", ["const:5370dc:8", "const:4:8"]]
+ 005370dc ["CALL", null, ["callee:00c58fe0:8"]]
- 00536dbc bytes 95841c94
+ 005370dc bytes c1871c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8141aac8cb6d507059882b51bbf6c12"></a>

### [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) → [`005371e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md) FUN_005371e8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 12件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00537064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md) [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md) [`00540728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005371f4",
      "incomplete_value": false,
      "site": "005371f8",
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
      "definition_site": "00536ed4",
      "incomplete_value": false,
      "site": "00536ed8",
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
      "005371f4",
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
      "005371f4",
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

- 旧版 [`00536ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md#insn-00536ed8) · [`00536ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md#insn-00536ed0) · [`00536ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md#insn-00536ed4)
- 新版 [`005371f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md#insn-005371f8) · [`005371f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md#insn-005371f0) · [`005371f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371e8.md#insn-005371f4)

~~~diff
- 00536ed8 ["INT_ADD", "register:40f0:8", ["const:536ed8:8", "const:4:8"]]
- 00536ed8 ["CALL", null, ["callee:0043bad8:8"]]
+ 005371f8 ["INT_ADD", "register:40f0:8", ["const:5371f8:8", "const:4:8"]]
+ 005371f8 ["CALL", null, ["callee:0043bad8:8"]]
- 00536ed8 bytes 3812fc97
+ 005371f8 bytes 3812fc97
- 00536ed0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005371f0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00536ed0 bytes 00ecffb0
+ 005371f0 bytes 00ecffb0
- 00536ed4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00536ed4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00536ed4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00536ed4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005371f4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005371f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005371f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005371f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00536ed4 bytes 00303e91
+ 005371f4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-278dfbd4153219efa5abe570b5480044"></a>

### [`00536edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md) → [`005371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md) FUN_005371fc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005370c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md) [`00537598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537598.md) · 呼出先 9件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`005373e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005373e4.md) [`005378b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005378b8.md) · 呼出先 9件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "definition_site": "00537284",
      "incomplete_value": false,
      "site": "0053728c",
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
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536f64",
      "incomplete_value": false,
      "site": "00536f6c",
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
            "const:725:8"
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
      "definition_site": "005372bc",
      "incomplete_value": true,
      "site": "005372c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536f9c",
      "incomplete_value": true,
      "site": "00536fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "definition_site": "005372b8",
      "incomplete_value": false,
      "site": "005372c8",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00536f98",
      "incomplete_value": false,
      "site": "00536fa8",
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
      "00537284",
      "PARAM",
      [
        "storage",
        "002a6725",
        null,
        "string"
      ]
    ],
    [
      "005372b8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "005372bc",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00537284",
      "PARAM",
      [
        "storage",
        "002a687d",
        null,
        "string"
      ]
    ],
    [
      "005372b8",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "005372bc",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536f6c) · [`00536fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536fa8) · [`00536f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md#insn-00536f14)
- 新版 [`0053728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md#insn-0053728c) · [`005372c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md#insn-005372c8) · [`00537234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md#insn-00537234)

~~~diff
- 00536f6c ["INT_ADD", "register:40f0:8", ["const:536f6c:8", "const:4:8"]]
- 00536f6c ["CALL", null, ["callee:0043e138:8"]]
+ 0053728c ["INT_ADD", "register:40f0:8", ["const:53728c:8", "const:4:8"]]
+ 0053728c ["CALL", null, ["callee:0043e138:8"]]
- 00536f6c bytes ab1bfc97
+ 0053728c bytes ab1bfc97
- 00536fa8 ["INT_ADD", "register:40f0:8", ["const:536fa8:8", "const:4:8"]]
- 00536fa8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005372c8 ["INT_ADD", "register:40f0:8", ["const:5372c8:8", "const:4:8"]]
+ 005372c8 ["CALL", null, ["callee:00c58fb0:8"]]
- 00536fa8 bytes 0e841c94
+ 005372c8 bytes 3a871c94
- 00536f14 ["INT_ADD", "register:40f0:8", ["const:536f14:8", "const:4:8"]]
- 00536f14 ["CALL", null, ["callee:00c59bc0:8"]]
+ 00537234 ["INT_ADD", "register:40f0:8", ["const:537234:8", "const:4:8"]]
+ 00537234 ["CALL", null, ["callee:00c59bc0:8"]]
- 00536f14 bytes 37871c94
+ 00537234 bytes 638a1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9550a62f9d0489c3d2c540ab7ae3fdb"></a>

### [`00536ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ff8.md) → [`00537318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537318.md) FUN_00537318

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00537338",
      "incomplete_value": true,
      "site": "00537338",
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
      "definition_site": "00537018",
      "incomplete_value": true,
      "site": "00537018",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00537358",
      "incomplete_value": false,
      "site": "00537358",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537038",
      "incomplete_value": false,
      "site": "00537038",
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
            "const:fe8:8"
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
      "0053732c",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "00537338",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00537358",
      "DATA",
      [
        "storage",
        "00c66fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053732c",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "00537338",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00537358",
      "DATA",
      [
        "storage",
        "00c67fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ff8.md#insn-00537004) · [`0053700c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ff8.md#insn-0053700c) · [`00537028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ff8.md#insn-00537028)
- 新版 [`00537324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537318.md#insn-00537324) · [`0053732c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537318.md#insn-0053732c) · [`00537348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537318.md#insn-00537348)

~~~diff
- 00537004 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00537324 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00537004 bytes 283b0090
+ 00537324 bytes 283b00b0
- 0053700c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 0053700c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053732c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 0053732c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053700c bytes 084140f9
+ 0053732c bytes 082940f9
- 00537028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00537028 ["INT_ADD", "register:40f0:8", ["const:537028:8", "const:4:8"]]
- 00537028 ["CALLIND", null, ["register:0:8"]]
+ 00537348 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00537348 ["INT_ADD", "register:40f0:8", ["const:537348:8", "const:4:8"]]
+ 00537348 ["CALLIND", null, ["register:0:8"]]
- 00537028 bytes 00013fd6
+ 00537348 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0dad30ed8a02e00de70523a9e70f61"></a>

### [`00537060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537060.md) → [`00537380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537380.md) FUN_00537380

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005373a0",
      "incomplete_value": true,
      "site": "005373a0",
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
      "definition_site": "00537080",
      "incomplete_value": true,
      "site": "00537080",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005373c0",
      "incomplete_value": false,
      "site": "005373c0",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005370a0",
      "incomplete_value": false,
      "site": "005370a0",
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
            "const:fe8:8"
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
      "00537394",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "005373a0",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005373c0",
      "DATA",
      [
        "storage",
        "00c66fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537394",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "005373a0",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005373c0",
      "DATA",
      [
        "storage",
        "00c67fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053706c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537060.md#insn-0053706c) · [`00537074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537060.md#insn-00537074) · [`00537090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537060.md#insn-00537090)
- 新版 [`0053738c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537380.md#insn-0053738c) · [`00537394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537380.md#insn-00537394) · [`005373b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537380.md#insn-005373b0)

~~~diff
- 0053706c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0053738c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0053706c bytes 283b0090
+ 0053738c bytes 283b00b0
- 00537074 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 00537074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 00537394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537074 bytes 084140f9
+ 00537394 bytes 082940f9
- 00537090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00537090 ["INT_ADD", "register:40f0:8", ["const:537090:8", "const:4:8"]]
- 00537090 ["CALLIND", null, ["register:0:8"]]
+ 005373b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005373b0 ["INT_ADD", "register:40f0:8", ["const:5373b0:8", "const:4:8"]]
+ 005373b0 ["CALLIND", null, ["register:0:8"]]
- 00537090 bytes 00013fd6
+ 005373b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fde931dd59ed013c82658f9d5865486"></a>

### [`005370c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md) → [`005373e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005373e4.md) FUN_005373e4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00536edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536edc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`005371fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005371fc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c599c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c599c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.65% / 新版 94.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053745c",
      "incomplete_value": true,
      "site": "0053745c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "0053713c",
      "incomplete_value": true,
      "site": "0053713c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00537540",
      "incomplete_value": true,
      "site": "00537540",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "00537220",
      "incomplete_value": true,
      "site": "00537220",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "0053762c",
      "incomplete_value": true,
      "site": "0053762c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "definition_site": "0053730c",
      "incomplete_value": true,
      "site": "0053730c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
      "0053744c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00537530",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053761c",
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
      "0053744c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00537530",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "0053761c",
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

- 旧版 [`0053713c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md#insn-0053713c) · [`00537220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md#insn-00537220) · [`0053730c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/005370c4.md#insn-0053730c)
- 新版 [`0053745c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005373e4.md#insn-0053745c) · [`00537540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005373e4.md#insn-00537540) · [`0053762c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005373e4.md#insn-0053762c)

~~~diff
- 0053713c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053713c ["INT_ADD", "register:40f0:8", ["const:53713c:8", "const:4:8"]]
- 0053713c ["CALLIND", null, ["register:0:8"]]
+ 0053745c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053745c ["INT_ADD", "register:40f0:8", ["const:53745c:8", "const:4:8"]]
+ 0053745c ["CALLIND", null, ["register:0:8"]]
- 0053713c bytes 20013fd6
+ 0053745c bytes 20013fd6
- 00537220 ["COPY", "register:0:8", ["register:4048:8"]]
- 00537220 ["INT_ADD", "register:40f0:8", ["const:537220:8", "const:4:8"]]
- 00537220 ["CALLIND", null, ["register:0:8"]]
+ 00537540 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00537540 ["INT_ADD", "register:40f0:8", ["const:537540:8", "const:4:8"]]
+ 00537540 ["CALLIND", null, ["register:0:8"]]
- 00537220 bytes 20013fd6
+ 00537540 bytes 20013fd6
- 0053730c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053730c ["INT_ADD", "register:40f0:8", ["const:53730c:8", "const:4:8"]]
- 0053730c ["CALLIND", null, ["register:0:8"]]
+ 0053762c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053762c ["INT_ADD", "register:40f0:8", ["const:53762c:8", "const:4:8"]]
+ 0053762c ["CALLIND", null, ["register:0:8"]]
- 0053730c bytes 20013fd6
+ 0053762c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23beaffa5af95eb89dabee474cb0d3f1"></a>

### [`0053741c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/0053741c.md) → [`0053773c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053773c.md) FUN_0053773c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
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
      "definition_site": "0053743c",
      "incomplete_value": true,
      "site": "0053743c",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00537778",
      "incomplete_value": false,
      "site": "0053777c",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537458",
      "incomplete_value": false,
      "site": "0053745c",
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
            "const:f88:8"
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
      "00537750",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053777c",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00537750",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "0053777c",
      "DATA",
      [
        "storage",
        "00c67f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/0053741c.md#insn-00537428) · [`00537430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/0053741c.md#insn-00537430) · [`0053744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/0053741c.md#insn-0053744c)
- 新版 [`00537748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053773c.md#insn-00537748) · [`00537750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053773c.md#insn-00537750) · [`0053776c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/0053773c.md#insn-0053776c)

~~~diff
- 00537428 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00537748 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00537428 bytes 283b0090
+ 00537748 bytes 283b00b0
- 00537430 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 00537430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537750 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 00537750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537430 bytes 084140f9
+ 00537750 bytes 082940f9
- 0053744c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053744c ["INT_ADD", "register:40f0:8", ["const:53744c:8", "const:4:8"]]
- 0053744c ["CALLIND", null, ["register:0:8"]]
+ 0053776c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0053776c ["INT_ADD", "register:40f0:8", ["const:53776c:8", "const:4:8"]]
+ 0053776c ["CALLIND", null, ["register:0:8"]]
- 0053744c bytes 00013fd6
+ 0053776c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3897e9b755b525d4ce676c2354078ec8"></a>

### [`00537498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537498.md) → [`005377b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005377b8.md) FUN_005377b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005377d8",
      "incomplete_value": true,
      "site": "005377d8",
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
      "definition_site": "005374b8",
      "incomplete_value": true,
      "site": "005374b8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005377f4",
      "incomplete_value": false,
      "site": "005377f8",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005374d4",
      "incomplete_value": false,
      "site": "005374d8",
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
            "const:f88:8"
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
      "005377cc",
      "READ",
      [
        "storage",
        "00c9b080",
        null,
        "pointer"
      ]
    ],
    [
      "005377d8",
      "DATA",
      [
        "storage",
        "00c66e28",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005377f8",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005377cc",
      "READ",
      [
        "storage",
        "00c9c050",
        null,
        "pointer"
      ]
    ],
    [
      "005377d8",
      "DATA",
      [
        "storage",
        "00c67df8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "005377f8",
      "DATA",
      [
        "storage",
        "00c67f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005374a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537498.md#insn-005374a4) · [`005374ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537498.md#insn-005374ac) · [`005374c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00537/00537498.md#insn-005374c8)
- 新版 [`005377c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005377b8.md#insn-005377c4) · [`005377cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005377b8.md#insn-005377cc) · [`005377e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/005377b8.md#insn-005377e8)

~~~diff
- 005374a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005377c4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005374a4 bytes 283b0090
+ 005377c4 bytes 283b00b0
- 005374ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:80:8"]]
- 005374ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005377cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:50:8"]]
+ 005377cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005374ac bytes 084140f9
+ 005377cc bytes 082940f9
- 005374c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005374c8 ["INT_ADD", "register:40f0:8", ["const:5374c8:8", "const:4:8"]]
- 005374c8 ["CALLIND", null, ["register:0:8"]]
+ 005377e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005377e8 ["INT_ADD", "register:40f0:8", ["const:5377e8:8", "const:4:8"]]
+ 005377e8 ["CALLIND", null, ["register:0:8"]]
- 005374c8 bytes 00013fd6
+ 005377e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

