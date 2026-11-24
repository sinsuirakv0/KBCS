# v16.0.0 → v16.0.1 · 最優先の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-7fc7cb9dd275114b357cdd7a0c0ea8df"></a>

### [`00488bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md) → [`00488c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md) FUN_00488c14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00488c2c",
      "incomplete_value": false,
      "site": "00488c38",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488bec",
      "incomplete_value": false,
      "site": "00488bf8",
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
            "const:418:8"
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
      "definition_site": "00488c4c",
      "incomplete_value": true,
      "site": "00488c4c",
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
      "definition_site": "00488c0c",
      "incomplete_value": true,
      "site": "00488c0c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00488c5c",
      "incomplete_value": true,
      "site": "00488c5c",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00488c1c",
      "incomplete_value": true,
      "site": "00488c1c",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "00488c30",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00488c38",
      "DATA",
      [
        "storage",
        "00c65418",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c44",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00488c30",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00488c38",
      "DATA",
      [
        "storage",
        "00c65818",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c44",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488bec) · [`00488bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488bf0) · [`00488bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488bd4.md#insn-00488bf4)
- 新版 [`00488c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md#insn-00488c2c) · [`00488c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md#insn-00488c30)

~~~diff
- 00488bec ["COPY", "tmp:0:8", ["const:418:8"]]
- 00488bec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00488bec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00488bec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00488c2c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00488c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00488c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00488c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00488bec bytes 08611091
+ 00488c2c bytes 08612091
- 00488bf0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
- 00488bf0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00488c30 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
+ 00488c30 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00488bf0 bytes d6de43f9
+ 00488c30 bytes d6de45f9
- 00488bf4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00488bf4 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb1705464de64aa4ef7399af32da9195"></a>

### [`00488c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md) → [`00488cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md) FUN_00488cc8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00488d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d60.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)
- 新版 呼出元 1件 [`00488da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.93% / 新版 75.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00488ce4",
      "incomplete_value": false,
      "site": "00488ce8",
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
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488ca4",
      "incomplete_value": false,
      "site": "00488ca8",
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
            "const:478:8"
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
      "definition_site": "00488d00",
      "incomplete_value": false,
      "site": "00488d0c",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488cc0",
      "incomplete_value": false,
      "site": "00488ccc",
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
            "const:418:8"
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
      "definition_site": "00488d1c",
      "incomplete_value": true,
      "site": "00488d1c",
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
      "definition_site": "00488cdc",
      "incomplete_value": true,
      "site": "00488cdc",
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00488ce8",
      "DATA",
      [
        "storage",
        "00c65478",
        null,
        "undefined *"
      ]
    ],
    [
      "00488d04",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00488d0c",
      "DATA",
      [
        "storage",
        "00c65418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00488ce8",
      "DATA",
      [
        "storage",
        "00c65878",
        null,
        "undefined *"
      ]
    ],
    [
      "00488d04",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00488d0c",
      "DATA",
      [
        "storage",
        "00c65818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488cb4) · [`00488ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488ce8) · [`00488d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488c88.md#insn-00488d0c)
- 新版 [`00488cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488cf4) · [`00488d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488d28) · [`00488d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488d4c)

~~~diff
- 00488cb4 ["INT_ADD", "register:40f0:8", ["const:488cb4:8", "const:4:8"]]
- 00488cb4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00488cf4 ["INT_ADD", "register:40f0:8", ["const:488cf4:8", "const:4:8"]]
+ 00488cf4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00488cb4 bytes 7f3b1f94
+ 00488cf4 bytes 6f3c1f94
- 00488ce8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00488ce8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00488d28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00488d28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00488ce8 bytes 29e143f9
+ 00488d28 bytes 29e145f9
- 00488d0c ["INT_ADD", "register:40f0:8", ["const:488d0c:8", "const:4:8"]]
- 00488d0c ["CALL", null, ["callee:00c57fa0:8"]]
+ 00488d4c ["INT_ADD", "register:40f0:8", ["const:488d4c:8", "const:4:8"]]
+ 00488d4c ["CALL", null, ["callee:00c57fa0:8"]]
- 00488d0c bytes a53b1f94
+ 00488d4c bytes 953c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd4b6ac5c4632b0f182277548d706e4b"></a>

### [`00488d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md) → [`00488dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md) FUN_00488dc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004882ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004882ac.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00488dd0",
      "incomplete_value": false,
      "site": "00488dd4",
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
    "old": {
      "definition_site": "00488d90",
      "incomplete_value": false,
      "site": "00488d94",
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
            "const:f0c:8"
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
      "00488dd0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00488dd0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md#insn-00488d94) · [`00488d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d84.md#insn-00488d90)
- 新版 [`00488dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md#insn-00488dd4) · [`00488dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md#insn-00488dd0)

~~~diff
- 00488d94 ["INT_ADD", "register:40f0:8", ["const:488d94:8", "const:4:8"]]
- 00488d94 ["CALL", null, ["callee:0043b778:8"]]
+ 00488dd4 ["INT_ADD", "register:40f0:8", ["const:488dd4:8", "const:4:8"]]
+ 00488dd4 ["CALL", null, ["callee:0043b778:8"]]
- 00488d94 bytes 69cafe97
+ 00488dd4 bytes 69cafe97
- 00488d90 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00488d90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00488d90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00488d90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00488dd0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00488dd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00488dd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00488dd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00488d90 bytes 00303c91
+ 00488dd0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad368c97b6198038ccae5165e009ce9"></a>

### [`00488d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md) → [`00488dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md) _INIT_19

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00488e14",
      "incomplete_value": true,
      "site": "00488e30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00488dd4",
      "incomplete_value": true,
      "site": "00488df0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "00488e38",
      "incomplete_value": true,
      "site": "00488e54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00488df8",
      "incomplete_value": true,
      "site": "00488e14",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "00488e58",
      "incomplete_value": true,
      "site": "00488e74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00488e18",
      "incomplete_value": true,
      "site": "00488e34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "00488e14",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00488e38",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00488e58",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00488e14",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00488e38",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00488e58",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488e10) · [`00488e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488e30) · [`00488ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488d98.md#insn-00488ef8)
- 新版 [`00488e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488e50) · [`00488e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488e70) · [`00488f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488f38)

~~~diff
- 00488e10 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00488e10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00488e10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00488e10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00488e50 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00488e50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00488e10 bytes 4a093691
+ 00488e50 bytes 4a093791
- 00488e30 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00488e30 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00488e30 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00488e30 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00488e70 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00488e70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00488e30 bytes 4a553a91
+ 00488e70 bytes 4a893d91
- 00488ef8 ["INT_ADD", "register:40f0:8", ["const:488ef8:8", "const:4:8"]]
- 00488ef8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00488f38 ["INT_ADD", "register:40f0:8", ["const:488f38:8", "const:4:8"]]
+ 00488f38 ["CALL", null, ["callee:0043b7f8:8"]]
- 00488ef8 bytes 30cafe97
+ 00488f38 bytes 30cafe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb4d419de23bd3c89a5877c0f612db6b"></a>

### [`00489128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md) → [`00489168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md) FUN_00489168

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 0件 
- 新版 呼出元 6件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00489174",
      "incomplete_value": true,
      "site": "0048917c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00489134",
      "incomplete_value": true,
      "site": "0048913c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1c0:8"
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
      "00489174",
      "READ",
      [
        "storage",
        "002c41c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00489174",
      "READ",
      [
        "storage",
        "002c4200",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489128.md#insn-00489134)
- 新版 [`00489174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md#insn-00489174)

~~~diff
- 00489134 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 00489134 ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
- 00489134 ["COPY", "register:5028:8", ["const:0:8"]]
- 00489134 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00489174 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 00489174 ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
+ 00489174 ["COPY", "register:5028:8", ["const:0:8"]]
+ 00489174 ["COPY", "register:5030:8", ["const:0:8"]]
- 00489134 bytes 01e140fd
+ 00489174 bytes 010141fd
~~~


<a id="compare-9434e6075710bdabeffa5f089e80aeb7"></a>

### [`00489184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md) → [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) FUN_004891c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00489154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489154.md) [`00635aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635aa0.md) · 呼出先 15件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 2件 [`00489194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489194.md) [`00635ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635ae0.md) · 呼出先 15件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00489204",
      "incomplete_value": false,
      "site": "0048920c",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004891c4",
      "incomplete_value": false,
      "site": "004891cc",
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
            "const:938:8"
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
      "definition_site": "004893cc",
      "incomplete_value": true,
      "site": "004893d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048938c",
      "incomplete_value": true,
      "site": "00489390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004893c8",
      "incomplete_value": true,
      "site": "004893d4",
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
      "definition_site": "00489388",
      "incomplete_value": true,
      "site": "00489394",
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
      "0048920c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "004893a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048965c"
      ]
    ],
    [
      "004893b8",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048920c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "004893a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048969c"
      ]
    ],
    [
      "004893b8",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-00489368) · [`004893a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-004893a8) · [`004893d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489184.md#insn-004893d4)
- 新版 [`004893a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md#insn-004893a8) · [`004893e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md#insn-004893e8) · [`00489414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md#insn-00489414)

~~~diff
- 00489368 ["INT_ADD", "register:40f0:8", ["const:489368:8", "const:4:8"]]
- 00489368 ["CALL", null, ["ram:48965c:8"]]
+ 004893a8 ["INT_ADD", "register:40f0:8", ["const:4893a8:8", "const:4:8"]]
+ 004893a8 ["CALL", null, ["ram:48969c:8"]]
- 00489368 bytes bd000094
+ 004893a8 bytes bd000094
- 004893a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
- 004893a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004893e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 004893e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004893a8 bytes 08e143f9
+ 004893e8 bytes 08e145f9
- 004893d4 ["INT_ADD", "register:40f0:8", ["const:4893d4:8", "const:4:8"]]
- 004893d4 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00489414 ["INT_ADD", "register:40f0:8", ["const:489414:8", "const:4:8"]]
+ 00489414 ["CALL", null, ["callee:00c57fb0:8"]]
- 004893d4 bytes f7391f94
+ 00489414 bytes e73a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf060f13d21dc5d6e89f836665b28e9d"></a>

### [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) → [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) FUN_00489f70

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0048a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md) [`0048a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a7f4.md) · 呼出先 21件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a650.md) [`0048a6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6ac.md) [`0048b5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b5a4.md) [`0048b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b7b8.md)
- 新版 呼出元 2件 [`0048a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a73c.md) [`0048a834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a834.md) · 呼出先 21件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a690.md) [`0048a6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a6ec.md) [`0048b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b5e4.md) [`0048b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b7f8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 79.67% / 新版 79.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `call_target` 3件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048a180",
      "incomplete_value": true,
      "site": "0048a184",
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
                "register:4000:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048a140",
      "incomplete_value": true,
      "site": "0048a144",
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
                "register:4000:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00489fa4",
      "incomplete_value": false,
      "site": "00489fb0",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00489f64",
      "incomplete_value": false,
      "site": "00489f70",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00489fc0",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00489f80",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "00489fa4",
      "PARAM",
      [
        "storage",
        "00ca4c50",
        null,
        null
      ]
    ],
    [
      "00489fc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00489fc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00493938"
      ]
    ]
  ],
  "added": [
    [
      "00489fa4",
      "PARAM",
      [
        "storage",
        "00ca5050",
        null,
        null
      ]
    ],
    [
      "00489fc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "00489fc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00493978"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-00489f70) · [`00489f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-00489f80) · [`00489f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md#insn-00489f84)
- 新版 [`00489fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md#insn-00489fb0) · [`00489fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md#insn-00489fc0) · [`00489fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md#insn-00489fc4)

~~~diff
- 00489f70 ["INT_ADD", "register:40f0:8", ["const:489f70:8", "const:4:8"]]
- 00489f70 ["CALL", null, ["callee:00c580e0:8"]]
+ 00489fb0 ["INT_ADD", "register:40f0:8", ["const:489fb0:8", "const:4:8"]]
+ 00489fb0 ["CALL", null, ["callee:00c580e0:8"]]
- 00489f70 bytes 5c371f94
+ 00489fb0 bytes 4c381f94
- 00489f80 ["INT_ADD", "register:40f0:8", ["const:489f80:8", "const:4:8"]]
- 00489f80 ["CALL", null, ["ram:48ccb8:8"]]
+ 00489fc0 ["INT_ADD", "register:40f0:8", ["const:489fc0:8", "const:4:8"]]
+ 00489fc0 ["CALL", null, ["ram:48ccf8:8"]]
- 00489f80 bytes 4e0b0094
+ 00489fc0 bytes 4e0b0094
- 00489f84 ["INT_ADD", "register:40f0:8", ["const:489f84:8", "const:4:8"]]
- 00489f84 ["CALL", null, ["ram:493938:8"]]
+ 00489fc4 ["INT_ADD", "register:40f0:8", ["const:489fc4:8", "const:4:8"]]
+ 00489fc4 ["CALL", null, ["ram:493978:8"]]
- 00489f84 bytes 6d260094
+ 00489fc4 bytes 6d260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8427d8baadfa802e73bf14432b8d68"></a>

### [`0048a6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md) → [`0048a73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a73c.md) FUN_0048a73c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0066d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d660.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`0074c890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074c/0074c890.md) [`00753834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00753/00753834.md) · 呼出先 4件 [`00489f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f30.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 11件 [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0066d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d6a0.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`0074c8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074c/0074c8d0.md) [`00753874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/00753874.md) · 呼出先 4件 [`00489f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f70.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a75c",
      "incomplete_value": false,
      "site": "0048a76c",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048a71c",
      "incomplete_value": false,
      "site": "0048a72c",
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
            "const:bc0:8"
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
      "0048a75c",
      "PARAM",
      [
        "storage",
        "00ca4bc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0048a75c",
      "PARAM",
      [
        "storage",
        "00ca4fc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a72c) · [`0048a76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a76c) · [`0048a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048a6fc.md#insn-0048a71c)
- 新版 [`0048a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a73c.md#insn-0048a76c) · [`0048a7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a73c.md#insn-0048a7ac) · [`0048a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a73c.md#insn-0048a75c)

~~~diff
- 0048a72c ["INT_ADD", "register:40f0:8", ["const:48a72c:8", "const:4:8"]]
- 0048a72c ["CALL", null, ["callee:00489f70:8"]]
+ 0048a76c ["INT_ADD", "register:40f0:8", ["const:48a76c:8", "const:4:8"]]
+ 0048a76c ["CALL", null, ["callee:00489f70:8"]]
- 0048a72c bytes 01feff97
+ 0048a76c bytes 01feff97
- 0048a76c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048a76c ["INT_ADD", "register:40f0:8", ["const:48a76c:8", "const:4:8"]]
- 0048a76c ["CALLIND", null, ["register:0:8"]]
+ 0048a7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048a7ac ["INT_ADD", "register:40f0:8", ["const:48a7ac:8", "const:4:8"]]
+ 0048a7ac ["CALLIND", null, ["register:0:8"]]
- 0048a76c bytes 00013fd6
+ 0048a7ac bytes 00013fd6
- 0048a71c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0048a71c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048a71c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048a71c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048a75c ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 0048a75c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048a75c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048a75c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048a71c bytes 00002f91
+ 0048a75c bytes 00003f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93e2f988751298e5a0f07867aa02685"></a>

### [`0048abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md) → [`0048ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md) FUN_0048ac20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 4件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`0048aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aa10.md) [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md)
- 新版 呼出元 1件 [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 4件 [`004894a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`0048aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048aa50.md) [`0055e624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e624.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "0048ac84",
      "value": [
        "leaf",
        "ram:48969c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048ac44",
      "value": [
        "leaf",
        "ram:48965c:8"
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
      "0048ac84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048965c"
      ]
    ]
  ],
  "added": [
    [
      "0048ac84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048969c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ac44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md#insn-0048ac44) · [`0048abf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md#insn-0048abf8) · [`0048ac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048abe0.md#insn-0048ac30)
- 新版 [`0048ac84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md#insn-0048ac84) · [`0048ac38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md#insn-0048ac38) · [`0048ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac20.md#insn-0048ac70)

~~~diff
- 0048ac44 ["INT_ADD", "register:40f0:8", ["const:48ac44:8", "const:4:8"]]
- 0048ac44 ["CALL", null, ["ram:48965c:8"]]
+ 0048ac84 ["INT_ADD", "register:40f0:8", ["const:48ac84:8", "const:4:8"]]
+ 0048ac84 ["CALL", null, ["ram:48969c:8"]]
- 0048ac44 bytes 86faff97
+ 0048ac84 bytes 86faff97
- 0048abf8 ["INT_ADD", "register:40f0:8", ["const:48abf8:8", "const:4:8"]]
- 0048abf8 ["CALL", null, ["callee:0055e624:8"]]
+ 0048ac38 ["INT_ADD", "register:40f0:8", ["const:48ac38:8", "const:4:8"]]
+ 0048ac38 ["CALL", null, ["callee:0055e624:8"]]
- 0048abf8 bytes 7b4e0394
+ 0048ac38 bytes 7b4e0394
- 0048ac30 ["INT_ADD", "register:40f0:8", ["const:48ac30:8", "const:4:8"]]
- 0048ac30 ["CALL", null, ["callee:0048aa50:8"]]
+ 0048ac70 ["INT_ADD", "register:40f0:8", ["const:48ac70:8", "const:4:8"]]
+ 0048ac70 ["CALL", null, ["callee:0048aa50:8"]]
- 0048ac30 bytes 78ffff97
+ 0048ac70 bytes 78ffff97
~~~


<a id="compare-f29e14c62a54a50a691752b181d45f3c"></a>

### [`0048b350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md) → [`0048b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md) FUN_0048b390

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00851914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/00851914.md) [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) · 呼出先 1件 [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 2件 [`00851954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851954.md) [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) · 呼出先 1件 [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b3a8",
      "incomplete_value": true,
      "site": "0048b3a8",
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
      "definition_site": "0048b368",
      "incomplete_value": true,
      "site": "0048b368",
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
            "const:ba8:8"
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
      "definition_site": "0048b3c4",
      "incomplete_value": true,
      "site": "0048b3c4",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b384",
      "incomplete_value": true,
      "site": "0048b384",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048b3c8",
      "incomplete_value": false,
      "site": "0048b3c8",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b388",
      "incomplete_value": false,
      "site": "0048b388",
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
            "const:bb0:8"
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
      "0048b398",
      "READ",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b3a4",
      "PARAM",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b3a8",
      "WRITE",
      [
        "storage",
        "00ca4ba8",
        null,
        "undefined2"
      ]
    ]
  ],
  "added": [
    [
      "0048b398",
      "READ",
      [
        "storage",
        "00ca4fa8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b3a4",
      "PARAM",
      [
        "storage",
        "00ca4fa8",
        null,
        "undefined2"
      ]
    ],
    [
      "0048b3a8",
      "WRITE",
      [
        "storage",
        "00ca4fa8",
        null,
        "undefined2"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048b368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b368) · [`0048b358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b358) · [`0048b364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b350.md#insn-0048b364)
- 新版 [`0048b3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md#insn-0048b3a8) · [`0048b398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md#insn-0048b398) · [`0048b3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md#insn-0048b3a4)

~~~diff
- 0048b368 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba8:8"]]
- 0048b368 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0048b368 ["COPY", "tmp:2:4", ["tmp:1:4"]]
- 0048b368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
+ 0048b3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 0048b3a8 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0048b3a8 ["COPY", "tmp:2:4", ["tmp:1:4"]]
+ 0048b3a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:2:2"]]
- 0048b368 bytes 1f511779
+ 0048b3a8 bytes 1f511f79
- 0048b358 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba8:8"]]
- 0048b358 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0048b358 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0048b398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 0048b398 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0048b398 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0048b358 bytes 09a16e39
+ 0048b398 bytes 09a17e39
- 0048b364 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 0048b364 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048b364 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048b364 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048b3a4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 0048b3a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b3a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b3a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048b364 bytes 00a02e91
+ 0048b3a4 bytes 00a03e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822d808d49a9a3f5d1f2bff352613c79"></a>

### [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) → [`0048b544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md) FUN_0048b544

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0048b390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b390.md) [`00877be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877be0.md) [`00ac8520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`0048b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b3d0.md) [`00877c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877c20.md) [`00ac871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac871c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0048b550",
      "incomplete_value": false,
      "site": "0048b554",
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
    "old": {
      "definition_site": "0048b510",
      "incomplete_value": false,
      "site": "0048b514",
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
            "const:f0c:8"
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
      "0048b550",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048b550",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048b514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md#insn-0048b514) · [`0048b510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md#insn-0048b510)
- 新版 [`0048b554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md#insn-0048b554) · [`0048b550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b544.md#insn-0048b550)

~~~diff
- 0048b514 ["INT_ADD", "register:40f0:8", ["const:48b514:8", "const:4:8"]]
- 0048b514 ["CALL", null, ["callee:0043b778:8"]]
+ 0048b554 ["INT_ADD", "register:40f0:8", ["const:48b554:8", "const:4:8"]]
+ 0048b554 ["CALL", null, ["callee:0043b778:8"]]
- 0048b514 bytes 89c0fe97
+ 0048b554 bytes 89c0fe97
- 0048b510 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0048b510 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048b510 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048b510 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048b550 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0048b550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048b550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048b510 bytes 00303c91
+ 0048b550 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae68b9eeddc990e96f716f6762284d73"></a>

### [`0048bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md) → [`0048baf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md) _INIT_20

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00489f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f28.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00489f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f68.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00bfa110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 28件, `store_value` 15件, `unresolved_call_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048bb30",
      "incomplete_value": true,
      "site": "0048bb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048baf0",
      "incomplete_value": true,
      "site": "0048bb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "0048bb54",
      "incomplete_value": true,
      "site": "0048bb70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048bb14",
      "incomplete_value": true,
      "site": "0048bb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "0048bb74",
      "incomplete_value": true,
      "site": "0048bb90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048bb34",
      "incomplete_value": true,
      "site": "0048bb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "0048bb30",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0048bb54",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0048bb74",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048bb30",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0048bb54",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0048bb74",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048bb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md#insn-0048bb2c) · [`0048bb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md#insn-0048bb4c) · [`0048bc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md#insn-0048bc3c)
- 新版 [`0048bb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md#insn-0048bb6c) · [`0048bb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md#insn-0048bb8c) · [`0048bc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048baf0.md#insn-0048bc7c)

~~~diff
- 0048bb2c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0048bb2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0048bb2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0048bb2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0048bb6c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0048bb6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0048bb6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0048bb6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0048bb2c bytes 4a093691
+ 0048bb6c bytes 4a093791
- 0048bb4c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0048bb4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0048bb4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0048bb4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0048bb8c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0048bb8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0048bb8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0048bb8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0048bb4c bytes 4a553a91
+ 0048bb8c bytes 4a893d91
- 0048bc3c ["INT_ADD", "register:40f0:8", ["const:48bc3c:8", "const:4:8"]]
- 0048bc3c ["CALL", null, ["callee:0043b7f8:8"]]
+ 0048bc7c ["INT_ADD", "register:40f0:8", ["const:48bc7c:8", "const:4:8"]]
+ 0048bc7c ["CALL", null, ["callee:0043b7f8:8"]]
- 0048bc3c bytes dfbefe97
+ 0048bc7c bytes dfbefe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-416f68df31daa10f30360b49ac000497"></a>

### [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) → [`0048c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md) FUN_0048c000

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0048bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md) [`008b4a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b4/008b4a48.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00944614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00944/00944614.md) [`009a754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a7/009a754c.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 6件 [`0048c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md) [`008b4a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b4/008b4a8c.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009447b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/009447b0.md) [`009a76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a7/009a76e8.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c158",
      "incomplete_value": false,
      "site": "0048c160",
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
            "const:f53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c118",
      "incomplete_value": false,
      "site": "0048c120",
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
            "const:f13:8"
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
      "definition_site": "0048c214",
      "incomplete_value": false,
      "site": "0048c21c",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c1d4",
      "incomplete_value": false,
      "site": "0048c1dc",
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
            "const:da7:8"
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
      "definition_site": "0048c22c",
      "incomplete_value": false,
      "site": "0048c238",
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
            "const:ee9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c1ec",
      "incomplete_value": false,
      "site": "0048c1f8",
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
            "const:ea9:8"
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
      "0048c158",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0048c214",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0048c22c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048c158",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0048c214",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0048c22c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048c120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c120) · [`0048c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c1dc) · [`0048c1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bfc0.md#insn-0048c1f8)
- 新版 [`0048c160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md#insn-0048c160) · [`0048c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md#insn-0048c21c) · [`0048c238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md#insn-0048c238)

~~~diff
- 0048c120 ["INT_ADD", "register:40f0:8", ["const:48c120:8", "const:4:8"]]
- 0048c120 ["CALL", null, ["callee:00441e94:8"]]
+ 0048c160 ["INT_ADD", "register:40f0:8", ["const:48c160:8", "const:4:8"]]
+ 0048c160 ["CALL", null, ["callee:00441e94:8"]]
- 0048c120 bytes 4dd7fe97
+ 0048c160 bytes 4dd7fe97
- 0048c1dc ["INT_ADD", "register:40f0:8", ["const:48c1dc:8", "const:4:8"]]
- 0048c1dc ["CALL", null, ["callee:00441e94:8"]]
+ 0048c21c ["INT_ADD", "register:40f0:8", ["const:48c21c:8", "const:4:8"]]
+ 0048c21c ["CALL", null, ["callee:00441e94:8"]]
- 0048c1dc bytes 1ed7fe97
+ 0048c21c bytes 1ed7fe97
- 0048c1f8 ["INT_ADD", "register:40f0:8", ["const:48c1f8:8", "const:4:8"]]
- 0048c1f8 ["CALL", null, ["callee:004427f4:8"]]
+ 0048c238 ["INT_ADD", "register:40f0:8", ["const:48c238:8", "const:4:8"]]
+ 0048c238 ["CALL", null, ["callee:004427f4:8"]]
- 0048c1f8 bytes 6fd9fe97
+ 0048c238 bytes 6fd9fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29264e0450d869ace8aefc34da144ca"></a>

### [`0048c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md) → [`0048c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c938.md) _INIT_21

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048c974",
      "incomplete_value": true,
      "site": "0048c990",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048c934",
      "incomplete_value": true,
      "site": "0048c950",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "0048c998",
      "incomplete_value": true,
      "site": "0048c9b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048c958",
      "incomplete_value": true,
      "site": "0048c974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "0048c9b8",
      "incomplete_value": true,
      "site": "0048c9d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0048c978",
      "incomplete_value": true,
      "site": "0048c994",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "0048c974",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0048c998",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0048c9b8",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048c974",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0048c998",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0048c9b8",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048c970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048c970) · [`0048c990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048c990) · [`0048ca58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048c8f8.md#insn-0048ca58)
- 新版 [`0048c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c938.md#insn-0048c9b0) · [`0048c9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c938.md#insn-0048c9d0) · [`0048ca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c938.md#insn-0048ca98)

~~~diff
- 0048c970 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0048c970 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0048c970 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0048c970 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0048c9b0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0048c9b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0048c9b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0048c9b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0048c970 bytes 4a093691
+ 0048c9b0 bytes 4a093791
- 0048c990 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0048c990 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0048c990 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0048c990 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0048c9d0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0048c9d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0048c9d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0048c9d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0048c990 bytes 4a553a91
+ 0048c9d0 bytes 4a893d91
- 0048ca58 ["INT_ADD", "register:40f0:8", ["const:48ca58:8", "const:4:8"]]
- 0048ca58 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0048ca98 ["INT_ADD", "register:40f0:8", ["const:48ca98:8", "const:4:8"]]
+ 0048ca98 ["CALL", null, ["callee:0043b7f8:8"]]
- 0048ca58 bytes 58bbfe97
+ 0048ca98 bytes 58bbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a07612e0bf0c67945f3f79fa65d222d"></a>

### [`0048cc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cc88.md) → [`0048ccc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccc8.md) FUN_0048ccc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 0件 

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
      "definition_site": "0048cccc",
      "incomplete_value": false,
      "site": "0048ccd4",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048cc8c",
      "incomplete_value": false,
      "site": "0048cc94",
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
            "const:518:8"
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
      "0048ccd4",
      "DATA",
      [
        "storage",
        "00c65518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0048ccd4",
      "DATA",
      [
        "storage",
        "00c65918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cc88.md#insn-0048cc8c)
- 新版 [`0048cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccc8.md#insn-0048cccc)

~~~diff
- 0048cc8c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0048cc8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048cc8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048cc8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048cccc ["COPY", "tmp:0:8", ["const:918:8"]]
+ 0048cccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048cccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048cccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048cc8c bytes 08611491
+ 0048cccc bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8427b2d106d84f0e14d9866b9d2addae"></a>

### [`0048cf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md) → [`0048cf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md) FUN_0048cf68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0048cf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf24.md) · 呼出先 12件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 1件 [`0048cf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf64.md) · 呼出先 12件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048cfd0",
      "incomplete_value": true,
      "site": "0048cfd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0048cf90",
      "incomplete_value": true,
      "site": "0048cf94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048cfcc",
      "incomplete_value": true,
      "site": "0048cfd8",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048cf8c",
      "incomplete_value": true,
      "site": "0048cf98",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0048cfe0",
      "incomplete_value": true,
      "site": "0048cfe0",
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
                "const:10:8"
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
      "definition_site": "0048cfa0",
      "incomplete_value": true,
      "site": "0048cfa0",
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
                "const:10:8"
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
      "0048cfbc",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0048cfc0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0048cfcc",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0048cfbc",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0048cfc0",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "0048cfcc",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cfb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048cfb8) · [`0048cfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048cfd8) · [`0048d034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cf28.md#insn-0048d034)
- 新版 [`0048cff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md#insn-0048cff8) · [`0048d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md#insn-0048d018) · [`0048d074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md#insn-0048d074)

~~~diff
- 0048cfb8 ["INT_ADD", "register:40f0:8", ["const:48cfb8:8", "const:4:8"]]
- 0048cfb8 ["CALL", null, ["callee:00c581e0:8"]]
+ 0048cff8 ["INT_ADD", "register:40f0:8", ["const:48cff8:8", "const:4:8"]]
+ 0048cff8 ["CALL", null, ["callee:00c581e0:8"]]
- 0048cfb8 bytes 8a2b1f94
+ 0048cff8 bytes 7a2c1f94
- 0048cfd8 ["INT_ADD", "register:40f0:8", ["const:48cfd8:8", "const:4:8"]]
- 0048cfd8 ["CALL", null, ["callee:00c581f0:8"]]
+ 0048d018 ["INT_ADD", "register:40f0:8", ["const:48d018:8", "const:4:8"]]
+ 0048d018 ["CALL", null, ["callee:00c581f0:8"]]
- 0048cfd8 bytes 862b1f94
+ 0048d018 bytes 762c1f94
- 0048d034 ["INT_ADD", "register:40f0:8", ["const:48d034:8", "const:4:8"]]
- 0048d034 ["CALL", null, ["callee:00c58280:8"]]
+ 0048d074 ["INT_ADD", "register:40f0:8", ["const:48d074:8", "const:4:8"]]
+ 0048d074 ["CALL", null, ["callee:00c58280:8"]]
- 0048d034 bytes 932b1f94
+ 0048d074 bytes 832c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3266be62658ace03c3ede9345d5821a5"></a>

### [`0048d4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md) → [`0048d530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d530.md) FUN_0048d530

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 6件 [`0055f054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f054.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 6件 [`0055f094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f094.md) [`00597608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597608.md) [`00597618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597618.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.35% / 新版 99.35%

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
      "site": "0048d57c",
      "value": [
        "leaf",
        "ram:55f094:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0048d53c",
      "value": [
        "leaf",
        "ram:55f054:8"
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
      "0048d57c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055f054"
      ]
    ]
  ],
  "added": [
    [
      "0048d57c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055f094"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d53c) · [`0048d524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d524) · [`0048d550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d4f0.md#insn-0048d550)
- 新版 [`0048d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d530.md#insn-0048d57c) · [`0048d564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d530.md#insn-0048d564) · [`0048d590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d530.md#insn-0048d590)

~~~diff
- 0048d53c ["INT_ADD", "register:40f0:8", ["const:48d53c:8", "const:4:8"]]
- 0048d53c ["CALL", null, ["ram:55f054:8"]]
+ 0048d57c ["INT_ADD", "register:40f0:8", ["const:48d57c:8", "const:4:8"]]
+ 0048d57c ["CALL", null, ["ram:55f094:8"]]
- 0048d53c bytes c6460394
+ 0048d57c bytes c6460394
- 0048d524 ["INT_ADD", "register:40f0:8", ["const:48d524:8", "const:4:8"]]
- 0048d524 ["CALL", null, ["callee:00597608:8"]]
+ 0048d564 ["INT_ADD", "register:40f0:8", ["const:48d564:8", "const:4:8"]]
+ 0048d564 ["CALL", null, ["callee:00597608:8"]]
- 0048d524 bytes 29280494
+ 0048d564 bytes 29280494
- 0048d550 ["INT_ADD", "register:40f0:8", ["const:48d550:8", "const:4:8"]]
- 0048d550 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048d590 ["INT_ADD", "register:40f0:8", ["const:48d590:8", "const:4:8"]]
+ 0048d590 ["CALL", null, ["callee:00c53d00:8"]]
- 0048d550 bytes e4181f94
+ 0048d590 bytes dc191f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a4d40c1b796f3f1b00e7d79b0169156"></a>

### [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) → [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) FUN_0048dd40

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) [`00491390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0048cd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048cd34.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e154.md)
- 新版 呼出元 3件 [`00490b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md) [`004913d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md) [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048cd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cd74.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 74.51% / 新版 74.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `call_target` 1件, `store_destination` 24件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 5件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048dd88",
      "incomplete_value": true,
      "site": "0048dd88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:253:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048dd48",
      "incomplete_value": true,
      "site": "0048dd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:213:8"
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
      "definition_site": "0048dd7c",
      "incomplete_value": true,
      "site": "0048dd8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0048dd3c",
      "incomplete_value": true,
      "site": "0048dd4c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048dda8",
      "incomplete_value": true,
      "site": "0048ddc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:69d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048dd68",
      "incomplete_value": true,
      "site": "0048dd80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c1:8"
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
      "0048dd64",
      "READ",
      [
        "storage",
        "002bb213",
        null,
        "string"
      ]
    ],
    [
      "0048dd7c",
      "READ",
      [
        "storage",
        "002bb21a",
        null,
        "string"
      ]
    ],
    [
      "0048dda8",
      "READ",
      [
        "storage",
        "002a75c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048dd64",
      "READ",
      [
        "storage",
        "002bb253",
        null,
        "string"
      ]
    ],
    [
      "0048dd7c",
      "READ",
      [
        "storage",
        "002bb25a",
        null,
        "string"
      ]
    ],
    [
      "0048dda8",
      "READ",
      [
        "storage",
        "002a769d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md#insn-0048dd8c) · [`0048ddd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md#insn-0048ddd8) · [`0048de18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md#insn-0048de18)
- 新版 [`0048ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md#insn-0048ddcc) · [`0048de18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md#insn-0048de18) · [`0048de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md#insn-0048de58)

~~~diff
- 0048dd8c ["INT_ADD", "register:40f0:8", ["const:48dd8c:8", "const:4:8"]]
- 0048dd8c ["CALL", null, ["callee:0048e0b8:8"]]
+ 0048ddcc ["INT_ADD", "register:40f0:8", ["const:48ddcc:8", "const:4:8"]]
+ 0048ddcc ["CALL", null, ["callee:0048e0b8:8"]]
- 0048dd8c bytes bb000094
+ 0048ddcc bytes bb000094
- 0048ddd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0048ddd8 ["INT_ADD", "register:40f0:8", ["const:48ddd8:8", "const:4:8"]]
- 0048ddd8 ["CALLIND", null, ["register:0:8"]]
+ 0048de18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048de18 ["INT_ADD", "register:40f0:8", ["const:48de18:8", "const:4:8"]]
+ 0048de18 ["CALLIND", null, ["register:0:8"]]
- 0048ddd8 bytes 00013fd6
+ 0048de18 bytes 00013fd6
- 0048de18 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0048de58 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0048de18 bytes a84000f0
+ 0048de58 bytes c8400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3cc8cf3497a3013830abdaf29809ba1"></a>

### [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) → [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) FUN_0048eef0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 22件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) [`006a9724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a9/006a9724.md) · 呼出先 17件 [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md)
- 新版 呼出元 22件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`0062ecfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062e/0062ecfc.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) [`006a9764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a9/006a9764.md) · 呼出先 17件 [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048ec08.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md) [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048efa4",
      "incomplete_value": false,
      "site": "0048efa4",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048ef64",
      "incomplete_value": false,
      "site": "0048ef64",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f074",
      "incomplete_value": true,
      "site": "0048f074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048f034",
      "incomplete_value": true,
      "site": "0048f034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0048f074",
      "incomplete_value": false,
      "site": "0048f074",
      "value": [
        "leaf",
        "const:48f398:8"
      ]
    },
    "old": {
      "definition_site": "0048f034",
      "incomplete_value": false,
      "site": "0048f034",
      "value": [
        "leaf",
        "const:48f358:8"
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
      "0048ef9c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0048efa4",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f010",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048ef9c",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "0048efa4",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f010",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048efa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048efa4) · [`0048f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048f064) · [`0048f1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md#insn-0048f1ac)
- 新版 [`0048efe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md#insn-0048efe4) · [`0048f0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md#insn-0048f0a4) · [`0048f1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md#insn-0048f1ec)

~~~diff
- 0048efa4 ["INT_ADD", "register:40f0:8", ["const:48efa4:8", "const:4:8"]]
- 0048efa4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0048efe4 ["INT_ADD", "register:40f0:8", ["const:48efe4:8", "const:4:8"]]
+ 0048efe4 ["CALL", null, ["callee:00c53d00:8"]]
- 0048efa4 bytes 4f121f94
+ 0048efe4 bytes 47131f94
- 0048f064 ["INT_ADD", "register:40f0:8", ["const:48f064:8", "const:4:8"]]
- 0048f064 ["CALL", null, ["callee:00550a04:8"]]
+ 0048f0a4 ["INT_ADD", "register:40f0:8", ["const:48f0a4:8", "const:4:8"]]
+ 0048f0a4 ["CALL", null, ["callee:00550a04:8"]]
- 0048f064 bytes 58060394
+ 0048f0a4 bytes 58060394
- 0048f1ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f1ac ["INT_ADD", "register:40f0:8", ["const:48f1ac:8", "const:4:8"]]
- 0048f1ac ["CALLIND", null, ["register:0:8"]]
+ 0048f1ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f1ec ["INT_ADD", "register:40f0:8", ["const:48f1ec:8", "const:4:8"]]
+ 0048f1ec ["CALLIND", null, ["register:0:8"]]
- 0048f1ac bytes 00013fd6
+ 0048f1ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a4c11dd3fe350a1963332a9912c99d9"></a>

### [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) → [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md) FUN_0048f398

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) [`00491c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 9件 [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md) [`00491cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md) [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) · 呼出先 3件 [`005509fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509fc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048f3b4",
      "incomplete_value": false,
      "site": "0048f3b4",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f374",
      "incomplete_value": false,
      "site": "0048f374",
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
            "const:d10:8"
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
      "definition_site": "0048f3b4",
      "incomplete_value": false,
      "site": "0048f3b4",
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
                "const:110:8"
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
      "definition_site": "0048f374",
      "incomplete_value": false,
      "site": "0048f374",
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
                "const:d10:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0048f3b8",
      "incomplete_value": true,
      "site": "0048f3b8",
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
      "definition_site": "0048f378",
      "incomplete_value": true,
      "site": "0048f378",
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
      "0048f3b0",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f3b4",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f3b4",
      "WRITE",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0048f3b0",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f3b4",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f3b4",
      "WRITE",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f36c) · [`0048f364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f364) · [`0048f368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md#insn-0048f368)
- 新版 [`0048f3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md#insn-0048f3ac) · [`0048f3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md#insn-0048f3a4) · [`0048f3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md#insn-0048f3a8)

~~~diff
- 0048f36c ["COPY", "tmp:0:8", ["const:d10:8"]]
- 0048f36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048f36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048f36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048f3ac ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0048f3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048f3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048f36c bytes 08413491
+ 0048f3ac bytes 08410491
- 0048f364 ["INT_ADD", "register:40f0:8", ["const:48f364:8", "const:4:8"]]
- 0048f364 ["CALL", null, ["callee:005509fc:8"]]
+ 0048f3a4 ["INT_ADD", "register:40f0:8", ["const:48f3a4:8", "const:4:8"]]
+ 0048f3a4 ["CALL", null, ["callee:005509fc:8"]]
- 0048f364 bytes 96050394
+ 0048f3a4 bytes 96050394
- 0048f368 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0048f3a8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0048f368 bytes a84000b0
+ 0048f3a8 bytes a84000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d337ed4f52dca916e082572e5520302"></a>

### [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) → [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md) FUN_0048f460

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) [`00491390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md) · 呼出先 17件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00446378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446378.md) [`004497ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/004497ec.md) [`0044998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/0044998c.md) [`005509c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c8.md)
- 新版 呼出元 8件 [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md) [`00490b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md) [`004913d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md) · 呼出先 17件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004463b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004463b8.md) [`0044982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/0044982c.md) [`004499cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499cc.md) [`00550a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a08.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f7c4",
      "incomplete_value": true,
      "site": "0048f7d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:301:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f784",
      "incomplete_value": true,
      "site": "0048f798",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:234:8"
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
      "definition_site": "0048f7c8",
      "incomplete_value": true,
      "site": "0048f7dc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0048f788",
      "incomplete_value": true,
      "site": "0048f79c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048f7cc",
      "incomplete_value": true,
      "site": "0048f7e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f78c",
      "incomplete_value": true,
      "site": "0048f7a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048f578",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f644",
      "PARAM",
      [
        "storage",
        "002ae653",
        null,
        "string"
      ]
    ],
    [
      "0048f650",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00446378"
      ]
    ]
  ],
  "added": [
    [
      "0048f578",
      "READ",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "0048f644",
      "PARAM",
      [
        "storage",
        "002ae693",
        null,
        "string"
      ]
    ],
    [
      "0048f650",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004463b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f55c) · [`0048f610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f610) · [`0048f758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md#insn-0048f758)
- 新版 [`0048f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md#insn-0048f59c) · [`0048f650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md#insn-0048f650) · [`0048f798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md#insn-0048f798)

~~~diff
- 0048f55c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048f55c ["INT_ADD", "register:40f0:8", ["const:48f55c:8", "const:4:8"]]
- 0048f55c ["CALLIND", null, ["register:0:8"]]
+ 0048f59c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0048f59c ["INT_ADD", "register:40f0:8", ["const:48f59c:8", "const:4:8"]]
+ 0048f59c ["CALLIND", null, ["register:0:8"]]
- 0048f55c bytes 00013fd6
+ 0048f59c bytes 00013fd6
- 0048f610 ["INT_ADD", "register:40f0:8", ["const:48f610:8", "const:4:8"]]
- 0048f610 ["CALL", null, ["ram:446378:8"]]
+ 0048f650 ["INT_ADD", "register:40f0:8", ["const:48f650:8", "const:4:8"]]
+ 0048f650 ["CALL", null, ["ram:4463b8:8"]]
- 0048f610 bytes 5adbfe97
+ 0048f650 bytes 5adbfe97
- 0048f758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c40:8"]]
- 0048f758 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0048f758 ["COPY", "register:5008:8", ["const:0:8"]]
- 0048f758 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0048f798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
+ 0048f798 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048f798 ["COPY", "register:5008:8", ["const:0:8"]]
+ 0048f798 ["COPY", "register:5010:8", ["const:0:8"]]
- 0048f758 bytes 002146fd
+ 0048f798 bytes 004146fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ce31f0b176398e768d730c90742578"></a>

### [`00490134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md) → [`00490174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md) FUN_00490174

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 21件 [`0046cac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cac4.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 21件 [`0046cb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb04.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048ec08.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.59% / 新版 87.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004901d8",
      "incomplete_value": true,
      "site": "004901ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490198",
      "incomplete_value": true,
      "site": "004901ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:186:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004902b0",
      "incomplete_value": false,
      "site": "004902b0",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490270",
      "incomplete_value": false,
      "site": "00490270",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490358",
      "incomplete_value": true,
      "site": "00490358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00490318",
      "incomplete_value": true,
      "site": "00490318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "004901d8",
      "READ",
      [
        "storage",
        "002b7186",
        null,
        "string"
      ]
    ],
    [
      "004901fc",
      "READ",
      [
        "storage",
        "002c3d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00490224",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004901d8",
      "READ",
      [
        "storage",
        "002b71c6",
        null,
        "string"
      ]
    ],
    [
      "004901fc",
      "READ",
      [
        "storage",
        "002c3da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00490224",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004901ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-004901ec) · [`004902b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-004902b0) · [`004902d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490134.md#insn-004902d8)
- 新版 [`0049022c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md#insn-0049022c) · [`004902f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md#insn-004902f0) · [`00490318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490174.md#insn-00490318)

~~~diff
- 004901ec ["INT_ADD", "register:40f0:8", ["const:4901ec:8", "const:4:8"]]
- 004901ec ["CALL", null, ["ram:46cac4:8"]]
+ 0049022c ["INT_ADD", "register:40f0:8", ["const:49022c:8", "const:4:8"]]
+ 0049022c ["CALL", null, ["ram:46cb04:8"]]
- 004901ec bytes 3672ff97
+ 0049022c bytes 3672ff97
- 004902b0 ["INT_ADD", "register:40f0:8", ["const:4902b0:8", "const:4:8"]]
- 004902b0 ["CALL", null, ["callee:00c53d00:8"]]
+ 004902f0 ["INT_ADD", "register:40f0:8", ["const:4902f0:8", "const:4:8"]]
+ 004902f0 ["CALL", null, ["callee:00c53d00:8"]]
- 004902b0 bytes 8c0d1f94
+ 004902f0 bytes 840e1f94
- 004902d8 ["COPY", "register:40c0:8", ["const:ca4000:8"]]
+ 00490318 ["COPY", "register:40c0:8", ["const:ca5000:8"]]
- 004902d8 bytes b8400090
+ 00490318 bytes b84000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-795f4708a0776f32051fb96efd145c4d"></a>

### [`0049065c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md) → [`0049069c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md) FUN_0049069c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) · 呼出先 17件 [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md)
- 新版 呼出元 1件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) · 呼出先 17件 [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048ec08.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md) [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490780",
      "incomplete_value": false,
      "site": "00490780",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490740",
      "incomplete_value": false,
      "site": "00490740",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490814",
      "incomplete_value": true,
      "site": "00490814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004907d4",
      "incomplete_value": true,
      "site": "004907d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00490814",
      "incomplete_value": false,
      "site": "00490814",
      "value": [
        "leaf",
        "const:48f398:8"
      ]
    },
    "old": {
      "definition_site": "004907d4",
      "incomplete_value": false,
      "site": "004907d4",
      "value": [
        "leaf",
        "const:48f358:8"
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
      "0049070c",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00490714",
      "READ",
      [
        "storage",
        "00ca4894",
        null,
        "undefined4"
      ]
    ],
    [
      "00490778",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049070c",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00490714",
      "READ",
      [
        "storage",
        "00ca4c94",
        null,
        "undefined4"
      ]
    ],
    [
      "00490778",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00490728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-00490728) · [`00490780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-00490780) · [`00490794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/0049065c.md#insn-00490794)
- 新版 [`00490768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md#insn-00490768) · [`004907c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md#insn-004907c0) · [`004907d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/0049069c.md#insn-004907d4)

~~~diff
- 00490728 ["INT_ADD", "register:40f0:8", ["const:490728:8", "const:4:8"]]
- 00490728 ["CALL", null, ["callee:00550a0c:8"]]
+ 00490768 ["INT_ADD", "register:40f0:8", ["const:490768:8", "const:4:8"]]
+ 00490768 ["CALL", null, ["callee:00550a0c:8"]]
- 00490728 bytes a9000394
+ 00490768 bytes a9000394
- 00490780 ["INT_ADD", "register:40f0:8", ["const:490780:8", "const:4:8"]]
- 00490780 ["CALL", null, ["callee:00c53d00:8"]]
+ 004907c0 ["INT_ADD", "register:40f0:8", ["const:4907c0:8", "const:4:8"]]
+ 004907c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00490780 bytes 580c1f94
+ 004907c0 bytes 500d1f94
- 00490794 ["COPY", "register:0:8", ["register:4040:8"]]
- 00490794 ["INT_ADD", "register:40f0:8", ["const:490794:8", "const:4:8"]]
- 00490794 ["CALLIND", null, ["register:0:8"]]
+ 004907d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004907d4 ["INT_ADD", "register:40f0:8", ["const:4907d4:8", "const:4:8"]]
+ 004907d4 ["CALLIND", null, ["register:0:8"]]
- 00490794 bytes 00013fd6
+ 004907d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff003bf4e86f75bd23ab837196a4a8e"></a>

### [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) → [`00490b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md) FUN_00490b34

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) · 呼出先 21件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0046cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cb1c.md) [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md)
- 新版 呼出元 3件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) · 呼出先 21件 [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`0046cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb5c.md) [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e4f0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00490bbc",
      "incomplete_value": false,
      "site": "00490bbc",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490b7c",
      "incomplete_value": false,
      "site": "00490b7c",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00490f00",
      "incomplete_value": false,
      "site": "00490f00",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490ec0",
      "incomplete_value": false,
      "site": "00490ec0",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00490fc0",
      "incomplete_value": true,
      "site": "00490fd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00490f80",
      "incomplete_value": true,
      "site": "00490f94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
              ]
            ]
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
      "00490bb4",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00490bbc",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00490c60",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00490bb4",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "00490bbc",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00490c60",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00490bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-00490bbc) · [`00490f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-00490f54) · [`00490f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md#insn-00490f60)
- 新版 [`00490bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md#insn-00490bfc) · [`00490f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md#insn-00490f94) · [`00490fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md#insn-00490fa0)

~~~diff
- 00490bbc ["INT_ADD", "register:40f0:8", ["const:490bbc:8", "const:4:8"]]
- 00490bbc ["CALL", null, ["callee:00c53d00:8"]]
+ 00490bfc ["INT_ADD", "register:40f0:8", ["const:490bfc:8", "const:4:8"]]
+ 00490bfc ["CALL", null, ["callee:00c53d00:8"]]
- 00490bbc bytes 490b1f94
+ 00490bfc bytes 410c1f94
- 00490f54 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:768:8"]]
- 00490f54 ["LOAD", "register:4060:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490f94 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:b68:8"]]
+ 00490f94 ["LOAD", "register:4060:8", ["const:1b1:8", "tmp:0:8"]]
- 00490f54 bytes 8cb543f9
+ 00490f94 bytes 8cb545f9
- 00490f60 ["INT_ADD", "register:40f0:8", ["const:490f60:8", "const:4:8"]]
- 00490f60 ["CALL", null, ["callee:0046cb5c:8"]]
+ 00490fa0 ["INT_ADD", "register:40f0:8", ["const:490fa0:8", "const:4:8"]]
+ 00490fa0 ["CALL", null, ["callee:0046cb5c:8"]]
- 00490f60 bytes ef6eff97
+ 00490fa0 bytes ef6eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64216222c0e823e33ee6e04aedca6cad"></a>

### [`00491390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md) → [`004913d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md) FUN_004913d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0083f428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f428.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) · 呼出先 20件 [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`00493f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493f70.md)
- 新版 呼出元 3件 [`0083f468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f468.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0086f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f91c.md) · 呼出先 20件 [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e4f0.md) [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md) [`00493fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493fb0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.84% / 新版 87.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00491484",
      "incomplete_value": false,
      "site": "00491484",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491444",
      "incomplete_value": false,
      "site": "00491444",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004917fc",
      "incomplete_value": false,
      "site": "004917fc",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004917bc",
      "incomplete_value": false,
      "site": "004917bc",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004918a8",
      "incomplete_value": true,
      "site": "004918c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491868",
      "incomplete_value": true,
      "site": "00491884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049147c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00491484",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00491510",
      "READ",
      [
        "storage",
        "002c4380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0049147c",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "00491484",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00491510",
      "READ",
      [
        "storage",
        "002c43c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00491488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-00491488) · [`004917fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-004917fc) · [`004918d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491390.md#insn-004918d4)
- 新版 [`004914c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md#insn-004914c8) · [`0049183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md#insn-0049183c) · [`00491914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md#insn-00491914)

~~~diff
- 00491488 ["INT_ADD", "register:40f0:8", ["const:491488:8", "const:4:8"]]
- 00491488 ["CALL", null, ["callee:00c53d00:8"]]
+ 004914c8 ["INT_ADD", "register:40f0:8", ["const:4914c8:8", "const:4:8"]]
+ 004914c8 ["CALL", null, ["callee:00c53d00:8"]]
- 00491488 bytes 16091f94
+ 004914c8 bytes 0e0a1f94
- 004917fc ["INT_ADD", "register:40f0:8", ["const:4917fc:8", "const:4:8"]]
- 004917fc ["CALL", null, ["callee:00c53d00:8"]]
+ 0049183c ["INT_ADD", "register:40f0:8", ["const:49183c:8", "const:4:8"]]
+ 0049183c ["CALL", null, ["callee:00c53d00:8"]]
- 004917fc bytes 39081f94
+ 0049183c bytes 31091f94
- 004918d4 ["INT_ADD", "register:40f0:8", ["const:4918d4:8", "const:4:8"]]
- 004918d4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00491914 ["INT_ADD", "register:40f0:8", ["const:491914:8", "const:4:8"]]
+ 00491914 ["CALL", null, ["callee:00c53d00:8"]]
- 004918d4 bytes 03081f94
+ 00491914 bytes fb081f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96310f9843c2de5535f8502f6e30bbeb"></a>

### [`00491c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md) → [`00491cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md) FUN_00491cbc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0062b6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062b6d4.md) · 呼出先 17件 [`0046cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cb1c.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)
- 新版 呼出元 1件 [`0062b714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062b/0062b714.md) · 呼出先 17件 [`0046cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb5c.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048ec08.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00491d40",
      "incomplete_value": false,
      "site": "00491d40",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491d00",
      "incomplete_value": false,
      "site": "00491d00",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00491e04",
      "incomplete_value": true,
      "site": "00491e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00491dc4",
      "incomplete_value": true,
      "site": "00491dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00491e04",
      "incomplete_value": false,
      "site": "00491e04",
      "value": [
        "leaf",
        "const:48f398:8"
      ]
    },
    "old": {
      "definition_site": "00491dc4",
      "incomplete_value": false,
      "site": "00491dc4",
      "value": [
        "leaf",
        "const:48f358:8"
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
      "00491d38",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d40",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00491dac",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00491d38",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "00491d40",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00491dac",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00491d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491d40) · [`00491d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491d98) · [`00491f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00491/00491c7c.md#insn-00491f18)
- 新版 [`00491d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md#insn-00491d80) · [`00491dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md#insn-00491dd8) · [`00491f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/00491cbc.md#insn-00491f58)

~~~diff
- 00491d40 ["INT_ADD", "register:40f0:8", ["const:491d40:8", "const:4:8"]]
- 00491d40 ["CALL", null, ["callee:00c53d00:8"]]
+ 00491d80 ["INT_ADD", "register:40f0:8", ["const:491d80:8", "const:4:8"]]
+ 00491d80 ["CALL", null, ["callee:00c53d00:8"]]
- 00491d40 bytes e8061f94
+ 00491d80 bytes e0071f94
- 00491d98 ["INT_ADD", "register:40f0:8", ["const:491d98:8", "const:4:8"]]
- 00491d98 ["CALL", null, ["callee:0046cb5c:8"]]
+ 00491dd8 ["INT_ADD", "register:40f0:8", ["const:491dd8:8", "const:4:8"]]
+ 00491dd8 ["CALL", null, ["callee:0046cb5c:8"]]
- 00491d98 bytes 616bff97
+ 00491dd8 bytes 616bff97
- 00491f18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00491f18 ["INT_ADD", "register:40f0:8", ["const:491f18:8", "const:4:8"]]
- 00491f18 ["CALLIND", null, ["register:0:8"]]
+ 00491f58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00491f58 ["INT_ADD", "register:40f0:8", ["const:491f58:8", "const:4:8"]]
+ 00491f58 ["CALLIND", null, ["register:0:8"]]
- 00491f18 bytes 00013fd6
+ 00491f58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e1d76e1f7342f618d23619cdaf907c5"></a>

### [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) → [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) FUN_00492120

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006da630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 17件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e8c0.md) [`0048ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048ebc8.md) [`0048f358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f358.md)
- 新版 呼出元 6件 [`006da670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da670.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 17件 [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) [`0048ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048ec08.md) [`0048f398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f398.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.22% / 新版 86.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492198",
      "incomplete_value": false,
      "site": "00492198",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492158",
      "incomplete_value": false,
      "site": "00492158",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492250",
      "incomplete_value": true,
      "site": "00492250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00492210",
      "incomplete_value": true,
      "site": "00492210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00492250",
      "incomplete_value": false,
      "site": "00492250",
      "value": [
        "leaf",
        "const:48f398:8"
      ]
    },
    "old": {
      "definition_site": "00492210",
      "incomplete_value": false,
      "site": "00492210",
      "value": [
        "leaf",
        "const:48f358:8"
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
      "00492190",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00492198",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492204",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00492190",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "00492198",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00492204",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-00492198) · [`004921d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-004921d0) · [`004921e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md#insn-004921e4)
- 新版 [`004921d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md#insn-004921d8) · [`00492210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md#insn-00492210) · [`00492224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md#insn-00492224)

~~~diff
- 00492198 ["INT_ADD", "register:40f0:8", ["const:492198:8", "const:4:8"]]
- 00492198 ["CALL", null, ["callee:00c53d00:8"]]
+ 004921d8 ["INT_ADD", "register:40f0:8", ["const:4921d8:8", "const:4:8"]]
+ 004921d8 ["CALL", null, ["callee:00c53d00:8"]]
- 00492198 bytes d2051f94
+ 004921d8 bytes ca061f94
- 004921d0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d10:8"]]
- 004921d0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492210 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:110:8"]]
+ 00492210 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 004921d0 bytes 168b46f9
+ 00492210 bytes 168b40f9
- 004921e4 ["INT_ADD", "register:40f0:8", ["const:4921e4:8", "const:4:8"]]
- 004921e4 ["CALL", null, ["callee:0046cb0c:8"]]
+ 00492224 ["INT_ADD", "register:40f0:8", ["const:492224:8", "const:4:8"]]
+ 00492224 ["CALL", null, ["callee:0046cb0c:8"]]
- 004921e4 bytes 3a6aff97
+ 00492224 bytes 3a6aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ecd25bde16a4fbb1be773cbc8a68e27"></a>

### [`0049252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md) → [`0049256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md) FUN_0049256c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 1件 [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md)
- 新版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 1件 [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0049258c",
      "incomplete_value": true,
      "site": "0049258c",
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
      "definition_site": "0049254c",
      "incomplete_value": true,
      "site": "0049254c",
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
      "definition_site": "0049264c",
      "incomplete_value": false,
      "site": "00492650",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049260c",
      "incomplete_value": false,
      "site": "00492610",
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
            "const:870:8"
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
      "definition_site": "00492688",
      "incomplete_value": false,
      "site": "0049268c",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492648",
      "incomplete_value": false,
      "site": "0049264c",
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
            "const:870:8"
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
      "00492588",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492598",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "004925a0",
      "READ",
      [
        "storage",
        "00ca489c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00492588",
      "READ",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00492598",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "004925a0",
      "READ",
      [
        "storage",
        "00ca4c9c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004925d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-004925d0) · [`0049260c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-0049260c) · [`00492610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md#insn-00492610)
- 新版 [`00492610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md#insn-00492610) · [`0049264c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md#insn-0049264c) · [`00492650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md#insn-00492650)

~~~diff
- 004925d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004925d0 ["INT_ADD", "register:40f0:8", ["const:4925d0:8", "const:4:8"]]
- 004925d0 ["CALLIND", null, ["register:0:8"]]
+ 00492610 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00492610 ["INT_ADD", "register:40f0:8", ["const:492610:8", "const:4:8"]]
+ 00492610 ["CALLIND", null, ["register:0:8"]]
- 004925d0 bytes 20013fd6
+ 00492610 bytes 20013fd6
- 0049260c ["COPY", "tmp:0:8", ["const:870:8"]]
- 0049260c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049260c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049260c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049264c ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0049264c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049264c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049264c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049260c bytes 00c02191
+ 0049264c bytes 00c03191
- 00492610 ["INT_ADD", "register:40f0:8", ["const:492610:8", "const:4:8"]]
- 00492610 ["CALL", null, ["callee:0046cb0c:8"]]
+ 00492650 ["INT_ADD", "register:40f0:8", ["const:492650:8", "const:4:8"]]
+ 00492650 ["CALL", null, ["callee:0046cb0c:8"]]
- 00492610 bytes 2f69ff97
+ 00492650 bytes 2f69ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7bee68f58ae70e9d4113e408c8533a"></a>

### [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) → [`004928ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) FUN_004928ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 29件 [`007aecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ae/007aecf8.md) [`008650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/008650d0.md) [`00871fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00871/00871fe0.md) [`00872210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00872/00872210.md) [`0087f0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f0cc.md) · 呼出先 9件 [`0048dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dd00.md) [`0048e078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`0048e4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e4b0.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`00493f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493f70.md)
- 新版 呼出元 29件 [`007aed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md) [`00865110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) [`00872020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872020.md) [`00872250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/00872250.md) [`0087f10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f10c.md) · 呼出先 9件 [`0048dd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e4f0.md) [`0048f460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048f/0048f460.md) [`00493fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.30% / 新版 84.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492968",
      "incomplete_value": true,
      "site": "00492968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00492928",
      "incomplete_value": true,
      "site": "00492928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00492968",
      "incomplete_value": false,
      "site": "00492968",
      "value": [
        "leaf",
        "const:48e4f0:8"
      ]
    },
    "old": {
      "definition_site": "00492928",
      "incomplete_value": false,
      "site": "00492928",
      "value": [
        "leaf",
        "const:48e4b0:8"
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00492980",
      "incomplete_value": true,
      "site": "00492980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00492940",
      "incomplete_value": true,
      "site": "00492940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049294c",
      "READ",
      [
        "storage",
        "00c9a8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00492950",
      "READ",
      [
        "storage",
        "00c9a8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00492968",
      "DATA",
      [
        "storage",
        "00c655f8",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0049294c",
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      "00492950",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00492968",
      "DATA",
      [
        "storage",
        "00c659f8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-0049291c) · [`0049295c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-0049295c) · [`004928c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md#insn-004928c0)
- 新版 [`0049295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md#insn-0049295c) · [`0049299c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md#insn-0049299c) · [`00492900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md#insn-00492900)

~~~diff
- 0049291c ["COPY", "register:4048:8", ["const:48e4b0:8"]]
+ 0049295c ["COPY", "register:4048:8", ["const:48e4f0:8"]]
- 0049291c bytes a9dcfd10
+ 0049295c bytes a9dcfd10
- 0049295c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049295c ["INT_ADD", "register:40f0:8", ["const:49295c:8", "const:4:8"]]
- 0049295c ["CALLIND", null, ["register:0:8"]]
+ 0049299c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0049299c ["INT_ADD", "register:40f0:8", ["const:49299c:8", "const:4:8"]]
+ 0049299c ["CALLIND", null, ["register:0:8"]]
- 0049295c bytes 00013fd6
+ 0049299c bytes 00013fd6
- 004928c0 ["INT_ADD", "register:40f0:8", ["const:4928c0:8", "const:4:8"]]
- 004928c0 ["CALL", null, ["callee:0048e0b8:8"]]
+ 00492900 ["INT_ADD", "register:40f0:8", ["const:492900:8", "const:4:8"]]
+ 00492900 ["CALL", null, ["callee:0048e0b8:8"]]
- 004928c0 bytes eeedff97
+ 00492900 bytes eeedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ae6a2d9a17a3e47c96a254556bcfc10"></a>

### [`00492ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md) → [`00492b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492b20.md) FUN_00492b20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00893b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893b40.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00893b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893b84.md) · 呼出先 3件 [`005509fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509fc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.93% / 新版 83.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492b70",
      "incomplete_value": false,
      "site": "00492b70",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492b30",
      "incomplete_value": false,
      "site": "00492b30",
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
            "const:d10:8"
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
      "definition_site": "00492b70",
      "incomplete_value": false,
      "site": "00492b70",
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
                "const:110:8"
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
      "definition_site": "00492b30",
      "incomplete_value": false,
      "site": "00492b30",
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
                "const:d10:8"
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492b38",
      "incomplete_value": true,
      "site": "00492b38",
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
      "definition_site": "00492af8",
      "incomplete_value": true,
      "site": "00492af8",
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
      "00492b34",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b50",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b6c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492b34",
      "READ",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b50",
      "READ",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00492b6c",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492af4) · [`00492b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492b5c) · [`00492b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ae0.md#insn-00492b74)
- 新版 [`00492b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492b20.md#insn-00492b34) · [`00492b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492b20.md#insn-00492b9c) · [`00492bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492b20.md#insn-00492bb4)

~~~diff
- 00492af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
- 00492af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492b34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:110:8"]]
+ 00492b34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00492af4 bytes 888a46f9
+ 00492b34 bytes 888a40f9
- 00492b5c ["INT_ADD", "register:40f0:8", ["const:492b5c:8", "const:4:8"]]
- 00492b5c ["CALL", null, ["callee:00c57e80:8"]]
+ 00492b9c ["INT_ADD", "register:40f0:8", ["const:492b9c:8", "const:4:8"]]
+ 00492b9c ["CALL", null, ["callee:00c57e80:8"]]
- 00492b5c bytes c9131f94
+ 00492b9c bytes b9141f94
- 00492b74 ["INT_ADD", "register:40f0:8", ["const:492b74:8", "const:4:8"]]
- 00492b74 ["CALL", null, ["callee:00c53d00:8"]]
+ 00492bb4 ["INT_ADD", "register:40f0:8", ["const:492bb4:8", "const:4:8"]]
+ 00492bb4 ["CALL", null, ["callee:00c53d00:8"]]
- 00492b74 bytes 5b031f94
+ 00492bb4 bytes 53041f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6271a7c7d55424f7d724334bbea74ccc"></a>

### [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md) → [`00492c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md) FUN_00492c00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`007ac380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007ac380.md) [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 3件 [`005509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509bc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 11件 [`007ac3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`0088018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/0088018c.md) [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`005509fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509fc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00492c20",
      "incomplete_value": false,
      "site": "00492c20",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492be0",
      "incomplete_value": false,
      "site": "00492be0",
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
            "const:d10:8"
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
      "definition_site": "00492c20",
      "incomplete_value": false,
      "site": "00492c20",
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
                "const:110:8"
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
      "definition_site": "00492be0",
      "incomplete_value": false,
      "site": "00492be0",
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
                "const:d10:8"
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00492c24",
      "incomplete_value": true,
      "site": "00492c24",
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
      "definition_site": "00492be4",
      "incomplete_value": true,
      "site": "00492be4",
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
      "00492c1c",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00492c20",
      "WRITE",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00492c20",
      "WRITE",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00492c1c",
      "READ",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ],
    [
      "00492c20",
      "WRITE",
      [
        "storage",
        "00ca5110",
        null,
        "undefined8"
      ]
    ],
    [
      "00492c20",
      "WRITE",
      [
        "storage",
        "00ca5118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492c0c) · [`00492c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492c24) · [`00492bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md#insn-00492bd0)
- 新版 [`00492c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md#insn-00492c4c) · [`00492c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md#insn-00492c64) · [`00492c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492c00.md#insn-00492c10)

~~~diff
- 00492c0c ["INT_ADD", "register:40f0:8", ["const:492c0c:8", "const:4:8"]]
- 00492c0c ["CALL", null, ["callee:00c57e80:8"]]
+ 00492c4c ["INT_ADD", "register:40f0:8", ["const:492c4c:8", "const:4:8"]]
+ 00492c4c ["CALL", null, ["callee:00c57e80:8"]]
- 00492c0c bytes 9d131f94
+ 00492c4c bytes 8d141f94
- 00492c24 ["INT_ADD", "register:40f0:8", ["const:492c24:8", "const:4:8"]]
- 00492c24 ["CALL", null, ["callee:00c53d00:8"]]
+ 00492c64 ["INT_ADD", "register:40f0:8", ["const:492c64:8", "const:4:8"]]
+ 00492c64 ["CALL", null, ["callee:00c53d00:8"]]
- 00492c24 bytes 2f031f94
+ 00492c64 bytes 27041f94
- 00492bd0 ["INT_ADD", "register:40f0:8", ["const:492bd0:8", "const:4:8"]]
- 00492bd0 ["CALL", null, ["callee:005509fc:8"]]
+ 00492c10 ["INT_ADD", "register:40f0:8", ["const:492c10:8", "const:4:8"]]
+ 00492c10 ["CALL", null, ["callee:005509fc:8"]]
- 00492bd0 bytes 7bf70294
+ 00492c10 bytes 7bf70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753c479f836a3016e4fe23283f937a23"></a>

### [`00492fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md) → [`00493008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md) FUN_00493008

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`00494444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494444.md) [`00494448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494448.md) [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md)
- 新版 呼出元 5件 [`00492f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492f28.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004932d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932d4.md) [`00494484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494484.md) [`00494488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494488.md) [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493058",
      "incomplete_value": false,
      "site": "00493058",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493018",
      "incomplete_value": false,
      "site": "00493018",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00493074",
      "incomplete_value": false,
      "site": "00493074",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493034",
      "incomplete_value": false,
      "site": "00493034",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493140",
      "incomplete_value": true,
      "site": "00493140",
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
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00493100",
      "incomplete_value": true,
      "site": "00493100",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00493044",
      "READ",
      [
        "storage",
        "00ca4da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00493050",
      "READ",
      [
        "storage",
        "00ca4d80",
        null,
        "undefined4"
      ]
    ],
    [
      "00493058",
      "WRITE",
      [
        "storage",
        "00ca4d80",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00493044",
      "READ",
      [
        "storage",
        "00ca51a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00493050",
      "READ",
      [
        "storage",
        "00ca5180",
        null,
        "undefined4"
      ]
    ],
    [
      "00493058",
      "WRITE",
      [
        "storage",
        "00ca5180",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00493018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-00493018) · [`00493100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-00493100) · [`004931cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492fc8.md#insn-004931cc)
- 新版 [`00493058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md#insn-00493058) · [`00493140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md#insn-00493140) · [`0049320c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493008.md#insn-0049320c)

~~~diff
- 00493018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00493018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
+ 00493058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:180:8"]]
+ 00493058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
- 00493018 bytes 15810db9
+ 00493058 bytes 158101b9
- 00493100 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d88:8"]]
- 00493100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00493140 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:188:8"]]
+ 00493140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00493100 bytes 09c506f9
+ 00493140 bytes 09c500f9
- 004931cc ["INT_ADD", "register:40f0:8", ["const:4931cc:8", "const:4:8"]]
- 004931cc ["CALL", null, ["callee:00c57e50:8"]]
+ 0049320c ["INT_ADD", "register:40f0:8", ["const:49320c:8", "const:4:8"]]
+ 0049320c ["CALL", null, ["callee:00c57e50:8"]]
- 004931cc bytes 21121f94
+ 0049320c bytes 11131f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a424b0d8aedc49a23c392eef64ab14"></a>

### [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md) → [`004932dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md) FUN_004932dc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`0086f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086f/0086f8dc.md) [`00883118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00493294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493294.md) [`00494b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b3c.md) [`005509d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 4件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`0086f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f91c.md) [`00883158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00883/00883158.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004932d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932d4.md) [`00494b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494b7c.md) [`00550a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 89.45% / 新版 89.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00493334",
      "incomplete_value": false,
      "site": "00493334",
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
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004932f4",
      "incomplete_value": false,
      "site": "004932f4",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049339c",
      "incomplete_value": false,
      "site": "0049339c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049335c",
      "incomplete_value": false,
      "site": "0049335c",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004934ec",
      "incomplete_value": true,
      "site": "004934ec",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004934ac",
      "incomplete_value": true,
      "site": "004934ac",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049331c",
      "READ",
      [
        "storage",
        "00ca4dc8",
        null,
        "undefined1"
      ]
    ],
    [
      "0049332c",
      "READ",
      [
        "storage",
        "00ca4da8",
        null,
        "undefined4"
      ]
    ],
    [
      "00493334",
      "WRITE",
      [
        "storage",
        "00ca4da8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0049331c",
      "READ",
      [
        "storage",
        "00ca51c8",
        null,
        "undefined1"
      ]
    ],
    [
      "0049332c",
      "READ",
      [
        "storage",
        "00ca51a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00493334",
      "WRITE",
      [
        "storage",
        "00ca51a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004932f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-004932f4) · [`004933f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-004933f8) · [`004934ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md#insn-004934ac)
- 新版 [`00493334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md#insn-00493334) · [`00493438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md#insn-00493438) · [`004934ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004932dc.md#insn-004934ec)

~~~diff
- 004932f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
- 004932f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 00493334 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
+ 00493334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 004932f4 bytes 18a90db9
+ 00493334 bytes 18a901b9
- 004933f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004933f8 ["INT_ADD", "register:40f0:8", ["const:4933f8:8", "const:4:8"]]
- 004933f8 ["CALLIND", null, ["register:0:8"]]
+ 00493438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00493438 ["INT_ADD", "register:40f0:8", ["const:493438:8", "const:4:8"]]
+ 00493438 ["CALLIND", null, ["register:0:8"]]
- 004933f8 bytes 00013fd6
+ 00493438 bytes 00013fd6
- 004934ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
- 004934ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 004934ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
+ 004934ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 004934ac bytes 09d906f9
+ 004934ec bytes 09d900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-364c9b8e3bd6d16ea30e0c6a1273498d"></a>

### [`0049404c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md) → [`0049408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049408c.md) FUN_0049408c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "004940ac",
      "incomplete_value": false,
      "site": "004940b0",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049406c",
      "incomplete_value": false,
      "site": "00494070",
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
            "const:758:8"
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
      "004940b0",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004940b0",
      "DATA",
      [
        "storage",
        "00c65b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md#insn-00494060) · [`0049406c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049404c.md#insn-0049406c)
- 新版 [`004940a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049408c.md#insn-004940a0) · [`004940ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049408c.md#insn-004940ac)

~~~diff
- 00494060 ["INT_ADD", "register:40f0:8", ["const:494060:8", "const:4:8"]]
- 00494060 ["CALL", null, ["callee:00c57e90:8"]]
+ 004940a0 ["INT_ADD", "register:40f0:8", ["const:4940a0:8", "const:4:8"]]
+ 004940a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00494060 bytes 8c0e1f94
+ 004940a0 bytes 7c0f1f94
- 0049406c ["COPY", "tmp:0:8", ["const:758:8"]]
- 0049406c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049406c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049406c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004940ac ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 004940ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004940ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004940ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049406c bytes 08611d91
+ 004940ac bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a8ba876b4b1d119181adcda3b72d7a"></a>

### [`00494084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494084.md) → [`004940c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004940c4.md) FUN_004940c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004940c8",
      "incomplete_value": false,
      "site": "004940cc",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494088",
      "incomplete_value": false,
      "site": "0049408c",
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
            "const:758:8"
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
      "004940cc",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004940cc",
      "DATA",
      [
        "storage",
        "00c65b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494084.md#insn-00494088)
- 新版 [`004940c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004940c4.md#insn-004940c8)

~~~diff
- 00494088 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00494088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004940c8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 004940c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004940c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004940c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494088 bytes 08611d91
+ 004940c8 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c1e62438a9466d849e1dc7416d11b5"></a>

### [`004940ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md) → [`0049412c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049412c.md) FUN_0049412c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0049414c",
      "incomplete_value": false,
      "site": "00494150",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049410c",
      "incomplete_value": false,
      "site": "00494110",
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
            "const:7d8:8"
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
      "00494150",
      "DATA",
      [
        "storage",
        "00c657d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494150",
      "DATA",
      [
        "storage",
        "00c65bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md#insn-00494100) · [`0049410c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004940ec.md#insn-0049410c)
- 新版 [`00494140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049412c.md#insn-00494140) · [`0049414c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049412c.md#insn-0049414c)

~~~diff
- 00494100 ["INT_ADD", "register:40f0:8", ["const:494100:8", "const:4:8"]]
- 00494100 ["CALL", null, ["callee:00c57e90:8"]]
+ 00494140 ["INT_ADD", "register:40f0:8", ["const:494140:8", "const:4:8"]]
+ 00494140 ["CALL", null, ["callee:00c57e90:8"]]
- 00494100 bytes 640e1f94
+ 00494140 bytes 540f1f94
- 0049410c ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0049410c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049410c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049410c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049414c ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 0049414c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049414c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049414c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049410c bytes 08611f91
+ 0049414c bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78d9e6180b8d04dca648b79b50a01d49"></a>

### [`00494124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494124.md) → [`00494164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494164.md) FUN_00494164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494168",
      "incomplete_value": false,
      "site": "0049416c",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494128",
      "incomplete_value": false,
      "site": "0049412c",
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
            "const:7d8:8"
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
      "0049416c",
      "DATA",
      [
        "storage",
        "00c657d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049416c",
      "DATA",
      [
        "storage",
        "00c65bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494124.md#insn-00494128)
- 新版 [`00494168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494164.md#insn-00494168)

~~~diff
- 00494128 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00494128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494168 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00494168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494128 bytes 08611f91
+ 00494168 bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2233e8dcf7652fce3e7180f741b586ff"></a>

### [`0049418c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md) → [`004941cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004941cc.md) FUN_004941cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "004941ec",
      "incomplete_value": false,
      "site": "004941f0",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004941ac",
      "incomplete_value": false,
      "site": "004941b0",
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
            "const:858:8"
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
      "004941f0",
      "DATA",
      [
        "storage",
        "00c65858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004941f0",
      "DATA",
      [
        "storage",
        "00c65c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004941a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md#insn-004941a0) · [`004941ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049418c.md#insn-004941ac)
- 新版 [`004941e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004941cc.md#insn-004941e0) · [`004941ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004941cc.md#insn-004941ec)

~~~diff
- 004941a0 ["INT_ADD", "register:40f0:8", ["const:4941a0:8", "const:4:8"]]
- 004941a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004941e0 ["INT_ADD", "register:40f0:8", ["const:4941e0:8", "const:4:8"]]
+ 004941e0 ["CALL", null, ["callee:00c57e90:8"]]
- 004941a0 bytes 3c0e1f94
+ 004941e0 bytes 2c0f1f94
- 004941ac ["COPY", "tmp:0:8", ["const:858:8"]]
- 004941ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004941ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004941ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004941ec ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 004941ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004941ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004941ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004941ac bytes 08612191
+ 004941ec bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eec27453a656a5a0e57f6d0f32268f3"></a>

### [`004941c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004941c4.md) → [`00494204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494204.md) FUN_00494204

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494208",
      "incomplete_value": false,
      "site": "0049420c",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004941c8",
      "incomplete_value": false,
      "site": "004941cc",
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
            "const:858:8"
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
      "0049420c",
      "DATA",
      [
        "storage",
        "00c65858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049420c",
      "DATA",
      [
        "storage",
        "00c65c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004941c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004941c4.md#insn-004941c8)
- 新版 [`00494208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494204.md#insn-00494208)

~~~diff
- 004941c8 ["COPY", "tmp:0:8", ["const:858:8"]]
- 004941c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004941c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004941c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494208 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 00494208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004941c8 bytes 08612191
+ 00494208 bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c3a26b2360a6ca3737c498eae8453b"></a>

### [`0049422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md) → [`0049426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049426c.md) FUN_0049426c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0049428c",
      "incomplete_value": false,
      "site": "00494290",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049424c",
      "incomplete_value": false,
      "site": "00494250",
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
            "const:8d8:8"
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
      "00494290",
      "DATA",
      [
        "storage",
        "00c658d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494290",
      "DATA",
      [
        "storage",
        "00c65cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md#insn-00494240) · [`0049424c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049422c.md#insn-0049424c)
- 新版 [`00494280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049426c.md#insn-00494280) · [`0049428c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049426c.md#insn-0049428c)

~~~diff
- 00494240 ["INT_ADD", "register:40f0:8", ["const:494240:8", "const:4:8"]]
- 00494240 ["CALL", null, ["callee:00c57e90:8"]]
+ 00494280 ["INT_ADD", "register:40f0:8", ["const:494280:8", "const:4:8"]]
+ 00494280 ["CALL", null, ["callee:00c57e90:8"]]
- 00494240 bytes 140e1f94
+ 00494280 bytes 040f1f94
- 0049424c ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0049424c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049424c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049424c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049428c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0049428c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049428c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049428c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049424c bytes 08612391
+ 0049428c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2c73a5bcf02892f8d46bd16b2b4eb0f"></a>

### [`00494264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494264.md) → [`004942a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004942a4.md) FUN_004942a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004942a8",
      "incomplete_value": false,
      "site": "004942ac",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494268",
      "incomplete_value": false,
      "site": "0049426c",
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
            "const:8d8:8"
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
      "004942ac",
      "DATA",
      [
        "storage",
        "00c658d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004942ac",
      "DATA",
      [
        "storage",
        "00c65cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494264.md#insn-00494268)
- 新版 [`004942a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004942a4.md#insn-004942a8)

~~~diff
- 00494268 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00494268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004942a8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 004942a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004942a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004942a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494268 bytes 08612391
+ 004942a8 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8944fabcf7f5cf4959ff0eb950a1b1"></a>

### [`004943f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md) → [`00494434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494434.md) FUN_00494434

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00494454",
      "incomplete_value": false,
      "site": "00494458",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494414",
      "incomplete_value": false,
      "site": "00494418",
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
            "const:958:8"
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
      "00494458",
      "DATA",
      [
        "storage",
        "00c65958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494458",
      "DATA",
      [
        "storage",
        "00c65d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md#insn-00494408) · [`00494414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004943f4.md#insn-00494414)
- 新版 [`00494448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494434.md#insn-00494448) · [`00494454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494434.md#insn-00494454)

~~~diff
- 00494408 ["INT_ADD", "register:40f0:8", ["const:494408:8", "const:4:8"]]
- 00494408 ["CALL", null, ["callee:00c57e90:8"]]
+ 00494448 ["INT_ADD", "register:40f0:8", ["const:494448:8", "const:4:8"]]
+ 00494448 ["CALL", null, ["callee:00c57e90:8"]]
- 00494408 bytes a20d1f94
+ 00494448 bytes 920e1f94
- 00494414 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00494414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494454 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00494454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494414 bytes 08612591
+ 00494454 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74d01bf026cab962984435c97868a806"></a>

### [`0049442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049442c.md) → [`0049446c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049446c.md) FUN_0049446c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00494470",
      "incomplete_value": false,
      "site": "00494474",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494430",
      "incomplete_value": false,
      "site": "00494434",
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
            "const:958:8"
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
      "00494474",
      "DATA",
      [
        "storage",
        "00c65958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494474",
      "DATA",
      [
        "storage",
        "00c65d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049442c.md#insn-00494430)
- 新版 [`00494470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049446c.md#insn-00494470)

~~~diff
- 00494430 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00494430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494470 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00494470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494430 bytes 08612591
+ 00494470 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279ce4551effb572cfb10b47c0081b6f"></a>

### [`0049495c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049495c.md) → [`0049499c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049499c.md) FUN_0049499c

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
      "definition_site": "004949a8",
      "incomplete_value": false,
      "site": "004949b4",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494968",
      "incomplete_value": false,
      "site": "00494974",
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
      "004949b4",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004949b4",
      "DATA",
      [
        "storage",
        "00c65de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/0049495c.md#insn-00494968)
- 新版 [`004949a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/0049499c.md#insn-004949a8)

~~~diff
- 00494968 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00494968 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00494968 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00494968 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004949a8 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 004949a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004949a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004949a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00494968 bytes 4aa12791
+ 004949a8 bytes 4aa13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c60f0fff869c73c49fe060428cb9782"></a>

### [`004949a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md) → [`004949e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004949e0.md) FUN_004949e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004949f8",
      "incomplete_value": false,
      "site": "00494a04",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004949b8",
      "incomplete_value": false,
      "site": "004949c4",
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
      "00494a04",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494a04",
      "DATA",
      [
        "storage",
        "00c65de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004949b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md#insn-004949b8) · [`004949e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949a0.md#insn-004949e8)
- 新版 [`004949f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004949e0.md#insn-004949f8) · [`00494a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/004949e0.md#insn-00494a28)

~~~diff
- 004949b8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 004949b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004949b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004949b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004949f8 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 004949f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004949f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004949f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004949b8 bytes 08a12791
+ 004949f8 bytes 08a13791
- 004949e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004949e8 ["INT_ADD", "register:40f0:8", ["const:4949e8:8", "const:4:8"]]
- 004949e8 ["CALLIND", null, ["register:0:8"]]
+ 00494a28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494a28 ["INT_ADD", "register:40f0:8", ["const:494a28:8", "const:4:8"]]
+ 00494a28 ["CALLIND", null, ["register:0:8"]]
- 004949e8 bytes 00013fd6
+ 00494a28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8744cac97ed169fa1fba943f8ef5e3e6"></a>

### [`004949fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md) → [`00494a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494a3c.md) FUN_00494a3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00494a68",
      "incomplete_value": false,
      "site": "00494a68",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494a28",
      "incomplete_value": false,
      "site": "00494a28",
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
            "const:9e8:8"
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
      "00494a68",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494a68",
      "DATA",
      [
        "storage",
        "00c65de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a10) · [`00494a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a20) · [`00494a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004949fc.md#insn-00494a44)
- 新版 [`00494a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494a3c.md#insn-00494a50) · [`00494a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494a3c.md#insn-00494a60) · [`00494a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494a3c.md#insn-00494a84)

~~~diff
- 00494a10 ["INT_ADD", "register:40f0:8", ["const:494a10:8", "const:4:8"]]
- 00494a10 ["CALL", null, ["callee:00c57e90:8"]]
+ 00494a50 ["INT_ADD", "register:40f0:8", ["const:494a50:8", "const:4:8"]]
+ 00494a50 ["CALL", null, ["callee:00c57e90:8"]]
- 00494a10 bytes 200c1f94
+ 00494a50 bytes 100d1f94
- 00494a20 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00494a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494a60 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00494a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494a20 bytes 08a12791
+ 00494a60 bytes 08a13791
- 00494a44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494a44 ["INT_ADD", "register:40f0:8", ["const:494a44:8", "const:4:8"]]
- 00494a44 ["CALLIND", null, ["register:0:8"]]
+ 00494a84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494a84 ["INT_ADD", "register:40f0:8", ["const:494a84:8", "const:4:8"]]
+ 00494a84 ["CALLIND", null, ["register:0:8"]]
- 00494a44 bytes 00013fd6
+ 00494a84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4ac4f277ab1c6a22e82eaf4349c1dd"></a>

### [`00494a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md) → [`00494acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494acc.md) FUN_00494acc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00494aec",
      "incomplete_value": false,
      "site": "00494aec",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494aac",
      "incomplete_value": false,
      "site": "00494aac",
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
            "const:9e8:8"
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
      "00494aec",
      "DATA",
      [
        "storage",
        "00c659e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00494aec",
      "DATA",
      [
        "storage",
        "00c65de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494aec) · [`00494aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494aa8) · [`00494ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494a8c.md#insn-00494ac8)
- 新版 [`00494b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494acc.md#insn-00494b2c) · [`00494ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494acc.md#insn-00494ae8) · [`00494b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494acc.md#insn-00494b08)

~~~diff
- 00494aec ["COPY", "register:0:8", ["register:4040:8"]]
- 00494aec ["INT_ADD", "register:40f0:8", ["const:494aec:8", "const:4:8"]]
- 00494aec ["CALLIND", null, ["register:0:8"]]
+ 00494b2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494b2c ["INT_ADD", "register:40f0:8", ["const:494b2c:8", "const:4:8"]]
+ 00494b2c ["CALLIND", null, ["register:0:8"]]
- 00494aec bytes 00013fd6
+ 00494b2c bytes 00013fd6
- 00494aa8 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00494aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00494aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00494aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00494ae8 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00494ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00494ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00494ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00494aa8 bytes 08a12791
+ 00494ae8 bytes 08a13791
- 00494ac8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494ac8 ["INT_ADD", "register:40f0:8", ["const:494ac8:8", "const:4:8"]]
- 00494ac8 ["CALLIND", null, ["register:0:8"]]
+ 00494b08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494b08 ["INT_ADD", "register:40f0:8", ["const:494b08:8", "const:4:8"]]
+ 00494b08 ["CALLIND", null, ["register:0:8"]]
- 00494ac8 bytes 00013fd6
+ 00494b08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd5a3cc8489033864addc51d14a539fd"></a>

### [`00494b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md) → [`00494bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md) FUN_00494bcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004944d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004944d4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00494514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494514.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00494c10",
      "incomplete_value": false,
      "site": "00494c18",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494bd0",
      "incomplete_value": false,
      "site": "00494bd8",
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
            "const:db0:8"
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
      "00494c10",
      "PARAM",
      [
        "storage",
        "00ca4db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00494c10",
      "PARAM",
      [
        "storage",
        "00ca51b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bd8) · [`00494bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bc8) · [`00494bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494b8c.md#insn-00494bcc)
- 新版 [`00494c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md#insn-00494c18) · [`00494c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md#insn-00494c08) · [`00494c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494bcc.md#insn-00494c0c)

~~~diff
- 00494bd8 ["INT_ADD", "register:40f0:8", ["const:494bd8:8", "const:4:8"]]
- 00494bd8 ["CALL", null, ["callee:00494514:8"]]
+ 00494c18 ["INT_ADD", "register:40f0:8", ["const:494c18:8", "const:4:8"]]
+ 00494c18 ["CALL", null, ["callee:00494514:8"]]
- 00494bd8 bytes 3ffeff97
+ 00494c18 bytes 3ffeff97
- 00494bc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00494bc8 ["INT_ADD", "register:40f0:8", ["const:494bc8:8", "const:4:8"]]
- 00494bc8 ["CALLIND", null, ["register:0:8"]]
+ 00494c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00494c08 ["INT_ADD", "register:40f0:8", ["const:494c08:8", "const:4:8"]]
+ 00494c08 ["CALLIND", null, ["register:0:8"]]
- 00494bc8 bytes 00013fd6
+ 00494c08 bytes 00013fd6
- 00494bcc ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 00494c0c ["COPY", "register:4000:8", ["const:ca5000:8"]]
- 00494bcc bytes 80400090
+ 00494c0c bytes 804000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-934bdab53f361f3b50ed66b1c7b5d552"></a>

### [`00494dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md) → [`00494e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md) _INIT_22

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0048dc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc28.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`0048dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc68.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 15件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00494e48",
      "incomplete_value": true,
      "site": "00494e64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00494e08",
      "incomplete_value": true,
      "site": "00494e24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "00494e6c",
      "incomplete_value": true,
      "site": "00494e88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00494e2c",
      "incomplete_value": true,
      "site": "00494e48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "00494e8c",
      "incomplete_value": true,
      "site": "00494ea8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00494e4c",
      "incomplete_value": true,
      "site": "00494e68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "00494e48",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00494e6c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00494e8c",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00494e48",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00494e6c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00494e8c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-00494e44) · [`00494e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-00494e64) · [`00494f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494dc8.md#insn-00494f2c)
- 新版 [`00494e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md#insn-00494e84) · [`00494ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md#insn-00494ea4) · [`00494f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494e08.md#insn-00494f6c)

~~~diff
- 00494e44 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00494e44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00494e44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00494e44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00494e84 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00494e84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00494e84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00494e84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00494e44 bytes 4a093691
+ 00494e84 bytes 4a093791
- 00494e64 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00494e64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00494e64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00494e64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00494ea4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00494ea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00494ea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00494ea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00494e64 bytes 4a553a91
+ 00494ea4 bytes 4a893d91
- 00494f2c ["INT_ADD", "register:40f0:8", ["const:494f2c:8", "const:4:8"]]
- 00494f2c ["CALL", null, ["callee:0043b7f8:8"]]
+ 00494f6c ["INT_ADD", "register:40f0:8", ["const:494f6c:8", "const:4:8"]]
+ 00494f6c ["CALL", null, ["callee:0043b7f8:8"]]
- 00494f2c bytes 239afe97
+ 00494f6c bytes 239afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e9c4a03085c918fdebd7b34ca39cd7"></a>

### [`00495240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md) → [`00495280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md) FUN_00495280

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) [`00b2b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004952ac",
      "incomplete_value": true,
      "site": "004952b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049526c",
      "incomplete_value": true,
      "site": "00495278",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f20:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00495288",
      "incomplete_value": true,
      "site": "00495288",
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
      "definition_site": "00495248",
      "incomplete_value": true,
      "site": "00495248",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00495248"
      ],
      [
        "FALL_THROUGH",
        "00495288"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00495288",
      "incomplete_value": true,
      "site": "00495290",
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
      "definition_site": "00495248",
      "incomplete_value": true,
      "site": "00495250",
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
      "00495284",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "004952ac",
      "READ",
      [
        "storage",
        "002c2f20",
        null,
        null
      ]
    ],
    [
      "004952bc",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00495284",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "004952ac",
      "READ",
      [
        "storage",
        "002c2f60",
        null,
        null
      ]
    ],
    [
      "004952bc",
      "READ",
      [
        "storage",
        "00ca5208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495240) · [`00495244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495244) · [`00495264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495240.md#insn-00495264)
- 新版 [`00495280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md#insn-00495280) · [`00495284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md#insn-00495284) · [`004952a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md#insn-004952a4)

~~~diff
- 00495240 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 00495280 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00495240 bytes 684000f0
+ 00495280 bytes 88400090
- 00495244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00495244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495284 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:210:8"]]
+ 00495284 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00495244 bytes 080947f9
+ 00495284 bytes 080941f9
- 00495264 ["COPY", "register:40a8:8", ["const:ca4000:8"]]
+ 004952a4 ["COPY", "register:40a8:8", ["const:ca5000:8"]]
- 00495264 bytes 754000f0
+ 004952a4 bytes 95400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845e33969b997f11b1d0b652f26132a6"></a>

### [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) → [`004953d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md) FUN_004953d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`008532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/008532c8.md) [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 2件 [`00495d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495d04.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 5件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00853308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) [`008766f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/008766f4.md) · 呼出先 2件 [`00495d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495d44.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00495490",
      "incomplete_value": true,
      "site": "00495490",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495450",
      "incomplete_value": true,
      "site": "00495450",
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
            "const:e10:8"
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
      "definition_site": "004953f0",
      "incomplete_value": true,
      "site": "004953f0",
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
      "definition_site": "004953b0",
      "incomplete_value": true,
      "site": "004953b0",
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
      "definition_site": "00495448",
      "incomplete_value": false,
      "site": "0049544c",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495408",
      "incomplete_value": false,
      "site": "0049540c",
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
            "const:de8:8"
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
      "004953ec",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00495404",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00495410",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004953ec",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00495404",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00495410",
      "READ",
      [
        "storage",
        "00ca51f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004953cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-004953cc) · [`0049540c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-0049540c) · [`00495450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md#insn-00495450)
- 新版 [`0049540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md#insn-0049540c) · [`0049544c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md#insn-0049544c) · [`00495490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md#insn-00495490)

~~~diff
- 004953cc ["COPY", "tmp:0:8", ["const:df0:8"]]
- 004953cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004953cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004953cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049540c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 0049540c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049540c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049540c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004953cc bytes 4ac13791
+ 0049540c bytes 4ac10791
- 0049540c ["INT_ADD", "register:40f0:8", ["const:49540c:8", "const:4:8"]]
- 0049540c ["CALL", null, ["callee:00495d44:8"]]
+ 0049544c ["INT_ADD", "register:40f0:8", ["const:49544c:8", "const:4:8"]]
+ 0049544c ["CALL", null, ["callee:00495d44:8"]]
- 0049540c bytes 3e020094
+ 0049544c bytes 3e020094
- 00495450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e10:8"]]
- 00495450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00495490 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:210:8"]]
+ 00495490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00495450 bytes a80a07f9
+ 00495490 bytes a80a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-597ef27e5ecc489172f0b260f646aac4"></a>

### [`00495478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md) → [`004954b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004954b8.md) FUN_004954b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 2件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) [`0085b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004954e4",
      "incomplete_value": true,
      "site": "004954ec",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004954a4",
      "incomplete_value": true,
      "site": "004954ac",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004954c0",
      "incomplete_value": true,
      "site": "004954c0",
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
      "definition_site": "00495480",
      "incomplete_value": true,
      "site": "00495480",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00495480"
      ],
      [
        "FALL_THROUGH",
        "004954c0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "004954c0",
      "incomplete_value": true,
      "site": "004954ec",
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
      "definition_site": "00495480",
      "incomplete_value": true,
      "site": "004954ac",
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
      "004954bc",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "004954cc",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ],
    [
      "004954d0",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004954bc",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "004954cc",
      "READ",
      [
        "storage",
        "00ca5208",
        null,
        "undefined8"
      ]
    ],
    [
      "004954d0",
      "READ",
      [
        "storage",
        "00ca51f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-00495478) · [`0049547c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-0049547c) · [`00495484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495478.md#insn-00495484)
- 新版 [`004954b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004954b8.md#insn-004954b8) · [`004954bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004954b8.md#insn-004954bc) · [`004954c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004954b8.md#insn-004954c4)

~~~diff
- 00495478 ["COPY", "register:4048:8", ["const:ca4000:8"]]
+ 004954b8 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 00495478 bytes 694000f0
+ 004954b8 bytes 89400090
- 0049547c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 0049547c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004954bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:210:8"]]
+ 004954bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049547c bytes 290947f9
+ 004954bc bytes 290941f9
- 00495484 ["COPY", "register:4048:8", ["const:ca4000:8"]]
+ 004954c4 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 00495484 bytes 694000f0
+ 004954c4 bytes 89400090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51f30cfad1834577f16faec42a4d2b57"></a>

### [`004954d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md) → [`00495518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md) FUN_00495518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 19件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468980.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 19件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`004689c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004689c0.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00495588",
      "incomplete_value": true,
      "site": "00495590",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495548",
      "incomplete_value": true,
      "site": "00495550",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00495a6c",
      "incomplete_value": false,
      "site": "00495a6c",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495a2c",
      "incomplete_value": false,
      "site": "00495a2c",
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
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00495554",
      "incomplete_value": true,
      "site": "00495554",
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
      "definition_site": "00495514",
      "incomplete_value": true,
      "site": "00495514",
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
      "00495550",
      "READ",
      [
        "storage",
        "00ca4e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00495564",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00495568",
      "READ",
      [
        "storage",
        "00ca4df0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00495550",
      "READ",
      [
        "storage",
        "00ca5210",
        null,
        "undefined8"
      ]
    ],
    [
      "00495564",
      "READ",
      [
        "storage",
        "00ca5208",
        null,
        "undefined8"
      ]
    ],
    [
      "00495568",
      "READ",
      [
        "storage",
        "00ca51f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md#insn-00495510) · [`004956c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md#insn-004956c0) · [`004956d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/004954d8.md#insn-004956d0)
- 新版 [`00495550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md#insn-00495550) · [`00495700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md#insn-00495700) · [`00495710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495518.md#insn-00495710)

~~~diff
- 00495510 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00495510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495550 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:210:8"]]
+ 00495550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00495510 bytes 080947f9
+ 00495550 bytes 080941f9
- 004956c0 ["INT_ADD", "register:40f0:8", ["const:4956c0:8", "const:4:8"]]
- 004956c0 ["CALL", null, ["callee:00c58610:8"]]
+ 00495700 ["INT_ADD", "register:40f0:8", ["const:495700:8", "const:4:8"]]
+ 00495700 ["CALL", null, ["callee:00c58610:8"]]
- 004956c0 bytes d40a1f94
+ 00495700 bytes c40b1f94
- 004956d0 ["INT_ADD", "register:40f0:8", ["const:4956d0:8", "const:4:8"]]
- 004956d0 ["CALL", null, ["callee:0046cb0c:8"]]
+ 00495710 ["INT_ADD", "register:40f0:8", ["const:495710:8", "const:4:8"]]
+ 00495710 ["CALL", null, ["callee:0046cb0c:8"]]
- 004956d0 bytes ff5cff97
+ 00495710 bytes ff5cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386f21c28a6891a7763d2958fda6a3cb"></a>

### [`00496664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md) → [`004966a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/004966a4.md) _INIT_23

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0049523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/0049523c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`0049527c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/0049527c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 6件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004966e0",
      "incomplete_value": true,
      "site": "004966fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004966a0",
      "incomplete_value": true,
      "site": "004966bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "00496704",
      "incomplete_value": true,
      "site": "00496720",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004966c4",
      "incomplete_value": true,
      "site": "004966e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "00496724",
      "incomplete_value": true,
      "site": "00496740",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004966e4",
      "incomplete_value": true,
      "site": "00496700",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "004966e0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00496704",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00496724",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004966e0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00496704",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00496724",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004966dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-004966dc) · [`004966fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-004966fc) · [`004967c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496664.md#insn-004967c4)
- 新版 [`0049671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/004966a4.md#insn-0049671c) · [`0049673c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/004966a4.md#insn-0049673c) · [`00496804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/004966a4.md#insn-00496804)

~~~diff
- 004966dc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 004966dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004966dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004966dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049671c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0049671c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049671c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049671c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004966dc bytes 4a093691
+ 0049671c bytes 4a093791
- 004966fc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 004966fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004966fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004966fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049673c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0049673c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049673c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049673c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004966fc bytes 4a553a91
+ 0049673c bytes 4a893d91
- 004967c4 ["INT_ADD", "register:40f0:8", ["const:4967c4:8", "const:4:8"]]
- 004967c4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00496804 ["INT_ADD", "register:40f0:8", ["const:496804:8", "const:4:8"]]
+ 00496804 ["CALL", null, ["callee:0043b7f8:8"]]
- 004967c4 bytes fd93fe97
+ 00496804 bytes fd93fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d8907c28c73f4e283794b0e40b4964"></a>

### [`00496a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md) → [`00496a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md) FUN_00496a5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`00768564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768564.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00550bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550bec.md) [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md)
- 新版 呼出元 6件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`007685a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007685a4.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768a28.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00550c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c2c.md) [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00496b6c",
      "incomplete_value": false,
      "site": "00496b74",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496b2c",
      "incomplete_value": false,
      "site": "00496b34",
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
            "const:a90:8"
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
      "definition_site": "00496b8c",
      "incomplete_value": false,
      "site": "00496b8c",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496b4c",
      "incomplete_value": false,
      "site": "00496b4c",
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
            "const:ae0:8"
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
      "definition_site": "00496c10",
      "incomplete_value": false,
      "site": "00496c18",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496bd0",
      "incomplete_value": false,
      "site": "00496bd8",
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
            "const:690:8"
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
      "00496b74",
      "DATA",
      [
        "storage",
        "00c65a90",
        null,
        "undefined *"
      ]
    ],
    [
      "00496b8c",
      "DATA",
      [
        "storage",
        "00c65ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "00496c18",
      "DATA",
      [
        "storage",
        "00c63690",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00496b74",
      "DATA",
      [
        "storage",
        "00c65e90",
        null,
        "undefined *"
      ]
    ],
    [
      "00496b8c",
      "DATA",
      [
        "storage",
        "00c65ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "00496c18",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496c18) · [`00496a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496a50) · [`00496ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496a1c.md#insn-00496ab8)
- 新版 [`00496c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md#insn-00496c58) · [`00496a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md#insn-00496a90) · [`00496af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496a5c.md#insn-00496af8)

~~~diff
- 00496c18 ["INT_ADD", "register:40f0:8", ["const:496c18:8", "const:4:8"]]
- 00496c18 ["CALL", null, ["callee:00c53d00:8"]]
+ 00496c58 ["INT_ADD", "register:40f0:8", ["const:496c58:8", "const:4:8"]]
+ 00496c58 ["CALL", null, ["callee:00c53d00:8"]]
- 00496c18 bytes 32f31e94
+ 00496c58 bytes 2af41e94
- 00496a50 ["INT_ADD", "register:40f0:8", ["const:496a50:8", "const:4:8"]]
- 00496a50 ["CALL", null, ["callee:00550c2c:8"]]
+ 00496a90 ["INT_ADD", "register:40f0:8", ["const:496a90:8", "const:4:8"]]
+ 00496a90 ["CALL", null, ["callee:00550c2c:8"]]
- 00496a50 bytes 67e80294
+ 00496a90 bytes 67e80294
- 00496ab8 ["INT_ADD", "register:40f0:8", ["const:496ab8:8", "const:4:8"]]
- 00496ab8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00496af8 ["INT_ADD", "register:40f0:8", ["const:496af8:8", "const:4:8"]]
+ 00496af8 ["CALL", null, ["callee:00c57e90:8"]]
- 00496ab8 bytes f6031f94
+ 00496af8 bytes e6041f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fe2bc861e0729b193cb511f01f46c12"></a>

### [`00496d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496d78.md) → [`00496db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496db8.md) FUN_00496db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00496dbc",
      "incomplete_value": false,
      "site": "00496dc0",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496d7c",
      "incomplete_value": false,
      "site": "00496d80",
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
            "const:a90:8"
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
      "00496dc0",
      "DATA",
      [
        "storage",
        "00c65a90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00496dc0",
      "DATA",
      [
        "storage",
        "00c65e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496d78.md#insn-00496d7c)
- 新版 [`00496dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496db8.md#insn-00496dbc)

~~~diff
- 00496d7c ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00496d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00496dbc ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00496dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496d7c bytes 08412a91
+ 00496dbc bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f20a85b0cec65f67f96301c3f572cea6"></a>

### [`00496d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496d88.md) → [`00496dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496dc8.md) FUN_00496dc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00496dd8",
      "incomplete_value": false,
      "site": "00496de0",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496d98",
      "incomplete_value": false,
      "site": "00496da0",
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
            "const:a90:8"
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
      "00496de0",
      "DATA",
      [
        "storage",
        "00c65a90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00496de0",
      "DATA",
      [
        "storage",
        "00c65e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496d88.md#insn-00496d98) · [`00496da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496d88.md#insn-00496da4)
- 新版 [`00496dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496dc8.md#insn-00496dd8) · [`00496de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496dc8.md#insn-00496de4)

~~~diff
- 00496d98 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00496d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00496dd8 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00496dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00496dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496d98 bytes 08412a91
+ 00496dd8 bytes 08413a91
- 00496da4 ["INT_ADD", "register:40f0:8", ["const:496da4:8", "const:4:8"]]
- 00496da4 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00496de4 ["INT_ADD", "register:40f0:8", ["const:496de4:8", "const:4:8"]]
+ 00496de4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00496da4 bytes 3f031f94
+ 00496de4 bytes 2f041f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c843a800d920e7434ed6b1d8c1eb7647"></a>

### [`00496db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md) → [`00496df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496df8.md) FUN_00496df8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00496e10",
      "incomplete_value": false,
      "site": "00496e14",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00496dd0",
      "incomplete_value": false,
      "site": "00496dd4",
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
            "const:ae0:8"
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
      "00496e14",
      "DATA",
      [
        "storage",
        "00c65ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00496e14",
      "DATA",
      [
        "storage",
        "00c65ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00496e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496e14) · [`00496dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496dd0) · [`00496de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496db8.md#insn-00496de4)
- 新版 [`00496e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496df8.md#insn-00496e54) · [`00496e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496df8.md#insn-00496e10) · [`00496e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00496/00496df8.md#insn-00496e24)

~~~diff
- 00496e14 ["INT_ADD", "register:40f0:8", ["const:496e14:8", "const:4:8"]]
- 00496e14 ["CALL", null, ["callee:00c57e80:8"]]
+ 00496e54 ["INT_ADD", "register:40f0:8", ["const:496e54:8", "const:4:8"]]
+ 00496e54 ["CALL", null, ["callee:00c57e80:8"]]
- 00496e14 bytes 1b031f94
+ 00496e54 bytes 0b041f94
- 00496dd0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00496dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00496dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00496dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00496e10 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00496e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00496e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00496e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00496dd0 bytes 08812b91
+ 00496e10 bytes 08813b91
- 00496de4 ["INT_ADD", "register:40f0:8", ["const:496de4:8", "const:4:8"]]
- 00496de4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00496e24 ["INT_ADD", "register:40f0:8", ["const:496e24:8", "const:4:8"]]
+ 00496e24 ["CALL", null, ["callee:00c53d00:8"]]
- 00496de4 bytes bff21e94
+ 00496e24 bytes b7f31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ecdcdd588ff231ca30668a7e7e6903"></a>

### [`00496ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md) → [`00497038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497038.md) FUN_00497038

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497080",
      "incomplete_value": true,
      "site": "00497088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00497040",
      "incomplete_value": true,
      "site": "00497048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00497074",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00497088",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "004970b0",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497074",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "00497088",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "004970b0",
      "READ",
      [
        "storage",
        "00c6d610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-00497028) · [`00497034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-00497034) · [`0049705c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00496/00496ff8.md#insn-0049705c)
- 新版 [`00497068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497038.md#insn-00497068) · [`00497074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497038.md#insn-00497074) · [`0049709c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497038.md#insn-0049709c)

~~~diff
- 00497028 ["INT_ADD", "register:40f0:8", ["const:497028:8", "const:4:8"]]
- 00497028 ["CALL", null, ["callee:00c57e90:8"]]
+ 00497068 ["INT_ADD", "register:40f0:8", ["const:497068:8", "const:4:8"]]
+ 00497068 ["CALL", null, ["callee:00c57e90:8"]]
- 00497028 bytes 9a021f94
+ 00497068 bytes 8a031f94
- 00497034 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
- 00497034 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497074 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
+ 00497074 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00497034 bytes 291144f9
+ 00497074 bytes 291146f9
- 0049705c ["INT_ADD", "register:40f0:8", ["const:49705c:8", "const:4:8"]]
- 0049705c ["CALL", null, ["callee:0045982c:8"]]
+ 0049709c ["INT_ADD", "register:40f0:8", ["const:49709c:8", "const:4:8"]]
+ 0049709c ["CALL", null, ["callee:0045982c:8"]]
- 0049705c bytes e409ff97
+ 0049709c bytes e409ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec351d084a70bfd4aaaf37bef209398e"></a>

### [`004970d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md) → [`00497114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497114.md) FUN_00497114

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00497164",
      "incomplete_value": true,
      "site": "0049716c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00497124",
      "incomplete_value": true,
      "site": "0049712c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00497158",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "0049716c",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497194",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497158",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "0049716c",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "00497194",
      "READ",
      [
        "storage",
        "00c6d610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-00497108) · [`00497118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-00497118) · [`00497140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004970d4.md#insn-00497140)
- 新版 [`00497148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497114.md#insn-00497148) · [`00497158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497114.md#insn-00497158) · [`00497180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497114.md#insn-00497180)

~~~diff
- 00497108 ["INT_ADD", "register:40f0:8", ["const:497108:8", "const:4:8"]]
- 00497108 ["CALL", null, ["callee:00c57e90:8"]]
+ 00497148 ["INT_ADD", "register:40f0:8", ["const:497148:8", "const:4:8"]]
+ 00497148 ["CALL", null, ["callee:00c57e90:8"]]
- 00497108 bytes 62021f94
+ 00497148 bytes 52031f94
- 00497118 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
- 00497118 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497158 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
+ 00497158 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00497118 bytes 291144f9
+ 00497158 bytes 291146f9
- 00497140 ["INT_ADD", "register:40f0:8", ["const:497140:8", "const:4:8"]]
- 00497140 ["CALL", null, ["callee:0045982c:8"]]
+ 00497180 ["INT_ADD", "register:40f0:8", ["const:497180:8", "const:4:8"]]
+ 00497180 ["CALL", null, ["callee:0045982c:8"]]
- 00497140 bytes ab09ff97
+ 00497180 bytes ab09ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e302bfa5a980a9b58d7feb55b6036de"></a>

### [`004971bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md) → [`004971fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004971fc.md) FUN_004971fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497248",
      "incomplete_value": true,
      "site": "00497250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00497208",
      "incomplete_value": true,
      "site": "00497210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0049723c",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00497250",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497278",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049723c",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "00497250",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "00497278",
      "READ",
      [
        "storage",
        "00c6d610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004971ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-004971ec) · [`004971fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-004971fc) · [`00497224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004971bc.md#insn-00497224)
- 新版 [`0049722c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004971fc.md#insn-0049722c) · [`0049723c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004971fc.md#insn-0049723c) · [`00497264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004971fc.md#insn-00497264)

~~~diff
- 004971ec ["INT_ADD", "register:40f0:8", ["const:4971ec:8", "const:4:8"]]
- 004971ec ["CALL", null, ["callee:00c57e90:8"]]
+ 0049722c ["INT_ADD", "register:40f0:8", ["const:49722c:8", "const:4:8"]]
+ 0049722c ["CALL", null, ["callee:00c57e90:8"]]
- 004971ec bytes 29021f94
+ 0049722c bytes 19031f94
- 004971fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
- 004971fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049723c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
+ 0049723c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004971fc bytes 291144f9
+ 0049723c bytes 291146f9
- 00497224 ["INT_ADD", "register:40f0:8", ["const:497224:8", "const:4:8"]]
- 00497224 ["CALL", null, ["callee:0045982c:8"]]
+ 00497264 ["INT_ADD", "register:40f0:8", ["const:497264:8", "const:4:8"]]
+ 00497264 ["CALL", null, ["callee:0045982c:8"]]
- 00497224 bytes 7209ff97
+ 00497264 bytes 7209ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e739ea60b0b4a89952ecc8de5c3a9e80"></a>

### [`0049729c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md) → [`004972dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004972dc.md) FUN_004972dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497324",
      "incomplete_value": true,
      "site": "0049732c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004972e4",
      "incomplete_value": true,
      "site": "004972ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00497318",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "0049732c",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ],
    [
      "00497354",
      "READ",
      [
        "storage",
        "00c6d210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497318",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "0049732c",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ],
    [
      "00497354",
      "READ",
      [
        "storage",
        "00c6d610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004972cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-004972cc) · [`004972d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-004972d8) · [`00497300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/0049729c.md#insn-00497300)
- 新版 [`0049730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004972dc.md#insn-0049730c) · [`00497318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004972dc.md#insn-00497318) · [`00497340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004972dc.md#insn-00497340)

~~~diff
- 004972cc ["INT_ADD", "register:40f0:8", ["const:4972cc:8", "const:4:8"]]
- 004972cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0049730c ["INT_ADD", "register:40f0:8", ["const:49730c:8", "const:4:8"]]
+ 0049730c ["CALL", null, ["callee:00c57e90:8"]]
- 004972cc bytes f1011f94
+ 0049730c bytes e1021f94
- 004972d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:820:8"]]
- 004972d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497318 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c20:8"]]
+ 00497318 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004972d8 bytes 291144f9
+ 00497318 bytes 291146f9
- 00497300 ["INT_ADD", "register:40f0:8", ["const:497300:8", "const:4:8"]]
- 00497300 ["CALL", null, ["callee:0045982c:8"]]
+ 00497340 ["INT_ADD", "register:40f0:8", ["const:497340:8", "const:4:8"]]
+ 00497340 ["CALL", null, ["callee:0045982c:8"]]
- 00497300 bytes 3b09ff97
+ 00497340 bytes 3b09ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a7b8dad635e40a2adfbfdb8e68653fa"></a>

### [`00497380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md) → [`004973c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md) FUN_004973c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`00550cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550cf8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00550d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550d38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497438",
      "incomplete_value": true,
      "site": "00497440",
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
      "definition_site": "004973f8",
      "incomplete_value": true,
      "site": "00497400",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00497448",
      "incomplete_value": true,
      "site": "00497448",
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
                "const:20:8"
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
      "definition_site": "00497408",
      "incomplete_value": true,
      "site": "00497408",
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
                "const:20:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497448",
      "incomplete_value": true,
      "site": "00497448",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00497408",
      "incomplete_value": true,
      "site": "00497408",
      "value": [
        "LOAD",
        "8",
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
      "00497434",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00497438",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0049743c",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00497434",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00497438",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0049743c",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004973c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973c8) · [`004973b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973b0) · [`004973bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497380.md#insn-004973bc)
- 新版 [`00497408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md#insn-00497408) · [`004973f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md#insn-004973f0) · [`004973fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md#insn-004973fc)

~~~diff
- 004973c8 ["INT_ADD", "register:40f0:8", ["const:4973c8:8", "const:4:8"]]
- 004973c8 ["CALL", null, ["callee:00c581b0:8"]]
+ 00497408 ["INT_ADD", "register:40f0:8", ["const:497408:8", "const:4:8"]]
+ 00497408 ["CALL", null, ["callee:00c581b0:8"]]
- 004973c8 bytes 7a021f94
+ 00497408 bytes 6a031f94
- 004973b0 ["INT_ADD", "register:40f0:8", ["const:4973b0:8", "const:4:8"]]
- 004973b0 ["CALL", null, ["callee:004518b0:8"]]
+ 004973f0 ["INT_ADD", "register:40f0:8", ["const:4973f0:8", "const:4:8"]]
+ 004973f0 ["CALL", null, ["callee:004518b0:8"]]
- 004973b0 bytes 30e9fe97
+ 004973f0 bytes 30e9fe97
- 004973bc ["INT_ADD", "register:40f0:8", ["const:4973bc:8", "const:4:8"]]
- 004973bc ["CALL", null, ["callee:004519d8:8"]]
+ 004973fc ["INT_ADD", "register:40f0:8", ["const:4973fc:8", "const:4:8"]]
+ 004973fc ["CALL", null, ["callee:004519d8:8"]]
- 004973bc bytes 77e9fe97
+ 004973fc bytes 77e9fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18aa7fb0cde69b33450784d0cbc2e259"></a>

### [`00497664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md) → [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) FUN_004976a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce40.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0048ce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce80.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004976e0",
      "incomplete_value": true,
      "site": "004976f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004976a0",
      "incomplete_value": true,
      "site": "004976b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:967:8"
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
      "definition_site": "004976fc",
      "incomplete_value": true,
      "site": "00497710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "004976bc",
      "incomplete_value": true,
      "site": "004976d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee5:8"
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
      "004976e0",
      "READ",
      [
        "storage",
        "002b0967",
        null,
        "string"
      ]
    ],
    [
      "004976fc",
      "READ",
      [
        "storage",
        "002a0ee5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004976e0",
      "READ",
      [
        "storage",
        "002b09a7",
        null,
        "string"
      ]
    ],
    [
      "004976fc",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-00497690) · [`004976f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-004976f8) · [`00497710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497664.md#insn-00497710)
- 新版 [`004976d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md#insn-004976d0) · [`00497738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md#insn-00497738) · [`00497750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md#insn-00497750)

~~~diff
- 00497690 ["INT_ADD", "register:40f0:8", ["const:497690:8", "const:4:8"]]
- 00497690 ["CALL", null, ["callee:0058915c:8"]]
+ 004976d0 ["INT_ADD", "register:40f0:8", ["const:4976d0:8", "const:4:8"]]
+ 004976d0 ["CALL", null, ["callee:0058915c:8"]]
- 00497690 bytes a3c60394
+ 004976d0 bytes a3c60394
- 004976f8 ["INT_ADD", "register:40f0:8", ["const:4976f8:8", "const:4:8"]]
- 004976f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00497738 ["INT_ADD", "register:40f0:8", ["const:497738:8", "const:4:8"]]
+ 00497738 ["CALL", null, ["callee:00c57eb0:8"]]
- 004976f8 bytes ee001f94
+ 00497738 bytes de011f94
- 00497710 ["INT_ADD", "register:40f0:8", ["const:497710:8", "const:4:8"]]
- 00497710 ["CALL", null, ["callee:00589144:8"]]
+ 00497750 ["INT_ADD", "register:40f0:8", ["const:497750:8", "const:4:8"]]
+ 00497750 ["CALL", null, ["callee:00589144:8"]]
- 00497710 bytes 7dc60394
+ 00497750 bytes 7dc60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a611a28324e705cd85e325bf5945fac2"></a>

### [`00497890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md) → [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) FUN_004978d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

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
      "definition_site": "00497910",
      "incomplete_value": true,
      "site": "00497928",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:31f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004978d0",
      "incomplete_value": true,
      "site": "004978e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:252:8"
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
      "00497910",
      "READ",
      [
        "storage",
        "002ab252",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00497910",
      "READ",
      [
        "storage",
        "002ab31f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004978b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978b0) · [`004978b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978b8) · [`004978c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497890.md#insn-004978c4)
- 新版 [`004978f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md#insn-004978f0) · [`004978f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md#insn-004978f8) · [`00497904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md#insn-00497904)

~~~diff
- 004978b0 ["INT_ADD", "register:40f0:8", ["const:4978b0:8", "const:4:8"]]
- 004978b0 ["CALL", null, ["callee:00588e6c:8"]]
+ 004978f0 ["INT_ADD", "register:40f0:8", ["const:4978f0:8", "const:4:8"]]
+ 004978f0 ["CALL", null, ["callee:00588e6c:8"]]
- 004978b0 bytes 5fc50394
+ 004978f0 bytes 5fc50394
- 004978b8 ["INT_ADD", "register:40f0:8", ["const:4978b8:8", "const:4:8"]]
- 004978b8 ["CALL", null, ["callee:0058915c:8"]]
+ 004978f8 ["INT_ADD", "register:40f0:8", ["const:4978f8:8", "const:4:8"]]
+ 004978f8 ["CALL", null, ["callee:0058915c:8"]]
- 004978b8 bytes 19c60394
+ 004978f8 bytes 19c60394
- 004978c4 ["COPY", "tmp:0:8", ["const:252:8"]]
- 004978c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004978c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004978c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00497904 ["COPY", "tmp:0:8", ["const:31f:8"]]
+ 00497904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00497904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00497904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004978c4 bytes 29490991
+ 00497904 bytes 297d0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c571fafb4255f049de76c6ef16bf95"></a>

### [`00497aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md) → [`00497ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497ae4.md) FUN_00497ae4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`006354f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006354f0.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00497b24",
      "incomplete_value": false,
      "site": "00497b28",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497ae4",
      "incomplete_value": false,
      "site": "00497ae8",
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
            "const:b78:8"
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
      "definition_site": "00497b6c",
      "incomplete_value": false,
      "site": "00497b70",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497b2c",
      "incomplete_value": false,
      "site": "00497b30",
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
            "const:bc8:8"
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
      "00497b28",
      "DATA",
      [
        "storage",
        "00c65b78",
        null,
        "undefined *"
      ]
    ],
    [
      "00497b70",
      "DATA",
      [
        "storage",
        "00c65bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00497b28",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined *"
      ]
    ],
    [
      "00497b70",
      "DATA",
      [
        "storage",
        "00c65fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497ad8) · [`00497ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497ae4) · [`00497b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497aa4.md#insn-00497b20)
- 新版 [`00497b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497ae4.md#insn-00497b18) · [`00497b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497ae4.md#insn-00497b24) · [`00497b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497ae4.md#insn-00497b60)

~~~diff
- 00497ad8 ["INT_ADD", "register:40f0:8", ["const:497ad8:8", "const:4:8"]]
- 00497ad8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00497b18 ["INT_ADD", "register:40f0:8", ["const:497b18:8", "const:4:8"]]
+ 00497b18 ["CALL", null, ["callee:00c57e90:8"]]
- 00497ad8 bytes eeff1e94
+ 00497b18 bytes de001f94
- 00497ae4 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00497ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00497ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00497ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00497b24 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00497b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00497b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00497b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00497ae4 bytes 08e12d91
+ 00497b24 bytes 08e13d91
- 00497b20 ["INT_ADD", "register:40f0:8", ["const:497b20:8", "const:4:8"]]
- 00497b20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00497b60 ["INT_ADD", "register:40f0:8", ["const:497b60:8", "const:4:8"]]
+ 00497b60 ["CALL", null, ["callee:00c57e90:8"]]
- 00497b20 bytes dcff1e94
+ 00497b60 bytes cc001f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57017d3aadfa9cbc189d52d46e5593b2"></a>

### [`00497c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md) → [`00497c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md) FUN_00497c7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 7件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md)
- 新版 呼出元 2件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`006354f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006354f0.md) · 呼出先 7件 [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497cc4",
      "incomplete_value": true,
      "site": "00497cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497c84",
      "incomplete_value": true,
      "site": "00497c88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
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
      "definition_site": "00497cb0",
      "incomplete_value": false,
      "site": "00497cb4",
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
            "const:689:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497c70",
      "incomplete_value": false,
      "site": "00497c74",
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
            "const:649:8"
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
      "00497cb0",
      "PARAM",
      [
        "storage",
        "002ad649",
        null,
        "string"
      ]
    ],
    [
      "00497cc4",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00497cb0",
      "PARAM",
      [
        "storage",
        "002ad689",
        null,
        "string"
      ]
    ],
    [
      "00497cc4",
      "READ",
      [
        "storage",
        "002c3f40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c74) · [`00497c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c70) · [`00497c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497c3c.md#insn-00497c84)
- 新版 [`00497cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md#insn-00497cb4) · [`00497cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md#insn-00497cb0) · [`00497cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497c7c.md#insn-00497cc4)

~~~diff
- 00497c74 ["INT_ADD", "register:40f0:8", ["const:497c74:8", "const:4:8"]]
- 00497c74 ["CALL", null, ["callee:00c58470:8"]]
+ 00497cb4 ["INT_ADD", "register:40f0:8", ["const:497cb4:8", "const:4:8"]]
+ 00497cb4 ["CALL", null, ["callee:00c58470:8"]]
- 00497c74 bytes ff001f94
+ 00497cb4 bytes ef011f94
- 00497c70 ["COPY", "tmp:0:8", ["const:649:8"]]
- 00497c70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00497c70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00497c70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00497cb0 ["COPY", "tmp:0:8", ["const:689:8"]]
+ 00497cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00497cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00497cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00497c70 bytes 00241991
+ 00497cb0 bytes 00241a91
- 00497c84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 00497c84 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00497c84 ["COPY", "register:5008:8", ["const:0:8"]]
- 00497c84 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00497cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00497cc4 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00497cc4 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00497cc4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00497c84 bytes 008147fd
+ 00497cc4 bytes 00a147fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ff7db639acd4bffef56d77a1024d67"></a>

### [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) → [`00497df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md) FUN_00497df4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006354b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006354b0.md) · 呼出先 11件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)
- 新版 呼出元 1件 [`006354f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/006354f0.md) · 呼出先 11件 [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497e44",
      "incomplete_value": true,
      "site": "00497e48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497e04",
      "incomplete_value": true,
      "site": "00497e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
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
      "definition_site": "00497e30",
      "incomplete_value": false,
      "site": "00497e34",
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
            "const:689:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00497df0",
      "incomplete_value": false,
      "site": "00497df4",
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
            "const:649:8"
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
      "definition_site": "00497f54",
      "incomplete_value": false,
      "site": "00497f64",
      "value": [
        "leaf",
        "const:498cfc:8"
      ]
    },
    "old": {
      "definition_site": "00497f14",
      "incomplete_value": false,
      "site": "00497f24",
      "value": [
        "leaf",
        "const:498cbc:8"
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00497e30",
      "PARAM",
      [
        "storage",
        "002ad649",
        null,
        "string"
      ]
    ],
    [
      "00497e44",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00497f54",
      "PARAM",
      [
        "storage",
        "00498cbc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00497e30",
      "PARAM",
      [
        "storage",
        "002ad689",
        null,
        "string"
      ]
    ],
    [
      "00497e44",
      "READ",
      [
        "storage",
        "002c3f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00497f54",
      "PARAM",
      [
        "storage",
        "00498cfc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00497df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497df4) · [`00497f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497f24) · [`00497fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md#insn-00497fb8)
- 新版 [`00497e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md#insn-00497e34) · [`00497f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md#insn-00497f64) · [`00497ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md#insn-00497ff8)

~~~diff
- 00497df4 ["INT_ADD", "register:40f0:8", ["const:497df4:8", "const:4:8"]]
- 00497df4 ["CALL", null, ["callee:00c58470:8"]]
+ 00497e34 ["INT_ADD", "register:40f0:8", ["const:497e34:8", "const:4:8"]]
+ 00497e34 ["CALL", null, ["callee:00c58470:8"]]
- 00497df4 bytes 9f001f94
+ 00497e34 bytes 8f011f94
- 00497f24 ["INT_ADD", "register:40f0:8", ["const:497f24:8", "const:4:8"]]
- 00497f24 ["CALL", null, ["callee:00c58110:8"]]
+ 00497f64 ["INT_ADD", "register:40f0:8", ["const:497f64:8", "const:4:8"]]
+ 00497f64 ["CALL", null, ["callee:00c58110:8"]]
- 00497f24 bytes 7bff1e94
+ 00497f64 bytes 6b001f94
- 00497fb8 ["INT_ADD", "register:40f0:8", ["const:497fb8:8", "const:4:8"]]
- 00497fb8 ["CALL", null, ["callee:00c58120:8"]]
+ 00497ff8 ["INT_ADD", "register:40f0:8", ["const:497ff8:8", "const:4:8"]]
+ 00497ff8 ["CALL", null, ["callee:00c58120:8"]]
- 00497fb8 bytes 5aff1e94
+ 00497ff8 bytes 4a001f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c3f0c5f73e9529cc84ad6aeb71a9450"></a>

### [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) → [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) FUN_00498348

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`00853660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853660.md) · 呼出先 4件 [`00498094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498094.md) [`004985a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004985a0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md)
- 新版 呼出元 4件 [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`008536a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) · 呼出先 4件 [`004980d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004980d4.md) [`004985e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004985e0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004983cc",
      "incomplete_value": true,
      "site": "004983d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049838c",
      "incomplete_value": true,
      "site": "00498398",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:30:8"
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
      "004983cc",
      "READ",
      [
        "storage",
        "002c4030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004983cc",
      "READ",
      [
        "storage",
        "002c4070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-00498330) · [`00498370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-00498370) · [`0049838c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md#insn-0049838c)
- 新版 [`00498370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md#insn-00498370) · [`004983b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md#insn-004983b0) · [`004983cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md#insn-004983cc)

~~~diff
- 00498330 ["INT_ADD", "register:40f0:8", ["const:498330:8", "const:4:8"]]
- 00498330 ["CALL", null, ["callee:00c58620:8"]]
+ 00498370 ["INT_ADD", "register:40f0:8", ["const:498370:8", "const:4:8"]]
+ 00498370 ["CALL", null, ["callee:00c58620:8"]]
- 00498330 bytes bcff1e94
+ 00498370 bytes ac001f94
- 00498370 ["COPY", "register:0:8", ["register:4040:8"]]
- 00498370 ["INT_ADD", "register:40f0:8", ["const:498370:8", "const:4:8"]]
- 00498370 ["CALLIND", null, ["register:0:8"]]
+ 004983b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004983b0 ["INT_ADD", "register:40f0:8", ["const:4983b0:8", "const:4:8"]]
+ 004983b0 ["CALLIND", null, ["register:0:8"]]
- 00498370 bytes 00013fd6
+ 004983b0 bytes 00013fd6
- 0049838c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:30:8"]]
- 0049838c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0049838c ["COPY", "register:5008:8", ["const:0:8"]]
- 0049838c ["COPY", "register:5010:8", ["const:0:8"]]
+ 004983cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
+ 004983cc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 004983cc ["COPY", "register:5008:8", ["const:0:8"]]
+ 004983cc ["COPY", "register:5010:8", ["const:0:8"]]
- 0049838c bytes 001940fd
+ 004983cc bytes 003940fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec5db6f7ffec700426f7b9483604219"></a>

### [`004986a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md) → [`004986e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md) FUN_004986e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00635aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635aa0.md) [`00636038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636038.md) [`0086af14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086af14.md) [`0086b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086b194.md) · 呼出先 6件 [`00498308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498308.md) [`0049aca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049aca4.md) [`0049acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049acb4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 4件 [`00635ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00635/00635ae0.md) [`00636078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/00636078.md) [`0086af54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086af54.md) [`0086b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086b/0086b1d4.md) · 呼出先 6件 [`00498348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498348.md) [`0049ace4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ace4.md) [`0049acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acf4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00498738",
      "incomplete_value": false,
      "site": "00498738",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004986f8",
      "incomplete_value": false,
      "site": "004986f8",
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
            "const:d18:8"
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
      "00498738",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ],
    [
      "00498770",
      "READ",
      [
        "storage",
        "00c65d38",
        null,
        "pointer"
      ]
    ],
    [
      "00498770",
      "READ",
      [
        "storage",
        "00c65d40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498738",
      "DATA",
      [
        "storage",
        "00c66118",
        null,
        "undefined *"
      ]
    ],
    [
      "00498770",
      "READ",
      [
        "storage",
        "00c66138",
        null,
        "pointer"
      ]
    ],
    [
      "00498770",
      "READ",
      [
        "storage",
        "00c66140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004986d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986d8) · [`004986e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986e4) · [`004986ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004986a4.md#insn-004986ec)
- 新版 [`00498718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md#insn-00498718) · [`00498724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md#insn-00498724) · [`0049872c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004986e4.md#insn-0049872c)

~~~diff
- 004986d8 ["INT_ADD", "register:40f0:8", ["const:4986d8:8", "const:4:8"]]
- 004986d8 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00498718 ["INT_ADD", "register:40f0:8", ["const:498718:8", "const:4:8"]]
+ 00498718 ["CALL", null, ["callee:00c53cd0:8"]]
- 004986d8 bytes 76ec1e94
+ 00498718 bytes 6eed1e94
- 004986e4 ["INT_ADD", "register:40f0:8", ["const:4986e4:8", "const:4:8"]]
- 004986e4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00498724 ["INT_ADD", "register:40f0:8", ["const:498724:8", "const:4:8"]]
+ 00498724 ["CALL", null, ["callee:00c53cd0:8"]]
- 004986e4 bytes 73ec1e94
+ 00498724 bytes 6bed1e94
- 004986ec ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 0049872c ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004986ec bytes 683e00b0
+ 0049872c bytes 683e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1347fa7247185ba590b0cb94d12c7a7"></a>

### [`0049889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049889c.md) → [`004988dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004988dc.md) FUN_004988dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "004988e0",
      "incomplete_value": false,
      "site": "004988e4",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004988a0",
      "incomplete_value": false,
      "site": "004988a4",
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
      "004988e4",
      "DATA",
      [
        "storage",
        "00c65b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004988e4",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004988a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/0049889c.md#insn-004988a0)
- 新版 [`004988e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004988dc.md#insn-004988e0)

~~~diff
- 004988a0 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 004988a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004988a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004988a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004988e0 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 004988e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004988e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004988e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004988a0 bytes 08e12d91
+ 004988e0 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-669be214ad2fb22b3e33319e530490bb"></a>

### [`004988ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988ac.md) → [`004988ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004988ec.md) FUN_004988ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004988fc",
      "incomplete_value": false,
      "site": "00498904",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004988bc",
      "incomplete_value": false,
      "site": "004988c4",
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
            "const:b78:8"
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
      "00498904",
      "DATA",
      [
        "storage",
        "00c65b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498904",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004988bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988ac.md#insn-004988bc) · [`004988c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/004988ac.md#insn-004988c8)
- 新版 [`004988fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004988ec.md#insn-004988fc) · [`00498908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004988ec.md#insn-00498908)

~~~diff
- 004988bc ["COPY", "tmp:0:8", ["const:b78:8"]]
- 004988bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004988bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004988bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004988fc ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 004988fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004988fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004988fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004988bc bytes 08e12d91
+ 004988fc bytes 08e13d91
- 004988c8 ["INT_ADD", "register:40f0:8", ["const:4988c8:8", "const:4:8"]]
- 004988c8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00498908 ["INT_ADD", "register:40f0:8", ["const:498908:8", "const:4:8"]]
+ 00498908 ["CALL", null, ["callee:00c57ea0:8"]]
- 004988c8 bytes 76fc1e94
+ 00498908 bytes 66fd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06fb79c247a49b8c628516a90122edad"></a>

### [`00498aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aac.md) → [`00498aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498aec.md) FUN_00498aec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "00498af0",
      "incomplete_value": false,
      "site": "00498af4",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498ab0",
      "incomplete_value": false,
      "site": "00498ab4",
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
            "const:bc8:8"
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
      "00498af4",
      "DATA",
      [
        "storage",
        "00c65bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498af4",
      "DATA",
      [
        "storage",
        "00c65fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498aac.md#insn-00498ab0)
- 新版 [`00498af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498aec.md#insn-00498af0)

~~~diff
- 00498ab0 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00498ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00498ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00498ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498af0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00498af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00498ab0 bytes 08212f91
+ 00498af0 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd42d75b99816a59dab72de5067301c"></a>

### [`00498abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498abc.md) → [`00498afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498afc.md) FUN_00498afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00498b0c",
      "incomplete_value": false,
      "site": "00498b14",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498acc",
      "incomplete_value": false,
      "site": "00498ad4",
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
            "const:bc8:8"
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
      "00498b14",
      "DATA",
      [
        "storage",
        "00c65bc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498b14",
      "DATA",
      [
        "storage",
        "00c65fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498abc.md#insn-00498acc) · [`00498ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498abc.md#insn-00498ad8)
- 新版 [`00498b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498afc.md#insn-00498b0c) · [`00498b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498afc.md#insn-00498b18)

~~~diff
- 00498acc ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00498acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00498acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00498acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00498b0c ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00498b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00498b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00498b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00498acc bytes 08212f91
+ 00498b0c bytes 08213f91
- 00498ad8 ["INT_ADD", "register:40f0:8", ["const:498ad8:8", "const:4:8"]]
- 00498ad8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00498b18 ["INT_ADD", "register:40f0:8", ["const:498b18:8", "const:4:8"]]
+ 00498b18 ["CALL", null, ["callee:00c57ea0:8"]]
- 00498ad8 bytes f2fb1e94
+ 00498b18 bytes e2fc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ea4dc2578b80a5348d9a5e0031a9ea"></a>

### [`00498cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md) → [`00498cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md) FUN_00498cfc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00497db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497db4.md) · 呼出先 15件 [`00499290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499290.md) [`00499430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499430.md) [`00499700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499700.md) [`00499704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/00499704.md) [`00597610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597610.md)
- 新版 呼出元 1件 [`00497df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497df4.md) · 呼出先 15件 [`004992d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004992d0.md) [`00499470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499470.md) [`00499740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499740.md) [`00499744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499744.md) [`00597650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.54% / 新版 96.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00498f64",
      "incomplete_value": false,
      "site": "00498f64",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498f24",
      "incomplete_value": false,
      "site": "00498f24",
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
            "const:c98:8"
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
      "definition_site": "00498d50",
      "incomplete_value": false,
      "site": "00498d54",
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
            "const:6ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498d10",
      "incomplete_value": false,
      "site": "00498d14",
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
            "const:6bf:8"
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
      "definition_site": "00499004",
      "incomplete_value": false,
      "site": "00499008",
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
            "const:56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498fc4",
      "incomplete_value": false,
      "site": "00498fc8",
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
            "const:16:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00498d50",
      "PARAM",
      [
        "storage",
        "002ae6bf",
        null,
        "string"
      ]
    ],
    [
      "00498f48",
      "PARAM",
      [
        "storage",
        "002ba027",
        null,
        "string"
      ]
    ],
    [
      "00498f64",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00498d50",
      "PARAM",
      [
        "storage",
        "002ae6ff",
        null,
        "string"
      ]
    ],
    [
      "00498f48",
      "PARAM",
      [
        "storage",
        "002ba067",
        null,
        "string"
      ]
    ],
    [
      "00498f64",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00498d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-00498d14) · [`00498ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-00498ee4) · [`00498fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498cbc.md#insn-00498fc8)
- 新版 [`00498d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md#insn-00498d54) · [`00498f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md#insn-00498f24) · [`00499008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/00498cfc.md#insn-00499008)

~~~diff
- 00498d14 ["INT_ADD", "register:40f0:8", ["const:498d14:8", "const:4:8"]]
- 00498d14 ["CALL", null, ["callee:00c58470:8"]]
+ 00498d54 ["INT_ADD", "register:40f0:8", ["const:498d54:8", "const:4:8"]]
+ 00498d54 ["CALL", null, ["callee:00c58470:8"]]
- 00498d14 bytes d7fc1e94
+ 00498d54 bytes c7fd1e94
- 00498ee4 ["INT_ADD", "register:40f0:8", ["const:498ee4:8", "const:4:8"]]
- 00498ee4 ["CALL", null, ["callee:00c580e0:8"]]
+ 00498f24 ["INT_ADD", "register:40f0:8", ["const:498f24:8", "const:4:8"]]
+ 00498f24 ["CALL", null, ["callee:00c580e0:8"]]
- 00498ee4 bytes 7ffb1e94
+ 00498f24 bytes 6ffc1e94
- 00498fc8 ["INT_ADD", "register:40f0:8", ["const:498fc8:8", "const:4:8"]]
- 00498fc8 ["CALL", null, ["callee:00c58470:8"]]
+ 00499008 ["INT_ADD", "register:40f0:8", ["const:499008:8", "const:4:8"]]
+ 00499008 ["CALL", null, ["callee:00c58470:8"]]
- 00498fc8 bytes 2afc1e94
+ 00499008 bytes 1afd1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b661393a79e28b77dfa5d1ddc4230bf7"></a>

### [`0049959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md) → [`004995dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004995dc.md) FUN_004995dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00499600",
      "incomplete_value": false,
      "site": "00499604",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004995c0",
      "incomplete_value": false,
      "site": "004995c4",
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
            "const:c18:8"
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
      "00499604",
      "DATA",
      [
        "storage",
        "00c65c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499604",
      "DATA",
      [
        "storage",
        "00c66018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004995b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995b0) · [`004995bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995bc) · [`004995c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/0049959c.md#insn-004995c0)
- 新版 [`004995f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004995dc.md#insn-004995f0) · [`004995fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004995dc.md#insn-004995fc) · [`00499600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004995dc.md#insn-00499600)

~~~diff
- 004995b0 ["INT_ADD", "register:40f0:8", ["const:4995b0:8", "const:4:8"]]
- 004995b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004995f0 ["INT_ADD", "register:40f0:8", ["const:4995f0:8", "const:4:8"]]
+ 004995f0 ["CALL", null, ["callee:00c57e90:8"]]
- 004995b0 bytes 38f91e94
+ 004995f0 bytes 28fa1e94
- 004995bc ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 004995fc ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004995bc bytes 683e0090
+ 004995fc bytes 683e00b0
- 004995c0 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 004995c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004995c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004995c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499600 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00499600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004995c0 bytes 08613091
+ 00499600 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d13ba27726c58db603abe45b22b996ff"></a>

### [`004995dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md) → [`0049961c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049961c.md) FUN_0049961c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00499620",
      "incomplete_value": false,
      "site": "00499624",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004995e0",
      "incomplete_value": false,
      "site": "004995e4",
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
            "const:c18:8"
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
      "00499624",
      "DATA",
      [
        "storage",
        "00c65c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499624",
      "DATA",
      [
        "storage",
        "00c66018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004995dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md#insn-004995dc) · [`004995e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004995dc.md#insn-004995e0)
- 新版 [`0049961c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049961c.md#insn-0049961c) · [`00499620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/0049961c.md#insn-00499620)

~~~diff
- 004995dc ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 0049961c ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004995dc bytes 683e0090
+ 0049961c bytes 683e00b0
- 004995e0 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 004995e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004995e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004995e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499620 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00499620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004995e0 bytes 08613091
+ 00499620 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94416c9b4d642a0226bd619e81a2a297"></a>

### [`004996b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md) → [`004996f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004996f0.md) FUN_004996f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00499710",
      "incomplete_value": false,
      "site": "00499714",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004996d0",
      "incomplete_value": false,
      "site": "004996d4",
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
            "const:c98:8"
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
      "00499714",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499714",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004996c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996c4) · [`004996cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996cc) · [`004996d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996b0.md#insn-004996d0)
- 新版 [`00499704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004996f0.md#insn-00499704) · [`0049970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004996f0.md#insn-0049970c) · [`00499710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/004996f0.md#insn-00499710)

~~~diff
- 004996c4 ["INT_ADD", "register:40f0:8", ["const:4996c4:8", "const:4:8"]]
- 004996c4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00499704 ["INT_ADD", "register:40f0:8", ["const:499704:8", "const:4:8"]]
+ 00499704 ["CALL", null, ["callee:00c57e90:8"]]
- 004996c4 bytes f3f81e94
+ 00499704 bytes e3f91e94
- 004996cc ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 0049970c ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004996cc bytes 683e0090
+ 0049970c bytes 683e00b0
- 004996d0 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 004996d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004996d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004996d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00499710 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00499710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00499710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00499710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004996d0 bytes 08613291
+ 00499710 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e90ee11534cdd79144f42fc8f32c300e"></a>

### [`004996e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md) → [`00499728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499728.md) FUN_00499728

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0049972c",
      "incomplete_value": false,
      "site": "00499730",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004996ec",
      "incomplete_value": false,
      "site": "004996f0",
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
            "const:c98:8"
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
      "00499730",
      "DATA",
      [
        "storage",
        "00c65c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00499730",
      "DATA",
      [
        "storage",
        "00c66098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004996e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md#insn-004996e8) · [`004996ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00499/004996e8.md#insn-004996ec)
- 新版 [`00499728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499728.md#insn-00499728) · [`0049972c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00499/00499728.md#insn-0049972c)

~~~diff
- 004996e8 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00499728 ["COPY", "register:4040:8", ["const:c66000:8"]]
- 004996e8 bytes 683e0090
+ 00499728 bytes 683e00b0
- 004996ec ["COPY", "tmp:0:8", ["const:c98:8"]]
- 004996ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004996ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004996ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049972c ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0049972c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049972c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049972c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004996ec bytes 08613291
+ 0049972c bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ffb596bdef15b27a890bda06cb7e44"></a>

### [`0049abc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md) → [`0049ac04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac04.md) FUN_0049ac04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "0049ac10",
      "incomplete_value": false,
      "site": "0049ac14",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049abd0",
      "incomplete_value": false,
      "site": "0049abd4",
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
            "const:d18:8"
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
      "0049ac14",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049ac14",
      "DATA",
      [
        "storage",
        "00c66118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049abcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md#insn-0049abcc) · [`0049abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abc4.md#insn-0049abd0)
- 新版 [`0049ac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac04.md#insn-0049ac0c) · [`0049ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac04.md#insn-0049ac10)

~~~diff
- 0049abcc ["COPY", "register:4048:8", ["const:c65000:8"]]
+ 0049ac0c ["COPY", "register:4048:8", ["const:c66000:8"]]
- 0049abcc bytes 493e00f0
+ 0049ac0c bytes 693e0090
- 0049abd0 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0049abd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049abd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049abd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049ac10 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0049ac10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049abd0 bytes 29613491
+ 0049ac10 bytes 29610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c32cc7fce4b5a608ec63c012119f8f78"></a>

### [`0049abe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md) → [`0049ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac24.md) FUN_0049ac24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0049ac2c",
      "incomplete_value": false,
      "site": "0049ac30",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049abec",
      "incomplete_value": false,
      "site": "0049abf0",
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
            "const:d18:8"
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
      "0049ac30",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049ac30",
      "DATA",
      [
        "storage",
        "00c66118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049abe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049abe8) · [`0049abec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049abec) · [`0049ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049abe4.md#insn-0049ac0c)
- 新版 [`0049ac28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac24.md#insn-0049ac28) · [`0049ac2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac24.md#insn-0049ac2c) · [`0049ac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac24.md#insn-0049ac4c)

~~~diff
- 0049abe8 ["COPY", "register:4048:8", ["const:c65000:8"]]
+ 0049ac28 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 0049abe8 bytes 493e00f0
+ 0049ac28 bytes 693e0090
- 0049abec ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0049abec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049abec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049abec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049ac2c ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0049ac2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049abec bytes 29613491
+ 0049ac2c bytes 29610491
- 0049ac0c ["INT_ADD", "register:40f0:8", ["const:49ac0c:8", "const:4:8"]]
- 0049ac0c ["CALL", null, ["callee:00c57e80:8"]]
+ 0049ac4c ["INT_ADD", "register:40f0:8", ["const:49ac4c:8", "const:4:8"]]
+ 0049ac4c ["CALL", null, ["callee:00c57e80:8"]]
- 0049ac0c bytes 9df31e94
+ 0049ac4c bytes 8df41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f834526d3b891bef2fadfb176122d52d"></a>

### [`0049ac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md) → [`0049ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac60.md) FUN_0049ac60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0049ac84",
      "incomplete_value": false,
      "site": "0049ac84",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ac44",
      "incomplete_value": false,
      "site": "0049ac44",
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
            "const:d18:8"
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
      "0049ac84",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049ac84",
      "DATA",
      [
        "storage",
        "00c66118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ac34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac34) · [`0049ac3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac3c) · [`0049ac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac20.md#insn-0049ac40)
- 新版 [`0049ac74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac60.md#insn-0049ac74) · [`0049ac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac60.md#insn-0049ac7c) · [`0049ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ac60.md#insn-0049ac80)

~~~diff
- 0049ac34 ["INT_ADD", "register:40f0:8", ["const:49ac34:8", "const:4:8"]]
- 0049ac34 ["CALL", null, ["callee:00c57e90:8"]]
+ 0049ac74 ["INT_ADD", "register:40f0:8", ["const:49ac74:8", "const:4:8"]]
+ 0049ac74 ["CALL", null, ["callee:00c57e90:8"]]
- 0049ac34 bytes 97f31e94
+ 0049ac74 bytes 87f41e94
- 0049ac3c ["COPY", "register:4048:8", ["const:c65000:8"]]
+ 0049ac7c ["COPY", "register:4048:8", ["const:c66000:8"]]
- 0049ac3c bytes 493e00f0
+ 0049ac7c bytes 693e0090
- 0049ac40 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0049ac40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049ac80 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0049ac80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049ac80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049ac40 bytes 29613491
+ 0049ac80 bytes 29610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-867b4b86ac7b8eddad4a52628d10d72b"></a>

### [`0049ac70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md) → [`0049acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acb0.md) FUN_0049acb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

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
      "definition_site": "0049acbc",
      "incomplete_value": false,
      "site": "0049acbc",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ac7c",
      "incomplete_value": false,
      "site": "0049ac7c",
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
            "const:d18:8"
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
      "0049acbc",
      "DATA",
      [
        "storage",
        "00c65d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0049acbc",
      "DATA",
      [
        "storage",
        "00c66118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ac74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac74) · [`0049ac78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac78) · [`0049ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049ac70.md#insn-0049ac98)
- 新版 [`0049acb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acb0.md#insn-0049acb4) · [`0049acb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acb0.md#insn-0049acb8) · [`0049acd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049acb0.md#insn-0049acd8)

~~~diff
- 0049ac74 ["COPY", "register:4048:8", ["const:c65000:8"]]
+ 0049acb4 ["COPY", "register:4048:8", ["const:c66000:8"]]
- 0049ac74 bytes 493e00f0
+ 0049acb4 bytes 693e0090
- 0049ac78 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 0049ac78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0049ac78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0049acb8 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 0049acb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0049acb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0049acb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0049ac78 bytes 29613491
+ 0049acb8 bytes 29610491
- 0049ac98 ["INT_ADD", "register:40f0:8", ["const:49ac98:8", "const:4:8"]]
- 0049ac98 ["CALL", null, ["callee:00c53cd0:8"]]
+ 0049acd8 ["INT_ADD", "register:40f0:8", ["const:49acd8:8", "const:4:8"]]
+ 0049acd8 ["CALL", null, ["callee:00c53cd0:8"]]
- 0049ac98 bytes 06e31e94
+ 0049acd8 bytes fee31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94dea64a7e76575338d6965371779239"></a>

### [`0049adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md) → [`0049ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ae2c.md) _INIT_24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ae68",
      "incomplete_value": true,
      "site": "0049ae84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0049ae28",
      "incomplete_value": true,
      "site": "0049ae44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "0049ae8c",
      "incomplete_value": true,
      "site": "0049aea8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0049ae4c",
      "incomplete_value": true,
      "site": "0049ae68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "0049aeac",
      "incomplete_value": true,
      "site": "0049aec8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0049ae6c",
      "incomplete_value": true,
      "site": "0049ae88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
      "0049ae68",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0049ae8c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0049aeac",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049ae68",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0049ae8c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0049aeac",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049ae64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049ae64) · [`0049ae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049ae84) · [`0049af4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049a/0049adec.md#insn-0049af4c)
- 新版 [`0049aea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ae2c.md#insn-0049aea4) · [`0049aec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ae2c.md#insn-0049aec4) · [`0049af8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049a/0049ae2c.md#insn-0049af8c)

~~~diff
- 0049ae64 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0049ae64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0049ae64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0049ae64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049aea4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0049aea4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049aea4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049aea4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0049ae64 bytes 4a093691
+ 0049aea4 bytes 4a093791
- 0049ae84 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0049ae84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0049ae84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0049ae84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049aec4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0049aec4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049aec4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049aec4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0049ae84 bytes 4a553a91
+ 0049aec4 bytes 4a893d91
- 0049af4c ["INT_ADD", "register:40f0:8", ["const:49af4c:8", "const:4:8"]]
- 0049af4c ["CALL", null, ["callee:0043b7f8:8"]]
+ 0049af8c ["INT_ADD", "register:40f0:8", ["const:49af8c:8", "const:4:8"]]
+ 0049af8c ["CALL", null, ["callee:0043b7f8:8"]]
- 0049af4c bytes 1b82fe97
+ 0049af8c bytes 1b82fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e23d4c246cfd204f320dde3e9eafe2e6"></a>

### [`0049b17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md) → [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) FUN_0049b1bc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004466bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/004466bc.md) · 呼出先 11件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md)
- 新版 呼出元 1件 [`004466fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004466fc.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b22c",
      "incomplete_value": true,
      "site": "0049b238",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b1ec",
      "incomplete_value": true,
      "site": "0049b1f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:320:8"
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
      "definition_site": "0049b228",
      "incomplete_value": true,
      "site": "0049b23c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f97:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b1e8",
      "incomplete_value": true,
      "site": "0049b1fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f57:8"
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
      "definition_site": "0049b228",
      "incomplete_value": true,
      "site": "0049b23c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0049b1e8",
      "incomplete_value": true,
      "site": "0049b1fc",
      "value": [
        "LOAD",
        "16",
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
      "0049b228",
      "READ",
      [
        "storage",
        "002c0f57",
        null,
        "string"
      ]
    ],
    [
      "0049b228",
      "READ",
      [
        "storage",
        "002c0f67",
        null,
        "string"
      ]
    ],
    [
      "0049b22c",
      "READ",
      [
        "storage",
        "002c2320",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049b228",
      "READ",
      [
        "storage",
        "002c0f97",
        null,
        "string"
      ]
    ],
    [
      "0049b228",
      "READ",
      [
        "storage",
        "002c0fa7",
        null,
        "string"
      ]
    ],
    [
      "0049b22c",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b23c) · [`0049b1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b1a8) · [`0049b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b17c.md#insn-0049b1b0)
- 新版 [`0049b27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md#insn-0049b27c) · [`0049b1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md#insn-0049b1e8) · [`0049b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md#insn-0049b1f0)

~~~diff
- 0049b23c ["INT_ADD", "register:40f0:8", ["const:49b23c:8", "const:4:8"]]
- 0049b23c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0049b27c ["INT_ADD", "register:40f0:8", ["const:49b27c:8", "const:4:8"]]
+ 0049b27c ["CALL", null, ["callee:00c57eb0:8"]]
- 0049b23c bytes 1df21e94
+ 0049b27c bytes 0df31e94
- 0049b1a8 ["INT_ADD", "register:40f0:8", ["const:49b1a8:8", "const:4:8"]]
- 0049b1a8 ["CALL", null, ["callee:00588e6c:8"]]
+ 0049b1e8 ["INT_ADD", "register:40f0:8", ["const:49b1e8:8", "const:4:8"]]
+ 0049b1e8 ["CALL", null, ["callee:00588e6c:8"]]
- 0049b1a8 bytes 21b70394
+ 0049b1e8 bytes 21b70394
- 0049b1b0 ["INT_ADD", "register:40f0:8", ["const:49b1b0:8", "const:4:8"]]
- 0049b1b0 ["CALL", null, ["callee:0058915c:8"]]
+ 0049b1f0 ["INT_ADD", "register:40f0:8", ["const:49b1f0:8", "const:4:8"]]
+ 0049b1f0 ["CALL", null, ["callee:0058915c:8"]]
- 0049b1b0 bytes dbb70394
+ 0049b1f0 bytes dbb70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3977e66821f38d2ab5428cfb74af5c31"></a>

### [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) → [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) FUN_0049b4a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) [`0049fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fab0.md) [`0049fc28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fc28.md) [`0049fd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049fd90.md) · 呼出先 4件 [`0047d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d574.md) [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 4件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) [`0049faf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md) [`0049fc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md) [`0049fdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md) · 呼出先 4件 [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049b594",
      "incomplete_value": false,
      "site": "0049b59c",
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
            "const:ade:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b554",
      "incomplete_value": false,
      "site": "0049b55c",
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
            "const:a11:8"
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
      "definition_site": "0049b5a4",
      "incomplete_value": true,
      "site": "0049b5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049b564",
      "incomplete_value": true,
      "site": "0049b568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049b59c",
      "DATA",
      [
        "storage",
        "002a8a11",
        null,
        "string"
      ]
    ],
    [
      "0049b5a4",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049b5a4",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049b59c",
      "DATA",
      [
        "storage",
        "002a8ade",
        null,
        "string"
      ]
    ],
    [
      "0049b5a4",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049b5a4",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b568) · [`0049b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b4f4) · [`0049b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md#insn-0049b544)
- 新版 [`0049b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md#insn-0049b5a8) · [`0049b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md#insn-0049b534) · [`0049b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md#insn-0049b584)

~~~diff
- 0049b568 ["INT_ADD", "register:40f0:8", ["const:49b568:8", "const:4:8"]]
- 0049b568 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049b5a8 ["INT_ADD", "register:40f0:8", ["const:49b5a8:8", "const:4:8"]]
+ 0049b5a8 ["CALL", null, ["callee:00c57f10:8"]]
- 0049b568 bytes 6af11e94
+ 0049b5a8 bytes 5af21e94
- 0049b4f4 ["INT_ADD", "register:40f0:8", ["const:49b4f4:8", "const:4:8"]]
- 0049b4f4 ["CALL", null, ["callee:0047d5b4:8"]]
+ 0049b534 ["INT_ADD", "register:40f0:8", ["const:49b534:8", "const:4:8"]]
+ 0049b534 ["CALL", null, ["callee:0047d5b4:8"]]
- 0049b4f4 bytes 2088ff97
+ 0049b534 bytes 2088ff97
- 0049b544 ["INT_ADD", "register:40f0:8", ["const:49b544:8", "const:4:8"]]
- 0049b544 ["CALL", null, ["callee:0047d6b8:8"]]
+ 0049b584 ["INT_ADD", "register:40f0:8", ["const:49b584:8", "const:4:8"]]
+ 0049b584 ["CALL", null, ["callee:0047d6b8:8"]]
- 0049b544 bytes 4d88ff97
+ 0049b584 bytes 4d88ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-825e8601ba29ab38b5829a1e90553bcd"></a>

### [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) → [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) FUN_0049b68c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0049b56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b56c.md) · 呼出先 15件 [`0049b388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b388.md) [`0049b394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b394.md) [`0049b460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b460.md) [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) [`0049ec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ec64.md)
- 新版 呼出元 1件 [`0049b5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b5ac.md) · 呼出先 15件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3d4.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) [`0049eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eca4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.22% / 新版 95.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049bb44",
      "incomplete_value": false,
      "site": "0049bb48",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bb04",
      "incomplete_value": false,
      "site": "0049bb08",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049bb08",
      "incomplete_value": true,
      "site": "0049bb0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bac8",
      "incomplete_value": true,
      "site": "0049bacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "definition_site": "0049bb68",
      "incomplete_value": true,
      "site": "0049bb6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bb28",
      "incomplete_value": true,
      "site": "0049bb2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049b87c",
      "DATA",
      [
        "storage",
        "002ca69d",
        null,
        null
      ]
    ],
    [
      "0049b880",
      "DATA",
      [
        "storage",
        "002ca5f9",
        null,
        null
      ]
    ],
    [
      "0049b888",
      "DATA",
      [
        "storage",
        "002ca622",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0049b87c",
      "DATA",
      [
        "storage",
        "002ca6dd",
        null,
        null
      ]
    ],
    [
      "0049b880",
      "DATA",
      [
        "storage",
        "002ca639",
        null,
        null
      ]
    ],
    [
      "0049b888",
      "DATA",
      [
        "storage",
        "002ca662",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049bac8) · [`0049bacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049bacc) · [`0049bb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md#insn-0049bb2c)
- 新版 [`0049bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md#insn-0049bb08) · [`0049bb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md#insn-0049bb0c) · [`0049bb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md#insn-0049bb6c)

~~~diff
- 0049bac8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:908:8"]]
- 0049bac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049bb08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d08:8"]]
+ 0049bb08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049bac8 bytes 218444f9
+ 0049bb08 bytes 218446f9
- 0049bacc ["INT_ADD", "register:40f0:8", ["const:49bacc:8", "const:4:8"]]
- 0049bacc ["CALL", null, ["callee:00c57f10:8"]]
+ 0049bb0c ["INT_ADD", "register:40f0:8", ["const:49bb0c:8", "const:4:8"]]
+ 0049bb0c ["CALL", null, ["callee:00c57f10:8"]]
- 0049bacc bytes 11f01e94
+ 0049bb0c bytes 01f11e94
- 0049bb2c ["INT_ADD", "register:40f0:8", ["const:49bb2c:8", "const:4:8"]]
- 0049bb2c ["CALL", null, ["callee:00c57f10:8"]]
+ 0049bb6c ["INT_ADD", "register:40f0:8", ["const:49bb6c:8", "const:4:8"]]
+ 0049bb6c ["CALL", null, ["callee:00c57f10:8"]]
- 0049bb2c bytes f9ef1e94
+ 0049bb6c bytes e9f01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5104bf9e6a863cbaec9d555a8241dd5d"></a>

### [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) → [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) FUN_0049bc5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049b64c.md) · 呼出先 15件 [`0047d678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d678.md) [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md)
- 新版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 15件 [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049bf30",
      "incomplete_value": false,
      "site": "0049bf34",
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
            "const:ade:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bef0",
      "incomplete_value": false,
      "site": "0049bef4",
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
            "const:a11:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049bf54",
      "incomplete_value": true,
      "site": "0049bf58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049bf14",
      "incomplete_value": true,
      "site": "0049bf18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049bf34",
      "DATA",
      [
        "storage",
        "002a8a11",
        null,
        "string"
      ]
    ],
    [
      "0049bf54",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049bf54",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049bf34",
      "DATA",
      [
        "storage",
        "002a8ade",
        null,
        "string"
      ]
    ],
    [
      "0049bf54",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049bf54",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049bf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bf18) · [`0049bf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bf34) · [`0049bc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md#insn-0049bc9c)
- 新版 [`0049bf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md#insn-0049bf58) · [`0049bf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md#insn-0049bf74) · [`0049bcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md#insn-0049bcdc)

~~~diff
- 0049bf18 ["INT_ADD", "register:40f0:8", ["const:49bf18:8", "const:4:8"]]
- 0049bf18 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049bf58 ["INT_ADD", "register:40f0:8", ["const:49bf58:8", "const:4:8"]]
+ 0049bf58 ["CALL", null, ["callee:00c57f10:8"]]
- 0049bf18 bytes feee1e94
+ 0049bf58 bytes eeef1e94
- 0049bf34 ["INT_ADD", "register:40f0:8", ["const:49bf34:8", "const:4:8"]]
- 0049bf34 ["CALL", null, ["callee:0047d6b8:8"]]
+ 0049bf74 ["INT_ADD", "register:40f0:8", ["const:49bf74:8", "const:4:8"]]
+ 0049bf74 ["CALL", null, ["callee:0047d6b8:8"]]
- 0049bf34 bytes d185ff97
+ 0049bf74 bytes d185ff97
- 0049bc9c ["INT_ADD", "register:40f0:8", ["const:49bc9c:8", "const:4:8"]]
- 0049bc9c ["CALL", null, ["callee:00c57e90:8"]]
+ 0049bcdc ["INT_ADD", "register:40f0:8", ["const:49bcdc:8", "const:4:8"]]
+ 0049bcdc ["CALL", null, ["callee:00c57e90:8"]]
- 0049bc9c bytes 7def1e94
+ 0049bcdc bytes 6df01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d616db4dcc9d5da5c67afa7dd3d8577"></a>

### [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) → [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) FUN_0049c378

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 14件 [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0049f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f400.md) [`0049f6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f6ec.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 14件 [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0049f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f440.md) [`0049f72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f72c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049c9f4",
      "incomplete_value": false,
      "site": "0049c9f8",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c9b4",
      "incomplete_value": false,
      "site": "0049c9b8",
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
            "const:a24:8"
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
      "definition_site": "0049c9e0",
      "incomplete_value": true,
      "site": "0049c9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c9a0",
      "incomplete_value": true,
      "site": "0049c9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "definition_site": "0049ca18",
      "incomplete_value": true,
      "site": "0049ca1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049c9d8",
      "incomplete_value": true,
      "site": "0049c9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049c9d4",
      "DATA",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "0049c9d4",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049c9e0",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049c9d4",
      "DATA",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "0049c9d4",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "0049c9e0",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049c9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c9a4) · [`0049c9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c9dc) · [`0049c3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md#insn-0049c3f8)
- 新版 [`0049c9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md#insn-0049c9e4) · [`0049ca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md#insn-0049ca1c) · [`0049c438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md#insn-0049c438)

~~~diff
- 0049c9a4 ["INT_ADD", "register:40f0:8", ["const:49c9a4:8", "const:4:8"]]
- 0049c9a4 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049c9e4 ["INT_ADD", "register:40f0:8", ["const:49c9e4:8", "const:4:8"]]
+ 0049c9e4 ["CALL", null, ["callee:00c57f10:8"]]
- 0049c9a4 bytes 5bec1e94
+ 0049c9e4 bytes 4bed1e94
- 0049c9dc ["INT_ADD", "register:40f0:8", ["const:49c9dc:8", "const:4:8"]]
- 0049c9dc ["CALL", null, ["callee:00c57f10:8"]]
+ 0049ca1c ["INT_ADD", "register:40f0:8", ["const:49ca1c:8", "const:4:8"]]
+ 0049ca1c ["CALL", null, ["callee:00c57f10:8"]]
- 0049c9dc bytes 4dec1e94
+ 0049ca1c bytes 3ded1e94
- 0049c3f8 ["COPY", "tmp:0:8", ["const:674:8"]]
- 0049c3f8 ["INT_CARRY", "register:105:1", ["register:4078:8", "tmp:0:8"]]
- 0049c3f8 ["INT_SCARRY", "register:106:1", ["register:4078:8", "tmp:0:8"]]
- 0049c3f8 ["INT_ADD", "tmp:1:8", ["register:4078:8", "tmp:0:8"]]
+ 0049c438 ["COPY", "tmp:0:8", ["const:6b4:8"]]
+ 0049c438 ["INT_CARRY", "register:105:1", ["register:4078:8", "tmp:0:8"]]
+ 0049c438 ["INT_SCARRY", "register:106:1", ["register:4078:8", "tmp:0:8"]]
+ 0049c438 ["INT_ADD", "tmp:1:8", ["register:4078:8", "tmp:0:8"]]
- 0049c3f8 bytes efd11991
+ 0049c438 bytes efd11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b28b264726216f7f4e5dc606deb32393"></a>

### [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) → [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) FUN_0049cadc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 5件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 5件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md) [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049ce18",
      "incomplete_value": true,
      "site": "0049ce1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049cdd8",
      "incomplete_value": true,
      "site": "0049cddc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049ce0c",
      "DATA",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049cddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cddc) · [`0049cd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cd40) · [`0049cd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md#insn-0049cd80)
- 新版 [`0049ce1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md#insn-0049ce1c) · [`0049cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md#insn-0049cd80) · [`0049cdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md#insn-0049cdc0)

~~~diff
- 0049cddc ["INT_ADD", "register:40f0:8", ["const:49cddc:8", "const:4:8"]]
- 0049cddc ["CALL", null, ["callee:00c57f10:8"]]
+ 0049ce1c ["INT_ADD", "register:40f0:8", ["const:49ce1c:8", "const:4:8"]]
+ 0049ce1c ["CALL", null, ["callee:00c57f10:8"]]
- 0049cddc bytes 4deb1e94
+ 0049ce1c bytes 3dec1e94
- 0049cd40 ["INT_ADD", "register:40f0:8", ["const:49cd40:8", "const:4:8"]]
- 0049cd40 ["CALL", null, ["callee:0049f418:8"]]
+ 0049cd80 ["INT_ADD", "register:40f0:8", ["const:49cd80:8", "const:4:8"]]
+ 0049cd80 ["CALL", null, ["callee:0049f418:8"]]
- 0049cd40 bytes a6090094
+ 0049cd80 bytes a6090094
- 0049cd80 ["INT_ADD", "register:40f0:8", ["const:49cd80:8", "const:4:8"]]
- 0049cd80 ["CALL", null, ["callee:0049f404:8"]]
+ 0049cdc0 ["INT_ADD", "register:40f0:8", ["const:49cdc0:8", "const:4:8"]]
+ 0049cdc0 ["CALL", null, ["callee:0049f404:8"]]
- 0049cd80 bytes 91090094
+ 0049cdc0 bytes 91090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02bfc7f038039304f315b020b7546601"></a>

### [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) → [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md) FUN_0049ce20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bc1c.md) · 呼出先 5件 [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) · 呼出先 5件 [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) [`0049dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md) [`0049df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d070",
      "incomplete_value": false,
      "site": "0049d078",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d030",
      "incomplete_value": false,
      "site": "0049d038",
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
            "const:a24:8"
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
      "definition_site": "0049d080",
      "incomplete_value": true,
      "site": "0049d084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d040",
      "incomplete_value": true,
      "site": "0049d044",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "0049d078",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049d080",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049d080",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d078",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049d080",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049d080",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049d044) · [`0049ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049ce14) · [`0049ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md#insn-0049ce20)
- 新版 [`0049d084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md#insn-0049d084) · [`0049ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md#insn-0049ce54) · [`0049ce60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md#insn-0049ce60)

~~~diff
- 0049d044 ["INT_ADD", "register:40f0:8", ["const:49d044:8", "const:4:8"]]
- 0049d044 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049d084 ["INT_ADD", "register:40f0:8", ["const:49d084:8", "const:4:8"]]
+ 0049d084 ["CALL", null, ["callee:00c57f10:8"]]
- 0049d044 bytes b3ea1e94
+ 0049d084 bytes a3eb1e94
- 0049ce14 ["INT_ADD", "register:40f0:8", ["const:49ce14:8", "const:4:8"]]
- 0049ce14 ["CALL", null, ["callee:0049d4c4:8"]]
+ 0049ce54 ["INT_ADD", "register:40f0:8", ["const:49ce54:8", "const:4:8"]]
+ 0049ce54 ["CALL", null, ["callee:0049d4c4:8"]]
- 0049ce14 bytes 9c010094
+ 0049ce54 bytes 9c010094
- 0049ce20 ["INT_ADD", "register:40f0:8", ["const:49ce20:8", "const:4:8"]]
- 0049ce20 ["CALL", null, ["callee:0049dcd4:8"]]
+ 0049ce60 ["INT_ADD", "register:40f0:8", ["const:49ce60:8", "const:4:8"]]
+ 0049ce60 ["CALL", null, ["callee:0049dcd4:8"]]
- 0049ce20 bytes 9d030094
+ 0049ce60 bytes 9d030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52d474da64841350de523abf0ed26dc4"></a>

### [`0049d234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md) → [`0049d274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md) FUN_0049d274

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 5件 [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) [`0049e694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e694.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) · 呼出先 5件 [`0049e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md) [`0049e6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e6d4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d3ac",
      "incomplete_value": false,
      "site": "0049d3b4",
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
            "const:97d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d36c",
      "incomplete_value": false,
      "site": "0049d374",
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
            "const:93d:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049d3bc",
      "incomplete_value": true,
      "site": "0049d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d37c",
      "incomplete_value": true,
      "site": "0049d380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049d3b4",
      "DATA",
      [
        "storage",
        "002b293d",
        null,
        "string"
      ]
    ],
    [
      "0049d3bc",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3bc",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049d3b4",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "0049d3bc",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049d3bc",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d380) · [`0049d3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d3b4) · [`0049d2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d234.md#insn-0049d2fc)
- 新版 [`0049d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md#insn-0049d3c0) · [`0049d3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md#insn-0049d3f4) · [`0049d33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d274.md#insn-0049d33c)

~~~diff
- 0049d380 ["INT_ADD", "register:40f0:8", ["const:49d380:8", "const:4:8"]]
- 0049d380 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049d3c0 ["INT_ADD", "register:40f0:8", ["const:49d3c0:8", "const:4:8"]]
+ 0049d3c0 ["CALL", null, ["callee:00c57f10:8"]]
- 0049d380 bytes e4e91e94
+ 0049d3c0 bytes d4ea1e94
- 0049d3b4 ["INT_ADD", "register:40f0:8", ["const:49d3b4:8", "const:4:8"]]
- 0049d3b4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 0049d3f4 ["INT_ADD", "register:40f0:8", ["const:49d3f4:8", "const:4:8"]]
+ 0049d3f4 ["CALL", null, ["callee:00c57ee0:8"]]
- 0049d3b4 bytes cbe91e94
+ 0049d3f4 bytes bbea1e94
- 0049d2fc ["INT_ADD", "register:40f0:8", ["const:49d2fc:8", "const:4:8"]]
- 0049d2fc ["CALL", null, ["callee:0049e4c4:8"]]
+ 0049d33c ["INT_ADD", "register:40f0:8", ["const:49d33c:8", "const:4:8"]]
+ 0049d33c ["CALL", null, ["callee:0049e4c4:8"]]
- 0049d2fc bytes 62040094
+ 0049d33c bytes 62040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8a237343c2b72374e325e37b57f2c9"></a>

### [`0049d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md) → [`0049d4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md) FUN_0049d4c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 3件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md) · 呼出先 3件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049d8a0",
      "incomplete_value": false,
      "site": "0049d8a8",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d860",
      "incomplete_value": false,
      "site": "0049d868",
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
            "const:a24:8"
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
      "definition_site": "0049d8b0",
      "incomplete_value": true,
      "site": "0049d8b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d870",
      "incomplete_value": true,
      "site": "0049d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049d500",
      "DATA",
      [
        "storage",
        "002c2d20",
        null,
        null
      ]
    ],
    [
      "0049d8a8",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049d8b0",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049d500",
      "DATA",
      [
        "storage",
        "002c2d60",
        null,
        null
      ]
    ],
    [
      "0049d8a8",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049d8b0",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d874) · [`0049d4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d4b8) · [`0049d560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d484.md#insn-0049d560)
- 新版 [`0049d8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md#insn-0049d8b4) · [`0049d4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md#insn-0049d4f8) · [`0049d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d4c4.md#insn-0049d5a0)

~~~diff
- 0049d874 ["INT_ADD", "register:40f0:8", ["const:49d874:8", "const:4:8"]]
- 0049d874 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049d8b4 ["INT_ADD", "register:40f0:8", ["const:49d8b4:8", "const:4:8"]]
+ 0049d8b4 ["CALL", null, ["callee:00c57f10:8"]]
- 0049d874 bytes a7e81e94
+ 0049d8b4 bytes 97e91e94
- 0049d4b8 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 0049d4b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0049d4b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0049d4b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0049d4f8 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 0049d4f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d4f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0049d4f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0049d4b8 bytes 4a813491
+ 0049d4f8 bytes 4a813591
- 0049d560 ["INT_ADD", "register:40f0:8", ["const:49d560:8", "const:4:8"]]
- 0049d560 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d5a0 ["INT_ADD", "register:40f0:8", ["const:49d5a0:8", "const:4:8"]]
+ 0049d5a0 ["CALL", null, ["callee:0049d198:8"]]
- 0049d560 bytes fefeff97
+ 0049d5a0 bytes fefeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f59c03897d47265de017005385917be"></a>

### [`0049d878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md) → [`0049d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md) FUN_0049d8b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) · 呼出先 3件 [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) · 呼出先 3件 [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049da08",
      "incomplete_value": false,
      "site": "0049da10",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d9c8",
      "incomplete_value": false,
      "site": "0049d9d0",
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
            "const:a24:8"
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
      "definition_site": "0049da18",
      "incomplete_value": true,
      "site": "0049da1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049d9d8",
      "incomplete_value": true,
      "site": "0049d9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049da10",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049da18",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049da18",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049da10",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049da18",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049da18",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049d9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d9dc) · [`0049d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d980) · [`0049d994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d878.md#insn-0049d994)
- 新版 [`0049da1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md#insn-0049da1c) · [`0049d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md#insn-0049d9c0) · [`0049d9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d8b8.md#insn-0049d9d4)

~~~diff
- 0049d9dc ["INT_ADD", "register:40f0:8", ["const:49d9dc:8", "const:4:8"]]
- 0049d9dc ["CALL", null, ["callee:00c57f10:8"]]
+ 0049da1c ["INT_ADD", "register:40f0:8", ["const:49da1c:8", "const:4:8"]]
+ 0049da1c ["CALL", null, ["callee:00c57f10:8"]]
- 0049d9dc bytes 4de81e94
+ 0049da1c bytes 3de91e94
- 0049d980 ["INT_ADD", "register:40f0:8", ["const:49d980:8", "const:4:8"]]
- 0049d980 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d9c0 ["INT_ADD", "register:40f0:8", ["const:49d9c0:8", "const:4:8"]]
+ 0049d9c0 ["CALL", null, ["callee:0049d198:8"]]
- 0049d980 bytes f6fdff97
+ 0049d9c0 bytes f6fdff97
- 0049d994 ["INT_ADD", "register:40f0:8", ["const:49d994:8", "const:4:8"]]
- 0049d994 ["CALL", null, ["callee:0049d198:8"]]
+ 0049d9d4 ["INT_ADD", "register:40f0:8", ["const:49d9d4:8", "const:4:8"]]
+ 0049d9d4 ["CALL", null, ["callee:0049d198:8"]]
- 0049d994 bytes f1fdff97
+ 0049d9d4 bytes f1fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-decafee6c7c45578209270f29c051897"></a>

### [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) → [`0049dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md) FUN_0049dcd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049cde0.md) · 呼出先 4件 [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0049ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049ce20.md) · 呼出先 4件 [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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
      "definition_site": "0049df28",
      "incomplete_value": false,
      "site": "0049df30",
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
            "const:a5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049dee8",
      "incomplete_value": false,
      "site": "0049def0",
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
            "const:991:8"
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
      "definition_site": "0049df38",
      "incomplete_value": true,
      "site": "0049df3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049def8",
      "incomplete_value": true,
      "site": "0049defc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049df30",
      "DATA",
      [
        "storage",
        "002a9991",
        null,
        "string"
      ]
    ],
    [
      "0049df38",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049df38",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049df30",
      "DATA",
      [
        "storage",
        "002a9a5e",
        null,
        "string"
      ]
    ],
    [
      "0049df38",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049df38",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049defc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049defc) · [`0049dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049dec0) · [`0049dec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md#insn-0049dec8)
- 新版 [`0049df3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md#insn-0049df3c) · [`0049df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md#insn-0049df00) · [`0049df08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md#insn-0049df08)

~~~diff
- 0049defc ["INT_ADD", "register:40f0:8", ["const:49defc:8", "const:4:8"]]
- 0049defc ["CALL", null, ["callee:00c57f10:8"]]
+ 0049df3c ["INT_ADD", "register:40f0:8", ["const:49df3c:8", "const:4:8"]]
+ 0049df3c ["CALL", null, ["callee:00c57f10:8"]]
- 0049defc bytes 05e71e94
+ 0049df3c bytes f5e71e94
- 0049dec0 ["INT_ADD", "register:40f0:8", ["const:49dec0:8", "const:4:8"]]
- 0049dec0 ["CALL", null, ["callee:0049f404:8"]]
+ 0049df00 ["INT_ADD", "register:40f0:8", ["const:49df00:8", "const:4:8"]]
+ 0049df00 ["CALL", null, ["callee:0049f404:8"]]
- 0049dec0 bytes 41050094
+ 0049df00 bytes 41050094
- 0049dec8 ["INT_ADD", "register:40f0:8", ["const:49dec8:8", "const:4:8"]]
- 0049dec8 ["CALL", null, ["callee:0049f418:8"]]
+ 0049df08 ["INT_ADD", "register:40f0:8", ["const:49df08:8", "const:4:8"]]
+ 0049df08 ["CALL", null, ["callee:0049f418:8"]]
- 0049dec8 bytes 44050094
+ 0049df08 bytes 44050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02092c220077a6157d7bbcaa229256ed"></a>

### [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) → [`0049e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) FUN_0049e904

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049c338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049c338.md) · 呼出先 8件 [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) [`0049f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f8a0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) · 呼出先 8件 [`0049eaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md) [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ea3c",
      "incomplete_value": false,
      "site": "0049ea40",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049e9fc",
      "incomplete_value": false,
      "site": "0049ea00",
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
            "const:a24:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ea60",
      "incomplete_value": false,
      "site": "0049ea64",
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
            "const:b01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ea20",
      "incomplete_value": false,
      "site": "0049ea24",
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
            "const:a34:8"
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
      "definition_site": "0049ea4c",
      "incomplete_value": true,
      "site": "0049ea50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049ea0c",
      "incomplete_value": true,
      "site": "0049ea10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "0049ea40",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049ea4c",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049ea4c",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049ea40",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049ea4c",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049ea4c",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049e9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049e9f4) · [`0049ea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049ea10) · [`0049ea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md#insn-0049ea34)
- 新版 [`0049ea34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md#insn-0049ea34) · [`0049ea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md#insn-0049ea50) · [`0049ea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md#insn-0049ea74)

~~~diff
- 0049e9f4 ["INT_ADD", "register:40f0:8", ["const:49e9f4:8", "const:4:8"]]
- 0049e9f4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0049ea34 ["INT_ADD", "register:40f0:8", ["const:49ea34:8", "const:4:8"]]
+ 0049ea34 ["CALL", null, ["callee:00c57ef0:8"]]
- 0049e9f4 bytes 3fe41e94
+ 0049ea34 bytes 2fe51e94
- 0049ea10 ["INT_ADD", "register:40f0:8", ["const:49ea10:8", "const:4:8"]]
- 0049ea10 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049ea50 ["INT_ADD", "register:40f0:8", ["const:49ea50:8", "const:4:8"]]
+ 0049ea50 ["CALL", null, ["callee:00c57f10:8"]]
- 0049ea10 bytes 40e41e94
+ 0049ea50 bytes 30e51e94
- 0049ea34 ["INT_ADD", "register:40f0:8", ["const:49ea34:8", "const:4:8"]]
- 0049ea34 ["CALL", null, ["callee:00c57f10:8"]]
+ 0049ea74 ["INT_ADD", "register:40f0:8", ["const:49ea74:8", "const:4:8"]]
+ 0049ea74 ["CALL", null, ["callee:00c57f10:8"]]
- 0049ea34 bytes 37e41e94
+ 0049ea74 bytes 27e51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32eb088d20d3457ca047fe6e95493156"></a>

### [`0049ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md) → [`0049eaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md) FUN_0049eaac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0049d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d9e0.md) [`0049e8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e8c4.md) · 呼出先 2件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) · 呼出先 2件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049eb88",
      "incomplete_value": false,
      "site": "0049eb90",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049eb48",
      "incomplete_value": false,
      "site": "0049eb50",
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
            "const:a24:8"
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
      "definition_site": "0049eb98",
      "incomplete_value": true,
      "site": "0049eb9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049eb58",
      "incomplete_value": true,
      "site": "0049eb5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
              ]
            ]
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
      "0049eb90",
      "DATA",
      [
        "storage",
        "002a8a24",
        null,
        "string"
      ]
    ],
    [
      "0049eb98",
      "READ",
      [
        "storage",
        "00c9a908",
        null,
        "pointer"
      ]
    ],
    [
      "0049eb98",
      "PARAM",
      [
        "storage",
        "00c96840",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049eb90",
      "DATA",
      [
        "storage",
        "002a8af1",
        null,
        "string"
      ]
    ],
    [
      "0049eb98",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049eb98",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049eb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb5c) · [`0049eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb40) · [`0049eb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049ea6c.md#insn-0049eb48)
- 新版 [`0049eb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md#insn-0049eb9c) · [`0049eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md#insn-0049eb80) · [`0049eb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eaac.md#insn-0049eb88)

~~~diff
- 0049eb5c ["INT_ADD", "register:40f0:8", ["const:49eb5c:8", "const:4:8"]]
- 0049eb5c ["CALL", null, ["callee:00c57f10:8"]]
+ 0049eb9c ["INT_ADD", "register:40f0:8", ["const:49eb9c:8", "const:4:8"]]
+ 0049eb9c ["CALL", null, ["callee:00c57f10:8"]]
- 0049eb5c bytes ede31e94
+ 0049eb9c bytes dde41e94
- 0049eb40 ["INT_ADD", "register:40f0:8", ["const:49eb40:8", "const:4:8"]]
- 0049eb40 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0049eb80 ["INT_ADD", "register:40f0:8", ["const:49eb80:8", "const:4:8"]]
+ 0049eb80 ["CALL", null, ["callee:00c57ef0:8"]]
- 0049eb40 bytes ece31e94
+ 0049eb80 bytes dce41e94
- 0049eb48 ["COPY", "tmp:0:8", ["const:a24:8"]]
- 0049eb48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049eb48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049eb48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049eb88 ["COPY", "tmp:0:8", ["const:af1:8"]]
+ 0049eb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049eb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049eb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049eb48 bytes 08912891
+ 0049eb88 bytes 08c52b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a74afe82c4efc4de6101c4368ab6e6c4"></a>

### [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) → [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) FUN_0049f3f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 66件 [`0049bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049b/0049bfe4.md) [`005b068c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b0/005b068c.md) [`005dd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005dd710.md) [`005e2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2e00.md) [`005e74c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e74c4.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 66件 [`0049c024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c024.md) [`005b06cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b06cc.md) [`005dd750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dd/005dd750.md) [`005e2e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e2/005e2e40.md) [`005e7504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7504.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0049f3fc",
      "incomplete_value": false,
      "site": "0049f400",
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
    "old": {
      "definition_site": "0049f3bc",
      "incomplete_value": false,
      "site": "0049f3c0",
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
            "const:f0c:8"
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
      "0049f3fc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049f3fc",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md#insn-0049f3c0) · [`0049f3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md#insn-0049f3bc)
- 新版 [`0049f400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md#insn-0049f400) · [`0049f3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md#insn-0049f3fc)

~~~diff
- 0049f3c0 ["INT_ADD", "register:40f0:8", ["const:49f3c0:8", "const:4:8"]]
- 0049f3c0 ["CALL", null, ["callee:00442930:8"]]
+ 0049f400 ["INT_ADD", "register:40f0:8", ["const:49f400:8", "const:4:8"]]
+ 0049f400 ["CALL", null, ["callee:00442930:8"]]
- 0049f3c0 bytes 4c8dfe97
+ 0049f400 bytes 4c8dfe97
- 0049f3bc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f3bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f3fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f3fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f3fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f3bc bytes 00303c91
+ 0049f3fc bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f58d03dda8fbca6e063f65ebcba44fe"></a>

### [`0049f3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md) → [`0049f404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md) FUN_0049f404

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 5件 [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049d100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md) [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`0049dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md) [`0049df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0049f410",
      "incomplete_value": false,
      "site": "0049f414",
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
    "old": {
      "definition_site": "0049f3d0",
      "incomplete_value": false,
      "site": "0049f3d4",
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
            "const:f0c:8"
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
      "0049f410",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049f410",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md#insn-0049f3d4) · [`0049f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3c4.md#insn-0049f3d0)
- 新版 [`0049f414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md#insn-0049f414) · [`0049f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f404.md#insn-0049f410)

~~~diff
- 0049f3d4 ["INT_ADD", "register:40f0:8", ["const:49f3d4:8", "const:4:8"]]
- 0049f3d4 ["CALL", null, ["callee:00442930:8"]]
+ 0049f414 ["INT_ADD", "register:40f0:8", ["const:49f414:8", "const:4:8"]]
+ 0049f414 ["CALL", null, ["callee:00442930:8"]]
- 0049f3d4 bytes 478dfe97
+ 0049f414 bytes 478dfe97
- 0049f3d0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f3d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f410 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f3d0 bytes 00303c91
+ 0049f410 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa340fd936e5df5bd5fa81f0f9c0e8ec"></a>

### [`0049f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md) → [`0049f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md) FUN_0049f418

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`0049ca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049c/0049ca9c.md) [`0049d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d0c0.md) [`0049d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049d158.md) [`0049dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049dc94.md) [`0049df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049d/0049df00.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 5件 [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049d100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d100.md) [`0049d198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049d198.md) [`0049dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049dcd4.md) [`0049df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049df40.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0049f424",
      "incomplete_value": false,
      "site": "0049f428",
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
    "old": {
      "definition_site": "0049f3e4",
      "incomplete_value": false,
      "site": "0049f3e8",
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
            "const:f0c:8"
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
      "0049f424",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0049f424",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049f3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md#insn-0049f3e8) · [`0049f3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3d8.md#insn-0049f3e4)
- 新版 [`0049f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md#insn-0049f428) · [`0049f424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f418.md#insn-0049f424)

~~~diff
- 0049f3e8 ["INT_ADD", "register:40f0:8", ["const:49f3e8:8", "const:4:8"]]
- 0049f3e8 ["CALL", null, ["callee:00442930:8"]]
+ 0049f428 ["INT_ADD", "register:40f0:8", ["const:49f428:8", "const:4:8"]]
+ 0049f428 ["CALL", null, ["callee:00442930:8"]]
- 0049f3e8 bytes 428dfe97
+ 0049f428 bytes 428dfe97
- 0049f3e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0049f3e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f3e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f424 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f424 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f424 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f424 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f3e4 bytes 00303c91
+ 0049f424 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

