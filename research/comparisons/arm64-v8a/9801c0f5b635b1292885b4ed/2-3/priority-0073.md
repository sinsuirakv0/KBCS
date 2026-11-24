# v16.0.1 → v16.0.2 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-f7c6a06f55faa38fc5b994fdcff12a88"></a>

### [`00b4ad84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md) → [`00b4ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae20.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4ada0",
      "incomplete_value": false,
      "site": "00b4ada4",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4adb0",
      "incomplete_value": true,
      "site": "00b4adbc",
      "value": [
        "LOAD",
        "8",
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
      "00b4ae3c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4ae4c",
      "DATA",
      [
        "storage",
        "01125af8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ae3c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4ae4c",
      "DATA",
      [
        "storage",
        "01125bf8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4ada4) · [`00b4ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4ada0) · [`00b4adac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4adac)
- 新版 `00b4ae40`（命令位置の公開資料なし） · `00b4ae3c`（命令位置の公開資料なし） · `00b4ae48`（命令位置の公開資料なし）

~~~diff
- 00b4ada4 ["INT_ADD", "register:40f0:8", ["const:b4ada4:8", "const:4:8"]]
- 00b4ada4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4ae40 ["INT_ADD", "register:40f0:8", ["const:b4ae40:8", "const:4:8"]]
+ 00b4ae40 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4ada4 bytes 97400494
+ 00b4ae40 bytes a4400494
- 00b4ada0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4ada0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ada0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ada0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4ae3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ada0 bytes 009c0d91
+ 00b4ae3c bytes 002c0c91
- 00b4adac ["COPY", "tmp:0:8", ["const:af8:8"]]
- 00b4adac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4adac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4adac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00b4ae48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4adac bytes 08e12b91
+ 00b4ae48 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72619e48889fdc18a352bf0680093074"></a>

### [`00b4adc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md) → [`00b4ae5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae5c.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4ae00",
      "incomplete_value": true,
      "site": "00b4ae00",
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
            "const:ae8:8"
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
    "old": {
      "definition_site": "00b4addc",
      "incomplete_value": true,
      "site": "00b4addc",
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
    "old": {
      "definition_site": "00b4ade4",
      "incomplete_value": false,
      "site": "00b4adf8",
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
            "const:580:8"
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
      "00b4ae70",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae80",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ae9c",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae70",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae80",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4ae9c",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4adf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4adf8) · [`00b4ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4ae00) · [`00b4add4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4add4)
- 新版 `00b4ae94`（命令位置の公開資料なし） · `00b4ae9c`（命令位置の公開資料なし） · `00b4ae70`（命令位置の公開資料なし）

~~~diff
- 00b4adf8 ["INT_ADD", "register:40f0:8", ["const:b4adf8:8", "const:4:8"]]
- 00b4adf8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ae94 ["INT_ADD", "register:40f0:8", ["const:b4ae94:8", "const:4:8"]]
+ 00b4ae94 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4adf8 bytes 46400494
+ 00b4ae94 bytes 53400494
- 00b4ae00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b4ae00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00b4ae9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae00 bytes 807605f9
+ 00b4ae9c bytes 80f605f9
- 00b4add4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b4add4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ae70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00b4ae70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4add4 bytes 817645f9
+ 00b4ae70 bytes 81f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c7bc51f24c7e020e58b584f626d734b"></a>

### [`00b4ae6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae6c.md) → [`00b4af08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af08.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ae98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4af34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00b4ae80",
      "incomplete_value": true,
      "site": "00b4ae80",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4af18",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4ae8c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ae90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b4af18",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af28",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4af2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae6c.md#insn-00b4ae90) · [`00b4ae98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae6c.md#insn-00b4ae98)
- 新版 `00b4af2c`（命令位置の公開資料なし）

~~~diff
- 00b4ae90 ["INT_ADD", "register:40f0:8", ["const:b4ae90:8", "const:4:8"]]
- 00b4ae90 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ae90 bytes 20400494
- 00b4ae98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b4ae98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae98 bytes 608a05f9
+ 00b4af2c ["INT_ADD", "register:40f0:8", ["const:b4af2c:8", "const:4:8"]]
+ 00b4af2c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4af2c bytes 2d400494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aed6bc6e5ee5f05ff034d893db2ce82"></a>

### [`00b4aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md) → [`00b4af48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aeb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aeb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aeac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aeb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4af58",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4af4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4af58",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md#insn-00b4aeac) · [`00b4aeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md#insn-00b4aeb0) · [`00b4aec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md#insn-00b4aec0)
- 新版 `00b4af5c`（命令位置の公開資料なし）

~~~diff
- 00b4aeac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4aeac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4aeac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4aeac bytes f30f1ef8
- 00b4aeb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aeb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aeb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aeb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aeb0 bytes fd7b01a9
- 00b4aec0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aec0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4af5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4af5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4aec0 bytes e80000b5
+ 00b4af5c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-289bfcc7295e8400aa749d362c6ebbbf"></a>

### [`00b4aeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md) → [`00b4af88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af88.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4af1c",
      "incomplete_value": true,
      "site": "00b4af1c",
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
            "const:b10:8"
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
    "old": {
      "definition_site": "00b4af00",
      "incomplete_value": true,
      "site": "00b4af00",
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
    "old": {
      "definition_site": "00b4af0c",
      "incomplete_value": false,
      "site": "00b4af14",
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
            "const:7e6:8"
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
      "00b4af98",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afa8",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4afb8",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af98",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afa8",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4afb8",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4af14) · [`00b4af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4af1c) · [`00b4aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4aefc)
- 新版 `00b4afb0`（命令位置の公開資料なし） · `00b4afb8`（命令位置の公開資料なし） · `00b4af98`（命令位置の公開資料なし）

~~~diff
- 00b4af14 ["INT_ADD", "register:40f0:8", ["const:b4af14:8", "const:4:8"]]
- 00b4af14 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4afb0 ["INT_ADD", "register:40f0:8", ["const:b4afb0:8", "const:4:8"]]
+ 00b4afb0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4af14 bytes ff3f0494
+ 00b4afb0 bytes 0c400494
- 00b4af1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b4af1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4afb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4afb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4af1c bytes 608a05f9
+ 00b4afb8 bytes 600a06f9
- 00b4aefc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b4aefc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4af98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4af98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aefc bytes 688a45f9
+ 00b4af98 bytes 680a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8914ec4984fa90cef4a733f4df96556b"></a>

### [`00b4af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md) → [`00b4afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4afcc.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4af60",
      "incomplete_value": true,
      "site": "00b4af60",
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
            "const:b10:8"
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
    "old": {
      "definition_site": "00b4af44",
      "incomplete_value": true,
      "site": "00b4af44",
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
    "old": {
      "definition_site": "00b4af4c",
      "incomplete_value": false,
      "site": "00b4af58",
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
            "const:7e6:8"
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
      "00b4afdc",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afe8",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4affc",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4afdc",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afe8",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4affc",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af58) · [`00b4af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af60) · [`00b4af40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af40)
- 新版 `00b4aff4`（命令位置の公開資料なし） · `00b4affc`（命令位置の公開資料なし） · `00b4afdc`（命令位置の公開資料なし）

~~~diff
- 00b4af58 ["INT_ADD", "register:40f0:8", ["const:b4af58:8", "const:4:8"]]
- 00b4af58 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4aff4 ["INT_ADD", "register:40f0:8", ["const:b4aff4:8", "const:4:8"]]
+ 00b4aff4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4af58 bytes ee3f0494
+ 00b4aff4 bytes fb3f0494
- 00b4af60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b4af60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4affc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4affc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4af60 bytes 608a05f9
+ 00b4affc bytes 600a06f9
- 00b4af40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b4af40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4afdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4afdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4af40 bytes 688a45f9
+ 00b4afdc bytes 680a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82475538d83e42146532c1e3381205c0"></a>

### [`00b4af80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md) → [`00b4b01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b01c.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4b008",
      "incomplete_value": true,
      "site": "00b4b008",
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
            "const:b18:8"
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
    "old": {
      "definition_site": "00b4afb4",
      "incomplete_value": true,
      "site": "00b4afc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
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
      "00b4b030",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b050",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0a4",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b030",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b050",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0a4",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4afc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4afc0) · [`00b4b008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4b008) · [`00b4af94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4af94)
- 新版 `00b4b05c`（命令位置の公開資料なし） · `00b4b0a4`（命令位置の公開資料なし） · `00b4b030`（命令位置の公開資料なし）

~~~diff
- 00b4afc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4afc0 ["INT_ADD", "register:40f0:8", ["const:b4afc0:8", "const:4:8"]]
- 00b4afc0 ["CALLIND", null, ["register:0:8"]]
+ 00b4b05c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b05c ["INT_ADD", "register:40f0:8", ["const:b4b05c:8", "const:4:8"]]
+ 00b4b05c ["CALLIND", null, ["register:0:8"]]
- 00b4afc0 bytes 00013fd6
+ 00b4b05c bytes 00013fd6
- 00b4b008 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b008 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b18:8"]]
- 00b4b008 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b0a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b0a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4b0a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b008 bytes a0622c39
+ 00b4b0a4 bytes a0623039
- 00b4af94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b18:8"]]
- 00b4af94 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4af94 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4b030 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4b030 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b030 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4af94 bytes a8626c39
+ 00b4b030 bytes a8627039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d636444c6628f938025a4db17161913"></a>

### [`00b4b01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md) → [`00b4b0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b0b8.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4b058",
      "incomplete_value": true,
      "site": "00b4b058",
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
            "const:b18:8"
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
    "old": {
      "definition_site": "00b4b0a8",
      "incomplete_value": true,
      "site": "00b4b0a8",
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
            "const:b10:8"
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
    "old": {
      "definition_site": "00b4b034",
      "incomplete_value": true,
      "site": "00b4b034",
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
      "00b4b0cc",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0d8",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b0f4",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0cc",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0d8",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b0f4",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md#insn-00b4b058) · [`00b4b0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md#insn-00b4b0a4) · [`00b4b0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md#insn-00b4b0a8)
- 新版 `00b4b0f4`（命令位置の公開資料なし） · `00b4b140`（命令位置の公開資料なし） · `00b4b144`（命令位置の公開資料なし）

~~~diff
- 00b4b058 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b058 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b058 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b18:8"]]
- 00b4b058 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b0f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b0f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b0f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4b0f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b058 bytes bf622c39
+ 00b4b0f4 bytes bf623039
- 00b4b0a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b0a4 ["INT_ADD", "register:40f0:8", ["const:b4b0a4:8", "const:4:8"]]
- 00b4b0a4 ["CALLIND", null, ["register:0:8"]]
+ 00b4b140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b140 ["INT_ADD", "register:40f0:8", ["const:b4b140:8", "const:4:8"]]
+ 00b4b140 ["CALLIND", null, ["register:0:8"]]
- 00b4b0a4 bytes 00013fd6
+ 00b4b140 bytes 00013fd6
- 00b4b0a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b4b0a8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b0a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4b144 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b0a8 bytes 9f8a05f9
+ 00b4b144 bytes 9f0a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20efb959c5d2b8d38a55cefe563869e8"></a>

### [`00b4b0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md) → [`00b4b158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b158.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4b0fc",
      "incomplete_value": true,
      "site": "00b4b0fc",
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
            "const:b10:8"
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
    "old": {
      "definition_site": "00b4b0d8",
      "incomplete_value": true,
      "site": "00b4b0d8",
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
    "old": {
      "definition_site": "00b4b0e0",
      "incomplete_value": false,
      "site": "00b4b0f4",
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
            "const:7e6:8"
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
      "00b4b16c",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b17c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4b198",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b16c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b17c",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4b198",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md#insn-00b4b0f4) · [`00b4b0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md#insn-00b4b0fc) · [`00b4b0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md#insn-00b4b0d0)
- 新版 `00b4b190`（命令位置の公開資料なし） · `00b4b198`（命令位置の公開資料なし） · `00b4b16c`（命令位置の公開資料なし）

~~~diff
- 00b4b0f4 ["INT_ADD", "register:40f0:8", ["const:b4b0f4:8", "const:4:8"]]
- 00b4b0f4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b190 ["INT_ADD", "register:40f0:8", ["const:b4b190:8", "const:4:8"]]
+ 00b4b190 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b0f4 bytes 873f0494
+ 00b4b190 bytes 943f0494
- 00b4b0fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b4b0fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4b198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b0fc bytes 808a05f9
+ 00b4b198 bytes 800a06f9
- 00b4b0d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b4b0d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b16c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4b16c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b0d0 bytes 818a45f9
+ 00b4b16c bytes 810a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60287f7127b8f1216e3cb52b2cfd3224"></a>

### [`00b4b12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md) → [`00b4b1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b1c8.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afb0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b080.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b148",
      "incomplete_value": false,
      "site": "00b4b14c",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4b158",
      "incomplete_value": true,
      "site": "00b4b164",
      "value": [
        "LOAD",
        "8",
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
      "00b4b1e4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b1f4",
      "DATA",
      [
        "storage",
        "01125b20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1e4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4b1f4",
      "DATA",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b14c) · [`00b4b148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b148) · [`00b4b154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b154)
- 新版 `00b4b1e8`（命令位置の公開資料なし） · `00b4b1e4`（命令位置の公開資料なし） · `00b4b1f0`（命令位置の公開資料なし）

~~~diff
- 00b4b14c ["INT_ADD", "register:40f0:8", ["const:b4b14c:8", "const:4:8"]]
- 00b4b14c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b1e8 ["INT_ADD", "register:40f0:8", ["const:b4b1e8:8", "const:4:8"]]
+ 00b4b1e8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b14c bytes ad3f0494
+ 00b4b1e8 bytes ba3f0494
- 00b4b148 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4b148 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b148 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1e4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4b1e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b148 bytes 009c0d91
+ 00b4b1e4 bytes 002c0c91
- 00b4b154 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00b4b154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b1f0 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00b4b1f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b1f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b1f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b154 bytes 08812c91
+ 00b4b1f0 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0039fb28b98a759e50613bbf65210092"></a>

### [`00b4b168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md) → [`00b4b204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b204.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b1a8",
      "incomplete_value": true,
      "site": "00b4b1a8",
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
            "const:b10:8"
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
    "old": {
      "definition_site": "00b4b184",
      "incomplete_value": true,
      "site": "00b4b184",
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
    "old": {
      "definition_site": "00b4b18c",
      "incomplete_value": false,
      "site": "00b4b1a0",
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
            "const:7e6:8"
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
      "00b4b218",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b228",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4b244",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b218",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b228",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4b244",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b1a0) · [`00b4b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b1a8) · [`00b4b17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b17c)
- 新版 `00b4b23c`（命令位置の公開資料なし） · `00b4b244`（命令位置の公開資料なし） · `00b4b218`（命令位置の公開資料なし）

~~~diff
- 00b4b1a0 ["INT_ADD", "register:40f0:8", ["const:b4b1a0:8", "const:4:8"]]
- 00b4b1a0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b23c ["INT_ADD", "register:40f0:8", ["const:b4b23c:8", "const:4:8"]]
+ 00b4b23c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b1a0 bytes 5c3f0494
+ 00b4b23c bytes 693f0494
- 00b4b1a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b4b1a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4b244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b1a8 bytes 808a05f9
+ 00b4b244 bytes 800a06f9
- 00b4b17c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b4b17c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4b218 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b17c bytes 818a45f9
+ 00b4b218 bytes 810a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93dd72109cb8e48ad75ebd36a65cb3da"></a>

### [`00b4b1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md) → [`00b4b274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b274.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b1f4",
      "incomplete_value": false,
      "site": "00b4b1f8",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4b204",
      "incomplete_value": true,
      "site": "00b4b210",
      "value": [
        "LOAD",
        "8",
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
      "00b4b290",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b2a0",
      "DATA",
      [
        "storage",
        "01125b28",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b290",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b2a0",
      "DATA",
      [
        "storage",
        "01125c28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b1f8) · [`00b4b1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b1f4) · [`00b4b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b200)
- 新版 `00b4b294`（命令位置の公開資料なし） · `00b4b290`（命令位置の公開資料なし） · `00b4b29c`（命令位置の公開資料なし）

~~~diff
- 00b4b1f8 ["INT_ADD", "register:40f0:8", ["const:b4b1f8:8", "const:4:8"]]
- 00b4b1f8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b294 ["INT_ADD", "register:40f0:8", ["const:b4b294:8", "const:4:8"]]
+ 00b4b294 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b1f8 bytes 823f0494
+ 00b4b294 bytes 8f3f0494
- 00b4b1f4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4b1f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b1f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b1f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b290 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4b290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b1f4 bytes 00781491
+ 00b4b290 bytes 00341591
- 00b4b200 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00b4b200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b29c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00b4b29c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b29c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b29c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b200 bytes 08a12c91
+ 00b4b29c bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4230b9c73358a192fe65edb3206c1f58"></a>

### [`00b4b214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md) → [`00b4b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2b0.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b240",
      "incomplete_value": true,
      "site": "00b4b240",
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
            "const:b30:8"
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
    "old": {
      "definition_site": "00b4b228",
      "incomplete_value": true,
      "site": "00b4b228",
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
    "old": {
      "definition_site": "00b4b234",
      "incomplete_value": false,
      "site": "00b4b238",
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
            "const:432:8"
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
      "00b4b2c0",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2d0",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b2dc",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2c0",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2d0",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4b2dc",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b238) · [`00b4b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b240) · [`00b4b224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b224)
- 新版 `00b4b2d4`（命令位置の公開資料なし） · `00b4b2dc`（命令位置の公開資料なし） · `00b4b2c0`（命令位置の公開資料なし）

~~~diff
- 00b4b238 ["INT_ADD", "register:40f0:8", ["const:b4b238:8", "const:4:8"]]
- 00b4b238 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b2d4 ["INT_ADD", "register:40f0:8", ["const:b4b2d4:8", "const:4:8"]]
+ 00b4b2d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b238 bytes 363f0494
+ 00b4b2d4 bytes 433f0494
- 00b4b240 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
- 00b4b240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00b4b2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b240 bytes 609a05f9
+ 00b4b2dc bytes 601a06f9
- 00b4b224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
- 00b4b224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00b4b2c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b224 bytes 689a45f9
+ 00b4b2c0 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f361376ef4e8e9d85d0b9c30c47a15c"></a>

### [`00b4b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md) → [`00b4b2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2f0.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b280",
      "incomplete_value": true,
      "site": "00b4b280",
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
            "const:b30:8"
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
    "old": {
      "definition_site": "00b4b268",
      "incomplete_value": true,
      "site": "00b4b268",
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
    "old": {
      "definition_site": "00b4b270",
      "incomplete_value": false,
      "site": "00b4b278",
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
            "const:432:8"
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
      "00b4b300",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b30c",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b31c",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b300",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b30c",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4b31c",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b278) · [`00b4b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b280) · [`00b4b264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b264)
- 新版 `00b4b314`（命令位置の公開資料なし） · `00b4b31c`（命令位置の公開資料なし） · `00b4b300`（命令位置の公開資料なし）

~~~diff
- 00b4b278 ["INT_ADD", "register:40f0:8", ["const:b4b278:8", "const:4:8"]]
- 00b4b278 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b314 ["INT_ADD", "register:40f0:8", ["const:b4b314:8", "const:4:8"]]
+ 00b4b314 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b278 bytes 263f0494
+ 00b4b314 bytes 333f0494
- 00b4b280 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
- 00b4b280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00b4b31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b280 bytes 609a05f9
+ 00b4b31c bytes 601a06f9
- 00b4b264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
- 00b4b264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
+ 00b4b300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b264 bytes 689a45f9
+ 00b4b300 bytes 681a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d57b100ddc5ad8c7fb86dc9c45b32215"></a>

### [`00b4b2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md) → [`00b4b374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b374.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b384",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b374",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b378",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b384",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md#insn-00b4b2d8) · [`00b4b2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md#insn-00b4b2dc) · [`00b4b2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md#insn-00b4b2ec)
- 新版 `00b4b388`（命令位置の公開資料なし）

~~~diff
- 00b4b2d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4b2d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4b2d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4b2d8 bytes f30f1ef8
- 00b4b2dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b2dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b2dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4b2dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b2dc bytes fd7b01a9
- 00b4b2ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b2ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4b388 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4b388 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4b2ec bytes 080100b5
+ 00b4b388 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-019aec35a7cbeb36b16ac0c4dc0471c7"></a>

### [`00b4b328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md) → [`00b4b3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b3c4.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00b4b3b0",
      "incomplete_value": true,
      "site": "00b4b3b0",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b368"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b37c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b33c",
      "READ",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4b35c",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b44c",
      "WRITE",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3d8",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b3f8",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b44c",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md#insn-00b4b368) · [`00b4b37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md#insn-00b4b37c) · [`00b4b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md#insn-00b4b3b0)
- 新版 `00b4b44c`（命令位置の公開資料なし）

~~~diff
- 00b4b368 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b368 ["INT_ADD", "register:40f0:8", ["const:b4b368:8", "const:4:8"]]
- 00b4b368 ["CALLIND", null, ["register:0:8"]]
- 00b4b368 bytes 00013fd6
- 00b4b37c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b37c ["INT_ADD", "register:40f0:8", ["const:b4b37c:8", "const:4:8"]]
- 00b4b37c ["CALLIND", null, ["register:0:8"]]
- 00b4b37c bytes 00013fd6
- 00b4b3b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b3b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b38:8"]]
- 00b4b3b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b44c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b44c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c38:8"]]
+ 00b4b44c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b3b0 bytes a0e22c39
+ 00b4b44c bytes a0e23039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283a862f987ba1417074689276321019"></a>

### [`00b4b3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md) → [`00b4b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b460.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4b400",
      "incomplete_value": true,
      "site": "00b4b400",
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
            "const:b38:8"
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
    "old": {
      "definition_site": "00b4b450",
      "incomplete_value": true,
      "site": "00b4b450",
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
            "const:b30:8"
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
    "old": {
      "definition_site": "00b4b3dc",
      "incomplete_value": true,
      "site": "00b4b3dc",
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
      "00b4b474",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b480",
      "READ",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b49c",
      "WRITE",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b474",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b480",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b49c",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b400) · [`00b4b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b44c) · [`00b4b450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b450)
- 新版 `00b4b49c`（命令位置の公開資料なし） · `00b4b4e8`（命令位置の公開資料なし） · `00b4b4ec`（命令位置の公開資料なし）

~~~diff
- 00b4b400 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b400 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b400 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b38:8"]]
- 00b4b400 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b49c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b49c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b49c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c38:8"]]
+ 00b4b49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b400 bytes bfe22c39
+ 00b4b49c bytes bfe23039
- 00b4b44c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b44c ["INT_ADD", "register:40f0:8", ["const:b4b44c:8", "const:4:8"]]
- 00b4b44c ["CALLIND", null, ["register:0:8"]]
+ 00b4b4e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b4e8 ["INT_ADD", "register:40f0:8", ["const:b4b4e8:8", "const:4:8"]]
+ 00b4b4e8 ["CALLIND", null, ["register:0:8"]]
- 00b4b44c bytes 00013fd6
+ 00b4b4e8 bytes 00013fd6
- 00b4b450 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
- 00b4b450 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b4ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00b4b4ec ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b4ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b450 bytes 9f9a05f9
+ 00b4b4ec bytes 9f1a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ceb7c582118001a7b06ad516d1ba60a"></a>

### [`00b4b464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md) → [`00b4b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b500.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4b4a4",
      "incomplete_value": true,
      "site": "00b4b4a4",
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
            "const:b30:8"
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
    "old": {
      "definition_site": "00b4b480",
      "incomplete_value": true,
      "site": "00b4b480",
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
    "old": {
      "definition_site": "00b4b488",
      "incomplete_value": false,
      "site": "00b4b49c",
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
            "const:432:8"
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
      "00b4b514",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b524",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b540",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b514",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b524",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4b540",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b49c) · [`00b4b4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b4a4) · [`00b4b478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b478)
- 新版 `00b4b538`（命令位置の公開資料なし） · `00b4b540`（命令位置の公開資料なし） · `00b4b514`（命令位置の公開資料なし）

~~~diff
- 00b4b49c ["INT_ADD", "register:40f0:8", ["const:b4b49c:8", "const:4:8"]]
- 00b4b49c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b538 ["INT_ADD", "register:40f0:8", ["const:b4b538:8", "const:4:8"]]
+ 00b4b538 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b49c bytes 9d3e0494
+ 00b4b538 bytes aa3e0494
- 00b4b4a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
- 00b4b4a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b540 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00b4b540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b4a4 bytes 809a05f9
+ 00b4b540 bytes 801a06f9
- 00b4b478 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
- 00b4b478 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b514 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00b4b514 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b478 bytes 819a45f9
+ 00b4b514 bytes 811a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a9543a7c23f6adc965d6b08b037253"></a>

### [`00b4b4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md) → [`00b4b570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b570.md) _ZN8firebase4util13integer_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b4f0",
      "incomplete_value": false,
      "site": "00b4b4f4",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4b500",
      "incomplete_value": true,
      "site": "00b4b50c",
      "value": [
        "LOAD",
        "8",
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
      "00b4b58c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b59c",
      "DATA",
      [
        "storage",
        "01125b40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b58c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4b59c",
      "DATA",
      [
        "storage",
        "01125c40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md#insn-00b4b4f4) · [`00b4b4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md#insn-00b4b4f0) · [`00b4b4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md#insn-00b4b4fc)
- 新版 `00b4b590`（命令位置の公開資料なし） · `00b4b58c`（命令位置の公開資料なし） · `00b4b598`（命令位置の公開資料なし）

~~~diff
- 00b4b4f4 ["INT_ADD", "register:40f0:8", ["const:b4b4f4:8", "const:4:8"]]
- 00b4b4f4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b590 ["INT_ADD", "register:40f0:8", ["const:b4b590:8", "const:4:8"]]
+ 00b4b590 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b4f4 bytes c33e0494
+ 00b4b590 bytes d03e0494
- 00b4b4f0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4b4f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b4f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b4f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b58c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4b58c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b58c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b58c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b4f0 bytes 009c0d91
+ 00b4b58c bytes 002c0c91
- 00b4b4fc ["COPY", "tmp:0:8", ["const:b40:8"]]
- 00b4b4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b598 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00b4b598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b4fc bytes 08012d91
+ 00b4b598 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd95afc580c0bce9ed073dfbe489c242"></a>

### [`00b4b510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md) → [`00b4b5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b5ac.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b550",
      "incomplete_value": true,
      "site": "00b4b550",
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
            "const:b30:8"
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
    "old": {
      "definition_site": "00b4b52c",
      "incomplete_value": true,
      "site": "00b4b52c",
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
    "old": {
      "definition_site": "00b4b534",
      "incomplete_value": false,
      "site": "00b4b548",
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
            "const:432:8"
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
      "00b4b5c0",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5d0",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b5ec",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5c0",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5d0",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4b5ec",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b548) · [`00b4b550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b550) · [`00b4b524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b524)
- 新版 `00b4b5e4`（命令位置の公開資料なし） · `00b4b5ec`（命令位置の公開資料なし） · `00b4b5c0`（命令位置の公開資料なし）

~~~diff
- 00b4b548 ["INT_ADD", "register:40f0:8", ["const:b4b548:8", "const:4:8"]]
- 00b4b548 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b5e4 ["INT_ADD", "register:40f0:8", ["const:b4b5e4:8", "const:4:8"]]
+ 00b4b5e4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b548 bytes 723e0494
+ 00b4b5e4 bytes 7f3e0494
- 00b4b550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
- 00b4b550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00b4b5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b550 bytes 809a05f9
+ 00b4b5ec bytes 801a06f9
- 00b4b524 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
- 00b4b524 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b5c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00b4b5c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b524 bytes 819a45f9
+ 00b4b5c0 bytes 811a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd0a48f8b75838dbbfa74316391e1995"></a>

### [`00b4b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md) → [`00b4b61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b61c.md) _ZN8firebase4util13integer_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b59c",
      "incomplete_value": false,
      "site": "00b4b5a0",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4b5ac",
      "incomplete_value": true,
      "site": "00b4b5b8",
      "value": [
        "LOAD",
        "8",
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
      "00b4b638",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b648",
      "DATA",
      [
        "storage",
        "01125b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b638",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b648",
      "DATA",
      [
        "storage",
        "01125c50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md#insn-00b4b5a0) · [`00b4b59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md#insn-00b4b59c) · [`00b4b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md#insn-00b4b5a8)
- 新版 `00b4b63c`（命令位置の公開資料なし） · `00b4b638`（命令位置の公開資料なし） · `00b4b644`（命令位置の公開資料なし）

~~~diff
- 00b4b5a0 ["INT_ADD", "register:40f0:8", ["const:b4b5a0:8", "const:4:8"]]
- 00b4b5a0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b63c ["INT_ADD", "register:40f0:8", ["const:b4b63c:8", "const:4:8"]]
+ 00b4b63c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b5a0 bytes 983e0494
+ 00b4b63c bytes a53e0494
- 00b4b59c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4b59c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b59c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b59c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b638 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4b638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b59c bytes 00781491
+ 00b4b638 bytes 00341591
- 00b4b5a8 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00b4b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b644 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00b4b644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b5a8 bytes 08412d91
+ 00b4b644 bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2280235472840f4c553a564542f18c9f"></a>

### [`00b4b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md) → [`00b4b658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b658.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b5e8",
      "incomplete_value": true,
      "site": "00b4b5e8",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b5d0",
      "incomplete_value": true,
      "site": "00b4b5d0",
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
    "old": {
      "definition_site": "00b4b5dc",
      "incomplete_value": false,
      "site": "00b4b5e0",
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
            "const:a31:8"
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
      "00b4b668",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b678",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b684",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b668",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b678",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b684",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5e0) · [`00b4b5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5e8) · [`00b4b5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5cc)
- 新版 `00b4b67c`（命令位置の公開資料なし） · `00b4b684`（命令位置の公開資料なし） · `00b4b668`（命令位置の公開資料なし）

~~~diff
- 00b4b5e0 ["INT_ADD", "register:40f0:8", ["const:b4b5e0:8", "const:4:8"]]
- 00b4b5e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b67c ["INT_ADD", "register:40f0:8", ["const:b4b67c:8", "const:4:8"]]
+ 00b4b67c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b5e0 bytes 4c3e0494
+ 00b4b67c bytes 593e0494
- 00b4b5e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b5e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b5e8 bytes 60ae05f9
+ 00b4b684 bytes 602e06f9
- 00b4b5cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b5cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b668 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b668 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b5cc bytes 68ae45f9
+ 00b4b668 bytes 682e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8577c95d117be30fce388bef3ae695b8"></a>

### [`00b4b5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md) → [`00b4b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b698.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b628",
      "incomplete_value": true,
      "site": "00b4b628",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b610",
      "incomplete_value": true,
      "site": "00b4b610",
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
    "old": {
      "definition_site": "00b4b618",
      "incomplete_value": false,
      "site": "00b4b620",
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
            "const:a31:8"
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
      "00b4b6a8",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6b4",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b6c4",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b6a8",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6b4",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b6c4",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b620) · [`00b4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b628) · [`00b4b60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b60c)
- 新版 `00b4b6bc`（命令位置の公開資料なし） · `00b4b6c4`（命令位置の公開資料なし） · `00b4b6a8`（命令位置の公開資料なし）

~~~diff
- 00b4b620 ["INT_ADD", "register:40f0:8", ["const:b4b620:8", "const:4:8"]]
- 00b4b620 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b6bc ["INT_ADD", "register:40f0:8", ["const:b4b6bc:8", "const:4:8"]]
+ 00b4b6bc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b620 bytes 3c3e0494
+ 00b4b6bc bytes 493e0494
- 00b4b628 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b6c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b6c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b628 bytes 60ae05f9
+ 00b4b6c4 bytes 602e06f9
- 00b4b60c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b60c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b6a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b6a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b60c bytes 68ae45f9
+ 00b4b6a8 bytes 682e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd5c91c9fbcdbef29f6cbc633c6fd3c"></a>

### [`00b4b63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md) → [`00b4b6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b6d8.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b66c",
      "incomplete_value": true,
      "site": "00b4b66c",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b650",
      "incomplete_value": true,
      "site": "00b4b650",
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
    "old": {
      "definition_site": "00b4b65c",
      "incomplete_value": false,
      "site": "00b4b664",
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
            "const:a31:8"
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
      "00b4b6e8",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6f8",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b708",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b6e8",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6f8",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b708",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b664) · [`00b4b66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b66c) · [`00b4b64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b64c)
- 新版 `00b4b700`（命令位置の公開資料なし） · `00b4b708`（命令位置の公開資料なし） · `00b4b6e8`（命令位置の公開資料なし）

~~~diff
- 00b4b664 ["INT_ADD", "register:40f0:8", ["const:b4b664:8", "const:4:8"]]
- 00b4b664 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b700 ["INT_ADD", "register:40f0:8", ["const:b4b700:8", "const:4:8"]]
+ 00b4b700 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b664 bytes 2b3e0494
+ 00b4b700 bytes 383e0494
- 00b4b66c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b66c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b66c bytes 60ae05f9
+ 00b4b708 bytes 602e06f9
- 00b4b64c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b64c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b6e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b64c bytes 68ae45f9
+ 00b4b6e8 bytes 682e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b539a258dc5b0bc4d1592cb2e0d9fdb4"></a>

### [`00b4b680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md) → [`00b4b71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b71c.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b6b0",
      "incomplete_value": true,
      "site": "00b4b6b0",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b694",
      "incomplete_value": true,
      "site": "00b4b694",
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
    "old": {
      "definition_site": "00b4b69c",
      "incomplete_value": false,
      "site": "00b4b6a8",
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
            "const:a31:8"
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
      "00b4b72c",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b738",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b74c",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b72c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b738",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b74c",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b6a8) · [`00b4b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b6b0) · [`00b4b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b690)
- 新版 `00b4b744`（命令位置の公開資料なし） · `00b4b74c`（命令位置の公開資料なし） · `00b4b72c`（命令位置の公開資料なし）

~~~diff
- 00b4b6a8 ["INT_ADD", "register:40f0:8", ["const:b4b6a8:8", "const:4:8"]]
- 00b4b6a8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b744 ["INT_ADD", "register:40f0:8", ["const:b4b744:8", "const:4:8"]]
+ 00b4b744 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b6a8 bytes 1a3e0494
+ 00b4b744 bytes 273e0494
- 00b4b6b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b6b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b6b0 bytes 60ae05f9
+ 00b4b74c bytes 602e06f9
- 00b4b690 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00b4b690 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b72c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4b72c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b690 bytes 68ae45f9
+ 00b4b72c bytes 682e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7618bfd115a05c5280491dda3800ec"></a>

### [`00b4b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md) → [`00b4b76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b76c.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4b758",
      "incomplete_value": true,
      "site": "00b4b758",
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
            "const:b60:8"
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
    "old": {
      "definition_site": "00b4b704",
      "incomplete_value": true,
      "site": "00b4b710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
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
      "00b4b780",
      "READ",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b7a0",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7f4",
      "WRITE",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b780",
      "READ",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b7a0",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7f4",
      "WRITE",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b710) · [`00b4b758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b758) · [`00b4b6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b6e4)
- 新版 `00b4b7ac`（命令位置の公開資料なし） · `00b4b7f4`（命令位置の公開資料なし） · `00b4b780`（命令位置の公開資料なし）

~~~diff
- 00b4b710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b710 ["INT_ADD", "register:40f0:8", ["const:b4b710:8", "const:4:8"]]
- 00b4b710 ["CALLIND", null, ["register:0:8"]]
+ 00b4b7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b7ac ["INT_ADD", "register:40f0:8", ["const:b4b7ac:8", "const:4:8"]]
+ 00b4b7ac ["CALLIND", null, ["register:0:8"]]
- 00b4b710 bytes 00013fd6
+ 00b4b7ac bytes 00013fd6
- 00b4b758 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b758 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b60:8"]]
- 00b4b758 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b7f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b7f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c60:8"]]
+ 00b4b7f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b758 bytes a0822d39
+ 00b4b7f4 bytes a0823139
- 00b4b6e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b60:8"]]
- 00b4b6e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4b6e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4b780 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c60:8"]]
+ 00b4b780 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b780 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4b6e4 bytes a8826d39
+ 00b4b780 bytes a8827139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc50954e1a502ee4457b35fe5857d739"></a>

### [`00b4b76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md) → [`00b4b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b808.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4b7a8",
      "incomplete_value": true,
      "site": "00b4b7a8",
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
            "const:b60:8"
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
    "old": {
      "definition_site": "00b4b7f8",
      "incomplete_value": true,
      "site": "00b4b7f8",
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
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00b4b784",
      "incomplete_value": true,
      "site": "00b4b784",
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
      "00b4b81c",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b828",
      "READ",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b844",
      "WRITE",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b81c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b828",
      "READ",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b844",
      "WRITE",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7a8) · [`00b4b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7f4) · [`00b4b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7f8)
- 新版 `00b4b844`（命令位置の公開資料なし） · `00b4b890`（命令位置の公開資料なし） · `00b4b894`（命令位置の公開資料なし）

~~~diff
- 00b4b7a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b7a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b7a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b60:8"]]
- 00b4b7a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b844 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b844 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b844 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c60:8"]]
+ 00b4b844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b7a8 bytes bf822d39
+ 00b4b844 bytes bf823139
- 00b4b7f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b7f4 ["INT_ADD", "register:40f0:8", ["const:b4b7f4:8", "const:4:8"]]
- 00b4b7f4 ["CALLIND", null, ["register:0:8"]]
+ 00b4b890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b890 ["INT_ADD", "register:40f0:8", ["const:b4b890:8", "const:4:8"]]
+ 00b4b890 ["CALLIND", null, ["register:0:8"]]
- 00b4b7f4 bytes 00013fd6
+ 00b4b890 bytes 00013fd6
- 00b4b7f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
- 00b4b7f8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b7f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4b894 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b7f8 bytes 9fae05f9
+ 00b4b894 bytes 9f2e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a134ccd4637a1585b6276bc496bd0ec"></a>

### [`00b4b80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md) → [`00b4b8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b8a8.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4b84c",
      "incomplete_value": true,
      "site": "00b4b84c",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b828",
      "incomplete_value": true,
      "site": "00b4b828",
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
    "old": {
      "definition_site": "00b4b830",
      "incomplete_value": false,
      "site": "00b4b844",
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
            "const:a31:8"
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
      "00b4b8bc",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8cc",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b8e8",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b8bc",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8cc",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b8e8",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b844) · [`00b4b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b84c) · [`00b4b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b820)
- 新版 `00b4b8e0`（命令位置の公開資料なし） · `00b4b8e8`（命令位置の公開資料なし） · `00b4b8bc`（命令位置の公開資料なし）

~~~diff
- 00b4b844 ["INT_ADD", "register:40f0:8", ["const:b4b844:8", "const:4:8"]]
- 00b4b844 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b8e0 ["INT_ADD", "register:40f0:8", ["const:b4b8e0:8", "const:4:8"]]
+ 00b4b8e0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b844 bytes b33d0494
+ 00b4b8e0 bytes c03d0494
- 00b4b84c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
- 00b4b84c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b8e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4b8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b84c bytes 80ae05f9
+ 00b4b8e8 bytes 802e06f9
- 00b4b820 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
- 00b4b820 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b8bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4b8bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b820 bytes 81ae45f9
+ 00b4b8bc bytes 812e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4e9ec7170150d40945c715020c88749"></a>

### [`00b4b87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md) → [`00b4b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b918.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b530.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b600.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b898",
      "incomplete_value": false,
      "site": "00b4b89c",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4b8a8",
      "incomplete_value": true,
      "site": "00b4b8b4",
      "value": [
        "LOAD",
        "8",
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
      "00b4b934",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b944",
      "DATA",
      [
        "storage",
        "01125b68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b934",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4b944",
      "DATA",
      [
        "storage",
        "01125c68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b89c) · [`00b4b898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b898) · [`00b4b8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b8a4)
- 新版 `00b4b938`（命令位置の公開資料なし） · `00b4b934`（命令位置の公開資料なし） · `00b4b940`（命令位置の公開資料なし）

~~~diff
- 00b4b89c ["INT_ADD", "register:40f0:8", ["const:b4b89c:8", "const:4:8"]]
- 00b4b89c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b938 ["INT_ADD", "register:40f0:8", ["const:b4b938:8", "const:4:8"]]
+ 00b4b938 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b89c bytes d93d0494
+ 00b4b938 bytes e63d0494
- 00b4b898 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4b898 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b898 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b898 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b934 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4b934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b898 bytes 009c0d91
+ 00b4b934 bytes 002c0c91
- 00b4b8a4 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00b4b8a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b8a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b940 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00b4b940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b8a4 bytes 08a12d91
+ 00b4b940 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ae041314954b1b56eeeb6cb609fe38"></a>

### [`00b4b8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md) → [`00b4b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b954.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b8f8",
      "incomplete_value": true,
      "site": "00b4b8f8",
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
            "const:b58:8"
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
    "old": {
      "definition_site": "00b4b8d4",
      "incomplete_value": true,
      "site": "00b4b8d4",
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
    "old": {
      "definition_site": "00b4b8dc",
      "incomplete_value": false,
      "site": "00b4b8f0",
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
            "const:a31:8"
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
      "00b4b968",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b978",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b994",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b968",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b978",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4b994",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8f0) · [`00b4b8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8f8) · [`00b4b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8cc)
- 新版 `00b4b98c`（命令位置の公開資料なし） · `00b4b994`（命令位置の公開資料なし） · `00b4b968`（命令位置の公開資料なし）

~~~diff
- 00b4b8f0 ["INT_ADD", "register:40f0:8", ["const:b4b8f0:8", "const:4:8"]]
- 00b4b8f0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4b98c ["INT_ADD", "register:40f0:8", ["const:b4b98c:8", "const:4:8"]]
+ 00b4b98c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b8f0 bytes 883d0494
+ 00b4b98c bytes 953d0494
- 00b4b8f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
- 00b4b8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4b994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b8f8 bytes 80ae05f9
+ 00b4b994 bytes 802e06f9
- 00b4b8cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
- 00b4b8cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b968 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4b968 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b8cc bytes 81ae45f9
+ 00b4b968 bytes 812e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7fcd5144d169393df2c22d4c6ed44a7"></a>

### [`00b4b928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md) → [`00b4b9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b9c4.md) _ZN8firebase4util6intent10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4b944",
      "incomplete_value": false,
      "site": "00b4b948",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4b954",
      "incomplete_value": true,
      "site": "00b4b960",
      "value": [
        "LOAD",
        "8",
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
      "00b4b9e0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b9f0",
      "DATA",
      [
        "storage",
        "01125b90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b9e0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b9f0",
      "DATA",
      [
        "storage",
        "01125c90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b948) · [`00b4b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b944) · [`00b4b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b950)
- 新版 `00b4b9e4`（命令位置の公開資料なし） · `00b4b9e0`（命令位置の公開資料なし） · `00b4b9ec`（命令位置の公開資料なし）

~~~diff
- 00b4b948 ["INT_ADD", "register:40f0:8", ["const:b4b948:8", "const:4:8"]]
- 00b4b948 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4b9e4 ["INT_ADD", "register:40f0:8", ["const:b4b9e4:8", "const:4:8"]]
+ 00b4b9e4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4b948 bytes ae3d0494
+ 00b4b9e4 bytes bb3d0494
- 00b4b944 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4b944 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b944 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b944 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b9e0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4b9e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b9e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b9e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b944 bytes 00781491
+ 00b4b9e0 bytes 00341591
- 00b4b950 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00b4b950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b9ec ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00b4b9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b950 bytes 08412e91
+ 00b4b9ec bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a54bf1e7ab4a19b9bdd831b63c3fd14f"></a>

### [`00b4b964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md) → [`00b4ba00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba00.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b990",
      "incomplete_value": true,
      "site": "00b4b990",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4b978",
      "incomplete_value": true,
      "site": "00b4b978",
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
    "old": {
      "definition_site": "00b4b984",
      "incomplete_value": false,
      "site": "00b4b988",
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
            "const:976:8"
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
      "00b4ba10",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba20",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4ba2c",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba10",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba20",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4ba2c",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b988) · [`00b4b990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b990) · [`00b4b974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b974)
- 新版 `00b4ba24`（命令位置の公開資料なし） · `00b4ba2c`（命令位置の公開資料なし） · `00b4ba10`（命令位置の公開資料なし）

~~~diff
- 00b4b988 ["INT_ADD", "register:40f0:8", ["const:b4b988:8", "const:4:8"]]
- 00b4b988 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ba24 ["INT_ADD", "register:40f0:8", ["const:b4ba24:8", "const:4:8"]]
+ 00b4ba24 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b988 bytes 623d0494
+ 00b4ba24 bytes 6f3d0494
- 00b4b990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4b990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ba2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4ba2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b990 bytes 60ce05f9
+ 00b4ba2c bytes 604e06f9
- 00b4b974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4b974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ba10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4ba10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b974 bytes 68ce45f9
+ 00b4ba10 bytes 684e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33e1148c317dab221eac317590bad86b"></a>

### [`00b4b9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md) → [`00b4ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba40.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4b9d0",
      "incomplete_value": true,
      "site": "00b4b9d0",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4b9b8",
      "incomplete_value": true,
      "site": "00b4b9b8",
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
    "old": {
      "definition_site": "00b4b9c0",
      "incomplete_value": false,
      "site": "00b4b9c8",
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
            "const:976:8"
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
      "00b4ba50",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba5c",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4ba6c",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba50",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba5c",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4ba6c",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9c8) · [`00b4b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9d0) · [`00b4b9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9b4)
- 新版 `00b4ba64`（命令位置の公開資料なし） · `00b4ba6c`（命令位置の公開資料なし） · `00b4ba50`（命令位置の公開資料なし）

~~~diff
- 00b4b9c8 ["INT_ADD", "register:40f0:8", ["const:b4b9c8:8", "const:4:8"]]
- 00b4b9c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ba64 ["INT_ADD", "register:40f0:8", ["const:b4ba64:8", "const:4:8"]]
+ 00b4ba64 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4b9c8 bytes 523d0494
+ 00b4ba64 bytes 5f3d0494
- 00b4b9d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4b9d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ba6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4ba6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b9d0 bytes 60ce05f9
+ 00b4ba6c bytes 604e06f9
- 00b4b9b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4b9b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ba50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4ba50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b9b4 bytes 68ce45f9
+ 00b4ba50 bytes 684e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af59f713e7e91280ebb998f5c871310d"></a>

### [`00b4b9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md) → [`00b4ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba80.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4ba14",
      "incomplete_value": true,
      "site": "00b4ba14",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4b9f8",
      "incomplete_value": true,
      "site": "00b4b9f8",
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
    "old": {
      "definition_site": "00b4ba04",
      "incomplete_value": false,
      "site": "00b4ba0c",
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
            "const:976:8"
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
      "00b4ba90",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4baa0",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4bab0",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba90",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4baa0",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4bab0",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4ba0c) · [`00b4ba14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4ba14) · [`00b4b9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4b9f4)
- 新版 `00b4baa8`（命令位置の公開資料なし） · `00b4bab0`（命令位置の公開資料なし） · `00b4ba90`（命令位置の公開資料なし）

~~~diff
- 00b4ba0c ["INT_ADD", "register:40f0:8", ["const:b4ba0c:8", "const:4:8"]]
- 00b4ba0c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4baa8 ["INT_ADD", "register:40f0:8", ["const:b4baa8:8", "const:4:8"]]
+ 00b4baa8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ba0c bytes 413d0494
+ 00b4baa8 bytes 4e3d0494
- 00b4ba14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4ba14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4bab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ba14 bytes 60ce05f9
+ 00b4bab0 bytes 604e06f9
- 00b4b9f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4b9f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ba90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4ba90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b9f4 bytes 68ce45f9
+ 00b4ba90 bytes 684e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64d213e91bf5341c0a81725ed58c024"></a>

### [`00b4ba28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md) → [`00b4bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bac4.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4ba58",
      "incomplete_value": true,
      "site": "00b4ba58",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4ba3c",
      "incomplete_value": true,
      "site": "00b4ba3c",
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
    "old": {
      "definition_site": "00b4ba44",
      "incomplete_value": false,
      "site": "00b4ba50",
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
            "const:976:8"
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
      "00b4bad4",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bae0",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4baf4",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bad4",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bae0",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4baf4",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba50) · [`00b4ba58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba58) · [`00b4ba38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba38)
- 新版 `00b4baec`（命令位置の公開資料なし） · `00b4baf4`（命令位置の公開資料なし） · `00b4bad4`（命令位置の公開資料なし）

~~~diff
- 00b4ba50 ["INT_ADD", "register:40f0:8", ["const:b4ba50:8", "const:4:8"]]
- 00b4ba50 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4baec ["INT_ADD", "register:40f0:8", ["const:b4baec:8", "const:4:8"]]
+ 00b4baec ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ba50 bytes 303d0494
+ 00b4baec bytes 3d3d0494
- 00b4ba58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4ba58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4baf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4baf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ba58 bytes 60ce05f9
+ 00b4baf4 bytes 604e06f9
- 00b4ba38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
- 00b4ba38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
+ 00b4bad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ba38 bytes 68ce45f9
+ 00b4bad4 bytes 684e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b886f196933a8eb440defb504096df8d"></a>

### [`00b4ba78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md) → [`00b4bb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bb14.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4bb00",
      "incomplete_value": true,
      "site": "00b4bb00",
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
            "const:ba0:8"
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
    "old": {
      "definition_site": "00b4baac",
      "incomplete_value": true,
      "site": "00b4bab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
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
      "00b4bb28",
      "READ",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bb48",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb9c",
      "WRITE",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bb28",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bb48",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb9c",
      "WRITE",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4bab8) · [`00b4bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4bb00) · [`00b4ba8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4ba8c)
- 新版 `00b4bb54`（命令位置の公開資料なし） · `00b4bb9c`（命令位置の公開資料なし） · `00b4bb28`（命令位置の公開資料なし）

~~~diff
- 00b4bab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bab8 ["INT_ADD", "register:40f0:8", ["const:b4bab8:8", "const:4:8"]]
- 00b4bab8 ["CALLIND", null, ["register:0:8"]]
+ 00b4bb54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bb54 ["INT_ADD", "register:40f0:8", ["const:b4bb54:8", "const:4:8"]]
+ 00b4bb54 ["CALLIND", null, ["register:0:8"]]
- 00b4bab8 bytes 00013fd6
+ 00b4bb54 bytes 00013fd6
- 00b4bb00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4bb00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ba0:8"]]
- 00b4bb00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4bb9c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4bb9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ca0:8"]]
+ 00b4bb9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4bb00 bytes a0822e39
+ 00b4bb9c bytes a0823239
- 00b4ba8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ba0:8"]]
- 00b4ba8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4ba8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4bb28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ca0:8"]]
+ 00b4bb28 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bb28 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4ba8c bytes a8826e39
+ 00b4bb28 bytes a8827239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d96968b74b4131db54acd8d59633d4"></a>

### [`00b4bb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md) → [`00b4bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bbb0.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4bb50",
      "incomplete_value": true,
      "site": "00b4bb50",
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
            "const:ba0:8"
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
    "old": {
      "definition_site": "00b4bba0",
      "incomplete_value": true,
      "site": "00b4bba0",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4bb2c",
      "incomplete_value": true,
      "site": "00b4bb2c",
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
      "00b4bbc4",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbd0",
      "READ",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bbec",
      "WRITE",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bbc4",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbd0",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bbec",
      "WRITE",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bb50) · [`00b4bb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bb9c) · [`00b4bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bba0)
- 新版 `00b4bbec`（命令位置の公開資料なし） · `00b4bc38`（命令位置の公開資料なし） · `00b4bc3c`（命令位置の公開資料なし）

~~~diff
- 00b4bb50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4bb50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4bb50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ba0:8"]]
- 00b4bb50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bbec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bbec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bbec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ca0:8"]]
+ 00b4bbec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4bb50 bytes bf822e39
+ 00b4bbec bytes bf823239
- 00b4bb9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bb9c ["INT_ADD", "register:40f0:8", ["const:b4bb9c:8", "const:4:8"]]
- 00b4bb9c ["CALLIND", null, ["register:0:8"]]
+ 00b4bc38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bc38 ["INT_ADD", "register:40f0:8", ["const:b4bc38:8", "const:4:8"]]
+ 00b4bc38 ["CALLIND", null, ["register:0:8"]]
- 00b4bb9c bytes 00013fd6
+ 00b4bc38 bytes 00013fd6
- 00b4bba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
- 00b4bba0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bc3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00b4bc3c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bba0 bytes 9fce05f9
+ 00b4bc3c bytes 9f4e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef014eda1111a398cb47c47b172c079"></a>

### [`00b4bbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md) → [`00b4bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bc50.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4bbf4",
      "incomplete_value": true,
      "site": "00b4bbf4",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4bbd0",
      "incomplete_value": true,
      "site": "00b4bbd0",
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
    "old": {
      "definition_site": "00b4bbd8",
      "incomplete_value": false,
      "site": "00b4bbec",
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
            "const:976:8"
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
      "00b4bc64",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc74",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4bc90",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bc64",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc74",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4bc90",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbec) · [`00b4bbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbf4) · [`00b4bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbc8)
- 新版 `00b4bc88`（命令位置の公開資料なし） · `00b4bc90`（命令位置の公開資料なし） · `00b4bc64`（命令位置の公開資料なし）

~~~diff
- 00b4bbec ["INT_ADD", "register:40f0:8", ["const:b4bbec:8", "const:4:8"]]
- 00b4bbec ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4bc88 ["INT_ADD", "register:40f0:8", ["const:b4bc88:8", "const:4:8"]]
+ 00b4bc88 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bbec bytes c93c0494
+ 00b4bc88 bytes d63c0494
- 00b4bbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
- 00b4bbf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00b4bc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bbf4 bytes 80ce05f9
+ 00b4bc90 bytes 804e06f9
- 00b4bbc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
- 00b4bbc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bc64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00b4bc64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bbc8 bytes 81ce45f9
+ 00b4bc64 bytes 814e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97ad407be10654f6d14847fc2cf2f6c9"></a>

### [`00b4bc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md) → [`00b4bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcc0.md) _ZN8firebase4util8iterable11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4bc40",
      "incomplete_value": false,
      "site": "00b4bc44",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4bc50",
      "incomplete_value": true,
      "site": "00b4bc5c",
      "value": [
        "LOAD",
        "8",
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
      "00b4bcdc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4bcec",
      "DATA",
      [
        "storage",
        "01125ba8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bcdc",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4bcec",
      "DATA",
      [
        "storage",
        "01125ca8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc44) · [`00b4bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc40) · [`00b4bc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc4c)
- 新版 `00b4bce0`（命令位置の公開資料なし） · `00b4bcdc`（命令位置の公開資料なし） · `00b4bce8`（命令位置の公開資料なし）

~~~diff
- 00b4bc44 ["INT_ADD", "register:40f0:8", ["const:b4bc44:8", "const:4:8"]]
- 00b4bc44 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4bce0 ["INT_ADD", "register:40f0:8", ["const:b4bce0:8", "const:4:8"]]
+ 00b4bce0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4bc44 bytes ef3c0494
+ 00b4bce0 bytes fc3c0494
- 00b4bc40 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4bc40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bc40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bc40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcdc ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4bcdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bc40 bytes 009c0d91
+ 00b4bcdc bytes 002c0c91
- 00b4bc4c ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00b4bc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4bce8 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00b4bce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bc4c bytes 08a12e91
+ 00b4bce8 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646dfe0f15d9090606102fd580b8f8f9"></a>

### [`00b4bc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md) → [`00b4bcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcfc.md) _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4bca0",
      "incomplete_value": true,
      "site": "00b4bca0",
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
            "const:b98:8"
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
    "old": {
      "definition_site": "00b4bc7c",
      "incomplete_value": true,
      "site": "00b4bc7c",
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
    "old": {
      "definition_site": "00b4bc84",
      "incomplete_value": false,
      "site": "00b4bc98",
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
            "const:976:8"
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
      "00b4bd10",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd20",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4bd3c",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd10",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd20",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4bd3c",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bc98) · [`00b4bca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bca0) · [`00b4bc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bc74)
- 新版 `00b4bd34`（命令位置の公開資料なし） · `00b4bd3c`（命令位置の公開資料なし） · `00b4bd10`（命令位置の公開資料なし）

~~~diff
- 00b4bc98 ["INT_ADD", "register:40f0:8", ["const:b4bc98:8", "const:4:8"]]
- 00b4bc98 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4bd34 ["INT_ADD", "register:40f0:8", ["const:b4bd34:8", "const:4:8"]]
+ 00b4bd34 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bc98 bytes 9e3c0494
+ 00b4bd34 bytes ab3c0494
- 00b4bca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
- 00b4bca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bd3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00b4bd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bca0 bytes 80ce05f9
+ 00b4bd3c bytes 804e06f9
- 00b4bc74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
- 00b4bc74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bd10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00b4bd10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bc74 bytes 81ce45f9
+ 00b4bd10 bytes 814e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ba4672055153c25609db6a4ae67dcc"></a>

### [`00b4bcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md) → [`00b4bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bd6c.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4bcec",
      "incomplete_value": false,
      "site": "00b4bcf0",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4bcfc",
      "incomplete_value": true,
      "site": "00b4bd08",
      "value": [
        "LOAD",
        "8",
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
      "00b4bd88",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4bd98",
      "DATA",
      [
        "storage",
        "01125bb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bd88",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4bd98",
      "DATA",
      [
        "storage",
        "01125cb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcf0) · [`00b4bcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcec) · [`00b4bcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcf8)
- 新版 `00b4bd8c`（命令位置の公開資料なし） · `00b4bd88`（命令位置の公開資料なし） · `00b4bd94`（命令位置の公開資料なし）

~~~diff
- 00b4bcf0 ["INT_ADD", "register:40f0:8", ["const:b4bcf0:8", "const:4:8"]]
- 00b4bcf0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4bd8c ["INT_ADD", "register:40f0:8", ["const:b4bd8c:8", "const:4:8"]]
+ 00b4bd8c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4bcf0 bytes c43c0494
+ 00b4bd8c bytes d13c0494
- 00b4bcec ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4bcec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bcec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bcec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bd88 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4bd88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bd88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bd88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bcec bytes 00781491
+ 00b4bd88 bytes 00341591
- 00b4bcf8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 00b4bcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4bd94 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00b4bd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bcf8 bytes 08c12e91
+ 00b4bd94 bytes 08c13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1abbab5693cf4996c5424edd82a04d8"></a>

### [`00b4bd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md) → [`00b4bda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bda8.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4bd38",
      "incomplete_value": true,
      "site": "00b4bd38",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bd20",
      "incomplete_value": true,
      "site": "00b4bd20",
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
    "old": {
      "definition_site": "00b4bd2c",
      "incomplete_value": false,
      "site": "00b4bd30",
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
            "const:157:8"
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
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdc8",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4bdd4",
      "WRITE",
      [
        "storage",
        "01125bb8",
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
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdc8",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4bdd4",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd30) · [`00b4bd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd38) · [`00b4bd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd1c)
- 新版 `00b4bdcc`（命令位置の公開資料なし） · `00b4bdd4`（命令位置の公開資料なし） · `00b4bdb8`（命令位置の公開資料なし）

~~~diff
- 00b4bd30 ["INT_ADD", "register:40f0:8", ["const:b4bd30:8", "const:4:8"]]
- 00b4bd30 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4bdcc ["INT_ADD", "register:40f0:8", ["const:b4bdcc:8", "const:4:8"]]
+ 00b4bdcc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bd30 bytes 783c0494
+ 00b4bdcc bytes 853c0494
- 00b4bd38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bd38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bdd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4bdd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bd38 bytes 60de05f9
+ 00b4bdd4 bytes 605e06f9
- 00b4bd1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bd1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bdb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4bdb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bd1c bytes 68de45f9
+ 00b4bdb8 bytes 685e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ba8c7659f7ee620e2b32f767c1f1d38"></a>

### [`00b4bd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md) → [`00b4bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4bd78",
      "incomplete_value": true,
      "site": "00b4bd78",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bd60",
      "incomplete_value": true,
      "site": "00b4bd60",
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
    "old": {
      "definition_site": "00b4bd68",
      "incomplete_value": false,
      "site": "00b4bd70",
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
            "const:157:8"
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
      "00b4bdf8",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be04",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4be14",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bdf8",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be04",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4be14",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd70) · [`00b4bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd78) · [`00b4bd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd5c)
- 新版 `00b4be0c`（命令位置の公開資料なし） · `00b4be14`（命令位置の公開資料なし） · `00b4bdf8`（命令位置の公開資料なし）

~~~diff
- 00b4bd70 ["INT_ADD", "register:40f0:8", ["const:b4bd70:8", "const:4:8"]]
- 00b4bd70 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4be0c ["INT_ADD", "register:40f0:8", ["const:b4be0c:8", "const:4:8"]]
+ 00b4be0c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bd70 bytes 683c0494
+ 00b4be0c bytes 753c0494
- 00b4bd78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bd78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4be14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4be14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bd78 bytes 60de05f9
+ 00b4be14 bytes 605e06f9
- 00b4bd5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bd5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bdf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4bdf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bd5c bytes 68de45f9
+ 00b4bdf8 bytes 685e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68d1b0a86e01fbb7cdcb26730dab6d11"></a>

### [`00b4bd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md) → [`00b4be28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be28.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4bdbc",
      "incomplete_value": true,
      "site": "00b4bdbc",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bda0",
      "incomplete_value": true,
      "site": "00b4bda0",
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
    "old": {
      "definition_site": "00b4bdac",
      "incomplete_value": false,
      "site": "00b4bdb4",
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
            "const:157:8"
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
      "00b4be38",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be48",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4be58",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4be38",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be48",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4be58",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bdb4) · [`00b4bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bdbc) · [`00b4bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bd9c)
- 新版 `00b4be50`（命令位置の公開資料なし） · `00b4be58`（命令位置の公開資料なし） · `00b4be38`（命令位置の公開資料なし）

~~~diff
- 00b4bdb4 ["INT_ADD", "register:40f0:8", ["const:b4bdb4:8", "const:4:8"]]
- 00b4bdb4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4be50 ["INT_ADD", "register:40f0:8", ["const:b4be50:8", "const:4:8"]]
+ 00b4be50 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bdb4 bytes 573c0494
+ 00b4be50 bytes 643c0494
- 00b4bdbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bdbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4be58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4be58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bdbc bytes 60de05f9
+ 00b4be58 bytes 605e06f9
- 00b4bd9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bd9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4be38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4be38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bd9c bytes 68de45f9
+ 00b4be38 bytes 685e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c861cabb3aa84afc4ec51f73b9356926"></a>

### [`00b4bdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md) → [`00b4be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be6c.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4be00",
      "incomplete_value": true,
      "site": "00b4be00",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bde4",
      "incomplete_value": true,
      "site": "00b4bde4",
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
    "old": {
      "definition_site": "00b4bdec",
      "incomplete_value": false,
      "site": "00b4bdf8",
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
            "const:157:8"
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
      "00b4be7c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be88",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4be9c",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4be7c",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be88",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4be9c",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4bdf8) · [`00b4be00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4be00) · [`00b4bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4bde0)
- 新版 `00b4be94`（命令位置の公開資料なし） · `00b4be9c`（命令位置の公開資料なし） · `00b4be7c`（命令位置の公開資料なし）

~~~diff
- 00b4bdf8 ["INT_ADD", "register:40f0:8", ["const:b4bdf8:8", "const:4:8"]]
- 00b4bdf8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4be94 ["INT_ADD", "register:40f0:8", ["const:b4be94:8", "const:4:8"]]
+ 00b4be94 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bdf8 bytes 463c0494
+ 00b4be94 bytes 533c0494
- 00b4be00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4be00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4be9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4be9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4be00 bytes 60de05f9
+ 00b4be9c bytes 605e06f9
- 00b4bde0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
- 00b4bde0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4be7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
+ 00b4be7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bde0 bytes 68de45f9
+ 00b4be7c bytes 685e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52cec2e9fdb0944ebfc31e7983cfd759"></a>

### [`00b4be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md) → [`00b4bebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bebc.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4bea8",
      "incomplete_value": true,
      "site": "00b4bea8",
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
            "const:bc0:8"
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
    "old": {
      "definition_site": "00b4be54",
      "incomplete_value": true,
      "site": "00b4be60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
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
      "00b4bed0",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bef0",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf44",
      "WRITE",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bed0",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bef0",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf44",
      "WRITE",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4be60) · [`00b4bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4bea8) · [`00b4be34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4be34)
- 新版 `00b4befc`（命令位置の公開資料なし） · `00b4bf44`（命令位置の公開資料なし） · `00b4bed0`（命令位置の公開資料なし）

~~~diff
- 00b4be60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4be60 ["INT_ADD", "register:40f0:8", ["const:b4be60:8", "const:4:8"]]
- 00b4be60 ["CALLIND", null, ["register:0:8"]]
+ 00b4befc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4befc ["INT_ADD", "register:40f0:8", ["const:b4befc:8", "const:4:8"]]
+ 00b4befc ["CALLIND", null, ["register:0:8"]]
- 00b4be60 bytes 00013fd6
+ 00b4befc bytes 00013fd6
- 00b4bea8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4bea8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bc0:8"]]
- 00b4bea8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4bf44 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4bf44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cc0:8"]]
+ 00b4bf44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4bea8 bytes a0022f39
+ 00b4bf44 bytes a0023339
- 00b4be34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bc0:8"]]
- 00b4be34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4be34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4bed0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc0:8"]]
+ 00b4bed0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bed0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4be34 bytes a8026f39
+ 00b4bed0 bytes a8027339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f663e5552a0c691eb11e94bd9cb565"></a>

### [`00b4bebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md) → [`00b4bf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4bef8",
      "incomplete_value": true,
      "site": "00b4bef8",
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
            "const:bc0:8"
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
    "old": {
      "definition_site": "00b4bf48",
      "incomplete_value": true,
      "site": "00b4bf48",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bed4",
      "incomplete_value": true,
      "site": "00b4bed4",
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
      "00b4bf6c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf78",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bf94",
      "WRITE",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf6c",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf78",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bf94",
      "WRITE",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bef8) · [`00b4bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bf44) · [`00b4bf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bf48)
- 新版 `00b4bf94`（命令位置の公開資料なし） · `00b4bfe0`（命令位置の公開資料なし） · `00b4bfe4`（命令位置の公開資料なし）

~~~diff
- 00b4bef8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4bef8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4bef8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bc0:8"]]
- 00b4bef8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bf94 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bf94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bf94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cc0:8"]]
+ 00b4bf94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4bef8 bytes bf022f39
+ 00b4bf94 bytes bf023339
- 00b4bf44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bf44 ["INT_ADD", "register:40f0:8", ["const:b4bf44:8", "const:4:8"]]
- 00b4bf44 ["CALLIND", null, ["register:0:8"]]
+ 00b4bfe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bfe0 ["INT_ADD", "register:40f0:8", ["const:b4bfe0:8", "const:4:8"]]
+ 00b4bfe0 ["CALLIND", null, ["register:0:8"]]
- 00b4bf44 bytes 00013fd6
+ 00b4bfe0 bytes 00013fd6
- 00b4bf48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00b4bf48 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bf48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bfe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00b4bfe4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bfe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bf48 bytes 9fde05f9
+ 00b4bfe4 bytes 9f5e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cfe55e7e30312054869da417961715d"></a>

### [`00b4bf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md) → [`00b4bff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4bf9c",
      "incomplete_value": true,
      "site": "00b4bf9c",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4bf78",
      "incomplete_value": true,
      "site": "00b4bf78",
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
    "old": {
      "definition_site": "00b4bf80",
      "incomplete_value": false,
      "site": "00b4bf94",
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
            "const:157:8"
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
      "00b4c00c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c01c",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4c038",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c00c",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c01c",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4c038",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf94) · [`00b4bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf9c) · [`00b4bf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf70)
- 新版 `00b4c030`（命令位置の公開資料なし） · `00b4c038`（命令位置の公開資料なし） · `00b4c00c`（命令位置の公開資料なし）

~~~diff
- 00b4bf94 ["INT_ADD", "register:40f0:8", ["const:b4bf94:8", "const:4:8"]]
- 00b4bf94 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c030 ["INT_ADD", "register:40f0:8", ["const:b4c030:8", "const:4:8"]]
+ 00b4c030 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4bf94 bytes df3b0494
+ 00b4c030 bytes ec3b0494
- 00b4bf9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00b4bf9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00b4c038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bf9c bytes 80de05f9
+ 00b4c038 bytes 805e06f9
- 00b4bf70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00b4bf70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c00c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00b4c00c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bf70 bytes 81de45f9
+ 00b4c00c bytes 815e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56cc42c836b41529ac775dc6adfab5ae"></a>

### [`00b4bfcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md) → [`00b4c068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b560.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b630.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4bfe8",
      "incomplete_value": false,
      "site": "00b4bfec",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4bff8",
      "incomplete_value": true,
      "site": "00b4c004",
      "value": [
        "LOAD",
        "8",
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
      "00b4c084",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4c094",
      "DATA",
      [
        "storage",
        "01125bc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c084",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4c094",
      "DATA",
      [
        "storage",
        "01125cc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bfec) · [`00b4bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bfe8) · [`00b4bff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bff4)
- 新版 `00b4c088`（命令位置の公開資料なし） · `00b4c084`（命令位置の公開資料なし） · `00b4c090`（命令位置の公開資料なし）

~~~diff
- 00b4bfec ["INT_ADD", "register:40f0:8", ["const:b4bfec:8", "const:4:8"]]
- 00b4bfec ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4c088 ["INT_ADD", "register:40f0:8", ["const:b4c088:8", "const:4:8"]]
+ 00b4c088 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4bfec bytes 053c0494
+ 00b4c088 bytes 123c0494
- 00b4bfe8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4bfe8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bfe8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bfe8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c084 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4c084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bfe8 bytes 009c0d91
+ 00b4c084 bytes 002c0c91
- 00b4bff4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00b4bff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c090 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00b4c090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bff4 bytes 08212f91
+ 00b4c090 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3680316524ea3a551b3ae52341e57f49"></a>

### [`00b4c008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md) → [`00b4c0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c0a4.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c048",
      "incomplete_value": true,
      "site": "00b4c048",
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
            "const:bb8:8"
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
    "old": {
      "definition_site": "00b4c024",
      "incomplete_value": true,
      "site": "00b4c024",
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
    "old": {
      "definition_site": "00b4c02c",
      "incomplete_value": false,
      "site": "00b4c040",
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
            "const:157:8"
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
      "00b4c0b8",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0c8",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e4",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c0b8",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0c8",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e4",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c040) · [`00b4c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c048) · [`00b4c01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c01c)
- 新版 `00b4c0dc`（命令位置の公開資料なし） · `00b4c0e4`（命令位置の公開資料なし） · `00b4c0b8`（命令位置の公開資料なし）

~~~diff
- 00b4c040 ["INT_ADD", "register:40f0:8", ["const:b4c040:8", "const:4:8"]]
- 00b4c040 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c0dc ["INT_ADD", "register:40f0:8", ["const:b4c0dc:8", "const:4:8"]]
+ 00b4c0dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c040 bytes b43b0494
+ 00b4c0dc bytes c13b0494
- 00b4c048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00b4c048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c0e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00b4c0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c048 bytes 80de05f9
+ 00b4c0e4 bytes 805e06f9
- 00b4c01c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00b4c01c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c0b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00b4c0b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c01c bytes 81de45f9
+ 00b4c0b8 bytes 815e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7303b000de6c6082863c92969648ffa"></a>

### [`00b4c078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md) → [`00b4c114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c114.md) _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4c094",
      "incomplete_value": false,
      "site": "00b4c098",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4c0a4",
      "incomplete_value": true,
      "site": "00b4c0b0",
      "value": [
        "LOAD",
        "8",
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
      "00b4c130",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4c140",
      "DATA",
      [
        "storage",
        "01125bd8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c130",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c140",
      "DATA",
      [
        "storage",
        "01125cd8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c098) · [`00b4c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c094) · [`00b4c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c0a0)
- 新版 `00b4c134`（命令位置の公開資料なし） · `00b4c130`（命令位置の公開資料なし） · `00b4c13c`（命令位置の公開資料なし）

~~~diff
- 00b4c098 ["INT_ADD", "register:40f0:8", ["const:b4c098:8", "const:4:8"]]
- 00b4c098 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4c134 ["INT_ADD", "register:40f0:8", ["const:b4c134:8", "const:4:8"]]
+ 00b4c134 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4c098 bytes da3b0494
+ 00b4c134 bytes e73b0494
- 00b4c094 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4c094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c130 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4c130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c094 bytes 00781491
+ 00b4c130 bytes 00341591
- 00b4c0a0 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00b4c0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c13c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00b4c13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c0a0 bytes 08612f91
+ 00b4c13c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1872cac990028465dee35b6be9d51fce"></a>

### [`00b4c0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md) → [`00b4c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c150.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c0e0",
      "incomplete_value": true,
      "site": "00b4c0e0",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c0c8",
      "incomplete_value": true,
      "site": "00b4c0c8",
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
    "old": {
      "definition_site": "00b4c0d4",
      "incomplete_value": false,
      "site": "00b4c0d8",
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
            "const:989:8"
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
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c170",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c17c",
      "WRITE",
      [
        "storage",
        "01125be0",
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
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c170",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c17c",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0d8) · [`00b4c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0e0) · [`00b4c0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0c4)
- 新版 `00b4c174`（命令位置の公開資料なし） · `00b4c17c`（命令位置の公開資料なし） · `00b4c160`（命令位置の公開資料なし）

~~~diff
- 00b4c0d8 ["INT_ADD", "register:40f0:8", ["const:b4c0d8:8", "const:4:8"]]
- 00b4c0d8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c174 ["INT_ADD", "register:40f0:8", ["const:b4c174:8", "const:4:8"]]
+ 00b4c174 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c0d8 bytes 8e3b0494
+ 00b4c174 bytes 9b3b0494
- 00b4c0e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c0e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c17c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c17c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c0e0 bytes 60f205f9
+ 00b4c17c bytes 607206f9
- 00b4c0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c0c4 bytes 68f245f9
+ 00b4c160 bytes 687246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25be6cf4a1602988439824216e3d8d91"></a>

### [`00b4c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md) → [`00b4c190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c190.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c120",
      "incomplete_value": true,
      "site": "00b4c120",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c108",
      "incomplete_value": true,
      "site": "00b4c108",
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
    "old": {
      "definition_site": "00b4c110",
      "incomplete_value": false,
      "site": "00b4c118",
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
            "const:989:8"
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
      "00b4c1a0",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1ac",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c1bc",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c1a0",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1ac",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c1bc",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c118) · [`00b4c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c120) · [`00b4c104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c104)
- 新版 `00b4c1b4`（命令位置の公開資料なし） · `00b4c1bc`（命令位置の公開資料なし） · `00b4c1a0`（命令位置の公開資料なし）

~~~diff
- 00b4c118 ["INT_ADD", "register:40f0:8", ["const:b4c118:8", "const:4:8"]]
- 00b4c118 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c1b4 ["INT_ADD", "register:40f0:8", ["const:b4c1b4:8", "const:4:8"]]
+ 00b4c1b4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c118 bytes 7e3b0494
+ 00b4c1b4 bytes 8b3b0494
- 00b4c120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c120 bytes 60f205f9
+ 00b4c1bc bytes 607206f9
- 00b4c104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c1a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c1a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c104 bytes 68f245f9
+ 00b4c1a0 bytes 687246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f47826d3760203d767176a58aef1beb"></a>

### [`00b4c134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md) → [`00b4c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c1d0.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c164",
      "incomplete_value": true,
      "site": "00b4c164",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c148",
      "incomplete_value": true,
      "site": "00b4c148",
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
    "old": {
      "definition_site": "00b4c154",
      "incomplete_value": false,
      "site": "00b4c15c",
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
            "const:989:8"
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
      "00b4c1e0",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1f0",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c200",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c1e0",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1f0",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c200",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c15c) · [`00b4c164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c164) · [`00b4c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c144)
- 新版 `00b4c1f8`（命令位置の公開資料なし） · `00b4c200`（命令位置の公開資料なし） · `00b4c1e0`（命令位置の公開資料なし）

~~~diff
- 00b4c15c ["INT_ADD", "register:40f0:8", ["const:b4c15c:8", "const:4:8"]]
- 00b4c15c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c1f8 ["INT_ADD", "register:40f0:8", ["const:b4c1f8:8", "const:4:8"]]
+ 00b4c1f8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c15c bytes 6d3b0494
+ 00b4c1f8 bytes 7a3b0494
- 00b4c164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c164 bytes 60f205f9
+ 00b4c200 bytes 607206f9
- 00b4c144 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c144 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c1e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c144 bytes 68f245f9
+ 00b4c1e0 bytes 687246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cdbb29192276b0a68ed2dcde1885484"></a>

### [`00b4c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md) → [`00b4c214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c214.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c1a8",
      "incomplete_value": true,
      "site": "00b4c1a8",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c18c",
      "incomplete_value": true,
      "site": "00b4c18c",
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
    "old": {
      "definition_site": "00b4c194",
      "incomplete_value": false,
      "site": "00b4c1a0",
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
            "const:989:8"
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
      "00b4c224",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c230",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c244",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c224",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c230",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c244",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c1a0) · [`00b4c1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c1a8) · [`00b4c188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c188)
- 新版 `00b4c23c`（命令位置の公開資料なし） · `00b4c244`（命令位置の公開資料なし） · `00b4c224`（命令位置の公開資料なし）

~~~diff
- 00b4c1a0 ["INT_ADD", "register:40f0:8", ["const:b4c1a0:8", "const:4:8"]]
- 00b4c1a0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c23c ["INT_ADD", "register:40f0:8", ["const:b4c23c:8", "const:4:8"]]
+ 00b4c23c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c1a0 bytes 5c3b0494
+ 00b4c23c bytes 693b0494
- 00b4c1a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c1a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c1a8 bytes 60f205f9
+ 00b4c244 bytes 607206f9
- 00b4c188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
- 00b4c188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
+ 00b4c224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c188 bytes 68f245f9
+ 00b4c224 bytes 687246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e135919914593db9b2d3b6efcd1275"></a>

### [`00b4c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md) → [`00b4c264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c264.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00b4c250",
      "incomplete_value": true,
      "site": "00b4c250",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c208"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4c2a4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c278",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4c1fc",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c2ec",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c278",
      "READ",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c298",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c2ec",
      "WRITE",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md#insn-00b4c208) · [`00b4c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md#insn-00b4c250)
- 新版 `00b4c2ec`（命令位置の公開資料なし） · `00b4c2a4`（命令位置の公開資料なし）

~~~diff
- 00b4c208 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c208 ["INT_ADD", "register:40f0:8", ["const:b4c208:8", "const:4:8"]]
- 00b4c208 ["CALLIND", null, ["register:0:8"]]
- 00b4c208 bytes 00013fd6
- 00b4c250 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c250 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:be8:8"]]
- 00b4c250 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c2ec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c2ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ce8:8"]]
+ 00b4c2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c250 bytes a0a22f39
+ 00b4c2ec bytes a0a23339
+ 00b4c2a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c2a4 ["INT_ADD", "register:40f0:8", ["const:b4c2a4:8", "const:4:8"]]
+ 00b4c2a4 ["CALLIND", null, ["register:0:8"]]
+ 00b4c2a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-029c4a8c03304639afcc92bcafa232ca"></a>

### [`00b4c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md) → [`00b4c300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c300.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4c2a0",
      "incomplete_value": true,
      "site": "00b4c2a0",
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
            "const:be8:8"
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
    "old": {
      "definition_site": "00b4c2f0",
      "incomplete_value": true,
      "site": "00b4c2f0",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c27c",
      "incomplete_value": true,
      "site": "00b4c27c",
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
      "00b4c314",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c320",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c33c",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c314",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c320",
      "READ",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c33c",
      "WRITE",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2a0) · [`00b4c2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2ec) · [`00b4c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2f0)
- 新版 `00b4c33c`（命令位置の公開資料なし） · `00b4c388`（命令位置の公開資料なし） · `00b4c38c`（命令位置の公開資料なし）

~~~diff
- 00b4c2a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c2a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c2a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:be8:8"]]
- 00b4c2a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c33c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c33c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c33c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ce8:8"]]
+ 00b4c33c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c2a0 bytes bfa22f39
+ 00b4c33c bytes bfa23339
- 00b4c2ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c2ec ["INT_ADD", "register:40f0:8", ["const:b4c2ec:8", "const:4:8"]]
- 00b4c2ec ["CALLIND", null, ["register:0:8"]]
+ 00b4c388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c388 ["INT_ADD", "register:40f0:8", ["const:b4c388:8", "const:4:8"]]
+ 00b4c388 ["CALLIND", null, ["register:0:8"]]
- 00b4c2ec bytes 00013fd6
+ 00b4c388 bytes 00013fd6
- 00b4c2f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00b4c2f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c2f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c38c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00b4c38c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c2f0 bytes 9ff205f9
+ 00b4c38c bytes 9f7206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a0ee879d746f8327bbaf6d978a99c0"></a>

### [`00b4c304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md) → [`00b4c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c3a0.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4c344",
      "incomplete_value": true,
      "site": "00b4c344",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c320",
      "incomplete_value": true,
      "site": "00b4c320",
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
    "old": {
      "definition_site": "00b4c328",
      "incomplete_value": false,
      "site": "00b4c33c",
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
            "const:989:8"
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
      "00b4c3b4",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c3c4",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c3e0",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c3b4",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c3c4",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c3e0",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c33c) · [`00b4c344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c344) · [`00b4c318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c318)
- 新版 `00b4c3d8`（命令位置の公開資料なし） · `00b4c3e0`（命令位置の公開資料なし） · `00b4c3b4`（命令位置の公開資料なし）

~~~diff
- 00b4c33c ["INT_ADD", "register:40f0:8", ["const:b4c33c:8", "const:4:8"]]
- 00b4c33c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c3d8 ["INT_ADD", "register:40f0:8", ["const:b4c3d8:8", "const:4:8"]]
+ 00b4c3d8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c33c bytes f53a0494
+ 00b4c3d8 bytes 023b0494
- 00b4c344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00b4c344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c3e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00b4c3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c344 bytes 80f205f9
+ 00b4c3e0 bytes 807206f9
- 00b4c318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00b4c318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c3b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00b4c3b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c318 bytes 81f245f9
+ 00b4c3b4 bytes 817246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d17a7461749d392831e35c826805d2ea"></a>

### [`00b4c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md) → [`00b4c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c410.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b520.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5f0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4c390",
      "incomplete_value": false,
      "site": "00b4c394",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4c3a0",
      "incomplete_value": true,
      "site": "00b4c3ac",
      "value": [
        "LOAD",
        "8",
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
      "00b4c42c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4c43c",
      "DATA",
      [
        "storage",
        "01125bf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c42c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4c43c",
      "DATA",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c394) · [`00b4c390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c390) · [`00b4c39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c39c)
- 新版 `00b4c430`（命令位置の公開資料なし） · `00b4c42c`（命令位置の公開資料なし） · `00b4c438`（命令位置の公開資料なし）

~~~diff
- 00b4c394 ["INT_ADD", "register:40f0:8", ["const:b4c394:8", "const:4:8"]]
- 00b4c394 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4c430 ["INT_ADD", "register:40f0:8", ["const:b4c430:8", "const:4:8"]]
+ 00b4c430 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4c394 bytes 1b3b0494
+ 00b4c430 bytes 283b0494
- 00b4c390 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4c390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c42c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4c42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c390 bytes 009c0d91
+ 00b4c42c bytes 002c0c91
- 00b4c39c ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 00b4c39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c438 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00b4c438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c39c bytes 08c12f91
+ 00b4c438 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58552cd47b3a2ede4ced545d78e2eff"></a>

### [`00b4c3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md) → [`00b4c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c44c.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c3f0",
      "incomplete_value": true,
      "site": "00b4c3f0",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00b4c3cc",
      "incomplete_value": true,
      "site": "00b4c3cc",
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
    "old": {
      "definition_site": "00b4c3d4",
      "incomplete_value": false,
      "site": "00b4c3e8",
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
            "const:989:8"
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
      "00b4c460",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c470",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c48c",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c460",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c470",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4c48c",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md#insn-00b4c3e8) · [`00b4c3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md#insn-00b4c3f0) · [`00b4c3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md#insn-00b4c3c4)
- 新版 `00b4c484`（命令位置の公開資料なし） · `00b4c48c`（命令位置の公開資料なし） · `00b4c460`（命令位置の公開資料なし）

~~~diff
- 00b4c3e8 ["INT_ADD", "register:40f0:8", ["const:b4c3e8:8", "const:4:8"]]
- 00b4c3e8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c484 ["INT_ADD", "register:40f0:8", ["const:b4c484:8", "const:4:8"]]
+ 00b4c484 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c3e8 bytes ca3a0494
+ 00b4c484 bytes d73a0494
- 00b4c3f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00b4c3f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c48c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00b4c48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c3f0 bytes 80f205f9
+ 00b4c48c bytes 807206f9
- 00b4c3c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00b4c3c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c460 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00b4c460 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c3c4 bytes 81f245f9
+ 00b4c460 bytes 817246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6464f9c7f3564e9c3dd6733c9d87b1"></a>

### [`00b4c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c420.md) → [`00b4c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4bc.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4c43c",
      "incomplete_value": false,
      "site": "00b4c440",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4c44c",
      "incomplete_value": true,
      "site": "00b4c458",
      "value": [
        "LOAD",
        "8",
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
      "00b4c4d8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4c4e8",
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
      "00b4c4d8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c4e8",
      "DATA",
      [
        "storage",
        "01125d08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c420.md#insn-00b4c440) · [`00b4c43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c420.md#insn-00b4c43c) · [`00b4c448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c420.md#insn-00b4c448)
- 新版 `00b4c4dc`（命令位置の公開資料なし） · `00b4c4d8`（命令位置の公開資料なし） · `00b4c4e4`（命令位置の公開資料なし）

~~~diff
- 00b4c440 ["INT_ADD", "register:40f0:8", ["const:b4c440:8", "const:4:8"]]
- 00b4c440 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4c4dc ["INT_ADD", "register:40f0:8", ["const:b4c4dc:8", "const:4:8"]]
+ 00b4c4dc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4c440 bytes f03a0494
+ 00b4c4dc bytes fd3a0494
- 00b4c43c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4c43c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c43c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c43c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c4d8 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4c4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c43c bytes 00781491
+ 00b4c4d8 bytes 00341591
- 00b4c448 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00b4c448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c4e4 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00b4c4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c448 bytes 08213091
+ 00b4c4e4 bytes 08213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12e1348141efcf64cbe394d2096e8a28"></a>

### [`00b4c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c4dc.md) → [`00b4c578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c578.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c50c",
      "incomplete_value": true,
      "site": "00b4c50c",
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
    "old": {
      "definition_site": "00b4c4f0",
      "incomplete_value": true,
      "site": "00b4c4f0",
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
    "old": {
      "definition_site": "00b4c4fc",
      "incomplete_value": false,
      "site": "00b4c504",
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
            "const:aac:8"
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
      "00b4c588",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c598",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c5a8",
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
      "00b4c588",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c598",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4c5a8",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c4dc.md#insn-00b4c504) · [`00b4c50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c4dc.md#insn-00b4c50c) · [`00b4c4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c4dc.md#insn-00b4c4ec)
- 新版 `00b4c5a0`（命令位置の公開資料なし） · `00b4c5a8`（命令位置の公開資料なし） · `00b4c588`（命令位置の公開資料なし）

~~~diff
- 00b4c504 ["INT_ADD", "register:40f0:8", ["const:b4c504:8", "const:4:8"]]
- 00b4c504 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c5a0 ["INT_ADD", "register:40f0:8", ["const:b4c5a0:8", "const:4:8"]]
+ 00b4c5a0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c504 bytes 833a0494
+ 00b4c5a0 bytes 903a0494
- 00b4c50c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4c50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
+ 00b4c5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c50c bytes 600a06f9
+ 00b4c5a8 bytes 608a06f9
- 00b4c4ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4c4ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
+ 00b4c588 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c4ec bytes 680a46f9
+ 00b4c588 bytes 688a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ea57cc2bed5fc53b74318916a170fe"></a>

### [`00b4c520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c520.md) → [`00b4c5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c5bc.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c550",
      "incomplete_value": true,
      "site": "00b4c550",
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
    "old": {
      "definition_site": "00b4c534",
      "incomplete_value": true,
      "site": "00b4c534",
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
    "old": {
      "definition_site": "00b4c53c",
      "incomplete_value": false,
      "site": "00b4c548",
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
            "const:aac:8"
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
      "00b4c5cc",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5d8",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c5ec",
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
      "00b4c5cc",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5d8",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4c5ec",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c520.md#insn-00b4c548) · [`00b4c550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c520.md#insn-00b4c550) · [`00b4c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c520.md#insn-00b4c530)
- 新版 `00b4c5e4`（命令位置の公開資料なし） · `00b4c5ec`（命令位置の公開資料なし） · `00b4c5cc`（命令位置の公開資料なし）

~~~diff
- 00b4c548 ["INT_ADD", "register:40f0:8", ["const:b4c548:8", "const:4:8"]]
- 00b4c548 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c5e4 ["INT_ADD", "register:40f0:8", ["const:b4c5e4:8", "const:4:8"]]
+ 00b4c5e4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c548 bytes 723a0494
+ 00b4c5e4 bytes 7f3a0494
- 00b4c550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4c550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
+ 00b4c5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c550 bytes 600a06f9
+ 00b4c5ec bytes 608a06f9
- 00b4c530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4c530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c5cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
+ 00b4c5cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c530 bytes 680a46f9
+ 00b4c5cc bytes 688a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86c6d48eda8f74416fc24f2ddc31094"></a>

### [`00b4c570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c570.md) → [`00b4c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c60c.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4c5f8",
      "incomplete_value": true,
      "site": "00b4c5f8",
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
    "old": {
      "definition_site": "00b4c5a4",
      "incomplete_value": true,
      "site": "00b4c5b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b4c620",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c640",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c694",
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
      "00b4c620",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c640",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c694",
      "WRITE",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c570.md#insn-00b4c5b0) · [`00b4c5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c570.md#insn-00b4c5f8) · [`00b4c584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c570.md#insn-00b4c584)
- 新版 `00b4c64c`（命令位置の公開資料なし） · `00b4c694`（命令位置の公開資料なし） · `00b4c620`（命令位置の公開資料なし）

~~~diff
- 00b4c5b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c5b0 ["INT_ADD", "register:40f0:8", ["const:b4c5b0:8", "const:4:8"]]
- 00b4c5b0 ["CALLIND", null, ["register:0:8"]]
+ 00b4c64c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c64c ["INT_ADD", "register:40f0:8", ["const:b4c64c:8", "const:4:8"]]
+ 00b4c64c ["CALLIND", null, ["register:0:8"]]
- 00b4c5b0 bytes 00013fd6
+ 00b4c64c bytes 00013fd6
- 00b4c5f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c5f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c18:8"]]
- 00b4c5f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c694 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c694 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d18:8"]]
+ 00b4c694 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c5f8 bytes a0623039
+ 00b4c694 bytes a0623439
- 00b4c584 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c18:8"]]
- 00b4c584 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4c584 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4c620 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d18:8"]]
+ 00b4c620 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c620 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4c584 bytes a8627039
+ 00b4c620 bytes a8627439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdb9cd22779819327025399acb01eb66"></a>

### [`00b4c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c60c.md) → [`00b4c6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c6a8.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4c648",
      "incomplete_value": true,
      "site": "00b4c648",
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
    "old": {
      "definition_site": "00b4c698",
      "incomplete_value": true,
      "site": "00b4c698",
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
    "old": {
      "definition_site": "00b4c624",
      "incomplete_value": true,
      "site": "00b4c624",
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
      "00b4c6bc",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6c8",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c6e4",
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
      "00b4c6bc",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6c8",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c6e4",
      "WRITE",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c60c.md#insn-00b4c648) · [`00b4c694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c60c.md#insn-00b4c694) · [`00b4c698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c60c.md#insn-00b4c698)
- 新版 `00b4c6e4`（命令位置の公開資料なし） · `00b4c730`（命令位置の公開資料なし） · `00b4c734`（命令位置の公開資料なし）

~~~diff
- 00b4c648 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c648 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c648 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c18:8"]]
- 00b4c648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c6e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c6e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c6e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d18:8"]]
+ 00b4c6e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c648 bytes bf623039
+ 00b4c6e4 bytes bf623439
- 00b4c694 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c694 ["INT_ADD", "register:40f0:8", ["const:b4c694:8", "const:4:8"]]
- 00b4c694 ["CALLIND", null, ["register:0:8"]]
+ 00b4c730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c730 ["INT_ADD", "register:40f0:8", ["const:b4c730:8", "const:4:8"]]
+ 00b4c730 ["CALLIND", null, ["register:0:8"]]
- 00b4c694 bytes 00013fd6
+ 00b4c730 bytes 00013fd6
- 00b4c698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4c698 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00b4c734 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c698 bytes 9f0a06f9
+ 00b4c734 bytes 9f8a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e6f85bd109b36490f4a3e9985e10ef"></a>

### [`00b4c6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c6ac.md) → [`00b4c748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c748.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c6ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c788"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c6c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c6c0",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c6c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c78c"
      ]
    ],
    [
      "unmatched:00b4c6d0",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c75c",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c78c"
      ]
    ],
    [
      "00b4c76c",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c6ac.md#insn-00b4c6c8) · [`00b4c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c6ac.md#insn-00b4c6e4) · [`00b4c6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c6ac.md#insn-00b4c6ec)
- 新版 `00b4c780`（命令位置の公開資料なし）

~~~diff
- 00b4c6c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c6c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4c6c8 bytes 410100b5
- 00b4c6e4 ["INT_ADD", "register:40f0:8", ["const:b4c6e4:8", "const:4:8"]]
- 00b4c6e4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c780 ["INT_ADD", "register:40f0:8", ["const:b4c780:8", "const:4:8"]]
+ 00b4c780 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c6e4 bytes 0b3a0494
+ 00b4c780 bytes 183a0494
- 00b4c6ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4c6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c6ec bytes 800a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b118f4bb54669e7e6c0952c7b239af66"></a>

### [`00b4c758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c758.md) → [`00b4c7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7f4.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c798",
      "incomplete_value": true,
      "site": "00b4c798",
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
    "old": {
      "definition_site": "00b4c774",
      "incomplete_value": true,
      "site": "00b4c774",
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
    "old": {
      "definition_site": "00b4c77c",
      "incomplete_value": false,
      "site": "00b4c790",
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
            "const:aac:8"
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
      "00b4c808",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c818",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c834",
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
      "00b4c808",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c818",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4c834",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c758.md#insn-00b4c790) · [`00b4c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c758.md#insn-00b4c798) · [`00b4c76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c758.md#insn-00b4c76c)
- 新版 `00b4c82c`（命令位置の公開資料なし） · `00b4c834`（命令位置の公開資料なし） · `00b4c808`（命令位置の公開資料なし）

~~~diff
- 00b4c790 ["INT_ADD", "register:40f0:8", ["const:b4c790:8", "const:4:8"]]
- 00b4c790 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c82c ["INT_ADD", "register:40f0:8", ["const:b4c82c:8", "const:4:8"]]
+ 00b4c82c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c790 bytes e0390494
+ 00b4c82c bytes ed390494
- 00b4c798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4c798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00b4c834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c798 bytes 800a06f9
+ 00b4c834 bytes 808a06f9
- 00b4c76c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4c76c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00b4c808 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c76c bytes 810a46f9
+ 00b4c808 bytes 818a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d631952c631fdf226e20a9f9f558d60e"></a>

### [`00b4c7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c7c8.md) → [`00b4c864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c864.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4c7e4",
      "incomplete_value": false,
      "site": "00b4c7e8",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4c7f4",
      "incomplete_value": true,
      "site": "00b4c800",
      "value": [
        "LOAD",
        "8",
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
      "00b4c880",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4c890",
      "DATA",
      [
        "storage",
        "01125c30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c880",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c890",
      "DATA",
      [
        "storage",
        "01125d30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c7c8.md#insn-00b4c7e8) · [`00b4c7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c7c8.md#insn-00b4c7e4) · [`00b4c7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c7c8.md#insn-00b4c7f0)
- 新版 `00b4c884`（命令位置の公開資料なし） · `00b4c880`（命令位置の公開資料なし） · `00b4c88c`（命令位置の公開資料なし）

~~~diff
- 00b4c7e8 ["INT_ADD", "register:40f0:8", ["const:b4c7e8:8", "const:4:8"]]
- 00b4c7e8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4c884 ["INT_ADD", "register:40f0:8", ["const:b4c884:8", "const:4:8"]]
+ 00b4c884 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4c7e8 bytes 063a0494
+ 00b4c884 bytes 133a0494
- 00b4c7e4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4c7e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c7e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c7e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c880 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4c880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c7e4 bytes 00781491
+ 00b4c880 bytes 00341591
- 00b4c7f0 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00b4c7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c88c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00b4c88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c7f0 bytes 08c13091
+ 00b4c88c bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-441a8c3b226721ec7db28b09c33f6af8"></a>

### [`00b4c804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c804.md) → [`00b4c8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8a0.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c830",
      "incomplete_value": true,
      "site": "00b4c830",
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
            "const:c38:8"
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
    "old": {
      "definition_site": "00b4c818",
      "incomplete_value": true,
      "site": "00b4c818",
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
    "old": {
      "definition_site": "00b4c824",
      "incomplete_value": false,
      "site": "00b4c828",
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
            "const:5da:8"
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
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8c0",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c8cc",
      "WRITE",
      [
        "storage",
        "01125c38",
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
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8c0",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4c8cc",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c804.md#insn-00b4c828) · [`00b4c830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c804.md#insn-00b4c830) · [`00b4c814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c804.md#insn-00b4c814)
- 新版 `00b4c8c4`（命令位置の公開資料なし） · `00b4c8cc`（命令位置の公開資料なし） · `00b4c8b0`（命令位置の公開資料なし）

~~~diff
- 00b4c828 ["INT_ADD", "register:40f0:8", ["const:b4c828:8", "const:4:8"]]
- 00b4c828 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c8c4 ["INT_ADD", "register:40f0:8", ["const:b4c8c4:8", "const:4:8"]]
+ 00b4c8c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c828 bytes ba390494
+ 00b4c8c4 bytes c7390494
- 00b4c830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c830 bytes 601e06f9
+ 00b4c8cc bytes 609e06f9
- 00b4c814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c8b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c8b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c814 bytes 681e46f9
+ 00b4c8b0 bytes 689e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70ae713f30d2b6485cee296a83a8cace"></a>

### [`00b4c844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c844.md) → [`00b4c8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8e0.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c870",
      "incomplete_value": true,
      "site": "00b4c870",
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
            "const:c38:8"
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
    "old": {
      "definition_site": "00b4c858",
      "incomplete_value": true,
      "site": "00b4c858",
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
    "old": {
      "definition_site": "00b4c860",
      "incomplete_value": false,
      "site": "00b4c868",
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
            "const:5da:8"
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
      "00b4c8f0",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8fc",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c90c",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c8f0",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8fc",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4c90c",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c844.md#insn-00b4c868) · [`00b4c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c844.md#insn-00b4c870) · [`00b4c854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c844.md#insn-00b4c854)
- 新版 `00b4c904`（命令位置の公開資料なし） · `00b4c90c`（命令位置の公開資料なし） · `00b4c8f0`（命令位置の公開資料なし）

~~~diff
- 00b4c868 ["INT_ADD", "register:40f0:8", ["const:b4c868:8", "const:4:8"]]
- 00b4c868 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c904 ["INT_ADD", "register:40f0:8", ["const:b4c904:8", "const:4:8"]]
+ 00b4c904 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c868 bytes aa390494
+ 00b4c904 bytes b7390494
- 00b4c870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c870 bytes 601e06f9
+ 00b4c90c bytes 609e06f9
- 00b4c854 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c8f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c8f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c854 bytes 681e46f9
+ 00b4c8f0 bytes 689e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7346bd6e41db20d222e773c03293dfcb"></a>

### [`00b4c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c884.md) → [`00b4c920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c920.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4c888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c930",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c920",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c924",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c930",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c884.md#insn-00b4c884) · [`00b4c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c884.md#insn-00b4c888) · [`00b4c898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c884.md#insn-00b4c898)
- 新版 `00b4c934`（命令位置の公開資料なし）

~~~diff
- 00b4c884 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4c884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4c884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4c884 bytes f30f1ef8
- 00b4c888 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4c888 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4c888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4c888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c888 bytes fd7b01a9
- 00b4c898 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4c898 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4c934 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4c934 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4c898 bytes 080100b5
+ 00b4c934 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c3321fb2b41e150c529dad187551b93"></a>

### [`00b4c8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c8c8.md) → [`00b4c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c964.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4c8f8",
      "incomplete_value": true,
      "site": "00b4c8f8",
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
            "const:c38:8"
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
    "old": {
      "definition_site": "00b4c8dc",
      "incomplete_value": true,
      "site": "00b4c8dc",
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
    "old": {
      "definition_site": "00b4c8e4",
      "incomplete_value": false,
      "site": "00b4c8f0",
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
            "const:5da:8"
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
      "00b4c974",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c980",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c994",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c974",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c980",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4c994",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c8c8.md#insn-00b4c8f0) · [`00b4c8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c8c8.md#insn-00b4c8f8) · [`00b4c8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c8c8.md#insn-00b4c8d8)
- 新版 `00b4c98c`（命令位置の公開資料なし） · `00b4c994`（命令位置の公開資料なし） · `00b4c974`（命令位置の公開資料なし）

~~~diff
- 00b4c8f0 ["INT_ADD", "register:40f0:8", ["const:b4c8f0:8", "const:4:8"]]
- 00b4c8f0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4c98c ["INT_ADD", "register:40f0:8", ["const:b4c98c:8", "const:4:8"]]
+ 00b4c98c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4c8f0 bytes 88390494
+ 00b4c98c bytes 95390494
- 00b4c8f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c8f8 bytes 601e06f9
+ 00b4c994 bytes 609e06f9
- 00b4c8d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00b4c8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
+ 00b4c974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c8d8 bytes 681e46f9
+ 00b4c974 bytes 689e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be96738b7b86030de070c98b8a430e14"></a>

### [`00b4c918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c918.md) → [`00b4c9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c9b4.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4c9a0",
      "incomplete_value": true,
      "site": "00b4c9a0",
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
            "const:c40:8"
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
    "old": {
      "definition_site": "00b4c94c",
      "incomplete_value": true,
      "site": "00b4c958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
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
      "00b4c9c8",
      "READ",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c9e8",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca3c",
      "WRITE",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c9c8",
      "READ",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c9e8",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca3c",
      "WRITE",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c918.md#insn-00b4c958) · [`00b4c9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c918.md#insn-00b4c9a0) · [`00b4c92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c918.md#insn-00b4c92c)
- 新版 `00b4c9f4`（命令位置の公開資料なし） · `00b4ca3c`（命令位置の公開資料なし） · `00b4c9c8`（命令位置の公開資料なし）

~~~diff
- 00b4c958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c958 ["INT_ADD", "register:40f0:8", ["const:b4c958:8", "const:4:8"]]
- 00b4c958 ["CALLIND", null, ["register:0:8"]]
+ 00b4c9f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c9f4 ["INT_ADD", "register:40f0:8", ["const:b4c9f4:8", "const:4:8"]]
+ 00b4c9f4 ["CALLIND", null, ["register:0:8"]]
- 00b4c958 bytes 00013fd6
+ 00b4c9f4 bytes 00013fd6
- 00b4c9a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c9a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c40:8"]]
- 00b4c9a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ca3c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ca3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d40:8"]]
+ 00b4ca3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c9a0 bytes a0023139
+ 00b4ca3c bytes a0023539
- 00b4c92c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c40:8"]]
- 00b4c92c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4c92c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4c9c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d40:8"]]
+ 00b4c9c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c9c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4c92c bytes a8027139
+ 00b4c9c8 bytes a8027539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa8c03e730ced7f766873144b4704ba5"></a>

### [`00b4c9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c9b4.md) → [`00b4ca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ca50.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4c9f0",
      "incomplete_value": true,
      "site": "00b4c9f0",
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
            "const:c40:8"
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
    "old": {
      "definition_site": "00b4ca40",
      "incomplete_value": true,
      "site": "00b4ca40",
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
            "const:c38:8"
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
    "old": {
      "definition_site": "00b4c9cc",
      "incomplete_value": true,
      "site": "00b4c9cc",
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
      "00b4ca64",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca70",
      "READ",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ca8c",
      "WRITE",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca64",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca70",
      "READ",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ca8c",
      "WRITE",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c9b4.md#insn-00b4c9f0) · [`00b4ca3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c9b4.md#insn-00b4ca3c) · [`00b4ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c9b4.md#insn-00b4ca40)
- 新版 `00b4ca8c`（命令位置の公開資料なし） · `00b4cad8`（命令位置の公開資料なし） · `00b4cadc`（命令位置の公開資料なし）

~~~diff
- 00b4c9f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c9f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c9f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c40:8"]]
- 00b4c9f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4ca8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4ca8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4ca8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d40:8"]]
+ 00b4ca8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c9f0 bytes bf023139
+ 00b4ca8c bytes bf023539
- 00b4ca3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ca3c ["INT_ADD", "register:40f0:8", ["const:b4ca3c:8", "const:4:8"]]
- 00b4ca3c ["CALLIND", null, ["register:0:8"]]
+ 00b4cad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cad8 ["INT_ADD", "register:40f0:8", ["const:b4cad8:8", "const:4:8"]]
+ 00b4cad8 ["CALLIND", null, ["register:0:8"]]
- 00b4ca3c bytes 00013fd6
+ 00b4cad8 bytes 00013fd6
- 00b4ca40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00b4ca40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4ca40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4cadc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
+ 00b4cadc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4cadc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4ca40 bytes 9f1e06f9
+ 00b4cadc bytes 9f9e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eceda8ef8d84e7c6f89b4c4b14dedc2"></a>

### [`00b4ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ca54.md) → [`00b4caf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4caf0.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4ca94",
      "incomplete_value": true,
      "site": "00b4ca94",
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
            "const:c38:8"
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
    "old": {
      "definition_site": "00b4ca70",
      "incomplete_value": true,
      "site": "00b4ca70",
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
    "old": {
      "definition_site": "00b4ca78",
      "incomplete_value": false,
      "site": "00b4ca8c",
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
            "const:5da:8"
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
      "00b4cb04",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb14",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4cb30",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb04",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb14",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4cb30",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ca54.md#insn-00b4ca8c) · [`00b4ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ca54.md#insn-00b4ca94) · [`00b4ca68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ca54.md#insn-00b4ca68)
- 新版 `00b4cb28`（命令位置の公開資料なし） · `00b4cb30`（命令位置の公開資料なし） · `00b4cb04`（命令位置の公開資料なし）

~~~diff
- 00b4ca8c ["INT_ADD", "register:40f0:8", ["const:b4ca8c:8", "const:4:8"]]
- 00b4ca8c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4cb28 ["INT_ADD", "register:40f0:8", ["const:b4cb28:8", "const:4:8"]]
+ 00b4cb28 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ca8c bytes 21390494
+ 00b4cb28 bytes 2e390494
- 00b4ca94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00b4ca94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cb30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
+ 00b4cb30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ca94 bytes 801e06f9
+ 00b4cb30 bytes 809e06f9
- 00b4ca68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00b4ca68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cb04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
+ 00b4cb04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ca68 bytes 811e46f9
+ 00b4cb04 bytes 819e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b61ee7d70af4ec7a81118a7a874e33"></a>

### [`00b4cac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cac4.md) → [`00b4cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb60.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af80.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b050.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4cae0",
      "incomplete_value": false,
      "site": "00b4cae4",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4caf0",
      "incomplete_value": true,
      "site": "00b4cafc",
      "value": [
        "LOAD",
        "8",
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
      "00b4cb7c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4cb8c",
      "DATA",
      [
        "storage",
        "01125c48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb7c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4cb8c",
      "DATA",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cac4.md#insn-00b4cae4) · [`00b4cae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cac4.md#insn-00b4cae0) · [`00b4caec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cac4.md#insn-00b4caec)
- 新版 `00b4cb80`（命令位置の公開資料なし） · `00b4cb7c`（命令位置の公開資料なし） · `00b4cb88`（命令位置の公開資料なし）

~~~diff
- 00b4cae4 ["INT_ADD", "register:40f0:8", ["const:b4cae4:8", "const:4:8"]]
- 00b4cae4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4cb80 ["INT_ADD", "register:40f0:8", ["const:b4cb80:8", "const:4:8"]]
+ 00b4cb80 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4cae4 bytes 47390494
+ 00b4cb80 bytes 54390494
- 00b4cae0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4cae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb7c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4cb7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cb7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cae0 bytes 009c0d91
+ 00b4cb7c bytes 002c0c91
- 00b4caec ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00b4caec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4caec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4caec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4cb88 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00b4cb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4caec bytes 08213191
+ 00b4cb88 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b40aa8b319d6a4bf3f9ced0ed0157c"></a>

### [`00b4cb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb00.md) → [`00b4cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb9c.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cb40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4cbdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cb1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4cb14",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4cb1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cbe0"
      ]
    ],
    [
      "unmatched:00b4cb24",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4cbb0",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cbe0"
      ]
    ],
    [
      "00b4cbc0",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb00.md#insn-00b4cb1c) · [`00b4cb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb00.md#insn-00b4cb38) · [`00b4cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb00.md#insn-00b4cb40)
- 新版 `00b4cbd4`（命令位置の公開資料なし）

~~~diff
- 00b4cb1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4cb1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4cb1c bytes 410100b5
- 00b4cb38 ["INT_ADD", "register:40f0:8", ["const:b4cb38:8", "const:4:8"]]
- 00b4cb38 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4cbd4 ["INT_ADD", "register:40f0:8", ["const:b4cbd4:8", "const:4:8"]]
+ 00b4cbd4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cb38 bytes f6380494
+ 00b4cbd4 bytes 03390494
- 00b4cb40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00b4cb40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cb40 bytes 801e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef701b296bbbedeb4deaac07f2e6612"></a>

### [`00b4cbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbac.md) → [`00b4cc48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4cbd8",
      "incomplete_value": true,
      "site": "00b4cbd8",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4cbc0",
      "incomplete_value": true,
      "site": "00b4cbc0",
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
    "old": {
      "definition_site": "00b4cbcc",
      "incomplete_value": false,
      "site": "00b4cbd0",
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
            "const:b2f:8"
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
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc68",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cc74",
      "WRITE",
      [
        "storage",
        "01125c68",
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
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc68",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4cc74",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbac.md#insn-00b4cbd0) · [`00b4cbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbac.md#insn-00b4cbd8) · [`00b4cbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbac.md#insn-00b4cbbc)
- 新版 `00b4cc6c`（命令位置の公開資料なし） · `00b4cc74`（命令位置の公開資料なし） · `00b4cc58`（命令位置の公開資料なし）

~~~diff
- 00b4cbd0 ["INT_ADD", "register:40f0:8", ["const:b4cbd0:8", "const:4:8"]]
- 00b4cbd0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4cc6c ["INT_ADD", "register:40f0:8", ["const:b4cc6c:8", "const:4:8"]]
+ 00b4cc6c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cbd0 bytes d0380494
+ 00b4cc6c bytes dd380494
- 00b4cbd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
- 00b4cbd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00b4cc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cbd8 bytes 603606f9
+ 00b4cc74 bytes 60b606f9
- 00b4cbbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
- 00b4cbbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cc58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00b4cc58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cbbc bytes 683646f9
+ 00b4cc58 bytes 68b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8446946b01a0f728e754ebfb8697cfd"></a>

### [`00b4cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc2c.md) → [`00b4ccc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

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
    "old": {
      "definition_site": "00b4cc5c",
      "incomplete_value": true,
      "site": "00b4cc5c",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4cc40",
      "incomplete_value": true,
      "site": "00b4cc40",
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
    "old": {
      "definition_site": "00b4cc4c",
      "incomplete_value": false,
      "site": "00b4cc54",
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
            "const:b2f:8"
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
      "00b4ccd8",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cce8",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4ccf8",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ccd8",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cce8",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4ccf8",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc2c.md#insn-00b4cc54) · [`00b4cc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc2c.md#insn-00b4cc5c) · [`00b4cc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc2c.md#insn-00b4cc34)
- 新版 `00b4ccf0`（命令位置の公開資料なし） · `00b4ccf8`（命令位置の公開資料なし）

~~~diff
- 00b4cc54 ["INT_ADD", "register:40f0:8", ["const:b4cc54:8", "const:4:8"]]
- 00b4cc54 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ccf0 ["INT_ADD", "register:40f0:8", ["const:b4ccf0:8", "const:4:8"]]
+ 00b4ccf0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cc54 bytes af380494
+ 00b4ccf0 bytes bc380494
- 00b4cc5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
- 00b4cc5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ccf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00b4ccf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cc5c bytes 603606f9
+ 00b4ccf8 bytes 60b606f9
- 00b4cc34 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00b4cc34 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00b4cc34 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00b4cc34 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00b4cc34 bytes fd430091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a749058eac1e904b0846d3330100bd2"></a>

### [`00b4cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc70.md) → [`00b4cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd0c.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4cca0",
      "incomplete_value": true,
      "site": "00b4cca0",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4cc84",
      "incomplete_value": true,
      "site": "00b4cc84",
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
    "old": {
      "definition_site": "00b4cc8c",
      "incomplete_value": false,
      "site": "00b4cc98",
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
            "const:b2f:8"
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
      "00b4cd1c",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd28",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cd3c",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd1c",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd28",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4cd3c",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc70.md#insn-00b4cc98) · [`00b4cca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc70.md#insn-00b4cca0) · [`00b4cc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc70.md#insn-00b4cc80)
- 新版 `00b4cd34`（命令位置の公開資料なし） · `00b4cd3c`（命令位置の公開資料なし） · `00b4cd1c`（命令位置の公開資料なし）

~~~diff
- 00b4cc98 ["INT_ADD", "register:40f0:8", ["const:b4cc98:8", "const:4:8"]]
- 00b4cc98 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4cd34 ["INT_ADD", "register:40f0:8", ["const:b4cd34:8", "const:4:8"]]
+ 00b4cd34 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cc98 bytes 9e380494
+ 00b4cd34 bytes ab380494
- 00b4cca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
- 00b4cca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00b4cd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cca0 bytes 603606f9
+ 00b4cd3c bytes 60b606f9
- 00b4cc80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
- 00b4cc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cd1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00b4cd1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cc80 bytes 683646f9
+ 00b4cd1c bytes 68b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce2f0d71dc305d19757858f6dea186be"></a>

### [`00b4ccc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ccc0.md) → [`00b4cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd5c.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4cd48",
      "incomplete_value": true,
      "site": "00b4cd48",
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
            "const:c70:8"
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
    "old": {
      "definition_site": "00b4ccf4",
      "incomplete_value": true,
      "site": "00b4cd00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c68:8"
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
      "00b4cd70",
      "READ",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cd90",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cde4",
      "WRITE",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd70",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cd90",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cde4",
      "WRITE",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ccc0.md#insn-00b4cd00) · [`00b4cd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ccc0.md#insn-00b4cd48) · [`00b4ccd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ccc0.md#insn-00b4ccd4)
- 新版 `00b4cd9c`（命令位置の公開資料なし） · `00b4cde4`（命令位置の公開資料なし） · `00b4cd70`（命令位置の公開資料なし）

~~~diff
- 00b4cd00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cd00 ["INT_ADD", "register:40f0:8", ["const:b4cd00:8", "const:4:8"]]
- 00b4cd00 ["CALLIND", null, ["register:0:8"]]
+ 00b4cd9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cd9c ["INT_ADD", "register:40f0:8", ["const:b4cd9c:8", "const:4:8"]]
+ 00b4cd9c ["CALLIND", null, ["register:0:8"]]
- 00b4cd00 bytes 00013fd6
+ 00b4cd9c bytes 00013fd6
- 00b4cd48 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4cd48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c70:8"]]
- 00b4cd48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4cde4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4cde4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d70:8"]]
+ 00b4cde4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4cd48 bytes a0c23139
+ 00b4cde4 bytes a0c23539
- 00b4ccd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c70:8"]]
- 00b4ccd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4ccd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4cd70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
+ 00b4cd70 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cd70 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4ccd4 bytes a8c27139
+ 00b4cd70 bytes a8c27539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36cfb2ae0e9d1adeb11782281570a403"></a>

### [`00b4cd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cd5c.md) → [`00b4cdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4cd98",
      "incomplete_value": true,
      "site": "00b4cd98",
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
            "const:c70:8"
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
    "old": {
      "definition_site": "00b4cde8",
      "incomplete_value": true,
      "site": "00b4cde8",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4cd74",
      "incomplete_value": true,
      "site": "00b4cd74",
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
      "00b4ce0c",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce18",
      "READ",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ce34",
      "WRITE",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce0c",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce18",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ce34",
      "WRITE",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cd5c.md#insn-00b4cd98) · [`00b4cde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cd5c.md#insn-00b4cde4) · [`00b4cde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cd5c.md#insn-00b4cde8)
- 新版 `00b4ce34`（命令位置の公開資料なし） · `00b4ce80`（命令位置の公開資料なし） · `00b4ce84`（命令位置の公開資料なし）

~~~diff
- 00b4cd98 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4cd98 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4cd98 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c70:8"]]
- 00b4cd98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4ce34 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4ce34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4ce34 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d70:8"]]
+ 00b4ce34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4cd98 bytes bfc23139
+ 00b4ce34 bytes bfc23539
- 00b4cde4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cde4 ["INT_ADD", "register:40f0:8", ["const:b4cde4:8", "const:4:8"]]
- 00b4cde4 ["CALLIND", null, ["register:0:8"]]
+ 00b4ce80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ce80 ["INT_ADD", "register:40f0:8", ["const:b4ce80:8", "const:4:8"]]
+ 00b4ce80 ["CALLIND", null, ["register:0:8"]]
- 00b4cde4 bytes 00013fd6
+ 00b4ce80 bytes 00013fd6
- 00b4cde8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
- 00b4cde8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4cde8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4ce84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00b4ce84 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4ce84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4cde8 bytes 9f3606f9
+ 00b4ce84 bytes 9fb606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5fa6d12cd4efd41397031040e9178bb"></a>

### [`00b4cdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cdfc.md) → [`00b4ce98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
    "old": {
      "definition_site": "00b4ce3c",
      "incomplete_value": true,
      "site": "00b4ce3c",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4ce18",
      "incomplete_value": true,
      "site": "00b4ce18",
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
    "old": {
      "definition_site": "00b4ce20",
      "incomplete_value": false,
      "site": "00b4ce34",
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
            "const:b2f:8"
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
      "00b4ceac",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cebc",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4ced8",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ceac",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cebc",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4ced8",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cdfc.md#insn-00b4ce34) · [`00b4ce3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cdfc.md#insn-00b4ce3c) · [`00b4ce10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cdfc.md#insn-00b4ce10)
- 新版 `00b4ced0`（命令位置の公開資料なし） · `00b4ced8`（命令位置の公開資料なし） · `00b4ceac`（命令位置の公開資料なし）

~~~diff
- 00b4ce34 ["INT_ADD", "register:40f0:8", ["const:b4ce34:8", "const:4:8"]]
- 00b4ce34 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ced0 ["INT_ADD", "register:40f0:8", ["const:b4ced0:8", "const:4:8"]]
+ 00b4ced0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ce34 bytes 37380494
+ 00b4ced0 bytes 44380494
- 00b4ce3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
- 00b4ce3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ced8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00b4ced8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ce3c bytes 803606f9
+ 00b4ced8 bytes 80b606f9
- 00b4ce10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
- 00b4ce10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ceac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00b4ceac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ce10 bytes 813646f9
+ 00b4ceac bytes 81b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baad69a1daefd18dc8bf0fa4c8d2f355"></a>

### [`00b4ce6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ce6c.md) → [`00b4cf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4ce88",
      "incomplete_value": false,
      "site": "00b4ce8c",
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
            "const:367:8"
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
    "old": {
      "definition_site": "00b4ce98",
      "incomplete_value": true,
      "site": "00b4cea4",
      "value": [
        "LOAD",
        "8",
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
      "00b4cf24",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4cf34",
      "DATA",
      [
        "storage",
        "01125c78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cf24",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4cf34",
      "DATA",
      [
        "storage",
        "01125d78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ce6c.md#insn-00b4ce8c) · [`00b4ce88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ce6c.md#insn-00b4ce88) · [`00b4ce94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ce6c.md#insn-00b4ce94)
- 新版 `00b4cf28`（命令位置の公開資料なし） · `00b4cf24`（命令位置の公開資料なし） · `00b4cf30`（命令位置の公開資料なし）

~~~diff
- 00b4ce8c ["INT_ADD", "register:40f0:8", ["const:b4ce8c:8", "const:4:8"]]
- 00b4ce8c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4cf28 ["INT_ADD", "register:40f0:8", ["const:b4cf28:8", "const:4:8"]]
+ 00b4cf28 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4ce8c bytes 5d380494
+ 00b4cf28 bytes 6a380494
- 00b4ce88 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4ce88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ce88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ce88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf24 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4cf24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ce88 bytes 009c0d91
+ 00b4cf24 bytes 002c0c91
- 00b4ce94 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00b4ce94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ce94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ce94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf30 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00b4cf30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4ce94 bytes 08e13191
+ 00b4cf30 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a617a6e078d70d434b4a717d1e85d1"></a>

### [`00b4cea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cea8.md) → [`00b4cf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf44.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4cee8",
      "incomplete_value": true,
      "site": "00b4cee8",
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
            "const:c68:8"
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
    "old": {
      "definition_site": "00b4cec4",
      "incomplete_value": true,
      "site": "00b4cec4",
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
    "old": {
      "definition_site": "00b4cecc",
      "incomplete_value": false,
      "site": "00b4cee0",
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
            "const:b2f:8"
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
      "00b4cf58",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf68",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cf84",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cf58",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf68",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4cf84",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cea8.md#insn-00b4cee0) · [`00b4cee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cea8.md#insn-00b4cee8) · [`00b4cebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cea8.md#insn-00b4cebc)
- 新版 `00b4cf7c`（命令位置の公開資料なし） · `00b4cf84`（命令位置の公開資料なし） · `00b4cf58`（命令位置の公開資料なし）

~~~diff
- 00b4cee0 ["INT_ADD", "register:40f0:8", ["const:b4cee0:8", "const:4:8"]]
- 00b4cee0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4cf7c ["INT_ADD", "register:40f0:8", ["const:b4cf7c:8", "const:4:8"]]
+ 00b4cf7c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cee0 bytes 0c380494
+ 00b4cf7c bytes 19380494
- 00b4cee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
- 00b4cee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cf84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00b4cf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cee8 bytes 803606f9
+ 00b4cf84 bytes 80b606f9
- 00b4cebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
- 00b4cebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cf58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00b4cf58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cebc bytes 813646f9
+ 00b4cf58 bytes 81b646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4050532784a66b347a1d1581a8a09f27"></a>

### [`00b4cf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf18.md) → [`00b4cfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cfb4.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
    "old": {
      "definition_site": "00b4cf34",
      "incomplete_value": false,
      "site": "00b4cf38",
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
            "const:51e:8"
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
    "old": {
      "definition_site": "00b4cf44",
      "incomplete_value": true,
      "site": "00b4cf50",
      "value": [
        "LOAD",
        "8",
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
      "00b4cfd0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4cfe0",
      "DATA",
      [
        "storage",
        "01125c80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cfd0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4cfe0",
      "DATA",
      [
        "storage",
        "01125d80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf18.md#insn-00b4cf38) · [`00b4cf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf18.md#insn-00b4cf34) · [`00b4cf40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf18.md#insn-00b4cf40)
- 新版 `00b4cfd4`（命令位置の公開資料なし） · `00b4cfd0`（命令位置の公開資料なし） · `00b4cfdc`（命令位置の公開資料なし）

~~~diff
- 00b4cf38 ["INT_ADD", "register:40f0:8", ["const:b4cf38:8", "const:4:8"]]
- 00b4cf38 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4cfd4 ["INT_ADD", "register:40f0:8", ["const:b4cfd4:8", "const:4:8"]]
+ 00b4cfd4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4cf38 bytes 32380494
+ 00b4cfd4 bytes 3f380494
- 00b4cf34 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4cf34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cf34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cf34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cfd0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4cfd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cfd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cfd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cf34 bytes 00781491
+ 00b4cfd0 bytes 00341591
- 00b4cf40 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 00b4cf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4cfdc ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00b4cfdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cfdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cfdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4cf40 bytes 08013291
+ 00b4cfdc bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9e8a7e2d68ca49fcd7289e4f54d129"></a>

### [`00b4cf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf54.md) → [`00b4cff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cff0.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4cf80",
      "incomplete_value": true,
      "site": "00b4cf80",
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
            "const:c88:8"
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
    "old": {
      "definition_site": "00b4cf68",
      "incomplete_value": true,
      "site": "00b4cf68",
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
    "old": {
      "definition_site": "00b4cf74",
      "incomplete_value": false,
      "site": "00b4cf78",
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
            "const:587:8"
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
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d010",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d01c",
      "WRITE",
      [
        "storage",
        "01125c88",
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
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d010",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d01c",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf54.md#insn-00b4cf78) · [`00b4cf80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf54.md#insn-00b4cf80) · [`00b4cf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf54.md#insn-00b4cf64)
- 新版 `00b4d014`（命令位置の公開資料なし） · `00b4d01c`（命令位置の公開資料なし） · `00b4d000`（命令位置の公開資料なし）

~~~diff
- 00b4cf78 ["INT_ADD", "register:40f0:8", ["const:b4cf78:8", "const:4:8"]]
- 00b4cf78 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d014 ["INT_ADD", "register:40f0:8", ["const:b4d014:8", "const:4:8"]]
+ 00b4d014 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cf78 bytes e6370494
+ 00b4d014 bytes f3370494
- 00b4cf80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4cf80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d01c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cf80 bytes 604606f9
+ 00b4d01c bytes 60c606f9
- 00b4cf64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4cf64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d000 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d000 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cf64 bytes 684646f9
+ 00b4d000 bytes 68c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6b6ad3053c50993132733688fca979"></a>

### [`00b4cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf94.md) → [`00b4d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d030.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4cfc0",
      "incomplete_value": true,
      "site": "00b4cfc0",
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
            "const:c88:8"
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
    "old": {
      "definition_site": "00b4cfa8",
      "incomplete_value": true,
      "site": "00b4cfa8",
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
    "old": {
      "definition_site": "00b4cfb0",
      "incomplete_value": false,
      "site": "00b4cfb8",
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
            "const:587:8"
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
      "00b4d040",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d04c",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d05c",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d040",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d04c",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d05c",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf94.md#insn-00b4cfb8) · [`00b4cfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf94.md#insn-00b4cfc0) · [`00b4cfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf94.md#insn-00b4cfa4)
- 新版 `00b4d054`（命令位置の公開資料なし） · `00b4d05c`（命令位置の公開資料なし） · `00b4d040`（命令位置の公開資料なし）

~~~diff
- 00b4cfb8 ["INT_ADD", "register:40f0:8", ["const:b4cfb8:8", "const:4:8"]]
- 00b4cfb8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d054 ["INT_ADD", "register:40f0:8", ["const:b4d054:8", "const:4:8"]]
+ 00b4d054 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cfb8 bytes d6370494
+ 00b4d054 bytes e3370494
- 00b4cfc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4cfc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cfc0 bytes 604606f9
+ 00b4d05c bytes 60c606f9
- 00b4cfa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4cfa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d040 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cfa4 bytes 684646f9
+ 00b4d040 bytes 68c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-832fd39fde7866701fe0c6d6e4ceb9f8"></a>

### [`00b4cfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md) → [`00b4d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d070.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4d004",
      "incomplete_value": true,
      "site": "00b4d004",
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
            "const:c88:8"
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
    "old": {
      "definition_site": "00b4cfe8",
      "incomplete_value": true,
      "site": "00b4cfe8",
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
    "old": {
      "definition_site": "00b4cff4",
      "incomplete_value": false,
      "site": "00b4cffc",
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
            "const:587:8"
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
      "00b4d080",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d090",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d0a0",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d080",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d090",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d0a0",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md#insn-00b4cffc) · [`00b4d004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md#insn-00b4d004) · [`00b4cfe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md#insn-00b4cfe4)
- 新版 `00b4d098`（命令位置の公開資料なし） · `00b4d0a0`（命令位置の公開資料なし） · `00b4d080`（命令位置の公開資料なし）

~~~diff
- 00b4cffc ["INT_ADD", "register:40f0:8", ["const:b4cffc:8", "const:4:8"]]
- 00b4cffc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d098 ["INT_ADD", "register:40f0:8", ["const:b4d098:8", "const:4:8"]]
+ 00b4d098 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4cffc bytes c5370494
+ 00b4d098 bytes d2370494
- 00b4d004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4d004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d004 bytes 604606f9
+ 00b4d0a0 bytes 60c606f9
- 00b4cfe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4cfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cfe4 bytes 684646f9
+ 00b4d080 bytes 68c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bac4d22bf6d26b1f4bda0a05b592c93"></a>

### [`00b4d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d018.md) → [`00b4d0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d0b4.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
    "old": {
      "definition_site": "00b4d048",
      "incomplete_value": true,
      "site": "00b4d048",
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
            "const:c88:8"
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
    "old": {
      "definition_site": "00b4d02c",
      "incomplete_value": true,
      "site": "00b4d02c",
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
    "old": {
      "definition_site": "00b4d034",
      "incomplete_value": false,
      "site": "00b4d040",
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
            "const:587:8"
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
      "00b4d0c4",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0d0",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d0e4",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d0c4",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0d0",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d0e4",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d018.md#insn-00b4d040) · [`00b4d048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d018.md#insn-00b4d048) · [`00b4d028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d018.md#insn-00b4d028)
- 新版 `00b4d0dc`（命令位置の公開資料なし） · `00b4d0e4`（命令位置の公開資料なし） · `00b4d0c4`（命令位置の公開資料なし）

~~~diff
- 00b4d040 ["INT_ADD", "register:40f0:8", ["const:b4d040:8", "const:4:8"]]
- 00b4d040 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d0dc ["INT_ADD", "register:40f0:8", ["const:b4d0dc:8", "const:4:8"]]
+ 00b4d0dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d040 bytes b4370494
+ 00b4d0dc bytes c1370494
- 00b4d048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4d048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d048 bytes 604606f9
+ 00b4d0e4 bytes 60c606f9
- 00b4d028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00b4d028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00b4d0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d028 bytes 684646f9
+ 00b4d0c4 bytes 68c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e84f9bc23da808ceb21a85a7690617f1"></a>

### [`00b4d068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d068.md) → [`00b4d104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d104.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00b4d0f0",
      "incomplete_value": true,
      "site": "00b4d0f0",
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
            "const:c90:8"
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
    "old": {
      "definition_site": "00b4d09c",
      "incomplete_value": true,
      "site": "00b4d0a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "00b4d118",
      "READ",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d138",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d18c",
      "WRITE",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d118",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d138",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d18c",
      "WRITE",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d068.md#insn-00b4d0a8) · [`00b4d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d068.md#insn-00b4d0f0) · [`00b4d07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d068.md#insn-00b4d07c)
- 新版 `00b4d144`（命令位置の公開資料なし） · `00b4d18c`（命令位置の公開資料なし） · `00b4d118`（命令位置の公開資料なし）

~~~diff
- 00b4d0a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d0a8 ["INT_ADD", "register:40f0:8", ["const:b4d0a8:8", "const:4:8"]]
- 00b4d0a8 ["CALLIND", null, ["register:0:8"]]
+ 00b4d144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d144 ["INT_ADD", "register:40f0:8", ["const:b4d144:8", "const:4:8"]]
+ 00b4d144 ["CALLIND", null, ["register:0:8"]]
- 00b4d0a8 bytes 00013fd6
+ 00b4d144 bytes 00013fd6
- 00b4d0f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d0f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c90:8"]]
- 00b4d0f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d18c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d18c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d90:8"]]
+ 00b4d18c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d0f0 bytes a0423239
+ 00b4d18c bytes a0423639
- 00b4d07c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c90:8"]]
- 00b4d07c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d07c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d118 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d90:8"]]
+ 00b4d118 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d118 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d07c bytes a8427239
+ 00b4d118 bytes a8427639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb749056d6b21d1d984b236b7e08c44f"></a>

### [`00b4d104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md) → [`00b4d1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d1a0.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4d1dc",
      "incomplete_value": true,
      "site": "00b4d1dc",
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
    "old": {
      "definition_site": "00b4d140",
      "incomplete_value": true,
      "site": "00b4d140",
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
            "const:c90:8"
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
      "definition_site": "00b4d22c",
      "incomplete_value": true,
      "site": "00b4d22c",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d190",
      "incomplete_value": true,
      "site": "00b4d190",
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
            "const:c88:8"
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
      "definition_site": "00b4d1b8",
      "incomplete_value": true,
      "site": "00b4d1b8",
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
      "definition_site": "00b4d11c",
      "incomplete_value": true,
      "site": "00b4d11c",
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
      "00b4d1b4",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1c0",
      "READ",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d1dc",
      "WRITE",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d1b4",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1c0",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d1dc",
      "WRITE",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md#insn-00b4d140) · [`00b4d18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md#insn-00b4d18c) · [`00b4d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md#insn-00b4d190)
- 新版 `00b4d1dc`（命令位置の公開資料なし） · `00b4d228`（命令位置の公開資料なし） · `00b4d22c`（命令位置の公開資料なし）

~~~diff
- 00b4d140 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d140 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d140 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c90:8"]]
- 00b4d140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d1dc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d1dc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d1dc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d90:8"]]
+ 00b4d1dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d140 bytes bf423239
+ 00b4d1dc bytes bf423639
- 00b4d18c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d18c ["INT_ADD", "register:40f0:8", ["const:b4d18c:8", "const:4:8"]]
- 00b4d18c ["CALLIND", null, ["register:0:8"]]
+ 00b4d228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d228 ["INT_ADD", "register:40f0:8", ["const:b4d228:8", "const:4:8"]]
+ 00b4d228 ["CALLIND", null, ["register:0:8"]]
- 00b4d18c bytes 00013fd6
+ 00b4d228 bytes 00013fd6
- 00b4d190 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00b4d190 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d22c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b4d22c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d22c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d190 bytes 9f4606f9
+ 00b4d22c bytes 9fc606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e2182368af0a8469353eaf062eaa8d1"></a>

### [`00b4d1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d1a4.md) → [`00b4d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d240.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4d280",
      "incomplete_value": true,
      "site": "00b4d280",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d1e4",
      "incomplete_value": true,
      "site": "00b4d1e4",
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
            "const:c88:8"
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
      "definition_site": "00b4d25c",
      "incomplete_value": true,
      "site": "00b4d25c",
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
      "definition_site": "00b4d1c0",
      "incomplete_value": true,
      "site": "00b4d1c0",
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
      "definition_site": "00b4d264",
      "incomplete_value": false,
      "site": "00b4d278",
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
    "old": {
      "definition_site": "00b4d1c8",
      "incomplete_value": false,
      "site": "00b4d1dc",
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
            "const:587:8"
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
      "00b4d254",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d264",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d280",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d254",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d264",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d280",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d1a4.md#insn-00b4d1dc) · [`00b4d1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d1a4.md#insn-00b4d1e4) · [`00b4d1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d1a4.md#insn-00b4d1b8)
- 新版 `00b4d278`（命令位置の公開資料なし） · `00b4d280`（命令位置の公開資料なし） · `00b4d254`（命令位置の公開資料なし）

~~~diff
- 00b4d1dc ["INT_ADD", "register:40f0:8", ["const:b4d1dc:8", "const:4:8"]]
- 00b4d1dc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d278 ["INT_ADD", "register:40f0:8", ["const:b4d278:8", "const:4:8"]]
+ 00b4d278 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d1dc bytes 4d370494
+ 00b4d278 bytes 5a370494
- 00b4d1e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00b4d1e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b4d280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d1e4 bytes 804606f9
+ 00b4d280 bytes 80c606f9
- 00b4d1b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00b4d1b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d254 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b4d254 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d1b8 bytes 814646f9
+ 00b4d254 bytes 81c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6e23341ef82ed3160e3d5e55f5b899"></a>

### [`00b4d214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d214.md) → [`00b4d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d2b0.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b500.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5d0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4d2cc",
      "incomplete_value": false,
      "site": "00b4d2d0",
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
    "old": {
      "definition_site": "00b4d230",
      "incomplete_value": false,
      "site": "00b4d234",
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
            "const:367:8"
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
      "definition_site": "00b4d2dc",
      "incomplete_value": true,
      "site": "00b4d2e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d240",
      "incomplete_value": true,
      "site": "00b4d24c",
      "value": [
        "LOAD",
        "8",
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
      "00b4d2cc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4d2dc",
      "DATA",
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
      "00b4d2cc",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4d2dc",
      "DATA",
      [
        "storage",
        "01125d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d214.md#insn-00b4d234) · [`00b4d230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d214.md#insn-00b4d230) · [`00b4d23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d214.md#insn-00b4d23c)
- 新版 `00b4d2d0`（命令位置の公開資料なし） · `00b4d2cc`（命令位置の公開資料なし） · `00b4d2d8`（命令位置の公開資料なし）

~~~diff
- 00b4d234 ["INT_ADD", "register:40f0:8", ["const:b4d234:8", "const:4:8"]]
- 00b4d234 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4d2d0 ["INT_ADD", "register:40f0:8", ["const:b4d2d0:8", "const:4:8"]]
+ 00b4d2d0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4d234 bytes 73370494
+ 00b4d2d0 bytes 80370494
- 00b4d230 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4d230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2cc ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4d2cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d230 bytes 009c0d91
+ 00b4d2cc bytes 002c0c91
- 00b4d23c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00b4d23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2d8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00b4d2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d23c bytes 08613291
+ 00b4d2d8 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b90b305d64729bdf63e921deeb8556"></a>

### [`00b4d250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d250.md) → [`00b4d2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d2ec.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d32c",
      "incomplete_value": true,
      "site": "00b4d32c",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d290",
      "incomplete_value": true,
      "site": "00b4d290",
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
            "const:c88:8"
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
      "definition_site": "00b4d308",
      "incomplete_value": true,
      "site": "00b4d308",
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
      "definition_site": "00b4d26c",
      "incomplete_value": true,
      "site": "00b4d26c",
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
      "definition_site": "00b4d310",
      "incomplete_value": false,
      "site": "00b4d324",
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
    "old": {
      "definition_site": "00b4d274",
      "incomplete_value": false,
      "site": "00b4d288",
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
            "const:587:8"
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
      "00b4d300",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d310",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d32c",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d300",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d310",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4d32c",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d250.md#insn-00b4d288) · [`00b4d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d250.md#insn-00b4d290) · [`00b4d264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d250.md#insn-00b4d264)
- 新版 `00b4d324`（命令位置の公開資料なし） · `00b4d32c`（命令位置の公開資料なし） · `00b4d300`（命令位置の公開資料なし）

~~~diff
- 00b4d288 ["INT_ADD", "register:40f0:8", ["const:b4d288:8", "const:4:8"]]
- 00b4d288 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d324 ["INT_ADD", "register:40f0:8", ["const:b4d324:8", "const:4:8"]]
+ 00b4d324 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d288 bytes 22370494
+ 00b4d324 bytes 2f370494
- 00b4d290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00b4d290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d32c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b4d32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d290 bytes 804606f9
+ 00b4d32c bytes 80c606f9
- 00b4d264 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
- 00b4d264 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00b4d300 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d264 bytes 814646f9
+ 00b4d300 bytes 81c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4eb4d7636b38a76434892813211cab"></a>

### [`00b4d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2c0.md) → [`00b4d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d35c.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4d378",
      "incomplete_value": false,
      "site": "00b4d37c",
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
    "old": {
      "definition_site": "00b4d2dc",
      "incomplete_value": false,
      "site": "00b4d2e0",
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
            "const:51e:8"
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
      "definition_site": "00b4d388",
      "incomplete_value": true,
      "site": "00b4d394",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d2ec",
      "incomplete_value": true,
      "site": "00b4d2f8",
      "value": [
        "LOAD",
        "8",
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
      "00b4d378",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4d388",
      "DATA",
      [
        "storage",
        "01125ca0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d378",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4d388",
      "DATA",
      [
        "storage",
        "01125da0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2c0.md#insn-00b4d2e0) · [`00b4d2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2c0.md#insn-00b4d2dc) · [`00b4d2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2c0.md#insn-00b4d2e8)
- 新版 `00b4d37c`（命令位置の公開資料なし） · `00b4d378`（命令位置の公開資料なし） · `00b4d384`（命令位置の公開資料なし）

~~~diff
- 00b4d2e0 ["INT_ADD", "register:40f0:8", ["const:b4d2e0:8", "const:4:8"]]
- 00b4d2e0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4d37c ["INT_ADD", "register:40f0:8", ["const:b4d37c:8", "const:4:8"]]
+ 00b4d37c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4d2e0 bytes 48370494
+ 00b4d37c bytes 55370494
- 00b4d2dc ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4d2dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d2dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d2dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d378 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4d378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d2dc bytes 00781491
+ 00b4d378 bytes 00341591
- 00b4d2e8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00b4d2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d384 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00b4d384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d2e8 bytes 08813291
+ 00b4d384 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae9c9296f057bb78369116244d22020"></a>

### [`00b4d2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2fc.md) → [`00b4d398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d398.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d3c4",
      "incomplete_value": true,
      "site": "00b4d3c4",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d328",
      "incomplete_value": true,
      "site": "00b4d328",
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
            "const:ca8:8"
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
      "definition_site": "00b4d3ac",
      "incomplete_value": true,
      "site": "00b4d3ac",
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
      "definition_site": "00b4d310",
      "incomplete_value": true,
      "site": "00b4d310",
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
      "site": "00b4d3bc",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d31c",
      "incomplete_value": false,
      "site": "00b4d320",
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
            "const:81a:8"
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
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3b8",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d3c4",
      "WRITE",
      [
        "storage",
        "01125ca8",
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
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3b8",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d3c4",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2fc.md#insn-00b4d320) · [`00b4d328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2fc.md#insn-00b4d328) · [`00b4d30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2fc.md#insn-00b4d30c)
- 新版 `00b4d3bc`（命令位置の公開資料なし） · `00b4d3c4`（命令位置の公開資料なし） · `00b4d3a8`（命令位置の公開資料なし）

~~~diff
- 00b4d320 ["INT_ADD", "register:40f0:8", ["const:b4d320:8", "const:4:8"]]
- 00b4d320 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d3bc ["INT_ADD", "register:40f0:8", ["const:b4d3bc:8", "const:4:8"]]
+ 00b4d3bc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d320 bytes fc360494
+ 00b4d3bc bytes 09370494
- 00b4d328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d3c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d328 bytes 605606f9
+ 00b4d3c4 bytes 60d606f9
- 00b4d30c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d30c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d3a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d3a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d30c bytes 685646f9
+ 00b4d3a8 bytes 68d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c81ca50879e5d6b892f114090da3ead"></a>

### [`00b4d33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d33c.md) → [`00b4d3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d3d8.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d404",
      "incomplete_value": true,
      "site": "00b4d404",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d368",
      "incomplete_value": true,
      "site": "00b4d368",
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
            "const:ca8:8"
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
      "definition_site": "00b4d3ec",
      "incomplete_value": true,
      "site": "00b4d3ec",
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
      "definition_site": "00b4d350",
      "incomplete_value": true,
      "site": "00b4d350",
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
      "definition_site": "00b4d3f4",
      "incomplete_value": false,
      "site": "00b4d3fc",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d358",
      "incomplete_value": false,
      "site": "00b4d360",
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
            "const:81a:8"
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
      "00b4d3e8",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3f4",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d404",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d3e8",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3f4",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d404",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d33c.md#insn-00b4d360) · [`00b4d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d33c.md#insn-00b4d368) · [`00b4d34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d33c.md#insn-00b4d34c)
- 新版 `00b4d3fc`（命令位置の公開資料なし） · `00b4d404`（命令位置の公開資料なし） · `00b4d3e8`（命令位置の公開資料なし）

~~~diff
- 00b4d360 ["INT_ADD", "register:40f0:8", ["const:b4d360:8", "const:4:8"]]
- 00b4d360 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d3fc ["INT_ADD", "register:40f0:8", ["const:b4d3fc:8", "const:4:8"]]
+ 00b4d3fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d360 bytes ec360494
+ 00b4d3fc bytes f9360494
- 00b4d368 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d368 bytes 605606f9
+ 00b4d404 bytes 60d606f9
- 00b4d34c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d34c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d3e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d3e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d34c bytes 685646f9
+ 00b4d3e8 bytes 68d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9aeaa15e4902948956d835fd6cd31c8"></a>

### [`00b4d37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d37c.md) → [`00b4d418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d418.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d448",
      "incomplete_value": true,
      "site": "00b4d448",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d3ac",
      "incomplete_value": true,
      "site": "00b4d3ac",
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
            "const:ca8:8"
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
      "definition_site": "00b4d42c",
      "incomplete_value": true,
      "site": "00b4d42c",
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
      "definition_site": "00b4d390",
      "incomplete_value": true,
      "site": "00b4d390",
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
      "definition_site": "00b4d438",
      "incomplete_value": false,
      "site": "00b4d440",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d39c",
      "incomplete_value": false,
      "site": "00b4d3a4",
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
            "const:81a:8"
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
      "00b4d428",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d438",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d448",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d428",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d438",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d448",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d3a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d37c.md#insn-00b4d3a4) · [`00b4d3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d37c.md#insn-00b4d3ac) · [`00b4d38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d37c.md#insn-00b4d38c)
- 新版 `00b4d440`（命令位置の公開資料なし） · `00b4d448`（命令位置の公開資料なし） · `00b4d428`（命令位置の公開資料なし）

~~~diff
- 00b4d3a4 ["INT_ADD", "register:40f0:8", ["const:b4d3a4:8", "const:4:8"]]
- 00b4d3a4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d440 ["INT_ADD", "register:40f0:8", ["const:b4d440:8", "const:4:8"]]
+ 00b4d440 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d3a4 bytes db360494
+ 00b4d440 bytes e8360494
- 00b4d3ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d3ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d3ac bytes 605606f9
+ 00b4d448 bytes 60d606f9
- 00b4d38c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d38c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d428 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d38c bytes 685646f9
+ 00b4d428 bytes 68d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149981aebb795d65cb2ca64a4e0fcdaf"></a>

### [`00b4d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d3c0.md) → [`00b4d45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d45c.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4d48c",
      "incomplete_value": true,
      "site": "00b4d48c",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d3f0",
      "incomplete_value": true,
      "site": "00b4d3f0",
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
            "const:ca8:8"
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
      "definition_site": "00b4d470",
      "incomplete_value": true,
      "site": "00b4d470",
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
      "definition_site": "00b4d3d4",
      "incomplete_value": true,
      "site": "00b4d3d4",
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
      "definition_site": "00b4d478",
      "incomplete_value": false,
      "site": "00b4d484",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d3dc",
      "incomplete_value": false,
      "site": "00b4d3e8",
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
            "const:81a:8"
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
      "00b4d46c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d478",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d48c",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d46c",
      "READ",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d478",
      "PARAM",
      [
        "storage",
        "002bf7c6",
        null,
        "string"
      ]
    ],
    [
      "00b4d48c",
      "WRITE",
      [
        "storage",
        "01125da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d3c0.md#insn-00b4d3e8) · [`00b4d3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d3c0.md#insn-00b4d3f0) · [`00b4d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d3c0.md#insn-00b4d3d0)
- 新版 `00b4d484`（命令位置の公開資料なし） · `00b4d48c`（命令位置の公開資料なし） · `00b4d46c`（命令位置の公開資料なし）

~~~diff
- 00b4d3e8 ["INT_ADD", "register:40f0:8", ["const:b4d3e8:8", "const:4:8"]]
- 00b4d3e8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4d484 ["INT_ADD", "register:40f0:8", ["const:b4d484:8", "const:4:8"]]
+ 00b4d484 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4d3e8 bytes ca360494
+ 00b4d484 bytes d7360494
- 00b4d3f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d3f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d48c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d3f0 bytes 605606f9
+ 00b4d48c bytes 60d606f9
- 00b4d3d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
- 00b4d3d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d46c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:da8:8"]]
+ 00b4d46c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d3d0 bytes 685646f9
+ 00b4d46c bytes 68d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

