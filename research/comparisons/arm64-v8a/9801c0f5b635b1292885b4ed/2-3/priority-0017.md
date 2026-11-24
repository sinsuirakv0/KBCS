# v16.0.1 → v16.0.2 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-6d6953a55de04e47270644d6d430e569"></a>

### [`00578790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md) → [`005787d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/005787d0.md) FUN_005787d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057882c",
      "incomplete_value": true,
      "site": "0057882c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:85a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005787ec",
      "incomplete_value": true,
      "site": "005787ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b6:8"
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
      "definition_site": "00578840",
      "incomplete_value": true,
      "site": "00578848",
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
                "const:767:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578800",
      "incomplete_value": true,
      "site": "00578808",
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
                "const:7c3:8"
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
      "definition_site": "0057884c",
      "incomplete_value": true,
      "site": "0057884c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057880c",
      "incomplete_value": true,
      "site": "0057880c",
      "value": [
        "LOAD",
        "8",
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
      "0057881c",
      "READ",
      [
        "storage",
        "002ad8b6",
        null,
        "string"
      ]
    ],
    [
      "00578840",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ],
    [
      "00578844",
      "READ",
      [
        "storage",
        "002a67d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057881c",
      "READ",
      [
        "storage",
        "002ad85a",
        null,
        "string"
      ]
    ],
    [
      "00578840",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ],
    [
      "00578844",
      "READ",
      [
        "storage",
        "002a6775",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-00578848) · [`005787b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-005787b8) · [`005787c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578790.md#insn-005787c0)
- 新版 `00578888`（命令位置の公開資料なし） · `005787f8`（命令位置の公開資料なし） · `00578800`（命令位置の公開資料なし）

~~~diff
- 00578848 ["INT_ADD", "register:40f0:8", ["const:578848:8", "const:4:8"]]
- 00578848 ["CALL", null, ["callee:00589184:8"]]
+ 00578888 ["INT_ADD", "register:40f0:8", ["const:578888:8", "const:4:8"]]
+ 00578888 ["CALL", null, ["callee:00589184:8"]]
- 00578848 bytes 3f420094
+ 00578888 bytes 3f420094
- 005787b8 ["INT_ADD", "register:40f0:8", ["const:5787b8:8", "const:4:8"]]
- 005787b8 ["CALL", null, ["callee:00588eac:8"]]
+ 005787f8 ["INT_ADD", "register:40f0:8", ["const:5787f8:8", "const:4:8"]]
+ 005787f8 ["CALL", null, ["callee:00588eac:8"]]
- 005787b8 bytes ad410094
+ 005787f8 bytes ad410094
- 005787c0 ["INT_ADD", "register:40f0:8", ["const:5787c0:8", "const:4:8"]]
- 005787c0 ["CALL", null, ["callee:0058919c:8"]]
+ 00578800 ["INT_ADD", "register:40f0:8", ["const:578800:8", "const:4:8"]]
+ 00578800 ["CALL", null, ["callee:0058919c:8"]]
- 005787c0 bytes 67420094
+ 00578800 bytes 67420094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd82851c1c6ba36adac88205529b647d"></a>

### [`00578910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md) → [`00578950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md) FUN_00578950

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005789a8",
      "incomplete_value": true,
      "site": "005789a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578968",
      "incomplete_value": true,
      "site": "00578968",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d4:8"
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
      "definition_site": "005789b0",
      "incomplete_value": true,
      "site": "005789b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578970",
      "incomplete_value": true,
      "site": "00578970",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005789ac",
      "incomplete_value": true,
      "site": "005789c0",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:230:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057896c",
      "incomplete_value": true,
      "site": "00578980",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:1f0:8"
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
      "00578990",
      "READ",
      [
        "storage",
        "002ab5d4",
        null,
        "string"
      ]
    ],
    [
      "00578998",
      "READ",
      [
        "storage",
        "002ab5d9",
        null,
        "string"
      ]
    ],
    [
      "005789ac",
      "READ",
      [
        "storage",
        "002b61f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578990",
      "READ",
      [
        "storage",
        "002ab578",
        null,
        "string"
      ]
    ],
    [
      "00578998",
      "READ",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "005789ac",
      "READ",
      [
        "storage",
        "002b6230",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-00578940) · [`005789c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-005789c4) · [`00578938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578910.md#insn-00578938)
- 新版 `00578980`（命令位置の公開資料なし） · `00578a04`（命令位置の公開資料なし） · `00578978`（命令位置の公開資料なし）

~~~diff
- 00578940 ["INT_ADD", "register:40f0:8", ["const:578940:8", "const:4:8"]]
- 00578940 ["CALL", null, ["callee:0058919c:8"]]
+ 00578980 ["INT_ADD", "register:40f0:8", ["const:578980:8", "const:4:8"]]
+ 00578980 ["CALL", null, ["callee:0058919c:8"]]
- 00578940 bytes 07420094
+ 00578980 bytes 07420094
- 005789c4 ["INT_ADD", "register:40f0:8", ["const:5789c4:8", "const:4:8"]]
- 005789c4 ["CALL", null, ["callee:00589184:8"]]
+ 00578a04 ["INT_ADD", "register:40f0:8", ["const:578a04:8", "const:4:8"]]
+ 00578a04 ["CALL", null, ["callee:00589184:8"]]
- 005789c4 bytes e0410094
+ 00578a04 bytes e0410094
- 00578938 ["INT_ADD", "register:40f0:8", ["const:578938:8", "const:4:8"]]
- 00578938 ["CALL", null, ["callee:00588eac:8"]]
+ 00578978 ["INT_ADD", "register:40f0:8", ["const:578978:8", "const:4:8"]]
+ 00578978 ["CALL", null, ["callee:00588eac:8"]]
- 00578938 bytes 4d410094
+ 00578978 bytes 4d410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3fc21959042c5baa88a2fbf7b6f6592"></a>

### [`00578aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md) → [`00578aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578aec.md) FUN_00578aec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578b38",
      "incomplete_value": true,
      "site": "00578b38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578af8",
      "incomplete_value": true,
      "site": "00578af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d82:8"
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
      "definition_site": "00578b3c",
      "incomplete_value": true,
      "site": "00578b3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578afc",
      "incomplete_value": true,
      "site": "00578afc",
      "value": [
        "LOAD",
        "8",
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
      "00578b28",
      "READ",
      [
        "storage",
        "002a8d82",
        null,
        "string"
      ]
    ],
    [
      "00578b30",
      "READ",
      [
        "storage",
        "002a8d87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578b28",
      "READ",
      [
        "storage",
        "002a8db1",
        null,
        "string"
      ]
    ],
    [
      "00578b30",
      "READ",
      [
        "storage",
        "002a8db6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578b38) · [`00578ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578ad0) · [`00578ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578aac.md#insn-00578ad8)
- 新版 `00578b78`（命令位置の公開資料なし） · `00578b10`（命令位置の公開資料なし） · `00578b18`（命令位置の公開資料なし）

~~~diff
- 00578b38 ["INT_ADD", "register:40f0:8", ["const:578b38:8", "const:4:8"]]
- 00578b38 ["CALL", null, ["callee:00c57f80:8"]]
+ 00578b78 ["INT_ADD", "register:40f0:8", ["const:578b78:8", "const:4:8"]]
+ 00578b78 ["CALL", null, ["callee:00c57f80:8"]]
- 00578b38 bytes de7c1b94
+ 00578b78 bytes 027d1b94
- 00578ad0 ["INT_ADD", "register:40f0:8", ["const:578ad0:8", "const:4:8"]]
- 00578ad0 ["CALL", null, ["callee:00588eac:8"]]
+ 00578b10 ["INT_ADD", "register:40f0:8", ["const:578b10:8", "const:4:8"]]
+ 00578b10 ["CALL", null, ["callee:00588eac:8"]]
- 00578ad0 bytes e7400094
+ 00578b10 bytes e7400094
- 00578ad8 ["INT_ADD", "register:40f0:8", ["const:578ad8:8", "const:4:8"]]
- 00578ad8 ["CALL", null, ["callee:0058919c:8"]]
+ 00578b18 ["INT_ADD", "register:40f0:8", ["const:578b18:8", "const:4:8"]]
+ 00578b18 ["CALL", null, ["callee:0058919c:8"]]
- 00578ad8 bytes a1410094
+ 00578b18 bytes a1410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b3c733e3afa89781c30158c3a7c907"></a>

### [`00578bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md) → [`00578c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578c1c.md) FUN_00578c1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578c68",
      "incomplete_value": true,
      "site": "00578c68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d04:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578c28",
      "incomplete_value": true,
      "site": "00578c28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
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
      "definition_site": "00578c6c",
      "incomplete_value": true,
      "site": "00578c6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578c2c",
      "incomplete_value": true,
      "site": "00578c2c",
      "value": [
        "LOAD",
        "8",
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
      "00578c58",
      "READ",
      [
        "storage",
        "002b0d60",
        null,
        "string"
      ]
    ],
    [
      "00578c60",
      "READ",
      [
        "storage",
        "002b0d65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578c58",
      "READ",
      [
        "storage",
        "002b0d04",
        null,
        "string"
      ]
    ],
    [
      "00578c60",
      "READ",
      [
        "storage",
        "002b0d09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c68) · [`00578c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c00) · [`00578c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578bdc.md#insn-00578c08)
- 新版 `00578ca8`（命令位置の公開資料なし） · `00578c40`（命令位置の公開資料なし） · `00578c48`（命令位置の公開資料なし）

~~~diff
- 00578c68 ["INT_ADD", "register:40f0:8", ["const:578c68:8", "const:4:8"]]
- 00578c68 ["CALL", null, ["callee:00c57f80:8"]]
+ 00578ca8 ["INT_ADD", "register:40f0:8", ["const:578ca8:8", "const:4:8"]]
+ 00578ca8 ["CALL", null, ["callee:00c57f80:8"]]
- 00578c68 bytes 927c1b94
+ 00578ca8 bytes b67c1b94
- 00578c00 ["INT_ADD", "register:40f0:8", ["const:578c00:8", "const:4:8"]]
- 00578c00 ["CALL", null, ["callee:00588eac:8"]]
+ 00578c40 ["INT_ADD", "register:40f0:8", ["const:578c40:8", "const:4:8"]]
+ 00578c40 ["CALL", null, ["callee:00588eac:8"]]
- 00578c00 bytes 9b400094
+ 00578c40 bytes 9b400094
- 00578c08 ["INT_ADD", "register:40f0:8", ["const:578c08:8", "const:4:8"]]
- 00578c08 ["CALL", null, ["callee:0058919c:8"]]
+ 00578c48 ["INT_ADD", "register:40f0:8", ["const:578c48:8", "const:4:8"]]
+ 00578c48 ["CALL", null, ["callee:0058919c:8"]]
- 00578c08 bytes 55410094
+ 00578c48 bytes 55410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13a258ac5b20d26af6287b9394ab78b0"></a>

### [`00578d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md) → [`00578d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578d8c.md) FUN_00578d8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578dd8",
      "incomplete_value": true,
      "site": "00578dd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578d98",
      "incomplete_value": true,
      "site": "00578d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cde:8"
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
      "definition_site": "00578ddc",
      "incomplete_value": true,
      "site": "00578ddc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578d9c",
      "incomplete_value": true,
      "site": "00578d9c",
      "value": [
        "LOAD",
        "8",
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
      "00578dc8",
      "READ",
      [
        "storage",
        "002b3cde",
        null,
        "string"
      ]
    ],
    [
      "00578dd0",
      "READ",
      [
        "storage",
        "002b3ce3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578dc8",
      "READ",
      [
        "storage",
        "002b3d0f",
        null,
        "string"
      ]
    ],
    [
      "00578dd0",
      "READ",
      [
        "storage",
        "002b3d14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578dd8) · [`00578d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578d70) · [`00578d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578d4c.md#insn-00578d78)
- 新版 `00578e18`（命令位置の公開資料なし） · `00578db0`（命令位置の公開資料なし） · `00578db8`（命令位置の公開資料なし）

~~~diff
- 00578dd8 ["INT_ADD", "register:40f0:8", ["const:578dd8:8", "const:4:8"]]
- 00578dd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00578e18 ["INT_ADD", "register:40f0:8", ["const:578e18:8", "const:4:8"]]
+ 00578e18 ["CALL", null, ["callee:00c57f80:8"]]
- 00578dd8 bytes 367c1b94
+ 00578e18 bytes 5a7c1b94
- 00578d70 ["INT_ADD", "register:40f0:8", ["const:578d70:8", "const:4:8"]]
- 00578d70 ["CALL", null, ["callee:00588eac:8"]]
+ 00578db0 ["INT_ADD", "register:40f0:8", ["const:578db0:8", "const:4:8"]]
+ 00578db0 ["CALL", null, ["callee:00588eac:8"]]
- 00578d70 bytes 3f400094
+ 00578db0 bytes 3f400094
- 00578d78 ["INT_ADD", "register:40f0:8", ["const:578d78:8", "const:4:8"]]
- 00578d78 ["CALL", null, ["callee:0058919c:8"]]
+ 00578db8 ["INT_ADD", "register:40f0:8", ["const:578db8:8", "const:4:8"]]
+ 00578db8 ["CALL", null, ["callee:0058919c:8"]]
- 00578d78 bytes f9400094
+ 00578db8 bytes f9400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb60c1a36b7b25c1611c29264b74175"></a>

### [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) → [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) FUN_00578efc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057905c",
      "incomplete_value": true,
      "site": "0057905c",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057901c",
      "incomplete_value": true,
      "site": "0057901c",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005792d0",
      "incomplete_value": true,
      "site": "005792d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:866:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579290",
      "incomplete_value": true,
      "site": "00579290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "005792d4",
      "incomplete_value": true,
      "site": "005792d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579294",
      "incomplete_value": true,
      "site": "00579294",
      "value": [
        "LOAD",
        "8",
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
      "00578fd8",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057903c",
      "DATA",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057904c",
      "WRITE",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00578fd8",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057903c",
      "DATA",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057904c",
      "WRITE",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md#insn-0057901c) · [`00578f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md#insn-00578f18)
- 新版 `0057905c`（命令位置の公開資料なし） · `005792bc`（命令位置の公開資料なし） · `00578f58`（命令位置の公開資料なし）

~~~diff
- 0057901c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
- 0057901c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057905c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 0057905c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057901c bytes 091d01f9
+ 0057905c bytes 099d01f9
+ 005792bc ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 005792bc bytes f60300aa
- 00578f18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00578f18 ["INT_ADD", "register:40f0:8", ["const:578f18:8", "const:4:8"]]
- 00578f18 ["CALLIND", null, ["register:0:8"]]
+ 00578f58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00578f58 ["INT_ADD", "register:40f0:8", ["const:578f58:8", "const:4:8"]]
+ 00578f58 ["CALLIND", null, ["register:0:8"]]
- 00578f18 bytes 20013fd6
+ 00578f58 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68a0bec5fc4d68108f8c917a12eefd78"></a>

### [`00579524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md) → [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) FUN_00579564

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a94.md)
- 新版 呼出元 1件 [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) · 呼出先 11件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005796a0",
      "incomplete_value": false,
      "site": "005796a8",
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
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579660",
      "incomplete_value": false,
      "site": "00579668",
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
            "const:1eb:8"
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
      "definition_site": "00579704",
      "incomplete_value": false,
      "site": "0057970c",
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
            "const:d12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005796c4",
      "incomplete_value": false,
      "site": "005796cc",
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
            "const:d6e:8"
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
      "definition_site": "00579768",
      "incomplete_value": false,
      "site": "00579770",
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
            "const:586:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579728",
      "incomplete_value": false,
      "site": "00579730",
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
            "const:5e2:8"
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
      "005796a0",
      "PARAM",
      [
        "storage",
        "002a01eb",
        null,
        "string"
      ]
    ],
    [
      "00579704",
      "PARAM",
      [
        "storage",
        "002b0d6e",
        null,
        "string"
      ]
    ],
    [
      "00579768",
      "PARAM",
      [
        "storage",
        "002ab5e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005796a0",
      "PARAM",
      [
        "storage",
        "002a019e",
        null,
        "string"
      ]
    ],
    [
      "00579704",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00579768",
      "PARAM",
      [
        "storage",
        "002ab586",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-00579668) · [`005796cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-005796cc) · [`00579730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579524.md#insn-00579730)
- 新版 `005796a8`（命令位置の公開資料なし） · `0057970c`（命令位置の公開資料なし） · `00579770`（命令位置の公開資料なし）

~~~diff
- 00579668 ["INT_ADD", "register:40f0:8", ["const:579668:8", "const:4:8"]]
- 00579668 ["CALL", null, ["callee:00c58040:8"]]
+ 005796a8 ["INT_ADD", "register:40f0:8", ["const:5796a8:8", "const:4:8"]]
+ 005796a8 ["CALL", null, ["callee:00c58040:8"]]
- 00579668 bytes 427a1b94
+ 005796a8 bytes 667a1b94
- 005796cc ["INT_ADD", "register:40f0:8", ["const:5796cc:8", "const:4:8"]]
- 005796cc ["CALL", null, ["callee:00c58040:8"]]
+ 0057970c ["INT_ADD", "register:40f0:8", ["const:57970c:8", "const:4:8"]]
+ 0057970c ["CALL", null, ["callee:00c58040:8"]]
- 005796cc bytes 297a1b94
+ 0057970c bytes 4d7a1b94
- 00579730 ["INT_ADD", "register:40f0:8", ["const:579730:8", "const:4:8"]]
- 00579730 ["CALL", null, ["callee:00c58040:8"]]
+ 00579770 ["INT_ADD", "register:40f0:8", ["const:579770:8", "const:4:8"]]
+ 00579770 ["CALL", null, ["callee:00c58040:8"]]
- 00579730 bytes 107a1b94
+ 00579770 bytes 347a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29907c712f880316fa6a64297f30f637"></a>

### [`00579acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md) → [`00579b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579b0c.md) FUN_00579b0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00579c68",
      "incomplete_value": true,
      "site": "00579c68",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579c28",
      "incomplete_value": true,
      "site": "00579c28",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00579e08",
      "incomplete_value": true,
      "site": "00579e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:866:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00579dc8",
      "incomplete_value": true,
      "site": "00579dc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
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
      "definition_site": "00579e10",
      "incomplete_value": true,
      "site": "00579e10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00579dd0",
      "incomplete_value": true,
      "site": "00579dd0",
      "value": [
        "LOAD",
        "8",
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
      "00579be4",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c48",
      "DATA",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c58",
      "WRITE",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00579be4",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c48",
      "DATA",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00579c58",
      "WRITE",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00579c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579c28) · [`00579da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579da0) · [`00579e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00579/00579acc.md#insn-00579e24)
- 新版 `00579c68`（命令位置の公開資料なし） · `00579de0`（命令位置の公開資料なし） · `00579e64`（命令位置の公開資料なし）

~~~diff
- 00579c28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:238:8"]]
- 00579c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00579c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
+ 00579c68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00579c28 bytes 091d01f9
+ 00579c68 bytes 099d01f9
- 00579da0 ["INT_ADD", "register:40f0:8", ["const:579da0:8", "const:4:8"]]
- 00579da0 ["CALL", null, ["callee:0058919c:8"]]
+ 00579de0 ["INT_ADD", "register:40f0:8", ["const:579de0:8", "const:4:8"]]
+ 00579de0 ["CALL", null, ["callee:0058919c:8"]]
- 00579da0 bytes ef3c0094
+ 00579de0 bytes ef3c0094
- 00579e24 ["COPY", "tmp:0:8", ["const:1d5:8"]]
- 00579e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00579e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00579e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00579e64 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00579e64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00579e64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00579e64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00579e24 bytes 29550791
+ 00579e64 bytes 29210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75859b4d6b02f8b218033c7feebdea7d"></a>

### [`0057a13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md) → [`0057a17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a17c.md) FUN_0057a17c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a1e0",
      "incomplete_value": true,
      "site": "0057a1e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a1a0",
      "incomplete_value": true,
      "site": "0057a1a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cec:8"
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
      "definition_site": "0057a1e4",
      "incomplete_value": true,
      "site": "0057a1e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a1a4",
      "incomplete_value": true,
      "site": "0057a1a4",
      "value": [
        "LOAD",
        "8",
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
      "0057a1d0",
      "READ",
      [
        "storage",
        "002b3cec",
        null,
        "string"
      ]
    ],
    [
      "0057a1d8",
      "READ",
      [
        "storage",
        "002b3cf1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a1d0",
      "READ",
      [
        "storage",
        "002b3d1d",
        null,
        "string"
      ]
    ],
    [
      "0057a1d8",
      "READ",
      [
        "storage",
        "002b3d22",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a178) · [`0057a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a180) · [`0057a18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a13c.md#insn-0057a18c)
- 新版 `0057a1b8`（命令位置の公開資料なし） · `0057a1c0`（命令位置の公開資料なし） · `0057a1cc`（命令位置の公開資料なし）

~~~diff
- 0057a178 ["INT_ADD", "register:40f0:8", ["const:57a178:8", "const:4:8"]]
- 0057a178 ["CALL", null, ["callee:00588eac:8"]]
+ 0057a1b8 ["INT_ADD", "register:40f0:8", ["const:57a1b8:8", "const:4:8"]]
+ 0057a1b8 ["CALL", null, ["callee:00588eac:8"]]
- 0057a178 bytes 3d3b0094
+ 0057a1b8 bytes 3d3b0094
- 0057a180 ["INT_ADD", "register:40f0:8", ["const:57a180:8", "const:4:8"]]
- 0057a180 ["CALL", null, ["callee:0058919c:8"]]
+ 0057a1c0 ["INT_ADD", "register:40f0:8", ["const:57a1c0:8", "const:4:8"]]
+ 0057a1c0 ["CALL", null, ["callee:0058919c:8"]]
- 0057a180 bytes f73b0094
+ 0057a1c0 bytes f73b0094
- 0057a18c ["COPY", "tmp:0:8", ["const:cec:8"]]
- 0057a18c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057a18c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057a18c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057a1cc ["COPY", "tmp:0:8", ["const:d1d:8"]]
+ 0057a1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057a1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057a18c bytes 29b13391
+ 0057a1cc bytes 29753491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed372ab61fb2f147b4a4ac81e02de9ef"></a>

### [`0057a38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md) → [`0057a3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a3cc.md) FUN_0057a3cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a420",
      "incomplete_value": true,
      "site": "0057a420",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:3ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a3e0",
      "incomplete_value": true,
      "site": "0057a3e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:441:8"
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
      "definition_site": "0057a424",
      "incomplete_value": true,
      "site": "0057a424",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a3e4",
      "incomplete_value": true,
      "site": "0057a3e4",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057a410",
      "READ",
      [
        "storage",
        "002ba441",
        null,
        "string"
      ]
    ],
    [
      "0057a418",
      "READ",
      [
        "storage",
        "002ba447",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a410",
      "READ",
      [
        "storage",
        "002ba3ed",
        null,
        "string"
      ]
    ],
    [
      "0057a418",
      "READ",
      [
        "storage",
        "002ba3f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a424) · [`0057a3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a3b8) · [`0057a3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a38c.md#insn-0057a3c0)
- 新版 `0057a464`（命令位置の公開資料なし） · `0057a3f8`（命令位置の公開資料なし） · `0057a400`（命令位置の公開資料なし）

~~~diff
- 0057a424 ["INT_ADD", "register:40f0:8", ["const:57a424:8", "const:4:8"]]
- 0057a424 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057a464 ["INT_ADD", "register:40f0:8", ["const:57a464:8", "const:4:8"]]
+ 0057a464 ["CALL", null, ["callee:00c57f80:8"]]
- 0057a424 bytes a3761b94
+ 0057a464 bytes c7761b94
- 0057a3b8 ["INT_ADD", "register:40f0:8", ["const:57a3b8:8", "const:4:8"]]
- 0057a3b8 ["CALL", null, ["callee:00588eac:8"]]
+ 0057a3f8 ["INT_ADD", "register:40f0:8", ["const:57a3f8:8", "const:4:8"]]
+ 0057a3f8 ["CALL", null, ["callee:00588eac:8"]]
- 0057a3b8 bytes ad3a0094
+ 0057a3f8 bytes ad3a0094
- 0057a3c0 ["INT_ADD", "register:40f0:8", ["const:57a3c0:8", "const:4:8"]]
- 0057a3c0 ["CALL", null, ["callee:0058919c:8"]]
+ 0057a400 ["INT_ADD", "register:40f0:8", ["const:57a400:8", "const:4:8"]]
+ 0057a400 ["CALL", null, ["callee:0058919c:8"]]
- 0057a3c0 bytes 673b0094
+ 0057a400 bytes 673b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9adeecc1d191966acdc7325bfd53f397"></a>

### [`0057a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md) → [`0057a504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a504.md) FUN_0057a504

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a558",
      "incomplete_value": true,
      "site": "0057a558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a518",
      "incomplete_value": true,
      "site": "0057a518",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45b:8"
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
      "definition_site": "0057a55c",
      "incomplete_value": true,
      "site": "0057a55c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057a51c",
      "incomplete_value": true,
      "site": "0057a51c",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057a548",
      "READ",
      [
        "storage",
        "002b745b",
        null,
        "string"
      ]
    ],
    [
      "0057a550",
      "READ",
      [
        "storage",
        "002b7461",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057a548",
      "READ",
      [
        "storage",
        "002b749b",
        null,
        "string"
      ]
    ],
    [
      "0057a550",
      "READ",
      [
        "storage",
        "002b74a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a55c) · [`0057a4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a4f0) · [`0057a4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a4c4.md#insn-0057a4f8)
- 新版 `0057a59c`（命令位置の公開資料なし） · `0057a530`（命令位置の公開資料なし） · `0057a538`（命令位置の公開資料なし）

~~~diff
- 0057a55c ["INT_ADD", "register:40f0:8", ["const:57a55c:8", "const:4:8"]]
- 0057a55c ["CALL", null, ["callee:00c57f80:8"]]
+ 0057a59c ["INT_ADD", "register:40f0:8", ["const:57a59c:8", "const:4:8"]]
+ 0057a59c ["CALL", null, ["callee:00c57f80:8"]]
- 0057a55c bytes 55761b94
+ 0057a59c bytes 79761b94
- 0057a4f0 ["INT_ADD", "register:40f0:8", ["const:57a4f0:8", "const:4:8"]]
- 0057a4f0 ["CALL", null, ["callee:00588eac:8"]]
+ 0057a530 ["INT_ADD", "register:40f0:8", ["const:57a530:8", "const:4:8"]]
+ 0057a530 ["CALL", null, ["callee:00588eac:8"]]
- 0057a4f0 bytes 5f3a0094
+ 0057a530 bytes 5f3a0094
- 0057a4f8 ["INT_ADD", "register:40f0:8", ["const:57a4f8:8", "const:4:8"]]
- 0057a4f8 ["CALL", null, ["callee:0058919c:8"]]
+ 0057a538 ["INT_ADD", "register:40f0:8", ["const:57a538:8", "const:4:8"]]
+ 0057a538 ["CALL", null, ["callee:0058919c:8"]]
- 0057a4f8 bytes 193b0094
+ 0057a538 bytes 193b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7788eaca528e2c5a2632c0267eb2b979"></a>

### [`0057a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md) → [`0057a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a63c.md) FUN_0057a63c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0057a674",
      "incomplete_value": false,
      "site": "0057a688",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a634",
      "incomplete_value": false,
      "site": "0057a648",
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
            "const:d88:8"
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
      "definition_site": "0057a67c",
      "incomplete_value": false,
      "site": "0057a688",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a63c",
      "incomplete_value": false,
      "site": "0057a648",
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
            "const:da0:8"
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
      "0057a674",
      "PARAM",
      [
        "storage",
        "00c6bd88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a67c",
      "PARAM",
      [
        "storage",
        "00c6bda0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0057a674",
      "PARAM",
      [
        "storage",
        "00c6be58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0057a67c",
      "PARAM",
      [
        "storage",
        "00c6be70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a648) · [`0057a634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a634) · [`0057a63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a5fc.md#insn-0057a63c)
- 新版 `0057a688`（命令位置の公開資料なし） · `0057a674`（命令位置の公開資料なし） · `0057a67c`（命令位置の公開資料なし）

~~~diff
- 0057a648 ["INT_ADD", "register:40f0:8", ["const:57a648:8", "const:4:8"]]
- 0057a648 ["CALL", null, ["callee:00c586e0:8"]]
+ 0057a688 ["INT_ADD", "register:40f0:8", ["const:57a688:8", "const:4:8"]]
+ 0057a688 ["CALL", null, ["callee:00c586e0:8"]]
- 0057a648 bytes f2771b94
+ 0057a688 bytes 16781b94
- 0057a634 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0057a634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0057a634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0057a634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0057a674 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0057a674 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a674 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0057a674 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0057a634 bytes 21203691
+ 0057a674 bytes 21603991
- 0057a63c ["COPY", "tmp:0:8", ["const:da0:8"]]
- 0057a63c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0057a63c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0057a63c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0057a67c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0057a67c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0057a67c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0057a67c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0057a63c bytes 42803691
+ 0057a67c bytes 42c03991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ad23aee35ad8b5b19576ce5151db1f0"></a>

### [`0057a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md) → [`0057a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a77c.md) FUN_0057a77c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a0c.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00550a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a4c.md) · 呼出先 8件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a7f8",
      "incomplete_value": true,
      "site": "0057a7f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a7b8",
      "incomplete_value": true,
      "site": "0057a7b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:524:8"
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
      "definition_site": "0057a81c",
      "incomplete_value": true,
      "site": "0057a81c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e29:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a7dc",
      "incomplete_value": true,
      "site": "0057a7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a8dc",
      "incomplete_value": false,
      "site": "0057a8e4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a89c",
      "incomplete_value": false,
      "site": "0057a8a4",
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
            "const:f20:8"
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
      "0057a7ec",
      "READ",
      [
        "storage",
        "002bb524",
        null,
        "string"
      ]
    ],
    [
      "0057a818",
      "READ",
      [
        "storage",
        "002b1df8",
        null,
        "string"
      ]
    ],
    [
      "0057a8e4",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a7ec",
      "READ",
      [
        "storage",
        "002bb4d0",
        null,
        "string"
      ]
    ],
    [
      "0057a818",
      "READ",
      [
        "storage",
        "002b1e29",
        null,
        "string"
      ]
    ],
    [
      "0057a8e4",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a788) · [`0057a790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a790) · [`0057a7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a73c.md#insn-0057a7a8)
- 新版 `0057a7c8`（命令位置の公開資料なし） · `0057a7d0`（命令位置の公開資料なし） · `0057a7e8`（命令位置の公開資料なし）

~~~diff
- 0057a788 ["INT_ADD", "register:40f0:8", ["const:57a788:8", "const:4:8"]]
- 0057a788 ["CALL", null, ["callee:00588eac:8"]]
+ 0057a7c8 ["INT_ADD", "register:40f0:8", ["const:57a7c8:8", "const:4:8"]]
+ 0057a7c8 ["CALL", null, ["callee:00588eac:8"]]
- 0057a788 bytes b9390094
+ 0057a7c8 bytes b9390094
- 0057a790 ["INT_ADD", "register:40f0:8", ["const:57a790:8", "const:4:8"]]
- 0057a790 ["CALL", null, ["callee:0058919c:8"]]
+ 0057a7d0 ["INT_ADD", "register:40f0:8", ["const:57a7d0:8", "const:4:8"]]
+ 0057a7d0 ["CALL", null, ["callee:0058919c:8"]]
- 0057a790 bytes 733a0094
+ 0057a7d0 bytes 733a0094
- 0057a7a8 ["COPY", "tmp:0:8", ["const:524:8"]]
- 0057a7a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a7a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a7a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a7e8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0057a7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a7a8 bytes 08911491
+ 0057a7e8 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85c3e5a372d8dce386135f8c8bb0314c"></a>

### [`0057a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md) → [`0057a9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9a8.md) FUN_0057a9a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057a9c4",
      "incomplete_value": false,
      "site": "0057a9cc",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a984",
      "incomplete_value": false,
      "site": "0057a98c",
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
            "const:f70:8"
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
      "definition_site": "0057a9e0",
      "incomplete_value": false,
      "site": "0057a9e0",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057a9a0",
      "incomplete_value": false,
      "site": "0057a9a0",
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
            "const:cd8:8"
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
      "0057a9cc",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a9e0",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057a9cc",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ],
    [
      "0057a9e0",
      "DATA",
      [
        "storage",
        "00c6bda8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md#insn-0057a97c) · [`0057a980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md#insn-0057a980) · [`0057a984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a968.md#insn-0057a984)
- 新版 `0057a9bc`（命令位置の公開資料なし） · `0057a9c0`（命令位置の公開資料なし） · `0057a9c4`（命令位置の公開資料なし）

~~~diff
- 0057a97c ["INT_ADD", "register:40f0:8", ["const:57a97c:8", "const:4:8"]]
- 0057a97c ["CALL", null, ["callee:00c57f60:8"]]
+ 0057a9bc ["INT_ADD", "register:40f0:8", ["const:57a9bc:8", "const:4:8"]]
+ 0057a9bc ["CALL", null, ["callee:00c57f60:8"]]
- 0057a97c bytes 45751b94
+ 0057a9bc bytes 69751b94
- 0057a980 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057a9c0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057a980 bytes 883700b0
+ 0057a9c0 bytes 883700d0
- 0057a984 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 0057a984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057a984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057a984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057a9c4 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0057a9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057a9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057a984 bytes 08c13d91
+ 0057a9c4 bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c958340b380659609d072bae6ce5e0b"></a>

### [`0057a9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md) → [`0057a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a9f4.md) FUN_0057a9f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aa68",
      "incomplete_value": true,
      "site": "0057aa68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
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
    "old": {
      "definition_site": "0057aa28",
      "incomplete_value": true,
      "site": "0057aa28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aa70",
      "incomplete_value": true,
      "site": "0057aa70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057aa30",
      "incomplete_value": true,
      "site": "0057aa30",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aa6c",
      "incomplete_value": true,
      "site": "0057aa80",
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
                "const:767:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057aa2c",
      "incomplete_value": true,
      "site": "0057aa40",
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
                "const:7c3:8"
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
      "0057aa50",
      "READ",
      [
        "storage",
        "002bff60",
        null,
        "string"
      ]
    ],
    [
      "0057aa58",
      "READ",
      [
        "storage",
        "002bff66",
        null,
        "string"
      ]
    ],
    [
      "0057aa6c",
      "READ",
      [
        "storage",
        "002a67c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057aa50",
      "READ",
      [
        "storage",
        "002bffa0",
        null,
        "string"
      ]
    ],
    [
      "0057aa58",
      "READ",
      [
        "storage",
        "002bffa6",
        null,
        "string"
      ]
    ],
    [
      "0057aa6c",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057a9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057a9e8) · [`0057aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057aa00) · [`0057aa80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a9b4.md#insn-0057aa80)
- 新版 `0057aa28`（命令位置の公開資料なし） · `0057aa40`（命令位置の公開資料なし） · `0057aac0`（命令位置の公開資料なし）

~~~diff
- 0057a9e8 ["INT_ADD", "register:40f0:8", ["const:57a9e8:8", "const:4:8"]]
- 0057a9e8 ["CALL", null, ["callee:00588eac:8"]]
+ 0057aa28 ["INT_ADD", "register:40f0:8", ["const:57aa28:8", "const:4:8"]]
+ 0057aa28 ["CALL", null, ["callee:00588eac:8"]]
- 0057a9e8 bytes 21390094
+ 0057aa28 bytes 21390094
- 0057aa00 ["INT_ADD", "register:40f0:8", ["const:57aa00:8", "const:4:8"]]
- 0057aa00 ["CALL", null, ["callee:0058919c:8"]]
+ 0057aa40 ["INT_ADD", "register:40f0:8", ["const:57aa40:8", "const:4:8"]]
+ 0057aa40 ["CALL", null, ["callee:0058919c:8"]]
- 0057aa00 bytes d7390094
+ 0057aa40 bytes d7390094
- 0057aa80 ["INT_ADD", "register:40f0:8", ["const:57aa80:8", "const:4:8"]]
- 0057aa80 ["CALL", null, ["callee:0058919c:8"]]
+ 0057aac0 ["INT_ADD", "register:40f0:8", ["const:57aac0:8", "const:4:8"]]
+ 0057aac0 ["CALL", null, ["callee:0058919c:8"]]
- 0057aa80 bytes b7390094
+ 0057aac0 bytes b7390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f35a555a37882c0a6333199279c57d0"></a>

### [`0057ac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md) → [`0057aca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057aca4.md) FUN_0057aca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ad04",
      "incomplete_value": true,
      "site": "0057ad04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057acc4",
      "incomplete_value": true,
      "site": "0057acc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:976:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0057ad80",
      "incomplete_value": true,
      "site": "0057ad80",
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
      "definition_site": "0057ad40",
      "incomplete_value": true,
      "site": "0057ad40",
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
      "0057acf4",
      "READ",
      [
        "storage",
        "002a7976",
        null,
        "string"
      ]
    ],
    [
      "0057ad7c",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ],
    [
      "0057add8",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057acf4",
      "READ",
      [
        "storage",
        "002a791a",
        null,
        "string"
      ]
    ],
    [
      "0057ad7c",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "0057add8",
      "READ",
      [
        "storage",
        "00ca63e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ad00) · [`0057ac94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ac94) · [`0057ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ac64.md#insn-0057ac9c)
- 新版 `0057ad40`（命令位置の公開資料なし） · `0057acd4`（命令位置の公開資料なし） · `0057acdc`（命令位置の公開資料なし）

~~~diff
- 0057ad00 ["INT_ADD", "register:40f0:8", ["const:57ad00:8", "const:4:8"]]
- 0057ad00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057ad40 ["INT_ADD", "register:40f0:8", ["const:57ad40:8", "const:4:8"]]
+ 0057ad40 ["CALL", null, ["callee:00c57f80:8"]]
- 0057ad00 bytes 6c741b94
+ 0057ad40 bytes 90741b94
- 0057ac94 ["INT_ADD", "register:40f0:8", ["const:57ac94:8", "const:4:8"]]
- 0057ac94 ["CALL", null, ["callee:00588eac:8"]]
+ 0057acd4 ["INT_ADD", "register:40f0:8", ["const:57acd4:8", "const:4:8"]]
+ 0057acd4 ["CALL", null, ["callee:00588eac:8"]]
- 0057ac94 bytes 76380094
+ 0057acd4 bytes 76380094
- 0057ac9c ["INT_ADD", "register:40f0:8", ["const:57ac9c:8", "const:4:8"]]
- 0057ac9c ["CALL", null, ["callee:0058919c:8"]]
+ 0057acdc ["INT_ADD", "register:40f0:8", ["const:57acdc:8", "const:4:8"]]
+ 0057acdc ["CALL", null, ["callee:0058919c:8"]]
- 0057ac9c bytes 30390094
+ 0057acdc bytes 30390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e91aefaf52d4f145d32820bc580b9d2"></a>

### [`0057ae5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md) → [`0057ae9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057ae9c.md) FUN_0057ae9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057aef8",
      "incomplete_value": true,
      "site": "0057aef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4aa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057aeb8",
      "incomplete_value": true,
      "site": "0057aeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:46a:8"
              ]
            ]
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
      "0057aee0",
      "READ",
      [
        "storage",
        "002b746a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057aee0",
      "READ",
      [
        "storage",
        "002b74aa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057aef8) · [`0057ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057ae80) · [`0057ae88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057ae5c.md#insn-0057ae88)
- 新版 `0057af38`（命令位置の公開資料なし） · `0057aec0`（命令位置の公開資料なし） · `0057aec8`（命令位置の公開資料なし）

~~~diff
- 0057aef8 ["INT_ADD", "register:40f0:8", ["const:57aef8:8", "const:4:8"]]
- 0057aef8 ["CALL", null, ["callee:0058919c:8"]]
+ 0057af38 ["INT_ADD", "register:40f0:8", ["const:57af38:8", "const:4:8"]]
+ 0057af38 ["CALL", null, ["callee:0058919c:8"]]
- 0057aef8 bytes 99380094
+ 0057af38 bytes 99380094
- 0057ae80 ["INT_ADD", "register:40f0:8", ["const:57ae80:8", "const:4:8"]]
- 0057ae80 ["CALL", null, ["callee:00588eac:8"]]
+ 0057aec0 ["INT_ADD", "register:40f0:8", ["const:57aec0:8", "const:4:8"]]
+ 0057aec0 ["CALL", null, ["callee:00588eac:8"]]
- 0057ae80 bytes fb370094
+ 0057aec0 bytes fb370094
- 0057ae88 ["INT_ADD", "register:40f0:8", ["const:57ae88:8", "const:4:8"]]
- 0057ae88 ["CALL", null, ["callee:0058919c:8"]]
+ 0057aec8 ["INT_ADD", "register:40f0:8", ["const:57aec8:8", "const:4:8"]]
+ 0057aec8 ["CALL", null, ["callee:0058919c:8"]]
- 0057ae88 bytes b5380094
+ 0057aec8 bytes b5380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fb93d9aeb3c15ea332e659cc7295a3"></a>

### [`0057af7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md) → [`0057afbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057afbc.md) FUN_0057afbc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 1件 [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b028",
      "incomplete_value": true,
      "site": "0057b030",
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
                "const:d4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057afe8",
      "incomplete_value": true,
      "site": "0057aff0",
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
                "const:121:8"
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
      "definition_site": "0057b034",
      "incomplete_value": true,
      "site": "0057b034",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057aff4",
      "incomplete_value": true,
      "site": "0057aff4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b0f4",
      "incomplete_value": false,
      "site": "0057b0fc",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b0b4",
      "incomplete_value": false,
      "site": "0057b0bc",
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
            "const:fc0:8"
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
      "0057b028",
      "READ",
      [
        "storage",
        "002a2121",
        null,
        "string"
      ]
    ],
    [
      "0057b02c",
      "READ",
      [
        "storage",
        "002a212e",
        null,
        "string"
      ]
    ],
    [
      "0057b0fc",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057b028",
      "READ",
      [
        "storage",
        "002a20d4",
        null,
        "string"
      ]
    ],
    [
      "0057b02c",
      "READ",
      [
        "storage",
        "002a20e1",
        null,
        "string"
      ]
    ],
    [
      "0057b0fc",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afb0) · [`0057afa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afa8) · [`0057afe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057af7c.md#insn-0057afe4)
- 新版 `0057aff0`（命令位置の公開資料なし） · `0057afe8`（命令位置の公開資料なし） · `0057b024`（命令位置の公開資料なし）

~~~diff
- 0057afb0 ["INT_ADD", "register:40f0:8", ["const:57afb0:8", "const:4:8"]]
- 0057afb0 ["CALL", null, ["callee:0058919c:8"]]
+ 0057aff0 ["INT_ADD", "register:40f0:8", ["const:57aff0:8", "const:4:8"]]
+ 0057aff0 ["CALL", null, ["callee:0058919c:8"]]
- 0057afb0 bytes 6b380094
+ 0057aff0 bytes 6b380094
- 0057afa8 ["INT_ADD", "register:40f0:8", ["const:57afa8:8", "const:4:8"]]
- 0057afa8 ["CALL", null, ["callee:00588eac:8"]]
+ 0057afe8 ["INT_ADD", "register:40f0:8", ["const:57afe8:8", "const:4:8"]]
+ 0057afe8 ["CALL", null, ["callee:00588eac:8"]]
- 0057afa8 bytes b1370094
+ 0057afe8 bytes b1370094
- 0057afe4 ["COPY", "tmp:0:8", ["const:121:8"]]
- 0057afe4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057afe4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057afe4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b024 ["COPY", "tmp:0:8", ["const:d4:8"]]
+ 0057b024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057afe4 bytes 29850491
+ 0057b024 bytes 29510391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab50ba371854a118d833553affcbd0a"></a>

### [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) → [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) FUN_0057b1a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`00550a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a50.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0057c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c694.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.90% / 新版 91.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b3cc",
      "incomplete_value": true,
      "site": "0057b3cc",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b38c",
      "incomplete_value": true,
      "site": "0057b38c",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b488",
      "incomplete_value": false,
      "site": "0057b490",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b448",
      "incomplete_value": false,
      "site": "0057b450",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057b4a0",
      "incomplete_value": false,
      "site": "0057b4a0",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b460",
      "incomplete_value": false,
      "site": "0057b460",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057b224",
      "READ",
      [
        "storage",
        "002a9d91",
        null,
        "string"
      ]
    ],
    [
      "0057b224",
      "READ",
      [
        "storage",
        "002a9da1",
        null,
        "string"
      ]
    ],
    [
      "0057b228",
      "READ",
      [
        "storage",
        "002c2ec0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057b224",
      "READ",
      [
        "storage",
        "002a9d35",
        null,
        "string"
      ]
    ],
    [
      "0057b224",
      "READ",
      [
        "storage",
        "002a9d45",
        null,
        "string"
      ]
    ],
    [
      "0057b228",
      "READ",
      [
        "storage",
        "002c2f00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b38c) · [`0057b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b1a0) · [`0057b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md#insn-0057b1a8)
- 新版 `0057b3cc`（命令位置の公開資料なし） · `0057b1e0`（命令位置の公開資料なし） · `0057b1e8`（命令位置の公開資料なし）

~~~diff
- 0057b38c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 0057b38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057b3cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
+ 0057b3cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057b38c bytes 094501f9
+ 0057b3cc bytes 09c501f9
- 0057b1a0 ["INT_ADD", "register:40f0:8", ["const:57b1a0:8", "const:4:8"]]
- 0057b1a0 ["CALL", null, ["callee:00588eac:8"]]
+ 0057b1e0 ["INT_ADD", "register:40f0:8", ["const:57b1e0:8", "const:4:8"]]
+ 0057b1e0 ["CALL", null, ["callee:00588eac:8"]]
- 0057b1a0 bytes 33370094
+ 0057b1e0 bytes 33370094
- 0057b1a8 ["INT_ADD", "register:40f0:8", ["const:57b1a8:8", "const:4:8"]]
- 0057b1a8 ["CALL", null, ["callee:0058919c:8"]]
+ 0057b1e8 ["INT_ADD", "register:40f0:8", ["const:57b1e8:8", "const:4:8"]]
+ 0057b1e8 ["CALL", null, ["callee:0058919c:8"]]
- 0057b1a8 bytes ed370094
+ 0057b1e8 bytes ed370094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9188105105abdf65dc2a34c569ce136f"></a>

### [`0057b518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md) → [`0057b558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b558.md) Java_jp_co_ponos_battlecats_MyActivity_onAlertClick

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.56% / 新版 92.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057b6c8",
      "incomplete_value": true,
      "site": "0057b6c8",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057b688",
      "incomplete_value": true,
      "site": "0057b688",
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
            "const:2a0:8"
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
      "definition_site": "0057b584",
      "incomplete_value": true,
      "site": "0057b584",
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
      "definition_site": "0057b544",
      "incomplete_value": true,
      "site": "0057b544",
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
      "definition_site": "0057b6c4",
      "incomplete_value": true,
      "site": "0057b6c4",
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
      "definition_site": "0057b684",
      "incomplete_value": true,
      "site": "0057b684",
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
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057b580",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5c8",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5fc",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b580",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5c8",
      "READ",
      [
        "storage",
        "00ca63e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b5fc",
      "READ",
      [
        "storage",
        "00ca63a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b688) · [`0057b53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b53c) · [`0057b54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b518.md#insn-0057b54c)
- 新版 `0057b6c8`（命令位置の公開資料なし） · `0057b57c`（命令位置の公開資料なし） · `0057b58c`（命令位置の公開資料なし）

~~~diff
- 0057b688 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2a0:8"]]
- 0057b688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0057b6c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3a0:8"]]
+ 0057b6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0057b688 bytes 285101f9
+ 0057b6c8 bytes 28d101f9
- 0057b53c ["COPY", "tmp:0:8", ["const:290:8"]]
- 0057b53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b57c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0057b57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b53c bytes 08410a91
+ 0057b57c bytes 08410e91
- 0057b54c ["COPY", "tmp:0:8", ["const:290:8"]]
- 0057b54c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b54c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b54c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b58c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 0057b58c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b58c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b58c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b54c bytes 29410a91
+ 0057b58c bytes 29410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0a52fdeac9eac9b5bf304b7814ae86"></a>

### [`0057b6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md) → [`0057b73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b73c.md) Java_jp_co_ponos_battlecats_MyActivity_onButtonClick

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b748",
      "incomplete_value": true,
      "site": "0057b748",
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
      "definition_site": "0057b708",
      "incomplete_value": true,
      "site": "0057b708",
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
      "0057b744",
      "READ",
      [
        "storage",
        "00ca6278",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b79c",
      "READ",
      [
        "storage",
        "00ca62a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b744",
      "READ",
      [
        "storage",
        "00ca6378",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b79c",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md#insn-0057b700) · [`0057b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b6fc.md#insn-0057b710)
- 新版 `0057b740`（命令位置の公開資料なし） · `0057b750`（命令位置の公開資料なし）

~~~diff
- 0057b700 ["COPY", "tmp:0:8", ["const:278:8"]]
- 0057b700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b740 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 0057b740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b700 bytes 08e10991
+ 0057b740 bytes 08e10d91
- 0057b710 ["COPY", "tmp:0:8", ["const:278:8"]]
- 0057b710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057b710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057b710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057b750 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 0057b750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057b750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057b710 bytes 29e10991
+ 0057b750 bytes 29e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac337ab3cc62fba2813910dd51454a7"></a>

### [`0057b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md) → [`0057b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b7b8.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewFilter

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b7e0",
      "incomplete_value": true,
      "site": "0057b7e0",
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
      "definition_site": "0057b7a0",
      "incomplete_value": true,
      "site": "0057b7a0",
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
      "0057b7dc",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b834",
      "READ",
      [
        "storage",
        "00ca62c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b7dc",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b834",
      "READ",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b798) · [`0057b7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b7a8) · [`0057b804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b778.md#insn-0057b804)
- 新版 `0057b7d8`（命令位置の公開資料なし） · `0057b7e8`（命令位置の公開資料なし） · `0057b844`（命令位置の公開資料なし）

~~~diff
- 0057b798 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0057b798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b7d8 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0057b7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b798 bytes 08010991
+ 0057b7d8 bytes 08010d91
- 0057b7a8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0057b7a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057b7a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057b7a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057b7e8 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0057b7e8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057b7e8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057b7e8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057b7a8 bytes 73020991
+ 0057b7e8 bytes 73020d91
- 0057b804 ["INT_ADD", "register:40f0:8", ["const:57b804:8", "const:4:8"]]
- 0057b804 ["CALL", null, ["callee:00589994:8"]]
+ 0057b844 ["INT_ADD", "register:40f0:8", ["const:57b844:8", "const:4:8"]]
+ 0057b844 ["CALL", null, ["callee:00589994:8"]]
- 0057b804 bytes 54380094
+ 0057b844 bytes 54380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5976ffac0bb4e487a3a5d73edfbfb63"></a>

### [`0057b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md) → [`0057b8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b8f0.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewResult

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057b920",
      "incomplete_value": true,
      "site": "0057b920",
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
      "definition_site": "0057b8e0",
      "incomplete_value": true,
      "site": "0057b8e0",
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
      "0057b91c",
      "READ",
      [
        "storage",
        "00ca6240",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b974",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057b91c",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057b974",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057b8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b8d8) · [`0057b8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b8e8) · [`0057b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b8b0.md#insn-0057b944)
- 新版 `0057b918`（命令位置の公開資料なし） · `0057b928`（命令位置の公開資料なし） · `0057b984`（命令位置の公開資料なし）

~~~diff
- 0057b8d8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0057b8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057b8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057b918 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0057b918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057b918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057b8d8 bytes 08010991
+ 0057b918 bytes 08010d91
- 0057b8e8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0057b8e8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0057b8e8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0057b8e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0057b928 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0057b928 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057b928 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057b928 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0057b8e8 bytes b5020991
+ 0057b928 bytes b5020d91
- 0057b944 ["INT_ADD", "register:40f0:8", ["const:57b944:8", "const:4:8"]]
- 0057b944 ["CALL", null, ["callee:00589994:8"]]
+ 0057b984 ["INT_ADD", "register:40f0:8", ["const:57b984:8", "const:4:8"]]
+ 0057b984 ["CALL", null, ["callee:00589994:8"]]
- 0057b944 bytes 04380094
+ 0057b984 bytes 04380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3649f3cdd82e336ffa1fc6e9d4ca824c"></a>

### [`0057b9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md) → [`0057ba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057ba28.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewEvalResult

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057ba58",
      "incomplete_value": true,
      "site": "0057ba58",
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
      "definition_site": "0057ba18",
      "incomplete_value": true,
      "site": "0057ba18",
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
      "0057ba54",
      "READ",
      [
        "storage",
        "00ca6258",
        null,
        "undefined8"
      ]
    ],
    [
      "0057baf0",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0057ba54",
      "READ",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ],
    [
      "0057baf0",
      "READ",
      [
        "storage",
        "00ca63a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba10) · [`0057ba20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba20) · [`0057ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b9e8.md#insn-0057ba80)
- 新版 `0057ba50`（命令位置の公開資料なし） · `0057ba60`（命令位置の公開資料なし） · `0057bac0`（命令位置の公開資料なし）

~~~diff
- 0057ba10 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0057ba10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057ba10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057ba50 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0057ba50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057ba50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057ba10 bytes 08610991
+ 0057ba50 bytes 08610d91
- 0057ba20 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0057ba20 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ba20 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0057ba20 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0057ba60 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0057ba60 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ba60 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0057ba60 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0057ba20 bytes b5620991
+ 0057ba60 bytes b5620d91
- 0057ba80 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0057ba80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057ba80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057ba80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057bac0 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0057bac0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057bac0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057bac0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057ba80 bytes 4a610991
+ 0057bac0 bytes 4a610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf57ee3897935c82893614bbaeb3b843"></a>

### [`0057bb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md) → [`0057bbbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bbbc.md) FUN_0057bbbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0057bbd4",
      "incomplete_value": false,
      "site": "0057bbd8",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057bb94",
      "incomplete_value": false,
      "site": "0057bb98",
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
            "const:be8:8"
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
      "0057bbd8",
      "DATA",
      [
        "storage",
        "00c6bbe8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057bbd8",
      "DATA",
      [
        "storage",
        "00c6bcb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057bbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bbd8) · [`0057bb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bb94) · [`0057bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bb7c.md#insn-0057bbc8)
- 新版 `0057bc18`（命令位置の公開資料なし） · `0057bbd4`（命令位置の公開資料なし） · `0057bc08`（命令位置の公開資料なし）

~~~diff
- 0057bbd8 ["INT_ADD", "register:40f0:8", ["const:57bbd8:8", "const:4:8"]]
- 0057bbd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057bc18 ["INT_ADD", "register:40f0:8", ["const:57bc18:8", "const:4:8"]]
+ 0057bc18 ["CALL", null, ["callee:00c57f80:8"]]
- 0057bbd8 bytes b6701b94
+ 0057bc18 bytes da701b94
- 0057bb94 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 0057bb94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057bb94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057bb94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057bbd4 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 0057bbd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bbd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057bbd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057bb94 bytes 29a12f91
+ 0057bbd4 bytes 29e13291
- 0057bbc8 ["INT_ADD", "register:40f0:8", ["const:57bbc8:8", "const:4:8"]]
- 0057bbc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057bc08 ["INT_ADD", "register:40f0:8", ["const:57bc08:8", "const:4:8"]]
+ 0057bc08 ["CALL", null, ["callee:00c57f80:8"]]
- 0057bbc8 bytes ba701b94
+ 0057bc08 bytes de701b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cd47f25e5afc9929e62a0abbe35b5ea"></a>

### [`0057c010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c010.md) → [`0057c050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c050.md) FUN_0057c050

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
      "definition_site": "0057c054",
      "incomplete_value": false,
      "site": "0057c058",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c014",
      "incomplete_value": false,
      "site": "0057c018",
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
            "const:e80:8"
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
      "0057c058",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c058",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c010.md#insn-0057c014)
- 新版 `0057c054`（命令位置の公開資料なし）

~~~diff
- 0057c014 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 0057c014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c054 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0057c054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c014 bytes 08013a91
+ 0057c054 bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db6730e064e02fc2ba4e3725a82e1fc"></a>

### [`0057c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md) → [`0057c060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c060.md) FUN_0057c060

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
      "definition_site": "0057c070",
      "incomplete_value": false,
      "site": "0057c078",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c030",
      "incomplete_value": false,
      "site": "0057c038",
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
            "const:e80:8"
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
      "0057c078",
      "DATA",
      [
        "storage",
        "00c6be80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c078",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md#insn-0057c030) · [`0057c03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c020.md#insn-0057c03c)
- 新版 `0057c070`（命令位置の公開資料なし） · `0057c07c`（命令位置の公開資料なし）

~~~diff
- 0057c030 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 0057c030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c070 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0057c070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c030 bytes 08013a91
+ 0057c070 bytes 08413d91
- 0057c03c ["INT_ADD", "register:40f0:8", ["const:57c03c:8", "const:4:8"]]
- 0057c03c ["CALL", null, ["callee:00c57f70:8"]]
+ 0057c07c ["INT_ADD", "register:40f0:8", ["const:57c07c:8", "const:4:8"]]
+ 0057c07c ["CALL", null, ["callee:00c57f70:8"]]
- 0057c03c bytes 996f1b94
+ 0057c07c bytes bd6f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9504df19d889f21fb1f2de1bc4beedcc"></a>

### [`0057c060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c060.md) → [`0057c0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0a0.md) FUN_0057c0a0

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
      "definition_site": "0057c0a4",
      "incomplete_value": false,
      "site": "0057c0a8",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c064",
      "incomplete_value": false,
      "site": "0057c068",
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
            "const:ed0:8"
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
      "0057c0a8",
      "DATA",
      [
        "storage",
        "00c6bed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c0a8",
      "DATA",
      [
        "storage",
        "00c6bfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c060.md#insn-0057c064)
- 新版 `0057c0a4`（命令位置の公開資料なし）

~~~diff
- 0057c064 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0057c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c0a4 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 0057c0a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c0a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c0a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c064 bytes 08413b91
+ 0057c0a4 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6457b91ab8473f21653beea8ca8f5747"></a>

### [`0057c070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md) → [`0057c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0b0.md) FUN_0057c0b0

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
      "definition_site": "0057c0c0",
      "incomplete_value": false,
      "site": "0057c0c8",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c080",
      "incomplete_value": false,
      "site": "0057c088",
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
            "const:ed0:8"
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
      "0057c0c8",
      "DATA",
      [
        "storage",
        "00c6bed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c0c8",
      "DATA",
      [
        "storage",
        "00c6bfa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md#insn-0057c080) · [`0057c08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c070.md#insn-0057c08c)
- 新版 `0057c0c0`（命令位置の公開資料なし） · `0057c0cc`（命令位置の公開資料なし）

~~~diff
- 0057c080 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0057c080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c0c0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 0057c0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c080 bytes 08413b91
+ 0057c0c0 bytes 08813e91
- 0057c08c ["INT_ADD", "register:40f0:8", ["const:57c08c:8", "const:4:8"]]
- 0057c08c ["CALL", null, ["callee:00c57f70:8"]]
+ 0057c0cc ["INT_ADD", "register:40f0:8", ["const:57c0cc:8", "const:4:8"]]
+ 0057c0cc ["CALL", null, ["callee:00c57f70:8"]]
- 0057c08c bytes 856f1b94
+ 0057c0cc bytes a96f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-406e69a09b69ec09d805f50205312abc"></a>

### [`0057c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md) → [`0057c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c24c.md) FUN_0057c24c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0057c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c0b0.md) [`0057c330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c330.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`0057c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c0f0.md) [`0057c370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c370.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0057c258",
      "incomplete_value": false,
      "site": "0057c25c",
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
      "definition_site": "0057c218",
      "incomplete_value": false,
      "site": "0057c21c",
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
      "0057c258",
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
      "0057c258",
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

- 旧版 [`0057c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md#insn-0057c21c) · [`0057c218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c20c.md#insn-0057c218)
- 新版 `0057c25c`（命令位置の公開資料なし） · `0057c258`（命令位置の公開資料なし）

~~~diff
- 0057c21c ["INT_ADD", "register:40f0:8", ["const:57c21c:8", "const:4:8"]]
- 0057c21c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0057c25c ["INT_ADD", "register:40f0:8", ["const:57c25c:8", "const:4:8"]]
+ 0057c25c ["CALL", null, ["callee:0043b7b8:8"]]
- 0057c21c bytes 57fdfa97
+ 0057c25c bytes 57fdfa97
- 0057c218 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0057c218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c258 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0057c258 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c258 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c258 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c218 bytes 00303d91
+ 0057c258 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-732d93726d5584ef2d2fb2280b2646c0"></a>

### [`0057c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md) → [`0057c35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c35c.md) FUN_0057c35c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0057a2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2a4.md) [`0057a2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a2fc.md) [`0057a344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057a/0057a344.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 3件 [`0057a2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a2e4.md) [`0057a33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a33c.md) [`0057a384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a384.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "0057c368",
      "incomplete_value": false,
      "site": "0057c36c",
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
      "definition_site": "0057c328",
      "incomplete_value": false,
      "site": "0057c32c",
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
      "0057c368",
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
      "0057c368",
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

- 旧版 [`0057c32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md#insn-0057c32c) · [`0057c328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c31c.md#insn-0057c328)
- 新版 `0057c36c`（命令位置の公開資料なし） · `0057c368`（命令位置の公開資料なし）

~~~diff
- 0057c32c ["INT_ADD", "register:40f0:8", ["const:57c32c:8", "const:4:8"]]
- 0057c32c ["CALL", null, ["callee:00442970:8"]]
+ 0057c36c ["INT_ADD", "register:40f0:8", ["const:57c36c:8", "const:4:8"]]
+ 0057c36c ["CALL", null, ["callee:00442970:8"]]
- 0057c32c bytes 8119fb97
+ 0057c36c bytes 8119fb97
- 0057c328 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0057c328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0057c328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0057c328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057c368 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0057c368 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c368 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057c368 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0057c328 bytes 00303d91
+ 0057c368 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa8071a2a0bc72c668fffbdbe3fd5ca8"></a>

### [`0057c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c48c.md) → [`0057c4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4cc.md) FUN_0057c4cc

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
      "definition_site": "0057c4d0",
      "incomplete_value": false,
      "site": "0057c4d4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c490",
      "incomplete_value": false,
      "site": "0057c494",
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
            "const:f20:8"
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
      "0057c4d4",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4d4",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c48c.md#insn-0057c490)
- 新版 `0057c4d0`（命令位置の公開資料なし）

~~~diff
- 0057c490 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 0057c490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 0057c4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c490 bytes 08813c91
+ 0057c4d0 bytes 08c13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b22b952fe615c9efd03f2f30bd2373"></a>

### [`0057c49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md) → [`0057c4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c4dc.md) FUN_0057c4dc

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
      "definition_site": "0057c4ec",
      "incomplete_value": false,
      "site": "0057c4f4",
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
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4ac",
      "incomplete_value": false,
      "site": "0057c4b4",
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
            "const:f20:8"
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
      "0057c4f4",
      "DATA",
      [
        "storage",
        "00c6bf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c4f4",
      "DATA",
      [
        "storage",
        "00c6bff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md#insn-0057c4ac) · [`0057c4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c49c.md#insn-0057c4b8)
- 新版 `0057c4ec`（命令位置の公開資料なし） · `0057c4f8`（命令位置の公開資料なし）

~~~diff
- 0057c4ac ["COPY", "tmp:0:8", ["const:f20:8"]]
- 0057c4ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ec ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 0057c4ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c4ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4ac bytes 08813c91
+ 0057c4ec bytes 08c13f91
- 0057c4b8 ["INT_ADD", "register:40f0:8", ["const:57c4b8:8", "const:4:8"]]
- 0057c4b8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0057c4f8 ["INT_ADD", "register:40f0:8", ["const:57c4f8:8", "const:4:8"]]
+ 0057c4f8 ["CALL", null, ["callee:00c57f70:8"]]
- 0057c4b8 bytes 7a6e1b94
+ 0057c4f8 bytes 9e6e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7f0638fc51b366d747822b071f1ded"></a>

### [`0057c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4dc.md) → [`0057c51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c51c.md) FUN_0057c51c

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
      "definition_site": "0057c520",
      "incomplete_value": false,
      "site": "0057c524",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4e0",
      "incomplete_value": false,
      "site": "0057c4e4",
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
            "const:f70:8"
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
      "0057c524",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c524",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4dc.md#insn-0057c4dc) · [`0057c4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4dc.md#insn-0057c4e0)
- 新版 `0057c51c`（命令位置の公開資料なし） · `0057c520`（命令位置の公開資料なし）

~~~diff
- 0057c4dc ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c51c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c4dc bytes 683700f0
+ 0057c51c bytes 88370090
- 0057c4e0 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 0057c4e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c520 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0057c520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4e0 bytes 08c13d91
+ 0057c520 bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-074ff5d5a5aaa9e382cd25458b2780ce"></a>

### [`0057c4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md) → [`0057c52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c52c.md) FUN_0057c52c

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
      "definition_site": "0057c53c",
      "incomplete_value": false,
      "site": "0057c544",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c4fc",
      "incomplete_value": false,
      "site": "0057c504",
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
            "const:f70:8"
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
      "0057c544",
      "DATA",
      [
        "storage",
        "00c6bf70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c544",
      "DATA",
      [
        "storage",
        "00c6c040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md#insn-0057c4f8) · [`0057c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md#insn-0057c4fc) · [`0057c508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c4ec.md#insn-0057c508)
- 新版 `0057c538`（命令位置の公開資料なし） · `0057c53c`（命令位置の公開資料なし） · `0057c548`（命令位置の公開資料なし）

~~~diff
- 0057c4f8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c538 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c4f8 bytes 683700f0
+ 0057c538 bytes 88370090
- 0057c4fc ["COPY", "tmp:0:8", ["const:f70:8"]]
- 0057c4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c53c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0057c53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c4fc bytes 08c13d91
+ 0057c53c bytes 08010191
- 0057c508 ["INT_ADD", "register:40f0:8", ["const:57c508:8", "const:4:8"]]
- 0057c508 ["CALL", null, ["callee:00c57f70:8"]]
+ 0057c548 ["INT_ADD", "register:40f0:8", ["const:57c548:8", "const:4:8"]]
+ 0057c548 ["CALL", null, ["callee:00c57f70:8"]]
- 0057c508 bytes 666e1b94
+ 0057c548 bytes 8a6e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b4e2face5d3dd05fad36a4b054fd73"></a>

### [`0057c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c60c.md) → [`0057c64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c64c.md) FUN_0057c64c

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
      "definition_site": "0057c650",
      "incomplete_value": false,
      "site": "0057c654",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c610",
      "incomplete_value": false,
      "site": "0057c614",
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
      "0057c654",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c654",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c60c.md#insn-0057c60c) · [`0057c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c60c.md#insn-0057c610)
- 新版 `0057c64c`（命令位置の公開資料なし） · `0057c650`（命令位置の公開資料なし）

~~~diff
- 0057c60c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c64c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c60c bytes 683700f0
+ 0057c64c bytes 88370090
- 0057c610 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 0057c610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0057c650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c610 bytes 08013f91
+ 0057c650 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e55ddf6f4dab674e4fd5cf054876760d"></a>

### [`0057c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md) → [`0057c65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c65c.md) FUN_0057c65c

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
      "definition_site": "0057c66c",
      "incomplete_value": false,
      "site": "0057c674",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057c62c",
      "incomplete_value": false,
      "site": "0057c634",
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
      "0057c674",
      "DATA",
      [
        "storage",
        "00c6bfc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057c674",
      "DATA",
      [
        "storage",
        "00c6c090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md#insn-0057c628) · [`0057c62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md#insn-0057c62c) · [`0057c638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c61c.md#insn-0057c638)
- 新版 `0057c668`（命令位置の公開資料なし） · `0057c66c`（命令位置の公開資料なし） · `0057c678`（命令位置の公開資料なし）

~~~diff
- 0057c628 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0057c668 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057c628 bytes 683700f0
+ 0057c668 bytes 88370090
- 0057c62c ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 0057c62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057c62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057c62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057c66c ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0057c66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057c66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057c62c bytes 08013f91
+ 0057c66c bytes 08410291
- 0057c638 ["INT_ADD", "register:40f0:8", ["const:57c638:8", "const:4:8"]]
- 0057c638 ["CALL", null, ["callee:00c57f70:8"]]
+ 0057c678 ["INT_ADD", "register:40f0:8", ["const:57c678:8", "const:4:8"]]
+ 0057c678 ["CALL", null, ["callee:00c57f70:8"]]
- 0057c638 bytes 1a6e1b94
+ 0057c678 bytes 3e6e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275cc7bae468ea800c52d75d3950c4bd"></a>

### [`0057c7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md) → [`0057c7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c7fc.md) _INIT_31

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`005765ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765ac.md) [`005765b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005765b4.md) [`005766f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`005765ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765ec.md) [`005765f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765f4.md) [`00576738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576738.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 12件, `store_value` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057c838",
      "incomplete_value": true,
      "site": "0057c854",
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
    "old": {
      "definition_site": "0057c7f8",
      "incomplete_value": true,
      "site": "0057c814",
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
                "const:f26:8"
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
      "definition_site": "0057c85c",
      "incomplete_value": true,
      "site": "0057c878",
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
    "old": {
      "definition_site": "0057c81c",
      "incomplete_value": true,
      "site": "0057c838",
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
                "const:f39:8"
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
      "definition_site": "0057c87c",
      "incomplete_value": true,
      "site": "0057c898",
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
    "old": {
      "definition_site": "0057c83c",
      "incomplete_value": true,
      "site": "0057c858",
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
                "const:dc2:8"
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
      "0057c838",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0057c85c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0057c87c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057c838",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0057c85c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0057c87c",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057c854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c854) · [`0057c9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c9dc) · [`0057c9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c7bc.md#insn-0057c9f4)
- 新版 `0057c894`（命令位置の公開資料なし） · `0057ca1c`（命令位置の公開資料なし） · `0057ca34`（命令位置の公開資料なし）

~~~diff
- 0057c854 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0057c854 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057c854 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057c854 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057c894 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0057c894 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057c894 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057c894 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057c854 bytes 4a893d91
+ 0057c894 bytes 4a553c91
- 0057c9dc ["COPY", "tmp:0:8", ["const:f90:8"]]
- 0057c9dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057c9dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057c9dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0057ca1c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0057ca1c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0057ca1c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0057ca1c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057c9dc bytes 73423e91
+ 0057ca1c bytes 73820191
- 0057c9f4 ["INT_ADD", "register:40f0:8", ["const:57c9f4:8", "const:4:8"]]
- 0057c9f4 ["CALL", null, ["callee:00c57f00:8"]]
+ 0057ca34 ["INT_ADD", "register:40f0:8", ["const:57ca34:8", "const:4:8"]]
+ 0057ca34 ["CALL", null, ["callee:00c57f00:8"]]
- 0057c9f4 bytes 0f6d1b94
+ 0057ca34 bytes 336d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4571d63c906b4f30909aff538ed866"></a>

### [`0057cc18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md) → [`0057cc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cc58.md) FUN_0057cc58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057cc78",
      "incomplete_value": false,
      "site": "0057cc78",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc38",
      "incomplete_value": false,
      "site": "0057cc38",
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
      "definition_site": "0057cc78",
      "incomplete_value": false,
      "site": "0057cc78",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc38",
      "incomplete_value": false,
      "site": "0057cc38",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057cc78",
      "DATA",
      [
        "storage",
        "00c6c010",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc78",
      "DATA",
      [
        "storage",
        "00c6c0d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057cc78",
      "DATA",
      [
        "storage",
        "00c6c0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057cc78",
      "DATA",
      [
        "storage",
        "00c6c1a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md#insn-0057cc2c) · [`0057cc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc18.md#insn-0057cc40)
- 新版 `0057cc6c`（命令位置の公開資料なし） · `0057cc80`（命令位置の公開資料なし）

~~~diff
- 0057cc2c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0057cc2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cc6c ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0057cc6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cc6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cc2c bytes 08410091
+ 0057cc6c bytes 08810391
- 0057cc40 ["INT_ADD", "register:40f0:8", ["const:57cc40:8", "const:4:8"]]
- 0057cc40 ["CALL", null, ["callee:00c5a210:8"]]
+ 0057cc80 ["INT_ADD", "register:40f0:8", ["const:57cc80:8", "const:4:8"]]
+ 0057cc80 ["CALL", null, ["callee:00c5a210:8"]]
- 0057cc40 bytes 40751b94
+ 0057cc80 bytes 64751b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-282de5c3b65ee76e613f506c51b06b89"></a>

### [`0057cc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md) → [`0057ccb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057ccb8.md) FUN_0057ccb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057ccd8",
      "incomplete_value": false,
      "site": "0057ccd8",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc98",
      "incomplete_value": false,
      "site": "0057cc98",
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
      "definition_site": "0057ccd8",
      "incomplete_value": false,
      "site": "0057ccd8",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057cc98",
      "incomplete_value": false,
      "site": "0057cc98",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057ccd8",
      "DATA",
      [
        "storage",
        "00c6c010",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ccd8",
      "DATA",
      [
        "storage",
        "00c6c0d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057ccd8",
      "DATA",
      [
        "storage",
        "00c6c0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057ccd8",
      "DATA",
      [
        "storage",
        "00c6c1a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057cc8c) · [`0057cca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057cca0) · [`0057ccbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057cc78.md#insn-0057ccbc)
- 新版 `0057cccc`（命令位置の公開資料なし） · `0057cce0`（命令位置の公開資料なし） · `0057ccfc`（命令位置の公開資料なし）

~~~diff
- 0057cc8c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0057cc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057cc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057cccc ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0057cccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057cccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057cc8c bytes 08410091
+ 0057cccc bytes 08810391
- 0057cca0 ["INT_ADD", "register:40f0:8", ["const:57cca0:8", "const:4:8"]]
- 0057cca0 ["CALL", null, ["callee:00c5a210:8"]]
+ 0057cce0 ["INT_ADD", "register:40f0:8", ["const:57cce0:8", "const:4:8"]]
+ 0057cce0 ["CALL", null, ["callee:00c5a210:8"]]
- 0057cca0 bytes 28751b94
+ 0057cce0 bytes 4c751b94
- 0057ccbc ["INT_ADD", "register:40f0:8", ["const:57ccbc:8", "const:4:8"]]
- 0057ccbc ["CALL", null, ["callee:00c57f80:8"]]
+ 0057ccfc ["INT_ADD", "register:40f0:8", ["const:57ccfc:8", "const:4:8"]]
+ 0057ccfc ["CALL", null, ["callee:00c57f80:8"]]
- 0057ccbc bytes 7d6c1b94
+ 0057ccfc bytes a16c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca77a0dd73b306da91d4729cf7ae856"></a>

### [`0057ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md) → [`0057cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md) FUN_0057cef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d068",
      "incomplete_value": false,
      "site": "0057d074",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d028",
      "incomplete_value": false,
      "site": "0057d034",
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
            "const:260:8"
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
      "0057d074",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d074",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf04) · [`0057cf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf20) · [`0057cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md#insn-0057cf58)
- 新版 `0057cf44`（命令位置の公開資料なし） · `0057cf60`（命令位置の公開資料なし） · `0057cf98`（命令位置の公開資料なし）

~~~diff
- 0057cf04 ["INT_ADD", "register:40f0:8", ["const:57cf04:8", "const:4:8"]]
- 0057cf04 ["CALL", null, ["callee:00c57f60:8"]]
+ 0057cf44 ["INT_ADD", "register:40f0:8", ["const:57cf44:8", "const:4:8"]]
+ 0057cf44 ["CALL", null, ["callee:00c57f60:8"]]
- 0057cf04 bytes e36b1b94
+ 0057cf44 bytes 076c1b94
- 0057cf20 ["INT_ADD", "register:40f0:8", ["const:57cf20:8", "const:4:8"]]
- 0057cf20 ["CALL", null, ["callee:00c58160:8"]]
+ 0057cf60 ["INT_ADD", "register:40f0:8", ["const:57cf60:8", "const:4:8"]]
+ 0057cf60 ["CALL", null, ["callee:00c58160:8"]]
- 0057cf20 bytes 5c6c1b94
+ 0057cf60 bytes 806c1b94
- 0057cf58 ["INT_ADD", "register:40f0:8", ["const:57cf58:8", "const:4:8"]]
- 0057cf58 ["CALL", null, ["callee:00c5a250:8"]]
+ 0057cf98 ["INT_ADD", "register:40f0:8", ["const:57cf98:8", "const:4:8"]]
+ 0057cf98 ["CALL", null, ["callee:00c5a250:8"]]
- 0057cf58 bytes 8a741b94
+ 0057cf98 bytes ae741b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46fa3faf49ddefecd6a29d28c483a8a1"></a>

### [`0057d494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md) → [`0057d4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md) FUN_0057d4d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057d64c",
      "incomplete_value": false,
      "site": "0057d658",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057d60c",
      "incomplete_value": false,
      "site": "0057d618",
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
            "const:260:8"
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
      "0057d658",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057d658",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d4e0) · [`0057d4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d4fc) · [`0057d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md#insn-0057d538)
- 新版 `0057d520`（命令位置の公開資料なし） · `0057d53c`（命令位置の公開資料なし） · `0057d578`（命令位置の公開資料なし）

~~~diff
- 0057d4e0 ["INT_ADD", "register:40f0:8", ["const:57d4e0:8", "const:4:8"]]
- 0057d4e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0057d520 ["INT_ADD", "register:40f0:8", ["const:57d520:8", "const:4:8"]]
+ 0057d520 ["CALL", null, ["callee:00c57f60:8"]]
- 0057d4e0 bytes 6c6a1b94
+ 0057d520 bytes 906a1b94
- 0057d4fc ["INT_ADD", "register:40f0:8", ["const:57d4fc:8", "const:4:8"]]
- 0057d4fc ["CALL", null, ["callee:00c58160:8"]]
+ 0057d53c ["INT_ADD", "register:40f0:8", ["const:57d53c:8", "const:4:8"]]
+ 0057d53c ["CALL", null, ["callee:00c58160:8"]]
- 0057d4fc bytes e56a1b94
+ 0057d53c bytes 096b1b94
- 0057d538 ["INT_ADD", "register:40f0:8", ["const:57d538:8", "const:4:8"]]
- 0057d538 ["CALL", null, ["callee:00c5a150:8"]]
+ 0057d578 ["INT_ADD", "register:40f0:8", ["const:57d578:8", "const:4:8"]]
+ 0057d578 ["CALL", null, ["callee:00c5a150:8"]]
- 0057d538 bytes d2721b94
+ 0057d578 bytes f6721b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8de6e4d8eea7e08c227a70b8937d28f"></a>

### [`0057d9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md) → [`0057d9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d9e8.md) FUN_0057d9e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md) [`00c5a160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a160.md)
- 新版 呼出元 1件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md) [`00c5a230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a230.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057da40",
      "incomplete_value": false,
      "site": "0057da4c",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da00",
      "incomplete_value": false,
      "site": "0057da0c",
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
            "const:2b0:8"
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
      "definition_site": "0057da60",
      "incomplete_value": false,
      "site": "0057da60",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da20",
      "incomplete_value": false,
      "site": "0057da20",
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
            "const:10:8"
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
      "definition_site": "0057da64",
      "incomplete_value": false,
      "site": "0057da68",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057da24",
      "incomplete_value": false,
      "site": "0057da28",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057da08",
      "READ",
      [
        "storage",
        "00c9b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0057da1c",
      "READ",
      [
        "storage",
        "00ca62b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057da4c",
      "DATA",
      [
        "storage",
        "00c6c2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057da08",
      "READ",
      [
        "storage",
        "00c9b3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0057da1c",
      "READ",
      [
        "storage",
        "00ca63b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057da4c",
      "DATA",
      [
        "storage",
        "00c6c380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057d9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057d9e8) · [`0057da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057da70) · [`0057d9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d9a8.md#insn-0057d9c8)
- 新版 `0057da28`（命令位置の公開資料なし） · `0057dab0`（命令位置の公開資料なし） · `0057da08`（命令位置の公開資料なし）

~~~diff
- 0057d9e8 ["INT_ADD", "register:40f0:8", ["const:57d9e8:8", "const:4:8"]]
- 0057d9e8 ["CALL", null, ["callee:00c5a230:8"]]
+ 0057da28 ["INT_ADD", "register:40f0:8", ["const:57da28:8", "const:4:8"]]
+ 0057da28 ["CALL", null, ["callee:00c5a230:8"]]
- 0057d9e8 bytes de711b94
+ 0057da28 bytes 02721b94
- 0057da70 ["INT_ADD", "register:40f0:8", ["const:57da70:8", "const:4:8"]]
- 0057da70 ["CALL", null, ["callee:00c5a160:8"]]
+ 0057dab0 ["INT_ADD", "register:40f0:8", ["const:57dab0:8", "const:4:8"]]
+ 0057dab0 ["CALL", null, ["callee:00c5a160:8"]]
- 0057da70 bytes 88711b94
+ 0057dab0 bytes ac711b94
- 0057d9c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2d0:8"]]
- 0057d9c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057da08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3a0:8"]]
+ 0057da08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057d9c8 bytes 086941f9
+ 0057da08 bytes 08d141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa8f95dba51e1e59cd26b7d3b971d10"></a>

### [`0057db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db40.md) → [`0057db80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057db80.md) FUN_0057db80

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db90",
      "incomplete_value": false,
      "site": "0057db90",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db50",
      "incomplete_value": false,
      "site": "0057db50",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057db90",
      "incomplete_value": false,
      "site": "0057db90",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db50",
      "incomplete_value": false,
      "site": "0057db50",
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
                "const:c6c000:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057db90",
      "DATA",
      [
        "storage",
        "00c6c0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db90",
      "DATA",
      [
        "storage",
        "00c6c1b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057db90",
      "DATA",
      [
        "storage",
        "00c6c1c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057db90",
      "DATA",
      [
        "storage",
        "00c6c288",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db40.md#insn-0057db44)
- 新版 `0057db84`（命令位置の公開資料なし）

~~~diff
- 0057db44 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0057db44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057db84 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 0057db84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057db84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db44 bytes 08c10391
+ 0057db84 bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07b003c9dab5245c6a9bdce9a36edce0"></a>

### [`0057db64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md) → [`0057dba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dba4.md) FUN_0057dba4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dbb4",
      "incomplete_value": true,
      "site": "0057dbb4",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db74",
      "incomplete_value": true,
      "site": "0057db74",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057dbb4",
      "incomplete_value": true,
      "site": "0057dbb4",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:1c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057db74",
      "incomplete_value": true,
      "site": "0057db74",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0057dbb4",
      "DATA",
      [
        "storage",
        "00c6c0f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057dbb4",
      "DATA",
      [
        "storage",
        "00c6c1b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057dbb4",
      "DATA",
      [
        "storage",
        "00c6c1c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0057dbb4",
      "DATA",
      [
        "storage",
        "00c6c288",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057db68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md#insn-0057db68) · [`0057db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057db64.md#insn-0057db94)
- 新版 `0057dba8`（命令位置の公開資料なし） · `0057dbd4`（命令位置の公開資料なし）

~~~diff
- 0057db68 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0057db68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057db68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057db68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dba8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 0057dba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057db68 bytes 08c10391
+ 0057dba8 bytes 08010791
- 0057db94 ["INT_ADD", "register:40f0:8", ["const:57db94:8", "const:4:8"]]
- 0057db94 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057dbd4 ["INT_ADD", "register:40f0:8", ["const:57dbd4:8", "const:4:8"]]
+ 0057dbd4 ["CALL", null, ["callee:00c57f80:8"]]
- 0057db94 bytes c7681b94
+ 0057dbd4 bytes eb681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7461d8ed7b15b1b969722dd517f944f"></a>

### [`0057dba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dba8.md) → [`0057dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dbe8.md) FUN_0057dbe8

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
      "definition_site": "0057dbec",
      "incomplete_value": false,
      "site": "0057dbf0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbac",
      "incomplete_value": false,
      "site": "0057dbb0",
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
            "const:260:8"
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
      "0057dbf0",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0057dbf0",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dba8.md#insn-0057dbac)
- 新版 `0057dbec`（命令位置の公開資料なし）

~~~diff
- 0057dbac ["COPY", "tmp:0:8", ["const:260:8"]]
- 0057dbac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dbec ["COPY", "tmp:0:8", ["const:330:8"]]
+ 0057dbec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dbec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dbac bytes 08810991
+ 0057dbec bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeee6ae2526816f00ddab74110e8ad6f"></a>

### [`0057dbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dbf8.md) → [`0057dc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc38.md) FUN_0057dc38

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
      "definition_site": "0057dc3c",
      "incomplete_value": false,
      "site": "0057dc40",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dbfc",
      "incomplete_value": false,
      "site": "0057dc00",
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
            "const:2b0:8"
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
      "0057dc40",
      "DATA",
      [
        "storage",
        "00c6c2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dc40",
      "DATA",
      [
        "storage",
        "00c6c380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dbf8.md#insn-0057dbfc)
- 新版 `0057dc3c`（命令位置の公開資料なし）

~~~diff
- 0057dbfc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0057dbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dc3c ["COPY", "tmp:0:8", ["const:380:8"]]
+ 0057dc3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dbfc bytes 08c10a91
+ 0057dc3c bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29dd0c6ca6618e973d6a6f0a5b4c24eb"></a>

### [`0057dc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc48.md) → [`0057dc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc88.md) FUN_0057dc88

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
      "definition_site": "0057dc8c",
      "incomplete_value": false,
      "site": "0057dc90",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc4c",
      "incomplete_value": false,
      "site": "0057dc50",
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
            "const:300:8"
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
      "0057dc90",
      "DATA",
      [
        "storage",
        "00c6c300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dc90",
      "DATA",
      [
        "storage",
        "00c6c3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc48.md#insn-0057dc4c)
- 新版 `0057dc8c`（命令位置の公開資料なし）

~~~diff
- 0057dc4c ["COPY", "tmp:0:8", ["const:300:8"]]
- 0057dc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dc8c ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 0057dc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc4c bytes 08010c91
+ 0057dc8c bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eca4c4e59aa0592c0be5453fba470ef"></a>

### [`0057dc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md) → [`0057dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057dc98.md) FUN_0057dc98

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
      "definition_site": "0057dca8",
      "incomplete_value": false,
      "site": "0057dcb0",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057dc68",
      "incomplete_value": false,
      "site": "0057dc70",
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
            "const:300:8"
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
      "0057dcb0",
      "DATA",
      [
        "storage",
        "00c6c300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057dcb0",
      "DATA",
      [
        "storage",
        "00c6c3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md#insn-0057dc68) · [`0057dc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dc58.md#insn-0057dc74)
- 新版 `0057dca8`（命令位置の公開資料なし） · `0057dcb4`（命令位置の公開資料なし）

~~~diff
- 0057dc68 ["COPY", "tmp:0:8", ["const:300:8"]]
- 0057dc68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057dc68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057dca8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 0057dca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057dca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057dc68 bytes 08010c91
+ 0057dca8 bytes 08410f91
- 0057dc74 ["INT_ADD", "register:40f0:8", ["const:57dc74:8", "const:4:8"]]
- 0057dc74 ["CALL", null, ["callee:00c57f70:8"]]
+ 0057dcb4 ["INT_ADD", "register:40f0:8", ["const:57dcb4:8", "const:4:8"]]
+ 0057dcb4 ["CALL", null, ["callee:00c57f70:8"]]
- 0057dc74 bytes 8b681b94
+ 0057dcb4 bytes af681b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac5b7d552a62b7d4ab1aa4d772de0d3"></a>

### [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) → [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) FUN_0057e0d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00550c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c08.md) [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`005862e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00550c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c48.md) [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`00586324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e104",
      "incomplete_value": false,
      "site": "0057e10c",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e0c4",
      "incomplete_value": false,
      "site": "0057e0cc",
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
            "const:3c8:8"
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
      "0057e10c",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e124",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e10c",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e124",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0bc) · [`0057e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0c4) · [`0057e0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md#insn-0057e0d8)
- 新版 `0057e0fc`（命令位置の公開資料なし） · `0057e104`（命令位置の公開資料なし） · `0057e118`（命令位置の公開資料なし）

~~~diff
- 0057e0bc ["INT_ADD", "register:40f0:8", ["const:57e0bc:8", "const:4:8"]]
- 0057e0bc ["CALL", null, ["callee:00c57f60:8"]]
+ 0057e0fc ["INT_ADD", "register:40f0:8", ["const:57e0fc:8", "const:4:8"]]
+ 0057e0fc ["CALL", null, ["callee:00c57f60:8"]]
- 0057e0bc bytes 75671b94
+ 0057e0fc bytes 99671b94
- 0057e0c4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0057e0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e104 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0057e104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e0c4 bytes 08210f91
+ 0057e104 bytes 08611291
- 0057e0d8 ["COPY", "tmp:0:8", ["const:350:8"]]
- 0057e0d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057e0d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057e0d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057e118 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 0057e118 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e118 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057e118 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057e0d8 bytes 29410d91
+ 0057e118 bytes 29811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ffa411104b22e95de73e601e796f7c"></a>

### [`0057e164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md) → [`0057e1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e1a4.md) FUN_0057e1a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e1bc",
      "incomplete_value": true,
      "site": "0057e1c0",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e17c",
      "incomplete_value": true,
      "site": "0057e180",
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
            "const:350:8"
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
      "0057e1c0",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e1c0",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e1c0) · [`0057e17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e17c) · [`0057e190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e164.md#insn-0057e190)
- 新版 `0057e200`（命令位置の公開資料なし） · `0057e1bc`（命令位置の公開資料なし） · `0057e1d0`（命令位置の公開資料なし）

~~~diff
- 0057e1c0 ["INT_ADD", "register:40f0:8", ["const:57e1c0:8", "const:4:8"]]
- 0057e1c0 ["CALL", null, ["callee:00c57f50:8"]]
+ 0057e200 ["INT_ADD", "register:40f0:8", ["const:57e200:8", "const:4:8"]]
+ 0057e200 ["CALL", null, ["callee:00c57f50:8"]]
- 0057e1c0 bytes 30671b94
+ 0057e200 bytes 54671b94
- 0057e17c ["COPY", "tmp:0:8", ["const:350:8"]]
- 0057e17c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e17c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e17c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e1bc ["COPY", "tmp:0:8", ["const:420:8"]]
+ 0057e1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e17c bytes 08410d91
+ 0057e1bc bytes 08811091
- 0057e190 ["INT_ADD", "register:40f0:8", ["const:57e190:8", "const:4:8"]]
- 0057e190 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057e1d0 ["INT_ADD", "register:40f0:8", ["const:57e1d0:8", "const:4:8"]]
+ 0057e1d0 ["CALL", null, ["callee:00c53da0:8"]]
- 0057e190 bytes dc561b94
+ 0057e1d0 bytes f4561b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5fe609316bb55ce450488489a9f1d4"></a>

### [`0057e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md) → [`0057e21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e21c.md) FUN_0057e21c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0057e234",
      "incomplete_value": false,
      "site": "0057e238",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e1f4",
      "incomplete_value": false,
      "site": "0057e1f8",
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
            "const:350:8"
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
      "0057e238",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e238",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e1f4) · [`0057e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e208) · [`0057e21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e1dc.md#insn-0057e21c)
- 新版 `0057e234`（命令位置の公開資料なし） · `0057e248`（命令位置の公開資料なし） · `0057e25c`（命令位置の公開資料なし）

~~~diff
- 0057e1f4 ["COPY", "tmp:0:8", ["const:350:8"]]
- 0057e1f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e1f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e234 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 0057e234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e1f4 bytes 08410d91
+ 0057e234 bytes 08811091
- 0057e208 ["INT_ADD", "register:40f0:8", ["const:57e208:8", "const:4:8"]]
- 0057e208 ["CALL", null, ["callee:00c53da0:8"]]
+ 0057e248 ["INT_ADD", "register:40f0:8", ["const:57e248:8", "const:4:8"]]
+ 0057e248 ["CALL", null, ["callee:00c53da0:8"]]
- 0057e208 bytes be561b94
+ 0057e248 bytes d6561b94
- 0057e21c ["INT_ADD", "register:40f0:8", ["const:57e21c:8", "const:4:8"]]
- 0057e21c ["CALL", null, ["callee:00c57f80:8"]]
+ 0057e25c ["INT_ADD", "register:40f0:8", ["const:57e25c:8", "const:4:8"]]
+ 0057e25c ["CALL", null, ["callee:00c57f80:8"]]
- 0057e21c bytes 25671b94
+ 0057e25c bytes 49671b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b69fa80ec94d7ac3e29aa664bf75fa65"></a>

### [`0057e254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md) → [`0057e294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e294.md) FUN_0057e294

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057de10.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0057de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de50.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e2c0",
      "incomplete_value": false,
      "site": "0057e2c4",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e280",
      "incomplete_value": false,
      "site": "0057e284",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e2cc",
      "incomplete_value": false,
      "site": "0057e2dc",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e28c",
      "incomplete_value": false,
      "site": "0057e29c",
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
            "const:350:8"
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
      "0057e2c4",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e2dc",
      "DATA",
      [
        "storage",
        "00c6c350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e2c4",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ],
    [
      "0057e2dc",
      "DATA",
      [
        "storage",
        "00c6c420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e2dc) · [`0057e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e280) · [`0057e288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e254.md#insn-0057e288)
- 新版 `0057e31c`（命令位置の公開資料なし） · `0057e2c0`（命令位置の公開資料なし）

~~~diff
- 0057e2dc ["INT_ADD", "register:40f0:8", ["const:57e2dc:8", "const:4:8"]]
- 0057e2dc ["CALL", null, ["callee:00c53d70:8"]]
+ 0057e31c ["INT_ADD", "register:40f0:8", ["const:57e31c:8", "const:4:8"]]
+ 0057e31c ["CALL", null, ["callee:00c53d70:8"]]
- 0057e2dc bytes 7d561b94
+ 0057e31c bytes 95561b94
- 0057e280 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0057e280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e2c0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0057e2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e280 bytes 08210f91
+ 0057e2c0 bytes 08611291
- 0057e288 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0057e288 bytes 683700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da29aa333dc1103635731e92648f0d69"></a>

### [`0057e37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e37c.md) → [`0057e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3bc.md) FUN_0057e3bc

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
      "definition_site": "0057e3c0",
      "incomplete_value": false,
      "site": "0057e3c4",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e380",
      "incomplete_value": false,
      "site": "0057e384",
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
            "const:3c8:8"
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
      "0057e3c4",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e3c4",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e37c.md#insn-0057e380)
- 新版 `0057e3c0`（命令位置の公開資料なし）

~~~diff
- 0057e380 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0057e380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e3c0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0057e3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e380 bytes 08210f91
+ 0057e3c0 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79f62af6a903441de8b921793bda4ac7"></a>

### [`0057e38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md) → [`0057e3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e3cc.md) FUN_0057e3cc

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
      "definition_site": "0057e3dc",
      "incomplete_value": false,
      "site": "0057e3e4",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e39c",
      "incomplete_value": false,
      "site": "0057e3a4",
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
            "const:3c8:8"
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
      "0057e3e4",
      "DATA",
      [
        "storage",
        "00c6c3c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057e3e4",
      "DATA",
      [
        "storage",
        "00c6c498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md#insn-0057e39c) · [`0057e3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e38c.md#insn-0057e3a8)
- 新版 `0057e3dc`（命令位置の公開資料なし） · `0057e3e8`（命令位置の公開資料なし）

~~~diff
- 0057e39c ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0057e39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057e39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057e39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057e3dc ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0057e3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057e3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057e39c bytes 08210f91
+ 0057e3dc bytes 08611291
- 0057e3a8 ["INT_ADD", "register:40f0:8", ["const:57e3a8:8", "const:4:8"]]
- 0057e3a8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0057e3e8 ["INT_ADD", "register:40f0:8", ["const:57e3e8:8", "const:4:8"]]
+ 0057e3e8 ["CALL", null, ["callee:00c57f70:8"]]
- 0057e3a8 bytes be661b94
+ 0057e3e8 bytes e2661b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673884cae3b3c8307f8daa29e3672ba3"></a>

### [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) → [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) FUN_0057e51c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00550c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c2c.md) [`0057ebf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ebf0.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md)
- 新版 呼出元 2件 [`00550c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c6c.md) [`0057ec30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057ec30.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e57c",
      "incomplete_value": true,
      "site": "0057e57c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:77e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e53c",
      "incomplete_value": true,
      "site": "0057e53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7da:8"
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
      "definition_site": "0057e588",
      "incomplete_value": true,
      "site": "0057e594",
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
                "const:a71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e548",
      "incomplete_value": true,
      "site": "0057e554",
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
                "const:ac5:8"
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
      "definition_site": "0057e634",
      "incomplete_value": true,
      "site": "0057e634",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:246:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e5f4",
      "incomplete_value": true,
      "site": "0057e5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:206:8"
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
      "0057e56c",
      "READ",
      [
        "storage",
        "002a67da",
        null,
        "string"
      ]
    ],
    [
      "0057e588",
      "READ",
      [
        "storage",
        "002bdac5",
        null,
        "string"
      ]
    ],
    [
      "0057e61c",
      "READ",
      [
        "storage",
        "002b6206",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e56c",
      "READ",
      [
        "storage",
        "002a677e",
        null,
        "string"
      ]
    ],
    [
      "0057e588",
      "READ",
      [
        "storage",
        "002bda71",
        null,
        "string"
      ]
    ],
    [
      "0057e61c",
      "READ",
      [
        "storage",
        "002b6246",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e5bc) · [`0057e508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e508) · [`0057e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md#insn-0057e510)
- 新版 `0057e5fc`（命令位置の公開資料なし） · `0057e548`（命令位置の公開資料なし） · `0057e550`（命令位置の公開資料なし）

~~~diff
- 0057e5bc ["INT_ADD", "register:40f0:8", ["const:57e5bc:8", "const:4:8"]]
- 0057e5bc ["CALL", null, ["callee:00497874:8"]]
+ 0057e5fc ["INT_ADD", "register:40f0:8", ["const:57e5fc:8", "const:4:8"]]
+ 0057e5fc ["CALL", null, ["callee:00497874:8"]]
- 0057e5bc bytes 9e64fc97
+ 0057e5fc bytes 9e64fc97
- 0057e508 ["INT_ADD", "register:40f0:8", ["const:57e508:8", "const:4:8"]]
- 0057e508 ["CALL", null, ["callee:00588eac:8"]]
+ 0057e548 ["INT_ADD", "register:40f0:8", ["const:57e548:8", "const:4:8"]]
+ 0057e548 ["CALL", null, ["callee:00588eac:8"]]
- 0057e508 bytes 592a0094
+ 0057e548 bytes 592a0094
- 0057e510 ["INT_ADD", "register:40f0:8", ["const:57e510:8", "const:4:8"]]
- 0057e510 ["CALL", null, ["callee:0058919c:8"]]
+ 0057e550 ["INT_ADD", "register:40f0:8", ["const:57e550:8", "const:4:8"]]
+ 0057e550 ["CALL", null, ["callee:0058919c:8"]]
- 0057e510 bytes 132b0094
+ 0057e550 bytes 132b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55144722bd04badf5636cec2ae590d0c"></a>

### [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) → [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) FUN_0057e874

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md)
- 新版 呼出元 1件 [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) · 呼出先 15件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057e8e0",
      "incomplete_value": true,
      "site": "0057e8ec",
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
                "const:a71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e8a0",
      "incomplete_value": true,
      "site": "0057e8ac",
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
                "const:ac5:8"
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
      "definition_site": "0057e98c",
      "incomplete_value": true,
      "site": "0057e98c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:246:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057e94c",
      "incomplete_value": true,
      "site": "0057e94c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:206:8"
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
      "definition_site": "0057e994",
      "incomplete_value": true,
      "site": "0057e994",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057e954",
      "incomplete_value": true,
      "site": "0057e954",
      "value": [
        "LOAD",
        "8",
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
      "0057e8c4",
      "READ",
      [
        "storage",
        "002a01f4",
        null,
        "string"
      ]
    ],
    [
      "0057e8e0",
      "READ",
      [
        "storage",
        "002bdac5",
        null,
        "string"
      ]
    ],
    [
      "0057e974",
      "READ",
      [
        "storage",
        "002b6206",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057e8c4",
      "READ",
      [
        "storage",
        "002a01a7",
        null,
        "string"
      ]
    ],
    [
      "0057e8e0",
      "READ",
      [
        "storage",
        "002bda71",
        null,
        "string"
      ]
    ],
    [
      "0057e974",
      "READ",
      [
        "storage",
        "002b6246",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e914) · [`0057e9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e9a8) · [`0057e860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md#insn-0057e860)
- 新版 `0057e954`（命令位置の公開資料なし） · `0057e9e8`（命令位置の公開資料なし） · `0057e8a0`（命令位置の公開資料なし）

~~~diff
- 0057e914 ["INT_ADD", "register:40f0:8", ["const:57e914:8", "const:4:8"]]
- 0057e914 ["CALL", null, ["callee:00497874:8"]]
+ 0057e954 ["INT_ADD", "register:40f0:8", ["const:57e954:8", "const:4:8"]]
+ 0057e954 ["CALL", null, ["callee:00497874:8"]]
- 0057e914 bytes c863fc97
+ 0057e954 bytes c863fc97
- 0057e9a8 ["INT_ADD", "register:40f0:8", ["const:57e9a8:8", "const:4:8"]]
- 0057e9a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057e9e8 ["INT_ADD", "register:40f0:8", ["const:57e9e8:8", "const:4:8"]]
+ 0057e9e8 ["CALL", null, ["callee:00c57f80:8"]]
- 0057e9a8 bytes 42651b94
+ 0057e9e8 bytes 66651b94
- 0057e860 ["INT_ADD", "register:40f0:8", ["const:57e860:8", "const:4:8"]]
- 0057e860 ["CALL", null, ["callee:00588eac:8"]]
+ 0057e8a0 ["INT_ADD", "register:40f0:8", ["const:57e8a0:8", "const:4:8"]]
+ 0057e8a0 ["CALL", null, ["callee:00588eac:8"]]
- 0057e860 bytes 83290094
+ 0057e8a0 bytes 83290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce1e52e8745ff909db22df113cff495a"></a>

### [`0057ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md) → [`0057eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057eea8.md) FUN_0057eea8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057eee8",
      "incomplete_value": true,
      "site": "0057eef8",
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
                "const:1b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057eea8",
      "incomplete_value": true,
      "site": "0057eeb8",
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
                "const:200:8"
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
      "definition_site": "0057eefc",
      "incomplete_value": true,
      "site": "0057eefc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057eebc",
      "incomplete_value": true,
      "site": "0057eebc",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057eee8",
      "READ",
      [
        "storage",
        "002a0200",
        null,
        "string"
      ]
    ],
    [
      "0057eef0",
      "READ",
      [
        "storage",
        "002a020d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057eee8",
      "READ",
      [
        "storage",
        "002a01b3",
        null,
        "string"
      ]
    ],
    [
      "0057eef0",
      "READ",
      [
        "storage",
        "002a01c0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057eef8) · [`0057ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057ee90) · [`0057ee98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057ee68.md#insn-0057ee98)
- 新版 `0057ef38`（命令位置の公開資料なし） · `0057eed0`（命令位置の公開資料なし） · `0057eed8`（命令位置の公開資料なし）

~~~diff
- 0057eef8 ["INT_ADD", "register:40f0:8", ["const:57eef8:8", "const:4:8"]]
- 0057eef8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057ef38 ["INT_ADD", "register:40f0:8", ["const:57ef38:8", "const:4:8"]]
+ 0057ef38 ["CALL", null, ["callee:00c57f80:8"]]
- 0057eef8 bytes ee631b94
+ 0057ef38 bytes 12641b94
- 0057ee90 ["INT_ADD", "register:40f0:8", ["const:57ee90:8", "const:4:8"]]
- 0057ee90 ["CALL", null, ["callee:00588eac:8"]]
+ 0057eed0 ["INT_ADD", "register:40f0:8", ["const:57eed0:8", "const:4:8"]]
+ 0057eed0 ["CALL", null, ["callee:00588eac:8"]]
- 0057ee90 bytes f7270094
+ 0057eed0 bytes f7270094
- 0057ee98 ["INT_ADD", "register:40f0:8", ["const:57ee98:8", "const:4:8"]]
- 0057ee98 ["CALL", null, ["callee:0058919c:8"]]
+ 0057eed8 ["INT_ADD", "register:40f0:8", ["const:57eed8:8", "const:4:8"]]
+ 0057eed8 ["CALL", null, ["callee:0058919c:8"]]
- 0057ee98 bytes b1280094
+ 0057eed8 bytes b1280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5952c28e0288faea7c2fed826cf80aca"></a>

### [`0057efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md) → [`0057f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f01c.md) FUN_0057f01c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f068",
      "incomplete_value": true,
      "site": "0057f084",
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
                "const:658:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f028",
      "incomplete_value": true,
      "site": "0057f044",
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
                "const:6b4:8"
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
      "0057f068",
      "READ",
      [
        "storage",
        "002a56b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f068",
      "READ",
      [
        "storage",
        "002a5658",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f004) · [`0057f084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f084) · [`0057f00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057efdc.md#insn-0057f00c)
- 新版 `0057f044`（命令位置の公開資料なし） · `0057f0c4`（命令位置の公開資料なし） · `0057f04c`（命令位置の公開資料なし）

~~~diff
- 0057f004 ["INT_ADD", "register:40f0:8", ["const:57f004:8", "const:4:8"]]
- 0057f004 ["CALL", null, ["callee:00588eac:8"]]
+ 0057f044 ["INT_ADD", "register:40f0:8", ["const:57f044:8", "const:4:8"]]
+ 0057f044 ["CALL", null, ["callee:00588eac:8"]]
- 0057f004 bytes 9a270094
+ 0057f044 bytes 9a270094
- 0057f084 ["INT_ADD", "register:40f0:8", ["const:57f084:8", "const:4:8"]]
- 0057f084 ["CALL", null, ["callee:0058919c:8"]]
+ 0057f0c4 ["INT_ADD", "register:40f0:8", ["const:57f0c4:8", "const:4:8"]]
+ 0057f0c4 ["CALL", null, ["callee:0058919c:8"]]
- 0057f084 bytes 36280094
+ 0057f0c4 bytes 36280094
- 0057f00c ["INT_ADD", "register:40f0:8", ["const:57f00c:8", "const:4:8"]]
- 0057f00c ["CALL", null, ["callee:0058919c:8"]]
+ 0057f04c ["INT_ADD", "register:40f0:8", ["const:57f04c:8", "const:4:8"]]
+ 0057f04c ["CALL", null, ["callee:0058919c:8"]]
- 0057f00c bytes 54280094
+ 0057f04c bytes 54280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc33f26e55edc75c0062193195409b8f"></a>

### [`0057f15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md) → [`0057f19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f19c.md) FUN_0057f19c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f1e8",
      "incomplete_value": true,
      "site": "0057f204",
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
                "const:179:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f1a8",
      "incomplete_value": true,
      "site": "0057f1c4",
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
                "const:1c6:8"
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
      "0057f1e8",
      "READ",
      [
        "storage",
        "0029f1c6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f1e8",
      "READ",
      [
        "storage",
        "0029f179",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f184) · [`0057f204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f204) · [`0057f18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f15c.md#insn-0057f18c)
- 新版 `0057f1c4`（命令位置の公開資料なし） · `0057f244`（命令位置の公開資料なし） · `0057f1cc`（命令位置の公開資料なし）

~~~diff
- 0057f184 ["INT_ADD", "register:40f0:8", ["const:57f184:8", "const:4:8"]]
- 0057f184 ["CALL", null, ["callee:00588eac:8"]]
+ 0057f1c4 ["INT_ADD", "register:40f0:8", ["const:57f1c4:8", "const:4:8"]]
+ 0057f1c4 ["CALL", null, ["callee:00588eac:8"]]
- 0057f184 bytes 3a270094
+ 0057f1c4 bytes 3a270094
- 0057f204 ["INT_ADD", "register:40f0:8", ["const:57f204:8", "const:4:8"]]
- 0057f204 ["CALL", null, ["callee:0058919c:8"]]
+ 0057f244 ["INT_ADD", "register:40f0:8", ["const:57f244:8", "const:4:8"]]
+ 0057f244 ["CALL", null, ["callee:0058919c:8"]]
- 0057f204 bytes d6270094
+ 0057f244 bytes d6270094
- 0057f18c ["INT_ADD", "register:40f0:8", ["const:57f18c:8", "const:4:8"]]
- 0057f18c ["CALL", null, ["callee:0058919c:8"]]
+ 0057f1cc ["INT_ADD", "register:40f0:8", ["const:57f1cc:8", "const:4:8"]]
+ 0057f1cc ["CALL", null, ["callee:0058919c:8"]]
- 0057f18c bytes f4270094
+ 0057f1cc bytes f4270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfabb2cdc6b4a110bf0e969890dd214e"></a>

### [`0057f2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md) → [`0057f314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f314.md) FUN_0057f314

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f360",
      "incomplete_value": true,
      "site": "0057f370",
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
                "const:8c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f320",
      "incomplete_value": true,
      "site": "0057f330",
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
                "const:91e:8"
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
      "definition_site": "0057f378",
      "incomplete_value": true,
      "site": "0057f378",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f338",
      "incomplete_value": true,
      "site": "0057f338",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f374",
      "incomplete_value": true,
      "site": "0057f38c",
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
    "old": {
      "definition_site": "0057f334",
      "incomplete_value": true,
      "site": "0057f34c",
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
      "0057f360",
      "READ",
      [
        "storage",
        "002ac91e",
        null,
        "string"
      ]
    ],
    [
      "0057f364",
      "READ",
      [
        "storage",
        "002ac92d",
        null,
        "string"
      ]
    ],
    [
      "0057f374",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057f360",
      "READ",
      [
        "storage",
        "002ac8c2",
        null,
        "string"
      ]
    ],
    [
      "0057f364",
      "READ",
      [
        "storage",
        "002ac8d1",
        null,
        "string"
      ]
    ],
    [
      "0057f374",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f38c) · [`0057f2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f2fc) · [`0057f304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f2d4.md#insn-0057f304)
- 新版 `0057f3cc`（命令位置の公開資料なし） · `0057f33c`（命令位置の公開資料なし） · `0057f344`（命令位置の公開資料なし）

~~~diff
- 0057f38c ["INT_ADD", "register:40f0:8", ["const:57f38c:8", "const:4:8"]]
- 0057f38c ["CALL", null, ["callee:00c57f80:8"]]
+ 0057f3cc ["INT_ADD", "register:40f0:8", ["const:57f3cc:8", "const:4:8"]]
+ 0057f3cc ["CALL", null, ["callee:00c57f80:8"]]
- 0057f38c bytes c9621b94
+ 0057f3cc bytes ed621b94
- 0057f2fc ["INT_ADD", "register:40f0:8", ["const:57f2fc:8", "const:4:8"]]
- 0057f2fc ["CALL", null, ["callee:00588eac:8"]]
+ 0057f33c ["INT_ADD", "register:40f0:8", ["const:57f33c:8", "const:4:8"]]
+ 0057f33c ["CALL", null, ["callee:00588eac:8"]]
- 0057f2fc bytes dc260094
+ 0057f33c bytes dc260094
- 0057f304 ["INT_ADD", "register:40f0:8", ["const:57f304:8", "const:4:8"]]
- 0057f304 ["CALL", null, ["callee:0058919c:8"]]
+ 0057f344 ["INT_ADD", "register:40f0:8", ["const:57f344:8", "const:4:8"]]
+ 0057f344 ["CALL", null, ["callee:0058919c:8"]]
- 0057f304 bytes 96270094
+ 0057f344 bytes 96270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca42bc8aea1ea6fc629132322fb4cfa8"></a>

### [`0057f464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md) → [`0057f4a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f4a4.md) FUN_0057f4a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f4f4",
      "incomplete_value": true,
      "site": "0057f50c",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e33:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f4b4",
      "incomplete_value": true,
      "site": "0057f4cc",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e87:8"
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
      "definition_site": "0057f510",
      "incomplete_value": true,
      "site": "0057f51c",
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
                "const:f4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f4d0",
      "incomplete_value": true,
      "site": "0057f4dc",
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
                "const:f1d:8"
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
      "definition_site": "0057f520",
      "incomplete_value": true,
      "site": "0057f520",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f4e0",
      "incomplete_value": true,
      "site": "0057f4e0",
      "value": [
        "LOAD",
        "8",
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
      "0057f4f4",
      "READ",
      [
        "storage",
        "002bee87",
        null,
        "string"
      ]
    ],
    [
      "0057f510",
      "READ",
      [
        "storage",
        "002b4f1d",
        null,
        "string"
      ]
    ],
    [
      "0057f514",
      "READ",
      [
        "storage",
        "002b4f2b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f4f4",
      "READ",
      [
        "storage",
        "002bee33",
        null,
        "string"
      ]
    ],
    [
      "0057f510",
      "READ",
      [
        "storage",
        "002b4f4e",
        null,
        "string"
      ]
    ],
    [
      "0057f514",
      "READ",
      [
        "storage",
        "002b4f5c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f49c) · [`0057f494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f494) · [`0057f4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f464.md#insn-0057f4a8)
- 新版 `0057f4dc`（命令位置の公開資料なし） · `0057f4d4`（命令位置の公開資料なし） · `0057f4e8`（命令位置の公開資料なし）

~~~diff
- 0057f49c ["INT_ADD", "register:40f0:8", ["const:57f49c:8", "const:4:8"]]
- 0057f49c ["CALL", null, ["callee:0058919c:8"]]
+ 0057f4dc ["INT_ADD", "register:40f0:8", ["const:57f4dc:8", "const:4:8"]]
+ 0057f4dc ["CALL", null, ["callee:0058919c:8"]]
- 0057f49c bytes 30270094
+ 0057f4dc bytes 30270094
- 0057f494 ["INT_ADD", "register:40f0:8", ["const:57f494:8", "const:4:8"]]
- 0057f494 ["CALL", null, ["callee:00588eac:8"]]
+ 0057f4d4 ["INT_ADD", "register:40f0:8", ["const:57f4d4:8", "const:4:8"]]
+ 0057f4d4 ["CALL", null, ["callee:00588eac:8"]]
- 0057f494 bytes 76260094
+ 0057f4d4 bytes 76260094
- 0057f4a8 ["COPY", "tmp:0:8", ["const:e87:8"]]
- 0057f4a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f4a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f4a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f4e8 ["COPY", "tmp:0:8", ["const:e33:8"]]
+ 0057f4e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f4e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f4a8 bytes 291d3a91
+ 0057f4e8 bytes 29cd3891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0ce8ca2e3ed16181a762f500250f11"></a>

### [`0057f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md) → [`0057f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f66c.md) FUN_0057f66c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589154.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589194.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.35% / 新版 90.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f6b4",
      "incomplete_value": true,
      "site": "0057f6c4",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:256:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f674",
      "incomplete_value": true,
      "site": "0057f684",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:216:8"
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
      "definition_site": "0057f6e0",
      "incomplete_value": true,
      "site": "0057f6f0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:faf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f6a0",
      "incomplete_value": true,
      "site": "0057f6b0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:f6f:8"
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
      "definition_site": "0057f6e4",
      "incomplete_value": true,
      "site": "0057f6f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057f6a4",
      "incomplete_value": true,
      "site": "0057f6b4",
      "value": [
        "LOAD",
        "8",
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
      "0057f6b4",
      "READ",
      [
        "storage",
        "002b6216",
        null,
        "string"
      ]
    ],
    [
      "0057f6e0",
      "READ",
      [
        "storage",
        "002bff6f",
        null,
        "string"
      ]
    ],
    [
      "0057f6e4",
      "READ",
      [
        "storage",
        "002bff7f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057f6b4",
      "READ",
      [
        "storage",
        "002b6256",
        null,
        "string"
      ]
    ],
    [
      "0057f6e0",
      "READ",
      [
        "storage",
        "002bffaf",
        null,
        "string"
      ]
    ],
    [
      "0057f6e4",
      "READ",
      [
        "storage",
        "002bffbf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f6f4) · [`0057f65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f65c) · [`0057f664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f62c.md#insn-0057f664)
- 新版 `0057f734`（命令位置の公開資料なし） · `0057f69c`（命令位置の公開資料なし） · `0057f6a4`（命令位置の公開資料なし）

~~~diff
- 0057f6f4 ["INT_ADD", "register:40f0:8", ["const:57f6f4:8", "const:4:8"]]
- 0057f6f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057f734 ["INT_ADD", "register:40f0:8", ["const:57f734:8", "const:4:8"]]
+ 0057f734 ["CALL", null, ["callee:00c57f80:8"]]
- 0057f6f4 bytes ef611b94
+ 0057f734 bytes 13621b94
- 0057f65c ["INT_ADD", "register:40f0:8", ["const:57f65c:8", "const:4:8"]]
- 0057f65c ["CALL", null, ["callee:00588eac:8"]]
+ 0057f69c ["INT_ADD", "register:40f0:8", ["const:57f69c:8", "const:4:8"]]
+ 0057f69c ["CALL", null, ["callee:00588eac:8"]]
- 0057f65c bytes 04260094
+ 0057f69c bytes 04260094
- 0057f664 ["INT_ADD", "register:40f0:8", ["const:57f664:8", "const:4:8"]]
- 0057f664 ["CALL", null, ["callee:0058919c:8"]]
+ 0057f6a4 ["INT_ADD", "register:40f0:8", ["const:57f6a4:8", "const:4:8"]]
+ 0057f6a4 ["CALL", null, ["callee:0058919c:8"]]
- 0057f664 bytes be260094
+ 0057f6a4 bytes be260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489a4012ba7d4dc20b4e7d0e8372431b"></a>

### [`0057f86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md) → [`0057f8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057f8ac.md) FUN_0057f8ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0055c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057f91c",
      "incomplete_value": true,
      "site": "0057f91c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f8dc",
      "incomplete_value": true,
      "site": "0057f8dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dba:8"
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
      "definition_site": "0057f938",
      "incomplete_value": true,
      "site": "0057f948",
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
                "const:8a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057f8f8",
      "incomplete_value": true,
      "site": "0057f908",
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
                "const:860:8"
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
      "0057f908",
      "READ",
      [
        "storage",
        "002a9dba",
        null,
        "string"
      ]
    ],
    [
      "0057f910",
      "READ",
      [
        "storage",
        "002a9dbf",
        null,
        "string"
      ]
    ],
    [
      "0057f938",
      "READ",
      [
        "storage",
        "002c2860",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0057f908",
      "READ",
      [
        "storage",
        "002a9d5e",
        null,
        "string"
      ]
    ],
    [
      "0057f910",
      "READ",
      [
        "storage",
        "002a9d63",
        null,
        "string"
      ]
    ],
    [
      "0057f938",
      "READ",
      [
        "storage",
        "002c28a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057f8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8b0) · [`0057f8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8b8) · [`0057f8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057f86c.md#insn-0057f8c4)
- 新版 `0057f8f0`（命令位置の公開資料なし） · `0057f8f8`（命令位置の公開資料なし） · `0057f904`（命令位置の公開資料なし）

~~~diff
- 0057f8b0 ["INT_ADD", "register:40f0:8", ["const:57f8b0:8", "const:4:8"]]
- 0057f8b0 ["CALL", null, ["callee:00588eac:8"]]
+ 0057f8f0 ["INT_ADD", "register:40f0:8", ["const:57f8f0:8", "const:4:8"]]
+ 0057f8f0 ["CALL", null, ["callee:00588eac:8"]]
- 0057f8b0 bytes 6f250094
+ 0057f8f0 bytes 6f250094
- 0057f8b8 ["INT_ADD", "register:40f0:8", ["const:57f8b8:8", "const:4:8"]]
- 0057f8b8 ["CALL", null, ["callee:0058919c:8"]]
+ 0057f8f8 ["INT_ADD", "register:40f0:8", ["const:57f8f8:8", "const:4:8"]]
+ 0057f8f8 ["CALL", null, ["callee:0058919c:8"]]
- 0057f8b8 bytes 29260094
+ 0057f8f8 bytes 29260094
- 0057f8c4 ["COPY", "tmp:0:8", ["const:dba:8"]]
- 0057f8c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057f8c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057f8c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0057f904 ["COPY", "tmp:0:8", ["const:d5e:8"]]
+ 0057f904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0057f904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057f8c4 bytes 29e93691
+ 0057f904 bytes 29793591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22fd25948187a740b2f344c65231538e"></a>

### [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) → [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) FUN_0057fb4c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00555298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555298.md) [`0057fd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fd20.md) [`0057fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md) [`0057fe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md) [`0057fefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fefc.md) · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 6件 [`005552d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552d8.md) [`0057fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fd60.md) [`0057fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md) [`0057fe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md) [`0057ff3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ff3c.md) · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fbb0",
      "incomplete_value": true,
      "site": "0057fbb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fb70",
      "incomplete_value": true,
      "site": "0057fb70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cde:8"
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
      "definition_site": "0057fbb8",
      "incomplete_value": true,
      "site": "0057fbb8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fb78",
      "incomplete_value": true,
      "site": "0057fb78",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fbb4",
      "incomplete_value": true,
      "site": "0057fbc8",
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
                "const:275:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fb74",
      "incomplete_value": true,
      "site": "0057fb88",
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
                "const:2c2:8"
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
      "0057fb98",
      "READ",
      [
        "storage",
        "002b2cde",
        null,
        "string"
      ]
    ],
    [
      "0057fba0",
      "READ",
      [
        "storage",
        "002b2ce3",
        null,
        "string"
      ]
    ],
    [
      "0057fbb4",
      "READ",
      [
        "storage",
        "002a12c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fb98",
      "READ",
      [
        "storage",
        "002b2d0f",
        null,
        "string"
      ]
    ],
    [
      "0057fba0",
      "READ",
      [
        "storage",
        "002b2d14",
        null,
        "string"
      ]
    ],
    [
      "0057fbb4",
      "READ",
      [
        "storage",
        "002a1275",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fb48) · [`0057fc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fc9c) · [`0057fb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md#insn-0057fb40)
- 新版 `0057fb88`（命令位置の公開資料なし） · `0057fcdc`（命令位置の公開資料なし） · `0057fb80`（命令位置の公開資料なし）

~~~diff
- 0057fb48 ["INT_ADD", "register:40f0:8", ["const:57fb48:8", "const:4:8"]]
- 0057fb48 ["CALL", null, ["callee:0058919c:8"]]
+ 0057fb88 ["INT_ADD", "register:40f0:8", ["const:57fb88:8", "const:4:8"]]
+ 0057fb88 ["CALL", null, ["callee:0058919c:8"]]
- 0057fb48 bytes 85250094
+ 0057fb88 bytes 85250094
- 0057fc9c ["INT_ADD", "register:40f0:8", ["const:57fc9c:8", "const:4:8"]]
- 0057fc9c ["CALL", null, ["callee:0058a8fc:8"]]
+ 0057fcdc ["INT_ADD", "register:40f0:8", ["const:57fcdc:8", "const:4:8"]]
+ 0057fcdc ["CALL", null, ["callee:0058a8fc:8"]]
- 0057fc9c bytes 082b0094
+ 0057fcdc bytes 082b0094
- 0057fb40 ["INT_ADD", "register:40f0:8", ["const:57fb40:8", "const:4:8"]]
- 0057fb40 ["CALL", null, ["callee:00588eac:8"]]
+ 0057fb80 ["INT_ADD", "register:40f0:8", ["const:57fb80:8", "const:4:8"]]
+ 0057fb80 ["CALL", null, ["callee:00588eac:8"]]
- 0057fb40 bytes cb240094
+ 0057fb80 bytes cb240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40dec2f09796a4048e14e72c8bd5521d"></a>

### [`0057fda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md) → [`0057fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fde8.md) FUN_0057fde8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a0.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005552e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e0.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fe24",
      "incomplete_value": true,
      "site": "0057fe24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fde4",
      "incomplete_value": true,
      "site": "0057fde4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:936:8"
              ]
            ]
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
      "0057fe08",
      "READ",
      [
        "storage",
        "002ac936",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057fe08",
      "READ",
      [
        "storage",
        "002ac8da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fdc0) · [`0057fdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fdf0) · [`0057fe00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fda8.md#insn-0057fe00)
- 新版 `0057fe00`（命令位置の公開資料なし） · `0057fe30`（命令位置の公開資料なし） · `0057fe40`（命令位置の公開資料なし）

~~~diff
- 0057fdc0 ["COPY", "tmp:0:8", ["const:936:8"]]
- 0057fdc0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0057fdc0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0057fdc0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0057fe00 ["COPY", "tmp:0:8", ["const:8da:8"]]
+ 0057fe00 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fe00 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0057fe00 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0057fdc0 bytes 6bd92491
+ 0057fe00 bytes 6b692391
- 0057fdf0 ["INT_ADD", "register:40f0:8", ["const:57fdf0:8", "const:4:8"]]
- 0057fdf0 ["CALL", null, ["callee:0057fb4c:8"]]
+ 0057fe30 ["INT_ADD", "register:40f0:8", ["const:57fe30:8", "const:4:8"]]
+ 0057fe30 ["CALL", null, ["callee:0057fb4c:8"]]
- 0057fdf0 bytes 47ffff97
+ 0057fe30 bytes 47ffff97
- 0057fe00 ["INT_ADD", "register:40f0:8", ["const:57fe00:8", "const:4:8"]]
- 0057fe00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057fe40 ["INT_ADD", "register:40f0:8", ["const:57fe40:8", "const:4:8"]]
+ 0057fe40 ["CALL", null, ["callee:00c57f80:8"]]
- 0057fe00 bytes 2c601b94
+ 0057fe40 bytes 50601b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2889fe563936c5184d7a585050fd431e"></a>

### [`0057fe54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md) → [`0057fe94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fe94.md) FUN_0057fe94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552a4.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005552e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552e4.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0057fec8",
      "incomplete_value": true,
      "site": "0057fec8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:3fc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057fe88",
      "incomplete_value": true,
      "site": "0057fe88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057fecc",
      "incomplete_value": true,
      "site": "0057fecc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057fe8c",
      "incomplete_value": true,
      "site": "0057fe8c",
      "value": [
        "LOAD",
        "8",
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
      "0057feb4",
      "READ",
      [
        "storage",
        "002ba450",
        null,
        "string"
      ]
    ],
    [
      "0057fec0",
      "READ",
      [
        "storage",
        "002ba456",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057feb4",
      "READ",
      [
        "storage",
        "002ba3fc",
        null,
        "string"
      ]
    ],
    [
      "0057fec0",
      "READ",
      [
        "storage",
        "002ba402",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057fe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fe6c) · [`0057fe98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fe98) · [`0057fea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fe54.md#insn-0057fea8)
- 新版 `0057feac`（命令位置の公開資料なし） · `0057fed8`（命令位置の公開資料なし） · `0057fee8`（命令位置の公開資料なし）

~~~diff
- 0057fe6c ["COPY", "tmp:0:8", ["const:450:8"]]
- 0057fe6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057fe6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057fe6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057feac ["COPY", "tmp:0:8", ["const:3fc:8"]]
+ 0057feac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057feac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057feac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057fe6c bytes 4a411191
+ 0057feac bytes 4af10f91
- 0057fe98 ["INT_ADD", "register:40f0:8", ["const:57fe98:8", "const:4:8"]]
- 0057fe98 ["CALL", null, ["callee:0057fb4c:8"]]
+ 0057fed8 ["INT_ADD", "register:40f0:8", ["const:57fed8:8", "const:4:8"]]
+ 0057fed8 ["CALL", null, ["callee:0057fb4c:8"]]
- 0057fe98 bytes 1dffff97
+ 0057fed8 bytes 1dffff97
- 0057fea8 ["INT_ADD", "register:40f0:8", ["const:57fea8:8", "const:4:8"]]
- 0057fea8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0057fee8 ["INT_ADD", "register:40f0:8", ["const:57fee8:8", "const:4:8"]]
+ 0057fee8 ["CALL", null, ["callee:00c57f80:8"]]
- 0057fea8 bytes 02601b94
+ 0057fee8 bytes 26601b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c864273016d198d5ec718c6c517e04"></a>

### [`0057ffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md) → [`0057ffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057ffe0.md) FUN_0057ffe0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005552ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/005552ac.md) · 呼出先 3件 [`0057fb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057fb0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005552ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552ec.md) · 呼出先 3件 [`0057fb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057f/0057fb4c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00580014",
      "incomplete_value": true,
      "site": "00580014",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057ffd4",
      "incomplete_value": true,
      "site": "0057ffd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b21:8"
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
      "definition_site": "00580018",
      "incomplete_value": true,
      "site": "00580018",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057ffd8",
      "incomplete_value": true,
      "site": "0057ffd8",
      "value": [
        "LOAD",
        "8",
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
      "00580000",
      "READ",
      [
        "storage",
        "002afb21",
        null,
        "string"
      ]
    ],
    [
      "0058000c",
      "READ",
      [
        "storage",
        "002afb26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580000",
      "READ",
      [
        "storage",
        "002afac5",
        null,
        "string"
      ]
    ],
    [
      "0058000c",
      "READ",
      [
        "storage",
        "002afaca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057ffb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057ffb8) · [`0057ffe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057ffe4) · [`0057fff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057f/0057ffa0.md#insn-0057fff4)
- 新版 `0057fff8`（命令位置の公開資料なし） · `00580024`（命令位置の公開資料なし） · `00580034`（命令位置の公開資料なし）

~~~diff
- 0057ffb8 ["COPY", "tmp:0:8", ["const:b21:8"]]
- 0057ffb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0057ffb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0057ffb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0057fff8 ["COPY", "tmp:0:8", ["const:ac5:8"]]
+ 0057fff8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fff8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0057fff8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0057ffb8 bytes 4a852c91
+ 0057fff8 bytes 4a152b91
- 0057ffe4 ["INT_ADD", "register:40f0:8", ["const:57ffe4:8", "const:4:8"]]
- 0057ffe4 ["CALL", null, ["callee:0057fb4c:8"]]
+ 00580024 ["INT_ADD", "register:40f0:8", ["const:580024:8", "const:4:8"]]
+ 00580024 ["CALL", null, ["callee:0057fb4c:8"]]
- 0057ffe4 bytes cafeff97
+ 00580024 bytes cafeff97
- 0057fff4 ["INT_ADD", "register:40f0:8", ["const:57fff4:8", "const:4:8"]]
- 0057fff4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00580034 ["INT_ADD", "register:40f0:8", ["const:580034:8", "const:4:8"]]
+ 00580034 ["CALL", null, ["callee:00c57f80:8"]]
- 0057fff4 bytes af5f1b94
+ 00580034 bytes d35f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580c1067888600ee94ddba663f088111"></a>

### [`00580048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580048.md) → [`00580088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580088.md) FUN_00580088

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
      "definition_site": "0058008c",
      "incomplete_value": false,
      "site": "00580090",
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
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058004c",
      "incomplete_value": false,
      "site": "00580050",
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
            "const:4c0:8"
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
      "00580090",
      "DATA",
      [
        "storage",
        "00c6c4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580090",
      "DATA",
      [
        "storage",
        "00c6c590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058004c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580048.md#insn-0058004c)
- 新版 `0058008c`（命令位置の公開資料なし）

~~~diff
- 0058004c ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 0058004c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058004c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058004c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058008c ["COPY", "tmp:0:8", ["const:590:8"]]
+ 0058008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058004c bytes 08011391
+ 0058008c bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e2b4c7dd5bbe30a3fe4f1b0515577b"></a>

### [`00580058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md) → [`00580098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580098.md) FUN_00580098

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
      "definition_site": "005800a8",
      "incomplete_value": false,
      "site": "005800b0",
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
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580068",
      "incomplete_value": false,
      "site": "00580070",
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
            "const:4c0:8"
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
      "005800b0",
      "DATA",
      [
        "storage",
        "00c6c4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005800b0",
      "DATA",
      [
        "storage",
        "00c6c590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md#insn-00580068) · [`00580074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580058.md#insn-00580074)
- 新版 `005800a8`（命令位置の公開資料なし） · `005800b4`（命令位置の公開資料なし）

~~~diff
- 00580068 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00580068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005800a8 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005800a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005800a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005800a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580068 bytes 08011391
+ 005800a8 bytes 08411691
- 00580074 ["INT_ADD", "register:40f0:8", ["const:580074:8", "const:4:8"]]
- 00580074 ["CALL", null, ["callee:00c57f70:8"]]
+ 005800b4 ["INT_ADD", "register:40f0:8", ["const:5800b4:8", "const:4:8"]]
+ 005800b4 ["CALL", null, ["callee:00c57f70:8"]]
- 00580074 bytes 8b5f1b94
+ 005800b4 bytes af5f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce699dcb10d2071c24e649346d2170c3"></a>

### [`00580098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md) → [`005800d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md) FUN_005800d8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6d0.md) · 呼出先 17件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`0055c6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6d4.md) [`0055c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c6dc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md)
- 新版 呼出元 1件 [`0055c710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c710.md) · 呼出先 17件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`0055c714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c714.md) [`0055c71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c71c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.69% / 新版 93.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580140",
      "incomplete_value": true,
      "site": "00580140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580100",
      "incomplete_value": true,
      "site": "00580100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cec:8"
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
      "definition_site": "0058015c",
      "incomplete_value": true,
      "site": "00580164",
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
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058011c",
      "incomplete_value": true,
      "site": "00580124",
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
                "const:920:8"
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
      "definition_site": "00580158",
      "incomplete_value": true,
      "site": "00580168",
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
                "const:874:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580118",
      "incomplete_value": true,
      "site": "00580128",
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
                "const:8d0:8"
              ]
            ]
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
      "0058012c",
      "READ",
      [
        "storage",
        "002b2cec",
        null,
        "string"
      ]
    ],
    [
      "00580158",
      "READ",
      [
        "storage",
        "002ad8d0",
        null,
        "string"
      ]
    ],
    [
      "00580158",
      "READ",
      [
        "storage",
        "002ad8e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058012c",
      "READ",
      [
        "storage",
        "002b2d1d",
        null,
        "string"
      ]
    ],
    [
      "00580158",
      "READ",
      [
        "storage",
        "002ad874",
        null,
        "string"
      ]
    ],
    [
      "00580158",
      "READ",
      [
        "storage",
        "002ad884",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-00580164) · [`0058017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-0058017c) · [`005803d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md#insn-005803d8)
- 新版 `005801a4`（命令位置の公開資料なし） · `005801bc`（命令位置の公開資料なし） · `00580418`（命令位置の公開資料なし）

~~~diff
- 00580164 ["INT_ADD", "register:40f0:8", ["const:580164:8", "const:4:8"]]
- 00580164 ["CALL", null, ["callee:00c57f80:8"]]
+ 005801a4 ["INT_ADD", "register:40f0:8", ["const:5801a4:8", "const:4:8"]]
+ 005801a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00580164 bytes 535f1b94
+ 005801a4 bytes 775f1b94
- 0058017c ["INT_ADD", "register:40f0:8", ["const:58017c:8", "const:4:8"]]
- 0058017c ["CALL", null, ["callee:00589184:8"]]
+ 005801bc ["INT_ADD", "register:40f0:8", ["const:5801bc:8", "const:4:8"]]
+ 005801bc ["CALL", null, ["callee:00589184:8"]]
- 0058017c bytes f2230094
+ 005801bc bytes f2230094
- 005803d8 ["INT_ADD", "register:40f0:8", ["const:5803d8:8", "const:4:8"]]
- 005803d8 ["CALL", null, ["ram:589f08:8"]]
+ 00580418 ["INT_ADD", "register:40f0:8", ["const:580418:8", "const:4:8"]]
+ 00580418 ["CALL", null, ["ram:589f48:8"]]
- 005803d8 bytes cc260094
+ 00580418 bytes cc260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5cac0444b570e96b8cd100e2a5afe4"></a>

### [`005804a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md) → [`005804e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005804e4.md) FUN_005804e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055c820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c820.md) · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`0055c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055c/0055c7c4.md) [`0057dde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057dde8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`0055c860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c860.md) · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0055c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055c/0055c804.md) [`0057de28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de28.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580538",
      "incomplete_value": true,
      "site": "00580538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005804f8",
      "incomplete_value": true,
      "site": "005804f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad6:8"
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
      "definition_site": "00580558",
      "incomplete_value": true,
      "site": "00580560",
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580518",
      "incomplete_value": true,
      "site": "00580520",
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
                "const:1a0:8"
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
      "definition_site": "00580554",
      "incomplete_value": true,
      "site": "00580564",
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
                "const:926:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580514",
      "incomplete_value": true,
      "site": "00580524",
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
                "const:982:8"
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
      "00580528",
      "READ",
      [
        "storage",
        "002bdad6",
        null,
        "string"
      ]
    ],
    [
      "00580554",
      "READ",
      [
        "storage",
        "002a7982",
        null,
        "string"
      ]
    ],
    [
      "00580554",
      "READ",
      [
        "storage",
        "002a7992",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580528",
      "READ",
      [
        "storage",
        "002bda82",
        null,
        "string"
      ]
    ],
    [
      "00580554",
      "READ",
      [
        "storage",
        "002a7926",
        null,
        "string"
      ]
    ],
    [
      "00580554",
      "READ",
      [
        "storage",
        "002a7936",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005804e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-005804e0) · [`0058059c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-0058059c) · [`005806bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/005804a4.md#insn-005806bc)
- 新版 `00580520`（命令位置の公開資料なし） · `005805dc`（命令位置の公開資料なし） · `005806fc`（命令位置の公開資料なし）

~~~diff
- 005804e0 ["COPY", "tmp:0:8", ["const:ad6:8"]]
- 005804e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005804e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005804e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00580520 ["COPY", "tmp:0:8", ["const:a82:8"]]
+ 00580520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00580520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00580520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005804e0 bytes 29592b91
+ 00580520 bytes 29092a91
- 0058059c ["INT_ADD", "register:40f0:8", ["const:58059c:8", "const:4:8"]]
- 0058059c ["CALL", null, ["callee:00c586e0:8"]]
+ 005805dc ["INT_ADD", "register:40f0:8", ["const:5805dc:8", "const:4:8"]]
+ 005805dc ["CALL", null, ["callee:00c586e0:8"]]
- 0058059c bytes 1d601b94
+ 005805dc bytes 41601b94
- 005806bc ["INT_ADD", "register:40f0:8", ["const:5806bc:8", "const:4:8"]]
- 005806bc ["CALL", null, ["callee:00c5a390:8"]]
+ 005806fc ["INT_ADD", "register:40f0:8", ["const:5806fc:8", "const:4:8"]]
+ 005806fc ["CALL", null, ["callee:00c5a390:8"]]
- 005806bc bytes 01671b94
+ 005806fc bytes 25671b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd67e4659a140b557d5c25d313182ffd"></a>

### [`00580888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md) → [`005808c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md) FUN_005808c8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560454.md) · 呼出先 10件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00560494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560494.md) · 呼出先 10件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058093c",
      "incomplete_value": true,
      "site": "0058094c",
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
                "const:1c9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005808fc",
      "incomplete_value": true,
      "site": "0058090c",
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
                "const:216:8"
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
      "definition_site": "00580940",
      "incomplete_value": true,
      "site": "00580950",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00580900",
      "incomplete_value": true,
      "site": "00580910",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580944",
      "incomplete_value": true,
      "site": "00580954",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580904",
      "incomplete_value": true,
      "site": "00580914",
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
                "const:2a0:8"
              ]
            ]
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
      "00580910",
      "READ",
      [
        "storage",
        "002c12cc",
        null,
        "string"
      ]
    ],
    [
      "0058093c",
      "READ",
      [
        "storage",
        "002a0216",
        null,
        "string"
      ]
    ],
    [
      "00580940",
      "READ",
      [
        "storage",
        "002a0226",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00580910",
      "READ",
      [
        "storage",
        "002c130c",
        null,
        "string"
      ]
    ],
    [
      "0058093c",
      "READ",
      [
        "storage",
        "002a01c9",
        null,
        "string"
      ]
    ],
    [
      "00580940",
      "READ",
      [
        "storage",
        "002a01d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-00580950) · [`005808b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-005808b4) · [`005808bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md#insn-005808bc)
- 新版 `00580990`（命令位置の公開資料なし） · `005808f4`（命令位置の公開資料なし） · `005808fc`（命令位置の公開資料なし）

~~~diff
- 00580950 ["INT_ADD", "register:40f0:8", ["const:580950:8", "const:4:8"]]
- 00580950 ["CALL", null, ["callee:00c57f80:8"]]
+ 00580990 ["INT_ADD", "register:40f0:8", ["const:580990:8", "const:4:8"]]
+ 00580990 ["CALL", null, ["callee:00c57f80:8"]]
- 00580950 bytes 585d1b94
+ 00580990 bytes 7c5d1b94
- 005808b4 ["INT_ADD", "register:40f0:8", ["const:5808b4:8", "const:4:8"]]
- 005808b4 ["CALL", null, ["callee:00588eac:8"]]
+ 005808f4 ["INT_ADD", "register:40f0:8", ["const:5808f4:8", "const:4:8"]]
+ 005808f4 ["CALL", null, ["callee:00588eac:8"]]
- 005808b4 bytes 6e210094
+ 005808f4 bytes 6e210094
- 005808bc ["INT_ADD", "register:40f0:8", ["const:5808bc:8", "const:4:8"]]
- 005808bc ["CALL", null, ["callee:0058919c:8"]]
+ 005808fc ["INT_ADD", "register:40f0:8", ["const:5808fc:8", "const:4:8"]]
+ 005808fc ["CALL", null, ["callee:0058919c:8"]]
- 005808bc bytes 28220094
+ 005808fc bytes 28220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ccbd150f182ae4771377828331ec25"></a>

### [`00580b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md) → [`00580b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md) FUN_00580b70

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056045c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056045c.md) · 呼出先 8件 [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0056049c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056049c.md) · 呼出先 8件 [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580bd4",
      "incomplete_value": false,
      "site": "00580be0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580b94",
      "incomplete_value": false,
      "site": "00580ba0",
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
            "const:260:8"
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
      "00580be0",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00580be0",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b80) · [`00580b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b88) · [`00580b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md#insn-00580b94)
- 新版 `00580bc0`（命令位置の公開資料なし） · `00580bc8`（命令位置の公開資料なし） · `00580bd4`（命令位置の公開資料なし）

~~~diff
- 00580b80 ["INT_ADD", "register:40f0:8", ["const:580b80:8", "const:4:8"]]
- 00580b80 ["CALL", null, ["callee:00c59230:8"]]
+ 00580bc0 ["INT_ADD", "register:40f0:8", ["const:580bc0:8", "const:4:8"]]
+ 00580bc0 ["CALL", null, ["callee:00c59230:8"]]
- 00580b80 bytes 78611b94
+ 00580bc0 bytes 9c611b94
- 00580b88 ["INT_ADD", "register:40f0:8", ["const:580b88:8", "const:4:8"]]
- 00580b88 ["CALL", null, ["callee:00c57f60:8"]]
+ 00580bc8 ["INT_ADD", "register:40f0:8", ["const:580bc8:8", "const:4:8"]]
+ 00580bc8 ["CALL", null, ["callee:00c57f60:8"]]
- 00580b88 bytes c25c1b94
+ 00580bc8 bytes e65c1b94
- 00580b94 ["COPY", "tmp:0:8", ["const:260:8"]]
- 00580b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00580b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00580b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00580bd4 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 00580bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00580bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00580bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00580b94 bytes 08810991
+ 00580bd4 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b0ec801adc6783950898bbdb7ea0c70"></a>

### [`00580ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md) → [`00580ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580ce0.md) FUN_00580ce0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec80.md) · 呼出先 9件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`0055ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc0.md) · 呼出先 9件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00580da0",
      "incomplete_value": true,
      "site": "00580da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00580d60",
      "incomplete_value": true,
      "site": "00580d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580df4",
      "incomplete_value": false,
      "site": "00580dfc",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580db4",
      "incomplete_value": false,
      "site": "00580dbc",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00580e0c",
      "incomplete_value": false,
      "site": "00580e0c",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00580dcc",
      "incomplete_value": false,
      "site": "00580dcc",
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
            "const:5b0:8"
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
      "00580d88",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00580da0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580dfc",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00580d88",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "00580da0",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00580dfc",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00580d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580d20) · [`00580d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580d8c) · [`00580dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580ca0.md#insn-00580dec)
- 新版 `00580d60`（命令位置の公開資料なし） · `00580dcc`（命令位置の公開資料なし） · `00580e2c`（命令位置の公開資料なし）

~~~diff
- 00580d20 ["COPY", "register:0:8", ["register:4048:8"]]
- 00580d20 ["INT_ADD", "register:40f0:8", ["const:580d20:8", "const:4:8"]]
- 00580d20 ["CALLIND", null, ["register:0:8"]]
+ 00580d60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580d60 ["INT_ADD", "register:40f0:8", ["const:580d60:8", "const:4:8"]]
+ 00580d60 ["CALLIND", null, ["register:0:8"]]
- 00580d20 bytes 20013fd6
+ 00580d60 bytes 20013fd6
- 00580d8c ["INT_ADD", "register:40f0:8", ["const:580d8c:8", "const:4:8"]]
- 00580d8c ["CALL", null, ["callee:00c580d0:8"]]
+ 00580dcc ["INT_ADD", "register:40f0:8", ["const:580dcc:8", "const:4:8"]]
+ 00580dcc ["CALL", null, ["callee:00c580d0:8"]]
- 00580d8c bytes 9d5c1b94
+ 00580dcc bytes c15c1b94
- 00580dec ["COPY", "register:0:8", ["register:4048:8"]]
- 00580dec ["INT_ADD", "register:40f0:8", ["const:580dec:8", "const:4:8"]]
- 00580dec ["CALLIND", null, ["register:0:8"]]
+ 00580e2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00580e2c ["INT_ADD", "register:40f0:8", ["const:580e2c:8", "const:4:8"]]
+ 00580e2c ["CALLIND", null, ["register:0:8"]]
- 00580dec bytes 20013fd6
+ 00580e2c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e59a45c046ca6cd8ed639265f646d66"></a>

### [`00581048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md) → [`00581088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581088.md) FUN_00581088

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec84.md) · 呼出先 12件 [`0059760c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059760c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0055ecc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc4.md) · 呼出先 12件 [`0059764c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059764c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581128",
      "incomplete_value": true,
      "site": "00581128",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a37:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005810e8",
      "incomplete_value": true,
      "site": "005810e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a93:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005810c4",
      "incomplete_value": false,
      "site": "005810d4",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581084",
      "incomplete_value": false,
      "site": "00581094",
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
            "const:5c8:8"
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
      "definition_site": "005810cc",
      "incomplete_value": false,
      "site": "005810d4",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058108c",
      "incomplete_value": false,
      "site": "00581094",
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
            "const:668:8"
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
      "005810c4",
      "PARAM",
      [
        "storage",
        "00c6c5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005810cc",
      "PARAM",
      [
        "storage",
        "00c6c668",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581108",
      "READ",
      [
        "storage",
        "002aea93",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005810c4",
      "PARAM",
      [
        "storage",
        "00c6c698",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005810cc",
      "PARAM",
      [
        "storage",
        "00c6c738",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581108",
      "READ",
      [
        "storage",
        "002aea37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-00581094) · [`00581084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-00581084) · [`0058108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581048.md#insn-0058108c)
- 新版 `005810d4`（命令位置の公開資料なし） · `005810c4`（命令位置の公開資料なし） · `005810cc`（命令位置の公開資料なし）

~~~diff
- 00581094 ["INT_ADD", "register:40f0:8", ["const:581094:8", "const:4:8"]]
- 00581094 ["CALL", null, ["callee:00c586e0:8"]]
+ 005810d4 ["INT_ADD", "register:40f0:8", ["const:5810d4:8", "const:4:8"]]
+ 005810d4 ["CALL", null, ["callee:00c586e0:8"]]
- 00581094 bytes 5f5d1b94
+ 005810d4 bytes 835d1b94
- 00581084 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00581084 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00581084 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00581084 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005810c4 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 005810c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005810c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005810c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00581084 bytes 21201791
+ 005810c4 bytes 21601a91
- 0058108c ["COPY", "tmp:0:8", ["const:668:8"]]
- 0058108c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0058108c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0058108c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005810cc ["COPY", "tmp:0:8", ["const:738:8"]]
+ 005810cc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005810cc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005810cc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0058108c bytes 42a01991
+ 005810cc bytes 42e01c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098ff8b08c3e124b4f48718166673cd2"></a>

### [`0058127c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md) → [`005812bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005812bc.md) FUN_005812bc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ec88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec88.md) · 呼出先 10件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0055ecc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc8.md) · 呼出先 10件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.99% / 新版 90.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581348",
      "incomplete_value": true,
      "site": "00581358",
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
                "const:ad3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581308",
      "incomplete_value": true,
      "site": "00581318",
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
                "const:b2f:8"
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
      "definition_site": "0058134c",
      "incomplete_value": true,
      "site": "0058135c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058130c",
      "incomplete_value": true,
      "site": "0058131c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581350",
      "incomplete_value": true,
      "site": "00581360",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581310",
      "incomplete_value": true,
      "site": "00581320",
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
                "const:2a0:8"
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
      "005812f8",
      "PARAM",
      [
        "storage",
        "00c6c5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581300",
      "PARAM",
      [
        "storage",
        "00c6c5d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581348",
      "READ",
      [
        "storage",
        "002afb2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005812f8",
      "PARAM",
      [
        "storage",
        "00c6c698",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581300",
      "PARAM",
      [
        "storage",
        "00c6c6a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00581348",
      "READ",
      [
        "storage",
        "002afad3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005812cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-005812cc) · [`00581360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-00581360) · [`005812b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/0058127c.md#insn-005812b8)
- 新版 `0058130c`（命令位置の公開資料なし） · `005813a0`（命令位置の公開資料なし） · `005812f8`（命令位置の公開資料なし）

~~~diff
- 005812cc ["INT_ADD", "register:40f0:8", ["const:5812cc:8", "const:4:8"]]
- 005812cc ["CALL", null, ["callee:00c586e0:8"]]
+ 0058130c ["INT_ADD", "register:40f0:8", ["const:58130c:8", "const:4:8"]]
+ 0058130c ["CALL", null, ["callee:00c586e0:8"]]
- 005812cc bytes d15c1b94
+ 0058130c bytes f55c1b94
- 00581360 ["INT_ADD", "register:40f0:8", ["const:581360:8", "const:4:8"]]
- 00581360 ["CALL", null, ["callee:00c57f80:8"]]
+ 005813a0 ["INT_ADD", "register:40f0:8", ["const:5813a0:8", "const:4:8"]]
+ 005813a0 ["CALL", null, ["callee:00c57f80:8"]]
- 00581360 bytes d45a1b94
+ 005813a0 bytes f85a1b94
- 005812b8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 005812b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005812b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005812b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005812f8 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 005812f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005812f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005812f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005812b8 bytes 21201791
+ 005812f8 bytes 21601a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea1e2460c0414d6cf69db0d66c7dfb5"></a>

### [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) → [`005814d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md) FUN_005814d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055ed08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ed08.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`0055ed48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ed48.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.97% / 新版 90.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581558",
      "incomplete_value": true,
      "site": "0058156c",
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
      "definition_site": "00581518",
      "incomplete_value": true,
      "site": "0058152c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581558",
      "incomplete_value": true,
      "site": "0058156c",
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
      "definition_site": "00581518",
      "incomplete_value": true,
      "site": "0058152c",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00581564",
      "incomplete_value": true,
      "site": "00581570",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581524",
      "incomplete_value": true,
      "site": "00581530",
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
                "const:40:8"
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
      "0058154c",
      "READ",
      [
        "storage",
        "002c2ed0",
        null,
        null
      ]
    ],
    [
      "00581558",
      "READ",
      [
        "storage",
        "002b7496",
        null,
        "string"
      ]
    ],
    [
      "00581558",
      "READ",
      [
        "storage",
        "002b74a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058154c",
      "READ",
      [
        "storage",
        "002c2f10",
        null,
        null
      ]
    ],
    [
      "00581558",
      "READ",
      [
        "storage",
        "002b74d6",
        null,
        "string"
      ]
    ],
    [
      "00581558",
      "READ",
      [
        "storage",
        "002b74e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005814fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-005814fc) · [`0058157c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-0058157c) · [`0058161c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md#insn-0058161c)
- 新版 `0058153c`（命令位置の公開資料なし） · `005815bc`（命令位置の公開資料なし） · `0058165c`（命令位置の公開資料なし）

~~~diff
- 005814fc ["INT_ADD", "register:40f0:8", ["const:5814fc:8", "const:4:8"]]
- 005814fc ["CALL", null, ["callee:00c57f60:8"]]
+ 0058153c ["INT_ADD", "register:40f0:8", ["const:58153c:8", "const:4:8"]]
+ 0058153c ["CALL", null, ["callee:00c57f60:8"]]
- 005814fc bytes 655a1b94
+ 0058153c bytes 895a1b94
- 0058157c ["INT_ADD", "register:40f0:8", ["const:58157c:8", "const:4:8"]]
- 0058157c ["CALL", null, ["callee:00589184:8"]]
+ 005815bc ["INT_ADD", "register:40f0:8", ["const:5815bc:8", "const:4:8"]]
+ 005815bc ["CALL", null, ["callee:00589184:8"]]
- 0058157c bytes f21e0094
+ 005815bc bytes f21e0094
- 0058161c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058161c ["INT_ADD", "register:40f0:8", ["const:58161c:8", "const:4:8"]]
- 0058161c ["CALLIND", null, ["register:0:8"]]
+ 0058165c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058165c ["INT_ADD", "register:40f0:8", ["const:58165c:8", "const:4:8"]]
+ 0058165c ["CALLIND", null, ["register:0:8"]]
- 0058161c bytes 00013fd6
+ 0058165c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace46f9030c5a57d138a747ab8a4556f"></a>

### [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) → [`005817a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md) FUN_005817a4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055f094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f094.md) [`0055f098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f098.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 2件 [`0055f0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d4.md) [`0055f0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f0d8.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058181c",
      "incomplete_value": true,
      "site": "00581830",
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005817dc",
      "incomplete_value": true,
      "site": "005817f0",
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
                "const:ed0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581960",
      "incomplete_value": false,
      "site": "0058196c",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581920",
      "incomplete_value": false,
      "site": "0058192c",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00581948",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00581908",
      "value": [
        "leaf",
        "ram:589f08:8"
      ]
    },
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058181c",
      "READ",
      [
        "storage",
        "002c2ed0",
        null,
        null
      ]
    ],
    [
      "00581828",
      "READ",
      [
        "storage",
        "002b7496",
        null,
        "string"
      ]
    ],
    [
      "00581828",
      "READ",
      [
        "storage",
        "002b74a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058181c",
      "READ",
      [
        "storage",
        "002c2f10",
        null,
        null
      ]
    ],
    [
      "00581828",
      "READ",
      [
        "storage",
        "002b74d6",
        null,
        "string"
      ]
    ],
    [
      "00581828",
      "READ",
      [
        "storage",
        "002b74e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005818ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-005818ec) · [`00581908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-00581908) · [`00581970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md#insn-00581970)
- 新版 `0058192c`（命令位置の公開資料なし） · `00581948`（命令位置の公開資料なし） · `005819b0`（命令位置の公開資料なし）

~~~diff
- 005818ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005818ec ["INT_ADD", "register:40f0:8", ["const:5818ec:8", "const:4:8"]]
- 005818ec ["CALLIND", null, ["register:0:8"]]
+ 0058192c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058192c ["INT_ADD", "register:40f0:8", ["const:58192c:8", "const:4:8"]]
+ 0058192c ["CALLIND", null, ["register:0:8"]]
- 005818ec bytes 00013fd6
+ 0058192c bytes 00013fd6
- 00581908 ["INT_ADD", "register:40f0:8", ["const:581908:8", "const:4:8"]]
- 00581908 ["CALL", null, ["ram:589f08:8"]]
+ 00581948 ["INT_ADD", "register:40f0:8", ["const:581948:8", "const:4:8"]]
+ 00581948 ["CALL", null, ["ram:589f48:8"]]
- 00581908 bytes 80210094
+ 00581948 bytes 80210094
- 00581970 ["INT_ADD", "register:40f0:8", ["const:581970:8", "const:4:8"]]
- 00581970 ["CALL", null, ["ram:589f08:8"]]
+ 005819b0 ["INT_ADD", "register:40f0:8", ["const:5819b0:8", "const:4:8"]]
+ 005819b0 ["CALL", null, ["ram:589f48:8"]]
- 00581970 bytes 66210094
+ 005819b0 bytes 66210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5869b9a416da850323a643a6ec4df74"></a>

### [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) → [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) FUN_00581a74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0055e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e750.md) [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md) · 呼出先 2件 [`005827b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`0055e790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e790.md) [`0055e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b0.md) [`0055e8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md) · 呼出先 2件 [`005827f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00581a9c",
      "incomplete_value": false,
      "site": "00581aa8",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581a5c",
      "incomplete_value": false,
      "site": "00581a68",
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
            "const:748:8"
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
      "00581aa8",
      "DATA",
      [
        "storage",
        "00c6c748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581aa8",
      "DATA",
      [
        "storage",
        "00c6c818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a50) · [`00581a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a5c) · [`00581a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md#insn-00581a74)
- 新版 `00581a90`（命令位置の公開資料なし） · `00581a9c`（命令位置の公開資料なし） · `00581ab4`（命令位置の公開資料なし）

~~~diff
- 00581a50 ["INT_ADD", "register:40f0:8", ["const:581a50:8", "const:4:8"]]
- 00581a50 ["CALL", null, ["callee:00c57f60:8"]]
+ 00581a90 ["INT_ADD", "register:40f0:8", ["const:581a90:8", "const:4:8"]]
+ 00581a90 ["CALL", null, ["callee:00c57f60:8"]]
- 00581a50 bytes 10591b94
+ 00581a90 bytes 34591b94
- 00581a5c ["COPY", "tmp:0:8", ["const:748:8"]]
- 00581a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581a9c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00581a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581a5c bytes 08211d91
+ 00581a9c bytes 08612091
- 00581a74 ["INT_ADD", "register:40f0:8", ["const:581a74:8", "const:4:8"]]
- 00581a74 ["CALL", null, ["callee:005827f8:8"]]
+ 00581ab4 ["INT_ADD", "register:40f0:8", ["const:581ab4:8", "const:4:8"]]
+ 00581ab4 ["CALL", null, ["callee:005827f8:8"]]
- 00581a74 bytes 51030094
+ 00581ab4 bytes 51030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8db8841831b8c796f052b0598280d47"></a>

### [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) → [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) FUN_00581ae8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md) [`0055eb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055eb1c.md) · 呼出先 2件 [`00582ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0055ea08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ea08.md) [`0055eb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055eb5c.md) · 呼出先 2件 [`00582d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00581b18",
      "incomplete_value": false,
      "site": "00581b24",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ad8",
      "incomplete_value": false,
      "site": "00581ae4",
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
            "const:7f0:8"
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
      "00581b24",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581b24",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581acc) · [`00581ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581ad8) · [`00581af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md#insn-00581af4)
- 新版 `00581b0c`（命令位置の公開資料なし） · `00581b18`（命令位置の公開資料なし） · `00581b34`（命令位置の公開資料なし）

~~~diff
- 00581acc ["INT_ADD", "register:40f0:8", ["const:581acc:8", "const:4:8"]]
- 00581acc ["CALL", null, ["callee:00c57f60:8"]]
+ 00581b0c ["INT_ADD", "register:40f0:8", ["const:581b0c:8", "const:4:8"]]
+ 00581b0c ["CALL", null, ["callee:00c57f60:8"]]
- 00581acc bytes f1581b94
+ 00581b0c bytes 15591b94
- 00581ad8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00581ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581b18 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00581b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581ad8 bytes 08c11f91
+ 00581b18 bytes 08012391
- 00581af4 ["INT_ADD", "register:40f0:8", ["const:581af4:8", "const:4:8"]]
- 00581af4 ["CALL", null, ["callee:00582d20:8"]]
+ 00581b34 ["INT_ADD", "register:40f0:8", ["const:581b34:8", "const:4:8"]]
+ 00581b34 ["CALL", null, ["callee:00582d20:8"]]
- 00581af4 bytes 7b040094
+ 00581b34 bytes 7b040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b63c29753c3e44560ca1da4ef2c02eb5"></a>

### [`00581dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581dd0.md) → [`00581e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e10.md) FUN_00581e10

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
      "definition_site": "00581e14",
      "incomplete_value": false,
      "site": "00581e18",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581dd4",
      "incomplete_value": false,
      "site": "00581dd8",
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
            "const:510:8"
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
      "00581e18",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00581e18",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581dd0.md#insn-00581dd4)
- 新版 `00581e14`（命令位置の公開資料なし）

~~~diff
- 00581dd4 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00581dd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581dd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581dd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e14 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00581e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581dd4 bytes 08411491
+ 00581e14 bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df83ec32e8d0c26d77b4da517f0edf18"></a>

### [`00581e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e20.md) → [`00581e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e60.md) FUN_00581e60

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
      "definition_site": "00581e64",
      "incomplete_value": false,
      "site": "00581e68",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e24",
      "incomplete_value": false,
      "site": "00581e28",
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
            "const:560:8"
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
      "00581e68",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581e68",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e20.md#insn-00581e24)
- 新版 `00581e64`（命令位置の公開資料なし）

~~~diff
- 00581e24 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00581e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e64 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00581e64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e24 bytes 08811591
+ 00581e64 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ef11deeb5cdb77c9895775ad54c65a"></a>

### [`00581e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md) → [`00581e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e70.md) FUN_00581e70

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
      "definition_site": "00581e80",
      "incomplete_value": false,
      "site": "00581e88",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581e40",
      "incomplete_value": false,
      "site": "00581e48",
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
            "const:560:8"
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
      "00581e88",
      "DATA",
      [
        "storage",
        "00c6c560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581e88",
      "DATA",
      [
        "storage",
        "00c6c630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md#insn-00581e40) · [`00581e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e30.md#insn-00581e4c)
- 新版 `00581e80`（命令位置の公開資料なし） · `00581e8c`（命令位置の公開資料なし）

~~~diff
- 00581e40 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00581e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581e80 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00581e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581e40 bytes 08811591
+ 00581e80 bytes 08c11891
- 00581e4c ["INT_ADD", "register:40f0:8", ["const:581e4c:8", "const:4:8"]]
- 00581e4c ["CALL", null, ["callee:00c57f70:8"]]
+ 00581e8c ["INT_ADD", "register:40f0:8", ["const:581e8c:8", "const:4:8"]]
+ 00581e8c ["CALL", null, ["callee:00c57f70:8"]]
- 00581e4c bytes 15581b94
+ 00581e8c bytes 39581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d5573b03186f0838793d4424fb60ffc"></a>

### [`00581ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ec0.md) → [`00581f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f00.md) FUN_00581f00

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
      "definition_site": "00581f04",
      "incomplete_value": false,
      "site": "00581f08",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ec4",
      "incomplete_value": false,
      "site": "00581ec8",
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
            "const:600:8"
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
      "00581f08",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581f08",
      "DATA",
      [
        "storage",
        "00c6c6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ec0.md#insn-00581ec4)
- 新版 `00581f04`（命令位置の公開資料なし）

~~~diff
- 00581ec4 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00581ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581f04 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00581f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581ec4 bytes 08011891
+ 00581f04 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83cb5f690423b1b3525c369cb4bb9d22"></a>

### [`00581ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md) → [`00581f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581f10.md) FUN_00581f10

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
      "definition_site": "00581f20",
      "incomplete_value": false,
      "site": "00581f28",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ee0",
      "incomplete_value": false,
      "site": "00581ee8",
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
            "const:600:8"
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
      "00581f28",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581f28",
      "DATA",
      [
        "storage",
        "00c6c6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md#insn-00581ee0) · [`00581eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581ed0.md#insn-00581eec)
- 新版 `00581f20`（命令位置の公開資料なし） · `00581f2c`（命令位置の公開資料なし）

~~~diff
- 00581ee0 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00581ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581f20 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00581f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581ee0 bytes 08011891
+ 00581f20 bytes 08411b91
- 00581eec ["INT_ADD", "register:40f0:8", ["const:581eec:8", "const:4:8"]]
- 00581eec ["CALL", null, ["callee:00c57f70:8"]]
+ 00581f2c ["INT_ADD", "register:40f0:8", ["const:581f2c:8", "const:4:8"]]
+ 00581f2c ["CALL", null, ["callee:00c57f70:8"]]
- 00581eec bytes ed571b94
+ 00581f2c bytes 11581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97e991cb0bccaf5ee34cea74b2aca873"></a>

### [`00581f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f6c.md) → [`00581fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fac.md) FUN_00581fac

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
      "definition_site": "00581fb0",
      "incomplete_value": false,
      "site": "00581fb4",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f70",
      "incomplete_value": false,
      "site": "00581f74",
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
            "const:690:8"
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
      "00581fb4",
      "DATA",
      [
        "storage",
        "00c6c690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581fb4",
      "DATA",
      [
        "storage",
        "00c6c760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f6c.md#insn-00581f70)
- 新版 `00581fb0`（命令位置の公開資料なし）

~~~diff
- 00581f70 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00581f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581fb0 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00581fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f70 bytes 08411a91
+ 00581fb0 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337cb63a029807b01ea15421f882bae9"></a>

### [`00581f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md) → [`00581fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581fbc.md) FUN_00581fbc

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
      "definition_site": "00581fcc",
      "incomplete_value": false,
      "site": "00581fd4",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581f8c",
      "incomplete_value": false,
      "site": "00581f94",
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
            "const:690:8"
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
      "00581fd4",
      "DATA",
      [
        "storage",
        "00c6c690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00581fd4",
      "DATA",
      [
        "storage",
        "00c6c760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00581f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md#insn-00581f8c) · [`00581f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581f7c.md#insn-00581f98)
- 新版 `00581fcc`（命令位置の公開資料なし） · `00581fd8`（命令位置の公開資料なし）

~~~diff
- 00581f8c ["COPY", "tmp:0:8", ["const:690:8"]]
- 00581f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00581f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00581f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00581fcc ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00581fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00581fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00581fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00581f8c bytes 08411a91
+ 00581fcc bytes 08811d91
- 00581f98 ["INT_ADD", "register:40f0:8", ["const:581f98:8", "const:4:8"]]
- 00581f98 ["CALL", null, ["callee:00c57f70:8"]]
+ 00581fd8 ["INT_ADD", "register:40f0:8", ["const:581fd8:8", "const:4:8"]]
+ 00581fd8 ["CALL", null, ["callee:00c57f70:8"]]
- 00581f98 bytes c2571b94
+ 00581fd8 bytes e6571b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42b1561013d8be95bc605934f5f6fe92"></a>

### [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) → [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) FUN_00581ffc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00581494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581494.md) [`00581764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581764.md) · 呼出先 5件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`005814d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005814d4.md) [`005817a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/005817a4.md) · 呼出先 5件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.63% / 新版 81.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582038",
      "incomplete_value": false,
      "site": "00582038",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00581ff8",
      "incomplete_value": false,
      "site": "00581ff8",
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
            "const:6e0:8"
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
      "definition_site": "0058207c",
      "incomplete_value": true,
      "site": "00582084",
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
    "old": {
      "definition_site": "0058203c",
      "incomplete_value": true,
      "site": "00582044",
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
                "const:f70:8"
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
      "definition_site": "00582078",
      "incomplete_value": true,
      "site": "00582088",
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
                "const:f65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582038",
      "incomplete_value": true,
      "site": "00582048",
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
                "const:f34:8"
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
      "00582038",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582078",
      "READ",
      [
        "storage",
        "002b4f34",
        null,
        "string"
      ]
    ],
    [
      "00582078",
      "READ",
      [
        "storage",
        "002b4f44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582038",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00582078",
      "READ",
      [
        "storage",
        "002b4f65",
        null,
        "string"
      ]
    ],
    [
      "00582078",
      "READ",
      [
        "storage",
        "002b4f75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00582118) · [`00581fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00581fd8) · [`00582000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md#insn-00582000)
- 新版 `00582158`（命令位置の公開資料なし） · `00582018`（命令位置の公開資料なし） · `00582040`（命令位置の公開資料なし）

~~~diff
- 00582118 ["INT_ADD", "register:40f0:8", ["const:582118:8", "const:4:8"]]
- 00582118 ["CALL", null, ["callee:00c57f80:8"]]
+ 00582158 ["INT_ADD", "register:40f0:8", ["const:582158:8", "const:4:8"]]
+ 00582158 ["CALL", null, ["callee:00c57f80:8"]]
- 00582118 bytes 66571b94
+ 00582158 bytes 8a571b94
- 00581fd8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00581fd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00581fd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00581fd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582018 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00582018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00581fd8 bytes 29811b91
+ 00582018 bytes 29c11e91
- 00582000 ["INT_ADD", "register:40f0:8", ["const:582000:8", "const:4:8"]]
- 00582000 ["CALL", null, ["callee:005897d0:8"]]
+ 00582040 ["INT_ADD", "register:40f0:8", ["const:582040:8", "const:4:8"]]
+ 00582040 ["CALL", null, ["callee:005897d0:8"]]
- 00582000 bytes e41d0094
+ 00582040 bytes e41d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6577fa562fb3dc790ef761df6903c997"></a>

### [`00582198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582198.md) → [`005821d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821d8.md) FUN_005821d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)

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
      "definition_site": "005821e0",
      "incomplete_value": false,
      "site": "005821e0",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005821a0",
      "incomplete_value": false,
      "site": "005821a0",
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
            "const:6e0:8"
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
      "005821e0",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005821e0",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058219c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582198.md#insn-0058219c)
- 新版 `005821dc`（命令位置の公開資料なし）

~~~diff
- 0058219c ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0058219c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058219c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058219c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821dc ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 005821dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058219c bytes 08811b91
+ 005821dc bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b1a613e66eb0c538e16ecaae0499ce1"></a>

### [`005821a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md) → [`005821e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005821e8.md) FUN_005821e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00582200",
      "incomplete_value": false,
      "site": "00582200",
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
            "const:7b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005821c0",
      "incomplete_value": false,
      "site": "005821c0",
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
            "const:6e0:8"
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
      "00582200",
      "DATA",
      [
        "storage",
        "00c6c6e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582200",
      "DATA",
      [
        "storage",
        "00c6c7b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005821b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md#insn-005821b8) · [`005821c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821a8.md#insn-005821c4)
- 新版 `005821f8`（命令位置の公開資料なし） · `00582204`（命令位置の公開資料なし）

~~~diff
- 005821b8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 005821b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005821b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005821b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005821f8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 005821f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005821f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005821f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005821b8 bytes 08811b91
+ 005821f8 bytes 08c11e91
- 005821c4 ["INT_ADD", "register:40f0:8", ["const:5821c4:8", "const:4:8"]]
- 005821c4 ["CALL", null, ["callee:0058a8fc:8"]]
+ 00582204 ["INT_ADD", "register:40f0:8", ["const:582204:8", "const:4:8"]]
+ 00582204 ["CALL", null, ["callee:0058a8fc:8"]]
- 005821c4 bytes be210094
+ 00582204 bytes be210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc68705b800798bef6dd65ef6616e41"></a>

### [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) → [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) FUN_00582218

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005822f4",
      "incomplete_value": false,
      "site": "00582300",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005822b4",
      "incomplete_value": false,
      "site": "005822c0",
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
            "const:510:8"
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
      "site": "00582330",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005822f0",
      "value": [
        "leaf",
        "ram:589f08:8"
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
      "00582300",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ],
    [
      "00582330",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f08"
      ]
    ]
  ],
  "added": [
    [
      "00582300",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00582330",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005822f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-005822f0) · [`00582208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-00582208) · [`00582220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md#insn-00582220)
- 新版 `00582330`（命令位置の公開資料なし） · `00582248`（命令位置の公開資料なし） · `00582260`（命令位置の公開資料なし）

~~~diff
- 005822f0 ["INT_ADD", "register:40f0:8", ["const:5822f0:8", "const:4:8"]]
- 005822f0 ["CALL", null, ["ram:589f08:8"]]
+ 00582330 ["INT_ADD", "register:40f0:8", ["const:582330:8", "const:4:8"]]
+ 00582330 ["CALL", null, ["ram:589f48:8"]]
- 005822f0 bytes 061f0094
+ 00582330 bytes 061f0094
- 00582208 ["INT_ADD", "register:40f0:8", ["const:582208:8", "const:4:8"]]
- 00582208 ["CALL", null, ["callee:00588eac:8"]]
+ 00582248 ["INT_ADD", "register:40f0:8", ["const:582248:8", "const:4:8"]]
+ 00582248 ["CALL", null, ["callee:00588eac:8"]]
- 00582208 bytes 191b0094
+ 00582248 bytes 191b0094
- 00582220 ["INT_ADD", "register:40f0:8", ["const:582220:8", "const:4:8"]]
- 00582220 ["CALL", null, ["callee:00589d08:8"]]
+ 00582260 ["INT_ADD", "register:40f0:8", ["const:582260:8", "const:4:8"]]
+ 00582260 ["CALL", null, ["callee:00589d08:8"]]
- 00582220 bytes aa1e0094
+ 00582260 bytes aa1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a79501cd45287de6c3a625a27181c0e"></a>

### [`00582360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md) → [`005823a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md) FUN_005823a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589d70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589db0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582484",
      "incomplete_value": false,
      "site": "00582490",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582444",
      "incomplete_value": false,
      "site": "00582450",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005824c0",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582480",
      "value": [
        "leaf",
        "ram:589f08:8"
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
      "00582490",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ],
    [
      "005824c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f08"
      ]
    ]
  ],
  "added": [
    [
      "00582490",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005824c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-00582480) · [`00582394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-00582394) · [`005823ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md#insn-005823ac)
- 新版 `005824c0`（命令位置の公開資料なし） · `005823d4`（命令位置の公開資料なし） · `005823ec`（命令位置の公開資料なし）

~~~diff
- 00582480 ["INT_ADD", "register:40f0:8", ["const:582480:8", "const:4:8"]]
- 00582480 ["CALL", null, ["ram:589f08:8"]]
+ 005824c0 ["INT_ADD", "register:40f0:8", ["const:5824c0:8", "const:4:8"]]
+ 005824c0 ["CALL", null, ["ram:589f48:8"]]
- 00582480 bytes a21e0094
+ 005824c0 bytes a21e0094
- 00582394 ["INT_ADD", "register:40f0:8", ["const:582394:8", "const:4:8"]]
- 00582394 ["CALL", null, ["callee:00588eac:8"]]
+ 005823d4 ["INT_ADD", "register:40f0:8", ["const:5823d4:8", "const:4:8"]]
+ 005823d4 ["CALL", null, ["callee:00588eac:8"]]
- 00582394 bytes b61a0094
+ 005823d4 bytes b61a0094
- 005823ac ["INT_ADD", "register:40f0:8", ["const:5823ac:8", "const:4:8"]]
- 005823ac ["CALL", null, ["callee:00589db0:8"]]
+ 005823ec ["INT_ADD", "register:40f0:8", ["const:5823ec:8", "const:4:8"]]
+ 005823ec ["CALL", null, ["callee:00589db0:8"]]
- 005823ac bytes 711e0094
+ 005823ec bytes 711e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acffb17b43a6358ea87dd2595ce2603f"></a>

### [`005824f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md) → [`00582534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md) FUN_00582534

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00589d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589d70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00589db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589db0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582604",
      "incomplete_value": false,
      "site": "00582610",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005825c4",
      "incomplete_value": false,
      "site": "005825d0",
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
            "const:510:8"
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
      "site": "00582640",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00582600",
      "value": [
        "leaf",
        "ram:589f08:8"
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
      "00582610",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ],
    [
      "00582640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f08"
      ]
    ]
  ],
  "added": [
    [
      "00582610",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ],
    [
      "00582640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582600) · [`00582528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582528) · [`00582540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md#insn-00582540)
- 新版 `00582640`（命令位置の公開資料なし） · `00582568`（命令位置の公開資料なし） · `00582580`（命令位置の公開資料なし）

~~~diff
- 00582600 ["INT_ADD", "register:40f0:8", ["const:582600:8", "const:4:8"]]
- 00582600 ["CALL", null, ["ram:589f08:8"]]
+ 00582640 ["INT_ADD", "register:40f0:8", ["const:582640:8", "const:4:8"]]
+ 00582640 ["CALL", null, ["ram:589f48:8"]]
- 00582600 bytes 421e0094
+ 00582640 bytes 421e0094
- 00582528 ["INT_ADD", "register:40f0:8", ["const:582528:8", "const:4:8"]]
- 00582528 ["CALL", null, ["callee:00588eac:8"]]
+ 00582568 ["INT_ADD", "register:40f0:8", ["const:582568:8", "const:4:8"]]
+ 00582568 ["CALL", null, ["callee:00588eac:8"]]
- 00582528 bytes 511a0094
+ 00582568 bytes 511a0094
- 00582540 ["INT_ADD", "register:40f0:8", ["const:582540:8", "const:4:8"]]
- 00582540 ["CALL", null, ["callee:00589db0:8"]]
+ 00582580 ["INT_ADD", "register:40f0:8", ["const:582580:8", "const:4:8"]]
+ 00582580 ["CALL", null, ["callee:00589db0:8"]]
- 00582540 bytes 0c1e0094
+ 00582580 bytes 0c1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25b85304f74d71e7db4186550ea0222"></a>

### [`00582670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md) → [`005826b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md) FUN_005826b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589858.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589898.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582740",
      "incomplete_value": false,
      "site": "0058274c",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582700",
      "incomplete_value": false,
      "site": "0058270c",
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
            "const:510:8"
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
      "0058274c",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058274c",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058268c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md#insn-0058268c) · [`00582698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md#insn-00582698) · [`005826ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md#insn-005826ac)
- 新版 `005826cc`（命令位置の公開資料なし） · `005826d8`（命令位置の公開資料なし） · `005826ec`（命令位置の公開資料なし）

~~~diff
- 0058268c ["INT_ADD", "register:40f0:8", ["const:58268c:8", "const:4:8"]]
- 0058268c ["CALL", null, ["callee:00588eac:8"]]
+ 005826cc ["INT_ADD", "register:40f0:8", ["const:5826cc:8", "const:4:8"]]
+ 005826cc ["CALL", null, ["callee:00588eac:8"]]
- 0058268c bytes f8190094
+ 005826cc bytes f8190094
- 00582698 ["INT_ADD", "register:40f0:8", ["const:582698:8", "const:4:8"]]
- 00582698 ["CALL", null, ["callee:00589898:8"]]
+ 005826d8 ["INT_ADD", "register:40f0:8", ["const:5826d8:8", "const:4:8"]]
+ 005826d8 ["CALL", null, ["callee:00589898:8"]]
- 00582698 bytes 701c0094
+ 005826d8 bytes 701c0094
- 005826ac ["INT_ADD", "register:40f0:8", ["const:5826ac:8", "const:4:8"]]
- 005826ac ["CALL", null, ["callee:00497874:8"]]
+ 005826ec ["INT_ADD", "register:40f0:8", ["const:5826ec:8", "const:4:8"]]
+ 005826ec ["CALL", null, ["callee:00497874:8"]]
- 005826ac bytes 6254fc97
+ 005826ec bytes 6254fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a1f79ad94afb7fef59ef150e46f865"></a>

### [`00582778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582778.md) → [`005827b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827b8.md) FUN_005827b8

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
      "definition_site": "005827c8",
      "incomplete_value": false,
      "site": "005827d0",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582788",
      "incomplete_value": false,
      "site": "00582790",
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
            "const:748:8"
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
      "005827d0",
      "DATA",
      [
        "storage",
        "00c6c748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005827d0",
      "DATA",
      [
        "storage",
        "00c6c818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582778.md#insn-00582788) · [`00582794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582778.md#insn-00582794)
- 新版 `005827c8`（命令位置の公開資料なし） · `005827d4`（命令位置の公開資料なし）

~~~diff
- 00582788 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00582788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005827c8 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 005827c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005827c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005827c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582788 bytes 08211d91
+ 005827c8 bytes 08612091
- 00582794 ["INT_ADD", "register:40f0:8", ["const:582794:8", "const:4:8"]]
- 00582794 ["CALL", null, ["callee:00c57f70:8"]]
+ 005827d4 ["INT_ADD", "register:40f0:8", ["const:5827d4:8", "const:4:8"]]
+ 005827d4 ["CALL", null, ["callee:00c57f70:8"]]
- 00582794 bytes c3551b94
+ 005827d4 bytes e7551b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6407381182adf8368120369315fa7df6"></a>

### [`005827b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md) → [`005827f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005827f8.md) FUN_005827f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00581a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581a34.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)
- 新版 呼出元 1件 [`00581a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581a74.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00582828",
      "incomplete_value": false,
      "site": "00582828",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005827e8",
      "incomplete_value": false,
      "site": "005827e8",
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
            "const:798:8"
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
      "00582828",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ],
    [
      "00582850",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00582828",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ],
    [
      "00582850",
      "DATA",
      [
        "storage",
        "0035444d",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005827d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md#insn-005827d8) · [`00582820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md#insn-00582820) · [`00582854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005827b8.md#insn-00582854)
- 新版 `00582818`（命令位置の公開資料なし） · `00582860`（命令位置の公開資料なし） · `00582894`（命令位置の公開資料なし）

~~~diff
- 005827d8 ["COPY", "tmp:0:8", ["const:798:8"]]
- 005827d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005827d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005827d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582818 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00582818 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582818 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582818 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005827d8 bytes 29611e91
+ 00582818 bytes 29a12191
- 00582820 ["INT_ADD", "register:40f0:8", ["const:582820:8", "const:4:8"]]
- 00582820 ["CALL", null, ["callee:00c58ec0:8"]]
+ 00582860 ["INT_ADD", "register:40f0:8", ["const:582860:8", "const:4:8"]]
+ 00582860 ["CALL", null, ["callee:00c58ec0:8"]]
- 00582820 bytes 74591b94
+ 00582860 bytes 98591b94
- 00582854 ["INT_ADD", "register:40f0:8", ["const:582854:8", "const:4:8"]]
- 00582854 ["CALL", null, ["callee:00c58ec0:8"]]
+ 00582894 ["INT_ADD", "register:40f0:8", ["const:582894:8", "const:4:8"]]
+ 00582894 ["CALL", null, ["callee:00c58ec0:8"]]
- 00582854 bytes 67591b94
+ 00582894 bytes 8b591b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bb017ecc9010a09d2e9631b4942c93a"></a>

### [`00582970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582970.md) → [`005829b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829b0.md) FUN_005829b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005829c0",
      "incomplete_value": false,
      "site": "005829c0",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582980",
      "incomplete_value": false,
      "site": "00582980",
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
            "const:798:8"
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
      "005829c0",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005829c0",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058297c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582970.md#insn-0058297c)
- 新版 `005829bc`（命令位置の公開資料なし）

~~~diff
- 0058297c ["COPY", "tmp:0:8", ["const:798:8"]]
- 0058297c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058297c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058297c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005829bc ["COPY", "tmp:0:8", ["const:868:8"]]
+ 005829bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005829bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005829bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058297c bytes 29611e91
+ 005829bc bytes 29a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b0ae4bffa8e75cdce5797ff979eaa2"></a>

### [`00582998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582998.md) → [`005829d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005829d8.md) FUN_005829d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005829e4",
      "incomplete_value": false,
      "site": "005829e4",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005829a4",
      "incomplete_value": false,
      "site": "005829a4",
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
            "const:798:8"
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
      "005829e4",
      "DATA",
      [
        "storage",
        "00c6c798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005829e4",
      "DATA",
      [
        "storage",
        "00c6c868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005829a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582998.md#insn-005829a0) · [`005829c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582998.md#insn-005829c8)
- 新版 `005829e0`（命令位置の公開資料なし） · `00582a08`（命令位置の公開資料なし）

~~~diff
- 005829a0 ["COPY", "tmp:0:8", ["const:798:8"]]
- 005829a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005829a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005829a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005829e0 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 005829e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005829e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005829e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005829a0 bytes 29611e91
+ 005829e0 bytes 29a12191
- 005829c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005829c8 ["INT_ADD", "register:40f0:8", ["const:5829c8:8", "const:4:8"]]
- 005829c8 ["CALLIND", null, ["register:0:8"]]
+ 00582a08 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00582a08 ["INT_ADD", "register:40f0:8", ["const:582a08:8", "const:4:8"]]
+ 00582a08 ["CALLIND", null, ["register:0:8"]]
- 005829c8 bytes 20013fd6
+ 00582a08 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3cfa46740ece1235038fd3b5c603b94"></a>

### [`00582c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582c90.md) → [`00582cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582cd0.md) FUN_00582cd0

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
      "definition_site": "00582cd4",
      "incomplete_value": false,
      "site": "00582cd8",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582c94",
      "incomplete_value": false,
      "site": "00582c98",
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
            "const:7f0:8"
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
      "00582cd8",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582cd8",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582c90.md#insn-00582c94)
- 新版 `00582cd4`（命令位置の公開資料なし）

~~~diff
- 00582c94 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00582c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582cd4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00582cd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582c94 bytes 08c11f91
+ 00582cd4 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

