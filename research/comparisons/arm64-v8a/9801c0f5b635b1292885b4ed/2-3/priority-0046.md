# v16.0.1 → v16.0.2 · 最優先の変更候補 (46)

[一覧の目次](README.md)

<a id="compare-63496e0b773b43280f457757f0afa231"></a>

### [`0086ff08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086ff08.md) → [`0086ff60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086ff60.md) FUN_0086ff60

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0086fedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086fedc.md) [`00870240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870240.md) · 呼出先 7件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00a86810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a86/00a86810.md)
- 新版 呼出元 2件 [`0086ff34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086ff34.md) [`00870298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870298.md) · 呼出先 7件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md) [`005509fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509fc.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00a86880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a86/00a86880.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086ff9c",
      "incomplete_value": true,
      "site": "0086ffb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ff44",
      "incomplete_value": true,
      "site": "0086ff5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:875:8"
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
      "definition_site": "0086ff9c",
      "incomplete_value": true,
      "site": "0086ffb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ff44",
      "incomplete_value": true,
      "site": "0086ff60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:875:8"
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
      "definition_site": "00870010",
      "incomplete_value": true,
      "site": "00870020",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:92f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086ffb8",
      "incomplete_value": true,
      "site": "0086ffc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:983:8"
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
      "0086ff78",
      "PARAM",
      [
        "storage",
        "00cb4578",
        null,
        null
      ]
    ],
    [
      "0086ff9c",
      "READ",
      [
        "storage",
        "002b7875",
        null,
        "string"
      ]
    ],
    [
      "00870010",
      "READ",
      [
        "storage",
        "002bb983",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0086ff78",
      "PARAM",
      [
        "storage",
        "00cb4678",
        null,
        null
      ]
    ],
    [
      "0086ff9c",
      "READ",
      [
        "storage",
        "002b78b5",
        null,
        "string"
      ]
    ],
    [
      "00870010",
      "READ",
      [
        "storage",
        "002bb92f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086ff2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086ff08.md#insn-0086ff2c) · [`0086ff20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086ff08.md#insn-0086ff20) · [`0086ff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086ff08.md#insn-0086ff3c)
- 新版 `0086ff84`（命令位置の公開資料なし） · `0086ff78`（命令位置の公開資料なし） · `0086ff94`（命令位置の公開資料なし）

~~~diff
- 0086ff2c ["INT_ADD", "register:40f0:8", ["const:86ff2c:8", "const:4:8"]]
- 0086ff2c ["CALL", null, ["callee:00a86880:8"]]
+ 0086ff84 ["INT_ADD", "register:40f0:8", ["const:86ff84:8", "const:4:8"]]
+ 0086ff84 ["CALL", null, ["callee:00a86880:8"]]
- 0086ff2c bytes 395a0894
+ 0086ff84 bytes 3f5a0894
- 0086ff20 ["COPY", "tmp:0:8", ["const:578:8"]]
- 0086ff20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0086ff20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0086ff20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0086ff78 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 0086ff78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0086ff78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0086ff78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0086ff20 bytes 00e01591
+ 0086ff78 bytes 00e01991
- 0086ff3c ["COPY", "tmp:0:8", ["const:875:8"]]
- 0086ff3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0086ff3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0086ff3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0086ff94 ["COPY", "tmp:0:8", ["const:8b5:8"]]
+ 0086ff94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ff94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0086ff94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0086ff3c bytes 29d52191
+ 0086ff94 bytes 29d52291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cdcc7de7c3820194e7a865870ec246f"></a>

### [`008701e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008701e8.md) → [`00870240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870240.md) FUN_00870240

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00870260",
      "incomplete_value": false,
      "site": "00870264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870208",
      "incomplete_value": false,
      "site": "0087020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "00870264",
      "DATA",
      [
        "storage",
        "00c7f7c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870264",
      "DATA",
      [
        "storage",
        "00c7f890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008701fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008701e8.md#insn-008701fc) · [`00870208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008701e8.md#insn-00870208)
- 新版 `00870254`（命令位置の公開資料なし） · `00870260`（命令位置の公開資料なし）

~~~diff
- 008701fc ["INT_ADD", "register:40f0:8", ["const:8701fc:8", "const:4:8"]]
- 008701fc ["CALL", null, ["callee:00c57f60:8"]]
+ 00870254 ["INT_ADD", "register:40f0:8", ["const:870254:8", "const:4:8"]]
+ 00870254 ["CALL", null, ["callee:00c57f60:8"]]
- 008701fc bytes 259f0f94
+ 00870254 bytes 439f0f94
- 00870208 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00870208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870260 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00870260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870208 bytes 08011f91
+ 00870260 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11e4d7a1b9fa12bd7072fbf5da21d7c9"></a>

### [`00870220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870220.md) → [`00870278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870278.md) FUN_00870278

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0087027c",
      "incomplete_value": false,
      "site": "00870280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870224",
      "incomplete_value": false,
      "site": "00870228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "00870280",
      "DATA",
      [
        "storage",
        "00c7f7c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870280",
      "DATA",
      [
        "storage",
        "00c7f890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870220.md#insn-00870224)
- 新版 `0087027c`（命令位置の公開資料なし）

~~~diff
- 00870224 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00870224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087027c ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0087027c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087027c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087027c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870224 bytes 08011f91
+ 0087027c bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a90b6b8e6c72a73961bf1b48dedf842"></a>

### [`00870270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870270.md) → [`008702c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/008702c8.md) FUN_008702c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "008702e8",
      "incomplete_value": false,
      "site": "008702ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870290",
      "incomplete_value": false,
      "site": "00870294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "008702ec",
      "DATA",
      [
        "storage",
        "00c7f840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008702ec",
      "DATA",
      [
        "storage",
        "00c7f910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870270.md#insn-00870284) · [`00870290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870270.md#insn-00870290)
- 新版 `008702dc`（命令位置の公開資料なし） · `008702e8`（命令位置の公開資料なし）

~~~diff
- 00870284 ["INT_ADD", "register:40f0:8", ["const:870284:8", "const:4:8"]]
- 00870284 ["CALL", null, ["callee:00c57f60:8"]]
+ 008702dc ["INT_ADD", "register:40f0:8", ["const:8702dc:8", "const:4:8"]]
+ 008702dc ["CALL", null, ["callee:00c57f60:8"]]
- 00870284 bytes 039f0f94
+ 008702dc bytes 219f0f94
- 00870290 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00870290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008702e8 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 008702e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008702e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008702e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870290 bytes 08012191
+ 008702e8 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c44bfbfd515a447f71a59ba42fe6083c"></a>

### [`008702a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702a8.md) → [`00870300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870300.md) FUN_00870300

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00870304",
      "incomplete_value": false,
      "site": "00870308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008702ac",
      "incomplete_value": false,
      "site": "008702b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "00870308",
      "DATA",
      [
        "storage",
        "00c7f840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870308",
      "DATA",
      [
        "storage",
        "00c7f910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008702ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702a8.md#insn-008702ac)
- 新版 `00870304`（命令位置の公開資料なし）

~~~diff
- 008702ac ["COPY", "tmp:0:8", ["const:840:8"]]
- 008702ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008702ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008702ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870304 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00870304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008702ac bytes 08012191
+ 00870304 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3df6f46811b515ebffd59a48606aea"></a>

### [`008702f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702f4.md) → [`0087034c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/0087034c.md) FUN_0087034c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008702c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702c8.md) [`00870c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c7c.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md)
- 新版 呼出元 2件 [`00870320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870320.md) [`00870cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870cd4.md) · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`005509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.43% / 新版 93.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00870394",
      "incomplete_value": true,
      "site": "00870394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087033c",
      "incomplete_value": true,
      "site": "0087033c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec9:8"
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
      "definition_site": "00870398",
      "incomplete_value": true,
      "site": "00870398",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00870340",
      "incomplete_value": true,
      "site": "00870340",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008703f0",
      "incomplete_value": true,
      "site": "008703fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:502:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870398",
      "incomplete_value": true,
      "site": "008703a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54f:8"
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
      "0087037c",
      "READ",
      [
        "storage",
        "002aeec9",
        null,
        "string"
      ]
    ],
    [
      "00870380",
      "READ",
      [
        "storage",
        "002aeed0",
        null,
        "string"
      ]
    ],
    [
      "008703f0",
      "READ",
      [
        "storage",
        "0029f54f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087037c",
      "READ",
      [
        "storage",
        "002aee6d",
        null,
        "string"
      ]
    ],
    [
      "00870380",
      "READ",
      [
        "storage",
        "002aee74",
        null,
        "string"
      ]
    ],
    [
      "008703f0",
      "READ",
      [
        "storage",
        "0029f502",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087034c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702f4.md#insn-0087034c) · [`00870440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702f4.md#insn-00870440) · [`0087047c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/008702f4.md#insn-0087047c)
- 新版 `008703a4`（命令位置の公開資料なし） · `00870498`（命令位置の公開資料なし） · `008704d4`（命令位置の公開資料なし）

~~~diff
- 0087034c ["INT_ADD", "register:40f0:8", ["const:87034c:8", "const:4:8"]]
- 0087034c ["CALL", null, ["callee:005509f0:8"]]
+ 008703a4 ["INT_ADD", "register:40f0:8", ["const:8703a4:8", "const:4:8"]]
+ 008703a4 ["CALL", null, ["callee:005509f0:8"]]
- 0087034c bytes 9981f397
+ 008703a4 bytes 9381f397
- 00870440 ["COPY", "tmp:0:8", ["const:212:8"]]
- 00870440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00870440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00870440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00870498 ["COPY", "tmp:0:8", ["const:243:8"]]
+ 00870498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00870498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00870498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00870440 bytes 29490891
+ 00870498 bytes 290d0991
- 0087047c ["COPY", "tmp:0:8", ["const:6d1:8"]]
- 0087047c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087047c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087047c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008704d4 ["COPY", "tmp:0:8", ["const:67d:8"]]
+ 008704d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008704d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008704d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087047c bytes 29451b91
+ 008704d4 bytes 29f51991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eee9074de1c317302a440a44ed1f444"></a>

### [`00870c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c24.md) → [`00870c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870c7c.md) FUN_00870c7c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00870c9c",
      "incomplete_value": false,
      "site": "00870ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870c44",
      "incomplete_value": false,
      "site": "00870c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00870ca0",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870ca0",
      "DATA",
      [
        "storage",
        "00c7f990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c24.md#insn-00870c38) · [`00870c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c24.md#insn-00870c44)
- 新版 `00870c90`（命令位置の公開資料なし） · `00870c9c`（命令位置の公開資料なし）

~~~diff
- 00870c38 ["INT_ADD", "register:40f0:8", ["const:870c38:8", "const:4:8"]]
- 00870c38 ["CALL", null, ["callee:00c57f60:8"]]
+ 00870c90 ["INT_ADD", "register:40f0:8", ["const:870c90:8", "const:4:8"]]
+ 00870c90 ["CALL", null, ["callee:00c57f60:8"]]
- 00870c38 bytes 969c0f94
+ 00870c90 bytes b49c0f94
- 00870c44 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00870c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870c9c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00870c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870c44 bytes 08012391
+ 00870c9c bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2da157b64ccce3dc24d8aeb7467f8c2"></a>

### [`00870c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c5c.md) → [`00870cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870cb4.md) FUN_00870cb4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00870cb8",
      "incomplete_value": false,
      "site": "00870cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00870c60",
      "incomplete_value": false,
      "site": "00870c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00870cbc",
      "DATA",
      [
        "storage",
        "00c7f8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870cbc",
      "DATA",
      [
        "storage",
        "00c7f990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00870c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870c5c.md#insn-00870c60)
- 新版 `00870cb8`（命令位置の公開資料なし）

~~~diff
- 00870c60 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00870c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00870c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00870c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00870cb8 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00870cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00870cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00870cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00870c60 bytes 08012391
+ 00870cb8 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7b70773ec82a8386f7bfe860b86269"></a>

### [`00870ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870ca8.md) → [`00870d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d00.md) FUN_00870d00

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0085d54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00870d0c",
      "incomplete_value": false,
      "site": "00870d10",
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
      "definition_site": "00870cb4",
      "incomplete_value": false,
      "site": "00870cb8",
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
      "00870d0c",
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
      "00870d0c",
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

- 旧版 [`00870cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870ca8.md#insn-00870cb8) · [`00870cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00870/00870ca8.md#insn-00870cb4)
- 新版 `00870d10`（命令位置の公開資料なし） · `00870d0c`（命令位置の公開資料なし）

~~~diff
- 00870cb8 ["INT_ADD", "register:40f0:8", ["const:870cb8:8", "const:4:8"]]
- 00870cb8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00870d10 ["INT_ADD", "register:40f0:8", ["const:870d10:8", "const:4:8"]]
+ 00870d10 ["CALL", null, ["callee:0043b7b8:8"]]
- 00870cb8 bytes b02aef97
+ 00870d10 bytes aa2aef97
- 00870cb4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00870cb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00870cb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00870cb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00870d0c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00870d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00870d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00870d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00870cb4 bytes 00303d91
+ 00870d0c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbd5169dfa88e82d430d4d6550c30c3"></a>

### [`00871938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871938.md) → [`00871990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871990.md) FUN_00871990

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "008719b4",
      "incomplete_value": false,
      "site": "008719b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087195c",
      "incomplete_value": false,
      "site": "0087195c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "008719b4",
      "DATA",
      [
        "storage",
        "00c7f940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719b4",
      "DATA",
      [
        "storage",
        "00c7fa10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871938.md#insn-0087194c) · [`00871958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871938.md#insn-00871958)
- 新版 `008719a4`（命令位置の公開資料なし） · `008719b0`（命令位置の公開資料なし）

~~~diff
- 0087194c ["INT_ADD", "register:40f0:8", ["const:87194c:8", "const:4:8"]]
- 0087194c ["CALL", null, ["callee:00c57f60:8"]]
+ 008719a4 ["INT_ADD", "register:40f0:8", ["const:8719a4:8", "const:4:8"]]
+ 008719a4 ["CALL", null, ["callee:00c57f60:8"]]
- 0087194c bytes 51990f94
+ 008719a4 bytes 6f990f94
- 00871958 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00871958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008719b0 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 008719b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008719b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008719b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871958 bytes 08012591
+ 008719b0 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7c8759489c5c2320fc8299764489e4"></a>

### [`0087196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087196c.md) → [`008719c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008719c4.md) FUN_008719c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008719d0",
      "incomplete_value": false,
      "site": "008719d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871978",
      "incomplete_value": false,
      "site": "00871978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "008719d0",
      "DATA",
      [
        "storage",
        "00c7f940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008719d0",
      "DATA",
      [
        "storage",
        "00c7fa10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/0087196c.md#insn-00871974)
- 新版 `008719cc`（命令位置の公開資料なし）

~~~diff
- 00871974 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00871974 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871974 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871974 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008719cc ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 008719cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008719cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008719cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871974 bytes 29012591
+ 008719cc bytes 29412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9883dbe99481d1940f348cb4e3fdc6b5"></a>

### [`00871988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md) → [`008719e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008719e0.md) FUN_008719e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0085d4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) · 呼出先 10件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`00801c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c44.md) [`00801c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00801/00801c90.md) [`008056ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md)
- 新版 呼出元 1件 [`0085d54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) · 呼出先 10件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00800244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800244.md) [`00801c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00801/00801c9c.md) [`00801ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00801/00801ce8.md) [`00805744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805744.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a60",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a08",
      "value": [
        "leaf",
        "ram:a65dec:8"
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
      "site": "00871a90",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a38",
      "value": [
        "leaf",
        "ram:a65dec:8"
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
      "site": "00871ae4",
      "value": [
        "leaf",
        "ram:8064b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00871a8c",
      "value": [
        "leaf",
        "ram:80645c:8"
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
      "00871a60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00871a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "00871ae4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0080645c"
      ]
    ]
  ],
  "added": [
    [
      "00871a60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ],
    [
      "00871a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ],
    [
      "00871ae4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008064b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008719e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md#insn-008719e0) · [`00871a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md#insn-00871a08) · [`00871a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md#insn-00871a38)
- 新版 `00871a38`（命令位置の公開資料なし） · `00871a60`（命令位置の公開資料なし） · `00871a90`（命令位置の公開資料なし）

~~~diff
- 008719e0 ["INT_ADD", "register:40f0:8", ["const:8719e0:8", "const:4:8"]]
- 008719e0 ["CALL", null, ["callee:00805744:8"]]
+ 00871a38 ["INT_ADD", "register:40f0:8", ["const:871a38:8", "const:4:8"]]
+ 00871a38 ["CALL", null, ["callee:00805744:8"]]
- 008719e0 bytes 434ffe97
+ 00871a38 bytes 434ffe97
- 00871a08 ["INT_ADD", "register:40f0:8", ["const:871a08:8", "const:4:8"]]
- 00871a08 ["CALL", null, ["ram:a65dec:8"]]
+ 00871a60 ["INT_ADD", "register:40f0:8", ["const:871a60:8", "const:4:8"]]
+ 00871a60 ["CALL", null, ["ram:a65e5c:8"]]
- 00871a08 bytes f9d00794
+ 00871a60 bytes ffd00794
- 00871a38 ["INT_ADD", "register:40f0:8", ["const:871a38:8", "const:4:8"]]
- 00871a38 ["CALL", null, ["ram:a65dec:8"]]
+ 00871a90 ["INT_ADD", "register:40f0:8", ["const:871a90:8", "const:4:8"]]
+ 00871a90 ["CALL", null, ["ram:a65e5c:8"]]
- 00871a38 bytes edd00794
+ 00871a90 bytes f3d00794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fbeb719e1515a10ccc1cb68d1973af6"></a>

### [`00871b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b3c.md) → [`00871b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871b94.md) FUN_00871b94

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00871bb8",
      "incomplete_value": false,
      "site": "00871bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871b60",
      "incomplete_value": false,
      "site": "00871b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "00871bb8",
      "DATA",
      [
        "storage",
        "00c7f9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871bb8",
      "DATA",
      [
        "storage",
        "00c7faa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b3c.md#insn-00871b50) · [`00871b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b3c.md#insn-00871b5c)
- 新版 `00871ba8`（命令位置の公開資料なし） · `00871bb4`（命令位置の公開資料なし）

~~~diff
- 00871b50 ["INT_ADD", "register:40f0:8", ["const:871b50:8", "const:4:8"]]
- 00871b50 ["CALL", null, ["callee:00c57f60:8"]]
+ 00871ba8 ["INT_ADD", "register:40f0:8", ["const:871ba8:8", "const:4:8"]]
+ 00871ba8 ["CALL", null, ["callee:00c57f60:8"]]
- 00871b50 bytes d0980f94
+ 00871ba8 bytes ee980f94
- 00871b5c ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00871b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871bb4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00871bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871b5c bytes 08412791
+ 00871bb4 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8fe36f83b66eaf427c4b0f9a6ca645c"></a>

### [`00871b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b70.md) → [`00871bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871bc8.md) FUN_00871bc8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00871bd4",
      "incomplete_value": false,
      "site": "00871bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871b7c",
      "incomplete_value": false,
      "site": "00871b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "00871bd4",
      "DATA",
      [
        "storage",
        "00c7f9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871bd4",
      "DATA",
      [
        "storage",
        "00c7faa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b70.md#insn-00871b78)
- 新版 `00871bd0`（命令位置の公開資料なし）

~~~diff
- 00871b78 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00871b78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871b78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871b78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871bd0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00871bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871b78 bytes 29412791
+ 00871bd0 bytes 29812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a9f3ee51dc57c087ef66ce750386a47"></a>

### [`00871ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ec8.md) → [`00871f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871f20.md) FUN_00871f20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00871f28",
      "incomplete_value": false,
      "site": "00871f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ed0",
      "incomplete_value": false,
      "site": "00871ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "00871f2c",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871f2c",
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ec8.md#insn-00871ed0)
- 新版 `00871f28`（命令位置の公開資料なし）

~~~diff
- 00871ed0 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00871ed0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871ed0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871ed0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871f28 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00871f28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871f28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871f28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871ed0 bytes 29812991
+ 00871f28 bytes 29c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e61d81450a0df1f74759420f5f1156c"></a>

### [`00871ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ee8.md) → [`00871f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871f40.md) FUN_00871f40

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00871f48",
      "incomplete_value": false,
      "site": "00871f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871ef0",
      "incomplete_value": false,
      "site": "00871ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "00871f4c",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871f4c",
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ee8.md#insn-00871ef0) · [`00871f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871ee8.md#insn-00871f14)
- 新版 `00871f48`（命令位置の公開資料なし） · `00871f6c`（命令位置の公開資料なし）

~~~diff
- 00871ef0 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00871ef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00871ef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00871ef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00871f48 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00871f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00871f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00871f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00871ef0 bytes 29812991
+ 00871f48 bytes 29c12c91
- 00871f14 ["INT_ADD", "register:40f0:8", ["const:871f14:8", "const:4:8"]]
- 00871f14 ["CALL", null, ["callee:00c57f80:8"]]
+ 00871f6c ["INT_ADD", "register:40f0:8", ["const:871f6c:8", "const:4:8"]]
+ 00871f6c ["CALL", null, ["callee:00c57f80:8"]]
- 00871f14 bytes e7970f94
+ 00871f6c bytes 05980f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a217a2caf10c48dc356be5da4529ece0"></a>

### [`00871f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f28.md) → [`00871f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871f80.md) FUN_00871f80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00871fac",
      "incomplete_value": false,
      "site": "00871fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871f54",
      "incomplete_value": false,
      "site": "00871f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "00871fac",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871fac",
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f28.md#insn-00871f3c) · [`00871f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f28.md#insn-00871f4c) · [`00871f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f28.md#insn-00871f74)
- 新版 `00871f94`（命令位置の公開資料なし） · `00871fa4`（命令位置の公開資料なし） · `00871fcc`（命令位置の公開資料なし）

~~~diff
- 00871f3c ["INT_ADD", "register:40f0:8", ["const:871f3c:8", "const:4:8"]]
- 00871f3c ["CALL", null, ["callee:00c57f60:8"]]
+ 00871f94 ["INT_ADD", "register:40f0:8", ["const:871f94:8", "const:4:8"]]
+ 00871f94 ["CALL", null, ["callee:00c57f60:8"]]
- 00871f3c bytes d5970f94
+ 00871f94 bytes f3970f94
- 00871f4c ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00871f4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00871f4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00871f4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00871fa4 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00871fa4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00871fa4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00871fa4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00871f4c bytes 4a812991
+ 00871fa4 bytes 4ac12c91
- 00871f74 ["INT_ADD", "register:40f0:8", ["const:871f74:8", "const:4:8"]]
- 00871f74 ["CALL", null, ["callee:0043bb60:8"]]
+ 00871fcc ["INT_ADD", "register:40f0:8", ["const:871fcc:8", "const:4:8"]]
+ 00871fcc ["CALL", null, ["callee:0043bb60:8"]]
- 00871f74 bytes eb26ef97
+ 00871fcc bytes e526ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ee71cf10e5c9095f5421c6c27a763c"></a>

### [`00871f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f9c.md) → [`00871ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871ff4.md) FUN_00871ff4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "00871ffc",
      "incomplete_value": false,
      "site": "00871ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00871fa4",
      "incomplete_value": false,
      "site": "00871fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "00871ffc",
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00871ffc",
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871f9c.md#insn-00871fa0)
- 新版 `00871ff8`（命令位置の公開資料なし）

~~~diff
- 00871fa0 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00871fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00871fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00871fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00871ff8 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 00871ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00871ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00871fa0 bytes 08812991
+ 00871ff8 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008bf73a33f55f219d37304329e2dcd4"></a>

### [`00872020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md) → [`00872078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872078.md) FUN_00872078

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "0087209c",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00872044",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "008720a4",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087204c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0087209c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008720a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "0087209c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "008720a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md#insn-00872044) · [`0087204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md#insn-0087204c) · [`00872048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md#insn-00872048)
- 新版 `0087209c`（命令位置の公開資料なし） · `008720a4`（命令位置の公開資料なし） · `008720a0`（命令位置の公開資料なし）

~~~diff
- 00872044 ["INT_ADD", "register:40f0:8", ["const:872044:8", "const:4:8"]]
- 00872044 ["CALL", null, ["ram:48ccf8:8"]]
+ 0087209c ["INT_ADD", "register:40f0:8", ["const:87209c:8", "const:4:8"]]
+ 0087209c ["CALL", null, ["ram:48cd38:8"]]
- 00872044 bytes 2d6bf097
+ 0087209c bytes 276bf097
- 0087204c ["INT_ADD", "register:40f0:8", ["const:87204c:8", "const:4:8"]]
- 0087204c ["CALL", null, ["ram:48ccf8:8"]]
+ 008720a4 ["INT_ADD", "register:40f0:8", ["const:8720a4:8", "const:4:8"]]
+ 008720a4 ["CALL", null, ["ram:48cd38:8"]]
- 0087204c bytes 2b6bf097
+ 008720a4 bytes 256bf097
- 00872048 ["INT_ADD", "register:40f0:8", ["const:872048:8", "const:4:8"]]
- 00872048 ["CALL", null, ["callee:0048e820:8"]]
+ 008720a0 ["INT_ADD", "register:40f0:8", ["const:8720a0:8", "const:4:8"]]
+ 008720a0 ["CALL", null, ["callee:0048e820:8"]]
- 00872048 bytes e671f097
+ 008720a0 bytes e071f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16606ec2361b8bd64c71623b07933eb7"></a>

### [`008720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008720f8.md) → [`00872150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872150.md) FUN_00872150

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00872158",
      "incomplete_value": true,
      "site": "0087215c",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872100",
      "incomplete_value": true,
      "site": "00872104",
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
            "const:ae0:8"
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
      "0087215c",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087215c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008720f8.md#insn-00872100)
- 新版 `00872158`（命令位置の公開資料なし）

~~~diff
- 00872100 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00872100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872158 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00872158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872100 bytes 29812b91
+ 00872158 bytes 29c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b705b98f2e6dec99b39848951c74a98"></a>

### [`00872118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872118.md) → [`00872170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872170.md) FUN_00872170

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00872178",
      "incomplete_value": false,
      "site": "0087217c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872120",
      "incomplete_value": false,
      "site": "00872124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0087217c",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087217c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872118.md#insn-00872120) · [`00872144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872118.md#insn-00872144)
- 新版 `00872178`（命令位置の公開資料なし） · `0087219c`（命令位置の公開資料なし）

~~~diff
- 00872120 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00872120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00872120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00872120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00872178 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00872178 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00872178 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00872178 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00872120 bytes 29812b91
+ 00872178 bytes 29c12e91
- 00872144 ["INT_ADD", "register:40f0:8", ["const:872144:8", "const:4:8"]]
- 00872144 ["CALL", null, ["callee:00c57f80:8"]]
+ 0087219c ["INT_ADD", "register:40f0:8", ["const:87219c:8", "const:4:8"]]
+ 0087219c ["CALL", null, ["callee:00c57f80:8"]]
- 00872144 bytes 5b970f94
+ 0087219c bytes 79970f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9c8ffc43b6bb2f8d69426ef0b7af84"></a>

### [`008721cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008721cc.md) → [`00872224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872224.md) FUN_00872224

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "0087222c",
      "incomplete_value": false,
      "site": "0087222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008721d4",
      "incomplete_value": false,
      "site": "008721d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0087222c",
      "DATA",
      [
        "storage",
        "00c7fae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087222c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008721d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008721cc.md#insn-008721d0)
- 新版 `00872228`（命令位置の公開資料なし）

~~~diff
- 008721d0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 008721d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008721d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008721d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872228 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00872228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008721d0 bytes 08812b91
+ 00872228 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ed057fbb5820131dbcd688343e3d2a"></a>

### [`00872250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md) → [`008722a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008722a8.md) FUN_008722a8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

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
      "site": "008722cc",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00872274",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "site": "008722d4",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087227c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "008722cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008722d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "008722cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "008722d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md#insn-00872274) · [`0087227c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md#insn-0087227c) · [`00872278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md#insn-00872278)
- 新版 `008722cc`（命令位置の公開資料なし） · `008722d4`（命令位置の公開資料なし） · `008722d0`（命令位置の公開資料なし）

~~~diff
- 00872274 ["INT_ADD", "register:40f0:8", ["const:872274:8", "const:4:8"]]
- 00872274 ["CALL", null, ["ram:48ccf8:8"]]
+ 008722cc ["INT_ADD", "register:40f0:8", ["const:8722cc:8", "const:4:8"]]
+ 008722cc ["CALL", null, ["ram:48cd38:8"]]
- 00872274 bytes a16af097
+ 008722cc bytes 9b6af097
- 0087227c ["INT_ADD", "register:40f0:8", ["const:87227c:8", "const:4:8"]]
- 0087227c ["CALL", null, ["ram:48ccf8:8"]]
+ 008722d4 ["INT_ADD", "register:40f0:8", ["const:8722d4:8", "const:4:8"]]
+ 008722d4 ["CALL", null, ["ram:48cd38:8"]]
- 0087227c bytes 9f6af097
+ 008722d4 bytes 996af097
- 00872278 ["INT_ADD", "register:40f0:8", ["const:872278:8", "const:4:8"]]
- 00872278 ["CALL", null, ["callee:0048e820:8"]]
+ 008722d0 ["INT_ADD", "register:40f0:8", ["const:8722d0:8", "const:4:8"]]
+ 008722d0 ["CALL", null, ["callee:0048e820:8"]]
- 00872278 bytes 5a71f097
+ 008722d0 bytes 5471f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41361d4b34be64cb959fc829d40ea345"></a>

### [`00872328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872328.md) → [`00872380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872380.md) FUN_00872380

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00872384",
      "incomplete_value": false,
      "site": "00872388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087232c",
      "incomplete_value": false,
      "site": "00872330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00872388",
      "DATA",
      [
        "storage",
        "00c7fb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00872388",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872328.md#insn-0087232c)
- 新版 `00872384`（命令位置の公開資料なし）

~~~diff
- 0087232c ["COPY", "tmp:0:8", ["const:b78:8"]]
- 0087232c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087232c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087232c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00872384 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00872384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00872384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00872384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087232c bytes 08e12d91
+ 00872384 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a1ebd3d540cf8cff1cefc73cb97e3eb"></a>

### [`00872378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872378.md) → [`008723d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md) FUN_008723d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) · 呼出先 6件 [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444680.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) · 呼出先 6件 [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00872410",
      "incomplete_value": false,
      "site": "00872410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008723b8",
      "incomplete_value": false,
      "site": "008723b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "definition_site": "00872428",
      "incomplete_value": false,
      "site": "00872430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:e0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008723d0",
      "incomplete_value": false,
      "site": "008723d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:dcc:8"
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
      "00872410",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00872428",
      "PARAM",
      [
        "storage",
        "002eedcc",
        null,
        "string"
      ]
    ],
    [
      "00872488",
      "READ",
      [
        "storage",
        "002a7e0b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872410",
      "DATA",
      [
        "storage",
        "00c7fc98",
        null,
        "undefined *"
      ]
    ],
    [
      "00872428",
      "PARAM",
      [
        "storage",
        "002eee0c",
        null,
        "string"
      ]
    ],
    [
      "00872488",
      "READ",
      [
        "storage",
        "002a7daf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008723d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872378.md#insn-008723d8) · [`008723b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872378.md#insn-008723b4) · [`008723d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872378.md#insn-008723d0)
- 新版 `00872430`（命令位置の公開資料なし） · `0087240c`（命令位置の公開資料なし） · `00872428`（命令位置の公開資料なし）

~~~diff
- 008723d8 ["INT_ADD", "register:40f0:8", ["const:8723d8:8", "const:4:8"]]
- 008723d8 ["CALL", null, ["callee:00c58260:8"]]
+ 00872430 ["INT_ADD", "register:40f0:8", ["const:872430:8", "const:4:8"]]
+ 00872430 ["CALL", null, ["callee:00c58260:8"]]
- 008723d8 bytes 6e970f94
+ 00872430 bytes 8c970f94
- 008723b4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 008723b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008723b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008723b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087240c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0087240c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087240c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087240c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008723b4 bytes 08212f91
+ 0087240c bytes 08613291
- 008723d0 ["COPY", "tmp:0:8", ["const:dcc:8"]]
- 008723d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008723d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008723d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00872428 ["COPY", "tmp:0:8", ["const:e0c:8"]]
+ 00872428 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00872428 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00872428 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008723d0 bytes 21303791
+ 00872428 bytes 21303891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-179ad44ec5696834baf65584f238a838"></a>

### [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) → [`008725f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md) FUN_008725f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008729ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008729ec.md) · 呼出先 5件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00872a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a44.md) · 呼出先 5件 [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.45% / 新版 87.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087265c",
      "incomplete_value": false,
      "site": "00872664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872604",
      "incomplete_value": false,
      "site": "0087260c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "definition_site": "0087266c",
      "incomplete_value": false,
      "site": "00872674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1122000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00872614",
      "incomplete_value": false,
      "site": "0087261c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1122000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "00872694",
      "incomplete_value": false,
      "site": "0087269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087263c",
      "incomplete_value": false,
      "site": "00872644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1121000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00872638",
      "DATA",
      [
        "storage",
        "00c7fbc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00872640",
      "READ",
      [
        "storage",
        "00fe0878",
        null,
        "undefined1"
      ]
    ],
    [
      "00872650",
      "READ",
      [
        "storage",
        "01070513",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00872638",
      "DATA",
      [
        "storage",
        "00c7fc98",
        null,
        "undefined *"
      ]
    ],
    [
      "00872640",
      "READ",
      [
        "storage",
        "00fe0978",
        null,
        "undefined1"
      ]
    ],
    [
      "00872650",
      "READ",
      [
        "storage",
        "01070613",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008725c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md#insn-008725c4) · [`0087260c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md#insn-0087260c) · [`0087261c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md#insn-0087261c)
- 新版 `0087261c`（命令位置の公開資料なし） · `00872664`（命令位置の公開資料なし） · `00872674`（命令位置の公開資料なし）

~~~diff
- 008725c4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 008725c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008725c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008725c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087261c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0087261c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087261c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087261c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008725c4 bytes 29212f91
+ 0087261c bytes 29613291
- 0087260c ["INT_ADD", "register:40f0:8", ["const:87260c:8", "const:4:8"]]
- 0087260c ["CALL", null, ["callee:00484800:8"]]
+ 00872664 ["INT_ADD", "register:40f0:8", ["const:872664:8", "const:4:8"]]
+ 00872664 ["CALL", null, ["callee:00484800:8"]]
- 0087260c bytes 6d48f097
+ 00872664 bytes 6748f097
- 0087261c ["INT_ADD", "register:40f0:8", ["const:87261c:8", "const:4:8"]]
- 0087261c ["CALL", null, ["callee:004939d8:8"]]
+ 00872674 ["INT_ADD", "register:40f0:8", ["const:872674:8", "const:4:8"]]
+ 00872674 ["CALL", null, ["callee:004939d8:8"]]
- 0087261c bytes df84f097
+ 00872674 bytes d984f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1374b4b6b92d8cc340d3a2269099ce6"></a>

### [`00872a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md) → [`00872a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md) FUN_00872a68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.26% / 新版 85.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `call_target` 2件, `store_destination` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00872ce0",
      "incomplete_value": false,
      "site": "00872ce0",
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
    "old": {
      "definition_site": "00872c88",
      "incomplete_value": false,
      "site": "00872c88",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 24,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00872ce4",
      "incomplete_value": false,
      "site": "00872ce4",
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
    "old": {
      "definition_site": "00872c8c",
      "incomplete_value": false,
      "site": "00872c8c",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00872ce0",
      "incomplete_value": false,
      "site": "00872ce4",
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
    "old": {
      "definition_site": "00872c88",
      "incomplete_value": false,
      "site": "00872c8c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "00872aa0",
      "PARAM",
      [
        "storage",
        "00ca8170",
        null,
        null
      ]
    ],
    [
      "00872aa4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009ccb7c"
      ]
    ],
    [
      "00872b14",
      "READ",
      [
        "storage",
        "002a7e1b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00872aa0",
      "PARAM",
      [
        "storage",
        "00ca8270",
        null,
        null
      ]
    ],
    [
      "00872aa4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009ccbd0"
      ]
    ],
    [
      "00872b14",
      "READ",
      [
        "storage",
        "002a7dbf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md#insn-00872a4c) · [`00872b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md#insn-00872b7c) · [`00872c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md#insn-00872c0c)
- 新版 `00872aa4`（命令位置の公開資料なし） · `00872bd4`（命令位置の公開資料なし） · `00872c64`（命令位置の公開資料なし）

~~~diff
- 00872a4c ["INT_ADD", "register:40f0:8", ["const:872a4c:8", "const:4:8"]]
- 00872a4c ["CALL", null, ["ram:9ccb7c:8"]]
+ 00872aa4 ["INT_ADD", "register:40f0:8", ["const:872aa4:8", "const:4:8"]]
+ 00872aa4 ["CALL", null, ["ram:9ccbd0:8"]]
- 00872a4c bytes 4c680594
+ 00872aa4 bytes 4b680594
- 00872b7c ["INT_ADD", "register:40f0:8", ["const:872b7c:8", "const:4:8"]]
- 00872b7c ["CALL", null, ["callee:0047e91c:8"]]
+ 00872bd4 ["INT_ADD", "register:40f0:8", ["const:872bd4:8", "const:4:8"]]
+ 00872bd4 ["CALL", null, ["callee:0047e91c:8"]]
- 00872b7c bytes 582ff097
+ 00872bd4 bytes 522ff097
- 00872c0c ["INT_ADD", "register:40f0:8", ["const:872c0c:8", "const:4:8"]]
- 00872c0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00872c64 ["INT_ADD", "register:40f0:8", ["const:872c64:8", "const:4:8"]]
+ 00872c64 ["CALL", null, ["callee:00c57f80:8"]]
- 00872c0c bytes a9940f94
+ 00872c64 bytes c7940f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb7b1aea9f74656371c4e0e9aec50c3"></a>

### [`00873048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873048.md) → [`008730a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730a0.md) FUN_008730a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008730a4",
      "incomplete_value": true,
      "site": "008730a8",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087304c",
      "incomplete_value": true,
      "site": "00873050",
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
            "const:c10:8"
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
      "008730a8",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008730a8",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873048.md#insn-0087304c)
- 新版 `008730a4`（命令位置の公開資料なし）

~~~diff
- 0087304c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0087304c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087304c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087304c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008730a4 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 008730a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008730a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008730a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087304c bytes 08413091
+ 008730a4 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366961453a7a17d89d3ebf0783972b43"></a>

### [`00873058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873058.md) → [`008730b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730b0.md) FUN_008730b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008730c0",
      "incomplete_value": false,
      "site": "008730c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873068",
      "incomplete_value": false,
      "site": "00873070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "008730c8",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008730c8",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873058.md#insn-00873068) · [`00873074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873058.md#insn-00873074)
- 新版 `008730c0`（命令位置の公開資料なし） · `008730cc`（命令位置の公開資料なし）

~~~diff
- 00873068 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00873068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008730c0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 008730c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008730c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008730c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873068 bytes 08413091
+ 008730c0 bytes 08813391
- 00873074 ["INT_ADD", "register:40f0:8", ["const:873074:8", "const:4:8"]]
- 00873074 ["CALL", null, ["callee:00c57f70:8"]]
+ 008730cc ["INT_ADD", "register:40f0:8", ["const:8730cc:8", "const:4:8"]]
+ 008730cc ["CALL", null, ["callee:00c57f70:8"]]
- 00873074 bytes 8b930f94
+ 008730cc bytes a9930f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2070f0484cc13bafb0b387563ea36753"></a>

### [`00873098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md) → [`008730f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md) FUN_008730f0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 2件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873134",
      "incomplete_value": false,
      "site": "00873134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008730dc",
      "incomplete_value": false,
      "site": "008730dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "0087319c",
      "incomplete_value": true,
      "site": "0087319c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873144",
      "incomplete_value": true,
      "site": "00873144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00873154",
      "incomplete_value": false,
      "site": "0087315c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008730fc",
      "incomplete_value": false,
      "site": "00873104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ee000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00873134",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ],
    [
      "00873154",
      "PARAM",
      [
        "storage",
        "002eee30",
        null,
        "string"
      ]
    ],
    [
      "00873168",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00873134",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "00873154",
      "PARAM",
      [
        "storage",
        "002eee70",
        null,
        "string"
      ]
    ],
    [
      "00873168",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md#insn-00873104) · [`00873180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md#insn-00873180) · [`0087335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md#insn-0087335c)
- 新版 `0087315c`（命令位置の公開資料なし） · `008731d8`（命令位置の公開資料なし） · `008733b4`（命令位置の公開資料なし）

~~~diff
- 00873104 ["INT_ADD", "register:40f0:8", ["const:873104:8", "const:4:8"]]
- 00873104 ["CALL", null, ["callee:00c58260:8"]]
+ 0087315c ["INT_ADD", "register:40f0:8", ["const:87315c:8", "const:4:8"]]
+ 0087315c ["CALL", null, ["callee:00c58260:8"]]
- 00873104 bytes 23940f94
+ 0087315c bytes 41940f94
- 00873180 ["INT_ADD", "register:40f0:8", ["const:873180:8", "const:4:8"]]
- 00873180 ["CALL", null, ["callee:0047e64c:8"]]
+ 008731d8 ["INT_ADD", "register:40f0:8", ["const:8731d8:8", "const:4:8"]]
+ 008731d8 ["CALL", null, ["callee:0047e64c:8"]]
- 00873180 bytes 232df097
+ 008731d8 bytes 1d2df097
- 0087335c ["INT_ADD", "register:40f0:8", ["const:87335c:8", "const:4:8"]]
- 0087335c ["CALL", null, ["callee:00c57f20:8"]]
+ 008733b4 ["INT_ADD", "register:40f0:8", ["const:8733b4:8", "const:4:8"]]
+ 008733b4 ["CALL", null, ["callee:00c57f20:8"]]
- 0087335c bytes bd920f94
+ 008733b4 bytes db920f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360ff2bbd5e5fac64219de5e2e93a5f5"></a>

### [`00873494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873494.md) → [`008734ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008734ec.md) FUN_008734ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873504",
      "incomplete_value": false,
      "site": "00873508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008734ac",
      "incomplete_value": false,
      "site": "008734b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "00873508",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873508",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873494.md#insn-00873508) · [`008734ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873494.md#insn-008734ac) · [`008734bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873494.md#insn-008734bc)
- 新版 `00873560`（命令位置の公開資料なし） · `00873504`（命令位置の公開資料なし） · `00873514`（命令位置の公開資料なし）

~~~diff
- 00873508 ["COPY", "register:0:8", ["register:4040:8"]]
- 00873508 ["INT_ADD", "register:40f0:8", ["const:873508:8", "const:4:8"]]
- 00873508 ["CALLIND", null, ["register:0:8"]]
+ 00873560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00873560 ["INT_ADD", "register:40f0:8", ["const:873560:8", "const:4:8"]]
+ 00873560 ["CALLIND", null, ["register:0:8"]]
- 00873508 bytes 00013fd6
+ 00873560 bytes 00013fd6
- 008734ac ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008734ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008734ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008734ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00873504 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00873504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00873504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00873504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008734ac bytes 29813191
+ 00873504 bytes 29c13491
- 008734bc ["INT_ADD", "register:40f0:8", ["const:8734bc:8", "const:4:8"]]
- 008734bc ["CALL", null, ["callee:00c57f80:8"]]
+ 00873514 ["INT_ADD", "register:40f0:8", ["const:873514:8", "const:4:8"]]
+ 00873514 ["CALL", null, ["callee:00c57f80:8"]]
- 008734bc bytes 7d920f94
+ 00873514 bytes 9b920f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-755069c5e87619ae2c79fd1cd7766a4e"></a>

### [`00873540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873540.md) → [`00873598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873598.md) FUN_00873598

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "008735b0",
      "incomplete_value": false,
      "site": "008735b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873558",
      "incomplete_value": false,
      "site": "0087355c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008735b4",
      "DATA",
      [
        "storage",
        "00c7fc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008735b4",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873540.md#insn-00873558) · [`00873568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873540.md#insn-00873568) · [`0087357c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873540.md#insn-0087357c)
- 新版 `008735b0`（命令位置の公開資料なし） · `008735c0`（命令位置の公開資料なし） · `008735d4`（命令位置の公開資料なし）

~~~diff
- 00873558 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00873558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00873558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00873558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008735b0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 008735b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008735b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008735b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00873558 bytes 29813191
+ 008735b0 bytes 29c13491
- 00873568 ["INT_ADD", "register:40f0:8", ["const:873568:8", "const:4:8"]]
- 00873568 ["CALL", null, ["callee:00c57f80:8"]]
+ 008735c0 ["INT_ADD", "register:40f0:8", ["const:8735c0:8", "const:4:8"]]
+ 008735c0 ["CALL", null, ["callee:00c57f80:8"]]
- 00873568 bytes 52920f94
+ 008735c0 bytes 70920f94
- 0087357c ["INT_ADD", "register:40f0:8", ["const:87357c:8", "const:4:8"]]
- 0087357c ["CALL", null, ["callee:00c53da0:8"]]
+ 008735d4 ["INT_ADD", "register:40f0:8", ["const:8735d4:8", "const:4:8"]]
+ 008735d4 ["CALL", null, ["callee:00c53da0:8"]]
- 0087357c bytes e1810f94
+ 008735d4 bytes f3810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fb6300ee8d049343108b997fe46859"></a>

### [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) → [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) FUN_00873634

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00560b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560b08.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00560b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0087365c",
      "value": [
        "leaf",
        "ram:768430:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873604",
      "value": [
        "leaf",
        "ram:7683d8:8"
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
      "site": "008737f0",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873798",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873808",
      "value": [
        "leaf",
        "ram:769298:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008737b0",
      "value": [
        "leaf",
        "ram:769240:8"
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
      "0087365c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "00873678",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "qword"
      ]
    ],
    [
      "00873688",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087365c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768430"
      ]
    ],
    [
      "00873678",
      "DATA",
      [
        "storage",
        "003c79f8",
        null,
        "dword"
      ]
    ],
    [
      "00873688",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md#insn-00873604) · [`00873798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md#insn-00873798) · [`008737b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md#insn-008737b0)
- 新版 `0087365c`（命令位置の公開資料なし） · `008737f0`（命令位置の公開資料なし） · `00873808`（命令位置の公開資料なし）

~~~diff
- 00873604 ["INT_ADD", "register:40f0:8", ["const:873604:8", "const:4:8"]]
- 00873604 ["CALL", null, ["ram:7683d8:8"]]
+ 0087365c ["INT_ADD", "register:40f0:8", ["const:87365c:8", "const:4:8"]]
+ 0087365c ["CALL", null, ["ram:768430:8"]]
- 00873604 bytes 75d3fb97
+ 0087365c bytes 75d3fb97
- 00873798 ["INT_ADD", "register:40f0:8", ["const:873798:8", "const:4:8"]]
- 00873798 ["CALL", null, ["ram:764ee0:8"]]
+ 008737f0 ["INT_ADD", "register:40f0:8", ["const:8737f0:8", "const:4:8"]]
+ 008737f0 ["CALL", null, ["ram:764f38:8"]]
- 00873798 bytes d2c5fb97
+ 008737f0 bytes d2c5fb97
- 008737b0 ["INT_ADD", "register:40f0:8", ["const:8737b0:8", "const:4:8"]]
- 008737b0 ["CALL", null, ["ram:769240:8"]]
+ 00873808 ["INT_ADD", "register:40f0:8", ["const:873808:8", "const:4:8"]]
+ 00873808 ["CALL", null, ["ram:769298:8"]]
- 008737b0 bytes a4d6fb97
+ 00873808 bytes a4d6fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a953a177b99b637adcd21242f85219"></a>

### [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) → [`00873b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md) FUN_00873b00

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`00874ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ad4.md) · 呼出先 9件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) [`00874578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874578.md) [`008745c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008745c8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 2件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874b2c.md) · 呼出先 9件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) [`008745d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008745d0.md) [`00874620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874620.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873b68",
      "incomplete_value": false,
      "site": "00873b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b10",
      "incomplete_value": false,
      "site": "00873b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "definition_site": "00873b88",
      "incomplete_value": false,
      "site": "00873b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b30",
      "incomplete_value": false,
      "site": "00873b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "00873b68",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b88",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873bc8",
      "READ",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873b68",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ],
    [
      "00873b88",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ],
    [
      "00873bc8",
      "READ",
      [
        "storage",
        "00c7fdb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md#insn-00873ad4) · [`00873af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md#insn-00873af8) · [`00873b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md#insn-00873b00)
- 新版 `00873b2c`（命令位置の公開資料なし） · `00873b50`（命令位置の公開資料なし） · `00873b58`（命令位置の公開資料なし）

~~~diff
- 00873ad4 ["INT_ADD", "register:40f0:8", ["const:873ad4:8", "const:4:8"]]
- 00873ad4 ["CALL", null, ["callee:0044f920:8"]]
+ 00873b2c ["INT_ADD", "register:40f0:8", ["const:873b2c:8", "const:4:8"]]
+ 00873b2c ["CALL", null, ["callee:0044f920:8"]]
- 00873ad4 bytes 836fef97
+ 00873b2c bytes 7d6fef97
- 00873af8 ["INT_ADD", "register:40f0:8", ["const:873af8:8", "const:4:8"]]
- 00873af8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00873b50 ["INT_ADD", "register:40f0:8", ["const:873b50:8", "const:4:8"]]
+ 00873b50 ["CALL", null, ["callee:00c53d70:8"]]
- 00873af8 bytes 76800f94
+ 00873b50 bytes 88800f94
- 00873b00 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00873b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873b58 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00873b58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873b58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873b58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873b00 bytes 08013391
+ 00873b58 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a84d410f5fe46a624627e517b30193a"></a>

### [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) → [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) FUN_00873ca8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) · 呼出先 7件 [`00874ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ca8.md) [`00874cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874cf8.md) [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 2件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) · 呼出先 7件 [`00874d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d00.md) [`00874d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md) [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873d08",
      "incomplete_value": false,
      "site": "00873d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873cb0",
      "incomplete_value": false,
      "site": "00873cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "definition_site": "00873d28",
      "incomplete_value": false,
      "site": "00873d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873cd0",
      "incomplete_value": false,
      "site": "00873cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00873d08",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d28",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d6c",
      "READ",
      [
        "storage",
        "00c7fde0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873d08",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d28",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ],
    [
      "00873d6c",
      "READ",
      [
        "storage",
        "00c7feb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md#insn-00873d28) · [`00873c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md#insn-00873c98) · [`00873ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md#insn-00873ca0)
- 新版 `00873d80`（命令位置の公開資料なし） · `00873cf0`（命令位置の公開資料なし） · `00873cf8`（命令位置の公開資料なし）

~~~diff
- 00873d28 ["INT_ADD", "register:40f0:8", ["const:873d28:8", "const:4:8"]]
- 00873d28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00873d80 ["INT_ADD", "register:40f0:8", ["const:873d80:8", "const:4:8"]]
+ 00873d80 ["CALL", null, ["callee:00c53da0:8"]]
- 00873d28 bytes f67f0f94
+ 00873d80 bytes 08800f94
- 00873c98 ["INT_ADD", "register:40f0:8", ["const:873c98:8", "const:4:8"]]
- 00873c98 ["CALL", null, ["callee:00c53d70:8"]]
+ 00873cf0 ["INT_ADD", "register:40f0:8", ["const:873cf0:8", "const:4:8"]]
+ 00873cf0 ["CALL", null, ["callee:00c53d70:8"]]
- 00873c98 bytes 0e800f94
+ 00873cf0 bytes 20800f94
- 00873ca0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00873ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873cf8 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00873cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873ca0 bytes 08013791
+ 00873cf8 bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fb272cdf39db9cea68dc8ccf1a7e4d"></a>

### [`00873dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md) → [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) FUN_00873e20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) · 呼出先 7件 [`008750e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750e0.md) [`00875130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875130.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) · 呼出先 7件 [`00875138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md) [`00875188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875188.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00873e80",
      "incomplete_value": false,
      "site": "00873e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e28",
      "incomplete_value": false,
      "site": "00873e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "definition_site": "00873ea0",
      "incomplete_value": false,
      "site": "00873ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e48",
      "incomplete_value": false,
      "site": "00873e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00873e80",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ee4",
      "READ",
      [
        "storage",
        "00c7fe60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00873e80",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ea0",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ],
    [
      "00873ee4",
      "READ",
      [
        "storage",
        "00c7ff30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md#insn-00873ea0) · [`00873e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md#insn-00873e10) · [`00873e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873dc8.md#insn-00873e18)
- 新版 `00873ef8`（命令位置の公開資料なし） · `00873e68`（命令位置の公開資料なし） · `00873e70`（命令位置の公開資料なし）

~~~diff
- 00873ea0 ["INT_ADD", "register:40f0:8", ["const:873ea0:8", "const:4:8"]]
- 00873ea0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00873ef8 ["INT_ADD", "register:40f0:8", ["const:873ef8:8", "const:4:8"]]
+ 00873ef8 ["CALL", null, ["callee:00c53da0:8"]]
- 00873ea0 bytes 987f0f94
+ 00873ef8 bytes aa7f0f94
- 00873e10 ["INT_ADD", "register:40f0:8", ["const:873e10:8", "const:4:8"]]
- 00873e10 ["CALL", null, ["callee:00c53d70:8"]]
+ 00873e68 ["INT_ADD", "register:40f0:8", ["const:873e68:8", "const:4:8"]]
+ 00873e68 ["CALL", null, ["callee:00c53d70:8"]]
- 00873e10 bytes b07f0f94
+ 00873e68 bytes c27f0f94
- 00873e18 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00873e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873e70 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00873e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873e18 bytes 08013991
+ 00873e70 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c319f8cf853aaeb9203e073a1023f409"></a>

### [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) → [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) FUN_00873f98

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008735dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/008735dc.md) [`00874d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md) [`008751b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md) [`00876058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876058.md) · 呼出先 16件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008753dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008753dc.md)
- 新版 呼出元 4件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md) [`0087520c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md) [`008760b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008760b0.md) · 呼出先 16件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.05% / 新版 89.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00873ff4",
      "incomplete_value": true,
      "site": "00873ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dcb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873f9c",
      "incomplete_value": true,
      "site": "00873f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e27:8"
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
      "definition_site": "00873ffc",
      "incomplete_value": true,
      "site": "00873ffc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00873fa4",
      "incomplete_value": true,
      "site": "00873fa4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874040",
      "incomplete_value": true,
      "site": "00874050",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:61b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873fe8",
      "incomplete_value": true,
      "site": "00873ff8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:668:8"
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
      "00873fe8",
      "READ",
      [
        "storage",
        "002a7e27",
        null,
        "string"
      ]
    ],
    [
      "00873fec",
      "READ",
      [
        "storage",
        "002a7e2c",
        null,
        "string"
      ]
    ],
    [
      "00874040",
      "READ",
      [
        "storage",
        "002a3668",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00873fe8",
      "READ",
      [
        "storage",
        "002a7dcb",
        null,
        "string"
      ]
    ],
    [
      "00873fec",
      "READ",
      [
        "storage",
        "002a7dd0",
        null,
        "string"
      ]
    ],
    [
      "00874040",
      "READ",
      [
        "storage",
        "002a361b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008740f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md#insn-008740f0) · [`008740fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md#insn-008740fc) · [`00873f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md#insn-00873f88)
- 新版 `00874148`（命令位置の公開資料なし） · `00874154`（命令位置の公開資料なし） · `00873fe0`（命令位置の公開資料なし）

~~~diff
- 008740f0 ["INT_ADD", "register:40f0:8", ["const:8740f0:8", "const:4:8"]]
- 008740f0 ["CALL", null, ["ram:764384:8"]]
+ 00874148 ["INT_ADD", "register:40f0:8", ["const:874148:8", "const:4:8"]]
+ 00874148 ["CALL", null, ["ram:7643dc:8"]]
- 008740f0 bytes a5c0fb97
+ 00874148 bytes a5c0fb97
- 008740fc ["INT_ADD", "register:40f0:8", ["const:8740fc:8", "const:4:8"]]
- 008740fc ["CALL", null, ["ram:764ee0:8"]]
+ 00874154 ["INT_ADD", "register:40f0:8", ["const:874154:8", "const:4:8"]]
+ 00874154 ["CALL", null, ["ram:764f38:8"]]
- 008740fc bytes 79c3fb97
+ 00874154 bytes 79c3fb97
- 00873f88 ["COPY", "tmp:0:8", ["const:e27:8"]]
- 00873f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00873fe0 ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 00873fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00873fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00873fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873f88 bytes 089d3891
+ 00873fe0 bytes 082d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f2be55969aca64352d1af84a924e9a0"></a>

### [`0087442c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087442c.md) → [`00874484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874484.md) FUN_00874484

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00874498",
      "incomplete_value": false,
      "site": "0087449c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874440",
      "incomplete_value": false,
      "site": "00874444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "0087449c",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087449c",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087442c.md#insn-00874440) · [`00874454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087442c.md#insn-00874454) · [`00874474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087442c.md#insn-00874474)
- 新版 `00874498`（命令位置の公開資料なし） · `008744ac`（命令位置の公開資料なし） · `008744cc`（命令位置の公開資料なし）

~~~diff
- 00874440 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00874440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874498 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00874498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874440 bytes 08013391
+ 00874498 bytes 08413691
- 00874454 ["INT_ADD", "register:40f0:8", ["const:874454:8", "const:4:8"]]
- 00874454 ["CALL", null, ["callee:00c53da0:8"]]
+ 008744ac ["INT_ADD", "register:40f0:8", ["const:8744ac:8", "const:4:8"]]
+ 008744ac ["CALL", null, ["callee:00c53da0:8"]]
- 00874454 bytes 2b7e0f94
+ 008744ac bytes 3d7e0f94
- 00874474 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874474 ["INT_ADD", "register:40f0:8", ["const:874474:8", "const:4:8"]]
- 00874474 ["CALLIND", null, ["register:0:8"]]
+ 008744cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008744cc ["INT_ADD", "register:40f0:8", ["const:8744cc:8", "const:4:8"]]
+ 008744cc ["CALLIND", null, ["register:0:8"]]
- 00874474 bytes 00013fd6
+ 008744cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dce9c537f7e77aa56a188a179f8634d"></a>

### [`00874488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874488.md) → [`008744e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008744e0.md) FUN_008744e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "008744f8",
      "incomplete_value": false,
      "site": "008744fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008744a0",
      "incomplete_value": false,
      "site": "008744a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "008744fc",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008744fc",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008744a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874488.md#insn-008744a0) · [`008744b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874488.md#insn-008744b4) · [`008744c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874488.md#insn-008744c8)
- 新版 `008744f8`（命令位置の公開資料なし） · `0087450c`（命令位置の公開資料なし） · `00874520`（命令位置の公開資料なし）

~~~diff
- 008744a0 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 008744a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008744a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008744a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008744f8 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 008744f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008744f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008744f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008744a0 bytes 08013391
+ 008744f8 bytes 08413691
- 008744b4 ["INT_ADD", "register:40f0:8", ["const:8744b4:8", "const:4:8"]]
- 008744b4 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087450c ["INT_ADD", "register:40f0:8", ["const:87450c:8", "const:4:8"]]
+ 0087450c ["CALL", null, ["callee:00c53da0:8"]]
- 008744b4 bytes 137e0f94
+ 0087450c bytes 257e0f94
- 008744c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008744c8 ["INT_ADD", "register:40f0:8", ["const:8744c8:8", "const:4:8"]]
- 008744c8 ["CALLIND", null, ["register:0:8"]]
+ 00874520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874520 ["INT_ADD", "register:40f0:8", ["const:874520:8", "const:4:8"]]
+ 00874520 ["CALLIND", null, ["register:0:8"]]
- 008744c8 bytes 00013fd6
+ 00874520 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf40ccf4537d950b1c430b2319c5cb5"></a>

### [`008744e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md) → [`0087453c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087453c.md) FUN_0087453c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874508",
      "incomplete_value": false,
      "site": "0087450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "00874564",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874564",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008744f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-008744f8) · [`00874508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-00874508) · [`00874528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008744e4.md#insn-00874528)
- 新版 `00874550`（命令位置の公開資料なし） · `00874560`（命令位置の公開資料なし） · `00874580`（命令位置の公開資料なし）

~~~diff
- 008744f8 ["INT_ADD", "register:40f0:8", ["const:8744f8:8", "const:4:8"]]
- 008744f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00874550 ["INT_ADD", "register:40f0:8", ["const:874550:8", "const:4:8"]]
+ 00874550 ["CALL", null, ["callee:00c57f60:8"]]
- 008744f8 bytes 668e0f94
+ 00874550 bytes 848e0f94
- 00874508 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00874508 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874508 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874508 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874560 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00874560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874508 bytes 29013391
+ 00874560 bytes 29413691
- 00874528 ["INT_ADD", "register:40f0:8", ["const:874528:8", "const:4:8"]]
- 00874528 ["CALL", null, ["callee:00c53d70:8"]]
+ 00874580 ["INT_ADD", "register:40f0:8", ["const:874580:8", "const:4:8"]]
+ 00874580 ["CALL", null, ["callee:00c53d70:8"]]
- 00874528 bytes ea7d0f94
+ 00874580 bytes fc7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3df060f98359767163085e3f390fcd"></a>

### [`0087453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md) → [`00874594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874594.md) FUN_00874594

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "0087459c",
      "incomplete_value": false,
      "site": "008745a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874544",
      "incomplete_value": false,
      "site": "00874548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "008745a0",
      "DATA",
      [
        "storage",
        "00c7fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008745a0",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md#insn-00874544) · [`0087456c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/0087453c.md#insn-0087456c)
- 新版 `0087459c`（命令位置の公開資料なし） · `008745c4`（命令位置の公開資料なし）

~~~diff
- 00874544 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00874544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087459c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 0087459c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087459c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087459c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874544 bytes 29013391
+ 0087459c bytes 29413691
- 0087456c ["INT_ADD", "register:40f0:8", ["const:87456c:8", "const:4:8"]]
- 0087456c ["CALL", null, ["callee:00c53d70:8"]]
+ 008745c4 ["INT_ADD", "register:40f0:8", ["const:8745c4:8", "const:4:8"]]
+ 008745c4 ["CALL", null, ["callee:00c53d70:8"]]
- 0087456c bytes d97d0f94
+ 008745c4 bytes eb7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25911c729d00b1fe7f5ece18b2ca2dfd"></a>

### [`008746e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md) → [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) FUN_00874740

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00874618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874618.md) · 呼出先 7件 [`00873c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873c50.md) [`00874a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a34.md) [`00874a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874a84.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00874670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874670.md) · 呼出先 7件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) [`00874a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a8c.md) [`00874adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874adc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008747dc",
      "incomplete_value": false,
      "site": "008747dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874784",
      "incomplete_value": false,
      "site": "00874784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008747f8",
      "incomplete_value": false,
      "site": "008747f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008747a0",
      "incomplete_value": false,
      "site": "008747a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "008747dc",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "008747f8",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "00874840",
      "READ",
      [
        "storage",
        "00c7fd50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008747dc",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ],
    [
      "008747f8",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ],
    [
      "00874840",
      "READ",
      [
        "storage",
        "00c7fe20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087476c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-0087476c) · [`00874774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-00874774) · [`0087478c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008746e8.md#insn-0087478c)
- 新版 `008747c4`（命令位置の公開資料なし） · `008747cc`（命令位置の公開資料なし） · `008747e4`（命令位置の公開資料なし）

~~~diff
- 0087476c ["INT_ADD", "register:40f0:8", ["const:87476c:8", "const:4:8"]]
- 0087476c ["CALL", null, ["callee:00c53d70:8"]]
+ 008747c4 ["INT_ADD", "register:40f0:8", ["const:8747c4:8", "const:4:8"]]
+ 008747c4 ["CALL", null, ["callee:00c53d70:8"]]
- 0087476c bytes 597d0f94
+ 008747c4 bytes 6b7d0f94
- 00874774 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00874774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008747cc ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008747cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008747cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008747cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874774 bytes 08c13491
+ 008747cc bytes 08013891
- 0087478c ["INT_ADD", "register:40f0:8", ["const:87478c:8", "const:4:8"]]
- 0087478c ["CALL", null, ["callee:00c53d70:8"]]
+ 008747e4 ["INT_ADD", "register:40f0:8", ["const:8747e4:8", "const:4:8"]]
+ 008747e4 ["CALL", null, ["callee:00c53d70:8"]]
- 0087478c bytes 517d0f94
+ 008747e4 bytes 637d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8db9aaffcf7e74e7f6718e1efd163c0"></a>

### [`008748e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md) → [`00874940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874940.md) FUN_00874940

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00874954",
      "incomplete_value": false,
      "site": "00874958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008748fc",
      "incomplete_value": false,
      "site": "00874900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "00874958",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874958",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008748fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-008748fc) · [`00874910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-00874910) · [`00874930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008748e8.md#insn-00874930)
- 新版 `00874954`（命令位置の公開資料なし） · `00874968`（命令位置の公開資料なし） · `00874988`（命令位置の公開資料なし）

~~~diff
- 008748fc ["COPY", "tmp:0:8", ["const:d30:8"]]
- 008748fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008748fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008748fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874954 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00874954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008748fc bytes 08c13491
+ 00874954 bytes 08013891
- 00874910 ["INT_ADD", "register:40f0:8", ["const:874910:8", "const:4:8"]]
- 00874910 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874968 ["INT_ADD", "register:40f0:8", ["const:874968:8", "const:4:8"]]
+ 00874968 ["CALL", null, ["callee:00c53da0:8"]]
- 00874910 bytes fc7c0f94
+ 00874968 bytes 0e7d0f94
- 00874930 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874930 ["INT_ADD", "register:40f0:8", ["const:874930:8", "const:4:8"]]
- 00874930 ["CALLIND", null, ["register:0:8"]]
+ 00874988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874988 ["INT_ADD", "register:40f0:8", ["const:874988:8", "const:4:8"]]
+ 00874988 ["CALLIND", null, ["register:0:8"]]
- 00874930 bytes 00013fd6
+ 00874988 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c34b7560e5c685cc4b98a9acfab7a261"></a>

### [`00874944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md) → [`0087499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087499c.md) FUN_0087499c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "008749b4",
      "incomplete_value": false,
      "site": "008749b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087495c",
      "incomplete_value": false,
      "site": "00874960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "008749b8",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008749b8",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087495c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-0087495c) · [`00874970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-00874970) · [`00874984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874944.md#insn-00874984)
- 新版 `008749b4`（命令位置の公開資料なし） · `008749c8`（命令位置の公開資料なし） · `008749dc`（命令位置の公開資料なし）

~~~diff
- 0087495c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0087495c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087495c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087495c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008749b4 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008749b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008749b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008749b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087495c bytes 08c13491
+ 008749b4 bytes 08013891
- 00874970 ["INT_ADD", "register:40f0:8", ["const:874970:8", "const:4:8"]]
- 00874970 ["CALL", null, ["callee:00c53da0:8"]]
+ 008749c8 ["INT_ADD", "register:40f0:8", ["const:8749c8:8", "const:4:8"]]
+ 008749c8 ["CALL", null, ["callee:00c53da0:8"]]
- 00874970 bytes e47c0f94
+ 008749c8 bytes f67c0f94
- 00874984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874984 ["INT_ADD", "register:40f0:8", ["const:874984:8", "const:4:8"]]
- 00874984 ["CALLIND", null, ["register:0:8"]]
+ 008749dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008749dc ["INT_ADD", "register:40f0:8", ["const:8749dc:8", "const:4:8"]]
+ 008749dc ["CALLIND", null, ["register:0:8"]]
- 00874984 bytes 00013fd6
+ 008749dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62fae96c0b201373c9223b939dd321f0"></a>

### [`008749a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md) → [`008749f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008749f8.md) FUN_008749f8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00874a1c",
      "incomplete_value": false,
      "site": "00874a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008749c4",
      "incomplete_value": false,
      "site": "008749c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "00874a20",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874a20",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008749b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749b4) · [`008749c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749c4) · [`008749e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749a0.md#insn-008749e4)
- 新版 `00874a0c`（命令位置の公開資料なし） · `00874a1c`（命令位置の公開資料なし） · `00874a3c`（命令位置の公開資料なし）

~~~diff
- 008749b4 ["INT_ADD", "register:40f0:8", ["const:8749b4:8", "const:4:8"]]
- 008749b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00874a0c ["INT_ADD", "register:40f0:8", ["const:874a0c:8", "const:4:8"]]
+ 00874a0c ["CALL", null, ["callee:00c57f60:8"]]
- 008749b4 bytes 378d0f94
+ 00874a0c bytes 558d0f94
- 008749c4 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 008749c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008749c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008749c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874a1c ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00874a1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008749c4 bytes 29c13491
+ 00874a1c bytes 29013891
- 008749e4 ["INT_ADD", "register:40f0:8", ["const:8749e4:8", "const:4:8"]]
- 008749e4 ["CALL", null, ["callee:00c53d70:8"]]
+ 00874a3c ["INT_ADD", "register:40f0:8", ["const:874a3c:8", "const:4:8"]]
+ 00874a3c ["CALL", null, ["callee:00c53d70:8"]]
- 008749e4 bytes bb7c0f94
+ 00874a3c bytes cd7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5df4e043a98089503eb5c16a9ea53f1"></a>

### [`008749f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md) → [`00874a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a50.md) FUN_00874a50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00874a58",
      "incomplete_value": false,
      "site": "00874a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874a00",
      "incomplete_value": false,
      "site": "00874a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "00874a5c",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874a5c",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md#insn-00874a00) · [`00874a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/008749f8.md#insn-00874a28)
- 新版 `00874a58`（命令位置の公開資料なし） · `00874a80`（命令位置の公開資料なし）

~~~diff
- 00874a00 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 00874a00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874a00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874a00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874a58 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00874a58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874a58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874a00 bytes 29c13491
+ 00874a58 bytes 29013891
- 00874a28 ["INT_ADD", "register:40f0:8", ["const:874a28:8", "const:4:8"]]
- 00874a28 ["CALL", null, ["callee:00c53d70:8"]]
+ 00874a80 ["INT_ADD", "register:40f0:8", ["const:874a80:8", "const:4:8"]]
+ 00874a80 ["CALL", null, ["callee:00c53d70:8"]]
- 00874a28 bytes aa7c0f94
+ 00874a80 bytes bc7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-832a44556da74b4f7456b0e0f0f4ef18"></a>

### [`00874b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md) → [`00874bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874bb4.md) FUN_00874bb4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00874bc8",
      "incomplete_value": false,
      "site": "00874bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874b70",
      "incomplete_value": false,
      "site": "00874b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00874bcc",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874bcc",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874b70) · [`00874b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874b84) · [`00874ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874b5c.md#insn-00874ba4)
- 新版 `00874bc8`（命令位置の公開資料なし） · `00874bdc`（命令位置の公開資料なし） · `00874bfc`（命令位置の公開資料なし）

~~~diff
- 00874b70 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00874b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874bc8 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00874bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874b70 bytes 08013791
+ 00874bc8 bytes 08413a91
- 00874b84 ["INT_ADD", "register:40f0:8", ["const:874b84:8", "const:4:8"]]
- 00874b84 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874bdc ["INT_ADD", "register:40f0:8", ["const:874bdc:8", "const:4:8"]]
+ 00874bdc ["CALL", null, ["callee:00c53da0:8"]]
- 00874b84 bytes 5f7c0f94
+ 00874bdc bytes 717c0f94
- 00874ba4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874ba4 ["INT_ADD", "register:40f0:8", ["const:874ba4:8", "const:4:8"]]
- 00874ba4 ["CALLIND", null, ["register:0:8"]]
+ 00874bfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874bfc ["INT_ADD", "register:40f0:8", ["const:874bfc:8", "const:4:8"]]
+ 00874bfc ["CALLIND", null, ["register:0:8"]]
- 00874ba4 bytes 00013fd6
+ 00874bfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a30fca4d00f322d847a46b242c9f1f"></a>

### [`00874bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md) → [`00874c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c10.md) FUN_00874c10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00874c28",
      "incomplete_value": false,
      "site": "00874c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874bd0",
      "incomplete_value": false,
      "site": "00874bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00874c2c",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874c2c",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874bd0) · [`00874be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874be4) · [`00874bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874bb8.md#insn-00874bf8)
- 新版 `00874c28`（命令位置の公開資料なし） · `00874c3c`（命令位置の公開資料なし） · `00874c50`（命令位置の公開資料なし）

~~~diff
- 00874bd0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00874bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874c28 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00874c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874bd0 bytes 08013791
+ 00874c28 bytes 08413a91
- 00874be4 ["INT_ADD", "register:40f0:8", ["const:874be4:8", "const:4:8"]]
- 00874be4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00874c3c ["INT_ADD", "register:40f0:8", ["const:874c3c:8", "const:4:8"]]
+ 00874c3c ["CALL", null, ["callee:00c53da0:8"]]
- 00874be4 bytes 477c0f94
+ 00874c3c bytes 597c0f94
- 00874bf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00874bf8 ["INT_ADD", "register:40f0:8", ["const:874bf8:8", "const:4:8"]]
- 00874bf8 ["CALLIND", null, ["register:0:8"]]
+ 00874c50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00874c50 ["INT_ADD", "register:40f0:8", ["const:874c50:8", "const:4:8"]]
+ 00874c50 ["CALLIND", null, ["register:0:8"]]
- 00874bf8 bytes 00013fd6
+ 00874c50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fbd5e3b2c38f8c5e691c26ba1430a57"></a>

### [`00874c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md) → [`00874c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c6c.md) FUN_00874c6c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00874c90",
      "incomplete_value": false,
      "site": "00874c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c38",
      "incomplete_value": false,
      "site": "00874c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00874c94",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874c94",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c28) · [`00874c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c38) · [`00874c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c14.md#insn-00874c58)
- 新版 `00874c80`（命令位置の公開資料なし） · `00874c90`（命令位置の公開資料なし） · `00874cb0`（命令位置の公開資料なし）

~~~diff
- 00874c28 ["INT_ADD", "register:40f0:8", ["const:874c28:8", "const:4:8"]]
- 00874c28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00874c80 ["INT_ADD", "register:40f0:8", ["const:874c80:8", "const:4:8"]]
+ 00874c80 ["CALL", null, ["callee:00c57f60:8"]]
- 00874c28 bytes 9a8c0f94
+ 00874c80 bytes b88c0f94
- 00874c38 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00874c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874c90 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00874c90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874c90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874c38 bytes 29013791
+ 00874c90 bytes 29413a91
- 00874c58 ["INT_ADD", "register:40f0:8", ["const:874c58:8", "const:4:8"]]
- 00874c58 ["CALL", null, ["callee:00c53d70:8"]]
+ 00874cb0 ["INT_ADD", "register:40f0:8", ["const:874cb0:8", "const:4:8"]]
+ 00874cb0 ["CALL", null, ["callee:00c53d70:8"]]
- 00874c58 bytes 1e7c0f94
+ 00874cb0 bytes 307c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11a38c197b73d66d6539b871c29503e3"></a>

### [`00874c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md) → [`00874cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874cc4.md) FUN_00874cc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00874ccc",
      "incomplete_value": false,
      "site": "00874cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c74",
      "incomplete_value": false,
      "site": "00874c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "00874cd0",
      "DATA",
      [
        "storage",
        "00c7fdc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874cd0",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md#insn-00874c74) · [`00874c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874c6c.md#insn-00874c9c)
- 新版 `00874ccc`（命令位置の公開資料なし） · `00874cf4`（命令位置の公開資料なし）

~~~diff
- 00874c74 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00874c74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874c74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874c74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00874ccc ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00874ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00874ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00874ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874c74 bytes 29013791
+ 00874ccc bytes 29413a91
- 00874c9c ["INT_ADD", "register:40f0:8", ["const:874c9c:8", "const:4:8"]]
- 00874c9c ["CALL", null, ["callee:00c53d70:8"]]
+ 00874cf4 ["INT_ADD", "register:40f0:8", ["const:874cf4:8", "const:4:8"]]
+ 00874cf4 ["CALL", null, ["callee:00c53d70:8"]]
- 00874c9c bytes 0d7c0f94
+ 00874cf4 bytes 1f7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf038d09129bb87042161c065415aa20"></a>

### [`00874d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md) → [`00874dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md) FUN_00874dd4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00874d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d48.md) · 呼出先 6件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00874da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874da0.md) · 呼出先 6件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 72.28% / 新版 72.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874e28",
      "incomplete_value": true,
      "site": "00874e30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00874dd0",
      "incomplete_value": true,
      "site": "00874dd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874e24",
      "incomplete_value": true,
      "site": "00874e34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:85f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874dcc",
      "incomplete_value": true,
      "site": "00874ddc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8ac:8"
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
      "definition_site": "00874e24",
      "incomplete_value": true,
      "site": "00874e34",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00874dcc",
      "incomplete_value": true,
      "site": "00874ddc",
      "value": [
        "LOAD",
        "16",
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
      "00874e24",
      "READ",
      [
        "storage",
        "002a48ac",
        null,
        "string"
      ]
    ],
    [
      "00874e24",
      "READ",
      [
        "storage",
        "002a48bc",
        null,
        "string"
      ]
    ],
    [
      "00874e28",
      "READ",
      [
        "storage",
        "002c31a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00874e24",
      "READ",
      [
        "storage",
        "002a485f",
        null,
        "string"
      ]
    ],
    [
      "00874e24",
      "READ",
      [
        "storage",
        "002a486f",
        null,
        "string"
      ]
    ],
    [
      "00874e28",
      "READ",
      [
        "storage",
        "002c31e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874e10) · [`00874e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874e88) · [`00874eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874d7c.md#insn-00874eb4)
- 新版 `00874e68`（命令位置の公開資料なし） · `00874ee0`（命令位置の公開資料なし） · `00874f0c`（命令位置の公開資料なし）

~~~diff
- 00874e10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:860:8"]]
- 00874e10 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00874e10 ["COPY", "register:5010:8", ["const:0:8"]]
- 00874e10 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00874e68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8a0:8"]]
+ 00874e68 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00874e68 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00874e68 ["COPY", "register:5018:8", ["const:0:8"]]
- 00874e10 bytes 0019c23d
+ 00874e68 bytes 0029c23d
- 00874e88 ["INT_ADD", "register:40f0:8", ["const:874e88:8", "const:4:8"]]
- 00874e88 ["CALL", null, ["callee:00597f0c:8"]]
+ 00874ee0 ["INT_ADD", "register:40f0:8", ["const:874ee0:8", "const:4:8"]]
+ 00874ee0 ["CALL", null, ["callee:00597f0c:8"]]
- 00874e88 bytes 118cf497
+ 00874ee0 bytes 0b8cf497
- 00874eb4 ["INT_ADD", "register:40f0:8", ["const:874eb4:8", "const:4:8"]]
- 00874eb4 ["CALL", null, ["callee:00a1a6f8:8"]]
+ 00874f0c ["INT_ADD", "register:40f0:8", ["const:874f0c:8", "const:4:8"]]
+ 00874f0c ["CALL", null, ["callee:00a1a6f8:8"]]
- 00874eb4 bytes fc950694
+ 00874f0c bytes fb950694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d951127f19cfd3178da5ab80e22ea13"></a>

### [`00874f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md) → [`00874fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874fec.md) FUN_00874fec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00875000",
      "incomplete_value": false,
      "site": "00875004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874fa8",
      "incomplete_value": false,
      "site": "00874fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00875004",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875004",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fa8) · [`00874fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fbc) · [`00874fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874f94.md#insn-00874fdc)
- 新版 `00875000`（命令位置の公開資料なし） · `00875014`（命令位置の公開資料なし） · `00875034`（命令位置の公開資料なし）

~~~diff
- 00874fa8 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00874fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875000 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00875000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874fa8 bytes 08013991
+ 00875000 bytes 08413c91
- 00874fbc ["INT_ADD", "register:40f0:8", ["const:874fbc:8", "const:4:8"]]
- 00874fbc ["CALL", null, ["callee:00c53da0:8"]]
+ 00875014 ["INT_ADD", "register:40f0:8", ["const:875014:8", "const:4:8"]]
+ 00875014 ["CALL", null, ["callee:00c53da0:8"]]
- 00874fbc bytes 517b0f94
+ 00875014 bytes 637b0f94
- 00874fdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00874fdc ["INT_ADD", "register:40f0:8", ["const:874fdc:8", "const:4:8"]]
- 00874fdc ["CALLIND", null, ["register:0:8"]]
+ 00875034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875034 ["INT_ADD", "register:40f0:8", ["const:875034:8", "const:4:8"]]
+ 00875034 ["CALLIND", null, ["register:0:8"]]
- 00874fdc bytes 00013fd6
+ 00875034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b96c0ce5b793d28d4084bf5491974f"></a>

### [`00874ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md) → [`00875048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875048.md) FUN_00875048

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00875060",
      "incomplete_value": false,
      "site": "00875064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875008",
      "incomplete_value": false,
      "site": "0087500c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00875064",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875064",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-00875008) · [`0087501c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-0087501c) · [`00875030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00874/00874ff0.md#insn-00875030)
- 新版 `00875060`（命令位置の公開資料なし） · `00875074`（命令位置の公開資料なし） · `00875088`（命令位置の公開資料なし）

~~~diff
- 00875008 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00875008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875060 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00875060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875008 bytes 08013991
+ 00875060 bytes 08413c91
- 0087501c ["INT_ADD", "register:40f0:8", ["const:87501c:8", "const:4:8"]]
- 0087501c ["CALL", null, ["callee:00c53da0:8"]]
+ 00875074 ["INT_ADD", "register:40f0:8", ["const:875074:8", "const:4:8"]]
+ 00875074 ["CALL", null, ["callee:00c53da0:8"]]
- 0087501c bytes 397b0f94
+ 00875074 bytes 4b7b0f94
- 00875030 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875030 ["INT_ADD", "register:40f0:8", ["const:875030:8", "const:4:8"]]
- 00875030 ["CALLIND", null, ["register:0:8"]]
+ 00875088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875088 ["INT_ADD", "register:40f0:8", ["const:875088:8", "const:4:8"]]
+ 00875088 ["CALLIND", null, ["register:0:8"]]
- 00875030 bytes 00013fd6
+ 00875088 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b25eb61ea72bcef300fd679d50c5eb6b"></a>

### [`0087504c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md) → [`008750a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750a4.md) FUN_008750a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "008750c8",
      "incomplete_value": false,
      "site": "008750cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875070",
      "incomplete_value": false,
      "site": "00875074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "008750cc",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008750cc",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875060) · [`00875070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875070) · [`00875090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/0087504c.md#insn-00875090)
- 新版 `008750b8`（命令位置の公開資料なし） · `008750c8`（命令位置の公開資料なし） · `008750e8`（命令位置の公開資料なし）

~~~diff
- 00875060 ["INT_ADD", "register:40f0:8", ["const:875060:8", "const:4:8"]]
- 00875060 ["CALL", null, ["callee:00c57f60:8"]]
+ 008750b8 ["INT_ADD", "register:40f0:8", ["const:8750b8:8", "const:4:8"]]
+ 008750b8 ["CALL", null, ["callee:00c57f60:8"]]
- 00875060 bytes 8c8b0f94
+ 008750b8 bytes aa8b0f94
- 00875070 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00875070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008750c8 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008750c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008750c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008750c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875070 bytes 29013991
+ 008750c8 bytes 29413c91
- 00875090 ["INT_ADD", "register:40f0:8", ["const:875090:8", "const:4:8"]]
- 00875090 ["CALL", null, ["callee:00c53d70:8"]]
+ 008750e8 ["INT_ADD", "register:40f0:8", ["const:8750e8:8", "const:4:8"]]
+ 008750e8 ["CALL", null, ["callee:00c53d70:8"]]
- 00875090 bytes 107b0f94
+ 008750e8 bytes 227b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b56ae8fa6c190d84b891199b4ef6a4d6"></a>

### [`008750a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md) → [`008750fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750fc.md) FUN_008750fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00875104",
      "incomplete_value": false,
      "site": "00875108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008750ac",
      "incomplete_value": false,
      "site": "008750b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00875108",
      "DATA",
      [
        "storage",
        "00c7fe40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875108",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008750ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md#insn-008750ac) · [`008750d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008750a4.md#insn-008750d4)
- 新版 `00875104`（命令位置の公開資料なし） · `0087512c`（命令位置の公開資料なし）

~~~diff
- 008750ac ["COPY", "tmp:0:8", ["const:e40:8"]]
- 008750ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008750ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008750ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875104 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00875104 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875104 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875104 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008750ac bytes 29013991
+ 00875104 bytes 29413c91
- 008750d4 ["INT_ADD", "register:40f0:8", ["const:8750d4:8", "const:4:8"]]
- 008750d4 ["CALL", null, ["callee:00c53d70:8"]]
+ 0087512c ["INT_ADD", "register:40f0:8", ["const:87512c:8", "const:4:8"]]
+ 0087512c ["CALL", null, ["callee:00c53d70:8"]]
- 008750d4 bytes ff7a0f94
+ 0087512c bytes 117b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b927a28ff1a36d33e2fee777f22f91f8"></a>

### [`008751b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md) → [`0087520c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md) FUN_0087520c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00875180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875180.md) · 呼出先 6件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`008751d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008751d8.md) · 呼出先 6件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 69.35% / 新版 69.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00875260",
      "incomplete_value": true,
      "site": "00875268",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00875208",
      "incomplete_value": true,
      "site": "00875210",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087525c",
      "incomplete_value": true,
      "site": "0087526c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:5ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875204",
      "incomplete_value": true,
      "site": "00875214",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:63a:8"
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
      "definition_site": "0087525c",
      "incomplete_value": true,
      "site": "0087526c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00875204",
      "incomplete_value": true,
      "site": "00875214",
      "value": [
        "LOAD",
        "16",
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
      "0087525c",
      "READ",
      [
        "storage",
        "002a363a",
        null,
        "string"
      ]
    ],
    [
      "0087525c",
      "READ",
      [
        "storage",
        "002a364a",
        null,
        "string"
      ]
    ],
    [
      "00875260",
      "READ",
      [
        "storage",
        "002c2f70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087525c",
      "READ",
      [
        "storage",
        "002a35ed",
        null,
        "string"
      ]
    ],
    [
      "0087525c",
      "READ",
      [
        "storage",
        "002a35fd",
        null,
        "string"
      ]
    ],
    [
      "00875260",
      "READ",
      [
        "storage",
        "002c2fb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087526c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md#insn-0087526c) · [`00875288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md#insn-00875288) · [`008752c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008751b4.md#insn-008752c0)
- 新版 `008752c4`（命令位置の公開資料なし） · `008752e0`（命令位置の公開資料なし） · `00875318`（命令位置の公開資料なし）

~~~diff
- 0087526c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:570:8"]]
- 0087526c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0087526c ["COPY", "register:5010:8", ["const:0:8"]]
- 0087526c ["COPY", "register:5018:8", ["const:0:8"]]
+ 008752c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b0:8"]]
+ 008752c4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 008752c4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 008752c4 ["COPY", "register:5018:8", ["const:0:8"]]
- 0087526c bytes 205dc13d
+ 008752c4 bytes 206dc13d
- 00875288 ["INT_ADD", "register:40f0:8", ["const:875288:8", "const:4:8"]]
- 00875288 ["CALL", null, ["callee:00597f0c:8"]]
+ 008752e0 ["INT_ADD", "register:40f0:8", ["const:8752e0:8", "const:4:8"]]
+ 008752e0 ["CALL", null, ["callee:00597f0c:8"]]
- 00875288 bytes 118bf497
+ 008752e0 bytes 0b8bf497
- 008752c0 ["INT_ADD", "register:40f0:8", ["const:8752c0:8", "const:4:8"]]
- 008752c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00875318 ["INT_ADD", "register:40f0:8", ["const:875318:8", "const:4:8"]]
+ 00875318 ["CALL", null, ["callee:00c57f60:8"]]
- 008752c0 bytes f48a0f94
+ 00875318 bytes 128b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e417afbe83fabd86d8ad5582f7bb7b"></a>

### [`008759c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md) → [`00875a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a18.md) FUN_00875a18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00875a3c",
      "incomplete_value": false,
      "site": "00875a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008759e4",
      "incomplete_value": false,
      "site": "008759e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
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
      "00875a3c",
      "DATA",
      [
        "storage",
        "00c7fec0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a3c",
      "DATA",
      [
        "storage",
        "00c7ff90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008759d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md#insn-008759d4) · [`008759e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759c0.md#insn-008759e0)
- 新版 `00875a2c`（命令位置の公開資料なし） · `00875a38`（命令位置の公開資料なし）

~~~diff
- 008759d4 ["INT_ADD", "register:40f0:8", ["const:8759d4:8", "const:4:8"]]
- 008759d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00875a2c ["INT_ADD", "register:40f0:8", ["const:875a2c:8", "const:4:8"]]
+ 00875a2c ["CALL", null, ["callee:00c57f60:8"]]
- 008759d4 bytes 2f890f94
+ 00875a2c bytes 4d890f94
- 008759e0 ["COPY", "tmp:0:8", ["const:ec0:8"]]
- 008759e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008759e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008759e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875a38 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00875a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008759e0 bytes 08013b91
+ 00875a38 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd888458dfb751d19842b98bfdce6307"></a>

### [`008759f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759f4.md) → [`00875a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a4c.md) FUN_00875a4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00875a58",
      "incomplete_value": false,
      "site": "00875a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875a00",
      "incomplete_value": false,
      "site": "00875a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
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
      "00875a58",
      "DATA",
      [
        "storage",
        "00c7fec0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a58",
      "DATA",
      [
        "storage",
        "00c7ff90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008759fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/008759f4.md#insn-008759fc)
- 新版 `00875a54`（命令位置の公開資料なし）

~~~diff
- 008759fc ["COPY", "tmp:0:8", ["const:ec0:8"]]
- 008759fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008759fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008759fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875a54 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00875a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008759fc bytes 29013b91
+ 00875a54 bytes 29413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62d6a5d88269c8ea1d64d506e78e28f"></a>

### [`00875a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md) → [`00875ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ab0.md) FUN_00875ab0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00875ac4",
      "incomplete_value": false,
      "site": "00875ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875a6c",
      "incomplete_value": false,
      "site": "00875a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "00875ac8",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875ac8",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875a68) · [`00875a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875a6c) · [`00875a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875a58.md#insn-00875a80)
- 新版 `00875ac0`（命令位置の公開資料なし） · `00875ac4`（命令位置の公開資料なし） · `00875ad8`（命令位置の公開資料なし）

~~~diff
- 00875a68 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875ac0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875a68 bytes 482000d0
+ 00875ac0 bytes 482000f0
- 00875a6c ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00875a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875ac4 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00875ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875a6c bytes 08013d91
+ 00875ac4 bytes 08410091
- 00875a80 ["INT_ADD", "register:40f0:8", ["const:875a80:8", "const:4:8"]]
- 00875a80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875ad8 ["INT_ADD", "register:40f0:8", ["const:875ad8:8", "const:4:8"]]
+ 00875ad8 ["CALL", null, ["callee:00c53da0:8"]]
- 00875a80 bytes a0780f94
+ 00875ad8 bytes b2780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9946139febe03d039e12905a87a38fde"></a>

### [`00875ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md) → [`00875b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b0c.md) FUN_00875b0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00875b24",
      "incomplete_value": false,
      "site": "00875b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875acc",
      "incomplete_value": false,
      "site": "00875ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00875b28",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b28",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875ac8) · [`00875acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875acc) · [`00875ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ab4.md#insn-00875ae0)
- 新版 `00875b20`（命令位置の公開資料なし） · `00875b24`（命令位置の公開資料なし） · `00875b38`（命令位置の公開資料なし）

~~~diff
- 00875ac8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875b20 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875ac8 bytes 482000d0
+ 00875b20 bytes 482000f0
- 00875acc ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00875acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875b24 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00875b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875acc bytes 08013d91
+ 00875b24 bytes 08410091
- 00875ae0 ["INT_ADD", "register:40f0:8", ["const:875ae0:8", "const:4:8"]]
- 00875ae0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875b38 ["INT_ADD", "register:40f0:8", ["const:875b38:8", "const:4:8"]]
+ 00875b38 ["CALL", null, ["callee:00c53da0:8"]]
- 00875ae0 bytes 88780f94
+ 00875b38 bytes 9a780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-397381134cd028265aca3ffb3e2d9bd0"></a>

### [`00875b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md) → [`00875b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b68.md) FUN_00875b68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00875b8c",
      "incomplete_value": false,
      "site": "00875b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875b34",
      "incomplete_value": false,
      "site": "00875b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "00875b90",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b90",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b24) · [`00875b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b30) · [`00875b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b10.md#insn-00875b34)
- 新版 `00875b7c`（命令位置の公開資料なし） · `00875b88`（命令位置の公開資料なし） · `00875b8c`（命令位置の公開資料なし）

~~~diff
- 00875b24 ["INT_ADD", "register:40f0:8", ["const:875b24:8", "const:4:8"]]
- 00875b24 ["CALL", null, ["callee:00c57f60:8"]]
+ 00875b7c ["INT_ADD", "register:40f0:8", ["const:875b7c:8", "const:4:8"]]
+ 00875b7c ["CALL", null, ["callee:00c57f60:8"]]
- 00875b24 bytes db880f94
+ 00875b7c bytes f9880f94
- 00875b30 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875b88 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00875b30 bytes 492000d0
+ 00875b88 bytes 492000f0
- 00875b34 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00875b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875b8c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00875b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875b34 bytes 29013d91
+ 00875b8c bytes 29410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-820bf5ed60dd6e243358cb8d0fde116a"></a>

### [`00875b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md) → [`00875bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bc0.md) FUN_00875bc0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00875bc8",
      "incomplete_value": false,
      "site": "00875bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875b70",
      "incomplete_value": false,
      "site": "00875b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "00875bcc",
      "DATA",
      [
        "storage",
        "00c7ff40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875bcc",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md#insn-00875b6c) · [`00875b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md#insn-00875b70) · [`00875b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875b68.md#insn-00875b98)
- 新版 `00875bc4`（命令位置の公開資料なし） · `00875bc8`（命令位置の公開資料なし） · `00875bf0`（命令位置の公開資料なし）

~~~diff
- 00875b6c ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875bc4 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00875b6c bytes 492000d0
+ 00875bc4 bytes 492000f0
- 00875b70 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00875b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875bc8 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00875bc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875bc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875bc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875b70 bytes 29013d91
+ 00875bc8 bytes 29410091
- 00875b98 ["INT_ADD", "register:40f0:8", ["const:875b98:8", "const:4:8"]]
- 00875b98 ["CALL", null, ["callee:00c53d70:8"]]
+ 00875bf0 ["INT_ADD", "register:40f0:8", ["const:875bf0:8", "const:4:8"]]
+ 00875bf0 ["CALL", null, ["callee:00c53d70:8"]]
- 00875b98 bytes 4e780f94
+ 00875bf0 bytes 60780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12ee11661e869a372959cb85c1f0c9f1"></a>

### [`00875c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md) → [`00875cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md) FUN_00875cd0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00875c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c44.md) · 呼出先 6件 [`00875fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875fb8.md) [`00876008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876008.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00875c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c9c.md) · 呼出先 6件 [`00876010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876010.md) [`00876060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00875d60",
      "incomplete_value": false,
      "site": "00875d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875d08",
      "incomplete_value": false,
      "site": "00875d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "definition_site": "00875d7c",
      "incomplete_value": false,
      "site": "00875d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875d24",
      "incomplete_value": false,
      "site": "00875d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "00875d10",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "qword"
      ]
    ],
    [
      "00875d60",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ],
    [
      "00875d7c",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875d10",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "dword"
      ]
    ],
    [
      "00875d60",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ],
    [
      "00875d7c",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cd0) · [`00875cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cf0) · [`00875cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875c78.md#insn-00875cf4)
- 新版 `00875d28`（命令位置の公開資料なし） · `00875d48`（命令位置の公開資料なし） · `00875d4c`（命令位置の公開資料なし）

~~~diff
- 00875cd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875cd0 ["INT_ADD", "register:40f0:8", ["const:875cd0:8", "const:4:8"]]
- 00875cd0 ["CALLIND", null, ["register:0:8"]]
+ 00875d28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875d28 ["INT_ADD", "register:40f0:8", ["const:875d28:8", "const:4:8"]]
+ 00875d28 ["CALLIND", null, ["register:0:8"]]
- 00875cd0 bytes 00013fd6
+ 00875d28 bytes 00013fd6
- 00875cf0 ["INT_ADD", "register:40f0:8", ["const:875cf0:8", "const:4:8"]]
- 00875cf0 ["CALL", null, ["callee:00c53d70:8"]]
+ 00875d48 ["INT_ADD", "register:40f0:8", ["const:875d48:8", "const:4:8"]]
+ 00875d48 ["CALL", null, ["callee:00c53d70:8"]]
- 00875cf0 bytes f8770f94
+ 00875d48 bytes 0a780f94
- 00875cf4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875d4c ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875cf4 bytes 482000d0
+ 00875d4c bytes 482000f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9914b11b19f87e4ecf2a391a2e2158b"></a>

### [`00875e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md) → [`00875ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ec4.md) FUN_00875ec4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00875ed8",
      "incomplete_value": false,
      "site": "00875edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875e80",
      "incomplete_value": false,
      "site": "00875e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "00875edc",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875edc",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875e7c) · [`00875e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875e80) · [`00875e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875e6c.md#insn-00875e94)
- 新版 `00875ed4`（命令位置の公開資料なし） · `00875ed8`（命令位置の公開資料なし） · `00875eec`（命令位置の公開資料なし）

~~~diff
- 00875e7c ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875ed4 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875e7c bytes 482000d0
+ 00875ed4 bytes 482000f0
- 00875e80 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00875e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875ed8 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00875ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875e80 bytes 08c13e91
+ 00875ed8 bytes 08010291
- 00875e94 ["INT_ADD", "register:40f0:8", ["const:875e94:8", "const:4:8"]]
- 00875e94 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875eec ["INT_ADD", "register:40f0:8", ["const:875eec:8", "const:4:8"]]
+ 00875eec ["CALL", null, ["callee:00c53da0:8"]]
- 00875e94 bytes 9b770f94
+ 00875eec bytes ad770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae7f8b27c347638ed862aaa4b6339f2"></a>

### [`00875ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md) → [`00875f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f20.md) FUN_00875f20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00875f38",
      "incomplete_value": false,
      "site": "00875f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875ee0",
      "incomplete_value": false,
      "site": "00875ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "00875f3c",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875f3c",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875edc) · [`00875ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875ee0) · [`00875ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875ec8.md#insn-00875ef4)
- 新版 `00875f34`（命令位置の公開資料なし） · `00875f38`（命令位置の公開資料なし） · `00875f4c`（命令位置の公開資料なし）

~~~diff
- 00875edc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875f34 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875edc bytes 482000d0
+ 00875f34 bytes 482000f0
- 00875ee0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00875ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875f38 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00875f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875ee0 bytes 08c13e91
+ 00875f38 bytes 08010291
- 00875ef4 ["INT_ADD", "register:40f0:8", ["const:875ef4:8", "const:4:8"]]
- 00875ef4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00875f4c ["INT_ADD", "register:40f0:8", ["const:875f4c:8", "const:4:8"]]
+ 00875f4c ["CALL", null, ["callee:00c53da0:8"]]
- 00875ef4 bytes 83770f94
+ 00875f4c bytes 95770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7ddff1990b25677d6d60eab8ac9930"></a>

### [`00875f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md) → [`00875f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f7c.md) FUN_00875f7c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00875fa0",
      "incomplete_value": false,
      "site": "00875fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875f48",
      "incomplete_value": false,
      "site": "00875f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "00875fa4",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875fa4",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f38) · [`00875f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f44) · [`00875f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f24.md#insn-00875f48)
- 新版 `00875f90`（命令位置の公開資料なし） · `00875f9c`（命令位置の公開資料なし） · `00875fa0`（命令位置の公開資料なし）

~~~diff
- 00875f38 ["INT_ADD", "register:40f0:8", ["const:875f38:8", "const:4:8"]]
- 00875f38 ["CALL", null, ["callee:00c57f60:8"]]
+ 00875f90 ["INT_ADD", "register:40f0:8", ["const:875f90:8", "const:4:8"]]
+ 00875f90 ["CALL", null, ["callee:00c57f60:8"]]
- 00875f38 bytes d6870f94
+ 00875f90 bytes f4870f94
- 00875f44 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875f9c ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00875f44 bytes 492000d0
+ 00875f9c bytes 492000f0
- 00875f48 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00875f48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875f48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875f48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875fa0 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00875fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875f48 bytes 29c13e91
+ 00875fa0 bytes 29010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7a40aedede0af42169ffa37800d3443"></a>

### [`00875f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md) → [`00875fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875fd4.md) FUN_00875fd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00875fdc",
      "incomplete_value": false,
      "site": "00875fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875f84",
      "incomplete_value": false,
      "site": "00875f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      "00875fe0",
      "DATA",
      [
        "storage",
        "00c7ffb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875fe0",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md#insn-00875f80) · [`00875f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md#insn-00875f84) · [`00875fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00875/00875f7c.md#insn-00875fac)
- 新版 `00875fd8`（命令位置の公開資料なし） · `00875fdc`（命令位置の公開資料なし） · `00876004`（命令位置の公開資料なし）

~~~diff
- 00875f80 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875fd8 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00875f80 bytes 492000d0
+ 00875fd8 bytes 492000f0
- 00875f84 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00875f84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875f84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875f84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875fdc ["COPY", "tmp:0:8", ["const:80:8"]]
+ 00875fdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875fdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875fdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875f84 bytes 29c13e91
+ 00875fdc bytes 29010291
- 00875fac ["INT_ADD", "register:40f0:8", ["const:875fac:8", "const:4:8"]]
- 00875fac ["CALL", null, ["callee:00c53d70:8"]]
+ 00876004 ["INT_ADD", "register:40f0:8", ["const:876004:8", "const:4:8"]]
+ 00876004 ["CALL", null, ["callee:00c53d70:8"]]
- 00875fac bytes 49770f94
+ 00876004 bytes 5b770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f741b5927cb4f499ae473b3af06a3387"></a>

### [`008760e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760e0.md) → [`00876138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876138.md) FUN_00876138

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0087613c",
      "incomplete_value": false,
      "site": "00876140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008760e4",
      "incomplete_value": false,
      "site": "008760e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "00876140",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00876140",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008760e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760e0.md#insn-008760e4)
- 新版 `0087613c`（命令位置の公開資料なし）

~~~diff
- 008760e4 ["COPY", "tmp:0:8", ["const:40:8"]]
- 008760e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008760e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008760e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087613c ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0087613c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087613c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087613c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008760e4 bytes 08010191
+ 0087613c bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1f8bb9c2e283cf7e969514f3913cfc0"></a>

### [`008760f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md) → [`00876148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876148.md) FUN_00876148

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00876158",
      "incomplete_value": false,
      "site": "00876160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876100",
      "incomplete_value": false,
      "site": "00876108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "00876160",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00876160",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md#insn-00876100) · [`0087610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008760f0.md#insn-0087610c)
- 新版 `00876158`（命令位置の公開資料なし） · `00876164`（命令位置の公開資料なし）

~~~diff
- 00876100 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00876100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00876100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00876100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876158 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00876158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00876100 bytes 08010191
+ 00876158 bytes 08410491
- 0087610c ["INT_ADD", "register:40f0:8", ["const:87610c:8", "const:4:8"]]
- 0087610c ["CALL", null, ["callee:00c57f70:8"]]
+ 00876164 ["INT_ADD", "register:40f0:8", ["const:876164:8", "const:4:8"]]
+ 00876164 ["CALL", null, ["callee:00c57f70:8"]]
- 0087610c bytes 65870f94
+ 00876164 bytes 83870f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c13c7ee71f5c34d919902dbf5752018"></a>

### [`00876130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md) → [`00876188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md) FUN_00876188

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 2件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008761cc",
      "incomplete_value": false,
      "site": "008761cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876174",
      "incomplete_value": false,
      "site": "00876174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "definition_site": "00876234",
      "incomplete_value": true,
      "site": "00876234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008761dc",
      "incomplete_value": true,
      "site": "008761dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087624c",
      "incomplete_value": true,
      "site": "0087624c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008761f4",
      "incomplete_value": true,
      "site": "008761f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
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
      "008761cc",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ],
    [
      "008761ec",
      "PARAM",
      [
        "storage",
        "002ef75a",
        null,
        "string"
      ]
    ],
    [
      "00876200",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008761cc",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ],
    [
      "008761ec",
      "PARAM",
      [
        "storage",
        "002ef79a",
        null,
        "string"
      ]
    ],
    [
      "00876200",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087619c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-0087619c) · [`008761a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-008761a0) · [`00876218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md#insn-00876218)
- 新版 `008761f4`（命令位置の公開資料なし） · `008761f8`（命令位置の公開資料なし） · `00876270`（命令位置の公開資料なし）

~~~diff
- 0087619c ["INT_ADD", "register:40f0:8", ["const:87619c:8", "const:4:8"]]
- 0087619c ["CALL", null, ["callee:00c58260:8"]]
+ 008761f4 ["INT_ADD", "register:40f0:8", ["const:8761f4:8", "const:4:8"]]
+ 008761f4 ["CALL", null, ["callee:00c58260:8"]]
- 0087619c bytes fd870f94
+ 008761f4 bytes 1b880f94
- 008761a0 ["COPY", "register:40d0:8", ["const:ca4000:8"]]
+ 008761f8 ["COPY", "register:40d0:8", ["const:ca5000:8"]]
- 008761a0 bytes 7a2100d0
+ 008761f8 bytes 7a2100f0
- 00876218 ["INT_ADD", "register:40f0:8", ["const:876218:8", "const:4:8"]]
- 00876218 ["CALL", null, ["callee:0047e64c:8"]]
+ 00876270 ["INT_ADD", "register:40f0:8", ["const:876270:8", "const:4:8"]]
+ 00876270 ["CALL", null, ["callee:0047e64c:8"]]
- 00876218 bytes fd20f097
+ 00876270 bytes f720f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c236df44f6b5c695ef1a46424d52d2c6"></a>

### [`0087652c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md) → [`00876584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876584.md) FUN_00876584

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087659c",
      "incomplete_value": false,
      "site": "008765a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876544",
      "incomplete_value": false,
      "site": "00876548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "008765a0",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008765a0",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008765a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-008765a0) · [`00876544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-00876544) · [`00876554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/0087652c.md#insn-00876554)
- 新版 `008765f8`（命令位置の公開資料なし） · `0087659c`（命令位置の公開資料なし） · `008765ac`（命令位置の公開資料なし）

~~~diff
- 008765a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008765a0 ["INT_ADD", "register:40f0:8", ["const:8765a0:8", "const:4:8"]]
- 008765a0 ["CALLIND", null, ["register:0:8"]]
+ 008765f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008765f8 ["INT_ADD", "register:40f0:8", ["const:8765f8:8", "const:4:8"]]
+ 008765f8 ["CALLIND", null, ["register:0:8"]]
- 008765a0 bytes 00013fd6
+ 008765f8 bytes 00013fd6
- 00876544 ["COPY", "tmp:0:8", ["const:90:8"]]
- 00876544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087659c ["COPY", "tmp:0:8", ["const:160:8"]]
+ 0087659c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087659c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087659c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876544 bytes 29410291
+ 0087659c bytes 29810591
- 00876554 ["INT_ADD", "register:40f0:8", ["const:876554:8", "const:4:8"]]
- 00876554 ["CALL", null, ["callee:00c57f80:8"]]
+ 008765ac ["INT_ADD", "register:40f0:8", ["const:8765ac:8", "const:4:8"]]
+ 008765ac ["CALL", null, ["callee:00c57f80:8"]]
- 00876554 bytes 57860f94
+ 008765ac bytes 75860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cbdd956c0aa9c4808cbff5e8590a47c"></a>

### [`008765d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md) → [`00876630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876630.md) FUN_00876630

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00876648",
      "incomplete_value": false,
      "site": "0087664c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008765f0",
      "incomplete_value": false,
      "site": "008765f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "0087664c",
      "DATA",
      [
        "storage",
        "00c80090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087664c",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008765f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-008765f0) · [`00876600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-00876600) · [`00876614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008765d8.md#insn-00876614)
- 新版 `00876648`（命令位置の公開資料なし） · `00876658`（命令位置の公開資料なし） · `0087666c`（命令位置の公開資料なし）

~~~diff
- 008765f0 ["COPY", "tmp:0:8", ["const:90:8"]]
- 008765f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008765f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008765f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876648 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 00876648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008765f0 bytes 29410291
+ 00876648 bytes 29810591
- 00876600 ["INT_ADD", "register:40f0:8", ["const:876600:8", "const:4:8"]]
- 00876600 ["CALL", null, ["callee:00c57f80:8"]]
+ 00876658 ["INT_ADD", "register:40f0:8", ["const:876658:8", "const:4:8"]]
+ 00876658 ["CALL", null, ["callee:00c57f80:8"]]
- 00876600 bytes 2c860f94
+ 00876658 bytes 4a860f94
- 00876614 ["INT_ADD", "register:40f0:8", ["const:876614:8", "const:4:8"]]
- 00876614 ["CALL", null, ["callee:00c53da0:8"]]
+ 0087666c ["INT_ADD", "register:40f0:8", ["const:87666c:8", "const:4:8"]]
+ 0087666c ["CALL", null, ["callee:00c53da0:8"]]
- 00876614 bytes bb750f94
+ 0087666c bytes cd750f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75b4390e4946651b5894aa9f98c9074"></a>

### [`008766a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md) → [`008766fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008766fc.md) FUN_008766fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00876720",
      "incomplete_value": false,
      "site": "00876720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008766c8",
      "incomplete_value": false,
      "site": "008766c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "00876720",
      "DATA",
      [
        "storage",
        "00c800f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876720",
      "DATA",
      [
        "storage",
        "00c801c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008766b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md#insn-008766b8) · [`008766c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766a4.md#insn-008766c4)
- 新版 `00876710`（命令位置の公開資料なし） · `0087671c`（命令位置の公開資料なし）

~~~diff
- 008766b8 ["INT_ADD", "register:40f0:8", ["const:8766b8:8", "const:4:8"]]
- 008766b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00876710 ["INT_ADD", "register:40f0:8", ["const:876710:8", "const:4:8"]]
+ 00876710 ["CALL", null, ["callee:00c57f60:8"]]
- 008766b8 bytes f6850f94
+ 00876710 bytes 14860f94
- 008766c4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008766c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008766c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008766c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087671c ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 0087671c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087671c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087671c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008766c4 bytes 08c10391
+ 0087671c bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77297092eb45708ed7ee02f04b3e0f4d"></a>

### [`008766d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766d8.md) → [`00876730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876730.md) FUN_00876730

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0087673c",
      "incomplete_value": false,
      "site": "0087673c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008766e4",
      "incomplete_value": false,
      "site": "008766e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087673c",
      "DATA",
      [
        "storage",
        "00c800f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087673c",
      "DATA",
      [
        "storage",
        "00c801c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008766e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766d8.md#insn-008766e0)
- 新版 `00876738`（命令位置の公開資料なし）

~~~diff
- 008766e0 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008766e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008766e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008766e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876738 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00876738 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876738 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876738 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008766e0 bytes 29c10391
+ 00876738 bytes 29010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54427108dcecbb9045d5fe9403939e07"></a>

### [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) → [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) FUN_0087674c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004953d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md) [`00873088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873088.md) [`00873098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873098.md) [`00876120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876120.md) [`00876130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876130.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00495414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md) [`008730e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730e0.md) [`008730f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md) [`00876178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876178.md) [`00876188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008767f8",
      "incomplete_value": false,
      "site": "00876804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008767a0",
      "incomplete_value": false,
      "site": "008767ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "00876870",
      "incomplete_value": false,
      "site": "0087687c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876818",
      "incomplete_value": false,
      "site": "00876824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "00876804",
      "DATA",
      [
        "storage",
        "00c7fc10",
        null,
        "pointer"
      ]
    ],
    [
      "00876850",
      "READ",
      [
        "storage",
        "00c7fc20",
        null,
        "undefined *"
      ]
    ],
    [
      "0087687c",
      "DATA",
      [
        "storage",
        "00c80040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00876804",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ],
    [
      "00876850",
      "READ",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "0087687c",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-00876754) · [`008767cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-008767cc) · [`00876804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md#insn-00876804)
- 新版 `008767ac`（命令位置の公開資料なし） · `00876824`（命令位置の公開資料なし） · `0087685c`（命令位置の公開資料なし）

~~~diff
- 00876754 ["INT_ADD", "register:40f0:8", ["const:876754:8", "const:4:8"]]
- 00876754 ["CALL", null, ["callee:00c53d70:8"]]
+ 008767ac ["INT_ADD", "register:40f0:8", ["const:8767ac:8", "const:4:8"]]
+ 008767ac ["CALL", null, ["callee:00c53d70:8"]]
- 00876754 bytes 5f750f94
+ 008767ac bytes 71750f94
- 008767cc ["INT_ADD", "register:40f0:8", ["const:8767cc:8", "const:4:8"]]
- 008767cc ["CALL", null, ["callee:00c53d70:8"]]
+ 00876824 ["INT_ADD", "register:40f0:8", ["const:876824:8", "const:4:8"]]
+ 00876824 ["CALL", null, ["callee:00c53d70:8"]]
- 008767cc bytes 41750f94
+ 00876824 bytes 53750f94
- 00876804 ["INT_ADD", "register:40f0:8", ["const:876804:8", "const:4:8"]]
- 00876804 ["CALL", null, ["callee:00c57f50:8"]]
+ 0087685c ["INT_ADD", "register:40f0:8", ["const:87685c:8", "const:4:8"]]
+ 0087685c ["CALL", null, ["callee:00c57f50:8"]]
- 00876804 bytes 9f850f94
+ 0087685c bytes bd850f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1d097120198b01739b51c2e006009b"></a>

### [`008769c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md) → [`00876a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a18.md) FUN_00876a18

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00876a3c",
      "incomplete_value": false,
      "site": "00876a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008769e4",
      "incomplete_value": false,
      "site": "008769e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "00876a3c",
      "DATA",
      [
        "storage",
        "00c80170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876a3c",
      "DATA",
      [
        "storage",
        "00c80240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008769d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md#insn-008769d4) · [`008769e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769c0.md#insn-008769e0)
- 新版 `00876a2c`（命令位置の公開資料なし） · `00876a38`（命令位置の公開資料なし）

~~~diff
- 008769d4 ["INT_ADD", "register:40f0:8", ["const:8769d4:8", "const:4:8"]]
- 008769d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00876a2c ["INT_ADD", "register:40f0:8", ["const:876a2c:8", "const:4:8"]]
+ 00876a2c ["CALL", null, ["callee:00c57f60:8"]]
- 008769d4 bytes 2f850f94
+ 00876a2c bytes 4d850f94
- 008769e0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 008769e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008769e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008769e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876a38 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00876a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008769e0 bytes 08c10591
+ 00876a38 bytes 08010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f529757f8c426bac61373b67bad16365"></a>

### [`008769f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769f4.md) → [`00876a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a4c.md) FUN_00876a4c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00876a58",
      "incomplete_value": false,
      "site": "00876a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876a00",
      "incomplete_value": false,
      "site": "00876a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00876a58",
      "DATA",
      [
        "storage",
        "00c80170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876a58",
      "DATA",
      [
        "storage",
        "00c80240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008769fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008769f4.md#insn-008769fc)
- 新版 `00876a54`（命令位置の公開資料なし）

~~~diff
- 008769fc ["COPY", "tmp:0:8", ["const:170:8"]]
- 008769fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008769fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008769fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876a54 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00876a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008769fc bytes 29c10591
+ 00876a54 bytes 29010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7af867803569079255b36b997d2dd7"></a>

### [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) → [`00876a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md) FUN_00876a68

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md) [`0044f43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md) [`0044f47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "site": "00876ab0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876a58",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00876b24",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876acc",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "00876ab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00876b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00876ab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00876b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876a58) · [`00876acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876acc) · [`00876a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md#insn-00876a54)
- 新版 `00876ab0`（命令位置の公開資料なし） · `00876b24`（命令位置の公開資料なし） · `00876aac`（命令位置の公開資料なし）

~~~diff
- 00876a58 ["INT_ADD", "register:40f0:8", ["const:876a58:8", "const:4:8"]]
- 00876a58 ["CALL", null, ["ram:47acf4:8"]]
+ 00876ab0 ["INT_ADD", "register:40f0:8", ["const:876ab0:8", "const:4:8"]]
+ 00876ab0 ["CALL", null, ["ram:47ad34:8"]]
- 00876a58 bytes a710f097
+ 00876ab0 bytes a110f097
- 00876acc ["INT_ADD", "register:40f0:8", ["const:876acc:8", "const:4:8"]]
- 00876acc ["CALL", null, ["ram:48ccf8:8"]]
+ 00876b24 ["INT_ADD", "register:40f0:8", ["const:876b24:8", "const:4:8"]]
+ 00876b24 ["CALL", null, ["ram:48cd38:8"]]
- 00876acc bytes 8b58f097
+ 00876b24 bytes 8558f097
- 00876a54 ["INT_ADD", "register:40f0:8", ["const:876a54:8", "const:4:8"]]
- 00876a54 ["CALL", null, ["callee:008b91d0:8"]]
+ 00876aac ["INT_ADD", "register:40f0:8", ["const:876aac:8", "const:4:8"]]
+ 00876aac ["CALL", null, ["callee:008b91d0:8"]]
- 00876a54 bytes c9090194
+ 00876aac bytes c9090194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb79e977af949c9e70df1120a15658d"></a>

### [`00876b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md) → [`00876bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876bcc.md) _INIT_157

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00876c08",
      "incomplete_value": true,
      "site": "00876c24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00876bb0",
      "incomplete_value": true,
      "site": "00876bcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00876c2c",
      "incomplete_value": true,
      "site": "00876c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00876bd4",
      "incomplete_value": true,
      "site": "00876bf0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00876c4c",
      "incomplete_value": true,
      "site": "00876c68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00876bf4",
      "incomplete_value": true,
      "site": "00876c10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00876c08",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00876c2c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00876c4c",
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
      "00876c08",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00876c2c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00876c4c",
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

- 旧版 [`00876c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876c48) · [`00876c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876c68) · [`00876cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876b74.md#insn-00876cd4)
- 新版 `00876ca0`（命令位置の公開資料なし） · `00876cc0`（命令位置の公開資料なし） · `00876d2c`（命令位置の公開資料なし）

~~~diff
- 00876c48 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 00876c48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876c48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876c48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876ca0 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00876ca0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876ca0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876ca0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876c48 bytes 29753d91
+ 00876ca0 bytes 29413c91
- 00876c68 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00876c68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876c68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876c68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876cc0 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00876cc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876cc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876cc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876c68 bytes 29253c91
+ 00876cc0 bytes 29f13a91
- 00876cd4 ["INT_ADD", "register:40f0:8", ["const:876cd4:8", "const:4:8"]]
- 00876cd4 ["CALL", null, ["callee:0043b838:8"]]
+ 00876d2c ["INT_ADD", "register:40f0:8", ["const:876d2c:8", "const:4:8"]]
+ 00876d2c ["CALL", null, ["callee:0043b838:8"]]
- 00876cd4 bytes c912ef97
+ 00876d2c bytes c312ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-173bdb91a1b5a67002b4db8d5f58ade6"></a>

### [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) → [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) FUN_00876f5c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00872a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872a10.md) · 呼出先 26件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md)
- 新版 呼出元 1件 [`00872a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md) · 呼出先 26件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.01% / 新版 91.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 11件, `store_destination` 2件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00876fd8",
      "incomplete_value": true,
      "site": "00876fe8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8c9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876f80",
      "incomplete_value": true,
      "site": "00876f90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:889:8"
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
      "definition_site": "00876fdc",
      "incomplete_value": true,
      "site": "00876fec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00876f84",
      "incomplete_value": true,
      "site": "00876f94",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00876fe0",
      "incomplete_value": true,
      "site": "00876ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876f88",
      "incomplete_value": true,
      "site": "00876f98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
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
      "00876fbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00876fd8",
      "READ",
      [
        "storage",
        "002b7889",
        null,
        "string"
      ]
    ],
    [
      "00876fdc",
      "READ",
      [
        "storage",
        "002b7898",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00876fbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00876fd8",
      "READ",
      [
        "storage",
        "002b78c9",
        null,
        "string"
      ]
    ],
    [
      "00876fdc",
      "READ",
      [
        "storage",
        "002b78d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-00876f64) · [`00876f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-00876f70) · [`008770f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md#insn-008770f8)
- 新版 `00876fbc`（命令位置の公開資料なし） · `00876fc8`（命令位置の公開資料なし） · `00877150`（命令位置の公開資料なし）

~~~diff
- 00876f64 ["INT_ADD", "register:40f0:8", ["const:876f64:8", "const:4:8"]]
- 00876f64 ["CALL", null, ["ram:48ccf8:8"]]
+ 00876fbc ["INT_ADD", "register:40f0:8", ["const:876fbc:8", "const:4:8"]]
+ 00876fbc ["CALL", null, ["ram:48cd38:8"]]
- 00876f64 bytes 6557f097
+ 00876fbc bytes 5f57f097
- 00876f70 ["INT_ADD", "register:40f0:8", ["const:876f70:8", "const:4:8"]]
- 00876f70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00876fc8 ["INT_ADD", "register:40f0:8", ["const:876fc8:8", "const:4:8"]]
+ 00876fc8 ["CALL", null, ["callee:00c57f60:8"]]
- 00876f70 bytes c8830f94
+ 00876fc8 bytes e6830f94
- 008770f8 ["INT_ADD", "register:40f0:8", ["const:8770f8:8", "const:4:8"]]
- 008770f8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00877150 ["INT_ADD", "register:40f0:8", ["const:877150:8", "const:4:8"]]
+ 00877150 ["CALL", null, ["ram:48cd38:8"]]
- 008770f8 bytes 0057f097
+ 00877150 bytes fa56f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a21a526b6f8bf19f9dd4c04462ccb281"></a>

### [`00877a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md) → [`00877ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md) FUN_00877ac8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`00597e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e48.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`00877d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`00877da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877da8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

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
      "definition_site": "00877b80",
      "incomplete_value": false,
      "site": "00877b8c",
      "value": [
        "leaf",
        "const:877da8:8"
      ]
    },
    "old": {
      "definition_site": "00877b28",
      "incomplete_value": false,
      "site": "00877b34",
      "value": [
        "leaf",
        "const:877d50:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00877c24",
      "incomplete_value": false,
      "site": "00877c28",
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
    "old": {
      "definition_site": "00877bcc",
      "incomplete_value": false,
      "site": "00877bd0",
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
            "const:f27:8"
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
      "00877b80",
      "PARAM",
      [
        "storage",
        "00877d50",
        null,
        null
      ]
    ],
    [
      "00877c24",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00877b80",
      "PARAM",
      [
        "storage",
        "00877da8",
        null,
        null
      ]
    ],
    [
      "00877c24",
      "PARAM",
      [
        "storage",
        "002a3eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877b34) · [`00877bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877bd0) · [`00877ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md#insn-00877ac8)
- 新版 `00877b8c`（命令位置の公開資料なし） · `00877c28`（命令位置の公開資料なし） · `00877b20`（命令位置の公開資料なし）

~~~diff
- 00877b34 ["INT_ADD", "register:40f0:8", ["const:877b34:8", "const:4:8"]]
- 00877b34 ["CALL", null, ["callee:00c581e0:8"]]
+ 00877b8c ["INT_ADD", "register:40f0:8", ["const:877b8c:8", "const:4:8"]]
+ 00877b8c ["CALL", null, ["callee:00c581e0:8"]]
- 00877b34 bytes 77810f94
+ 00877b8c bytes 95810f94
- 00877bd0 ["INT_ADD", "register:40f0:8", ["const:877bd0:8", "const:4:8"]]
- 00877bd0 ["CALL", null, ["callee:00c581f0:8"]]
+ 00877c28 ["INT_ADD", "register:40f0:8", ["const:877c28:8", "const:4:8"]]
+ 00877c28 ["CALL", null, ["callee:00c581f0:8"]]
- 00877bd0 bytes 54810f94
+ 00877c28 bytes 72810f94
- 00877ac8 ["INT_ADD", "register:40f0:8", ["const:877ac8:8", "const:4:8"]]
- 00877ac8 ["CALL", null, ["callee:00597e88:8"]]
+ 00877b20 ["INT_ADD", "register:40f0:8", ["const:877b20:8", "const:4:8"]]
+ 00877b20 ["CALL", null, ["callee:00597e88:8"]]
- 00877ac8 bytes e080f497
+ 00877b20 bytes da80f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dacc5d1c1c954505d3a351b73480b8a"></a>

### [`00877e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md) → [`00877ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ef0.md) _INIT_158

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00877f2c",
      "incomplete_value": true,
      "site": "00877f48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00877ed4",
      "incomplete_value": true,
      "site": "00877ef0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00877f50",
      "incomplete_value": true,
      "site": "00877f6c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00877ef8",
      "incomplete_value": true,
      "site": "00877f14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00877f70",
      "incomplete_value": true,
      "site": "00877f8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00877f18",
      "incomplete_value": true,
      "site": "00877f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00877f2c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00877f50",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00877f70",
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
      "00877f2c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00877f50",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00877f70",
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

- 旧版 [`00877f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-00877f6c) · [`00877f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-00877f8c) · [`008780cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877e98.md#insn-008780cc)
- 新版 `00877fc4`（命令位置の公開資料なし） · `00877fe4`（命令位置の公開資料なし） · `00878124`（命令位置の公開資料なし）

~~~diff
- 00877f6c ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 00877f6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877f6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877f6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877fc4 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00877fc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877fc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877fc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877f6c bytes 29753d91
+ 00877fc4 bytes 29413c91
- 00877f8c ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00877f8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00877f8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00877f8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877fe4 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00877fe4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877fe4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877fe4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00877f8c bytes 29253c91
+ 00877fe4 bytes 29f13a91
- 008780cc ["INT_ADD", "register:40f0:8", ["const:8780cc:8", "const:4:8"]]
- 008780cc ["CALL", null, ["callee:00c57f00:8"]]
+ 00878124 ["INT_ADD", "register:40f0:8", ["const:878124:8", "const:4:8"]]
+ 00878124 ["CALL", null, ["callee:00c57f00:8"]]
- 008780cc bytes 597f0f94
+ 00878124 bytes 777f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4f18252c72c8c339cd665dff3e9bbf"></a>

### [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) → [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) FUN_00878448

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 19件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006eecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006eecac.md) [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`0070d3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070d3b8.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) · 呼出先 6件 [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)
- 新版 呼出元 19件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md) [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`0070d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md) [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) · 呼出先 6件 [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878508",
      "incomplete_value": false,
      "site": "00878508",
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
            "const:fcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008784b0",
      "incomplete_value": false,
      "site": "008784b0",
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
            "const:27:8"
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
      "definition_site": "00878578",
      "incomplete_value": false,
      "site": "00878578",
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
            "const:252:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878520",
      "incomplete_value": false,
      "site": "00878520",
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
            "const:223:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008785e8",
      "incomplete_value": false,
      "site": "008785e8",
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
            "const:14e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878590",
      "incomplete_value": false,
      "site": "00878590",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878508",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878550",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "unmatched:00878508",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a900"
      ]
    ]
  ],
  "added": [
    [
      "00878508",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00878550",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00878560",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a900"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008784c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md#insn-008784c8) · [`00878508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md#insn-00878508) · [`00878510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md#insn-00878510)
- 新版 `00878520`（命令位置の公開資料なし） · `00878568`（命令位置の公開資料なし）

~~~diff
- 008784c8 ["INT_ADD", "register:40f0:8", ["const:8784c8:8", "const:4:8"]]
- 008784c8 ["CALL", null, ["callee:00c5a900:8"]]
+ 00878520 ["INT_ADD", "register:40f0:8", ["const:878520:8", "const:4:8"]]
+ 00878520 ["CALL", null, ["callee:00c5a900:8"]]
- 008784c8 bytes da880f94
+ 00878520 bytes f8880f94
- 00878508 ["INT_ADD", "register:40f0:8", ["const:878508:8", "const:4:8"]]
- 00878508 ["CALL", null, ["callee:00c5a900:8"]]
- 00878508 bytes ca880f94
- 00878510 ["INT_ADD", "register:40f0:8", ["const:878510:8", "const:4:8"]]
- 00878510 ["CALL", null, ["ram:71bed8:8"]]
+ 00878568 ["INT_ADD", "register:40f0:8", ["const:878568:8", "const:4:8"]]
+ 00878568 ["CALL", null, ["ram:71bf30:8"]]
- 00878510 bytes 728efa97
+ 00878568 bytes 728efa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6696d13ec346fb1a78146770903bbb5d"></a>

### [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) → [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) FUN_008787b0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) [`00878bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md) [`00878ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878ed8.md) [`00878ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878ef0.md) [`0087929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/0087929c.md) · 呼出先 11件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`00b3c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c8dc.md)
- 新版 呼出元 5件 [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) [`00878c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md) [`00878f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f30.md) [`00878f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f48.md) [`008792f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/008792f4.md) · 呼出先 11件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`007842d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/007842d8.md) [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md)

変更の種類 call, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878848",
      "incomplete_value": false,
      "site": "00878848",
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
            "const:31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008787f0",
      "incomplete_value": false,
      "site": "008787f0",
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
            "const:0:8"
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
      "definition_site": "008788b0",
      "incomplete_value": false,
      "site": "008788b0",
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
            "const:6cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878858",
      "incomplete_value": false,
      "site": "00878858",
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
            "const:723:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008788b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878848",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "0087886c",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "0087889c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00878848",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "0087886c",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "0087889c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-00878844) · [`00878848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-00878848) · [`008788b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md#insn-008788b0)
- 新版 `0087889c`（命令位置の公開資料なし） · `008788a0`（命令位置の公開資料なし） · `00878908`（命令位置の公開資料なし）

~~~diff
- 00878844 ["INT_ADD", "register:40f0:8", ["const:878844:8", "const:4:8"]]
- 00878844 ["CALL", null, ["ram:48ccf8:8"]]
+ 0087889c ["INT_ADD", "register:40f0:8", ["const:87889c:8", "const:4:8"]]
+ 0087889c ["CALL", null, ["ram:48cd38:8"]]
- 00878844 bytes 2d51f097
+ 0087889c bytes 2751f097
- 00878848 ["INT_ADD", "register:40f0:8", ["const:878848:8", "const:4:8"]]
- 00878848 ["CALL", null, ["callee:0048cec4:8"]]
+ 008788a0 ["INT_ADD", "register:40f0:8", ["const:8788a0:8", "const:4:8"]]
+ 008788a0 ["CALL", null, ["callee:0048cec4:8"]]
- 00878848 bytes 8f51f097
+ 008788a0 bytes 8951f097
- 008788b0 ["COPY", "register:4040:8", ["const:2b0000:8"]]
+ 00878908 ["COPY", "register:4040:8", ["const:2af000:8"]]
- 008788b0 bytes c8d1ff90
+ 00878908 bytes a8d1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd27e5db4f89ae76055f477412ab81b5"></a>

### [`00878bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md) → [`00878c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md) FUN_00878c44

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00611e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611e60.md) [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 6件 [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`00878758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878758.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)
- 新版 呼出元 5件 [`00611ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611ea0.md) [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 6件 [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878cf4",
      "incomplete_value": false,
      "site": "00878cf4",
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
            "const:fcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878c9c",
      "incomplete_value": false,
      "site": "00878c9c",
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
            "const:27:8"
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
      "definition_site": "00878d68",
      "incomplete_value": false,
      "site": "00878d68",
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
            "const:252:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878d10",
      "incomplete_value": false,
      "site": "00878d10",
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
            "const:223:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878dd8",
      "incomplete_value": false,
      "site": "00878dd8",
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
            "const:14e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878d80",
      "incomplete_value": false,
      "site": "00878d80",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878cf4",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878d3c",
      "DATA",
      [
        "storage",
        "002b0027",
        null,
        null
      ]
    ],
    [
      "00878d54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ],
  "added": [
    [
      "00878cf4",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00878d3c",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00878d54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878cf4) · [`00878cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878cfc) · [`00878d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878bec.md#insn-00878d28)
- 新版 `00878d4c`（命令位置の公開資料なし） · `00878d54`（命令位置の公開資料なし） · `00878d80`（命令位置の公開資料なし）

~~~diff
- 00878cf4 ["INT_ADD", "register:40f0:8", ["const:878cf4:8", "const:4:8"]]
- 00878cf4 ["CALL", null, ["callee:00c5a900:8"]]
+ 00878d4c ["INT_ADD", "register:40f0:8", ["const:878d4c:8", "const:4:8"]]
+ 00878d4c ["CALL", null, ["callee:00c5a900:8"]]
- 00878cf4 bytes cf860f94
+ 00878d4c bytes ed860f94
- 00878cfc ["INT_ADD", "register:40f0:8", ["const:878cfc:8", "const:4:8"]]
- 00878cfc ["CALL", null, ["ram:71bed8:8"]]
+ 00878d54 ["INT_ADD", "register:40f0:8", ["const:878d54:8", "const:4:8"]]
+ 00878d54 ["CALL", null, ["ram:71bf30:8"]]
- 00878cfc bytes 778cfa97
+ 00878d54 bytes 778cfa97
- 00878d28 ["INT_ADD", "register:40f0:8", ["const:878d28:8", "const:4:8"]]
- 00878d28 ["CALL", null, ["callee:00c5a900:8"]]
+ 00878d80 ["INT_ADD", "register:40f0:8", ["const:878d80:8", "const:4:8"]]
+ 00878d80 ["CALL", null, ["callee:00c5a900:8"]]
- 00878d28 bytes c2860f94
+ 00878d80 bytes e0860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197707cccb87d306486525e0c005bd31"></a>

### [`00878f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md) → [`00878f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f60.md) FUN_00878f60

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 11件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`00b3c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c8dc.md)
- 新版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 11件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`007842d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/007842d8.md) [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md)

変更の種類 call, call_argument_candidate, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878fe8",
      "incomplete_value": false,
      "site": "00878fe8",
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
            "const:31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878f90",
      "incomplete_value": false,
      "site": "00878f90",
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
            "const:0:8"
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
      "definition_site": "00879050",
      "incomplete_value": false,
      "site": "00879050",
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
            "const:6cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878ff8",
      "incomplete_value": false,
      "site": "00878ff8",
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
            "const:723:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879058"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878fe8",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "0087900c",
      "DATA",
      [
        "storage",
        "002b3000",
        null,
        null
      ]
    ],
    [
      "0087903c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00878fe8",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "0087900c",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "0087903c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00878fe4) · [`00878fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00878fe8) · [`00879050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/00878f08.md#insn-00879050)
- 新版 `0087903c`（命令位置の公開資料なし） · `00879040`（命令位置の公開資料なし） · `008790a8`（命令位置の公開資料なし）

~~~diff
- 00878fe4 ["INT_ADD", "register:40f0:8", ["const:878fe4:8", "const:4:8"]]
- 00878fe4 ["CALL", null, ["ram:48ccf8:8"]]
+ 0087903c ["INT_ADD", "register:40f0:8", ["const:87903c:8", "const:4:8"]]
+ 0087903c ["CALL", null, ["ram:48cd38:8"]]
- 00878fe4 bytes 454ff097
+ 0087903c bytes 3f4ff097
- 00878fe8 ["INT_ADD", "register:40f0:8", ["const:878fe8:8", "const:4:8"]]
- 00878fe8 ["CALL", null, ["callee:0048cec4:8"]]
+ 00879040 ["INT_ADD", "register:40f0:8", ["const:879040:8", "const:4:8"]]
+ 00879040 ["CALL", null, ["callee:0048cec4:8"]]
- 00878fe8 bytes a74ff097
+ 00879040 bytes a14ff097
- 00879050 ["COPY", "register:4040:8", ["const:2b0000:8"]]
+ 008790a8 ["COPY", "register:4040:8", ["const:2af000:8"]]
- 00879050 bytes a8d1fff0
+ 008790a8 bytes a8d1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236b82acd4e5e283b148e9c978963dca"></a>

### [`008792b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md) → [`0087930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087930c.md) _INIT_159

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087936c",
      "incomplete_value": true,
      "site": "00879388",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00879314",
      "incomplete_value": true,
      "site": "00879330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087938c",
      "incomplete_value": true,
      "site": "008793a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00879334",
      "incomplete_value": true,
      "site": "00879350",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008793ac",
      "incomplete_value": true,
      "site": "008793c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879354",
      "incomplete_value": true,
      "site": "0087936c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
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
      "00879348",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087936c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087938c",
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
      "00879348",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0087936c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0087938c",
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

- 旧版 [`00879388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-00879388) · [`008793a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-008793a8) · [`008794e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008792b4.md#insn-008794e8)
- 新版 `008793e0`（命令位置の公開資料なし） · `00879400`（命令位置の公開資料なし） · `00879540`（命令位置の公開資料なし）

~~~diff
- 00879388 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 00879388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008793e0 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008793e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008793e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008793e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879388 bytes 29753d91
+ 008793e0 bytes 29413c91
- 008793a8 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 008793a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008793a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008793a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879400 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00879400 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879400 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879400 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008793a8 bytes 29253c91
+ 00879400 bytes 29f13a91
- 008794e8 ["INT_ADD", "register:40f0:8", ["const:8794e8:8", "const:4:8"]]
- 008794e8 ["CALL", null, ["callee:00c57f00:8"]]
+ 00879540 ["INT_ADD", "register:40f0:8", ["const:879540:8", "const:4:8"]]
+ 00879540 ["CALL", null, ["callee:00c57f00:8"]]
- 008794e8 bytes 527a0f94
+ 00879540 bytes 707a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a7f52f2ecc4805d821e5020ed66066"></a>

### [`00879644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md) → [`0087969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md) FUN_0087969c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0087bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bc44.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`005626f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00562/005626f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0087bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00879728",
      "incomplete_value": false,
      "site": "00879730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008796d0",
      "incomplete_value": false,
      "site": "008796d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "008796d8",
      "PARAM",
      [
        "storage",
        "011235f8",
        null,
        "undefined2"
      ]
    ],
    [
      "00879728",
      "PARAM",
      [
        "storage",
        "011235e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008796d8",
      "PARAM",
      [
        "storage",
        "011236f8",
        null,
        "undefined2"
      ]
    ],
    [
      "00879728",
      "PARAM",
      [
        "storage",
        "011236e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-00879680) · [`008796d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-008796d8) · [`0087968c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879644.md#insn-0087968c)
- 新版 `008796d8`（命令位置の公開資料なし） · `00879730`（命令位置の公開資料なし） · `008796e4`（命令位置の公開資料なし）

~~~diff
- 00879680 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00879680 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00879680 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00879680 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008796d8 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008796d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008796d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008796d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00879680 bytes 21e01791
+ 008796d8 bytes 21e01b91
- 008796d8 ["INT_ADD", "register:40f0:8", ["const:8796d8:8", "const:4:8"]]
- 008796d8 ["CALL", null, ["callee:004939d8:8"]]
+ 00879730 ["INT_ADD", "register:40f0:8", ["const:879730:8", "const:4:8"]]
+ 00879730 ["CALL", null, ["callee:004939d8:8"]]
- 008796d8 bytes b068f097
+ 00879730 bytes aa68f097
- 0087968c ["INT_ADD", "register:40f0:8", ["const:87968c:8", "const:4:8"]]
- 0087968c ["CALL", null, ["callee:00562734:8"]]
+ 008796e4 ["INT_ADD", "register:40f0:8", ["const:8796e4:8", "const:4:8"]]
+ 008796e4 ["CALL", null, ["callee:00562734:8"]]
- 0087968c bytes 1aa4f397
+ 008796e4 bytes 14a4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4c162e693b5d7f83fcb1cd90d05e85c"></a>

### [`008797b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md) → [`0087980c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087980c.md) _INIT_160

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.24% / 新版 75.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879848",
      "incomplete_value": true,
      "site": "00879864",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008797f0",
      "incomplete_value": true,
      "site": "0087980c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087986c",
      "incomplete_value": true,
      "site": "00879888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00879814",
      "incomplete_value": true,
      "site": "00879830",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0087988c",
      "incomplete_value": true,
      "site": "008798a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00879834",
      "incomplete_value": true,
      "site": "00879850",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00879848",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0087986c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0087988c",
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
      "00879848",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0087986c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0087988c",
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

- 旧版 [`00879888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-00879888) · [`008798a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-008798a8) · [`00879914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/008797b4.md#insn-00879914)
- 新版 `008798e0`（命令位置の公開資料なし） · `00879900`（命令位置の公開資料なし） · `0087996c`（命令位置の公開資料なし）

~~~diff
- 00879888 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 00879888 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879888 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879888 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008798e0 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008798e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008798e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008798e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879888 bytes 29753d91
+ 008798e0 bytes 29413c91
- 008798a8 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 008798a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008798a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008798a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879900 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00879900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008798a8 bytes 29253c91
+ 00879900 bytes 29f13a91
- 00879914 ["INT_ADD", "register:40f0:8", ["const:879914:8", "const:4:8"]]
- 00879914 ["CALL", null, ["callee:0043b838:8"]]
+ 0087996c ["INT_ADD", "register:40f0:8", ["const:87996c:8", "const:4:8"]]
+ 0087996c ["CALL", null, ["callee:0043b838:8"]]
- 00879914 bytes b907ef97
+ 0087996c bytes b307ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f966dbeb18559143bdbe2e2651789fc"></a>

### [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md) → [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md) FUN_00879de0

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0087a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a308.md) [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`0087bbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bbc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005b1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1910.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0087a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md) [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`0087bc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc1c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.44% / 新版 95.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879e68",
      "incomplete_value": true,
      "site": "00879e74",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00879e10",
      "incomplete_value": true,
      "site": "00879e1c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00879e64",
      "incomplete_value": true,
      "site": "00879e78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e0c",
      "incomplete_value": true,
      "site": "00879e20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c6b:8"
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
      "definition_site": "00879e64",
      "incomplete_value": true,
      "site": "00879e78",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00879e0c",
      "incomplete_value": true,
      "site": "00879e20",
      "value": [
        "LOAD",
        "16",
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
      "00879e64",
      "READ",
      [
        "storage",
        "002a6c6b",
        null,
        null
      ]
    ],
    [
      "00879e64",
      "READ",
      [
        "storage",
        "002a6c7b",
        null,
        null
      ]
    ],
    [
      "00879e68",
      "READ",
      [
        "storage",
        "002a6c8b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879e64",
      "READ",
      [
        "storage",
        "002a6c0f",
        null,
        null
      ]
    ],
    [
      "00879e64",
      "READ",
      [
        "storage",
        "002a6c1f",
        null,
        null
      ]
    ],
    [
      "00879e68",
      "READ",
      [
        "storage",
        "002a6c2f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879dec) · [`00879dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879dfc) · [`00879e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md#insn-00879e04)
- 新版 `00879e44`（命令位置の公開資料なし） · `00879e54`（命令位置の公開資料なし） · `00879e5c`（命令位置の公開資料なし）

~~~diff
- 00879dec ["COPY", "register:0:8", ["register:4040:8"]]
- 00879dec ["INT_ADD", "register:40f0:8", ["const:879dec:8", "const:4:8"]]
- 00879dec ["CALLIND", null, ["register:0:8"]]
+ 00879e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00879e44 ["INT_ADD", "register:40f0:8", ["const:879e44:8", "const:4:8"]]
+ 00879e44 ["CALLIND", null, ["register:0:8"]]
- 00879dec bytes 00013fd6
+ 00879e44 bytes 00013fd6
- 00879dfc ["INT_ADD", "register:40f0:8", ["const:879dfc:8", "const:4:8"]]
- 00879dfc ["CALL", null, ["callee:00c57f60:8"]]
+ 00879e54 ["INT_ADD", "register:40f0:8", ["const:879e54:8", "const:4:8"]]
+ 00879e54 ["CALL", null, ["callee:00c57f60:8"]]
- 00879dfc bytes 25780f94
+ 00879e54 bytes 43780f94
- 00879e04 ["COPY", "tmp:0:8", ["const:c6b:8"]]
- 00879e04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879e04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879e04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00879e5c ["COPY", "tmp:0:8", ["const:c0f:8"]]
+ 00879e5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00879e5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00879e5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879e04 bytes 29ad3191
+ 00879e5c bytes 293d3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c597c525c36562b52ddb43929353ed70"></a>

### [`0087aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md) → [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) FUN_0087aa68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a748.md) [`00b34ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b34/00b34ea4.md) · 呼出先 7件 [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) [`0087bfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087bfa0.md) [`0087c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c178.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) [`00b34f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34f40.md) · 呼出先 7件 [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) [`0087bff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bff8.md) [`0087c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ab30",
      "incomplete_value": false,
      "site": "0087ab30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087aad8",
      "incomplete_value": false,
      "site": "0087aad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "definition_site": "0087aad0",
      "incomplete_value": false,
      "site": "0087aae8",
      "value": [
        "leaf",
        "const:87bff8:8"
      ]
    },
    "old": {
      "definition_site": "0087aa78",
      "incomplete_value": false,
      "site": "0087aa90",
      "value": [
        "leaf",
        "const:87bfa0:8"
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
      "0087aad0",
      "PARAM",
      [
        "storage",
        "0087bfa0",
        null,
        null
      ]
    ],
    [
      "0087ab30",
      "DATA",
      [
        "storage",
        "00c80388",
        null,
        "undefined *"
      ]
    ],
    [
      "0087abb0",
      "READ",
      [
        "storage",
        "00c803b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087aad0",
      "PARAM",
      [
        "storage",
        "0087bff8",
        null,
        null
      ]
    ],
    [
      "0087ab30",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ],
    [
      "0087abb0",
      "READ",
      [
        "storage",
        "00c80480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087aa90) · [`0087ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087ab30) · [`0087aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087aa10.md#insn-0087aa50)
- 新版 `0087aae8`（命令位置の公開資料なし） · `0087ab88`（命令位置の公開資料なし） · `0087aaa8`（命令位置の公開資料なし）

~~~diff
- 0087aa90 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aa90 ["INT_ADD", "register:40f0:8", ["const:87aa90:8", "const:4:8"]]
- 0087aa90 ["CALLIND", null, ["register:0:8"]]
+ 0087aae8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087aae8 ["INT_ADD", "register:40f0:8", ["const:87aae8:8", "const:4:8"]]
+ 0087aae8 ["CALLIND", null, ["register:0:8"]]
- 0087aa90 bytes 20013fd6
+ 0087aae8 bytes 20013fd6
- 0087ab30 ["INT_ADD", "register:40f0:8", ["const:87ab30:8", "const:4:8"]]
- 0087ab30 ["CALL", null, ["callee:0087b4a0:8"]]
+ 0087ab88 ["INT_ADD", "register:40f0:8", ["const:87ab88:8", "const:4:8"]]
+ 0087ab88 ["CALL", null, ["callee:0087b4a0:8"]]
- 0087ab30 bytes 46020094
+ 0087ab88 bytes 46020094
- 0087aa50 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aa50 ["INT_ADD", "register:40f0:8", ["const:87aa50:8", "const:4:8"]]
- 0087aa50 ["CALLIND", null, ["register:0:8"]]
+ 0087aaa8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087aaa8 ["INT_ADD", "register:40f0:8", ["const:87aaa8:8", "const:4:8"]]
+ 0087aaa8 ["CALLIND", null, ["register:0:8"]]
- 0087aa50 bytes 20013fd6
+ 0087aaa8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca3af2ceed025be1aec2b38c0781d29a"></a>

### [`0087b0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md) → [`0087b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md) FUN_0087b148

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md) · 呼出先 7件 [`0087b448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b448.md) [`0087c608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c608.md) [`0087c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087c/0087c7e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md) · 呼出先 7件 [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) [`0087c660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c660.md) [`0087c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087b210",
      "incomplete_value": false,
      "site": "0087b210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b1b8",
      "incomplete_value": false,
      "site": "0087b1b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
      "definition_site": "0087b1b0",
      "incomplete_value": false,
      "site": "0087b1c8",
      "value": [
        "leaf",
        "const:87c660:8"
      ]
    },
    "old": {
      "definition_site": "0087b158",
      "incomplete_value": false,
      "site": "0087b170",
      "value": [
        "leaf",
        "const:87c608:8"
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
      "0087b1b0",
      "PARAM",
      [
        "storage",
        "0087c608",
        null,
        null
      ]
    ],
    [
      "0087b210",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ],
    [
      "0087b290",
      "READ",
      [
        "storage",
        "00c804c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b1b0",
      "PARAM",
      [
        "storage",
        "0087c660",
        null,
        null
      ]
    ],
    [
      "0087b210",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ],
    [
      "0087b290",
      "READ",
      [
        "storage",
        "00c80590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b170) · [`0087b210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b210) · [`0087b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b0f0.md#insn-0087b130)
- 新版 `0087b1c8`（命令位置の公開資料なし） · `0087b268`（命令位置の公開資料なし） · `0087b188`（命令位置の公開資料なし）

~~~diff
- 0087b170 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b170 ["INT_ADD", "register:40f0:8", ["const:87b170:8", "const:4:8"]]
- 0087b170 ["CALLIND", null, ["register:0:8"]]
+ 0087b1c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b1c8 ["INT_ADD", "register:40f0:8", ["const:87b1c8:8", "const:4:8"]]
+ 0087b1c8 ["CALLIND", null, ["register:0:8"]]
- 0087b170 bytes 20013fd6
+ 0087b1c8 bytes 20013fd6
- 0087b210 ["INT_ADD", "register:40f0:8", ["const:87b210:8", "const:4:8"]]
- 0087b210 ["CALL", null, ["callee:0087b4a0:8"]]
+ 0087b268 ["INT_ADD", "register:40f0:8", ["const:87b268:8", "const:4:8"]]
+ 0087b268 ["CALL", null, ["callee:0087b4a0:8"]]
- 0087b210 bytes 8e000094
+ 0087b268 bytes 8e000094
- 0087b130 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b130 ["INT_ADD", "register:40f0:8", ["const:87b130:8", "const:4:8"]]
- 0087b130 ["CALLIND", null, ["register:0:8"]]
+ 0087b188 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b188 ["INT_ADD", "register:40f0:8", ["const:87b188:8", "const:4:8"]]
+ 0087b188 ["CALLIND", null, ["register:0:8"]]
- 0087b130 bytes 20013fd6
+ 0087b188 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b5b448bf7ea2b69b15d725f376cfa6"></a>

### [`0087b5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5a4.md) → [`0087b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b5fc.md) FUN_0087b5fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b608",
      "incomplete_value": false,
      "site": "0087b614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b5b0",
      "incomplete_value": false,
      "site": "0087b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0087b614",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b614",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5a4.md#insn-0087b5b0)
- 新版 `0087b608`（命令位置の公開資料なし）

~~~diff
- 0087b5b0 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0087b5b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087b5b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087b5b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087b608 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0087b608 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087b608 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087b608 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087b5b0 bytes 4aa10991
+ 0087b608 bytes 4ae10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4134771cc11a88c925ce0c1186b7505"></a>

### [`0087b5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md) → [`0087b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b640.md) FUN_0087b640

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b658",
      "incomplete_value": false,
      "site": "0087b664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b600",
      "incomplete_value": false,
      "site": "0087b60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0087b664",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b664",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md#insn-0087b600) · [`0087b630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b5e8.md#insn-0087b630)
- 新版 `0087b658`（命令位置の公開資料なし） · `0087b688`（命令位置の公開資料なし）

~~~diff
- 0087b600 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0087b600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b658 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0087b658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b600 bytes 08a10991
+ 0087b658 bytes 08e10c91
- 0087b630 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b630 ["INT_ADD", "register:40f0:8", ["const:87b630:8", "const:4:8"]]
- 0087b630 ["CALLIND", null, ["register:0:8"]]
+ 0087b688 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b688 ["INT_ADD", "register:40f0:8", ["const:87b688:8", "const:4:8"]]
+ 0087b688 ["CALLIND", null, ["register:0:8"]]
- 0087b630 bytes 00013fd6
+ 0087b688 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69aaf66482d72a6e9a9ac0dafeb233dc"></a>

### [`0087b644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md) → [`0087b69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b69c.md) FUN_0087b69c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b6c8",
      "incomplete_value": false,
      "site": "0087b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b670",
      "incomplete_value": false,
      "site": "0087b670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0087b6c8",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b6c8",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b658) · [`0087b668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b668) · [`0087b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b644.md#insn-0087b68c)
- 新版 `0087b6b0`（命令位置の公開資料なし） · `0087b6c0`（命令位置の公開資料なし） · `0087b6e4`（命令位置の公開資料なし）

~~~diff
- 0087b658 ["INT_ADD", "register:40f0:8", ["const:87b658:8", "const:4:8"]]
- 0087b658 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087b6b0 ["INT_ADD", "register:40f0:8", ["const:87b6b0:8", "const:4:8"]]
+ 0087b6b0 ["CALL", null, ["callee:00c57f60:8"]]
- 0087b658 bytes 0e720f94
+ 0087b6b0 bytes 2c720f94
- 0087b668 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0087b668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b6c0 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0087b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b668 bytes 08a10991
+ 0087b6c0 bytes 08e10c91
- 0087b68c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b68c ["INT_ADD", "register:40f0:8", ["const:87b68c:8", "const:4:8"]]
- 0087b68c ["CALLIND", null, ["register:0:8"]]
+ 0087b6e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b6e4 ["INT_ADD", "register:40f0:8", ["const:87b6e4:8", "const:4:8"]]
+ 0087b6e4 ["CALLIND", null, ["register:0:8"]]
- 0087b68c bytes 00013fd6
+ 0087b6e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d3c46cb348d7a7dde217a12ef8f9c7"></a>

### [`0087b6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md) → [`0087b724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b724.md) FUN_0087b724

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087b740",
      "incomplete_value": false,
      "site": "0087b740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b6e8",
      "incomplete_value": false,
      "site": "0087b6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0087b740",
      "DATA",
      [
        "storage",
        "00c80268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b740",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md#insn-0087b6e4) · [`0087b708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b6cc.md#insn-0087b708)
- 新版 `0087b73c`（命令位置の公開資料なし） · `0087b760`（命令位置の公開資料なし）

~~~diff
- 0087b6e4 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0087b6e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087b6e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087b6e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087b73c ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0087b73c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087b73c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087b73c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087b6e4 bytes 29a10991
+ 0087b73c bytes 29e10c91
- 0087b708 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b708 ["INT_ADD", "register:40f0:8", ["const:87b708:8", "const:4:8"]]
- 0087b708 ["CALLIND", null, ["register:0:8"]]
+ 0087b760 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087b760 ["INT_ADD", "register:40f0:8", ["const:87b760:8", "const:4:8"]]
+ 0087b760 ["CALLIND", null, ["register:0:8"]]
- 0087b708 bytes 20013fd6
+ 0087b760 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68a96f9b36d5e08f91511ed56ea99b1a"></a>

### [`0087b810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md) → [`0087b868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b868.md) FUN_0087b868

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087b880",
      "incomplete_value": false,
      "site": "0087b890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b828",
      "incomplete_value": false,
      "site": "0087b838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0087b890",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b890",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md#insn-0087b828) · [`0087b85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b810.md#insn-0087b85c)
- 新版 `0087b880`（命令位置の公開資料なし） · `0087b8b4`（命令位置の公開資料なし）

~~~diff
- 0087b828 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0087b828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b880 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0087b880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b828 bytes 08e10b91
+ 0087b880 bytes 08210f91
- 0087b85c ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b85c ["INT_ADD", "register:40f0:8", ["const:87b85c:8", "const:4:8"]]
- 0087b85c ["CALLIND", null, ["register:0:8"]]
+ 0087b8b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b8b4 ["INT_ADD", "register:40f0:8", ["const:87b8b4:8", "const:4:8"]]
+ 0087b8b4 ["CALLIND", null, ["register:0:8"]]
- 0087b85c bytes 00013fd6
+ 0087b8b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11daa42d7cfbf2a82a9a7629c9191169"></a>

### [`0087b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md) → [`0087b8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b8f8.md) FUN_0087b8f8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0087b910",
      "incomplete_value": false,
      "site": "0087b920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b8b8",
      "incomplete_value": false,
      "site": "0087b8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0087b920",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b920",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b8b8) · [`0087b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b8ec) · [`0087b918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b8a0.md#insn-0087b918)
- 新版 `0087b910`（命令位置の公開資料なし） · `0087b944`（命令位置の公開資料なし） · `0087b970`（命令位置の公開資料なし）

~~~diff
- 0087b8b8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0087b8b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b8b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b8b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b910 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0087b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b8b8 bytes 08e10b91
+ 0087b910 bytes 08210f91
- 0087b8ec ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b8ec ["INT_ADD", "register:40f0:8", ["const:87b8ec:8", "const:4:8"]]
- 0087b8ec ["CALLIND", null, ["register:0:8"]]
+ 0087b944 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b944 ["INT_ADD", "register:40f0:8", ["const:87b944:8", "const:4:8"]]
+ 0087b944 ["CALLIND", null, ["register:0:8"]]
- 0087b8ec bytes 00013fd6
+ 0087b944 bytes 00013fd6
- 0087b918 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b918 ["INT_ADD", "register:40f0:8", ["const:87b918:8", "const:4:8"]]
- 0087b918 ["CALLIND", null, ["register:0:8"]]
+ 0087b970 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b970 ["INT_ADD", "register:40f0:8", ["const:87b970:8", "const:4:8"]]
+ 0087b970 ["CALLIND", null, ["register:0:8"]]
- 0087b918 bytes 00013fd6
+ 0087b970 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6248ccd69f8db45d0653377728ed6823"></a>

### [`0087b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md) → [`0087b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b984.md) FUN_0087b984

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087b9b4",
      "incomplete_value": false,
      "site": "0087b9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b95c",
      "incomplete_value": false,
      "site": "0087b95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0087b9b4",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087b9b4",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b944) · [`0087b954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b954) · [`0087b978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b92c.md#insn-0087b978)
- 新版 `0087b99c`（命令位置の公開資料なし） · `0087b9ac`（命令位置の公開資料なし） · `0087b9d0`（命令位置の公開資料なし）

~~~diff
- 0087b944 ["INT_ADD", "register:40f0:8", ["const:87b944:8", "const:4:8"]]
- 0087b944 ["CALL", null, ["callee:00c57f60:8"]]
+ 0087b99c ["INT_ADD", "register:40f0:8", ["const:87b99c:8", "const:4:8"]]
+ 0087b99c ["CALL", null, ["callee:00c57f60:8"]]
- 0087b944 bytes 53710f94
+ 0087b99c bytes 71710f94
- 0087b954 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0087b954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087b9ac ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0087b9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087b9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b954 bytes 08e10b91
+ 0087b9ac bytes 08210f91
- 0087b978 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b978 ["INT_ADD", "register:40f0:8", ["const:87b978:8", "const:4:8"]]
- 0087b978 ["CALLIND", null, ["register:0:8"]]
+ 0087b9d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087b9d0 ["INT_ADD", "register:40f0:8", ["const:87b9d0:8", "const:4:8"]]
+ 0087b9d0 ["CALLIND", null, ["register:0:8"]]
- 0087b978 bytes 00013fd6
+ 0087b9d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15e3e612f54a86d4abba407f37c11590"></a>

### [`0087ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md) → [`0087ba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087ba94.md) FUN_0087ba94

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0087babc",
      "incomplete_value": true,
      "site": "0087babc",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ba64",
      "incomplete_value": true,
      "site": "0087ba64",
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
            "const:2f8:8"
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
      "0087babc",
      "DATA",
      [
        "storage",
        "00c802f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087babc",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087ba5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087ba5c) · [`0087ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087ba80) · [`0087baa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087ba3c.md#insn-0087baa8)
- 新版 `0087bab4`（命令位置の公開資料なし） · `0087bad8`（命令位置の公開資料なし） · `0087bb00`（命令位置の公開資料なし）

~~~diff
- 0087ba5c ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0087ba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087ba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087ba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087bab4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0087bab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087bab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087bab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087ba5c bytes 08e10b91
+ 0087bab4 bytes 08210f91
- 0087ba80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087ba80 ["INT_ADD", "register:40f0:8", ["const:87ba80:8", "const:4:8"]]
- 0087ba80 ["CALLIND", null, ["register:0:8"]]
+ 0087bad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bad8 ["INT_ADD", "register:40f0:8", ["const:87bad8:8", "const:4:8"]]
+ 0087bad8 ["CALLIND", null, ["register:0:8"]]
- 0087ba80 bytes 00013fd6
+ 0087bad8 bytes 00013fd6
- 0087baa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087baa8 ["INT_ADD", "register:40f0:8", ["const:87baa8:8", "const:4:8"]]
- 0087baa8 ["CALLIND", null, ["register:0:8"]]
+ 0087bb00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087bb00 ["INT_ADD", "register:40f0:8", ["const:87bb00:8", "const:4:8"]]
+ 0087bb00 ["CALLIND", null, ["register:0:8"]]
- 0087baa8 bytes 00013fd6
+ 0087bb00 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

