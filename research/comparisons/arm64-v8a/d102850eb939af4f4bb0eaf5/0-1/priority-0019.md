# v16.0.1 → v16.0.2 · 最優先の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-af6ce1029ff7dfe85b0705f930a414b5"></a>

### [`0058e378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md) → [`0058e3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md) FUN_0058e3b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.10% / 新版 90.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e434",
      "incomplete_value": true,
      "site": "0058e43c",
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
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e3f4",
      "incomplete_value": true,
      "site": "0058e3fc",
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
                "const:3a0:8"
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
      "definition_site": "0058e430",
      "incomplete_value": true,
      "site": "0058e440",
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
                "const:5ee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e3f0",
      "incomplete_value": true,
      "site": "0058e400",
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
                "const:64a:8"
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
      "definition_site": "0058e430",
      "incomplete_value": true,
      "site": "0058e440",
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
      "definition_site": "0058e3f0",
      "incomplete_value": true,
      "site": "0058e400",
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
      "0058e430",
      "READ",
      [
        "storage",
        "002ab64a",
        null,
        "string"
      ]
    ],
    [
      "0058e430",
      "READ",
      [
        "storage",
        "002ab65a",
        null,
        "string"
      ]
    ],
    [
      "0058e434",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e430",
      "READ",
      [
        "storage",
        "002ab5ee",
        null,
        "string"
      ]
    ],
    [
      "0058e430",
      "READ",
      [
        "storage",
        "002ab5fe",
        null,
        "string"
      ]
    ],
    [
      "0058e434",
      "READ",
      [
        "storage",
        "002c23e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e43c) · [`0058e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e454) · [`0058e3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e378.md#insn-0058e3ac)
- 新版 [`0058e47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e47c) · [`0058e494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e494) · [`0058e3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e3b8.md#insn-0058e3ec)

~~~diff
- 0058e43c ["INT_ADD", "register:40f0:8", ["const:58e43c:8", "const:4:8"]]
- 0058e43c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058e47c ["INT_ADD", "register:40f0:8", ["const:58e47c:8", "const:4:8"]]
+ 0058e47c ["CALL", null, ["callee:00c57f80:8"]]
- 0058e43c bytes 9d261b94
+ 0058e47c bytes c1261b94
- 0058e454 ["INT_ADD", "register:40f0:8", ["const:58e454:8", "const:4:8"]]
- 0058e454 ["CALL", null, ["callee:00589184:8"]]
+ 0058e494 ["INT_ADD", "register:40f0:8", ["const:58e494:8", "const:4:8"]]
+ 0058e494 ["CALL", null, ["callee:00589184:8"]]
- 0058e454 bytes 3cebff97
+ 0058e494 bytes 3cebff97
- 0058e3ac ["INT_ADD", "register:40f0:8", ["const:58e3ac:8", "const:4:8"]]
- 0058e3ac ["CALL", null, ["callee:00589880:8"]]
+ 0058e3ec ["INT_ADD", "register:40f0:8", ["const:58e3ec:8", "const:4:8"]]
+ 0058e3ec ["CALL", null, ["callee:00589880:8"]]
- 0058e3ac bytes 25edff97
+ 0058e3ec bytes 25edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc12a61dfb41357f58a2ff9e70d3566"></a>

### [`0058e748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md) → [`0058e788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md) FUN_0058e788

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e804",
      "incomplete_value": true,
      "site": "0058e80c",
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
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e7c4",
      "incomplete_value": true,
      "site": "0058e7cc",
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
                "const:3a0:8"
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
      "definition_site": "0058e800",
      "incomplete_value": true,
      "site": "0058e810",
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
                "const:fd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e7c0",
      "incomplete_value": true,
      "site": "0058e7d0",
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
                "const:fa2:8"
              ]
            ]
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
      "definition_site": "0058e800",
      "incomplete_value": true,
      "site": "0058e810",
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
      "definition_site": "0058e7c0",
      "incomplete_value": true,
      "site": "0058e7d0",
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
      "0058e800",
      "READ",
      [
        "storage",
        "002b4fa2",
        null,
        "string"
      ]
    ],
    [
      "0058e800",
      "READ",
      [
        "storage",
        "002b4fb2",
        null,
        "string"
      ]
    ],
    [
      "0058e804",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e800",
      "READ",
      [
        "storage",
        "002b4fd3",
        null,
        "string"
      ]
    ],
    [
      "0058e800",
      "READ",
      [
        "storage",
        "002b4fe3",
        null,
        "string"
      ]
    ],
    [
      "0058e804",
      "READ",
      [
        "storage",
        "002c23e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e80c) · [`0058e77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e77c) · [`0058e784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e748.md#insn-0058e784)
- 新版 [`0058e84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e84c) · [`0058e7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e7bc) · [`0058e7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e788.md#insn-0058e7c4)

~~~diff
- 0058e80c ["INT_ADD", "register:40f0:8", ["const:58e80c:8", "const:4:8"]]
- 0058e80c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058e84c ["INT_ADD", "register:40f0:8", ["const:58e84c:8", "const:4:8"]]
+ 0058e84c ["CALL", null, ["callee:00c57f80:8"]]
- 0058e80c bytes a9251b94
+ 0058e84c bytes cd251b94
- 0058e77c ["INT_ADD", "register:40f0:8", ["const:58e77c:8", "const:4:8"]]
- 0058e77c ["CALL", null, ["callee:00589880:8"]]
+ 0058e7bc ["INT_ADD", "register:40f0:8", ["const:58e7bc:8", "const:4:8"]]
+ 0058e7bc ["CALL", null, ["callee:00589880:8"]]
- 0058e77c bytes 31ecff97
+ 0058e7bc bytes 31ecff97
- 0058e784 ["INT_ADD", "register:40f0:8", ["const:58e784:8", "const:4:8"]]
- 0058e784 ["CALL", null, ["callee:00588eac:8"]]
+ 0058e7c4 ["INT_ADD", "register:40f0:8", ["const:58e7c4:8", "const:4:8"]]
+ 0058e7c4 ["CALL", null, ["callee:00588eac:8"]]
- 0058e784 bytes bae9ff97
+ 0058e7c4 bytes bae9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f73ea694967443974a8c37f62600948b"></a>

### [`0058e92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md) → [`0058e96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md) FUN_0058e96c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.07% / 新版 88.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e9c8",
      "incomplete_value": true,
      "site": "0058e9c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:317:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e988",
      "incomplete_value": true,
      "site": "0058e988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d7:8"
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
      "definition_site": "0058e9e8",
      "incomplete_value": true,
      "site": "0058e9f0",
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e9a8",
      "incomplete_value": true,
      "site": "0058e9b0",
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
                "const:e20:8"
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
      "definition_site": "0058e9e4",
      "incomplete_value": true,
      "site": "0058e9f4",
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
      "definition_site": "0058e9a4",
      "incomplete_value": true,
      "site": "0058e9b4",
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
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e9b8",
      "READ",
      [
        "storage",
        "002c12d7",
        null,
        "string"
      ]
    ],
    [
      "0058e9e4",
      "READ",
      [
        "storage",
        "002a4444",
        null,
        "string"
      ]
    ],
    [
      "0058e9e4",
      "READ",
      [
        "storage",
        "002a4454",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e9b8",
      "READ",
      [
        "storage",
        "002c1317",
        null,
        "string"
      ]
    ],
    [
      "0058e9e4",
      "READ",
      [
        "storage",
        "002a43f7",
        null,
        "string"
      ]
    ],
    [
      "0058e9e4",
      "READ",
      [
        "storage",
        "002a4407",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058e970) · [`0058e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058e9f0) · [`0058ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e92c.md#insn-0058ea00)
- 新版 [`0058e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058e9b0) · [`0058ea30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058ea30) · [`0058ea40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e96c.md#insn-0058ea40)

~~~diff
- 0058e970 ["COPY", "tmp:0:8", ["const:2d7:8"]]
- 0058e970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e9b0 ["COPY", "tmp:0:8", ["const:317:8"]]
+ 0058e9b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e9b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e9b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e970 bytes 295d0b91
+ 0058e9b0 bytes 295d0c91
- 0058e9f0 ["INT_ADD", "register:40f0:8", ["const:58e9f0:8", "const:4:8"]]
- 0058e9f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058ea30 ["INT_ADD", "register:40f0:8", ["const:58ea30:8", "const:4:8"]]
+ 0058ea30 ["CALL", null, ["callee:00c57f80:8"]]
- 0058e9f0 bytes 30251b94
+ 0058ea30 bytes 54251b94
- 0058ea00 ["INT_ADD", "register:40f0:8", ["const:58ea00:8", "const:4:8"]]
- 0058ea00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058ea40 ["INT_ADD", "register:40f0:8", ["const:58ea40:8", "const:4:8"]]
+ 0058ea40 ["CALL", null, ["callee:00c57f80:8"]]
- 0058ea00 bytes 2c251b94
+ 0058ea40 bytes 50251b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-effa5228de690f716aeadb89a0a126de"></a>

### [`0058ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md) → [`0058ed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md) FUN_0058ed00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) · 呼出先 2件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) · 呼出先 2件 [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0058ed28",
      "incomplete_value": false,
      "site": "0058ed34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ece8",
      "incomplete_value": false,
      "site": "0058ecf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "0058ed34",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ed34",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ecdc) · [`0058ece4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ece4) · [`0058ece8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md#insn-0058ece8)
- 新版 [`0058ed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed1c) · [`0058ed24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed24) · [`0058ed28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md#insn-0058ed28)

~~~diff
- 0058ecdc ["INT_ADD", "register:40f0:8", ["const:58ecdc:8", "const:4:8"]]
- 0058ecdc ["CALL", null, ["callee:00c57f60:8"]]
+ 0058ed1c ["INT_ADD", "register:40f0:8", ["const:58ed1c:8", "const:4:8"]]
+ 0058ed1c ["CALL", null, ["callee:00c57f60:8"]]
- 0058ecdc bytes 6d241b94
+ 0058ed1c bytes 91241b94
- 0058ece4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058ed24 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058ece4 bytes e83600d0
+ 0058ed24 bytes e83600f0
- 0058ece8 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 0058ece8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ece8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ece8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ed28 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0058ed28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ed28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ed28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ece8 bytes 08013f91
+ 0058ed28 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e36b17b1497b2e6122005efc67887651"></a>

### [`0058eea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md) → [`0058eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md) FUN_0058eee0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec4.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f04.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058ef4c",
      "incomplete_value": true,
      "site": "0058ef5c",
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
                "const:f65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ef0c",
      "incomplete_value": true,
      "site": "0058ef1c",
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
                "const:fb2:8"
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
      "0058ef28",
      "READ",
      [
        "storage",
        "002b74cb",
        null,
        "string"
      ]
    ],
    [
      "0058ef4c",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058ef28",
      "READ",
      [
        "storage",
        "002b750b",
        null,
        "string"
      ]
    ],
    [
      "0058ef4c",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058eec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eec4) · [`0058eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eecc) · [`0058eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058eea0.md#insn-0058eee4)
- 新版 [`0058ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef04) · [`0058ef0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef0c) · [`0058ef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058eee0.md#insn-0058ef24)

~~~diff
- 0058eec4 ["INT_ADD", "register:40f0:8", ["const:58eec4:8", "const:4:8"]]
- 0058eec4 ["CALL", null, ["callee:00588eac:8"]]
+ 0058ef04 ["INT_ADD", "register:40f0:8", ["const:58ef04:8", "const:4:8"]]
+ 0058ef04 ["CALL", null, ["callee:00588eac:8"]]
- 0058eec4 bytes eae7ff97
+ 0058ef04 bytes eae7ff97
- 0058eecc ["INT_ADD", "register:40f0:8", ["const:58eecc:8", "const:4:8"]]
- 0058eecc ["CALL", null, ["callee:0058919c:8"]]
+ 0058ef0c ["INT_ADD", "register:40f0:8", ["const:58ef0c:8", "const:4:8"]]
+ 0058ef0c ["CALL", null, ["callee:0058919c:8"]]
- 0058eecc bytes a4e8ff97
+ 0058ef0c bytes a4e8ff97
- 0058eee4 ["COPY", "tmp:0:8", ["const:4cb:8"]]
- 0058eee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058eee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058eee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ef24 ["COPY", "tmp:0:8", ["const:50b:8"]]
+ 0058ef24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ef24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ef24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058eee4 bytes 082d1391
+ 0058ef24 bytes 082d1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e181107e74d97d33d0dbe66d711386"></a>

### [`0058f04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md) → [`0058f08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md) FUN_0058f08c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f100",
      "incomplete_value": true,
      "site": "0058f10c",
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
                "const:9c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f0c0",
      "incomplete_value": true,
      "site": "0058f0cc",
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
                "const:980:8"
              ]
            ]
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
      "0058f0fc",
      "READ",
      [
        "storage",
        "002a215e",
        null,
        "string"
      ]
    ],
    [
      "0058f0fc",
      "READ",
      [
        "storage",
        "002a216e",
        null,
        "string"
      ]
    ],
    [
      "0058f100",
      "READ",
      [
        "storage",
        "002c2980",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058f0fc",
      "READ",
      [
        "storage",
        "002a2111",
        null,
        "string"
      ]
    ],
    [
      "0058f0fc",
      "READ",
      [
        "storage",
        "002a2121",
        null,
        "string"
      ]
    ],
    [
      "0058f100",
      "READ",
      [
        "storage",
        "002c29c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f078) · [`0058f080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f080) · [`0058f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f04c.md#insn-0058f0ac)
- 新版 [`0058f0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0b8) · [`0058f0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0c0) · [`0058f0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f08c.md#insn-0058f0ec)

~~~diff
- 0058f078 ["INT_ADD", "register:40f0:8", ["const:58f078:8", "const:4:8"]]
- 0058f078 ["CALL", null, ["callee:00588eac:8"]]
+ 0058f0b8 ["INT_ADD", "register:40f0:8", ["const:58f0b8:8", "const:4:8"]]
+ 0058f0b8 ["CALL", null, ["callee:00588eac:8"]]
- 0058f078 bytes 7de7ff97
+ 0058f0b8 bytes 7de7ff97
- 0058f080 ["INT_ADD", "register:40f0:8", ["const:58f080:8", "const:4:8"]]
- 0058f080 ["CALL", null, ["callee:0058919c:8"]]
+ 0058f0c0 ["INT_ADD", "register:40f0:8", ["const:58f0c0:8", "const:4:8"]]
+ 0058f0c0 ["CALL", null, ["callee:0058919c:8"]]
- 0058f080 bytes 37e8ff97
+ 0058f0c0 bytes 37e8ff97
- 0058f0ac ["INT_ADD", "register:40f0:8", ["const:58f0ac:8", "const:4:8"]]
- 0058f0ac ["CALL", null, ["callee:00c57f60:8"]]
+ 0058f0ec ["INT_ADD", "register:40f0:8", ["const:58f0ec:8", "const:4:8"]]
+ 0058f0ec ["CALL", null, ["callee:00c57f60:8"]]
- 0058f0ac bytes 79231b94
+ 0058f0ec bytes 9d231b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-542f30bea5967f10c1f121017a012b74"></a>

### [`0058f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f638.md) → [`0058f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md) FUN_0058f678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0058f67c",
      "incomplete_value": false,
      "site": "0058f680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f63c",
      "incomplete_value": false,
      "site": "0058f640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "0058f680",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f680",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f638.md#insn-0058f638) · [`0058f63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f638.md#insn-0058f63c)
- 新版 [`0058f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md#insn-0058f678) · [`0058f67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md#insn-0058f67c)

~~~diff
- 0058f638 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058f678 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058f638 bytes e83600b0
+ 0058f678 bytes e83600d0
- 0058f63c ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 0058f63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f67c ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0058f67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f63c bytes 08013f91
+ 0058f67c bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00f284cad589431362a49b0e7eb98e78"></a>

### [`0058f648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md) → [`0058f688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md) FUN_0058f688

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0058f698",
      "incomplete_value": false,
      "site": "0058f6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f658",
      "incomplete_value": false,
      "site": "0058f660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "0058f6a0",
      "DATA",
      [
        "storage",
        "00c6cfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f6a0",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md#insn-0058f654) · [`0058f658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md#insn-0058f658) · [`0058f664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f648.md#insn-0058f664)
- 新版 [`0058f694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f694) · [`0058f698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f698) · [`0058f6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f6a4)

~~~diff
- 0058f654 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058f694 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058f654 bytes e83600b0
+ 0058f694 bytes e83600d0
- 0058f658 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 0058f658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f698 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0058f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f658 bytes 08013f91
+ 0058f698 bytes 08410291
- 0058f664 ["INT_ADD", "register:40f0:8", ["const:58f664:8", "const:4:8"]]
- 0058f664 ["CALL", null, ["callee:00c57f70:8"]]
+ 0058f6a4 ["INT_ADD", "register:40f0:8", ["const:58f6a4:8", "const:4:8"]]
+ 0058f6a4 ["CALL", null, ["callee:00c57f70:8"]]
- 0058f664 bytes 0f221b94
+ 0058f6a4 bytes 33221b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-170a57ee51a7e8a2aeafd21ba8d8669e"></a>

### [`0058f678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md) → [`0058f6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md) FUN_0058f6b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)

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
      "definition_site": "0058f6c8",
      "incomplete_value": false,
      "site": "0058f6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f688",
      "incomplete_value": false,
      "site": "0058f690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058f6d0",
      "DATA",
      [
        "storage",
        "00c6cf38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f6d0",
      "DATA",
      [
        "storage",
        "00c6d008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md#insn-0058f684) · [`0058f688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md#insn-0058f688) · [`0058f698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f678.md#insn-0058f698)
- 新版 [`0058f6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md#insn-0058f6c4) · [`0058f6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md#insn-0058f6c8) · [`0058f6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md#insn-0058f6d8)

~~~diff
- 0058f684 ["COPY", "register:4040:8", ["const:c6c000:8"]]
+ 0058f6c4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
- 0058f684 bytes e83600b0
+ 0058f6c4 bytes e83600d0
- 0058f688 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0058f688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f6c8 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 0058f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f688 bytes 08e13c91
+ 0058f6c8 bytes 08210091
- 0058f698 ["INT_ADD", "register:40f0:8", ["const:58f698:8", "const:4:8"]]
- 0058f698 ["CALL", null, ["callee:0058a8fc:8"]]
+ 0058f6d8 ["INT_ADD", "register:40f0:8", ["const:58f6d8:8", "const:4:8"]]
+ 0058f6d8 ["CALL", null, ["callee:0058a8fc:8"]]
- 0058f698 bytes 89ecff97
+ 0058f6d8 bytes 89ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58dbe042014e16189f1a61f9fdc0ff9c"></a>

### [`0058f6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md) → [`0058f6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md) _INIT_34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0057a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a958.md) [`0058cc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cc80.md) [`00bfa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057a998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a998.md) [`0058ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccc0.md) [`00bfa1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f71c",
      "incomplete_value": false,
      "site": "0058f71c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:498:8"
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
      "definition_site": "0058f6dc",
      "incomplete_value": false,
      "site": "0058f6dc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:398:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f720",
      "incomplete_value": false,
      "site": "0058f720",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:498:8"
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
      "definition_site": "0058f6e0",
      "incomplete_value": false,
      "site": "0058f6e0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:398:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f724",
      "incomplete_value": false,
      "site": "0058f724",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f6e4",
      "incomplete_value": false,
      "site": "0058f6e4",
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
            "const:398:8"
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
      "0058f700",
      "PARAM",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f714",
      "PARAM",
      [
        "storage",
        "0057a958",
        null,
        null
      ]
    ],
    [
      "0058f718",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058f700",
      "PARAM",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f714",
      "PARAM",
      [
        "storage",
        "0057a998",
        null,
        null
      ]
    ],
    [
      "0058f718",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f6c0) · [`0058f6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f6e8) · [`0058f700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f6b0.md#insn-0058f700)
- 新版 [`0058f700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f700) · [`0058f728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f728) · [`0058f740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f740)

~~~diff
- 0058f6c0 ["COPY", "tmp:0:8", ["const:398:8"]]
- 0058f6c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058f6c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058f6c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058f700 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0058f700 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058f700 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058f700 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058f6c0 bytes 21600e91
+ 0058f700 bytes 21601291
- 0058f6e8 ["INT_ADD", "register:40f0:8", ["const:58f6e8:8", "const:4:8"]]
- 0058f6e8 ["CALL", null, ["callee:00c57f00:8"]]
+ 0058f728 ["INT_ADD", "register:40f0:8", ["const:58f728:8", "const:4:8"]]
+ 0058f728 ["CALL", null, ["callee:00c57f00:8"]]
- 0058f6e8 bytes d2211b94
+ 0058f728 bytes f6211b94
- 0058f700 ["INT_ADD", "register:40f0:8", ["const:58f700:8", "const:4:8"]]
- 0058f700 ["CALL", null, ["callee:00c57f00:8"]]
+ 0058f740 ["INT_ADD", "register:40f0:8", ["const:58f740:8", "const:4:8"]]
+ 0058f740 ["CALL", null, ["callee:00c57f00:8"]]
- 0058f700 bytes cc211b94
+ 0058f740 bytes f0211b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c0ef2f44c9b73eff9686dd4e6281d7"></a>

### [`0058f788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md) → [`0058f7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md) FUN_0058f7c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f820",
      "incomplete_value": false,
      "site": "0058f820",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:574:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f7e0",
      "incomplete_value": false,
      "site": "0058f7e0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:474:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058f828",
      "incomplete_value": false,
      "site": "0058f828",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:574:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f7e8",
      "incomplete_value": false,
      "site": "0058f7e8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:474:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058f8d8",
      "incomplete_value": true,
      "site": "0058f8d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f898",
      "incomplete_value": true,
      "site": "0058f898",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:80:8"
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
      "0058f814",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f820",
      "WRITE",
      [
        "storage",
        "00ca6480",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f828",
      "WRITE",
      [
        "storage",
        "00ca6478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f814",
      "READ",
      [
        "storage",
        "00ca6610",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f820",
      "WRITE",
      [
        "storage",
        "00ca6580",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f828",
      "WRITE",
      [
        "storage",
        "00ca6578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f898) · [`0058f8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f8b0) · [`0058f7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md#insn-0058f7cc)
- 新版 [`0058f8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f8d8) · [`0058f8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f8f0) · [`0058f80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f80c)

~~~diff
- 0058f898 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f898 ["INT_ADD", "register:40f0:8", ["const:58f898:8", "const:4:8"]]
- 0058f898 ["CALLIND", null, ["register:0:8"]]
+ 0058f8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f8d8 ["INT_ADD", "register:40f0:8", ["const:58f8d8:8", "const:4:8"]]
+ 0058f8d8 ["CALLIND", null, ["register:0:8"]]
- 0058f898 bytes 00013fd6
+ 0058f8d8 bytes 00013fd6
- 0058f8b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f8b0 ["INT_ADD", "register:40f0:8", ["const:58f8b0:8", "const:4:8"]]
- 0058f8b0 ["CALLIND", null, ["register:0:8"]]
+ 0058f8f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f8f0 ["INT_ADD", "register:40f0:8", ["const:58f8f0:8", "const:4:8"]]
+ 0058f8f0 ["CALLIND", null, ["register:0:8"]]
- 0058f8b0 bytes 00013fd6
+ 0058f8f0 bytes 00013fd6
- 0058f7cc ["COPY", "tmp:0:8", ["const:474:8"]]
- 0058f7cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f7cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f7cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f80c ["COPY", "tmp:0:8", ["const:574:8"]]
+ 0058f80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f7cc bytes 08d11191
+ 0058f80c bytes 08d11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7b308d5afd3d85ace58d4ede4381d7"></a>

### [`0058f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md) → [`0058f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md) FUN_0058f940

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa1c",
      "incomplete_value": false,
      "site": "0058fa1c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "0058f9dc",
      "incomplete_value": false,
      "site": "0058f9dc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa24",
      "incomplete_value": false,
      "site": "0058fa24",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
              ]
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
      "definition_site": "0058f9e4",
      "incomplete_value": false,
      "site": "0058f9e4",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa24",
      "incomplete_value": false,
      "site": "0058fa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058f9e4",
      "incomplete_value": false,
      "site": "0058f9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058f960",
      "READ",
      [
        "storage",
        "00ca6430",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f988",
      "READ",
      [
        "storage",
        "00ca6438",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f98c",
      "WRITE",
      [
        "storage",
        "00ca6430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058f960",
      "READ",
      [
        "storage",
        "00ca6530",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f988",
      "READ",
      [
        "storage",
        "00ca6538",
        null,
        "undefined8"
      ]
    ],
    [
      "0058f98c",
      "WRITE",
      [
        "storage",
        "00ca6530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f99c) · [`0058f9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f9a8) · [`0058f9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md#insn-0058f9c8)
- 新版 [`0058f9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058f9dc) · [`0058f9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058f9e8) · [`0058fa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058fa08)

~~~diff
- 0058f99c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
- 0058f99c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058f9dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
+ 0058f9dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0058f99c bytes 808a42f9
+ 0058f9dc bytes 800a43f9
- 0058f9a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f9a8 ["INT_ADD", "register:40f0:8", ["const:58f9a8:8", "const:4:8"]]
- 0058f9a8 ["CALLIND", null, ["register:0:8"]]
+ 0058f9e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058f9e8 ["INT_ADD", "register:40f0:8", ["const:58f9e8:8", "const:4:8"]]
+ 0058f9e8 ["CALLIND", null, ["register:0:8"]]
- 0058f9a8 bytes 00013fd6
+ 0058f9e8 bytes 00013fd6
- 0058f9c8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0058f9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058fa08 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0058fa08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fa08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058fa08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f9c8 bytes 08011391
+ 0058fa08 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1a8b67836ce26dd55ee895caefb6179"></a>

### [`0058fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md) → [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) FUN_0058fa88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043affc.md) [`0043b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b2ac.md) [`00467d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467d44.md) · 呼出先 5件 [`0058f788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f788.md) [`0058f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f900.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0043b03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md) [`0043b2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md) [`00467d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467d84.md) · 呼出先 5件 [`0058f7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md) [`0058f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.16% / 新版 81.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fac8",
      "incomplete_value": false,
      "site": "0058fac8",
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
            "const:55c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa88",
      "incomplete_value": false,
      "site": "0058fa88",
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
            "const:45c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fad0",
      "incomplete_value": false,
      "site": "0058fad0",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa90",
      "incomplete_value": false,
      "site": "0058fa90",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fad8",
      "incomplete_value": false,
      "site": "0058fad8",
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
            "const:564:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa98",
      "incomplete_value": false,
      "site": "0058fa98",
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
            "const:464:8"
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
      "0058fac8",
      "WRITE",
      [
        "storage",
        "00ca645c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fad0",
      "WRITE",
      [
        "storage",
        "00ca6460",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fad8",
      "WRITE",
      [
        "storage",
        "00ca6464",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fac8",
      "WRITE",
      [
        "storage",
        "00ca655c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fad0",
      "WRITE",
      [
        "storage",
        "00ca6560",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fad8",
      "WRITE",
      [
        "storage",
        "00ca6564",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa88) · [`0058fa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa90) · [`0058fa98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fa48.md#insn-0058fa98)
- 新版 [`0058fac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fac8) · [`0058fad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fad0) · [`0058fad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fad8)

~~~diff
- 0058fa88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:45c:8"]]
- 0058fa88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
+ 0058fac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:55c:8"]]
+ 0058fac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0058fa88 bytes 045d04b9
+ 0058fac8 bytes 045d05b9
- 0058fa90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:460:8"]]
- 0058fa90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
+ 0058fad0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 0058fad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0058fa90 bytes 056104b9
+ 0058fad0 bytes 056105b9
- 0058fa98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:464:8"]]
- 0058fa98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0058fad8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:564:8"]]
+ 0058fad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0058fa98 bytes 006504b9
+ 0058fad8 bytes 006505b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2593310affa1e5e73bb4cd57e38cf4be"></a>

### [`0058fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md) → [`0058fbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md) FUN_0058fbc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0061a0cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a0cc.md) [`008ab8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab8e8.md) [`008ac95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac95c.md) [`008d9464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9464.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0061a10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a10c.md) [`008ab940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ab/008ab940.md) [`008ac9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008ac9b4.md) [`008d94b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d94b8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fbdc",
      "incomplete_value": false,
      "site": "0058fbdc",
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
            "const:564:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fb9c",
      "incomplete_value": false,
      "site": "0058fb9c",
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
            "const:464:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fbe4",
      "incomplete_value": false,
      "site": "0058fbe4",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fba4",
      "incomplete_value": false,
      "site": "0058fba4",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fbf0",
      "incomplete_value": false,
      "site": "0058fbf0",
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
            "const:56c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fbb0",
      "incomplete_value": false,
      "site": "0058fbb0",
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
            "const:46c:8"
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
      "0058fbd0",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fbdc",
      "WRITE",
      [
        "storage",
        "00ca6464",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fbe4",
      "WRITE",
      [
        "storage",
        "00ca6468",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fbd0",
      "READ",
      [
        "storage",
        "00ca6610",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fbdc",
      "WRITE",
      [
        "storage",
        "00ca6564",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fbe4",
      "WRITE",
      [
        "storage",
        "00ca6568",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fb9c) · [`0058fba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fba4) · [`0058fbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md#insn-0058fbb0)
- 新版 [`0058fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbdc) · [`0058fbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbe4) · [`0058fbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbf0)

~~~diff
- 0058fb9c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:464:8"]]
- 0058fb9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0058fbdc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:564:8"]]
+ 0058fbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0058fb9c bytes 886504b9
+ 0058fbdc bytes 886505b9
- 0058fba4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:468:8"]]
- 0058fba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0058fbe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
+ 0058fbe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0058fba4 bytes 096904b9
+ 0058fbe4 bytes 096905b9
- 0058fbb0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:46c:8"]]
- 0058fbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0058fbf0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:56c:8"]]
+ 0058fbf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0058fbb0 bytes 4b6d04b9
+ 0058fbf0 bytes 4b6d05b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1e196d641cbb3c86b9f0862c73d0b9"></a>

### [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) → [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) FUN_0058fc04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00591b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591b34.md) [`00591bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591bc0.md) [`00591c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md) [`00591dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00591b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md) [`00591c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591c00.md) [`00591cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md) [`00591e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 38.71% / 新版 38.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fc3c",
      "incomplete_value": false,
      "site": "0058fc3c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "0058fbfc",
      "incomplete_value": false,
      "site": "0058fbfc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
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
      "definition_site": "0058fc40",
      "incomplete_value": false,
      "site": "0058fc40",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
              ]
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
      "definition_site": "0058fc00",
      "incomplete_value": false,
      "site": "0058fc00",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fc40",
      "incomplete_value": false,
      "site": "0058fc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058fc00",
      "incomplete_value": false,
      "site": "0058fc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "0058fc14",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fc28",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fc28",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fc14",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0058fc28",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fc28",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md#insn-0058fbf0) · [`0058fc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md#insn-0058fc2c)
- 新版 [`0058fc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc30) · [`0058fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc24) · [`0058fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc6c)

~~~diff
- 0058fbf0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0058fbf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058fbf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058fbf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058fc30 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0058fc30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058fc30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058fc30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058fbf0 bytes 21601491
+ 0058fc30 bytes 21601891
+ 0058fc24 ["COPY", "register:4048:8", ["const:ca6000:8"]]
+ 0058fc24 bytes a93800f0
- 0058fc2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058fc2c ["INT_ADD", "register:40f0:8", ["const:58fc2c:8", "const:4:8"]]
- 0058fc2c ["CALLIND", null, ["register:0:8"]]
+ 0058fc6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058fc6c ["INT_ADD", "register:40f0:8", ["const:58fc6c:8", "const:4:8"]]
+ 0058fc6c ["CALLIND", null, ["register:0:8"]]
- 0058fc2c bytes 00013fd6
+ 0058fc6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f5130249eff8b33784d93e6b1e4734"></a>

### [`0058fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md) → [`0058fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md) FUN_0058fd14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 44.00% / 新版 44.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058fd18",
      "READ",
      [
        "storage",
        "00ca6500",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fd2c",
      "READ",
      [
        "storage",
        "00ca64f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0058fd0c",
      "READ",
      [
        "storage",
        "00ca64e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fd18",
      "READ",
      [
        "storage",
        "00ca6600",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fd2c",
      "READ",
      [
        "storage",
        "00ca65f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fd4c",
      "READ",
      [
        "storage",
        "00ca65e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md#insn-0058fd1c) · [`0058fd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fcd4.md#insn-0058fd40)
- 新版 [`0058fd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md#insn-0058fd40)

~~~diff
- 0058fd1c ["INT_RIGHT", "register:4070:8", ["register:4070:8", "const:7:8"]]
- 0058fd1c bytes cefd47d3
- 0058fd40 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0058fd40 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0058fd40 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0058fd40 ["COPY", "tmp:1:8", ["register:4080:8"]]
- 0058fd40 bytes eb03909a
+ 0058fd40 ["COPY", "tmp:0:8", ["register:4060:8"]]
+ 0058fd40 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0058fd40 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0058fd40 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0058fd40 bytes 6d010c8b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca108cc1e4e05b17f2f0e2e27d570c5"></a>

### [`0058fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md) → [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md) FUN_0058fddc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 1件 [`005903b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005903b8.md)
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 1件 [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fe74",
      "incomplete_value": true,
      "site": "0058fe7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058fe34",
      "incomplete_value": true,
      "site": "0058fe3c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058fe78",
      "incomplete_value": true,
      "site": "0058fe80",
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
                "const:ca6000:8"
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
      "definition_site": "0058fe38",
      "incomplete_value": true,
      "site": "0058fe40",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:4c0:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fe90",
      "incomplete_value": false,
      "site": "0058fe90",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fe50",
      "incomplete_value": false,
      "site": "0058fe50",
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
            "const:500:8"
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
      "0058fdf4",
      "READ",
      [
        "storage",
        "00ca64e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe14",
      "READ",
      [
        "storage",
        "00ca64f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe14",
      "READ",
      [
        "storage",
        "00ca6500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fdf4",
      "READ",
      [
        "storage",
        "00ca65e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe14",
      "READ",
      [
        "storage",
        "00ca65f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fe14",
      "READ",
      [
        "storage",
        "00ca6600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fdf4) · [`0058fe50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fe50) · [`0058fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fd9c.md#insn-0058fdac)
- 新版 [`0058fe34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fe34) · [`0058fe90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fe90) · [`0058fdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fdec)

~~~diff
- 0058fdf4 ["INT_ADD", "register:40f0:8", ["const:58fdf4:8", "const:4:8"]]
- 0058fdf4 ["CALL", null, ["callee:005903f8:8"]]
+ 0058fe34 ["INT_ADD", "register:40f0:8", ["const:58fe34:8", "const:4:8"]]
+ 0058fe34 ["CALL", null, ["callee:005903f8:8"]]
- 0058fdf4 bytes 71010094
+ 0058fe34 bytes 71010094
- 0058fe50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 0058fe50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0058fe90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 0058fe90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0058fe50 bytes 098102f9
+ 0058fe90 bytes 090103f9
- 0058fdac ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 0058fdac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058fdac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058fdac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058fdec ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 0058fdec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058fdec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058fdec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058fdac bytes 29811391
+ 0058fdec bytes 29811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ae6b8b3a514937972f7dbec62f5aa38"></a>

### [`0058fe60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md) → [`0058fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md) FUN_0058fea0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 1件 [`00c58390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58390.md)
- 新版 呼出元 1件 [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 1件 [`00c58460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58460.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff08",
      "incomplete_value": false,
      "site": "0058ff08",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fec8",
      "incomplete_value": false,
      "site": "0058fec8",
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
            "const:508:8"
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
      "0058fec0",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fed4",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fed4",
      "READ",
      [
        "storage",
        "00ca64cc",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fec0",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fed4",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fed4",
      "READ",
      [
        "storage",
        "00ca65cc",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fe88) · [`0058fec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fec8) · [`0058fe78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fe60.md#insn-0058fe78)
- 新版 [`0058fec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058fec8) · [`0058ff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058ff08) · [`0058feb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058feb8)

~~~diff
- 0058fe88 ["INT_ADD", "register:40f0:8", ["const:58fe88:8", "const:4:8"]]
- 0058fe88 ["CALL", null, ["callee:00c58460:8"]]
+ 0058fec8 ["INT_ADD", "register:40f0:8", ["const:58fec8:8", "const:4:8"]]
+ 0058fec8 ["CALL", null, ["callee:00c58460:8"]]
- 0058fe88 bytes 42211b94
+ 0058fec8 bytes 66211b94
- 0058fec8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0058fec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
- 0058fec8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff08 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0058ff08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:608:8"]]
+ 0058ff08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058fec8 bytes 09211439
+ 0058ff08 bytes 09211839
- 0058fe78 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0058fe78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058fe78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058fe78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058feb8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0058feb8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058feb8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058feb8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058fe78 bytes 73021391
+ 0058feb8 bytes 73021791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd3a086a2b1f60b050a2accd3001f4bd"></a>

### [`0058fee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md) → [`0058ff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md) FUN_0058ff20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0055a6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff30",
      "incomplete_value": false,
      "site": "0058ff30",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fef0",
      "incomplete_value": false,
      "site": "0058fef0",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff38",
      "incomplete_value": true,
      "site": "0058ff38",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fef8",
      "incomplete_value": true,
      "site": "0058fef8",
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
            "const:4c0:8"
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
      "0058ff2c",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff30",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff38",
      "WRITE",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ff2c",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff30",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff38",
      "WRITE",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058fef0) · [`0058fef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058fef8) · [`0058feec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fee0.md#insn-0058feec)
- 新版 [`0058ff30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff30) · [`0058ff38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff38) · [`0058ff2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff2c)

~~~diff
- 0058fef0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058fef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
- 0058fef0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff30 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058ff30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
+ 0058ff30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058fef0 bytes 2a211439
+ 0058ff30 bytes 2a211839
- 0058fef8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
- 0058fef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 0058ff38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 0058ff38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058fef8 bytes 0031813d
+ 0058ff38 bytes 0071813d
- 0058feec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
- 0058feec ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0058feec ["COPY", "register:5030:8", ["const:0:8"]]
- 0058feec ["COPY", "register:5038:8", ["const:0:8"]]
+ 0058ff2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 0058ff2c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0058ff2c ["COPY", "register:5030:8", ["const:0:8"]]
+ 0058ff2c ["COPY", "register:5038:8", ["const:0:8"]]
- 0058feec bytes 0131c13d
+ 0058ff2c bytes 0171c13d
~~~


<a id="compare-7f63ef26291c3eaf3e0d0bd836d203b3"></a>

### [`0058ff00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md) → [`0058ff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md) FUN_0058ff40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055a6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6ac.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0055a6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6ec.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff54",
      "incomplete_value": true,
      "site": "0058ff54",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff14",
      "incomplete_value": true,
      "site": "0058ff14",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff60",
      "incomplete_value": true,
      "site": "0058ff60",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff20",
      "incomplete_value": true,
      "site": "0058ff20",
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
            "const:4c0:8"
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
      "0058ff50",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff54",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff60",
      "WRITE",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ff50",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff54",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff60",
      "WRITE",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff14) · [`0058ff20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff20) · [`0058ff10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff00.md#insn-0058ff10)
- 新版 [`0058ff54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff54) · [`0058ff60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff60) · [`0058ff50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff50)

~~~diff
- 0058ff14 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058ff14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
- 0058ff14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff54 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058ff54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
+ 0058ff54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff14 bytes 2a211439
+ 0058ff54 bytes 2a211839
- 0058ff20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
- 0058ff20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 0058ff60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 0058ff60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058ff20 bytes 0031813d
+ 0058ff60 bytes 0071813d
- 0058ff10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
- 0058ff10 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0058ff10 ["COPY", "register:5030:8", ["const:0:8"]]
- 0058ff10 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0058ff50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 0058ff50 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0058ff50 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0058ff50 ["COPY", "register:5038:8", ["const:0:8"]]
- 0058ff10 bytes 0131c13d
+ 0058ff50 bytes 0171c13d
~~~


<a id="compare-16638bc2d2b14ee06add9e81f4f1844b"></a>

### [`0058ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md) → [`0058ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md) FUN_0058ff68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b0.md) [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055a6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6f0.md) [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff7c",
      "incomplete_value": false,
      "site": "0058ff7c",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff3c",
      "incomplete_value": false,
      "site": "0058ff3c",
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
            "const:508:8"
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
      "0058ff74",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff74",
      "READ",
      [
        "storage",
        "00ca64c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff7c",
      "WRITE",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0058ff74",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff74",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff7c",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md#insn-0058ff3c) · [`0058ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md#insn-0058ff28) · [`0058ff2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ff28.md#insn-0058ff2c)
- 新版 [`0058ff7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md#insn-0058ff7c) · [`0058ff6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md#insn-0058ff6c)

~~~diff
- 0058ff3c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058ff3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:508:8"]]
- 0058ff3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0058ff7c ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0058ff7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
+ 0058ff7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff3c bytes 2a211439
+ 0058ff7c bytes 2a211839
- 0058ff28 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0058ff28 bytes a83800f0
- 0058ff2c ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0058ff2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ff6c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0058ff6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ff6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ff6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ff2c bytes 08011391
+ 0058ff6c bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6c8beca0a9a73096f4268f02449431b"></a>

### [`0058ffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md) → [`0058ffe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md) FUN_0058ffe8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00555c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555c94.md) [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`0055a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a438.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00468200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468200.md) [`005554b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005554b8.md) [`00555cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md) [`005599a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005599a4.md) [`0055a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a478.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.91% / 新版 65.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 5件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590030",
      "incomplete_value": false,
      "site": "00590030",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "0058fff0",
      "incomplete_value": false,
      "site": "0058fff0",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590038",
      "incomplete_value": false,
      "site": "00590038",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
              ]
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
      "definition_site": "0058fff8",
      "incomplete_value": false,
      "site": "0058fff8",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590038",
      "incomplete_value": false,
      "site": "00590038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "0058fff8",
      "incomplete_value": false,
      "site": "0058fff8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "00590008",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "00590024",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590028",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590008",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "00590024",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "00590028",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-00590028) · [`0058ffc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-0058ffc8) · [`0058ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058ffa8.md#insn-0058ffdc)
- 新版 [`00590068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-00590068) · [`00590008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-00590008) · [`0059001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-0059001c)

~~~diff
- 00590028 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590028 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590028 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:508:8"]]
- 00590028 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590068 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590068 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590068 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:608:8"]]
+ 00590068 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590028 bytes df221439
+ 00590068 bytes df221839
- 0058ffc8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:508:8"]]
- 0058ffc8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0058ffc8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00590008 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:608:8"]]
+ 00590008 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00590008 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0058ffc8 bytes c8225439
+ 00590008 bytes c8225839
- 0058ffdc ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0058ffdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ffdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ffdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059001c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0059001c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059001c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059001c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ffdc bytes 08011391
+ 0059001c bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dc5406a9bcb3ae9bba41c10d708881f"></a>

### [`00590058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md) → [`00590098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md) FUN_00590098

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`00551488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/00551488.md) [`0055151c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/0055151c.md) [`005515b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/005515b0.md) [`005517fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/005517fc.md) [`0055196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00551/0055196c.md) · 呼出先 0件 
- 新版 呼出元 13件 [`005514c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005514c8.md) [`0055155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/0055155c.md) [`005515f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005515f0.md) [`0055183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/0055183c.md) [`005519ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005519ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590110",
      "incomplete_value": true,
      "site": "00590110",
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
    "old": {
      "definition_site": "005900d0",
      "incomplete_value": true,
      "site": "005900d0",
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
            "const:508:8"
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
      "005900b4",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "005900cc",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "005900d0",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005900b4",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "005900cc",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "005900d0",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005900d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md#insn-005900d0) · [`00590074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md#insn-00590074) · [`00590078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590058.md#insn-00590078)
- 新版 [`00590110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md#insn-00590110) · [`005900b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md#insn-005900b4)

~~~diff
- 005900d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005900d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005900d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:508:8"]]
- 005900d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590110 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590110 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590110 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
+ 00590110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005900d0 bytes bf221439
+ 00590110 bytes bf221839
- 00590074 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
- 00590074 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00590074 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 005900b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:608:8"]]
+ 005900b4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 005900b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00590074 bytes a8225439
+ 005900b4 bytes a8225839
- 00590078 ["COPY", "register:40b0:8", ["const:ca6000:8"]]
- 00590078 bytes b63800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0edc81bf6fd4695dcf17aaaeb2f7e5ba"></a>

### [`005900f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md) → [`00590138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md) FUN_00590138

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 62.90% / 新版 62.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005901c4",
      "incomplete_value": true,
      "site": "005901c4",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590184",
      "incomplete_value": true,
      "site": "00590184",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005901dc",
      "incomplete_value": true,
      "site": "005901dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
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
      "definition_site": "0059019c",
      "incomplete_value": true,
      "site": "0059019c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "005901c8",
      "incomplete_value": true,
      "site": "005901dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:610:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590188",
      "incomplete_value": true,
      "site": "0059019c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:510:8"
              ]
            ]
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
      "0059015c",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "00590180",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590184",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059015c",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "00590180",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "00590184",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059015c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-0059015c) · [`00590180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-00590180) · [`00590184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005900f8.md#insn-00590184)
- 新版 [`0059019c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-0059019c) · [`005901c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-005901c0) · [`005901c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-005901c4)

~~~diff
- 0059015c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
- 0059015c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0059015c ["COPY", "register:5008:8", ["const:0:8"]]
- 0059015c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0059019c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
+ 0059019c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0059019c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0059019c ["COPY", "register:5010:8", ["const:0:8"]]
- 0059015c bytes 20cd46fd
+ 0059019c bytes 20ed46fd
- 00590180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00590180 ["INT_ADD", "register:40f0:8", ["const:590180:8", "const:4:8"]]
- 00590180 ["CALLIND", null, ["register:0:8"]]
+ 005901c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005901c0 ["INT_ADD", "register:40f0:8", ["const:5901c0:8", "const:4:8"]]
+ 005901c0 ["CALLIND", null, ["register:0:8"]]
- 00590180 bytes 00013fd6
+ 005901c0 bytes 00013fd6
- 00590184 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590184 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590184 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:508:8"]]
- 00590184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 005901c4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 005901c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 005901c4 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:608:8"]]
+ 005901c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590184 bytes 3f231439
+ 005901c4 bytes 3f231839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5865f5d37eb3c0da2c152545a7518c4f"></a>

### [`005901f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md) → [`00590230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md) FUN_00590230

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d5e8.md) [`0055d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d7c0.md) [`0055d99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055d/0055d99c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590288",
      "incomplete_value": false,
      "site": "00590288",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "00590248",
      "incomplete_value": false,
      "site": "00590248",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590290",
      "incomplete_value": false,
      "site": "00590290",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:618:8"
              ]
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
      "definition_site": "00590250",
      "incomplete_value": false,
      "site": "00590250",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590290",
      "incomplete_value": false,
      "site": "00590290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
      "definition_site": "00590250",
      "incomplete_value": false,
      "site": "00590250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:18:8"
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00590254",
      "READ",
      [
        "storage",
        "00ca6508",
        null,
        "undefined1"
      ]
    ],
    [
      "0059027c",
      "PARAM",
      [
        "storage",
        "00ca6518",
        null,
        "undefined8"
      ]
    ],
    [
      "00590280",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590254",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0059027c",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "00590280",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-00590214) · [`00590234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-00590234) · [`0059023c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/005901f0.md#insn-0059023c)
- 新版 [`00590254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-00590254) · [`00590274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-00590274) · [`0059027c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-0059027c)

~~~diff
- 00590214 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:508:8"]]
- 00590214 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00590214 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00590254 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:608:8"]]
+ 00590254 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00590254 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00590214 bytes 28235439
+ 00590254 bytes 28235839
- 00590234 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00590234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00590234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00590234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00590274 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00590274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00590274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00590274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00590234 bytes 08011391
+ 00590274 bytes 08011791
- 0059023c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0059023c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0059023c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0059023c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059027c ["COPY", "tmp:0:8", ["const:618:8"]]
+ 0059027c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059027c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059027c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0059023c bytes 21601491
+ 0059027c bytes 21601891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870014ad9d6cd35eaa59586299d66d5b"></a>

### [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) → [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) FUN_00590df8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005923b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md) · 呼出先 17件 [`00550c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c04.md) [`00555274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555274.md) [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`005923f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md) · 呼出先 17件 [`00550c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c44.md) [`005552b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552b4.md) [`0059129c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md) [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00590e24",
      "incomplete_value": false,
      "site": "00590e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590de4",
      "incomplete_value": false,
      "site": "00590df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "definition_site": "00590e64",
      "incomplete_value": true,
      "site": "00590e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e24",
      "incomplete_value": true,
      "site": "00590e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:22f:8"
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
      "definition_site": "00590ea4",
      "incomplete_value": true,
      "site": "00590ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e64",
      "incomplete_value": true,
      "site": "00590e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cfa:8"
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
      "00590e30",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ],
    [
      "00590e54",
      "READ",
      [
        "storage",
        "002a022f",
        null,
        "string"
      ]
    ],
    [
      "00590e94",
      "READ",
      [
        "storage",
        "002b3cfa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00590e30",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00590e54",
      "READ",
      [
        "storage",
        "002a01e2",
        null,
        "string"
      ]
    ],
    [
      "00590e94",
      "READ",
      [
        "storage",
        "002b3d2b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590de4) · [`00590ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590ee8) · [`00590f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md#insn-00590f28)
- 新版 [`00590e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590e24) · [`00590f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590f28) · [`00590f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590f68)

~~~diff
- 00590de4 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00590de4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00590de4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00590de4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00590e24 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00590e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00590e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00590e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00590de4 bytes 29410091
+ 00590e24 bytes 29810391
- 00590ee8 ["INT_ADD", "register:40f0:8", ["const:590ee8:8", "const:4:8"]]
- 00590ee8 ["CALL", null, ["callee:00c586e0:8"]]
+ 00590f28 ["INT_ADD", "register:40f0:8", ["const:590f28:8", "const:4:8"]]
+ 00590f28 ["CALL", null, ["callee:00c586e0:8"]]
- 00590ee8 bytes ca1d1b94
+ 00590f28 bytes ee1d1b94
- 00590f28 ["INT_ADD", "register:40f0:8", ["const:590f28:8", "const:4:8"]]
- 00590f28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00590f68 ["INT_ADD", "register:40f0:8", ["const:590f68:8", "const:4:8"]]
+ 00590f68 ["CALL", null, ["callee:00c53da0:8"]]
- 00590f28 bytes 760b1b94
+ 00590f68 bytes 8e0b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002016532126d176220aa68399b7c989"></a>

### [`005912b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md) → [`005912f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md) FUN_005912f8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a360.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005913c4",
      "incomplete_value": false,
      "site": "005913c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591384",
      "incomplete_value": false,
      "site": "00591384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "definition_site": "005913dc",
      "incomplete_value": true,
      "site": "005913e4",
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059139c",
      "incomplete_value": true,
      "site": "005913a4",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591354",
      "incomplete_value": true,
      "site": "00591358",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591314",
      "incomplete_value": true,
      "site": "00591318",
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
              "LOAD"
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
      "00591350",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00591354",
      "READ",
      [
        "storage",
        "00ca3e44",
        null,
        "undefined4"
      ]
    ],
    [
      "0059135c",
      "READ",
      [
        "storage",
        "00ca3e48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00591350",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "00591354",
      "READ",
      [
        "storage",
        "00ca3f14",
        null,
        "undefined4"
      ]
    ],
    [
      "0059135c",
      "READ",
      [
        "storage",
        "00ca3f18",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-00591318) · [`00591364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-00591364) · [`005912f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005912b8.md#insn-005912f4)
- 新版 [`00591358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-00591358) · [`005913a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-005913a4) · [`00591334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-00591334)

~~~diff
- 00591318 ["INT_ADD", "register:40f0:8", ["const:591318:8", "const:4:8"]]
- 00591318 ["CALL", null, ["callee:00c5a450:8"]]
+ 00591358 ["INT_ADD", "register:40f0:8", ["const:591358:8", "const:4:8"]]
+ 00591358 ["CALL", null, ["callee:00c5a450:8"]]
- 00591318 bytes 1a241b94
+ 00591358 bytes 3e241b94
- 00591364 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00591364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005913a4 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 005913a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005913a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005913a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591364 bytes 08810791
+ 005913a4 bytes 08c10a91
- 005912f4 ["INT_ADD", "register:40f0:8", ["const:5912f4:8", "const:4:8"]]
- 005912f4 ["CALL", null, ["callee:00c5a430:8"]]
+ 00591334 ["INT_ADD", "register:40f0:8", ["const:591334:8", "const:4:8"]]
+ 00591334 ["CALL", null, ["callee:00c5a430:8"]]
- 005912f4 bytes 1b241b94
+ 00591334 bytes 3f241b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3e32bc5dde52d5ce3d3fe5b9ce2e6d"></a>

### [`00591400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md) → [`00591440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md) FUN_00591440

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a360.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md)
- 新版 呼出元 0件  · 呼出先 10件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059151c",
      "incomplete_value": false,
      "site": "00591524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005914dc",
      "incomplete_value": false,
      "site": "005914e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "definition_site": "0059153c",
      "incomplete_value": false,
      "site": "0059153c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005914fc",
      "incomplete_value": false,
      "site": "005914fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "definition_site": "00591554",
      "incomplete_value": true,
      "site": "00591558",
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591514",
      "incomplete_value": true,
      "site": "00591518",
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
      "005914a0",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "005914a4",
      "READ",
      [
        "storage",
        "00ca3e44",
        null,
        "undefined4"
      ]
    ],
    [
      "005914ac",
      "READ",
      [
        "storage",
        "00ca3e48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005914a0",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "005914a4",
      "READ",
      [
        "storage",
        "00ca3f14",
        null,
        "undefined4"
      ]
    ],
    [
      "005914ac",
      "READ",
      [
        "storage",
        "00ca3f18",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-00591468) · [`00591558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-00591558) · [`00591444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591400.md#insn-00591444)
- 新版 [`005914a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-005914a8) · [`00591598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-00591598) · [`00591484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-00591484)

~~~diff
- 00591468 ["INT_ADD", "register:40f0:8", ["const:591468:8", "const:4:8"]]
- 00591468 ["CALL", null, ["callee:00c5a450:8"]]
+ 005914a8 ["INT_ADD", "register:40f0:8", ["const:5914a8:8", "const:4:8"]]
+ 005914a8 ["CALL", null, ["callee:00c5a450:8"]]
- 00591468 bytes c6231b94
+ 005914a8 bytes ea231b94
- 00591558 ["INT_ADD", "register:40f0:8", ["const:591558:8", "const:4:8"]]
- 00591558 ["CALL", null, ["callee:00c5a4b0:8"]]
+ 00591598 ["INT_ADD", "register:40f0:8", ["const:591598:8", "const:4:8"]]
+ 00591598 ["CALL", null, ["callee:00c5a4b0:8"]]
- 00591558 bytes a2231b94
+ 00591598 bytes c6231b94
- 00591444 ["INT_ADD", "register:40f0:8", ["const:591444:8", "const:4:8"]]
- 00591444 ["CALL", null, ["callee:00c5a430:8"]]
+ 00591484 ["INT_ADD", "register:40f0:8", ["const:591484:8", "const:4:8"]]
+ 00591484 ["CALL", null, ["callee:00c5a430:8"]]
- 00591444 bytes c7231b94
+ 00591484 bytes eb231b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5b37c248ca47c890b44ec5eaa8796fc"></a>

### [`005915fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md) → [`0059163c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md) FUN_0059163c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a400.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a4d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591680",
      "incomplete_value": false,
      "site": "00591688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591640",
      "incomplete_value": false,
      "site": "00591648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005916a0",
      "incomplete_value": false,
      "site": "005916a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591660",
      "incomplete_value": false,
      "site": "00591660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "00591688",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ],
    [
      "005916a0",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00591688",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ],
    [
      "005916a0",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-00591630) · [`00591638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-00591638) · [`00591640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005915fc.md#insn-00591640)
- 新版 [`00591670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-00591670) · [`00591678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-00591678) · [`00591680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-00591680)

~~~diff
- 00591630 ["INT_ADD", "register:40f0:8", ["const:591630:8", "const:4:8"]]
- 00591630 ["CALL", null, ["callee:00c5a4d0:8"]]
+ 00591670 ["INT_ADD", "register:40f0:8", ["const:591670:8", "const:4:8"]]
+ 00591670 ["CALL", null, ["callee:00c5a4d0:8"]]
- 00591630 bytes 74231b94
+ 00591670 bytes 98231b94
- 00591638 ["INT_ADD", "register:40f0:8", ["const:591638:8", "const:4:8"]]
- 00591638 ["CALL", null, ["callee:00c57f60:8"]]
+ 00591678 ["INT_ADD", "register:40f0:8", ["const:591678:8", "const:4:8"]]
+ 00591678 ["CALL", null, ["callee:00c57f60:8"]]
- 00591638 bytes 161a1b94
+ 00591678 bytes 3a1a1b94
- 00591640 ["COPY", "tmp:0:8", ["const:350:8"]]
- 00591640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00591640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00591680 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00591680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00591680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00591680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00591640 bytes 08410d91
+ 00591680 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69079bb755b8447790e607332440eed"></a>

### [`00591788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md) → [`005917c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md) FUN_005917c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005917e0",
      "incomplete_value": false,
      "site": "005917ec",
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
            "const:e53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005917a0",
      "incomplete_value": false,
      "site": "005917ac",
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
            "const:ea7:8"
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
      "005917e0",
      "PARAM",
      [
        "storage",
        "002beea7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005917e0",
      "PARAM",
      [
        "storage",
        "002bee53",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005917ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md#insn-005917ac) · [`005917a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591788.md#insn-005917a0)
- 新版 [`005917ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md#insn-005917ec) · [`005917e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md#insn-005917e0)

~~~diff
- 005917ac ["INT_ADD", "register:40f0:8", ["const:5917ac:8", "const:4:8"]]
- 005917ac ["CALL", null, ["callee:005925b8:8"]]
+ 005917ec ["INT_ADD", "register:40f0:8", ["const:5917ec:8", "const:4:8"]]
+ 005917ec ["CALL", null, ["callee:005925b8:8"]]
- 005917ac bytes 73030094
+ 005917ec bytes 73030094
- 005917a0 ["COPY", "tmp:0:8", ["const:ea7:8"]]
- 005917a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005917a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005917a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005917e0 ["COPY", "tmp:0:8", ["const:e53:8"]]
+ 005917e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005917e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005917e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005917a0 bytes 219c3a91
+ 005917e0 bytes 214c3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236e02b9b96da427b5c3a498a30cbe5a"></a>

### [`00591840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md) → [`00591880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md) FUN_00591880

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591898",
      "incomplete_value": false,
      "site": "005918a4",
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
            "const:28a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591858",
      "incomplete_value": false,
      "site": "00591864",
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
            "const:2d7:8"
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
      "00591898",
      "PARAM",
      [
        "storage",
        "002a32d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591898",
      "PARAM",
      [
        "storage",
        "002a328a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md#insn-00591864) · [`00591858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591840.md#insn-00591858)
- 新版 [`005918a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md#insn-005918a4) · [`00591898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md#insn-00591898)

~~~diff
- 00591864 ["INT_ADD", "register:40f0:8", ["const:591864:8", "const:4:8"]]
- 00591864 ["CALL", null, ["callee:005925b8:8"]]
+ 005918a4 ["INT_ADD", "register:40f0:8", ["const:5918a4:8", "const:4:8"]]
+ 005918a4 ["CALL", null, ["callee:005925b8:8"]]
- 00591864 bytes 45030094
+ 005918a4 bytes 45030094
- 00591858 ["COPY", "tmp:0:8", ["const:2d7:8"]]
- 00591858 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591858 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591858 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591898 ["COPY", "tmp:0:8", ["const:28a:8"]]
+ 00591898 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591898 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591898 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591858 bytes 215c0b91
+ 00591898 bytes 21280a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e040c102d5fba69105f967d9f03a907d"></a>

### [`00591888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md) → [`005918c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md) FUN_005918c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00592578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592578.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005918e0",
      "incomplete_value": false,
      "site": "005918f0",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005918a0",
      "incomplete_value": false,
      "site": "005918b0",
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
            "const:934:8"
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
      "005918e0",
      "PARAM",
      [
        "storage",
        "002ad934",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005918e0",
      "PARAM",
      [
        "storage",
        "002ad8d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005918b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md#insn-005918b0) · [`005918a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591888.md#insn-005918a0)
- 新版 [`005918f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md#insn-005918f0) · [`005918e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md#insn-005918e0)

~~~diff
- 005918b0 ["INT_ADD", "register:40f0:8", ["const:5918b0:8", "const:4:8"]]
- 005918b0 ["CALL", null, ["callee:005925b8:8"]]
+ 005918f0 ["INT_ADD", "register:40f0:8", ["const:5918f0:8", "const:4:8"]]
+ 005918f0 ["CALL", null, ["callee:005925b8:8"]]
- 005918b0 bytes 32030094
+ 005918f0 bytes 32030094
- 005918a0 ["COPY", "tmp:0:8", ["const:934:8"]]
- 005918a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005918a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005918a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005918e0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 005918e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005918e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005918e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005918a0 bytes 21d02491
+ 005918e0 bytes 21602391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c6feeca9d46ba024c411eb127162c09"></a>

### [`005919b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md) → [`005919f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md) FUN_005919f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a470.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md)

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
      "definition_site": "00591a20",
      "incomplete_value": false,
      "site": "00591a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005919e0",
      "incomplete_value": false,
      "site": "005919f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "definition_site": "00591a24",
      "incomplete_value": true,
      "site": "00591a30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005919e4",
      "incomplete_value": true,
      "site": "005919f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
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
      "00591a20",
      "PARAM",
      [
        "storage",
        "00c6d1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591a24",
      "READ",
      [
        "storage",
        "00c9b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00591a24",
      "PARAM",
      [
        "storage",
        "00c6d4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591a20",
      "PARAM",
      [
        "storage",
        "00c6d290",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591a24",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "00591a24",
      "PARAM",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005919f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-005919f0) · [`00591a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-00591a30) · [`005919e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005919b8.md#insn-005919e0)
- 新版 [`00591a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a30) · [`00591a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a70) · [`00591a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a20)

~~~diff
- 005919f0 ["INT_ADD", "register:40f0:8", ["const:5919f0:8", "const:4:8"]]
- 005919f0 ["CALL", null, ["callee:00c586e0:8"]]
+ 00591a30 ["INT_ADD", "register:40f0:8", ["const:591a30:8", "const:4:8"]]
+ 00591a30 ["CALL", null, ["callee:00c586e0:8"]]
- 005919f0 bytes 081b1b94
+ 00591a30 bytes 2c1b1b94
- 00591a30 ["INT_ADD", "register:40f0:8", ["const:591a30:8", "const:4:8"]]
- 00591a30 ["CALL", null, ["callee:00c53da0:8"]]
+ 00591a70 ["INT_ADD", "register:40f0:8", ["const:591a70:8", "const:4:8"]]
+ 00591a70 ["CALL", null, ["callee:00c53da0:8"]]
- 00591a30 bytes b4081b94
+ 00591a70 bytes cc081b94
- 005919e0 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005919e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005919e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005919e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591a20 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 00591a20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591a20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591a20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005919e0 bytes 21000791
+ 00591a20 bytes 21400a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f70d7d1bd468adf2a0e7fe85fa45abf2"></a>

### [`00591c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md) → [`00591cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md) FUN_00591cbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3a0.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a470.md) [`00c5a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591cfc",
      "incomplete_value": true,
      "site": "00591d08",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591cbc",
      "incomplete_value": true,
      "site": "00591cc8",
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
            "const:130:8"
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
      "definition_site": "00591d20",
      "incomplete_value": false,
      "site": "00591d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ce0",
      "incomplete_value": false,
      "site": "00591cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "definition_site": "00591d28",
      "incomplete_value": false,
      "site": "00591d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591ce8",
      "incomplete_value": false,
      "site": "00591cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00591cf4",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591cfc",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591d20",
      "PARAM",
      [
        "storage",
        "00c6d148",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591cf4",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591cfc",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591d20",
      "PARAM",
      [
        "storage",
        "00c6d218",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cc8) · [`00591cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cf0) · [`00591cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591c7c.md#insn-00591cb4)
- 新版 [`00591d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591d08) · [`00591d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591d30) · [`00591cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591cf4)

~~~diff
- 00591cc8 ["INT_ADD", "register:40f0:8", ["const:591cc8:8", "const:4:8"]]
- 00591cc8 ["CALL", null, ["callee:00c586e0:8"]]
+ 00591d08 ["INT_ADD", "register:40f0:8", ["const:591d08:8", "const:4:8"]]
+ 00591d08 ["CALL", null, ["callee:00c586e0:8"]]
- 00591cc8 bytes 521a1b94
+ 00591d08 bytes 761a1b94
- 00591cf0 ["INT_ADD", "register:40f0:8", ["const:591cf0:8", "const:4:8"]]
- 00591cf0 ["CALL", null, ["callee:00c586e0:8"]]
+ 00591d30 ["INT_ADD", "register:40f0:8", ["const:591d30:8", "const:4:8"]]
+ 00591d30 ["CALL", null, ["callee:00c586e0:8"]]
- 00591cf0 bytes 481a1b94
+ 00591d30 bytes 6c1a1b94
- 00591cb4 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00591cb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591cb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591cb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591cf4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00591cf4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591cf4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591cf4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591cb4 bytes 21800491
+ 00591cf4 bytes 21c00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7e9962eee6ce033a2becee3de49e8e1"></a>

### [`00591dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md) → [`00591e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md) FUN_00591e04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fbc4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md) [`00c5a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a370.md) [`00c5a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a3a0.md) [`00c5a4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a4d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a470.md) [`00c5a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e34",
      "incomplete_value": false,
      "site": "00591e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "definition_site": "00591e90",
      "incomplete_value": false,
      "site": "00591ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e50",
      "incomplete_value": false,
      "site": "00591e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "definition_site": "00591e98",
      "incomplete_value": false,
      "site": "00591ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e58",
      "incomplete_value": false,
      "site": "00591e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00591e44",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e4c",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e6c",
      "PARAM",
      [
        "storage",
        "00c6d148",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591e44",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e4c",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591e6c",
      "PARAM",
      [
        "storage",
        "00c6d218",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e3c) · [`00591e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e60) · [`00591e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/00591dc4.md#insn-00591e04)
- 新版 [`00591e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591e7c) · [`00591ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591ea0) · [`00591e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591e44)

~~~diff
- 00591e3c ["INT_ADD", "register:40f0:8", ["const:591e3c:8", "const:4:8"]]
- 00591e3c ["CALL", null, ["callee:00c586e0:8"]]
+ 00591e7c ["INT_ADD", "register:40f0:8", ["const:591e7c:8", "const:4:8"]]
+ 00591e7c ["CALL", null, ["callee:00c586e0:8"]]
- 00591e3c bytes f5191b94
+ 00591e7c bytes 191a1b94
- 00591e60 ["INT_ADD", "register:40f0:8", ["const:591e60:8", "const:4:8"]]
- 00591e60 ["CALL", null, ["callee:00c586e0:8"]]
+ 00591ea0 ["INT_ADD", "register:40f0:8", ["const:591ea0:8", "const:4:8"]]
+ 00591ea0 ["CALL", null, ["callee:00c586e0:8"]]
- 00591e60 bytes ec191b94
+ 00591ea0 bytes 101a1b94
- 00591e04 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00591e04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591e04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591e04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591e44 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00591e44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591e44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591e44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591e04 bytes 21800491
+ 00591e44 bytes 21c00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf13abf7fe2edb222f4132878ad57db"></a>

### [`005920c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md) → [`00592100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md) FUN_00592100

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00592148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592148.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00592188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00592128",
      "incomplete_value": false,
      "site": "00592144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920e8",
      "incomplete_value": false,
      "site": "00592104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "definition_site": "00592130",
      "incomplete_value": false,
      "site": "00592144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005920f0",
      "incomplete_value": false,
      "site": "00592104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:180:8"
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
      "00592128",
      "PARAM",
      [
        "storage",
        "00c6d170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592130",
      "PARAM",
      [
        "storage",
        "00c6d180",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592128",
      "PARAM",
      [
        "storage",
        "00c6d240",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592130",
      "PARAM",
      [
        "storage",
        "00c6d250",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-00592104) · [`005920e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-005920e8) · [`005920f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005920c0.md#insn-005920f0)
- 新版 [`00592144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592144) · [`00592128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592128) · [`00592130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592130)

~~~diff
- 00592104 ["INT_ADD", "register:40f0:8", ["const:592104:8", "const:4:8"]]
- 00592104 ["CALL", null, ["callee:00c586e0:8"]]
+ 00592144 ["INT_ADD", "register:40f0:8", ["const:592144:8", "const:4:8"]]
+ 00592144 ["CALL", null, ["callee:00c586e0:8"]]
- 00592104 bytes 43191b94
+ 00592144 bytes 67191b94
- 005920e8 ["COPY", "tmp:0:8", ["const:170:8"]]
- 005920e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005920e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005920e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00592128 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00592128 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00592128 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00592128 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005920e8 bytes 21c00591
+ 00592128 bytes 21000991
- 005920f0 ["COPY", "tmp:0:8", ["const:180:8"]]
- 005920f0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005920f0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005920f0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00592130 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00592130 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00592130 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00592130 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005920f0 bytes 42000691
+ 00592130 bytes 42400991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308031e00bf21e91644c5d95eb22c9f6"></a>

### [`005923b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md) → [`005923f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md) FUN_005923f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0043b0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b0e8.md) · 呼出先 2件 [`00590db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00590/00590db8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0043b128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md) · 呼出先 2件 [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592414",
      "incomplete_value": false,
      "site": "00592420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005923d4",
      "incomplete_value": false,
      "site": "005923e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "00592420",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592420",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005923c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923c8) · [`005923d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923d4) · [`005923e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005923b0.md#insn-005923e8)
- 新版 [`00592408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592408) · [`00592414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592414) · [`00592428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592428)

~~~diff
- 005923c8 ["INT_ADD", "register:40f0:8", ["const:5923c8:8", "const:4:8"]]
- 005923c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00592408 ["INT_ADD", "register:40f0:8", ["const:592408:8", "const:4:8"]]
+ 00592408 ["CALL", null, ["callee:00c57f60:8"]]
- 005923c8 bytes b2161b94
+ 00592408 bytes d6161b94
- 005923d4 ["COPY", "tmp:0:8", ["const:460:8"]]
- 005923d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005923d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005923d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592414 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00592414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005923d4 bytes 08811191
+ 00592414 bytes 08c11491
- 005923e8 ["INT_ADD", "register:40f0:8", ["const:5923e8:8", "const:4:8"]]
- 005923e8 ["CALL", null, ["callee:00590df8:8"]]
+ 00592428 ["INT_ADD", "register:40f0:8", ["const:592428:8", "const:4:8"]]
+ 00592428 ["CALL", null, ["callee:00590df8:8"]]
- 005923e8 bytes 74faff97
+ 00592428 bytes 74faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84570da6e6e56cae2a71d1230689cfe1"></a>

### [`0059241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md) → [`0059245c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md) FUN_0059245c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592474",
      "incomplete_value": false,
      "site": "00592478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592434",
      "incomplete_value": false,
      "site": "00592438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "00592478",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592478",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592434) · [`00592448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592448) · [`00592460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059241c.md#insn-00592460)
- 新版 [`00592474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-00592474) · [`00592488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-00592488) · [`005924a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-005924a0)

~~~diff
- 00592434 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00592434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592474 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00592474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592434 bytes 08410091
+ 00592474 bytes 08810391
- 00592448 ["INT_ADD", "register:40f0:8", ["const:592448:8", "const:4:8"]]
- 00592448 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592488 ["INT_ADD", "register:40f0:8", ["const:592488:8", "const:4:8"]]
+ 00592488 ["CALL", null, ["callee:00c53da0:8"]]
- 00592448 bytes 2e061b94
+ 00592488 bytes 46061b94
- 00592460 ["INT_ADD", "register:40f0:8", ["const:592460:8", "const:4:8"]]
- 00592460 ["CALL", null, ["callee:00c53da0:8"]]
+ 005924a0 ["INT_ADD", "register:40f0:8", ["const:5924a0:8", "const:4:8"]]
+ 005924a0 ["CALL", null, ["callee:00c53da0:8"]]
- 00592460 bytes 28061b94
+ 005924a0 bytes 40061b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d0c0245c40c827c5506ac032578e4b5"></a>

### [`005924b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md) → [`005924f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md) FUN_005924f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592510",
      "incomplete_value": false,
      "site": "00592514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005924d0",
      "incomplete_value": false,
      "site": "005924d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "00592514",
      "DATA",
      [
        "storage",
        "00c6d010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592514",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-00592514) · [`005924d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-005924d0) · [`005924e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005924b8.md#insn-005924e4)
- 新版 [`00592554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-00592554) · [`00592510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-00592510) · [`00592524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-00592524)

~~~diff
- 00592514 ["INT_ADD", "register:40f0:8", ["const:592514:8", "const:4:8"]]
- 00592514 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592554 ["INT_ADD", "register:40f0:8", ["const:592554:8", "const:4:8"]]
+ 00592554 ["CALL", null, ["callee:00c53da0:8"]]
- 00592514 bytes fb051b94
+ 00592554 bytes 13061b94
- 005924d0 ["COPY", "tmp:0:8", ["const:10:8"]]
- 005924d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005924d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005924d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592510 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00592510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005924d0 bytes 08410091
+ 00592510 bytes 08810391
- 005924e4 ["INT_ADD", "register:40f0:8", ["const:5924e4:8", "const:4:8"]]
- 005924e4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592524 ["INT_ADD", "register:40f0:8", ["const:592524:8", "const:4:8"]]
+ 00592524 ["CALL", null, ["callee:00c53da0:8"]]
- 005924e4 bytes 07061b94
+ 00592524 bytes 1f061b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eb2a4d287a0c0b00982f82be35771f9"></a>

### [`005925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925c4.md) → [`00592604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592604.md) FUN_00592604

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00592608",
      "incomplete_value": false,
      "site": "0059260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005925c8",
      "incomplete_value": false,
      "site": "005925cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "0059260c",
      "DATA",
      [
        "storage",
        "00c6d1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059260c",
      "DATA",
      [
        "storage",
        "00c6d2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005925c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925c4.md#insn-005925c8)
- 新版 [`00592608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592604.md#insn-00592608)

~~~diff
- 005925c8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005925c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005925c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005925c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592608 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00592608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005925c8 bytes 08810791
+ 00592608 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3029e06bb53294553be240573ed795cb"></a>

### [`005925d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md) → [`00592614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md) FUN_00592614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592624",
      "incomplete_value": false,
      "site": "0059262c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005925e4",
      "incomplete_value": false,
      "site": "005925ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
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
      "0059262c",
      "DATA",
      [
        "storage",
        "00c6d1e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059262c",
      "DATA",
      [
        "storage",
        "00c6d2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005925e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md#insn-005925e4) · [`005925f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005925d4.md#insn-005925f0)
- 新版 [`00592624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md#insn-00592624) · [`00592630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md#insn-00592630)

~~~diff
- 005925e4 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 005925e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005925e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005925e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592624 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00592624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005925e4 bytes 08810791
+ 00592624 bytes 08c10a91
- 005925f0 ["INT_ADD", "register:40f0:8", ["const:5925f0:8", "const:4:8"]]
- 005925f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00592630 ["INT_ADD", "register:40f0:8", ["const:592630:8", "const:4:8"]]
+ 00592630 ["CALL", null, ["callee:00c57f70:8"]]
- 005925f0 bytes 2c161b94
+ 00592630 bytes 50161b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8365e43e33252024c1dd79aa034de668"></a>

### [`00592614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md) → [`00592654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md) FUN_00592654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a550.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a620.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059266c",
      "incomplete_value": false,
      "site": "00592670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059262c",
      "incomplete_value": false,
      "site": "00592630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "00592670",
      "DATA",
      [
        "storage",
        "00c6d230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592670",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059262c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-0059262c) · [`00592634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-00592634) · [`00592648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592614.md#insn-00592648)
- 新版 [`0059266c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-0059266c) · [`00592674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-00592674) · [`00592688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-00592688)

~~~diff
- 0059262c ["COPY", "tmp:0:8", ["const:230:8"]]
- 0059262c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059262c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059262c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059266c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 0059266c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059266c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059266c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059262c bytes 08c10891
+ 0059266c bytes 08010c91
- 00592634 ["INT_ADD", "register:40f0:8", ["const:592634:8", "const:4:8"]]
- 00592634 ["CALL", null, ["callee:005552c8:8"]]
+ 00592674 ["INT_ADD", "register:40f0:8", ["const:592674:8", "const:4:8"]]
+ 00592674 ["CALL", null, ["callee:005552c8:8"]]
- 00592634 bytes 150bff97
+ 00592674 bytes 150bff97
- 00592648 ["INT_ADD", "register:40f0:8", ["const:592648:8", "const:4:8"]]
- 00592648 ["CALL", null, ["callee:00c5a620:8"]]
+ 00592688 ["INT_ADD", "register:40f0:8", ["const:592688:8", "const:4:8"]]
+ 00592688 ["CALL", null, ["callee:00c5a620:8"]]
- 00592648 bytes c21f1b94
+ 00592688 bytes e61f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af701a13284c13dc836d7aeca8df5770"></a>

### [`0059265c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md) → [`0059269c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md) FUN_0059269c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a550.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a620.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005926b4",
      "incomplete_value": false,
      "site": "005926b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592674",
      "incomplete_value": false,
      "site": "00592678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "005926b8",
      "DATA",
      [
        "storage",
        "00c6d230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005926b8",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-00592674) · [`0059267c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-0059267c) · [`00592690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059265c.md#insn-00592690)
- 新版 [`005926b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926b4) · [`005926bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926bc) · [`005926d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926d0)

~~~diff
- 00592674 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00592674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005926b4 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 005926b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005926b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005926b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592674 bytes 08c10891
+ 005926b4 bytes 08010c91
- 0059267c ["INT_ADD", "register:40f0:8", ["const:59267c:8", "const:4:8"]]
- 0059267c ["CALL", null, ["callee:005552c8:8"]]
+ 005926bc ["INT_ADD", "register:40f0:8", ["const:5926bc:8", "const:4:8"]]
+ 005926bc ["CALL", null, ["callee:005552c8:8"]]
- 0059267c bytes 030bff97
+ 005926bc bytes 030bff97
- 00592690 ["INT_ADD", "register:40f0:8", ["const:592690:8", "const:4:8"]]
- 00592690 ["CALL", null, ["callee:00c5a620:8"]]
+ 005926d0 ["INT_ADD", "register:40f0:8", ["const:5926d0:8", "const:4:8"]]
+ 005926d0 ["CALL", null, ["callee:00c5a620:8"]]
- 00592690 bytes b01f1b94
+ 005926d0 bytes d41f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1c5b05add96e3cdb3b78d7c65bdefa"></a>

### [`0059284c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059284c.md) → [`0059288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059288c.md) FUN_0059288c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00592890",
      "incomplete_value": false,
      "site": "00592894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592850",
      "incomplete_value": false,
      "site": "00592854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "00592894",
      "DATA",
      [
        "storage",
        "00c6d298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592894",
      "DATA",
      [
        "storage",
        "00c6d368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059284c.md#insn-00592850)
- 新版 [`00592890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059288c.md#insn-00592890)

~~~diff
- 00592850 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00592850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592890 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00592890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592850 bytes 08610a91
+ 00592890 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-491b9cd9df12945ef89bbb99ad3447c0"></a>

### [`0059285c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md) → [`0059289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md) FUN_0059289c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005928ac",
      "incomplete_value": false,
      "site": "005928b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059286c",
      "incomplete_value": false,
      "site": "00592874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "005928b4",
      "DATA",
      [
        "storage",
        "00c6d298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005928b4",
      "DATA",
      [
        "storage",
        "00c6d368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059286c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md#insn-0059286c) · [`00592878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059285c.md#insn-00592878)
- 新版 [`005928ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md#insn-005928ac) · [`005928b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md#insn-005928b8)

~~~diff
- 0059286c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0059286c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059286c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059286c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005928ac ["COPY", "tmp:0:8", ["const:368:8"]]
+ 005928ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005928ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005928ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059286c bytes 08610a91
+ 005928ac bytes 08a10d91
- 00592878 ["INT_ADD", "register:40f0:8", ["const:592878:8", "const:4:8"]]
- 00592878 ["CALL", null, ["callee:00c57f70:8"]]
+ 005928b8 ["INT_ADD", "register:40f0:8", ["const:5928b8:8", "const:4:8"]]
+ 005928b8 ["CALL", null, ["callee:00c57f70:8"]]
- 00592878 bytes 8a151b94
+ 005928b8 bytes ae151b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6ceb5545d873daecf6eb7ac35c501e"></a>

### [`0059289c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md) → [`005928dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md) FUN_005928dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a560.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a630.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005928f4",
      "incomplete_value": false,
      "site": "005928f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005928b4",
      "incomplete_value": false,
      "site": "005928b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "005928f8",
      "DATA",
      [
        "storage",
        "00c6d2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005928f8",
      "DATA",
      [
        "storage",
        "00c6d3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005928b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928b4) · [`005928bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928bc) · [`005928d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/0059289c.md#insn-005928d0)
- 新版 [`005928f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-005928f4) · [`005928fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-005928fc) · [`00592910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-00592910)

~~~diff
- 005928b4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 005928b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005928b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005928b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005928f4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 005928f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005928f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005928f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005928b4 bytes 08a10b91
+ 005928f4 bytes 08e10e91
- 005928bc ["INT_ADD", "register:40f0:8", ["const:5928bc:8", "const:4:8"]]
- 005928bc ["CALL", null, ["callee:005552c8:8"]]
+ 005928fc ["INT_ADD", "register:40f0:8", ["const:5928fc:8", "const:4:8"]]
+ 005928fc ["CALL", null, ["callee:005552c8:8"]]
- 005928bc bytes 730aff97
+ 005928fc bytes 730aff97
- 005928d0 ["INT_ADD", "register:40f0:8", ["const:5928d0:8", "const:4:8"]]
- 005928d0 ["CALL", null, ["callee:00c5a630:8"]]
+ 00592910 ["INT_ADD", "register:40f0:8", ["const:592910:8", "const:4:8"]]
+ 00592910 ["CALL", null, ["callee:00c5a630:8"]]
- 005928d0 bytes 241f1b94
+ 00592910 bytes 481f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52e3843e1cd8ce01d60ecea7440fd754"></a>

### [`005928e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md) → [`00592924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md) FUN_00592924

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a560.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a630.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059293c",
      "incomplete_value": false,
      "site": "00592940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005928fc",
      "incomplete_value": false,
      "site": "00592900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "00592940",
      "DATA",
      [
        "storage",
        "00c6d2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592940",
      "DATA",
      [
        "storage",
        "00c6d3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005928fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-005928fc) · [`00592904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-00592904) · [`00592918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005928e4.md#insn-00592918)
- 新版 [`0059293c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-0059293c) · [`00592944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-00592944) · [`00592958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-00592958)

~~~diff
- 005928fc ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 005928fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005928fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005928fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059293c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0059293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005928fc bytes 08a10b91
+ 0059293c bytes 08e10e91
- 00592904 ["INT_ADD", "register:40f0:8", ["const:592904:8", "const:4:8"]]
- 00592904 ["CALL", null, ["callee:005552c8:8"]]
+ 00592944 ["INT_ADD", "register:40f0:8", ["const:592944:8", "const:4:8"]]
+ 00592944 ["CALL", null, ["callee:005552c8:8"]]
- 00592904 bytes 610aff97
+ 00592944 bytes 610aff97
- 00592918 ["INT_ADD", "register:40f0:8", ["const:592918:8", "const:4:8"]]
- 00592918 ["CALL", null, ["callee:00c5a630:8"]]
+ 00592958 ["INT_ADD", "register:40f0:8", ["const:592958:8", "const:4:8"]]
+ 00592958 ["CALL", null, ["callee:00c5a630:8"]]
- 00592918 bytes 121f1b94
+ 00592958 bytes 361f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d129553e1e658c4dd61c83be10d68ae"></a>

### [`00592978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592978.md) → [`005929b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929b8.md) FUN_005929b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005929bc",
      "incomplete_value": false,
      "site": "005929c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059297c",
      "incomplete_value": false,
      "site": "00592980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
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
      "005929c0",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929c0",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592978.md#insn-0059297c)
- 新版 [`005929bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929b8.md#insn-005929bc)

~~~diff
- 0059297c ["COPY", "tmp:0:8", ["const:350:8"]]
- 0059297c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059297c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059297c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929bc ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005929bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059297c bytes 08410d91
+ 005929bc bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb40796f9a58b2a16a760ddb6cbfdced"></a>

### [`00592988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md) → [`005929c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md) FUN_005929c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005929d8",
      "incomplete_value": false,
      "site": "005929e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592998",
      "incomplete_value": false,
      "site": "005929a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:350:8"
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
      "005929e0",
      "DATA",
      [
        "storage",
        "00c6d350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929e0",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md#insn-00592998) · [`005929a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592988.md#insn-005929a4)
- 新版 [`005929d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md#insn-005929d8) · [`005929e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md#insn-005929e4)

~~~diff
- 00592998 ["COPY", "tmp:0:8", ["const:350:8"]]
- 00592998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929d8 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005929d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592998 bytes 08410d91
+ 005929d8 bytes 08811091
- 005929a4 ["INT_ADD", "register:40f0:8", ["const:5929a4:8", "const:4:8"]]
- 005929a4 ["CALL", null, ["callee:00c57f70:8"]]
+ 005929e4 ["INT_ADD", "register:40f0:8", ["const:5929e4:8", "const:4:8"]]
+ 005929e4 ["CALL", null, ["callee:00c57f70:8"]]
- 005929a4 bytes 3f151b94
+ 005929e4 bytes 63151b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1fbb524d99a4eca7d89fb3ab1f56431"></a>

### [`005929c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md) → [`00592a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md) FUN_00592a08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c5a570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a570.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a640.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592a20",
      "incomplete_value": false,
      "site": "00592a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005929e0",
      "incomplete_value": false,
      "site": "005929e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "00592a24",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592a24",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005929e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929e0) · [`005929e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929e8) · [`005929fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/005929c8.md#insn-005929fc)
- 新版 [`00592a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a20) · [`00592a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a28) · [`00592a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a3c)

~~~diff
- 005929e0 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005929e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005929e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005929e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592a20 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 00592a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005929e0 bytes 08810e91
+ 00592a20 bytes 08c11191
- 005929e8 ["INT_ADD", "register:40f0:8", ["const:5929e8:8", "const:4:8"]]
- 005929e8 ["CALL", null, ["callee:005552c8:8"]]
+ 00592a28 ["INT_ADD", "register:40f0:8", ["const:592a28:8", "const:4:8"]]
+ 00592a28 ["CALL", null, ["callee:005552c8:8"]]
- 005929e8 bytes 280aff97
+ 00592a28 bytes 280aff97
- 005929fc ["INT_ADD", "register:40f0:8", ["const:5929fc:8", "const:4:8"]]
- 005929fc ["CALL", null, ["callee:00c5a640:8"]]
+ 00592a3c ["INT_ADD", "register:40f0:8", ["const:592a3c:8", "const:4:8"]]
+ 00592a3c ["CALL", null, ["callee:00c5a640:8"]]
- 005929fc bytes dd1e1b94
+ 00592a3c bytes 011f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95d47659bd6867166ab3db9c4fe796b2"></a>

### [`00592a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md) → [`00592a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md) FUN_00592a50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a570.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a640.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592a68",
      "incomplete_value": false,
      "site": "00592a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592a28",
      "incomplete_value": false,
      "site": "00592a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "00592a6c",
      "DATA",
      [
        "storage",
        "00c6d3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592a6c",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a28) · [`00592a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a30) · [`00592a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592a10.md#insn-00592a44)
- 新版 [`00592a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a68) · [`00592a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a70) · [`00592a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a84)

~~~diff
- 00592a28 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00592a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592a68 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 00592a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592a28 bytes 08810e91
+ 00592a68 bytes 08c11191
- 00592a30 ["INT_ADD", "register:40f0:8", ["const:592a30:8", "const:4:8"]]
- 00592a30 ["CALL", null, ["callee:005552c8:8"]]
+ 00592a70 ["INT_ADD", "register:40f0:8", ["const:592a70:8", "const:4:8"]]
+ 00592a70 ["CALL", null, ["callee:005552c8:8"]]
- 00592a30 bytes 160aff97
+ 00592a70 bytes 160aff97
- 00592a44 ["INT_ADD", "register:40f0:8", ["const:592a44:8", "const:4:8"]]
- 00592a44 ["CALL", null, ["callee:00c5a640:8"]]
+ 00592a84 ["INT_ADD", "register:40f0:8", ["const:592a84:8", "const:4:8"]]
+ 00592a84 ["CALL", null, ["callee:00c5a640:8"]]
- 00592a44 bytes cb1e1b94
+ 00592a84 bytes ef1e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63313b25bd5acab91584b0c8bc21db8b"></a>

### [`00592b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md) → [`00592bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md) FUN_00592bac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005916cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/005916cc.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a5b0.md)
- 新版 呼出元 1件 [`0059170c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059170c.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592bd4",
      "incomplete_value": false,
      "site": "00592bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592b94",
      "incomplete_value": false,
      "site": "00592bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592bf0",
      "incomplete_value": false,
      "site": "00592bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592bb0",
      "incomplete_value": false,
      "site": "00592bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00592bec",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592bf0",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592bec",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592bf0",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b84) · [`00592b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b94) · [`00592b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592b6c.md#insn-00592b98)
- 新版 [`00592bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md#insn-00592bc4) · [`00592bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md#insn-00592bd4)

~~~diff
- 00592b84 ["INT_ADD", "register:40f0:8", ["const:592b84:8", "const:4:8"]]
- 00592b84 ["CALL", null, ["callee:00c57f60:8"]]
+ 00592bc4 ["INT_ADD", "register:40f0:8", ["const:592bc4:8", "const:4:8"]]
+ 00592bc4 ["CALL", null, ["callee:00c57f60:8"]]
- 00592b84 bytes c3141b94
+ 00592bc4 bytes e7141b94
- 00592b94 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00592b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592bd4 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 00592bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592b94 bytes 08610f91
+ 00592bd4 bytes 08a11291
- 00592b98 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 00592b98 bytes c93600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-909bfb3b9490a6f88d619526902e96ac"></a>

### [`00592c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c14.md) → [`00592c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c54.md) FUN_00592c54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00592c58",
      "incomplete_value": false,
      "site": "00592c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c18",
      "incomplete_value": false,
      "site": "00592c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00592c5c",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c5c",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c14.md#insn-00592c18)
- 新版 [`00592c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c54.md#insn-00592c58)

~~~diff
- 00592c18 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00592c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c58 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 00592c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c18 bytes 08610f91
+ 00592c58 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f6e3ca274aea5c908be731e9ccc771"></a>

### [`00592c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md) → [`00592c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md) FUN_00592c64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592c74",
      "incomplete_value": false,
      "site": "00592c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c34",
      "incomplete_value": false,
      "site": "00592c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00592c7c",
      "DATA",
      [
        "storage",
        "00c6d3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c7c",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md#insn-00592c34) · [`00592c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592c24.md#insn-00592c40)
- 新版 [`00592c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md#insn-00592c74) · [`00592c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md#insn-00592c80)

~~~diff
- 00592c34 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00592c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c74 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 00592c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c34 bytes 08610f91
+ 00592c74 bytes 08a11291
- 00592c40 ["INT_ADD", "register:40f0:8", ["const:592c40:8", "const:4:8"]]
- 00592c40 ["CALL", null, ["callee:00c57f70:8"]]
+ 00592c80 ["INT_ADD", "register:40f0:8", ["const:592c80:8", "const:4:8"]]
+ 00592c80 ["CALL", null, ["callee:00c57f70:8"]]
- 00592c40 bytes 98141b94
+ 00592c80 bytes bc141b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08fef5c515d32192794d80480a85b91"></a>

### [`00592cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md) → [`00592cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md) FUN_00592cf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592d0c",
      "incomplete_value": false,
      "site": "00592d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ccc",
      "incomplete_value": false,
      "site": "00592cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00592d10",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d10",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592d10) · [`00592ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592ccc) · [`00592ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592cb4.md#insn-00592ce0)
- 新版 [`00592d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d50) · [`00592d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d0c) · [`00592d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d20)

~~~diff
- 00592d10 ["INT_ADD", "register:40f0:8", ["const:592d10:8", "const:4:8"]]
- 00592d10 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592d50 ["INT_ADD", "register:40f0:8", ["const:592d50:8", "const:4:8"]]
+ 00592d50 ["CALL", null, ["callee:00c53da0:8"]]
- 00592d10 bytes fc031b94
+ 00592d50 bytes 14041b94
- 00592ccc ["COPY", "tmp:0:8", ["const:428:8"]]
- 00592ccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592ccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592ccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d0c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00592d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592ccc bytes 08a11091
+ 00592d0c bytes 08e11391
- 00592ce0 ["INT_ADD", "register:40f0:8", ["const:592ce0:8", "const:4:8"]]
- 00592ce0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00592d20 ["INT_ADD", "register:40f0:8", ["const:592d20:8", "const:4:8"]]
+ 00592d20 ["CALL", null, ["callee:00c53da0:8"]]
- 00592ce0 bytes 08041b94
+ 00592d20 bytes 20041b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b5795456259b56504e233560d675e6"></a>

### [`00592d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md) → [`00592dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md) FUN_00592dc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592dd8",
      "incomplete_value": false,
      "site": "00592ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592d98",
      "incomplete_value": false,
      "site": "00592d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00592ddc",
      "DATA",
      [
        "storage",
        "00c6d428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592ddc",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592ddc) · [`00592d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592d98) · [`00592dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592d80.md#insn-00592dac)
- 新版 [`00592e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592e1c) · [`00592dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592dd8) · [`00592dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592dec)

~~~diff
- 00592ddc ["INT_ADD", "register:40f0:8", ["const:592ddc:8", "const:4:8"]]
- 00592ddc ["CALL", null, ["callee:00c53da0:8"]]
+ 00592e1c ["INT_ADD", "register:40f0:8", ["const:592e1c:8", "const:4:8"]]
+ 00592e1c ["CALL", null, ["callee:00c53da0:8"]]
- 00592ddc bytes c9031b94
+ 00592e1c bytes e1031b94
- 00592d98 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00592d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592dd8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00592dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592d98 bytes 08a11091
+ 00592dd8 bytes 08e11391
- 00592dac ["INT_ADD", "register:40f0:8", ["const:592dac:8", "const:4:8"]]
- 00592dac ["CALL", null, ["callee:00c53da0:8"]]
+ 00592dec ["INT_ADD", "register:40f0:8", ["const:592dec:8", "const:4:8"]]
+ 00592dec ["CALL", null, ["callee:00c53da0:8"]]
- 00592dac bytes d5031b94
+ 00592dec bytes ed031b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a1ef011d6014d0c132d927f4de9863a"></a>

### [`00592fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md) → [`00592ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md) FUN_00592ff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593030",
      "incomplete_value": false,
      "site": "00593044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ff0",
      "incomplete_value": false,
      "site": "00593004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "definition_site": "00593038",
      "incomplete_value": false,
      "site": "00593044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592ff8",
      "incomplete_value": false,
      "site": "00593004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "00593030",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593038",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00593030",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593038",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00593004) · [`00592ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00592ff0) · [`00592ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00592/00592fb8.md#insn-00592ff8)
- 新版 [`00593044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-00593044) · [`00593030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-00593030) · [`00593038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-00593038)

~~~diff
- 00593004 ["INT_ADD", "register:40f0:8", ["const:593004:8", "const:4:8"]]
- 00593004 ["CALL", null, ["callee:00c586e0:8"]]
+ 00593044 ["INT_ADD", "register:40f0:8", ["const:593044:8", "const:4:8"]]
+ 00593044 ["CALL", null, ["callee:00c586e0:8"]]
- 00593004 bytes 83151b94
+ 00593044 bytes a7151b94
- 00592ff0 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00592ff0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00592ff0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00592ff0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00593030 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00593030 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00593030 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00593030 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00592ff0 bytes 21800491
+ 00593030 bytes 21c00791
- 00592ff8 ["COPY", "tmp:0:8", ["const:130:8"]]
- 00592ff8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00592ff8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00592ff8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00593038 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 00593038 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00593038 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00593038 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00592ff8 bytes 42c00491
+ 00593038 bytes 42000891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d77b97ca9d5ffcb6a31e6918facddfd"></a>

### [`00593174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md) → [`005931b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md) FUN_005931b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ed0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005931f4",
      "incomplete_value": true,
      "site": "00593200",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005931b4",
      "incomplete_value": true,
      "site": "005931c0",
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
            "const:130:8"
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
      "005931ec",
      "PARAM",
      [
        "storage",
        "00c6d120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005931f4",
      "PARAM",
      [
        "storage",
        "00c6d130",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005931ec",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005931f4",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005931c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931c0) · [`005931ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931ac) · [`005931b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593174.md#insn-005931b4)
- 新版 [`00593200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-00593200) · [`005931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-005931ec) · [`005931f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-005931f4)

~~~diff
- 005931c0 ["INT_ADD", "register:40f0:8", ["const:5931c0:8", "const:4:8"]]
- 005931c0 ["CALL", null, ["callee:00c586e0:8"]]
+ 00593200 ["INT_ADD", "register:40f0:8", ["const:593200:8", "const:4:8"]]
+ 00593200 ["CALL", null, ["callee:00c586e0:8"]]
- 005931c0 bytes 14151b94
+ 00593200 bytes 38151b94
- 005931ac ["COPY", "tmp:0:8", ["const:120:8"]]
- 005931ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005931ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005931ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005931ec ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 005931ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005931ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005931ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005931ac bytes 21800491
+ 005931ec bytes 21c00791
- 005931b4 ["COPY", "tmp:0:8", ["const:130:8"]]
- 005931b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005931b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005931b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005931f4 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 005931f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005931f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005931f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005931b4 bytes 42c00491
+ 005931f4 bytes 42000891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103df173422bb46fec9bc45bc3b39389"></a>

### [`00593330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593330.md) → [`00593370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593370.md) FUN_00593370

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00593374",
      "incomplete_value": false,
      "site": "00593378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593334",
      "incomplete_value": false,
      "site": "00593338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "00593378",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593378",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593330.md#insn-00593334)
- 新版 [`00593374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593370.md#insn-00593374)

~~~diff
- 00593334 ["COPY", "tmp:0:8", ["const:460:8"]]
- 00593334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593374 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00593374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593334 bytes 08811191
+ 00593374 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe907aff4ff024cc7b15f55d60353ba"></a>

### [`00593340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md) → [`00593380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md) FUN_00593380

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593390",
      "incomplete_value": false,
      "site": "00593398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593350",
      "incomplete_value": false,
      "site": "00593358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "00593398",
      "DATA",
      [
        "storage",
        "00c6d460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593398",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md#insn-00593350) · [`0059335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593340.md#insn-0059335c)
- 新版 [`00593390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md#insn-00593390) · [`0059339c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md#insn-0059339c)

~~~diff
- 00593350 ["COPY", "tmp:0:8", ["const:460:8"]]
- 00593350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593390 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00593390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593350 bytes 08811191
+ 00593390 bytes 08c11491
- 0059335c ["INT_ADD", "register:40f0:8", ["const:59335c:8", "const:4:8"]]
- 0059335c ["CALL", null, ["callee:00c57f70:8"]]
+ 0059339c ["INT_ADD", "register:40f0:8", ["const:59339c:8", "const:4:8"]]
+ 0059339c ["CALL", null, ["callee:00c57f70:8"]]
- 0059335c bytes d1121b94
+ 0059339c bytes f5121b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b340eaf1294b5c83f801bdec5304a215"></a>

### [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) → [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) FUN_005933c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md) [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`005937c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/005937c4.md)
- 新版 呼出元 1件 [`00593ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md) · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00593804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593804.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593400",
      "incomplete_value": false,
      "site": "00593404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005933c0",
      "incomplete_value": false,
      "site": "005933c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "00593404",
      "DATA",
      [
        "storage",
        "00c6d4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593404",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005933c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-005933c0) · [`005933c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-005933c8) · [`0059341c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md#insn-0059341c)
- 新版 [`00593400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-00593400) · [`00593408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-00593408) · [`0059345c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-0059345c)

~~~diff
- 005933c0 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 005933c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005933c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005933c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593400 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00593400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005933c0 bytes 08c11291
+ 00593400 bytes 08011691
- 005933c8 ["INT_ADD", "register:40f0:8", ["const:5933c8:8", "const:4:8"]]
- 005933c8 ["CALL", null, ["callee:005552c8:8"]]
+ 00593408 ["INT_ADD", "register:40f0:8", ["const:593408:8", "const:4:8"]]
+ 00593408 ["CALL", null, ["callee:005552c8:8"]]
- 005933c8 bytes b007ff97
+ 00593408 bytes b007ff97
- 0059341c ["INT_ADD", "register:40f0:8", ["const:59341c:8", "const:4:8"]]
- 0059341c ["CALL", null, ["callee:0043bb60:8"]]
+ 0059345c ["INT_ADD", "register:40f0:8", ["const:59345c:8", "const:4:8"]]
+ 0059345c ["CALL", null, ["callee:0043bb60:8"]]
- 0059341c bytes c1a1fa97
+ 0059345c bytes c1a1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de260cd843e4389d4f199aeab27969bd"></a>

### [`00593ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md) → [`00593ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md) FUN_00593ce4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059125c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00591/0059125c.md) · 呼出先 21件 [`00593380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593380.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0059129c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md) · 呼出先 21件 [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005941d0",
      "incomplete_value": false,
      "site": "005941dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594190",
      "incomplete_value": false,
      "site": "0059419c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593dd0",
      "incomplete_value": false,
      "site": "00593ddc",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593d90",
      "incomplete_value": false,
      "site": "00593d9c",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593dfc",
      "incomplete_value": false,
      "site": "00593e04",
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
    "old": {
      "definition_site": "00593dbc",
      "incomplete_value": false,
      "site": "00593dc4",
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
            "const:be0:8"
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
      "00593dd0",
      "PARAM",
      [
        "storage",
        "002b6228",
        null,
        "string"
      ]
    ],
    [
      "00593dfc",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ],
    [
      "00593f14",
      "PARAM",
      [
        "storage",
        "002a023a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00593dd0",
      "PARAM",
      [
        "storage",
        "002b6268",
        null,
        "string"
      ]
    ],
    [
      "00593dfc",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ],
    [
      "00593f14",
      "PARAM",
      [
        "storage",
        "002a01ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593d9c) · [`00593dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593dc4) · [`00593ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00593/00593ca4.md#insn-00593ee0)
- 新版 [`00593ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593ddc) · [`00593e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593e04) · [`00593f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593f20)

~~~diff
- 00593d9c ["INT_ADD", "register:40f0:8", ["const:593d9c:8", "const:4:8"]]
- 00593d9c ["CALL", null, ["callee:00c58030:8"]]
+ 00593ddc ["INT_ADD", "register:40f0:8", ["const:593ddc:8", "const:4:8"]]
+ 00593ddc ["CALL", null, ["callee:00c58030:8"]]
- 00593d9c bytes 71101b94
+ 00593ddc bytes 95101b94
- 00593dc4 ["INT_ADD", "register:40f0:8", ["const:593dc4:8", "const:4:8"]]
- 00593dc4 ["CALL", null, ["callee:00c58040:8"]]
+ 00593e04 ["INT_ADD", "register:40f0:8", ["const:593e04:8", "const:4:8"]]
+ 00593e04 ["CALL", null, ["callee:00c58040:8"]]
- 00593dc4 bytes 6b101b94
+ 00593e04 bytes 8f101b94
- 00593ee0 ["INT_ADD", "register:40f0:8", ["const:593ee0:8", "const:4:8"]]
- 00593ee0 ["CALL", null, ["callee:00c58030:8"]]
+ 00593f20 ["INT_ADD", "register:40f0:8", ["const:593f20:8", "const:4:8"]]
+ 00593f20 ["CALL", null, ["callee:00c58030:8"]]
- 00593ee0 bytes 20101b94
+ 00593f20 bytes 44101b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6b0a719c91041aad99be359c77d816"></a>

### [`005948a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948a0.md) → [`005948e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948e0.md) FUN_005948e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005948e4",
      "incomplete_value": false,
      "site": "005948e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005948a4",
      "incomplete_value": false,
      "site": "005948a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "005948e8",
      "DATA",
      [
        "storage",
        "00c6d508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005948e8",
      "DATA",
      [
        "storage",
        "00c6d5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948a0.md#insn-005948a4)
- 新版 [`005948e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948e0.md#insn-005948e4)

~~~diff
- 005948a4 ["COPY", "tmp:0:8", ["const:508:8"]]
- 005948a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005948a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005948a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005948e4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 005948e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005948e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005948e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005948a4 bytes 08211491
+ 005948e4 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe08ca4068175a3b9b2d5cd931f01f8"></a>

### [`005948b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md) → [`005948f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md) FUN_005948f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594900",
      "incomplete_value": false,
      "site": "00594908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005948c0",
      "incomplete_value": false,
      "site": "005948c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "00594908",
      "DATA",
      [
        "storage",
        "00c6d508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594908",
      "DATA",
      [
        "storage",
        "00c6d5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md#insn-005948c0) · [`005948cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948b0.md#insn-005948cc)
- 新版 [`00594900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md#insn-00594900) · [`0059490c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md#insn-0059490c)

~~~diff
- 005948c0 ["COPY", "tmp:0:8", ["const:508:8"]]
- 005948c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005948c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005948c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594900 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00594900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005948c0 bytes 08211491
+ 00594900 bytes 08611791
- 005948cc ["INT_ADD", "register:40f0:8", ["const:5948cc:8", "const:4:8"]]
- 005948cc ["CALL", null, ["callee:00c57f70:8"]]
+ 0059490c ["INT_ADD", "register:40f0:8", ["const:59490c:8", "const:4:8"]]
+ 0059490c ["CALL", null, ["callee:00c57f70:8"]]
- 005948cc bytes 750d1b94
+ 0059490c bytes 990d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd67593af2d99ecc77cc5c548d644f5"></a>

### [`005948e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md) → [`00594920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md) FUN_00594920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00555288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555288.md) [`00594340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594340.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a640.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00594380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a710.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594934",
      "incomplete_value": false,
      "site": "00594938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005948f4",
      "incomplete_value": false,
      "site": "005948f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "00594938",
      "DATA",
      [
        "storage",
        "00c6d4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594938",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-005948f4) · [`005948fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-005948fc) · [`00594908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/005948e0.md#insn-00594908)
- 新版 [`00594934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-00594934) · [`0059493c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-0059493c) · [`00594948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-00594948)

~~~diff
- 005948f4 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 005948f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005948f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005948f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594934 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00594934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005948f4 bytes 08c11291
+ 00594934 bytes 08011691
- 005948fc ["INT_ADD", "register:40f0:8", ["const:5948fc:8", "const:4:8"]]
- 005948fc ["CALL", null, ["callee:005552c8:8"]]
+ 0059493c ["INT_ADD", "register:40f0:8", ["const:59493c:8", "const:4:8"]]
+ 0059493c ["CALL", null, ["callee:005552c8:8"]]
- 005948fc bytes 6302ff97
+ 0059493c bytes 6302ff97
- 00594908 ["INT_ADD", "register:40f0:8", ["const:594908:8", "const:4:8"]]
- 00594908 ["CALL", null, ["callee:00c5a710:8"]]
+ 00594948 ["INT_ADD", "register:40f0:8", ["const:594948:8", "const:4:8"]]
+ 00594948 ["CALL", null, ["callee:00c5a710:8"]]
- 00594908 bytes 4e171b94
+ 00594948 bytes 72171b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63bf6ded9d7f507a602b5b8ea47a1162"></a>

### [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) → [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) FUN_00594978

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005884c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00588508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005949ac",
      "incomplete_value": false,
      "site": "005949bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059496c",
      "incomplete_value": false,
      "site": "0059497c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "definition_site": "00594ae0",
      "incomplete_value": true,
      "site": "00594aec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594aa0",
      "incomplete_value": true,
      "site": "00594aac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d38:8"
              ]
            ]
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
      "005949bc",
      "DATA",
      [
        "storage",
        "00c6d558",
        null,
        "undefined *"
      ]
    ],
    [
      "00594ae0",
      "READ",
      [
        "storage",
        "002c3d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005949bc",
      "DATA",
      [
        "storage",
        "00c6d628",
        null,
        "undefined *"
      ]
    ],
    [
      "00594ae0",
      "READ",
      [
        "storage",
        "002c3d78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-0059496c) · [`005949a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-005949a0) · [`005949b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md#insn-005949b8)
- 新版 [`005949ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949ac) · [`005949e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949e0) · [`005949f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949f8)

~~~diff
- 0059496c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0059496c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059496c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059496c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005949ac ["COPY", "tmp:0:8", ["const:628:8"]]
+ 005949ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005949ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005949ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059496c bytes 29611591
+ 005949ac bytes 29a11891
- 005949a0 ["INT_ADD", "register:40f0:8", ["const:5949a0:8", "const:4:8"]]
- 005949a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005949e0 ["INT_ADD", "register:40f0:8", ["const:5949e0:8", "const:4:8"]]
+ 005949e0 ["CALL", null, ["callee:00c57f60:8"]]
- 005949a0 bytes 3c0d1b94
+ 005949e0 bytes 600d1b94
- 005949b8 ["INT_ADD", "register:40f0:8", ["const:5949b8:8", "const:4:8"]]
- 005949b8 ["CALL", null, ["callee:00c58160:8"]]
+ 005949f8 ["INT_ADD", "register:40f0:8", ["const:5949f8:8", "const:4:8"]]
+ 005949f8 ["CALL", null, ["callee:00c58160:8"]]
- 005949b8 bytes b60d1b94
+ 005949f8 bytes da0d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014111de9a01f991bfd1f04addf40725"></a>

### [`00594b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md) → [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) FUN_00594bac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) · 呼出先 12件 [`0055f4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f4c4.md) [`0055f52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f52c.md) [`0055f540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f540.md) [`0055f560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f560.md) [`00595190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595190.md)
- 新版 呼出元 1件 [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) · 呼出先 12件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f56c.md) [`0055f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f580.md) [`0055f5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5a0.md) [`005951d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005951d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.23% / 新版 97.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00594d34",
      "incomplete_value": true,
      "site": "00594d44",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b03:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594cf4",
      "incomplete_value": true,
      "site": "00594d04",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b5f:8"
              ]
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
      "00594d34",
      "READ",
      [
        "storage",
        "002afb5f",
        null,
        "string"
      ]
    ],
    [
      "00594d38",
      "READ",
      [
        "storage",
        "002afb6a",
        null,
        "string"
      ]
    ],
    [
      "00594d3c",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00594d34",
      "READ",
      [
        "storage",
        "002afb03",
        null,
        "string"
      ]
    ],
    [
      "00594d38",
      "READ",
      [
        "storage",
        "002afb0e",
        null,
        "string"
      ]
    ],
    [
      "00594d3c",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594d44) · [`00594bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594bc0) · [`00594bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594b6c.md#insn-00594bdc)
- 新版 [`00594d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594d84) · [`00594c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594c00) · [`00594c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594c1c)

~~~diff
- 00594d44 ["INT_ADD", "register:40f0:8", ["const:594d44:8", "const:4:8"]]
- 00594d44 ["CALL", null, ["callee:00595210:8"]]
+ 00594d84 ["INT_ADD", "register:40f0:8", ["const:594d84:8", "const:4:8"]]
+ 00594d84 ["CALL", null, ["callee:00595210:8"]]
- 00594d44 bytes 23010094
+ 00594d84 bytes 23010094
- 00594bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00594bc0 ["INT_ADD", "register:40f0:8", ["const:594bc0:8", "const:4:8"]]
- 00594bc0 ["CALLIND", null, ["register:0:8"]]
+ 00594c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00594c00 ["INT_ADD", "register:40f0:8", ["const:594c00:8", "const:4:8"]]
+ 00594c00 ["CALLIND", null, ["register:0:8"]]
- 00594bc0 bytes 00013fd6
+ 00594c00 bytes 00013fd6
- 00594bdc ["COPY", "register:0:8", ["register:4048:8"]]
- 00594bdc ["INT_ADD", "register:40f0:8", ["const:594bdc:8", "const:4:8"]]
- 00594bdc ["CALLIND", null, ["register:0:8"]]
+ 00594c1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00594c1c ["INT_ADD", "register:40f0:8", ["const:594c1c:8", "const:4:8"]]
+ 00594c1c ["CALLIND", null, ["register:0:8"]]
- 00594bdc bytes 20013fd6
+ 00594c1c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d914a7d2433960dd14e07a25949267c"></a>

### [`00594fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md) → [`00594ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md) FUN_00594ff8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058859c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005885dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885dc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00595010",
      "incomplete_value": false,
      "site": "00595014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594fd0",
      "incomplete_value": false,
      "site": "00594fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "00595014",
      "DATA",
      [
        "storage",
        "00c6d558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595014",
      "DATA",
      [
        "storage",
        "00c6d628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00595014) · [`00594fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00594fd0) · [`00594fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594fb8.md#insn-00594fe0)
- 新版 [`00595054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-00595054) · [`00595010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-00595010) · [`00595020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-00595020)

~~~diff
- 00595014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00595014 ["INT_ADD", "register:40f0:8", ["const:595014:8", "const:4:8"]]
- 00595014 ["CALLIND", null, ["register:0:8"]]
+ 00595054 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595054 ["INT_ADD", "register:40f0:8", ["const:595054:8", "const:4:8"]]
+ 00595054 ["CALLIND", null, ["register:0:8"]]
- 00595014 bytes 00013fd6
+ 00595054 bytes 00013fd6
- 00594fd0 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00594fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595010 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 00595010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594fd0 bytes 08611591
+ 00595010 bytes 08a11891
- 00594fe0 ["INT_ADD", "register:40f0:8", ["const:594fe0:8", "const:4:8"]]
- 00594fe0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00595020 ["INT_ADD", "register:40f0:8", ["const:595020:8", "const:4:8"]]
+ 00595020 ["CALL", null, ["callee:00c57f80:8"]]
- 00594fe0 bytes b40b1b94
+ 00595020 bytes d80b1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d819cf691404bdb72d746abb36c95b34"></a>

### [`0059536c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md) → [`005953ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md) FUN_005953ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595484",
      "incomplete_value": false,
      "site": "00595488",
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
            "const:622:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595444",
      "incomplete_value": false,
      "site": "00595448",
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
            "const:67e:8"
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
      "definition_site": "005954b4",
      "incomplete_value": false,
      "site": "005954b8",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595474",
      "incomplete_value": false,
      "site": "00595478",
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
            "const:3ea:8"
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
      "00595424",
      "PARAM",
      [
        "storage",
        "002ae6fa",
        null,
        null
      ]
    ],
    [
      "00595424",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ],
    [
      "00595484",
      "PARAM",
      [
        "storage",
        "002a767e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00595424",
      "PARAM",
      [
        "storage",
        "002ae69e",
        null,
        null
      ]
    ],
    [
      "00595424",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ],
    [
      "00595484",
      "PARAM",
      [
        "storage",
        "002a7622",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-00595448) · [`00595478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-00595478) · [`005953d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059536c.md#insn-005953d0)
- 新版 [`00595488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-00595488) · [`005954b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-005954b8) · [`00595410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-00595410)

~~~diff
- 00595448 ["INT_ADD", "register:40f0:8", ["const:595448:8", "const:4:8"]]
- 00595448 ["CALL", null, ["callee:00c580b0:8"]]
+ 00595488 ["INT_ADD", "register:40f0:8", ["const:595488:8", "const:4:8"]]
+ 00595488 ["CALL", null, ["callee:00c580b0:8"]]
- 00595448 bytes e60a1b94
+ 00595488 bytes 0a0b1b94
- 00595478 ["INT_ADD", "register:40f0:8", ["const:595478:8", "const:4:8"]]
- 00595478 ["CALL", null, ["callee:00c580b0:8"]]
+ 005954b8 ["INT_ADD", "register:40f0:8", ["const:5954b8:8", "const:4:8"]]
+ 005954b8 ["CALL", null, ["callee:00c580b0:8"]]
- 00595478 bytes da0a1b94
+ 005954b8 bytes fe0a1b94
- 005953d0 ["COPY", "tmp:0:8", ["const:6fa:8"]]
- 005953d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005953d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005953d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00595410 ["COPY", "tmp:0:8", ["const:69e:8"]]
+ 00595410 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00595410 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00595410 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005953d0 bytes 29e91b91
+ 00595410 bytes 29791a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9df339d80bea3860ff3db477fbd9ee"></a>

### [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) → [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) FUN_005955c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) · 呼出先 2件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) · 呼出先 2件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005955d4",
      "incomplete_value": false,
      "site": "005955dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595594",
      "incomplete_value": false,
      "site": "0059559c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "005955dc",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005955dc",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-00595594) · [`005955c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-005955c4) · [`005955d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md#insn-005955d8)
- 新版 [`005955d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-005955d4) · [`00595604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-00595604) · [`00595618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-00595618)

~~~diff
- 00595594 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00595594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005955d4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 005955d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005955d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005955d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595594 bytes 08a11791
+ 005955d4 bytes 08e11a91
- 005955c4 ["INT_ADD", "register:40f0:8", ["const:5955c4:8", "const:4:8"]]
- 005955c4 ["CALL", null, ["callee:00c53d70:8"]]
+ 00595604 ["INT_ADD", "register:40f0:8", ["const:595604:8", "const:4:8"]]
+ 00595604 ["CALL", null, ["callee:00c53d70:8"]]
- 005955c4 bytes c3f91a94
+ 00595604 bytes dbf91a94
- 005955d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005955d8 ["INT_ADD", "register:40f0:8", ["const:5955d8:8", "const:4:8"]]
- 005955d8 ["CALLIND", null, ["register:0:8"]]
+ 00595618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595618 ["INT_ADD", "register:40f0:8", ["const:595618:8", "const:4:8"]]
+ 00595618 ["CALLIND", null, ["register:0:8"]]
- 005955d8 bytes 00013fd6
+ 00595618 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841b812f23000dc063193bd51b0c6fca"></a>

### [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) → [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) FUN_005956cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) · 呼出先 4件 [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) · 呼出先 4件 [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595720",
      "incomplete_value": false,
      "site": "00595724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005956e0",
      "incomplete_value": false,
      "site": "005956e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595774",
      "incomplete_value": false,
      "site": "00595778",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595734",
      "incomplete_value": false,
      "site": "00595738",
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
            "const:ae0:8"
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
      "00595724",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595778",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00595724",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00595778",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005956a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956a8) · [`005956c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956c8) · [`005956e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md#insn-005956e0)
- 新版 [`005956e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-005956e8) · [`00595708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-00595708) · [`00595720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-00595720)

~~~diff
- 005956a8 ["INT_ADD", "register:40f0:8", ["const:5956a8:8", "const:4:8"]]
- 005956a8 ["CALL", null, ["callee:005958b0:8"]]
+ 005956e8 ["INT_ADD", "register:40f0:8", ["const:5956e8:8", "const:4:8"]]
+ 005956e8 ["CALL", null, ["callee:005958b0:8"]]
- 005956a8 bytes 72000094
+ 005956e8 bytes 72000094
- 005956c8 ["INT_ADD", "register:40f0:8", ["const:5956c8:8", "const:4:8"]]
- 005956c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00595708 ["INT_ADD", "register:40f0:8", ["const:595708:8", "const:4:8"]]
+ 00595708 ["CALL", null, ["callee:00c57f60:8"]]
- 005956c8 bytes f2091b94
+ 00595708 bytes 160a1b94
- 005956e0 ["COPY", "tmp:0:8", ["const:678:8"]]
- 005956e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005956e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005956e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595720 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00595720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005956e0 bytes 08e11991
+ 00595720 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e17296742017612e207ad0ffffce6a"></a>

### [`00595784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md) → [`005957c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md) FUN_005957c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005957dc",
      "incomplete_value": false,
      "site": "005957e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059579c",
      "incomplete_value": false,
      "site": "005957a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "005957e4",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005957e4",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059579c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-0059579c) · [`005957b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-005957b4) · [`005957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595784.md#insn-005957c8)
- 新版 [`005957dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-005957dc) · [`005957f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-005957f4) · [`00595808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-00595808)

~~~diff
- 0059579c ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 0059579c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059579c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059579c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005957dc ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 005957dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005957dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005957dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059579c bytes 08a11791
+ 005957dc bytes 08e11a91
- 005957b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005957b4 ["INT_ADD", "register:40f0:8", ["const:5957b4:8", "const:4:8"]]
- 005957b4 ["CALLIND", null, ["register:0:8"]]
+ 005957f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005957f4 ["INT_ADD", "register:40f0:8", ["const:5957f4:8", "const:4:8"]]
+ 005957f4 ["CALLIND", null, ["register:0:8"]]
- 005957b4 bytes 00013fd6
+ 005957f4 bytes 00013fd6
- 005957c8 ["INT_ADD", "register:40f0:8", ["const:5957c8:8", "const:4:8"]]
- 005957c8 ["CALL", null, ["callee:00c53da0:8"]]
+ 00595808 ["INT_ADD", "register:40f0:8", ["const:595808:8", "const:4:8"]]
+ 00595808 ["CALL", null, ["callee:00c53da0:8"]]
- 005957c8 bytes 4ef91a94
+ 00595808 bytes 66f91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118f57eff200e0844c45267b4ad1dea8"></a>

### [`005957fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md) → [`0059583c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md) FUN_0059583c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595854",
      "incomplete_value": false,
      "site": "0059585c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595814",
      "incomplete_value": false,
      "site": "0059581c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "0059585c",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059585c",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-0059585c) · [`00595814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-00595814) · [`0059582c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005957fc.md#insn-0059582c)
- 新版 [`0059589c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-0059589c) · [`00595854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-00595854) · [`0059586c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-0059586c)

~~~diff
- 0059585c ["INT_ADD", "register:40f0:8", ["const:59585c:8", "const:4:8"]]
- 0059585c ["CALL", null, ["callee:00c57f50:8"]]
+ 0059589c ["INT_ADD", "register:40f0:8", ["const:59589c:8", "const:4:8"]]
+ 0059589c ["CALL", null, ["callee:00c57f50:8"]]
- 0059585c bytes 89091b94
+ 0059589c bytes ad091b94
- 00595814 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00595814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595854 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00595854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595814 bytes 08a11791
+ 00595854 bytes 08e11a91
- 0059582c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059582c ["INT_ADD", "register:40f0:8", ["const:59582c:8", "const:4:8"]]
- 0059582c ["CALLIND", null, ["register:0:8"]]
+ 0059586c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059586c ["INT_ADD", "register:40f0:8", ["const:59586c:8", "const:4:8"]]
+ 0059586c ["CALLIND", null, ["register:0:8"]]
- 0059582c bytes 00013fd6
+ 0059586c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eef1cb06e2b580688990fc04f985494f"></a>

### [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) → [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) FUN_00595a1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md)
- 新版 呼出元 3件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595ab4",
      "incomplete_value": false,
      "site": "00595ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595a74",
      "incomplete_value": false,
      "site": "00595a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "definition_site": "00595b48",
      "incomplete_value": false,
      "site": "00595b4c",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595b08",
      "incomplete_value": false,
      "site": "00595b0c",
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
            "const:ae0:8"
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
      "definition_site": "00595cd8",
      "incomplete_value": true,
      "site": "00595cdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595c98",
      "incomplete_value": true,
      "site": "00595c9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
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
      "00595ab8",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595b4c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "00595c9c",
      "READ",
      [
        "storage",
        "00c63ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595ab8",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00595b4c",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "00595c9c",
      "READ",
      [
        "storage",
        "00c63bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595c9c) · [`00595cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595cdc) · [`00595a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md#insn-00595a00)
- 新版 [`00595cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595cdc) · [`00595d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595d1c) · [`00595a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595a40)

~~~diff
- 00595c9c ["INT_ADD", "register:40f0:8", ["const:595c9c:8", "const:4:8"]]
- 00595c9c ["CALL", null, ["callee:00459510:8"]]
+ 00595cdc ["INT_ADD", "register:40f0:8", ["const:595cdc:8", "const:4:8"]]
+ 00595cdc ["CALL", null, ["callee:00459510:8"]]
- 00595c9c bytes 0d0efb97
+ 00595cdc bytes 0d0efb97
- 00595cdc ["INT_ADD", "register:40f0:8", ["const:595cdc:8", "const:4:8"]]
- 00595cdc ["CALL", null, ["callee:00440f00:8"]]
+ 00595d1c ["INT_ADD", "register:40f0:8", ["const:595d1c:8", "const:4:8"]]
+ 00595d1c ["CALL", null, ["callee:00440f00:8"]]
- 00595cdc bytes 79acfa97
+ 00595d1c bytes 79acfa97
- 00595a00 ["INT_ADD", "register:40f0:8", ["const:595a00:8", "const:4:8"]]
- 00595a00 ["CALL", null, ["callee:005958b0:8"]]
+ 00595a40 ["INT_ADD", "register:40f0:8", ["const:595a40:8", "const:4:8"]]
+ 00595a40 ["CALL", null, ["callee:005958b0:8"]]
- 00595a00 bytes 9cffff97
+ 00595a40 bytes 9cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f056402260636231f9b4f725deb2305"></a>

### [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) → [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) FUN_00595d5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 15件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md)
- 新版 呼出元 3件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 15件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.46% / 新版 93.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596024",
      "incomplete_value": true,
      "site": "00596028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595fe4",
      "incomplete_value": true,
      "site": "00595fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059607c",
      "incomplete_value": false,
      "site": "00596080",
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
            "const:69a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059603c",
      "incomplete_value": false,
      "site": "00596040",
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
            "const:6f6:8"
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
      "definition_site": "00596090",
      "incomplete_value": true,
      "site": "00596094",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596050",
      "incomplete_value": true,
      "site": "00596054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
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
      "00595e3c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "00595ec0",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00595f84",
      "READ",
      [
        "storage",
        "00c63ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595e3c",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "00595ec0",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00595f84",
      "READ",
      [
        "storage",
        "00c63bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00595fe8) · [`00596040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00596040) · [`00596054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md#insn-00596054)
- 新版 [`00596028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596028) · [`00596080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596080) · [`00596094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596094)

~~~diff
- 00595fe8 ["INT_ADD", "register:40f0:8", ["const:595fe8:8", "const:4:8"]]
- 00595fe8 ["CALL", null, ["callee:00459510:8"]]
+ 00596028 ["INT_ADD", "register:40f0:8", ["const:596028:8", "const:4:8"]]
+ 00596028 ["CALL", null, ["callee:00459510:8"]]
- 00595fe8 bytes 3a0dfb97
+ 00596028 bytes 3a0dfb97
- 00596040 ["INT_ADD", "register:40f0:8", ["const:596040:8", "const:4:8"]]
- 00596040 ["CALL", null, ["callee:00c580b0:8"]]
+ 00596080 ["INT_ADD", "register:40f0:8", ["const:596080:8", "const:4:8"]]
+ 00596080 ["CALL", null, ["callee:00c580b0:8"]]
- 00596040 bytes e8071b94
+ 00596080 bytes 0c081b94
- 00596054 ["INT_ADD", "register:40f0:8", ["const:596054:8", "const:4:8"]]
- 00596054 ["CALL", null, ["callee:00459510:8"]]
+ 00596094 ["INT_ADD", "register:40f0:8", ["const:596094:8", "const:4:8"]]
+ 00596094 ["CALL", null, ["callee:00459510:8"]]
- 00596054 bytes 1f0dfb97
+ 00596094 bytes 1f0dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca71e9f3ee892690226885f46217ec1a"></a>

### [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) → [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) FUN_00596134

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 3件 [`005964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md) [`00596838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 3件 [`005964e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md) [`00596878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596198",
      "incomplete_value": false,
      "site": "005961a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596158",
      "incomplete_value": false,
      "site": "00596160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005961c0",
      "incomplete_value": false,
      "site": "005961c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596180",
      "incomplete_value": false,
      "site": "00596188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "005961a0",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "005961c8",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "005961f4",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005961a0",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "005961c8",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "005961f4",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005961a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-005961a0) · [`00596150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-00596150) · [`00596158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md#insn-00596158)
- 新版 [`005961e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-005961e0) · [`00596190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-00596190) · [`00596198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-00596198)

~~~diff
- 005961a0 ["INT_ADD", "register:40f0:8", ["const:5961a0:8", "const:4:8"]]
- 005961a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005961e0 ["INT_ADD", "register:40f0:8", ["const:5961e0:8", "const:4:8"]]
+ 005961e0 ["CALL", null, ["callee:00c57f60:8"]]
- 005961a0 bytes 3c071b94
+ 005961e0 bytes 60071b94
- 00596150 ["INT_ADD", "register:40f0:8", ["const:596150:8", "const:4:8"]]
- 00596150 ["CALL", null, ["callee:00c57f60:8"]]
+ 00596190 ["INT_ADD", "register:40f0:8", ["const:596190:8", "const:4:8"]]
+ 00596190 ["CALL", null, ["callee:00c57f60:8"]]
- 00596150 bytes 50071b94
+ 00596190 bytes 74071b94
- 00596158 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00596158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596198 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00596198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596158 bytes 08211891
+ 00596198 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac4577fdd6f8c70e8eded5b4fd0c8ce"></a>

### [`005964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md) → [`005964e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md) FUN_005964e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596634",
      "incomplete_value": false,
      "site": "00596638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005965f4",
      "incomplete_value": false,
      "site": "005965f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005966d4",
      "incomplete_value": false,
      "site": "005966d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596694",
      "incomplete_value": false,
      "site": "00596698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "005967d4",
      "incomplete_value": false,
      "site": "005967dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596794",
      "incomplete_value": false,
      "site": "0059679c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "005965c8",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ],
    [
      "005965f4",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ],
    [
      "00596638",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005965c8",
      "PARAM",
      [
        "storage",
        "002b8f0b",
        null,
        null
      ]
    ],
    [
      "005965f4",
      "PARAM",
      [
        "storage",
        "002b8f0b",
        null,
        null
      ]
    ],
    [
      "00596638",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059658c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-0059658c) · [`00596544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-00596544) · [`00596564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005964a4.md#insn-00596564)
- 新版 [`005965cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-005965cc) · [`00596584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-00596584) · [`005965a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-005965a4)

~~~diff
- 0059658c ["INT_ADD", "register:40f0:8", ["const:59658c:8", "const:4:8"]]
- 0059658c ["CALL", null, ["callee:00c580b0:8"]]
+ 005965cc ["INT_ADD", "register:40f0:8", ["const:5965cc:8", "const:4:8"]]
+ 005965cc ["CALL", null, ["callee:00c580b0:8"]]
- 0059658c bytes 95061b94
+ 005965cc bytes b9061b94
- 00596544 ["INT_ADD", "register:40f0:8", ["const:596544:8", "const:4:8"]]
- 00596544 ["CALL", null, ["callee:00c57f60:8"]]
+ 00596584 ["INT_ADD", "register:40f0:8", ["const:596584:8", "const:4:8"]]
+ 00596584 ["CALL", null, ["callee:00c57f60:8"]]
- 00596544 bytes 53061b94
+ 00596584 bytes 77061b94
- 00596564 ["INT_ADD", "register:40f0:8", ["const:596564:8", "const:4:8"]]
- 00596564 ["CALL", null, ["callee:00c58010:8"]]
+ 005965a4 ["INT_ADD", "register:40f0:8", ["const:5965a4:8", "const:4:8"]]
+ 005965a4 ["CALL", null, ["callee:00c58010:8"]]
- 00596564 bytes 77061b94
+ 005965a4 bytes 9b061b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8322c4adf229e8ec7f17a3f239761d35"></a>

### [`00596838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md) → [`00596878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md) FUN_00596878

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005960f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/005960f4.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596c34",
      "incomplete_value": false,
      "site": "00596c38",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596bf4",
      "incomplete_value": false,
      "site": "00596bf8",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005969ec",
      "incomplete_value": false,
      "site": "005969f8",
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
            "const:a55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005969ac",
      "incomplete_value": false,
      "site": "005969b8",
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
            "const:ab1:8"
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
      "005968cc",
      "READ",
      [
        "storage",
        "00c9b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00596948",
      "PARAM",
      [
        "storage",
        "002aeab1",
        null,
        null
      ]
    ],
    [
      "005969b8",
      "PARAM",
      [
        "storage",
        "002a32eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005968cc",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ],
    [
      "00596948",
      "PARAM",
      [
        "storage",
        "002aea55",
        null,
        null
      ]
    ],
    [
      "005969b8",
      "PARAM",
      [
        "storage",
        "002a329e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005969b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-005969b8) · [`00596888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-00596888) · [`0059688c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596838.md#insn-0059688c)
- 新版 [`005969f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005969f8) · [`005968c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005968c8) · [`005968cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005968cc)

~~~diff
- 005969b8 ["INT_ADD", "register:40f0:8", ["const:5969b8:8", "const:4:8"]]
- 005969b8 ["CALL", null, ["callee:00c580b0:8"]]
+ 005969f8 ["INT_ADD", "register:40f0:8", ["const:5969f8:8", "const:4:8"]]
+ 005969f8 ["CALL", null, ["callee:00c580b0:8"]]
- 005969b8 bytes 8a051b94
+ 005969f8 bytes ae051b94
- 00596888 ["COPY", "tmp:0:8", ["const:2eb:8"]]
- 00596888 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00596888 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00596888 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005968c8 ["COPY", "tmp:0:8", ["const:29e:8"]]
+ 005968c8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005968c8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005968c8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00596888 bytes 94ae0b91
+ 005968c8 bytes 947a0a91
- 0059688c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2e8:8"]]
- 0059688c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005968cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3b8:8"]]
+ 005968cc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0059688c bytes b57641f9
+ 005968cc bytes b5de41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548c0e7df5f47e384bc52a930dcbaaa2"></a>

### [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) → [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) FUN_00596d50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) [`0045a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md) [`0046010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md) · 呼出先 5件 [`00595580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595580.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 14件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`0045a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md) [`0045a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md) [`0046014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md) · 呼出先 5件 [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596da8",
      "incomplete_value": false,
      "site": "00596da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d68",
      "incomplete_value": false,
      "site": "00596d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "definition_site": "00596dd8",
      "incomplete_value": false,
      "site": "00596de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d98",
      "incomplete_value": false,
      "site": "00596da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "00596da8",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596de0",
      "DATA",
      [
        "storage",
        "00c6d5e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00596da8",
      "DATA",
      [
        "storage",
        "00c6d7a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596de0",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d60) · [`00596d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d44) · [`00596d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md#insn-00596d58)
- 新版 [`00596da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596da0) · [`00596d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596d84) · [`00596d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596d98)

~~~diff
- 00596d60 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00596d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596da0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00596da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d60 bytes 08611b91
+ 00596da0 bytes 08a11e91
- 00596d44 ["INT_ADD", "register:40f0:8", ["const:596d44:8", "const:4:8"]]
- 00596d44 ["CALL", null, ["callee:005955c0:8"]]
+ 00596d84 ["INT_ADD", "register:40f0:8", ["const:596d84:8", "const:4:8"]]
+ 00596d84 ["CALL", null, ["callee:005955c0:8"]]
- 00596d44 bytes 0ffaff97
+ 00596d84 bytes 0ffaff97
- 00596d58 ["INT_ADD", "register:40f0:8", ["const:596d58:8", "const:4:8"]]
- 00596d58 ["CALL", null, ["callee:00c57f60:8"]]
+ 00596d98 ["INT_ADD", "register:40f0:8", ["const:596d98:8", "const:4:8"]]
+ 00596d98 ["CALL", null, ["callee:00c57f60:8"]]
- 00596d58 bytes 4e041b94
+ 00596d98 bytes 72041b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d28a052f0697500e0b25077acf43d3eb"></a>

### [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) → [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) FUN_00596f6c

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 42件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`005712e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/005712e0.md) [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) · 呼出先 6件 [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 42件 [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) · 呼出先 6件 [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596fac",
      "incomplete_value": false,
      "site": "00596fbc",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596f6c",
      "incomplete_value": false,
      "site": "00596f7c",
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
            "const:798:8"
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
      "definition_site": "00596fb4",
      "incomplete_value": false,
      "site": "00596fbc",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596f74",
      "incomplete_value": false,
      "site": "00596f7c",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00596fac",
      "PARAM",
      [
        "storage",
        "00c63798",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596fb4",
      "PARAM",
      [
        "storage",
        "00c63b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00596fac",
      "PARAM",
      [
        "storage",
        "00c63868",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00596fb4",
      "PARAM",
      [
        "storage",
        "00c63be8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596f7c) · [`00596fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596fbc) · [`00596f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md#insn-00596f50)
- 新版 [`00596fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596fbc) · [`00596ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596ffc) · [`00596f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596f90)

~~~diff
- 00596f7c ["INT_ADD", "register:40f0:8", ["const:596f7c:8", "const:4:8"]]
- 00596f7c ["CALL", null, ["callee:00c586e0:8"]]
+ 00596fbc ["INT_ADD", "register:40f0:8", ["const:596fbc:8", "const:4:8"]]
+ 00596fbc ["CALL", null, ["callee:00c586e0:8"]]
- 00596f7c bytes a5051b94
+ 00596fbc bytes c9051b94
- 00596fbc ["INT_ADD", "register:40f0:8", ["const:596fbc:8", "const:4:8"]]
- 00596fbc ["CALL", null, ["callee:00c53da0:8"]]
+ 00596ffc ["INT_ADD", "register:40f0:8", ["const:596ffc:8", "const:4:8"]]
+ 00596ffc ["CALL", null, ["callee:00c53da0:8"]]
- 00596fbc bytes 51f31a94
+ 00596ffc bytes 69f31a94
- 00596f50 ["INT_ADD", "register:40f0:8", ["const:596f50:8", "const:4:8"]]
- 00596f50 ["CALL", null, ["callee:00596d50:8"]]
+ 00596f90 ["INT_ADD", "register:40f0:8", ["const:596f90:8", "const:4:8"]]
+ 00596f90 ["CALL", null, ["callee:00596d50:8"]]
- 00596f50 bytes 70ffff97
+ 00596f90 bytes 70ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0721f4f02a5a5a93fdae1a7a5bed1a9b"></a>

### [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md) → [`0059705c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md) FUN_0059705c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00496a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md) [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) · 呼出先 6件 [`00596e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596e1c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00496a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md) [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) · 呼出先 6件 [`00596e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059709c",
      "incomplete_value": false,
      "site": "005970ac",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059705c",
      "incomplete_value": false,
      "site": "0059706c",
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
            "const:798:8"
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
      "definition_site": "005970a4",
      "incomplete_value": false,
      "site": "005970ac",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597064",
      "incomplete_value": false,
      "site": "0059706c",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0059709c",
      "PARAM",
      [
        "storage",
        "00c63798",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005970a4",
      "PARAM",
      [
        "storage",
        "00c63b18",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0059709c",
      "PARAM",
      [
        "storage",
        "00c63868",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005970a4",
      "PARAM",
      [
        "storage",
        "00c63be8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059706c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-0059706c) · [`005970ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-005970ac) · [`00597040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md#insn-00597040)
- 新版 [`005970ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-005970ac) · [`005970ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-005970ec) · [`00597080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-00597080)

~~~diff
- 0059706c ["INT_ADD", "register:40f0:8", ["const:59706c:8", "const:4:8"]]
- 0059706c ["CALL", null, ["callee:00c586e0:8"]]
+ 005970ac ["INT_ADD", "register:40f0:8", ["const:5970ac:8", "const:4:8"]]
+ 005970ac ["CALL", null, ["callee:00c586e0:8"]]
- 0059706c bytes 69051b94
+ 005970ac bytes 8d051b94
- 005970ac ["INT_ADD", "register:40f0:8", ["const:5970ac:8", "const:4:8"]]
- 005970ac ["CALL", null, ["callee:00c53da0:8"]]
+ 005970ec ["INT_ADD", "register:40f0:8", ["const:5970ec:8", "const:4:8"]]
+ 005970ec ["CALL", null, ["callee:00c53da0:8"]]
- 005970ac bytes 15f31a94
+ 005970ec bytes 2df31a94
- 00597040 ["INT_ADD", "register:40f0:8", ["const:597040:8", "const:4:8"]]
- 00597040 ["CALL", null, ["callee:00596e5c:8"]]
+ 00597080 ["INT_ADD", "register:40f0:8", ["const:597080:8", "const:4:8"]]
+ 00597080 ["CALL", null, ["callee:00596e5c:8"]]
- 00597040 bytes 77ffff97
+ 00597080 bytes 77ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff6d3f9753275b98fa4d24d8ce4ee4e"></a>

### [`00597114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md) → [`00597154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md) FUN_00597154

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059716c",
      "incomplete_value": false,
      "site": "00597170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059712c",
      "incomplete_value": false,
      "site": "00597130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00597170",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00597170",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059712c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md#insn-0059712c) · [`0059716c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597114.md#insn-0059716c)
- 新版 [`0059716c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md#insn-0059716c) · [`005971ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md#insn-005971ac)

~~~diff
- 0059712c ["COPY", "tmp:0:8", ["const:678:8"]]
- 0059712c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059712c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059712c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059716c ["COPY", "tmp:0:8", ["const:748:8"]]
+ 0059716c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059716c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059716c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059712c bytes 08e11991
+ 0059716c bytes 08211d91
- 0059716c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059716c ["INT_ADD", "register:40f0:8", ["const:59716c:8", "const:4:8"]]
- 0059716c ["CALLIND", null, ["register:0:8"]]
+ 005971ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005971ac ["INT_ADD", "register:40f0:8", ["const:5971ac:8", "const:4:8"]]
+ 005971ac ["CALLIND", null, ["register:0:8"]]
- 0059716c bytes 00013fd6
+ 005971ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02bbd7a692f5992eb0114096803bc3dc"></a>

### [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) → [`005971dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md) FUN_005971dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`005a14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a14b0.md) [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005971f8",
      "incomplete_value": false,
      "site": "005971fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005971b8",
      "incomplete_value": false,
      "site": "005971bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "005971fc",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005971fc",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005971b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-005971b8) · [`005971f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-005971f4) · [`00597204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md#insn-00597204)
- 新版 [`005971f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-005971f8) · [`00597234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-00597234) · [`00597244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-00597244)

~~~diff
- 005971b8 ["COPY", "tmp:0:8", ["const:678:8"]]
- 005971b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005971b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005971b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005971f8 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 005971f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005971f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005971f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005971b8 bytes 08e11991
+ 005971f8 bytes 08211d91
- 005971f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005971f4 ["INT_ADD", "register:40f0:8", ["const:5971f4:8", "const:4:8"]]
- 005971f4 ["CALLIND", null, ["register:0:8"]]
+ 00597234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00597234 ["INT_ADD", "register:40f0:8", ["const:597234:8", "const:4:8"]]
+ 00597234 ["CALLIND", null, ["register:0:8"]]
- 005971f4 bytes 00013fd6
+ 00597234 bytes 00013fd6
- 00597204 ["INT_ADD", "register:40f0:8", ["const:597204:8", "const:4:8"]]
- 00597204 ["CALL", null, ["callee:00c57f80:8"]]
+ 00597244 ["INT_ADD", "register:40f0:8", ["const:597244:8", "const:4:8"]]
+ 00597244 ["CALL", null, ["callee:00c57f80:8"]]
- 00597204 bytes 2b031b94
+ 00597244 bytes 4f031b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e6360bb72909a66d0d56d1c61513886"></a>

### [`0059721c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md) → [`0059725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md) FUN_0059725c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md) [`0076701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/0076701c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00597544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597544.md) [`00767074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00597268",
      "incomplete_value": false,
      "site": "0059726c",
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
    "old": {
      "definition_site": "00597228",
      "incomplete_value": false,
      "site": "0059722c",
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
            "const:f4c:8"
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
      "00597268",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00597268",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059722c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md#insn-0059722c) · [`00597228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059721c.md#insn-00597228)
- 新版 [`0059726c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md#insn-0059726c) · [`00597268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md#insn-00597268)

~~~diff
- 0059722c ["INT_ADD", "register:40f0:8", ["const:59722c:8", "const:4:8"]]
- 0059722c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0059726c ["INT_ADD", "register:40f0:8", ["const:59726c:8", "const:4:8"]]
+ 0059726c ["CALL", null, ["callee:0043b7b8:8"]]
- 0059722c bytes 5391fa97
+ 0059726c bytes 5391fa97
- 00597228 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00597228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00597228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00597228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00597268 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00597268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00597268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00597268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00597228 bytes 00303d91
+ 00597268 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba66415b7094856ab3d96d4768d2059"></a>

### [`005978e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md) → [`00597920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md) FUN_00597920

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005977bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005977bc.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005977fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977fc.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)

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
      "definition_site": "00597988",
      "incomplete_value": true,
      "site": "0059798c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597948",
      "incomplete_value": true,
      "site": "0059794c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:2f0:8"
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
      "00597988",
      "READ",
      [
        "storage",
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00597988",
      "PARAM",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00597988",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00597988",
      "PARAM",
      [
        "storage",
        "01127cb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059794c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059794c) · [`0059791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059791c) · [`0059793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005978e0.md#insn-0059793c)
- 新版 [`0059798c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059798c) · [`0059795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059795c) · [`0059797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059797c)

~~~diff
- 0059794c ["INT_ADD", "register:40f0:8", ["const:59794c:8", "const:4:8"]]
- 0059794c ["CALL", null, ["callee:00c58350:8"]]
+ 0059798c ["INT_ADD", "register:40f0:8", ["const:59798c:8", "const:4:8"]]
+ 0059798c ["CALL", null, ["callee:00c58350:8"]]
- 0059794c bytes 4d021b94
+ 0059798c bytes 71021b94
- 0059791c ["INT_ADD", "register:40f0:8", ["const:59791c:8", "const:4:8"]]
- 0059791c ["CALL", null, ["callee:00c59ea0:8"]]
+ 0059795c ["INT_ADD", "register:40f0:8", ["const:59795c:8", "const:4:8"]]
+ 0059795c ["CALL", null, ["callee:00c59ea0:8"]]
- 0059791c bytes 2d091b94
+ 0059795c bytes 51091b94
- 0059793c ["INT_ADD", "register:40f0:8", ["const:59793c:8", "const:4:8"]]
- 0059793c ["CALL", null, ["callee:00c58340:8"]]
+ 0059797c ["INT_ADD", "register:40f0:8", ["const:59797c:8", "const:4:8"]]
+ 0059797c ["CALL", null, ["callee:00c58340:8"]]
- 0059793c bytes 4d021b94
+ 0059797c bytes 71021b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-373085bbc1e00d7dadb010e13a3ebcc0"></a>

### [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md) → [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md) FUN_00597ad4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`009bad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009bad00.md) · 呼出先 9件 [`00597c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) [`009bad54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ba/009bad54.md) · 呼出先 9件 [`00597c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.32% / 新版 94.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597b8c",
      "incomplete_value": true,
      "site": "00597b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00597b4c",
      "incomplete_value": true,
      "site": "00597b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "unmatched:00597acc",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00597b24",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00597b24",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00597b08",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00597b24",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00597b24",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597b10) · [`00597ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597ac8) · [`00597acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md#insn-00597acc)
- 新版 [`00597b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md#insn-00597b50) · [`00597b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md#insn-00597b0c)

~~~diff
- 00597b10 ["INT_ADD", "register:40f0:8", ["const:597b10:8", "const:4:8"]]
- 00597b10 ["CALL", null, ["callee:00c582b0:8"]]
+ 00597b50 ["INT_ADD", "register:40f0:8", ["const:597b50:8", "const:4:8"]]
+ 00597b50 ["CALL", null, ["callee:00c582b0:8"]]
- 00597b10 bytes b4011b94
+ 00597b50 bytes d8011b94
- 00597ac8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
- 00597ac8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597b0c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c88:8"]]
+ 00597b0c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00597ac8 bytes 5a4746f9
+ 00597b0c bytes 394746f9
- 00597acc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:bb8:8"]]
- 00597acc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00597acc bytes 39df45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e70bea188c9c92d8660c02b33a8fea74"></a>

### [`00597c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md) → [`00597c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md) FUN_00597c80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md) · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)
- 新版 呼出元 1件 [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md) · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597ce0",
      "incomplete_value": true,
      "site": "00597ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597ca0",
      "incomplete_value": true,
      "site": "00597ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
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
      "definition_site": "00597d24",
      "incomplete_value": true,
      "site": "00597d28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597ce4",
      "incomplete_value": true,
      "site": "00597ce8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
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
      "00597ce0",
      "READ",
      [
        "storage",
        "00c9b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ce0",
      "PARAM",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597d24",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00597ce0",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00597ce0",
      "PARAM",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00597d24",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ca4) · [`00597ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ce4) · [`00597ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597c40.md#insn-00597ce8)
- 新版 [`00597ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597ce4) · [`00597d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597d24) · [`00597d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597d28)

~~~diff
- 00597ca4 ["INT_ADD", "register:40f0:8", ["const:597ca4:8", "const:4:8"]]
- 00597ca4 ["CALL", null, ["callee:00c58350:8"]]
+ 00597ce4 ["INT_ADD", "register:40f0:8", ["const:597ce4:8", "const:4:8"]]
+ 00597ce4 ["CALL", null, ["callee:00c58350:8"]]
- 00597ca4 bytes 77011b94
+ 00597ce4 bytes 9b011b94
- 00597ce4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
- 00597ce4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597d24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d00:8"]]
+ 00597d24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00597ce4 bytes 211846f9
+ 00597d24 bytes 218046f9
- 00597ce8 ["INT_ADD", "register:40f0:8", ["const:597ce8:8", "const:4:8"]]
- 00597ce8 ["CALL", null, ["callee:00c58350:8"]]
+ 00597d28 ["INT_ADD", "register:40f0:8", ["const:597d28:8", "const:4:8"]]
+ 00597d28 ["CALL", null, ["callee:00c58350:8"]]
- 00597ce8 bytes 66011b94
+ 00597d28 bytes 8a011b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7916f6cbb5f269865fe31b4b27f6dc99"></a>

### [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) → [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) FUN_00597f10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) [`005b77ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md) [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md) · 呼出先 0件 
- 新版 呼出元 18件 [`005aca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca50.md) [`005b71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md) [`005b77ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md) [`005b7d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md) [`005b811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597f18",
      "incomplete_value": false,
      "site": "00597f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597ed8",
      "incomplete_value": false,
      "site": "00597edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00597f1c",
      "DATA",
      [
        "storage",
        "00c6d728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00597f1c",
      "DATA",
      [
        "storage",
        "00c6d7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md#insn-00597ed8)
- 新版 [`00597f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md#insn-00597f18)

~~~diff
- 00597ed8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 00597ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597f18 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00597f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597ed8 bytes 08a11c91
+ 00597f18 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e01cb25697d1a49f1c4962f0d6e2f97"></a>

### [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) → [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) FUN_00597f3c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)
- 新版 呼出元 4件 [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) [`0059929c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md) [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) [`005acf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acf00.md) · 呼出先 24件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0044ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044ff9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005983e4",
      "incomplete_value": true,
      "site": "005983ec",
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
      "definition_site": "005983a4",
      "incomplete_value": true,
      "site": "005983ac",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005983f4",
      "incomplete_value": true,
      "site": "005983f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "005983b4",
      "incomplete_value": true,
      "site": "005983b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005983f4",
      "incomplete_value": true,
      "site": "005983f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005983b4",
      "incomplete_value": true,
      "site": "005983b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00597fdc",
      "READ",
      [
        "storage",
        "00c9b300",
        null,
        "pointer"
      ]
    ],
    [
      "00597fec",
      "READ",
      [
        "storage",
        "00ca65d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00597ff8",
      "READ",
      [
        "storage",
        "00ca65d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00597fdc",
      "READ",
      [
        "storage",
        "00c9b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00597fec",
      "READ",
      [
        "storage",
        "00ca66d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00597ff8",
      "READ",
      [
        "storage",
        "00ca66d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598038) · [`00598048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598048) · [`00598450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md#insn-00598450)
- 新版 [`00598078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-00598078) · [`00598088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-00598088) · [`00598490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-00598490)

~~~diff
- 00598038 ["INT_ADD", "register:40f0:8", ["const:598038:8", "const:4:8"]]
- 00598038 ["CALL", null, ["callee:00c58180:8"]]
+ 00598078 ["INT_ADD", "register:40f0:8", ["const:598078:8", "const:4:8"]]
+ 00598078 ["CALL", null, ["callee:00c58180:8"]]
- 00598038 bytes 1e001b94
+ 00598078 bytes 42001b94
- 00598048 ["INT_ADD", "register:40f0:8", ["const:598048:8", "const:4:8"]]
- 00598048 ["CALL", null, ["callee:00c58040:8"]]
+ 00598088 ["INT_ADD", "register:40f0:8", ["const:598088:8", "const:4:8"]]
+ 00598088 ["CALL", null, ["callee:00c58040:8"]]
- 00598048 bytes caff1a94
+ 00598088 bytes eeff1a94
- 00598450 ["INT_ADD", "register:40f0:8", ["const:598450:8", "const:4:8"]]
- 00598450 ["CALL", null, ["callee:00c57f60:8"]]
+ 00598490 ["INT_ADD", "register:40f0:8", ["const:598490:8", "const:4:8"]]
+ 00598490 ["CALL", null, ["callee:00c57f60:8"]]
- 00598450 bytes 90fe1a94
+ 00598490 bytes b4fe1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6508618132a51e93978540f72138ac63"></a>

### [`00598b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md) → [`00598b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md) FUN_00598b7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) · 呼出先 3件 [`0059a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a1c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) · 呼出先 3件 [`0059a208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a208.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598c1c",
      "incomplete_value": false,
      "site": "00598c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598bdc",
      "incomplete_value": false,
      "site": "00598be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "00598c20",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598c20",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598b7c) · [`00598bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598bb8) · [`00598bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b3c.md#insn-00598bcc)
- 新版 [`00598bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598bbc) · [`00598bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598bf8) · [`00598c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598c0c)

~~~diff
- 00598b7c ["COPY", "register:0:8", ["register:4048:8"]]
- 00598b7c ["INT_ADD", "register:40f0:8", ["const:598b7c:8", "const:4:8"]]
- 00598b7c ["CALLIND", null, ["register:0:8"]]
+ 00598bbc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00598bbc ["INT_ADD", "register:40f0:8", ["const:598bbc:8", "const:4:8"]]
+ 00598bbc ["CALLIND", null, ["register:0:8"]]
- 00598b7c bytes 20013fd6
+ 00598bbc bytes 20013fd6
- 00598bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598bb8 ["INT_ADD", "register:40f0:8", ["const:598bb8:8", "const:4:8"]]
- 00598bb8 ["CALLIND", null, ["register:0:8"]]
+ 00598bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598bf8 ["INT_ADD", "register:40f0:8", ["const:598bf8:8", "const:4:8"]]
+ 00598bf8 ["CALLIND", null, ["register:0:8"]]
- 00598bb8 bytes 00013fd6
+ 00598bf8 bytes 00013fd6
- 00598bcc ["INT_ADD", "register:40f0:8", ["const:598bcc:8", "const:4:8"]]
- 00598bcc ["CALL", null, ["callee:00c57f60:8"]]
+ 00598c0c ["INT_ADD", "register:40f0:8", ["const:598c0c:8", "const:4:8"]]
+ 00598c0c ["CALL", null, ["callee:00c57f60:8"]]
- 00598bcc bytes b1fc1a94
+ 00598c0c bytes d5fc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92346ac208997fc916c631d65bdb2b94"></a>

### [`00598dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md) → [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) FUN_00598e00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059921c.md) [`0059a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a498.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`0059925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059925c.md) [`0059a4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599020",
      "incomplete_value": false,
      "site": "00599020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598fe0",
      "incomplete_value": false,
      "site": "00598fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00598f04",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "00599020",
      "DATA",
      [
        "storage",
        "00c6d880",
        null,
        "undefined *"
      ]
    ],
    [
      "00599090",
      "READ",
      [
        "storage",
        "00c6d8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598f04",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "00599020",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ],
    [
      "00599090",
      "READ",
      [
        "storage",
        "00c6d978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598dec) · [`00598e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598e0c) · [`00598e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598dc0.md#insn-00598e20)
- 新版 [`00598e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e2c) · [`00598e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e4c) · [`00598e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e60)

~~~diff
- 00598dec ["INT_ADD", "register:40f0:8", ["const:598dec:8", "const:4:8"]]
- 00598dec ["CALL", null, ["callee:00597f3c:8"]]
+ 00598e2c ["INT_ADD", "register:40f0:8", ["const:598e2c:8", "const:4:8"]]
+ 00598e2c ["CALL", null, ["callee:00597f3c:8"]]
- 00598dec bytes 44fcff97
+ 00598e2c bytes 44fcff97
- 00598e0c ["INT_ADD", "register:40f0:8", ["const:598e0c:8", "const:4:8"]]
- 00598e0c ["CALL", null, ["callee:00c53da0:8"]]
+ 00598e4c ["INT_ADD", "register:40f0:8", ["const:598e4c:8", "const:4:8"]]
+ 00598e4c ["CALL", null, ["callee:00c53da0:8"]]
- 00598e0c bytes bdeb1a94
+ 00598e4c bytes d5eb1a94
- 00598e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598e20 ["INT_ADD", "register:40f0:8", ["const:598e20:8", "const:4:8"]]
- 00598e20 ["CALLIND", null, ["register:0:8"]]
+ 00598e60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598e60 ["INT_ADD", "register:40f0:8", ["const:598e60:8", "const:4:8"]]
+ 00598e60 ["CALLIND", null, ["register:0:8"]]
- 00598e20 bytes 00013fd6
+ 00598e60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f554eadf1b41a000f32dbe9cb56786"></a>

### [`0059925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md) → [`0059929c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md) FUN_0059929c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059adb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059adb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`0059adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059adf8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599464",
      "incomplete_value": false,
      "site": "0059946c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599424",
      "incomplete_value": false,
      "site": "0059942c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "definition_site": "00599358",
      "incomplete_value": false,
      "site": "00599360",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599318",
      "incomplete_value": false,
      "site": "00599320",
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
            "const:588:8"
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
      "00599358",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "0059946c",
      "DATA",
      [
        "storage",
        "00c6d900",
        null,
        "undefined *"
      ]
    ],
    [
      "005994f8",
      "READ",
      [
        "storage",
        "00c6d928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599358",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "0059946c",
      "DATA",
      [
        "storage",
        "00c6d9d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005994f8",
      "READ",
      [
        "storage",
        "00c6d9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-00599320) · [`0059928c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-0059928c) · [`005992ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/0059925c.md#insn-005992ac)
- 新版 [`00599360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-00599360) · [`005992cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-005992cc) · [`005992ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-005992ec)

~~~diff
- 00599320 ["INT_ADD", "register:40f0:8", ["const:599320:8", "const:4:8"]]
- 00599320 ["CALL", null, ["callee:004410cc:8"]]
+ 00599360 ["INT_ADD", "register:40f0:8", ["const:599360:8", "const:4:8"]]
+ 00599360 ["CALL", null, ["callee:004410cc:8"]]
- 00599320 bytes 5b9ffa97
+ 00599360 bytes 5b9ffa97
- 0059928c ["INT_ADD", "register:40f0:8", ["const:59928c:8", "const:4:8"]]
- 0059928c ["CALL", null, ["callee:00597f3c:8"]]
+ 005992cc ["INT_ADD", "register:40f0:8", ["const:5992cc:8", "const:4:8"]]
+ 005992cc ["CALL", null, ["callee:00597f3c:8"]]
- 0059928c bytes 1cfbff97
+ 005992cc bytes 1cfbff97
- 005992ac ["INT_ADD", "register:40f0:8", ["const:5992ac:8", "const:4:8"]]
- 005992ac ["CALL", null, ["callee:00c53da0:8"]]
+ 005992ec ["INT_ADD", "register:40f0:8", ["const:5992ec:8", "const:4:8"]]
+ 005992ec ["CALL", null, ["callee:00c53da0:8"]]
- 005992ac bytes 95ea1a94
+ 005992ec bytes adea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a8c1370cb09eb47354fc0ea7d91124"></a>

### [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) → [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) FUN_005996f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`007690c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007690c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 2件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) [`0076911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076911c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059971c",
      "incomplete_value": false,
      "site": "0059972c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005996dc",
      "incomplete_value": false,
      "site": "005996ec",
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
            "const:570:8"
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
      "0059971c",
      "PARAM",
      [
        "storage",
        "00ca6570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0059971c",
      "PARAM",
      [
        "storage",
        "00ca6670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005996ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-005996ec) · [`005996dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-005996dc) · [`00599708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md#insn-00599708)
- 新版 [`0059972c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-0059972c) · [`0059971c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-0059971c) · [`00599748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-00599748)

~~~diff
- 005996ec ["INT_ADD", "register:40f0:8", ["const:5996ec:8", "const:4:8"]]
- 005996ec ["CALL", null, ["callee:004410cc:8"]]
+ 0059972c ["INT_ADD", "register:40f0:8", ["const:59972c:8", "const:4:8"]]
+ 0059972c ["CALL", null, ["callee:004410cc:8"]]
- 005996ec bytes 689efa97
+ 0059972c bytes 689efa97
- 005996dc ["COPY", "tmp:0:8", ["const:570:8"]]
- 005996dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005996dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005996dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059971c ["COPY", "tmp:0:8", ["const:670:8"]]
+ 0059971c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059971c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059971c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005996dc bytes 21c01591
+ 0059971c bytes 21c01991
- 00599708 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599708 ["INT_ADD", "register:40f0:8", ["const:599708:8", "const:4:8"]]
- 00599708 ["CALLIND", null, ["register:0:8"]]
+ 00599748 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599748 ["INT_ADD", "register:40f0:8", ["const:599748:8", "const:4:8"]]
+ 00599748 ["CALLIND", null, ["register:0:8"]]
- 00599708 bytes 00013fd6
+ 00599748 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c778a46df102da7ddb0325613434577"></a>

### [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) → [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) FUN_00599844

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005996b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/005996b4.md) · 呼出先 12件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`0059b340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b340.md) [`0059b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b390.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md)
- 新版 呼出元 1件 [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) · 呼出先 12件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`0059b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b380.md) [`0059b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b3d0.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005998e4",
      "incomplete_value": false,
      "site": "005998e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005998a4",
      "incomplete_value": false,
      "site": "005998a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599870",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599830",
      "value": [
        "leaf",
        "ram:764384:8"
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
      "00599870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "005998e4",
      "DATA",
      [
        "storage",
        "00c6d980",
        null,
        "undefined *"
      ]
    ],
    [
      "00599920",
      "READ",
      [
        "storage",
        "00c6d9a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00599870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "005998e4",
      "DATA",
      [
        "storage",
        "00c6da50",
        null,
        "undefined *"
      ]
    ],
    [
      "00599920",
      "READ",
      [
        "storage",
        "00c6da70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md#insn-00599830) · [`00599870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md#insn-00599870) · [`005998e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md#insn-005998e4)
- 新版 [`00599870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-00599870) · [`005998b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-005998b0) · [`00599924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-00599924)

~~~diff
- 00599830 ["INT_ADD", "register:40f0:8", ["const:599830:8", "const:4:8"]]
- 00599830 ["CALL", null, ["ram:764384:8"]]
+ 00599870 ["INT_ADD", "register:40f0:8", ["const:599870:8", "const:4:8"]]
+ 00599870 ["CALL", null, ["ram:7643dc:8"]]
- 00599830 bytes d52a0794
+ 00599870 bytes db2a0794
- 00599870 ["INT_ADD", "register:40f0:8", ["const:599870:8", "const:4:8"]]
- 00599870 ["CALL", null, ["callee:00c53d70:8"]]
+ 005998b0 ["INT_ADD", "register:40f0:8", ["const:5998b0:8", "const:4:8"]]
+ 005998b0 ["CALL", null, ["callee:00c53d70:8"]]
- 00599870 bytes 18e91a94
+ 005998b0 bytes 30e91a94
- 005998e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005998e4 ["INT_ADD", "register:40f0:8", ["const:5998e4:8", "const:4:8"]]
- 005998e4 ["CALLIND", null, ["register:0:8"]]
+ 00599924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599924 ["INT_ADD", "register:40f0:8", ["const:599924:8", "const:4:8"]]
+ 00599924 ["CALLIND", null, ["register:0:8"]]
- 005998e4 bytes 00013fd6
+ 00599924 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e86fcc5887b9312cad1083b6fd773b1c"></a>

### [`00599a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md) → [`00599ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md) FUN_00599ab4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) · 呼出先 4件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) · 呼出先 4件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00599ae8",
      "incomplete_value": false,
      "site": "00599af8",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599aa8",
      "incomplete_value": false,
      "site": "00599ab8",
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
            "const:588:8"
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
      "definition_site": "00599b5c",
      "incomplete_value": false,
      "site": "00599b64",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599b1c",
      "incomplete_value": false,
      "site": "00599b24",
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
            "const:570:8"
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
      "00599ae8",
      "PARAM",
      [
        "storage",
        "00ca6588",
        null,
        "undefined1"
      ]
    ],
    [
      "00599b5c",
      "PARAM",
      [
        "storage",
        "00ca6570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00599ae8",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "00599b5c",
      "PARAM",
      [
        "storage",
        "00ca6670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md#insn-00599ab8) · [`00599b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md#insn-00599b24) · [`00599aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599a74.md#insn-00599aa8)
- 新版 [`00599af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599af8) · [`00599b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599b64) · [`00599ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599ae8)

~~~diff
- 00599ab8 ["INT_ADD", "register:40f0:8", ["const:599ab8:8", "const:4:8"]]
- 00599ab8 ["CALL", null, ["callee:004410cc:8"]]
+ 00599af8 ["INT_ADD", "register:40f0:8", ["const:599af8:8", "const:4:8"]]
+ 00599af8 ["CALL", null, ["callee:004410cc:8"]]
- 00599ab8 bytes 759dfa97
+ 00599af8 bytes 759dfa97
- 00599b24 ["INT_ADD", "register:40f0:8", ["const:599b24:8", "const:4:8"]]
- 00599b24 ["CALL", null, ["callee:004410cc:8"]]
+ 00599b64 ["INT_ADD", "register:40f0:8", ["const:599b64:8", "const:4:8"]]
+ 00599b64 ["CALL", null, ["callee:004410cc:8"]]
- 00599b24 bytes 5a9dfa97
+ 00599b64 bytes 5a9dfa97
- 00599aa8 ["COPY", "tmp:0:8", ["const:588:8"]]
- 00599aa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00599aa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00599aa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00599ae8 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00599ae8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00599ae8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00599ae8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00599aa8 bytes 21201691
+ 00599ae8 bytes 21201a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2907d669cd5e175c44bf6575f475107a"></a>

### [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) → [`00599e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md) FUN_00599e94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00599f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f38.md) [`005ad484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md) [`005ad510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`00599f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f78.md) [`005ad4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad4c4.md) [`005ad550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad550.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599eac",
      "incomplete_value": false,
      "site": "00599eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599e6c",
      "incomplete_value": false,
      "site": "00599e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00599eb0",
      "DATA",
      [
        "storage",
        "00c6d728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599eb0",
      "DATA",
      [
        "storage",
        "00c6d7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md#insn-00599e6c) · [`00599e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md#insn-00599e80) · [`00599e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md#insn-00599e94)
- 新版 [`00599eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599eac) · [`00599ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599ec0) · [`00599ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599ed4)

~~~diff
- 00599e6c ["COPY", "tmp:0:8", ["const:728:8"]]
- 00599e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599eac ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00599eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599e6c bytes 08a11c91
+ 00599eac bytes 08e11f91
- 00599e80 ["INT_ADD", "register:40f0:8", ["const:599e80:8", "const:4:8"]]
- 00599e80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00599ec0 ["INT_ADD", "register:40f0:8", ["const:599ec0:8", "const:4:8"]]
+ 00599ec0 ["CALL", null, ["callee:00c53da0:8"]]
- 00599e80 bytes a0e71a94
+ 00599ec0 bytes b8e71a94
- 00599e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599e94 ["INT_ADD", "register:40f0:8", ["const:599e94:8", "const:4:8"]]
- 00599e94 ["CALLIND", null, ["register:0:8"]]
+ 00599ed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599ed4 ["INT_ADD", "register:40f0:8", ["const:599ed4:8", "const:4:8"]]
+ 00599ed4 ["CALLIND", null, ["register:0:8"]]
- 00599e94 bytes 00013fd6
+ 00599ed4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21ac8c582045b6f74dfe008cd73433f9"></a>

### [`00599f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f5c.md) → [`00599f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f9c.md) FUN_00599f9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599fa8",
      "incomplete_value": false,
      "site": "00599fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599f68",
      "incomplete_value": false,
      "site": "00599f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "00599fb4",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599fb4",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599f5c.md#insn-00599f68)
- 新版 [`00599fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f9c.md#insn-00599fa8)

~~~diff
- 00599f68 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00599f68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00599f68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00599f68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00599fa8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00599fa8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00599fa8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00599fa8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00599f68 bytes 4a411e91
+ 00599fa8 bytes 4a812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8547a55fc2c65c688b11ff651ada440d"></a>

### [`00599fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599fa0.md) → [`00599fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md) FUN_00599fe0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599ff8",
      "incomplete_value": false,
      "site": "0059a004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599fb8",
      "incomplete_value": false,
      "site": "00599fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "0059a004",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a004",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599fa0.md#insn-00599fb8) · [`00599fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599fa0.md#insn-00599fe8)
- 新版 [`00599ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md#insn-00599ff8) · [`0059a028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md#insn-0059a028)

~~~diff
- 00599fb8 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00599fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599ff8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00599ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599fb8 bytes 08411e91
+ 00599ff8 bytes 08812191
- 00599fe8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00599fe8 ["INT_ADD", "register:40f0:8", ["const:599fe8:8", "const:4:8"]]
- 00599fe8 ["CALLIND", null, ["register:0:8"]]
+ 0059a028 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a028 ["INT_ADD", "register:40f0:8", ["const:59a028:8", "const:4:8"]]
+ 0059a028 ["CALLIND", null, ["register:0:8"]]
- 00599fe8 bytes 00013fd6
+ 0059a028 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04582289effb272b74919b792d955c57"></a>

### [`00599ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599ffc.md) → [`0059a03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md) FUN_0059a03c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a068",
      "incomplete_value": false,
      "site": "0059a068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a028",
      "incomplete_value": false,
      "site": "0059a028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "0059a068",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a068",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599ffc.md#insn-0059a010) · [`0059a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599ffc.md#insn-0059a020) · [`0059a044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599ffc.md#insn-0059a044)
- 新版 [`0059a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a050) · [`0059a060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a060) · [`0059a084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a084)

~~~diff
- 0059a010 ["INT_ADD", "register:40f0:8", ["const:59a010:8", "const:4:8"]]
- 0059a010 ["CALL", null, ["callee:00c57f60:8"]]
+ 0059a050 ["INT_ADD", "register:40f0:8", ["const:59a050:8", "const:4:8"]]
+ 0059a050 ["CALL", null, ["callee:00c57f60:8"]]
- 0059a010 bytes a0f71a94
+ 0059a050 bytes c4f71a94
- 0059a020 ["COPY", "tmp:0:8", ["const:790:8"]]
- 0059a020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059a020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059a020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a060 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0059a060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059a020 bytes 08411e91
+ 0059a060 bytes 08812191
- 0059a044 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a044 ["INT_ADD", "register:40f0:8", ["const:59a044:8", "const:4:8"]]
- 0059a044 ["CALLIND", null, ["register:0:8"]]
+ 0059a084 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a084 ["INT_ADD", "register:40f0:8", ["const:59a084:8", "const:4:8"]]
+ 0059a084 ["CALLIND", null, ["register:0:8"]]
- 0059a044 bytes 00013fd6
+ 0059a084 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-075a879b41104452b57bfb7b9dffcc6e"></a>

### [`0059a084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a084.md) → [`0059a0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md) FUN_0059a0c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a0e0",
      "incomplete_value": false,
      "site": "0059a0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a0a0",
      "incomplete_value": false,
      "site": "0059a0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "0059a0e0",
      "DATA",
      [
        "storage",
        "00c6d790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a0e0",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a084.md#insn-0059a09c) · [`0059a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a084.md#insn-0059a0c0)
- 新版 [`0059a0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md#insn-0059a0dc) · [`0059a100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md#insn-0059a100)

~~~diff
- 0059a09c ["COPY", "tmp:0:8", ["const:790:8"]]
- 0059a09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a0dc ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0059a0dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a0dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a0dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a09c bytes 29411e91
+ 0059a0dc bytes 29812191
- 0059a0c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0059a0c0 ["INT_ADD", "register:40f0:8", ["const:59a0c0:8", "const:4:8"]]
- 0059a0c0 ["CALLIND", null, ["register:0:8"]]
+ 0059a100 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a100 ["INT_ADD", "register:40f0:8", ["const:59a100:8", "const:4:8"]]
+ 0059a100 ["CALLIND", null, ["register:0:8"]]
- 0059a0c0 bytes 20013fd6
+ 0059a100 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

