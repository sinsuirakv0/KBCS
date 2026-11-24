# v16.0.1 → v16.0.2 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-02f4cd3c0af75389ebbf18aa4675677b"></a>

### [`00b48588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md) → [`00b48624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48624.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b485c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48664"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b485a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4859c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b485a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48668"
      ]
    ],
    [
      "unmatched:00b485ac",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48638",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48668"
      ]
    ],
    [
      "00b48648",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b485a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md#insn-00b485a4) · [`00b485c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md#insn-00b485c0) · [`00b485c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48588.md#insn-00b485c8)
- 新版 `00b4865c`（命令位置の公開資料なし）

~~~diff
- 00b485a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b485a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b485a4 bytes 410100b5
- 00b485c0 ["INT_ADD", "register:40f0:8", ["const:b485c0:8", "const:4:8"]]
- 00b485c0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4865c ["INT_ADD", "register:40f0:8", ["const:b4865c:8", "const:4:8"]]
+ 00b4865c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b485c0 bytes 544a0494
+ 00b4865c bytes 614a0494
- 00b485c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b485c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b485c8 bytes 805604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02060e000d02855e25f124082b68d8e9"></a>

### [`00b48634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md) → [`00b486d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b486d0.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b48660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b486fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b486e4",
      "incomplete_value": true,
      "site": "00b486e4",
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
      "definition_site": "00b48648",
      "incomplete_value": true,
      "site": "00b48648",
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
      "00b486e0",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48654",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48658",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b486e0",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b486f0",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b486f4",
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

- 旧版 [`00b48648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md#insn-00b48648) · [`00b48658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md#insn-00b48658) · [`00b48660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48634.md#insn-00b48660)
- 新版 `00b486e4`（命令位置の公開資料なし）

~~~diff
- 00b48648 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48648 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b486e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b486e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48648 bytes e80000b5
+ 00b486e4 bytes e80000b5
- 00b48658 ["INT_ADD", "register:40f0:8", ["const:b48658:8", "const:4:8"]]
- 00b48658 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48658 bytes 2e4a0494
- 00b48660 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b48660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48660 bytes 608604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cedacf4d4352c1876eb2d5797a4bd8c"></a>

### [`00b48674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md) → [`00b48710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48710.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4873c",
      "incomplete_value": true,
      "site": "00b4873c",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b486a0",
      "incomplete_value": true,
      "site": "00b486a0",
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
            "const:908:8"
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
      "definition_site": "00b48724",
      "incomplete_value": true,
      "site": "00b48724",
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
      "definition_site": "00b48688",
      "incomplete_value": true,
      "site": "00b48688",
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
      "definition_site": "00b4872c",
      "incomplete_value": false,
      "site": "00b48734",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48690",
      "incomplete_value": false,
      "site": "00b48698",
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
            "const:47:8"
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
      "00b48720",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4872c",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b4873c",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48720",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4872c",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b4873c",
      "WRITE",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b48698) · [`00b486a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b486a0) · [`00b48684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48674.md#insn-00b48684)
- 新版 `00b48734`（命令位置の公開資料なし） · `00b4873c`（命令位置の公開資料なし） · `00b48720`（命令位置の公開資料なし）

~~~diff
- 00b48698 ["INT_ADD", "register:40f0:8", ["const:b48698:8", "const:4:8"]]
- 00b48698 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48734 ["INT_ADD", "register:40f0:8", ["const:b48734:8", "const:4:8"]]
+ 00b48734 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48698 bytes 1e4a0494
+ 00b48734 bytes 2b4a0494
- 00b486a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b486a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4873c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b4873c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b486a0 bytes 608604f9
+ 00b4873c bytes 600605f9
- 00b48684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b48684 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b48720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48684 bytes 688644f9
+ 00b48720 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f319872dbb0cff4047caae160f661a2f"></a>

### [`00b486b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md) → [`00b48750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48750.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48780",
      "incomplete_value": true,
      "site": "00b48780",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b486e4",
      "incomplete_value": true,
      "site": "00b486e4",
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
            "const:908:8"
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
      "definition_site": "00b48764",
      "incomplete_value": true,
      "site": "00b48764",
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
      "definition_site": "00b486c8",
      "incomplete_value": true,
      "site": "00b486c8",
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
      "definition_site": "00b48770",
      "incomplete_value": false,
      "site": "00b48778",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b486d4",
      "incomplete_value": false,
      "site": "00b486dc",
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
            "const:47:8"
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
      "00b48760",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48770",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b48780",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48760",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48770",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b48780",
      "WRITE",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b486dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486dc) · [`00b486e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486e4) · [`00b486c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486b4.md#insn-00b486c4)
- 新版 `00b48778`（命令位置の公開資料なし） · `00b48780`（命令位置の公開資料なし） · `00b48760`（命令位置の公開資料なし）

~~~diff
- 00b486dc ["INT_ADD", "register:40f0:8", ["const:b486dc:8", "const:4:8"]]
- 00b486dc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48778 ["INT_ADD", "register:40f0:8", ["const:b48778:8", "const:4:8"]]
+ 00b48778 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b486dc bytes 0d4a0494
+ 00b48778 bytes 1a4a0494
- 00b486e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b486e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b48780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b486e4 bytes 608604f9
+ 00b48780 bytes 600605f9
- 00b486c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b486c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b48760 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b486c4 bytes 688644f9
+ 00b48760 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04540bd40798c58e22804484e21bc8ee"></a>

### [`00b486f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md) → [`00b48794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48794.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b487c4",
      "incomplete_value": true,
      "site": "00b487c4",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48728",
      "incomplete_value": true,
      "site": "00b48728",
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
            "const:908:8"
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
      "definition_site": "00b487a8",
      "incomplete_value": true,
      "site": "00b487a8",
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
      "definition_site": "00b4870c",
      "incomplete_value": true,
      "site": "00b4870c",
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
      "definition_site": "00b487b0",
      "incomplete_value": false,
      "site": "00b487bc",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48714",
      "incomplete_value": false,
      "site": "00b48720",
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
            "const:47:8"
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
      "00b487a4",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b487b0",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b487c4",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b487a4",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b487b0",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b487c4",
      "WRITE",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md#insn-00b48720) · [`00b48728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md#insn-00b48728) · [`00b48708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b486f8.md#insn-00b48708)
- 新版 `00b487bc`（命令位置の公開資料なし） · `00b487c4`（命令位置の公開資料なし） · `00b487a4`（命令位置の公開資料なし）

~~~diff
- 00b48720 ["INT_ADD", "register:40f0:8", ["const:b48720:8", "const:4:8"]]
- 00b48720 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b487bc ["INT_ADD", "register:40f0:8", ["const:b487bc:8", "const:4:8"]]
+ 00b487bc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48720 bytes fc490494
+ 00b487bc bytes 094a0494
- 00b48728 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b48728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b487c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b487c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48728 bytes 608604f9
+ 00b487c4 bytes 600605f9
- 00b48708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:908:8"]]
- 00b48708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b487a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
+ 00b487a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48708 bytes 688644f9
+ 00b487a4 bytes 680645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e39acc54ba04de6489850438026d2646"></a>

### [`00b48748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md) → [`00b487e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b487e4.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4886c",
      "incomplete_value": true,
      "site": "00b4886c",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b487d0",
      "incomplete_value": true,
      "site": "00b487d0",
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
            "const:910:8"
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
      "definition_site": "00b48818",
      "incomplete_value": true,
      "site": "00b48824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4877c",
      "incomplete_value": true,
      "site": "00b48788",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "00b487f8",
      "READ",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48818",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4886c",
      "WRITE",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b487f8",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48818",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4886c",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b48788) · [`00b487d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b487d0) · [`00b4875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48748.md#insn-00b4875c)
- 新版 `00b48824`（命令位置の公開資料なし） · `00b4886c`（命令位置の公開資料なし） · `00b487f8`（命令位置の公開資料なし）

~~~diff
- 00b48788 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48788 ["INT_ADD", "register:40f0:8", ["const:b48788:8", "const:4:8"]]
- 00b48788 ["CALLIND", null, ["register:0:8"]]
+ 00b48824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48824 ["INT_ADD", "register:40f0:8", ["const:b48824:8", "const:4:8"]]
+ 00b48824 ["CALLIND", null, ["register:0:8"]]
- 00b48788 bytes 00013fd6
+ 00b48824 bytes 00013fd6
- 00b487d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b487d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:910:8"]]
- 00b487d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4886c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4886c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a10:8"]]
+ 00b4886c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b487d0 bytes a0422439
+ 00b4886c bytes a0422839
- 00b4875c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:910:8"]]
- 00b4875c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4875c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b487f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a10:8"]]
+ 00b487f8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b487f8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4875c bytes a8426439
+ 00b487f8 bytes a8426839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f7737832f21466c4a87b6093444d67"></a>

### [`00b487e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md) → [`00b48880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48880.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call, call_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b488bc",
      "incomplete_value": true,
      "site": "00b488bc",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48820",
      "incomplete_value": true,
      "site": "00b48820",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4890c"
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
      "00b48894",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488a0",
      "READ",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ],
    [
      "00b488bc",
      "WRITE",
      [
        "storage",
        "01125910",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48894",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488a0",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b488bc",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md#insn-00b48820) · [`00b4886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md#insn-00b4886c) · [`00b48870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b487e4.md#insn-00b48870)
- 新版 `00b488bc`（命令位置の公開資料なし）

~~~diff
- 00b48820 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48820 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48820 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:910:8"]]
- 00b48820 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b488bc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b488bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b488bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a10:8"]]
+ 00b488bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48820 bytes bf422439
+ 00b488bc bytes bf422839
- 00b4886c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4886c ["INT_ADD", "register:40f0:8", ["const:b4886c:8", "const:4:8"]]
- 00b4886c ["CALLIND", null, ["register:0:8"]]
- 00b4886c bytes 00013fd6
- 00b48870 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
- 00b48870 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b48870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b48870 bytes 9f8604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06fc236f2328b59f8166ed1e668fc8c3"></a>

### [`00b48884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md) → [`00b48920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48920.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48898",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48920",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48924",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48934",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md#insn-00b48884) · [`00b48888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md#insn-00b48888) · [`00b488a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48884.md#insn-00b488a0)

~~~diff
- 00b48884 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b48884 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b48884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48884 bytes f44fbea9
- 00b48888 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48888 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48888 bytes fd7b01a9
- 00b488a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b488a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b488a0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6049e87699e21add9c64b94ef02de7b"></a>

### [`00b488f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md) → [`00b48990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48990.md) _ZN8firebase4util10byte_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b489ac",
      "incomplete_value": false,
      "site": "00b489b0",
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
      "definition_site": "00b48910",
      "incomplete_value": false,
      "site": "00b48914",
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
      "definition_site": "00b489bc",
      "incomplete_value": true,
      "site": "00b489c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48920",
      "incomplete_value": true,
      "site": "00b4892c",
      "value": [
        "LOAD",
        "8",
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
      "00b489ac",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b489bc",
      "DATA",
      [
        "storage",
        "01125918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b489ac",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b489bc",
      "DATA",
      [
        "storage",
        "01125a18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b48914) · [`00b48910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b48910) · [`00b4891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b488f4.md#insn-00b4891c)
- 新版 `00b489b0`（命令位置の公開資料なし） · `00b489ac`（命令位置の公開資料なし） · `00b489b8`（命令位置の公開資料なし）

~~~diff
- 00b48914 ["INT_ADD", "register:40f0:8", ["const:b48914:8", "const:4:8"]]
- 00b48914 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b489b0 ["INT_ADD", "register:40f0:8", ["const:b489b0:8", "const:4:8"]]
+ 00b489b0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b48914 bytes bb490494
+ 00b489b0 bytes c8490494
- 00b48910 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b48910 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48910 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48910 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b489ac ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b489ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b489ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b489ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48910 bytes 009c0d91
+ 00b489ac bytes 002c0c91
- 00b4891c ["COPY", "tmp:0:8", ["const:918:8"]]
- 00b4891c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4891c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4891c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b489b8 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 00b489b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b489b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b489b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4891c bytes 08612491
+ 00b489b8 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496205e3d26507c3b0f21249329b8b93"></a>

### [`00b48930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md) → [`00b489cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b489cc.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48a0c",
      "incomplete_value": true,
      "site": "00b48a0c",
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
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48970",
      "incomplete_value": true,
      "site": "00b48970",
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
            "const:908:8"
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
      "definition_site": "00b489e8",
      "incomplete_value": true,
      "site": "00b489e8",
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
      "definition_site": "00b4894c",
      "incomplete_value": true,
      "site": "00b4894c",
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
      "definition_site": "00b489f0",
      "incomplete_value": false,
      "site": "00b48a04",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48954",
      "incomplete_value": false,
      "site": "00b48968",
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
            "const:47:8"
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
      "00b489e0",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489f0",
      "PARAM",
      [
        "storage",
        "002a6047",
        null,
        "string"
      ]
    ],
    [
      "00b48a0c",
      "WRITE",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b489e0",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489f0",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b48a0c",
      "WRITE",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48968) · [`00b48970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48970) · [`00b48944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48930.md#insn-00b48944)
- 新版 `00b48a04`（命令位置の公開資料なし） · `00b48a0c`（命令位置の公開資料なし） · `00b489e0`（命令位置の公開資料なし）

~~~diff
- 00b48968 ["INT_ADD", "register:40f0:8", ["const:b48968:8", "const:4:8"]]
- 00b48968 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48a04 ["INT_ADD", "register:40f0:8", ["const:b48a04:8", "const:4:8"]]
+ 00b48a04 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48968 bytes 6a490494
+ 00b48a04 bytes 77490494
- 00b48970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
- 00b48970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00b48a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48970 bytes 808604f9
+ 00b48a0c bytes 800605f9
- 00b48944 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:908:8"]]
- 00b48944 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b489e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
+ 00b489e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48944 bytes 818644f9
+ 00b489e0 bytes 810645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639a83dcf8f6b5a9443c13e3a02b5434"></a>

### [`00b48a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md) → [`00b48ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ab8.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48ae4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48acc",
      "incomplete_value": true,
      "site": "00b48acc",
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
      "definition_site": "00b48a30",
      "incomplete_value": true,
      "site": "00b48a30",
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
      "00b48ac8",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48a38",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48a40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b48ac8",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ad4",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b48adc",
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

- 旧版 [`00b48a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md#insn-00b48a30) · [`00b48a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md#insn-00b48a40) · [`00b48a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a1c.md#insn-00b48a48)
- 新版 `00b48acc`（命令位置の公開資料なし）

~~~diff
- 00b48a30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48a30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b48acc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48acc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48a30 bytes e80000b5
+ 00b48acc bytes e80000b5
- 00b48a40 ["INT_ADD", "register:40f0:8", ["const:b48a40:8", "const:4:8"]]
- 00b48a40 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48a40 bytes 34490494
- 00b48a48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b48a48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48a48 bytes 609a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66462a0db92de9594f5abe74d38f6fd9"></a>

### [`00b48a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a5c.md) → [`00b48af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48af8.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48b28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48b0c",
      "incomplete_value": true,
      "site": "00b48b0c",
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
      "definition_site": "00b48a70",
      "incomplete_value": true,
      "site": "00b48a70",
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
      "00b48b08",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48a90"
      ]
    ],
    [
      "unmatched:00b48a7c",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48b08",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48b2c"
      ]
    ],
    [
      "00b48b18",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a5c.md#insn-00b48a84) · [`00b48a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a5c.md#insn-00b48a8c) · [`00b48a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48a5c.md#insn-00b48a9c)

~~~diff
- 00b48a84 ["INT_ADD", "register:40f0:8", ["const:b48a84:8", "const:4:8"]]
- 00b48a84 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48a84 bytes 23490494
- 00b48a8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b48a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48a8c bytes 609a04f9
- 00b48a9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48a9c ["RETURN", null, ["register:0:8"]]
- 00b48a9c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d336297903836b7b75b5b4f986a756f"></a>

### [`00b48aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md) → [`00b48b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b3c.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48b6c",
      "incomplete_value": true,
      "site": "00b48b6c",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ad0",
      "incomplete_value": true,
      "site": "00b48ad0",
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
            "const:930:8"
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
      "definition_site": "00b48b50",
      "incomplete_value": true,
      "site": "00b48b50",
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
      "definition_site": "00b48ab4",
      "incomplete_value": true,
      "site": "00b48ab4",
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
      "definition_site": "00b48b58",
      "incomplete_value": false,
      "site": "00b48b64",
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
            "const:da5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48abc",
      "incomplete_value": false,
      "site": "00b48ac8",
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
            "const:df9:8"
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
      "00b48b4c",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b58",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ],
    [
      "00b48b6c",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48b4c",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b58",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b48b6c",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md#insn-00b48ac8) · [`00b48ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md#insn-00b48ad0) · [`00b48ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48aa0.md#insn-00b48ab0)
- 新版 `00b48b64`（命令位置の公開資料なし） · `00b48b6c`（命令位置の公開資料なし） · `00b48b4c`（命令位置の公開資料なし）

~~~diff
- 00b48ac8 ["INT_ADD", "register:40f0:8", ["const:b48ac8:8", "const:4:8"]]
- 00b48ac8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48b64 ["INT_ADD", "register:40f0:8", ["const:b48b64:8", "const:4:8"]]
+ 00b48b64 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48ac8 bytes 12490494
+ 00b48b64 bytes 1f490494
- 00b48ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b48ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00b48b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48ad0 bytes 609a04f9
+ 00b48b6c bytes 601a05f9
- 00b48ab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b48ab0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
+ 00b48b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48ab0 bytes 689a44f9
+ 00b48b4c bytes 681a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ff3b543830e9f503ceae5586056a8e"></a>

### [`00b48af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md) → [`00b48b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b8c.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 71.43% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48c14",
      "incomplete_value": true,
      "site": "00b48c14",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b78",
      "incomplete_value": true,
      "site": "00b48b78",
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
            "const:938:8"
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
      "definition_site": "00b48bc0",
      "incomplete_value": true,
      "site": "00b48bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b24",
      "incomplete_value": true,
      "site": "00b48b30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48b5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48ba0",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48bc0",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c14",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48ba0",
      "READ",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48bc0",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c14",
      "WRITE",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b30) · [`00b48b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b5c) · [`00b48b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48af0.md#insn-00b48b78)
- 新版 `00b48bcc`（命令位置の公開資料なし） · `00b48c14`（命令位置の公開資料なし）

~~~diff
- 00b48b30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48b30 ["INT_ADD", "register:40f0:8", ["const:b48b30:8", "const:4:8"]]
- 00b48b30 ["CALLIND", null, ["register:0:8"]]
+ 00b48bcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48bcc ["INT_ADD", "register:40f0:8", ["const:b48bcc:8", "const:4:8"]]
+ 00b48bcc ["CALLIND", null, ["register:0:8"]]
- 00b48b30 bytes 00013fd6
+ 00b48bcc bytes 00013fd6
- 00b48b5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48b5c ["INT_ADD", "register:40f0:8", ["const:b48b5c:8", "const:4:8"]]
- 00b48b5c ["CALLIND", null, ["register:0:8"]]
- 00b48b5c bytes 00013fd6
- 00b48b78 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48b78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:938:8"]]
- 00b48b78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48c14 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48c14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a38:8"]]
+ 00b48c14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48b78 bytes a0e22439
+ 00b48c14 bytes a0e22839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31e79f9351127704eb2c083242dcce2f"></a>

### [`00b48b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md) → [`00b48c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48c28.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48c64",
      "incomplete_value": true,
      "site": "00b48c64",
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
            "const:a38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48bc8",
      "incomplete_value": true,
      "site": "00b48bc8",
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
            "const:938:8"
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
      "definition_site": "00b48cb4",
      "incomplete_value": true,
      "site": "00b48cb4",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48c18",
      "incomplete_value": true,
      "site": "00b48c18",
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
            "const:930:8"
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
      "definition_site": "00b48c40",
      "incomplete_value": true,
      "site": "00b48c40",
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
      "definition_site": "00b48ba4",
      "incomplete_value": true,
      "site": "00b48ba4",
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
      "00b48c3c",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c48",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48c64",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48c3c",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c48",
      "READ",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48c64",
      "WRITE",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48ba4) · [`00b48bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48bc8) · [`00b48c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48b8c.md#insn-00b48c14)
- 新版 `00b48c40`（命令位置の公開資料なし） · `00b48c64`（命令位置の公開資料なし） · `00b48cb0`（命令位置の公開資料なし）

~~~diff
- 00b48ba4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48ba4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b48c40 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b48c40 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b48ba4 bytes c10300b4
+ 00b48c40 bytes c10300b4
- 00b48bc8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48bc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48bc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:938:8"]]
- 00b48bc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48c64 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48c64 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48c64 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a38:8"]]
+ 00b48c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48bc8 bytes bfe22439
+ 00b48c64 bytes bfe22839
- 00b48c14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48c14 ["INT_ADD", "register:40f0:8", ["const:b48c14:8", "const:4:8"]]
- 00b48c14 ["CALLIND", null, ["register:0:8"]]
+ 00b48cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48cb0 ["INT_ADD", "register:40f0:8", ["const:b48cb0:8", "const:4:8"]]
+ 00b48cb0 ["CALLIND", null, ["register:0:8"]]
- 00b48c14 bytes 00013fd6
+ 00b48cb0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e074f7dddc700a483b1d66e62f962be"></a>

### [`00b48c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md) → [`00b48cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48cc8.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b48c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48d08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48c48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48c40",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d0c"
      ]
    ],
    [
      "unmatched:00b48c50",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48cdc",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d0c"
      ]
    ],
    [
      "00b48cec",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md#insn-00b48c48) · [`00b48c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md#insn-00b48c64) · [`00b48c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c2c.md#insn-00b48c6c)
- 新版 `00b48d00`（命令位置の公開資料なし）

~~~diff
- 00b48c48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48c48 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48c48 bytes 410100b5
- 00b48c64 ["INT_ADD", "register:40f0:8", ["const:b48c64:8", "const:4:8"]]
- 00b48c64 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48d00 ["INT_ADD", "register:40f0:8", ["const:b48d00:8", "const:4:8"]]
+ 00b48d00 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48c64 bytes ab480494
+ 00b48d00 bytes b8480494
- 00b48c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00b48c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48c6c bytes 809a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e67b3176c7ba01cecba67d6f4b9e4f58"></a>

### [`00b48c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md) → [`00b48d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d38.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48d54",
      "incomplete_value": false,
      "site": "00b48d58",
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
      "definition_site": "00b48cb8",
      "incomplete_value": false,
      "site": "00b48cbc",
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
      "definition_site": "00b48d64",
      "incomplete_value": true,
      "site": "00b48d70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48cc8",
      "incomplete_value": true,
      "site": "00b48cd4",
      "value": [
        "LOAD",
        "8",
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
      "00b48d54",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b48d64",
      "DATA",
      [
        "storage",
        "01125940",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48d54",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48d64",
      "DATA",
      [
        "storage",
        "01125a40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md#insn-00b48cbc) · [`00b48cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md#insn-00b48cb8) · [`00b48cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md#insn-00b48cc4)
- 新版 `00b48d58`（命令位置の公開資料なし） · `00b48d54`（命令位置の公開資料なし） · `00b48d60`（命令位置の公開資料なし）

~~~diff
- 00b48cbc ["INT_ADD", "register:40f0:8", ["const:b48cbc:8", "const:4:8"]]
- 00b48cbc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b48d58 ["INT_ADD", "register:40f0:8", ["const:b48d58:8", "const:4:8"]]
+ 00b48d58 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b48cbc bytes d1480494
+ 00b48d58 bytes de480494
- 00b48cb8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b48cb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48cb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48cb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48d54 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b48d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48cb8 bytes 009c0d91
+ 00b48d54 bytes 002c0c91
- 00b48cc4 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00b48cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b48d60 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00b48d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48cc4 bytes 08012591
+ 00b48d60 bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efb2e943594f274ee032cc0ec30f541"></a>

### [`00b48cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md) → [`00b48d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d74.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48db4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48cf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48cec",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48db8"
      ]
    ],
    [
      "unmatched:00b48cfc",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48d88",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48db8"
      ]
    ],
    [
      "00b48d98",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md#insn-00b48cf4) · [`00b48d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md#insn-00b48d10) · [`00b48d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48cd8.md#insn-00b48d18)
- 新版 `00b48dac`（命令位置の公開資料なし）

~~~diff
- 00b48cf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48cf4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48cf4 bytes 410100b5
- 00b48d10 ["INT_ADD", "register:40f0:8", ["const:b48d10:8", "const:4:8"]]
- 00b48d10 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48dac ["INT_ADD", "register:40f0:8", ["const:b48dac:8", "const:4:8"]]
+ 00b48dac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48d10 bytes 80480494
+ 00b48dac bytes 8d480494
- 00b48d18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00b48d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48d18 bytes 809a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e876d53354f785f4f6036735119ec7"></a>

### [`00b48d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md) → [`00b48e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e20.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b48db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48e4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48e34",
      "incomplete_value": true,
      "site": "00b48e34",
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
      "definition_site": "00b48d98",
      "incomplete_value": true,
      "site": "00b48d98",
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
      "00b48e30",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48da4",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48da8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b48e30",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e40",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b48e44",
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

- 旧版 [`00b48d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48d98) · [`00b48da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48da8) · [`00b48db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d84.md#insn-00b48db0)
- 新版 `00b48e34`（命令位置の公開資料なし）

~~~diff
- 00b48d98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48d98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48e34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48e34 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b48d98 bytes e80000b5
+ 00b48e34 bytes e80000b5
- 00b48da8 ["INT_ADD", "register:40f0:8", ["const:b48da8:8", "const:4:8"]]
- 00b48da8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48da8 bytes 5a480494
- 00b48db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
- 00b48db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48db0 bytes 60ae04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143aa6763a6783b8823f2112140b0658"></a>

### [`00b48e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md) → [`00b48ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ea0.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48ed0",
      "incomplete_value": true,
      "site": "00b48ed0",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e34",
      "incomplete_value": true,
      "site": "00b48e34",
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
            "const:958:8"
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
      "definition_site": "00b48eb4",
      "incomplete_value": true,
      "site": "00b48eb4",
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
      "definition_site": "00b48e18",
      "incomplete_value": true,
      "site": "00b48e18",
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
      "definition_site": "00b48ec0",
      "incomplete_value": false,
      "site": "00b48ec8",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e24",
      "incomplete_value": false,
      "site": "00b48e2c",
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
            "const:40e:8"
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
      "00b48eb0",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ec0",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b48ed0",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48eb0",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ec0",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b48ed0",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e2c) · [`00b48e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e34) · [`00b48e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e04.md#insn-00b48e14)
- 新版 `00b48ec8`（命令位置の公開資料なし） · `00b48ed0`（命令位置の公開資料なし） · `00b48eb0`（命令位置の公開資料なし）

~~~diff
- 00b48e2c ["INT_ADD", "register:40f0:8", ["const:b48e2c:8", "const:4:8"]]
- 00b48e2c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48ec8 ["INT_ADD", "register:40f0:8", ["const:b48ec8:8", "const:4:8"]]
+ 00b48ec8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48e2c bytes 39480494
+ 00b48ec8 bytes 46480494
- 00b48e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
- 00b48e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
+ 00b48ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48e34 bytes 60ae04f9
+ 00b48ed0 bytes 602e05f9
- 00b48e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
- 00b48e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
+ 00b48eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48e14 bytes 68ae44f9
+ 00b48eb0 bytes 682e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01aebc3da4c553a6b4f10ec4f7f95a7"></a>

### [`00b48e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md) → [`00b48ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ee4.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48f14",
      "incomplete_value": true,
      "site": "00b48f14",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e78",
      "incomplete_value": true,
      "site": "00b48e78",
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
            "const:958:8"
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
      "definition_site": "00b48ef8",
      "incomplete_value": true,
      "site": "00b48ef8",
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
      "definition_site": "00b48e5c",
      "incomplete_value": true,
      "site": "00b48e5c",
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
      "definition_site": "00b48f00",
      "incomplete_value": false,
      "site": "00b48f0c",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e64",
      "incomplete_value": false,
      "site": "00b48e70",
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
            "const:40e:8"
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
      "00b48ef4",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f00",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b48f14",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48ef4",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f00",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b48f14",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e70) · [`00b48e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e78) · [`00b48e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e48.md#insn-00b48e58)
- 新版 `00b48f0c`（命令位置の公開資料なし） · `00b48f14`（命令位置の公開資料なし） · `00b48ef4`（命令位置の公開資料なし）

~~~diff
- 00b48e70 ["INT_ADD", "register:40f0:8", ["const:b48e70:8", "const:4:8"]]
- 00b48e70 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48f0c ["INT_ADD", "register:40f0:8", ["const:b48f0c:8", "const:4:8"]]
+ 00b48f0c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48e70 bytes 28480494
+ 00b48f0c bytes 35480494
- 00b48e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
- 00b48e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
+ 00b48f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48e78 bytes 60ae04f9
+ 00b48f14 bytes 602e05f9
- 00b48e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:958:8"]]
- 00b48e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
+ 00b48ef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48e58 bytes 68ae44f9
+ 00b48ef4 bytes 682e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91e2afda6463136a0334ca0ff68d72a"></a>

### [`00b48e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e98.md) → [`00b48f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48f34.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48fbc",
      "incomplete_value": true,
      "site": "00b48fbc",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f20",
      "incomplete_value": true,
      "site": "00b48f20",
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
            "const:960:8"
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
      "definition_site": "00b48f68",
      "incomplete_value": true,
      "site": "00b48f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ecc",
      "incomplete_value": true,
      "site": "00b48ed8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
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
      "00b48f48",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48f68",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48fbc",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48f48",
      "READ",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48f68",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48fbc",
      "WRITE",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e98.md#insn-00b48ed8) · [`00b48f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e98.md#insn-00b48f20) · [`00b48eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48e98.md#insn-00b48eac)
- 新版 `00b48f74`（命令位置の公開資料なし） · `00b48fbc`（命令位置の公開資料なし） · `00b48f48`（命令位置の公開資料なし）

~~~diff
- 00b48ed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48ed8 ["INT_ADD", "register:40f0:8", ["const:b48ed8:8", "const:4:8"]]
- 00b48ed8 ["CALLIND", null, ["register:0:8"]]
+ 00b48f74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48f74 ["INT_ADD", "register:40f0:8", ["const:b48f74:8", "const:4:8"]]
+ 00b48f74 ["CALLIND", null, ["register:0:8"]]
- 00b48ed8 bytes 00013fd6
+ 00b48f74 bytes 00013fd6
- 00b48f20 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48f20 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:960:8"]]
- 00b48f20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48fbc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48fbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a60:8"]]
+ 00b48fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48f20 bytes a0822539
+ 00b48fbc bytes a0822939
- 00b48eac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:960:8"]]
- 00b48eac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b48eac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b48f48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a60:8"]]
+ 00b48f48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b48f48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b48eac bytes a8826539
+ 00b48f48 bytes a8826939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113a8aeed73582ee1b026666ae57ad0a"></a>

### [`00b48f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md) → [`00b48fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48fd0.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4900c",
      "incomplete_value": true,
      "site": "00b4900c",
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
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f70",
      "incomplete_value": true,
      "site": "00b48f70",
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
            "const:960:8"
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
      "definition_site": "00b4905c",
      "incomplete_value": true,
      "site": "00b4905c",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48fc0",
      "incomplete_value": true,
      "site": "00b48fc0",
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
            "const:958:8"
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
      "definition_site": "00b48fe8",
      "incomplete_value": true,
      "site": "00b48fe8",
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
      "definition_site": "00b48f4c",
      "incomplete_value": true,
      "site": "00b48f4c",
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
      "00b48fe4",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ff0",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4900c",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48fe4",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ff0",
      "READ",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4900c",
      "WRITE",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md#insn-00b48f4c) · [`00b48f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md#insn-00b48f70) · [`00b48f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48f34.md#insn-00b48f98)
- 新版 `00b48fe8`（命令位置の公開資料なし） · `00b4900c`（命令位置の公開資料なし）

~~~diff
- 00b48f4c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48f4c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b48fe8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b48fe8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b48f4c bytes c10300b4
+ 00b48fe8 bytes c10300b4
- 00b48f70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48f70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48f70 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:960:8"]]
- 00b48f70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4900c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4900c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4900c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a60:8"]]
+ 00b4900c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48f70 bytes bf822539
+ 00b4900c bytes bf822939
- 00b48f98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48f98 ["INT_ADD", "register:40f0:8", ["const:b48f98:8", "const:4:8"]]
- 00b48f98 ["CALLIND", null, ["register:0:8"]]
- 00b48f98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4726d8a6a6f73650a4fcab2454e4367d"></a>

### [`00b48fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48fd4.md) → [`00b49070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49070.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48fd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48fd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48fd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48fd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48fe8",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49070",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49074",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49084",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48fd4.md#insn-00b48fd4) · [`00b48fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48fd4.md#insn-00b48fd8) · [`00b48ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48fd4.md#insn-00b48ff0)

~~~diff
- 00b48fd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b48fd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b48fd4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48fd4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48fd4 bytes f44fbea9
- 00b48fd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48fd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48fd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48fd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48fd8 bytes fd7b01a9
- 00b48ff0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48ff0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b48ff0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c99812e8eaa98b5e4400ea9030063e85"></a>

### [`00b49044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md) → [`00b490e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b490e0.md) _ZN8firebase4util11class_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b490fc",
      "incomplete_value": false,
      "site": "00b49100",
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
      "definition_site": "00b49060",
      "incomplete_value": false,
      "site": "00b49064",
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
      "definition_site": "00b4910c",
      "incomplete_value": true,
      "site": "00b49118",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49070",
      "incomplete_value": true,
      "site": "00b4907c",
      "value": [
        "LOAD",
        "8",
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
      "00b490fc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4910c",
      "DATA",
      [
        "storage",
        "01125968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b490fc",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4910c",
      "DATA",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b49064) · [`00b49060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b49060) · [`00b4906c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49044.md#insn-00b4906c)
- 新版 `00b49100`（命令位置の公開資料なし） · `00b490fc`（命令位置の公開資料なし） · `00b49108`（命令位置の公開資料なし）

~~~diff
- 00b49064 ["INT_ADD", "register:40f0:8", ["const:b49064:8", "const:4:8"]]
- 00b49064 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b49100 ["INT_ADD", "register:40f0:8", ["const:b49100:8", "const:4:8"]]
+ 00b49100 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b49064 bytes e7470494
+ 00b49100 bytes f4470494
- 00b49060 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b49060 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49060 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49060 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b490fc ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b490fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b490fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b490fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49060 bytes 009c0d91
+ 00b490fc bytes 002c0c91
- 00b4906c ["COPY", "tmp:0:8", ["const:968:8"]]
- 00b4906c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4906c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4906c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49108 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00b49108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4906c bytes 08a12591
+ 00b49108 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb25a9262184101c9851346352dafcb2"></a>

### [`00b49080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md) → [`00b4911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4911c.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4915c",
      "incomplete_value": true,
      "site": "00b4915c",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490c0",
      "incomplete_value": true,
      "site": "00b490c0",
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
            "const:958:8"
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
      "definition_site": "00b49138",
      "incomplete_value": true,
      "site": "00b49138",
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
      "definition_site": "00b4909c",
      "incomplete_value": true,
      "site": "00b4909c",
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
      "definition_site": "00b49140",
      "incomplete_value": false,
      "site": "00b49154",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490a4",
      "incomplete_value": false,
      "site": "00b490b8",
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
            "const:40e:8"
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
      "00b49130",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49140",
      "PARAM",
      [
        "storage",
        "002a840e",
        null,
        "string"
      ]
    ],
    [
      "00b4915c",
      "WRITE",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49130",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49140",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b4915c",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b490b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b490b8) · [`00b490c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b490c0) · [`00b49094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49080.md#insn-00b49094)
- 新版 `00b49154`（命令位置の公開資料なし） · `00b4915c`（命令位置の公開資料なし） · `00b49130`（命令位置の公開資料なし）

~~~diff
- 00b490b8 ["INT_ADD", "register:40f0:8", ["const:b490b8:8", "const:4:8"]]
- 00b490b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49154 ["INT_ADD", "register:40f0:8", ["const:b49154:8", "const:4:8"]]
+ 00b49154 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b490b8 bytes 96470494
+ 00b49154 bytes a3470494
- 00b490c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
- 00b490c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4915c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a58:8"]]
+ 00b4915c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b490c0 bytes 80ae04f9
+ 00b4915c bytes 802e05f9
- 00b49094 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:958:8"]]
- 00b49094 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a58:8"]]
+ 00b49130 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49094 bytes 81ae44f9
+ 00b49130 bytes 812e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4165e52c6d9ccba3052aaf6cf30add45"></a>

### [`00b490f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md) → [`00b4918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4918c.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b491a8",
      "incomplete_value": false,
      "site": "00b491ac",
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
      "definition_site": "00b4910c",
      "incomplete_value": false,
      "site": "00b49110",
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
      "definition_site": "00b491b8",
      "incomplete_value": true,
      "site": "00b491c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4911c",
      "incomplete_value": true,
      "site": "00b49128",
      "value": [
        "LOAD",
        "8",
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
      "00b491a8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b491b8",
      "DATA",
      [
        "storage",
        "01125978",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b491a8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b491b8",
      "DATA",
      [
        "storage",
        "01125a78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b49110) · [`00b4910c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b4910c) · [`00b49118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b490f0.md#insn-00b49118)
- 新版 `00b491ac`（命令位置の公開資料なし） · `00b491a8`（命令位置の公開資料なし） · `00b491b4`（命令位置の公開資料なし）

~~~diff
- 00b49110 ["INT_ADD", "register:40f0:8", ["const:b49110:8", "const:4:8"]]
- 00b49110 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b491ac ["INT_ADD", "register:40f0:8", ["const:b491ac:8", "const:4:8"]]
+ 00b491ac ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b49110 bytes bc470494
+ 00b491ac bytes c9470494
- 00b4910c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4910c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4910c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4910c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b491a8 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b491a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b491a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b491a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4910c bytes 00781491
+ 00b491a8 bytes 00341591
- 00b49118 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00b49118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b491b4 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00b491b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b491b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b491b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49118 bytes 08e12591
+ 00b491b4 bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0df1f0a4db3f326824ba51162fc9395e"></a>

### [`00b4912c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md) → [`00b491c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b491c8.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00b491f4",
      "incomplete_value": true,
      "site": "00b491f4",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49158",
      "incomplete_value": true,
      "site": "00b49158",
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
            "const:980:8"
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
      "definition_site": "00b491dc",
      "incomplete_value": true,
      "site": "00b491dc",
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
      "definition_site": "00b49140",
      "incomplete_value": true,
      "site": "00b49140",
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
      "definition_site": "00b491e8",
      "incomplete_value": false,
      "site": "00b491ec",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4914c",
      "incomplete_value": false,
      "site": "00b49150",
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
            "const:33f:8"
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
      "00b491d8",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491e8",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b491f4",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b491d8",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491e8",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b491f4",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b49150) · [`00b49158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b49158) · [`00b4913c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4912c.md#insn-00b4913c)
- 新版 `00b491ec`（命令位置の公開資料なし） · `00b491f4`（命令位置の公開資料なし） · `00b491d8`（命令位置の公開資料なし）

~~~diff
- 00b49150 ["INT_ADD", "register:40f0:8", ["const:b49150:8", "const:4:8"]]
- 00b49150 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b491ec ["INT_ADD", "register:40f0:8", ["const:b491ec:8", "const:4:8"]]
+ 00b491ec ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49150 bytes 70470494
+ 00b491ec bytes 7d470494
- 00b49158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b49158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b491f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
+ 00b491f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49158 bytes 60c204f9
+ 00b491f4 bytes 604205f9
- 00b4913c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b4913c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b491d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
+ 00b491d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4913c bytes 68c244f9
+ 00b491d8 bytes 684245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e4e31ad719a7b16fbcf515863758150"></a>

### [`00b4916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md) → [`00b49208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49208.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "site": "00b4916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49170"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4916c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49170",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49218",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49208",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4920c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49218",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md#insn-00b4916c) · [`00b49170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md#insn-00b49170) · [`00b49180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4916c.md#insn-00b49180)
- 新版 `00b4921c`（命令位置の公開資料なし）

~~~diff
- 00b4916c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4916c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4916c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4916c bytes f30f1ef8
- 00b49170 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49170 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49170 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49170 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49170 bytes fd7b01a9
- 00b49180 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49180 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4921c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4921c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49180 bytes e80000b5
+ 00b4921c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75bbe150779c3f1a963c9f25e9ad24f4"></a>

### [`00b491ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md) → [`00b49248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49248.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49278",
      "incomplete_value": true,
      "site": "00b49278",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491dc",
      "incomplete_value": true,
      "site": "00b491dc",
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
            "const:980:8"
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
      "definition_site": "00b4925c",
      "incomplete_value": true,
      "site": "00b4925c",
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
      "definition_site": "00b491c0",
      "incomplete_value": true,
      "site": "00b491c0",
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
      "definition_site": "00b49268",
      "incomplete_value": false,
      "site": "00b49270",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491cc",
      "incomplete_value": false,
      "site": "00b491d4",
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
            "const:33f:8"
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
      "00b49258",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49268",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ],
    [
      "00b49278",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49258",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49268",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b49278",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b491d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491d4) · [`00b491dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491dc) · [`00b491bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491ac.md#insn-00b491bc)
- 新版 `00b49270`（命令位置の公開資料なし） · `00b49278`（命令位置の公開資料なし） · `00b49258`（命令位置の公開資料なし）

~~~diff
- 00b491d4 ["INT_ADD", "register:40f0:8", ["const:b491d4:8", "const:4:8"]]
- 00b491d4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49270 ["INT_ADD", "register:40f0:8", ["const:b49270:8", "const:4:8"]]
+ 00b49270 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b491d4 bytes 4f470494
+ 00b49270 bytes 5c470494
- 00b491dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b491dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
+ 00b49278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b491dc bytes 60c204f9
+ 00b49278 bytes 604205f9
- 00b491bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b491bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
+ 00b49258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b491bc bytes 68c244f9
+ 00b49258 bytes 684245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bbf21b37cd18c9af9243331b83b1f1b"></a>

### [`00b491f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md) → [`00b4928c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4928c.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b492bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b492a0",
      "incomplete_value": true,
      "site": "00b492a0",
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
      "definition_site": "00b49204",
      "incomplete_value": true,
      "site": "00b49204",
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
      "00b4929c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49224"
      ]
    ],
    [
      "unmatched:00b4920c",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4929c",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b492a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b492c0"
      ]
    ],
    [
      "00b492a8",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49218) · [`00b49220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49220) · [`00b49230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b491f0.md#insn-00b49230)
- 新版 `00b492b4`（命令位置の公開資料なし）

~~~diff
- 00b49218 ["INT_ADD", "register:40f0:8", ["const:b49218:8", "const:4:8"]]
- 00b49218 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b492b4 ["INT_ADD", "register:40f0:8", ["const:b492b4:8", "const:4:8"]]
+ 00b492b4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49218 bytes 3e470494
+ 00b492b4 bytes 4b470494
- 00b49220 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b49220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49220 bytes 60c204f9
- 00b49230 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49230 ["RETURN", null, ["register:0:8"]]
- 00b49230 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9131ba1fa799bec4b235272047c651f7"></a>

### [`00b49240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md) → [`00b492dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492dc.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 44.44% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49364",
      "incomplete_value": true,
      "site": "00b49364",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492c8",
      "incomplete_value": true,
      "site": "00b492c8",
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
            "const:988:8"
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
      "site": "00b49280"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4931c"
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
      "00b492f0",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b49274",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49364",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b492f0",
      "READ",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49310",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49364",
      "WRITE",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md#insn-00b49280) · [`00b492c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49240.md#insn-00b492c8)
- 新版 `00b49364`（命令位置の公開資料なし） · `00b4931c`（命令位置の公開資料なし）

~~~diff
- 00b49280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49280 ["INT_ADD", "register:40f0:8", ["const:b49280:8", "const:4:8"]]
- 00b49280 ["CALLIND", null, ["register:0:8"]]
- 00b49280 bytes 00013fd6
- 00b492c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b492c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:988:8"]]
- 00b492c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49364 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49364 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a88:8"]]
+ 00b49364 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b492c8 bytes a0222639
+ 00b49364 bytes a0222a39
+ 00b4931c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4931c ["INT_ADD", "register:40f0:8", ["const:b4931c:8", "const:4:8"]]
+ 00b4931c ["CALLIND", null, ["register:0:8"]]
+ 00b4931c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54216b36c861f74d43ad624ef8665332"></a>

### [`00b492dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md) → [`00b49378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49378.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b493b4",
      "incomplete_value": true,
      "site": "00b493b4",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49318",
      "incomplete_value": true,
      "site": "00b49318",
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
            "const:988:8"
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
      "definition_site": "00b49404",
      "incomplete_value": true,
      "site": "00b49404",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49368",
      "incomplete_value": true,
      "site": "00b49368",
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
            "const:980:8"
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
      "definition_site": "00b49390",
      "incomplete_value": true,
      "site": "00b49390",
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
      "definition_site": "00b492f4",
      "incomplete_value": true,
      "site": "00b492f4",
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
      "00b4938c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49398",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b493b4",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4938c",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49398",
      "READ",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b493b4",
      "WRITE",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49318) · [`00b49364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49364) · [`00b49368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b492dc.md#insn-00b49368)
- 新版 `00b493b4`（命令位置の公開資料なし） · `00b49400`（命令位置の公開資料なし） · `00b49404`（命令位置の公開資料なし）

~~~diff
- 00b49318 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49318 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49318 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
- 00b49318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b493b4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b493b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b493b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a88:8"]]
+ 00b493b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49318 bytes bf222639
+ 00b493b4 bytes bf222a39
- 00b49364 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49364 ["INT_ADD", "register:40f0:8", ["const:b49364:8", "const:4:8"]]
- 00b49364 ["CALLIND", null, ["register:0:8"]]
+ 00b49400 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49400 ["INT_ADD", "register:40f0:8", ["const:b49400:8", "const:4:8"]]
+ 00b49400 ["CALLIND", null, ["register:0:8"]]
- 00b49364 bytes 00013fd6
+ 00b49400 bytes 00013fd6
- 00b49368 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b49368 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b49404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a80:8"]]
+ 00b49404 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b49404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49368 bytes 9fc204f9
+ 00b49404 bytes 9f4205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf18ebe69abc7b3e9d4a6fb1b06b4e8"></a>

### [`00b4937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md) → [`00b49418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49418.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b493bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49458"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49390",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49398",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4945c"
      ]
    ],
    [
      "unmatched:00b493a0",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4942c",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49434",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4945c"
      ]
    ],
    [
      "00b4943c",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md#insn-00b49398) · [`00b493b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md#insn-00b493b4) · [`00b493bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4937c.md#insn-00b493bc)
- 新版 `00b49450`（命令位置の公開資料なし）

~~~diff
- 00b49398 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49398 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49398 bytes 410100b5
- 00b493b4 ["INT_ADD", "register:40f0:8", ["const:b493b4:8", "const:4:8"]]
- 00b493b4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49450 ["INT_ADD", "register:40f0:8", ["const:b49450:8", "const:4:8"]]
+ 00b49450 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b493b4 bytes d7460494
+ 00b49450 bytes e4460494
- 00b493bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b493bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b493bc bytes 80c204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26131dba9c7ed566a92186247abc2781"></a>

### [`00b493ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md) → [`00b49488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49488.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b494a4",
      "incomplete_value": false,
      "site": "00b494a8",
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
      "definition_site": "00b49408",
      "incomplete_value": false,
      "site": "00b4940c",
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
      "definition_site": "00b494b4",
      "incomplete_value": true,
      "site": "00b494c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49418",
      "incomplete_value": true,
      "site": "00b49424",
      "value": [
        "LOAD",
        "8",
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
      "00b494a4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b494b4",
      "DATA",
      [
        "storage",
        "01125990",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b494a4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b494b4",
      "DATA",
      [
        "storage",
        "01125a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4940c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b4940c) · [`00b49408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b49408) · [`00b49414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b493ec.md#insn-00b49414)
- 新版 `00b494a8`（命令位置の公開資料なし） · `00b494a4`（命令位置の公開資料なし） · `00b494b0`（命令位置の公開資料なし）

~~~diff
- 00b4940c ["INT_ADD", "register:40f0:8", ["const:b4940c:8", "const:4:8"]]
- 00b4940c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b494a8 ["INT_ADD", "register:40f0:8", ["const:b494a8:8", "const:4:8"]]
+ 00b494a8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4940c bytes fd460494
+ 00b494a8 bytes 0a470494
- 00b49408 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b49408 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49408 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49408 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b494a4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b494a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b494a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b494a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49408 bytes 009c0d91
+ 00b494a4 bytes 002c0c91
- 00b49414 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00b49414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b494b0 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 00b494b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b494b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b494b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49414 bytes 08412691
+ 00b494b0 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ab56c30091d347d6baaecc8e9ad03d6"></a>

### [`00b49428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md) → [`00b494c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b494c4.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b49468"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49504"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49444"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4943c",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49508"
      ]
    ],
    [
      "unmatched:00b4944c",
      "PARAM",
      [
        "storage",
        "002af33f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b494d8",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49508"
      ]
    ],
    [
      "00b494e8",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b49444) · [`00b49460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b49460) · [`00b49468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49428.md#insn-00b49468)
- 新版 `00b494fc`（命令位置の公開資料なし）

~~~diff
- 00b49444 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49444 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49444 bytes 410100b5
- 00b49460 ["INT_ADD", "register:40f0:8", ["const:b49460:8", "const:4:8"]]
- 00b49460 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b494fc ["INT_ADD", "register:40f0:8", ["const:b494fc:8", "const:4:8"]]
+ 00b494fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49460 bytes ac460494
+ 00b494fc bytes b9460494
- 00b49468 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b49468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49468 bytes 80c204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6e42c1c00dbc0bc7542c1133fc149a0"></a>

### [`00b494d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md) → [`00b49570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49570.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

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
      "definition_site": "00b4959c",
      "incomplete_value": true,
      "site": "00b4959c",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49500",
      "incomplete_value": true,
      "site": "00b49500",
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
            "const:9a8:8"
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
      "definition_site": "00b49584",
      "incomplete_value": true,
      "site": "00b49584",
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
      "definition_site": "00b494e8",
      "incomplete_value": true,
      "site": "00b494e8",
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
      "definition_site": "00b49590",
      "incomplete_value": false,
      "site": "00b49594",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494f4",
      "incomplete_value": false,
      "site": "00b494f8",
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
            "const:139:8"
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
      "00b49580",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49590",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b4959c",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49580",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49590",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4959c",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b494f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b494f8) · [`00b49500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b49500) · [`00b494e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b494d4.md#insn-00b494e4)
- 新版 `00b49594`（命令位置の公開資料なし） · `00b4959c`（命令位置の公開資料なし） · `00b49580`（命令位置の公開資料なし）

~~~diff
- 00b494f8 ["INT_ADD", "register:40f0:8", ["const:b494f8:8", "const:4:8"]]
- 00b494f8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49594 ["INT_ADD", "register:40f0:8", ["const:b49594:8", "const:4:8"]]
+ 00b49594 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b494f8 bytes 86460494
+ 00b49594 bytes 93460494
- 00b49500 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b49500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4959c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b4959c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49500 bytes 60d604f9
+ 00b4959c bytes 605605f9
- 00b494e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b494e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b49580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b494e4 bytes 68d644f9
+ 00b49580 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3d3c7599bdcc9e775e25bee01f6c3a"></a>

### [`00b49514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md) → [`00b495b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495b0.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b495dc",
      "incomplete_value": true,
      "site": "00b495dc",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49540",
      "incomplete_value": true,
      "site": "00b49540",
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
            "const:9a8:8"
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
      "definition_site": "00b495c4",
      "incomplete_value": true,
      "site": "00b495c4",
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
      "definition_site": "00b49528",
      "incomplete_value": true,
      "site": "00b49528",
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
      "definition_site": "00b495cc",
      "incomplete_value": false,
      "site": "00b495d4",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49530",
      "incomplete_value": false,
      "site": "00b49538",
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
            "const:139:8"
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
      "00b495c0",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495cc",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b495dc",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b495c0",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495cc",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b495dc",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49538) · [`00b49540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49540) · [`00b49524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49514.md#insn-00b49524)
- 新版 `00b495d4`（命令位置の公開資料なし） · `00b495dc`（命令位置の公開資料なし） · `00b495c0`（命令位置の公開資料なし）

~~~diff
- 00b49538 ["INT_ADD", "register:40f0:8", ["const:b49538:8", "const:4:8"]]
- 00b49538 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b495d4 ["INT_ADD", "register:40f0:8", ["const:b495d4:8", "const:4:8"]]
+ 00b495d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49538 bytes 76460494
+ 00b495d4 bytes 83460494
- 00b49540 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b49540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b495dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b495dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49540 bytes 60d604f9
+ 00b495dc bytes 605605f9
- 00b49524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b49524 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b495c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b495c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49524 bytes 68d644f9
+ 00b495c0 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0be9f40ab317f8f99495b9d4ff3c4f"></a>

### [`00b49554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md) → [`00b495f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495f0.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49620",
      "incomplete_value": true,
      "site": "00b49620",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49584",
      "incomplete_value": true,
      "site": "00b49584",
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
            "const:9a8:8"
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
      "definition_site": "00b49604",
      "incomplete_value": true,
      "site": "00b49604",
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
      "definition_site": "00b49568",
      "incomplete_value": true,
      "site": "00b49568",
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
      "definition_site": "00b49610",
      "incomplete_value": false,
      "site": "00b49618",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49574",
      "incomplete_value": false,
      "site": "00b4957c",
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
            "const:139:8"
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
      "00b49600",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49610",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49620",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49600",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49610",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b49620",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4957c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b4957c) · [`00b49584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b49584) · [`00b49564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49554.md#insn-00b49564)
- 新版 `00b49618`（命令位置の公開資料なし） · `00b49620`（命令位置の公開資料なし） · `00b49600`（命令位置の公開資料なし）

~~~diff
- 00b4957c ["INT_ADD", "register:40f0:8", ["const:b4957c:8", "const:4:8"]]
- 00b4957c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49618 ["INT_ADD", "register:40f0:8", ["const:b49618:8", "const:4:8"]]
+ 00b49618 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4957c bytes 65460494
+ 00b49618 bytes 72460494
- 00b49584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b49584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b49620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49584 bytes 60d604f9
+ 00b49620 bytes 605605f9
- 00b49564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b49564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49600 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b49600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49564 bytes 68d644f9
+ 00b49600 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19cadd6879b157a774acc9c969aa3298"></a>

### [`00b49598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md) → [`00b49634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49634.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49664",
      "incomplete_value": true,
      "site": "00b49664",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b495c8",
      "incomplete_value": true,
      "site": "00b495c8",
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
            "const:9a8:8"
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
      "definition_site": "00b49648",
      "incomplete_value": true,
      "site": "00b49648",
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
      "definition_site": "00b495ac",
      "incomplete_value": true,
      "site": "00b495ac",
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
      "definition_site": "00b49650",
      "incomplete_value": false,
      "site": "00b4965c",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b495b4",
      "incomplete_value": false,
      "site": "00b495c0",
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
            "const:139:8"
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
      "00b49644",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49650",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49664",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49644",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49650",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b49664",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b495c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495c0) · [`00b495c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495c8) · [`00b495a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49598.md#insn-00b495a8)
- 新版 `00b4965c`（命令位置の公開資料なし） · `00b49664`（命令位置の公開資料なし） · `00b49644`（命令位置の公開資料なし）

~~~diff
- 00b495c0 ["INT_ADD", "register:40f0:8", ["const:b495c0:8", "const:4:8"]]
- 00b495c0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4965c ["INT_ADD", "register:40f0:8", ["const:b4965c:8", "const:4:8"]]
+ 00b4965c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b495c0 bytes 54460494
+ 00b4965c bytes 61460494
- 00b495c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b495c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b49664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b495c8 bytes 60d604f9
+ 00b49664 bytes 605605f9
- 00b495a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b495a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
+ 00b49644 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b495a8 bytes 68d644f9
+ 00b49644 bytes 685645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e572234149c25f3da323a37ef7867fd"></a>

### [`00b495e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md) → [`00b49684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49684.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4970c",
      "incomplete_value": true,
      "site": "00b4970c",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49670",
      "incomplete_value": true,
      "site": "00b49670",
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
            "const:9b0:8"
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
      "definition_site": "00b496b8",
      "incomplete_value": true,
      "site": "00b496c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4961c",
      "incomplete_value": true,
      "site": "00b49628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "00b49698",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b496b8",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4970c",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49698",
      "READ",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b496b8",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4970c",
      "WRITE",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md#insn-00b49628) · [`00b49670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md#insn-00b49670) · [`00b495fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b495e8.md#insn-00b495fc)
- 新版 `00b496c4`（命令位置の公開資料なし） · `00b4970c`（命令位置の公開資料なし） · `00b49698`（命令位置の公開資料なし）

~~~diff
- 00b49628 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49628 ["INT_ADD", "register:40f0:8", ["const:b49628:8", "const:4:8"]]
- 00b49628 ["CALLIND", null, ["register:0:8"]]
+ 00b496c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b496c4 ["INT_ADD", "register:40f0:8", ["const:b496c4:8", "const:4:8"]]
+ 00b496c4 ["CALLIND", null, ["register:0:8"]]
- 00b49628 bytes 00013fd6
+ 00b496c4 bytes 00013fd6
- 00b49670 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49670 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00b49670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4970c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4970c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b4970c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49670 bytes a0c22639
+ 00b4970c bytes a0c22a39
- 00b495fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00b495fc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b495fc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b49698 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b49698 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b49698 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b495fc bytes a8c26639
+ 00b49698 bytes a8c26a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e415917538caf23441beec4887936f47"></a>

### [`00b49684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md) → [`00b49720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49720.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4975c",
      "incomplete_value": true,
      "site": "00b4975c",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b496c0",
      "incomplete_value": true,
      "site": "00b496c0",
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
            "const:9b0:8"
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
      "definition_site": "00b497ac",
      "incomplete_value": true,
      "site": "00b497ac",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49710",
      "incomplete_value": true,
      "site": "00b49710",
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
            "const:9a8:8"
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
      "definition_site": "00b49738",
      "incomplete_value": true,
      "site": "00b49738",
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
      "definition_site": "00b4969c",
      "incomplete_value": true,
      "site": "00b4969c",
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
      "00b49734",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49740",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4975c",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49734",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49740",
      "READ",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4975c",
      "WRITE",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b496c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md#insn-00b496c0) · [`00b4970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md#insn-00b4970c) · [`00b49710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49684.md#insn-00b49710)
- 新版 `00b4975c`（命令位置の公開資料なし） · `00b497a8`（命令位置の公開資料なし） · `00b497ac`（命令位置の公開資料なし）

~~~diff
- 00b496c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b496c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b496c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
- 00b496c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4975c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4975c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4975c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ab0:8"]]
+ 00b4975c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b496c0 bytes bfc22639
+ 00b4975c bytes bfc22a39
- 00b4970c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4970c ["INT_ADD", "register:40f0:8", ["const:b4970c:8", "const:4:8"]]
- 00b4970c ["CALLIND", null, ["register:0:8"]]
+ 00b497a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b497a8 ["INT_ADD", "register:40f0:8", ["const:b497a8:8", "const:4:8"]]
+ 00b497a8 ["CALLIND", null, ["register:0:8"]]
- 00b4970c bytes 00013fd6
+ 00b497a8 bytes 00013fd6
- 00b49710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b49710 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b497ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b497ac ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b497ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49710 bytes 9fd604f9
+ 00b497ac bytes 9f5605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cc10ccd4d919bee10d0b932e64f717"></a>

### [`00b49724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md) → [`00b497c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b497c0.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49800",
      "incomplete_value": true,
      "site": "00b49800",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49764",
      "incomplete_value": true,
      "site": "00b49764",
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
            "const:9a8:8"
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
      "definition_site": "00b497dc",
      "incomplete_value": true,
      "site": "00b497dc",
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
      "definition_site": "00b49740",
      "incomplete_value": true,
      "site": "00b49740",
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
      "definition_site": "00b497e4",
      "incomplete_value": false,
      "site": "00b497f8",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49748",
      "incomplete_value": false,
      "site": "00b4975c",
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
            "const:139:8"
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
      "00b497d4",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497e4",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b49800",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b497d4",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497e4",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b49800",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4975c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b4975c) · [`00b49764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b49764) · [`00b49738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49724.md#insn-00b49738)
- 新版 `00b497f8`（命令位置の公開資料なし） · `00b49800`（命令位置の公開資料なし） · `00b497d4`（命令位置の公開資料なし）

~~~diff
- 00b4975c ["INT_ADD", "register:40f0:8", ["const:b4975c:8", "const:4:8"]]
- 00b4975c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b497f8 ["INT_ADD", "register:40f0:8", ["const:b497f8:8", "const:4:8"]]
+ 00b497f8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4975c bytes ed450494
+ 00b497f8 bytes fa450494
- 00b49764 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b49764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49800 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b49800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49764 bytes 80d604f9
+ 00b49800 bytes 805605f9
- 00b49738 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b49738 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b497d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b497d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49738 bytes 81d644f9
+ 00b497d4 bytes 815645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01b9b196b3e5ba9425be92a111c7d9c7"></a>

### [`00b49794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md) → [`00b49830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49830.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b540.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b610.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4984c",
      "incomplete_value": false,
      "site": "00b49850",
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
      "definition_site": "00b497b0",
      "incomplete_value": false,
      "site": "00b497b4",
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
      "definition_site": "00b4985c",
      "incomplete_value": true,
      "site": "00b49868",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b497c0",
      "incomplete_value": true,
      "site": "00b497cc",
      "value": [
        "LOAD",
        "8",
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
      "00b4984c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4985c",
      "DATA",
      [
        "storage",
        "011259b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4984c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4985c",
      "DATA",
      [
        "storage",
        "01125ab8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b497b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497b4) · [`00b497b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497b0) · [`00b497bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49794.md#insn-00b497bc)
- 新版 `00b49850`（命令位置の公開資料なし） · `00b4984c`（命令位置の公開資料なし） · `00b49858`（命令位置の公開資料なし）

~~~diff
- 00b497b4 ["INT_ADD", "register:40f0:8", ["const:b497b4:8", "const:4:8"]]
- 00b497b4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b49850 ["INT_ADD", "register:40f0:8", ["const:b49850:8", "const:4:8"]]
+ 00b49850 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b497b4 bytes 13460494
+ 00b49850 bytes 20460494
- 00b497b0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b497b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b497b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b497b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4984c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4984c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4984c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4984c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b497b0 bytes 009c0d91
+ 00b4984c bytes 002c0c91
- 00b497bc ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00b497bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b497bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b497bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49858 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 00b49858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b497bc bytes 08e12691
+ 00b49858 bytes 08e12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea96ffd984e57765596c8ae09322fcf"></a>

### [`00b497d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md) → [`00b4986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4986c.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b498ac",
      "incomplete_value": true,
      "site": "00b498ac",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49810",
      "incomplete_value": true,
      "site": "00b49810",
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
            "const:9a8:8"
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
      "definition_site": "00b49888",
      "incomplete_value": true,
      "site": "00b49888",
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
      "definition_site": "00b497ec",
      "incomplete_value": true,
      "site": "00b497ec",
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
      "definition_site": "00b49890",
      "incomplete_value": false,
      "site": "00b498a4",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b497f4",
      "incomplete_value": false,
      "site": "00b49808",
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
            "const:139:8"
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
      "00b49880",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49890",
      "PARAM",
      [
        "storage",
        "002ae139",
        null,
        "string"
      ]
    ],
    [
      "00b498ac",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49880",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49890",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b498ac",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b49808) · [`00b49810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b49810) · [`00b497e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b497d0.md#insn-00b497e4)
- 新版 `00b498a4`（命令位置の公開資料なし） · `00b498ac`（命令位置の公開資料なし） · `00b49880`（命令位置の公開資料なし）

~~~diff
- 00b49808 ["INT_ADD", "register:40f0:8", ["const:b49808:8", "const:4:8"]]
- 00b49808 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b498a4 ["INT_ADD", "register:40f0:8", ["const:b498a4:8", "const:4:8"]]
+ 00b498a4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49808 bytes c2450494
+ 00b498a4 bytes cf450494
- 00b49810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b49810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b498ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b498ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49810 bytes 80d604f9
+ 00b498ac bytes 805605f9
- 00b497e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b497e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49880 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
+ 00b49880 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b497e4 bytes 81d644f9
+ 00b49880 bytes 815645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e4c2ef061e13450aee038be6d65619"></a>

### [`00b4987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md) → [`00b49918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49918.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b49944",
      "incomplete_value": true,
      "site": "00b49944",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498a8",
      "incomplete_value": true,
      "site": "00b498a8",
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
            "const:9d8:8"
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
      "definition_site": "00b4992c",
      "incomplete_value": true,
      "site": "00b4992c",
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
      "definition_site": "00b49890",
      "incomplete_value": true,
      "site": "00b49890",
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
      "definition_site": "00b49938",
      "incomplete_value": false,
      "site": "00b4993c",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4989c",
      "incomplete_value": false,
      "site": "00b498a0",
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
            "const:b17:8"
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
      "00b49928",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49938",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b49944",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49928",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49938",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b49944",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b498a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b498a0) · [`00b498a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b498a8) · [`00b4988c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b4987c.md#insn-00b4988c)
- 新版 `00b4993c`（命令位置の公開資料なし） · `00b49944`（命令位置の公開資料なし） · `00b49928`（命令位置の公開資料なし）

~~~diff
- 00b498a0 ["INT_ADD", "register:40f0:8", ["const:b498a0:8", "const:4:8"]]
- 00b498a0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4993c ["INT_ADD", "register:40f0:8", ["const:b4993c:8", "const:4:8"]]
+ 00b4993c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b498a0 bytes 9c450494
+ 00b4993c bytes a9450494
- 00b498a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b498a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b49944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b498a8 bytes 60ee04f9
+ 00b49944 bytes 606e05f9
- 00b4988c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b4988c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49928 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b49928 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4988c bytes 68ee44f9
+ 00b49928 bytes 686e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-179c5f7f764582fe43bda074b8605964"></a>

### [`00b498bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md) → [`00b49958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49958.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b49984",
      "incomplete_value": true,
      "site": "00b49984",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498e8",
      "incomplete_value": true,
      "site": "00b498e8",
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
            "const:9d8:8"
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
      "definition_site": "00b4996c",
      "incomplete_value": true,
      "site": "00b4996c",
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
      "definition_site": "00b498d0",
      "incomplete_value": true,
      "site": "00b498d0",
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
      "definition_site": "00b49974",
      "incomplete_value": false,
      "site": "00b4997c",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498d8",
      "incomplete_value": false,
      "site": "00b498e0",
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
            "const:b17:8"
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
      "00b49968",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49974",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b49984",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49968",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49974",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b49984",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b498e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498e0) · [`00b498e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498e8) · [`00b498cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498bc.md#insn-00b498cc)
- 新版 `00b4997c`（命令位置の公開資料なし） · `00b49984`（命令位置の公開資料なし） · `00b49968`（命令位置の公開資料なし）

~~~diff
- 00b498e0 ["INT_ADD", "register:40f0:8", ["const:b498e0:8", "const:4:8"]]
- 00b498e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4997c ["INT_ADD", "register:40f0:8", ["const:b4997c:8", "const:4:8"]]
+ 00b4997c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b498e0 bytes 8c450494
+ 00b4997c bytes 99450494
- 00b498e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b498e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b49984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b498e8 bytes 60ee04f9
+ 00b49984 bytes 606e05f9
- 00b498cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b498cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b49968 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b498cc bytes 68ee44f9
+ 00b49968 bytes 686e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b7859deb8a27d5bfeb3db22a6ed7ebf"></a>

### [`00b498fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md) → [`00b49998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49998.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b499c8",
      "incomplete_value": true,
      "site": "00b499c8",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4992c",
      "incomplete_value": true,
      "site": "00b4992c",
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
            "const:9d8:8"
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
      "definition_site": "00b499ac",
      "incomplete_value": true,
      "site": "00b499ac",
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
      "definition_site": "00b49910",
      "incomplete_value": true,
      "site": "00b49910",
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
      "definition_site": "00b499b8",
      "incomplete_value": false,
      "site": "00b499c0",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4991c",
      "incomplete_value": false,
      "site": "00b49924",
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
            "const:b17:8"
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
      "00b499a8",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b499b8",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "00b499c8",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b499a8",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b499b8",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b499c8",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b49924) · [`00b4992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b4992c) · [`00b4990c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b498fc.md#insn-00b4990c)
- 新版 `00b499c0`（命令位置の公開資料なし） · `00b499c8`（命令位置の公開資料なし） · `00b499a8`（命令位置の公開資料なし）

~~~diff
- 00b49924 ["INT_ADD", "register:40f0:8", ["const:b49924:8", "const:4:8"]]
- 00b49924 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b499c0 ["INT_ADD", "register:40f0:8", ["const:b499c0:8", "const:4:8"]]
+ 00b499c0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49924 bytes 7b450494
+ 00b499c0 bytes 88450494
- 00b4992c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b4992c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b499c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b499c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4992c bytes 60ee04f9
+ 00b499c8 bytes 606e05f9
- 00b4990c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b4990c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b499a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
+ 00b499a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4990c bytes 68ee44f9
+ 00b499a8 bytes 686e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5be02e305fb9cc7758fdca043407d36"></a>

### [`00b49940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md) → [`00b499dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b499dc.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49a0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b499f0",
      "incomplete_value": true,
      "site": "00b499f0",
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
      "definition_site": "00b49954",
      "incomplete_value": true,
      "site": "00b49954",
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
      "00b499ec",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4995c",
      "PARAM",
      [
        "storage",
        "002a3b17",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b49970",
      "WRITE",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b499ec",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b499f8",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b49a0c",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49954) · [`00b49968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49968) · [`00b49970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49940.md#insn-00b49970)
- 新版 `00b499f0`（命令位置の公開資料なし） · `00b49a04`（命令位置の公開資料なし）

~~~diff
- 00b49954 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49954 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b499f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b499f0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b49954 bytes 080100b5
+ 00b499f0 bytes 080100b5
- 00b49968 ["INT_ADD", "register:40f0:8", ["const:b49968:8", "const:4:8"]]
- 00b49968 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49a04 ["INT_ADD", "register:40f0:8", ["const:b49a04:8", "const:4:8"]]
+ 00b49a04 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49968 bytes 6a450494
+ 00b49a04 bytes 77450494
- 00b49970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
- 00b49970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49970 bytes 60ee04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1c1eaedf3ad419202d13121765fa80"></a>

### [`00b49990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49990.md) → [`00b49a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49a2c.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49994"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49990",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49994",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49998",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49a2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b49a30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49a34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49990.md#insn-00b49990) · [`00b49994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49990.md#insn-00b49994) · [`00b49998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49990.md#insn-00b49998)

~~~diff
- 00b49990 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b49990 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b49990 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49990 bytes f50f1df8
- 00b49994 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b49994 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b49994 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49994 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49994 bytes f44f01a9
- 00b49998 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49998 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49998 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b49998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49998 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6945703c75268c6ca31c41369d52e816"></a>

### [`00b49a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md) → [`00b49ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49b54",
      "incomplete_value": true,
      "site": "00b49b54",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ab8",
      "incomplete_value": true,
      "site": "00b49ab8",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49b04"
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
      "00b49adc",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ae8",
      "READ",
      [
        "storage",
        "011259e0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b49a68",
      "WRITE",
      [
        "storage",
        "011259e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49adc",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ae8",
      "READ",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49b04",
      "WRITE",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md#insn-00b49a64) · [`00b49a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md#insn-00b49a68) · [`00b49a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49a2c.md#insn-00b49a90)

~~~diff
- 00b49a64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49a64 ["INT_ADD", "register:40f0:8", ["const:b49a64:8", "const:4:8"]]
- 00b49a64 ["CALLIND", null, ["register:0:8"]]
- 00b49a64 bytes 00013fd6
- 00b49a68 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49a68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49a68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9e0:8"]]
- 00b49a68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49a68 bytes bf822739
- 00b49a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49a90 ["INT_ADD", "register:40f0:8", ["const:b49a90:8", "const:4:8"]]
- 00b49a90 ["CALLIND", null, ["register:0:8"]]
- 00b49a90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4733297f005b121e020a968e70f48290"></a>

### [`00b49acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md) → [`00b49b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49b68.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49ad0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49acc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49ad0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49ae0",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49b68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49b6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49b7c",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md#insn-00b49acc) · [`00b49ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md#insn-00b49ad0) · [`00b49ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49acc.md#insn-00b49ae8)

~~~diff
- 00b49acc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b49acc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b49acc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b49acc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49acc bytes f44fbea9
- 00b49ad0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49ad0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49ad0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49ad0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49ad0 bytes fd7b01a9
- 00b49ae8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49ae8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b49ae8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e11090e49ad9aa83827b61bb56d7ce05"></a>

### [`00b49b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md) → [`00b49bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49bd8.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b49bf4",
      "incomplete_value": false,
      "site": "00b49bf8",
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
      "definition_site": "00b49b58",
      "incomplete_value": false,
      "site": "00b49b5c",
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
      "definition_site": "00b49c04",
      "incomplete_value": true,
      "site": "00b49c10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49b68",
      "incomplete_value": true,
      "site": "00b49b74",
      "value": [
        "LOAD",
        "8",
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
      "00b49bf4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49c04",
      "DATA",
      [
        "storage",
        "011259e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49bf4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b49c04",
      "DATA",
      [
        "storage",
        "01125ae8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b5c) · [`00b49b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b58) · [`00b49b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b3c.md#insn-00b49b64)
- 新版 `00b49bf8`（命令位置の公開資料なし） · `00b49bf4`（命令位置の公開資料なし） · `00b49c00`（命令位置の公開資料なし）

~~~diff
- 00b49b5c ["INT_ADD", "register:40f0:8", ["const:b49b5c:8", "const:4:8"]]
- 00b49b5c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b49bf8 ["INT_ADD", "register:40f0:8", ["const:b49bf8:8", "const:4:8"]]
+ 00b49bf8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b49b5c bytes 29450494
+ 00b49bf8 bytes 36450494
- 00b49b58 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b49b58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49b58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49b58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49bf4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b49bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49b58 bytes 009c0d91
+ 00b49bf4 bytes 002c0c91
- 00b49b64 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00b49b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49c00 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00b49c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49b64 bytes 08a12791
+ 00b49c00 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad131571d2ec071e58c71bcfe429aa79"></a>

### [`00b49b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md) → [`00b49c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c14.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49b7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49b8c",
      "READ",
      [
        "storage",
        "011259d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49c18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49c28",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md#insn-00b49b78) · [`00b49b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md#insn-00b49b7c) · [`00b49b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49b78.md#insn-00b49b94)

~~~diff
- 00b49b78 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b49b78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b49b78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b49b78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49b78 bytes f44fbea9
- 00b49b7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49b7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49b7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49b7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49b7c bytes fd7b01a9
- 00b49b94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49b94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b49b94 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4843999a89adfaba048018dd95a19aff"></a>

### [`00b49c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md) → [`00b49d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d00.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49d2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49d14",
      "incomplete_value": true,
      "site": "00b49d14",
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
      "definition_site": "00b49c78",
      "incomplete_value": true,
      "site": "00b49c78",
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
      "00b49d10",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49c94"
      ]
    ],
    [
      "unmatched:00b49c80",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49d10",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49d30"
      ]
    ],
    [
      "00b49d1c",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49c88) · [`00b49c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49c90) · [`00b49ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c64.md#insn-00b49ca0)

~~~diff
- 00b49c88 ["INT_ADD", "register:40f0:8", ["const:b49c88:8", "const:4:8"]]
- 00b49c88 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49c88 bytes a2440494
- 00b49c90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00b49c90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49c90 bytes 600a05f9
- 00b49ca0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49ca0 ["RETURN", null, ["register:0:8"]]
- 00b49ca0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26456682d1c042c609435927ae377434"></a>

### [`00b49ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ca4.md) → [`00b49d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d40.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00b49ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49ca8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49d50",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49d50",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ca4.md#insn-00b49ca4) · [`00b49ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ca4.md#insn-00b49ca8) · [`00b49cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ca4.md#insn-00b49cb8)
- 新版 `00b49d54`（命令位置の公開資料なし）

~~~diff
- 00b49ca4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b49ca4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b49ca4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49ca4 bytes f30f1ef8
- 00b49ca8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49ca8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49ca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49ca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49ca8 bytes fd7b01a9
- 00b49cb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49cb8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b49d54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b49d54 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49cb8 bytes 080100b5
+ 00b49d54 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b435adb2a422949b9e29737ba9c2426c"></a>

### [`00b49ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md) → [`00b49d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d84.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49db4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49d98",
      "incomplete_value": true,
      "site": "00b49d98",
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
      "definition_site": "00b49cfc",
      "incomplete_value": true,
      "site": "00b49cfc",
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
      "00b49d94",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49d1c"
      ]
    ],
    [
      "unmatched:00b49d04",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49d94",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49db8"
      ]
    ],
    [
      "00b49da0",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49d10) · [`00b49d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49d18) · [`00b49d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ce8.md#insn-00b49d28)
- 新版 `00b49dac`（命令位置の公開資料なし）

~~~diff
- 00b49d10 ["INT_ADD", "register:40f0:8", ["const:b49d10:8", "const:4:8"]]
- 00b49d10 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49dac ["INT_ADD", "register:40f0:8", ["const:b49dac:8", "const:4:8"]]
+ 00b49dac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49d10 bytes 80440494
+ 00b49dac bytes 8d440494
- 00b49d18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a10:8"]]
- 00b49d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49d18 bytes 600a05f9
- 00b49d28 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49d28 ["RETURN", null, ["register:0:8"]]
- 00b49d28 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b8406c85836ab6d53370542a52e74c"></a>

### [`00b49d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md) → [`00b49dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dd4.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49e5c",
      "incomplete_value": true,
      "site": "00b49e5c",
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
    "old": {
      "definition_site": "00b49dc0",
      "incomplete_value": true,
      "site": "00b49dc0",
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
            "const:a18:8"
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
      "definition_site": "00b49e08",
      "incomplete_value": true,
      "site": "00b49e14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b49d6c",
      "incomplete_value": true,
      "site": "00b49d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
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
      "00b49de8",
      "READ",
      [
        "storage",
        "01125a18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49e08",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e5c",
      "WRITE",
      [
        "storage",
        "01125a18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49de8",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49e08",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e5c",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49d78) · [`00b49dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49dc0) · [`00b49d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49d38.md#insn-00b49d4c)
- 新版 `00b49e14`（命令位置の公開資料なし） · `00b49e5c`（命令位置の公開資料なし） · `00b49de8`（命令位置の公開資料なし）

~~~diff
- 00b49d78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49d78 ["INT_ADD", "register:40f0:8", ["const:b49d78:8", "const:4:8"]]
- 00b49d78 ["CALLIND", null, ["register:0:8"]]
+ 00b49e14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49e14 ["INT_ADD", "register:40f0:8", ["const:b49e14:8", "const:4:8"]]
+ 00b49e14 ["CALLIND", null, ["register:0:8"]]
- 00b49d78 bytes 00013fd6
+ 00b49e14 bytes 00013fd6
- 00b49dc0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49dc0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a18:8"]]
- 00b49dc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49e5c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49e5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b18:8"]]
+ 00b49e5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49dc0 bytes a0622839
+ 00b49e5c bytes a0622c39
- 00b49d4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a18:8"]]
- 00b49d4c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b49d4c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b49de8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b18:8"]]
+ 00b49de8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b49de8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b49d4c bytes a8626839
+ 00b49de8 bytes a8626c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bb222d3e3efcbe9cc148d77d672b59e"></a>

### [`00b49dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49dd4.md) → [`00b49e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49e70.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 10.00% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49eac"
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
      "00b49e84",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49e64"
      ]
    ],
    [
      "00b49e90",
      "READ",
      [
        "storage",
        "01125a18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49e84",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f00"
      ]
    ],
    [
      "00b49e90",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49dd4.md#insn-00b49e10) · [`00b49e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49dd4.md#insn-00b49e20) · [`00b49e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49dd4.md#insn-00b49e48)

~~~diff
- 00b49e10 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49e10 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49e10 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a18:8"]]
- 00b49e10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49e10 bytes bf622839
- 00b49e20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49e20 ["INT_ADD", "register:40f0:8", ["const:b49e20:8", "const:4:8"]]
- 00b49e20 ["CALLIND", null, ["register:0:8"]]
- 00b49e20 bytes 00013fd6
- 00b49e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49e48 ["INT_ADD", "register:40f0:8", ["const:b49e48:8", "const:4:8"]]
- 00b49e48 ["CALLIND", null, ["register:0:8"]]
- 00b49e48 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1abe629f29cfc56f5d6cfd731d24f3a"></a>

### [`00b49e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md) → [`00b49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f10.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b49eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49f50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49e90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49e88",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49e90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f54"
      ]
    ],
    [
      "unmatched:00b49e98",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49f24",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f54"
      ]
    ],
    [
      "00b49f34",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md#insn-00b49e90) · [`00b49eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md#insn-00b49eac) · [`00b49eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49e74.md#insn-00b49eb4)
- 新版 `00b49f48`（命令位置の公開資料なし）

~~~diff
- 00b49e90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49e90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b49e90 bytes 410100b5
- 00b49eac ["INT_ADD", "register:40f0:8", ["const:b49eac:8", "const:4:8"]]
- 00b49eac ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49f48 ["INT_ADD", "register:40f0:8", ["const:b49f48:8", "const:4:8"]]
+ 00b49f48 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49eac bytes 19440494
+ 00b49f48 bytes 26440494
- 00b49eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00b49eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49eb4 bytes 800a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9656af8c862bf376f6a46210573f0a21"></a>

### [`00b49ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md) → [`00b49f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f80.md) _ZN8firebase4util4date11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b49f9c",
      "incomplete_value": false,
      "site": "00b49fa0",
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
      "definition_site": "00b49f00",
      "incomplete_value": false,
      "site": "00b49f04",
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
      "definition_site": "00b49fac",
      "incomplete_value": true,
      "site": "00b49fb8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49f10",
      "incomplete_value": true,
      "site": "00b49f1c",
      "value": [
        "LOAD",
        "8",
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
      "00b49f9c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49fac",
      "DATA",
      [
        "storage",
        "01125a20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49f9c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b49fac",
      "DATA",
      [
        "storage",
        "01125b20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md#insn-00b49f04) · [`00b49f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md#insn-00b49f00) · [`00b49f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md#insn-00b49f0c)
- 新版 `00b49fa0`（命令位置の公開資料なし） · `00b49f9c`（命令位置の公開資料なし） · `00b49fa8`（命令位置の公開資料なし）

~~~diff
- 00b49f04 ["INT_ADD", "register:40f0:8", ["const:b49f04:8", "const:4:8"]]
- 00b49f04 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b49fa0 ["INT_ADD", "register:40f0:8", ["const:b49fa0:8", "const:4:8"]]
+ 00b49fa0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b49f04 bytes 3f440494
+ 00b49fa0 bytes 4c440494
- 00b49f00 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b49f00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49f9c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b49f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49f00 bytes 009c0d91
+ 00b49f9c bytes 002c0c91
- 00b49f0c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00b49f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49fa8 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00b49fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49f0c bytes 08812891
+ 00b49fa8 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ef64563943314b30d065dc41c2670c7"></a>

### [`00b49f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md) → [`00b49fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49fbc.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49ffc",
      "incomplete_value": true,
      "site": "00b49ffc",
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
    "old": {
      "definition_site": "00b49f60",
      "incomplete_value": true,
      "site": "00b49f60",
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
            "const:a10:8"
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
      "definition_site": "00b49fd8",
      "incomplete_value": true,
      "site": "00b49fd8",
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
      "definition_site": "00b49f3c",
      "incomplete_value": true,
      "site": "00b49f3c",
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
      "definition_site": "00b49fe0",
      "incomplete_value": false,
      "site": "00b49ff4",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f44",
      "incomplete_value": false,
      "site": "00b49f58",
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
            "const:41e:8"
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
      "00b49fd0",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fe0",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ],
    [
      "00b49ffc",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49fd0",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fe0",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b49ffc",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md#insn-00b49f58) · [`00b49f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md#insn-00b49f60) · [`00b49f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md#insn-00b49f34)
- 新版 `00b49ff4`（命令位置の公開資料なし） · `00b49ffc`（命令位置の公開資料なし） · `00b49fd0`（命令位置の公開資料なし）

~~~diff
- 00b49f58 ["INT_ADD", "register:40f0:8", ["const:b49f58:8", "const:4:8"]]
- 00b49f58 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b49ff4 ["INT_ADD", "register:40f0:8", ["const:b49ff4:8", "const:4:8"]]
+ 00b49ff4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49f58 bytes ee430494
+ 00b49ff4 bytes fb430494
- 00b49f60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00b49f60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
+ 00b49ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49f60 bytes 800a05f9
+ 00b49ffc bytes 808a05f9
- 00b49f34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a10:8"]]
- 00b49f34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49fd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
+ 00b49fd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49f34 bytes 810a45f9
+ 00b49fd0 bytes 818a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b94328db826aec5bcb05a1ce7df5deb"></a>

### [`00b49f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md) → [`00b4a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a02c.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4a048",
      "incomplete_value": false,
      "site": "00b4a04c",
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
      "definition_site": "00b49fac",
      "incomplete_value": false,
      "site": "00b49fb0",
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
      "definition_site": "00b4a058",
      "incomplete_value": true,
      "site": "00b4a064",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b49fbc",
      "incomplete_value": true,
      "site": "00b49fc8",
      "value": [
        "LOAD",
        "8",
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
      "00b4a048",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4a058",
      "DATA",
      [
        "storage",
        "01125a38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a048",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a058",
      "DATA",
      [
        "storage",
        "01125b38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fb0) · [`00b49fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fac) · [`00b49fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fb8)
- 新版 `00b4a04c`（命令位置の公開資料なし） · `00b4a048`（命令位置の公開資料なし） · `00b4a054`（命令位置の公開資料なし）

~~~diff
- 00b49fb0 ["INT_ADD", "register:40f0:8", ["const:b49fb0:8", "const:4:8"]]
- 00b49fb0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4a04c ["INT_ADD", "register:40f0:8", ["const:b4a04c:8", "const:4:8"]]
+ 00b4a04c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b49fb0 bytes 14440494
+ 00b4a04c bytes 21440494
- 00b49fac ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b49fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a048 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4a048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49fac bytes 00781491
+ 00b4a048 bytes 00341591
- 00b49fb8 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00b49fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a054 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00b4a054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49fb8 bytes 08e12891
+ 00b4a054 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c20e038d580ef1adeb2af65717c1108d"></a>

### [`00b49fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md) → [`00b4a068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a068.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00b4a094",
      "incomplete_value": true,
      "site": "00b4a094",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ff8",
      "incomplete_value": true,
      "site": "00b49ff8",
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
            "const:a40:8"
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
      "definition_site": "00b4a07c",
      "incomplete_value": true,
      "site": "00b4a07c",
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
      "definition_site": "00b49fe0",
      "incomplete_value": true,
      "site": "00b49fe0",
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
      "definition_site": "00b4a088",
      "incomplete_value": false,
      "site": "00b4a08c",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fec",
      "incomplete_value": false,
      "site": "00b49ff0",
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
            "const:c74:8"
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
      "00b4a078",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a088",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a094",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a078",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a088",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a094",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49ff0) · [`00b49ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49ff8) · [`00b49fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49fdc)
- 新版 `00b4a08c`（命令位置の公開資料なし） · `00b4a094`（命令位置の公開資料なし） · `00b4a078`（命令位置の公開資料なし）

~~~diff
- 00b49ff0 ["INT_ADD", "register:40f0:8", ["const:b49ff0:8", "const:4:8"]]
- 00b49ff0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a08c ["INT_ADD", "register:40f0:8", ["const:b4a08c:8", "const:4:8"]]
+ 00b4a08c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b49ff0 bytes c8430494
+ 00b4a08c bytes d5430494
- 00b49ff8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b49ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49ff8 bytes 602205f9
+ 00b4a094 bytes 60a205f9
- 00b49fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b49fdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a078 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a078 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49fdc bytes 682245f9
+ 00b4a078 bytes 68a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5604d44cdeec0d770f158449eb37fbd3"></a>

### [`00b4a00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md) → [`00b4a0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0a8.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00b4a0d4",
      "incomplete_value": true,
      "site": "00b4a0d4",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a038",
      "incomplete_value": true,
      "site": "00b4a038",
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
            "const:a40:8"
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
      "definition_site": "00b4a0bc",
      "incomplete_value": true,
      "site": "00b4a0bc",
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
      "definition_site": "00b4a020",
      "incomplete_value": true,
      "site": "00b4a020",
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
      "definition_site": "00b4a0c4",
      "incomplete_value": false,
      "site": "00b4a0cc",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a028",
      "incomplete_value": false,
      "site": "00b4a030",
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
            "const:c74:8"
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
      "00b4a0b8",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0c4",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a0d4",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a0b8",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0c4",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a0d4",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a030) · [`00b4a038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a038) · [`00b4a01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a01c)
- 新版 `00b4a0cc`（命令位置の公開資料なし） · `00b4a0d4`（命令位置の公開資料なし） · `00b4a0b8`（命令位置の公開資料なし）

~~~diff
- 00b4a030 ["INT_ADD", "register:40f0:8", ["const:b4a030:8", "const:4:8"]]
- 00b4a030 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a0cc ["INT_ADD", "register:40f0:8", ["const:b4a0cc:8", "const:4:8"]]
+ 00b4a0cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a030 bytes b8430494
+ 00b4a0cc bytes c5430494
- 00b4a038 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a038 bytes 602205f9
+ 00b4a0d4 bytes 60a205f9
- 00b4a01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a01c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a0b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a0b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a01c bytes 682245f9
+ 00b4a0b8 bytes 68a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9197fffe2bd7ff1f527dceb0a3190e8"></a>

### [`00b4a04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md) → [`00b4a0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0e8.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4a118",
      "incomplete_value": true,
      "site": "00b4a118",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a07c",
      "incomplete_value": true,
      "site": "00b4a07c",
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
            "const:a40:8"
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
      "definition_site": "00b4a0fc",
      "incomplete_value": true,
      "site": "00b4a0fc",
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
      "definition_site": "00b4a060",
      "incomplete_value": true,
      "site": "00b4a060",
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
      "definition_site": "00b4a108",
      "incomplete_value": false,
      "site": "00b4a110",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a06c",
      "incomplete_value": false,
      "site": "00b4a074",
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
            "const:c74:8"
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
      "00b4a0f8",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a108",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a118",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a0f8",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a108",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a118",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md#insn-00b4a074) · [`00b4a07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md#insn-00b4a07c) · [`00b4a05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md#insn-00b4a05c)
- 新版 `00b4a110`（命令位置の公開資料なし） · `00b4a118`（命令位置の公開資料なし） · `00b4a0f8`（命令位置の公開資料なし）

~~~diff
- 00b4a074 ["INT_ADD", "register:40f0:8", ["const:b4a074:8", "const:4:8"]]
- 00b4a074 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a110 ["INT_ADD", "register:40f0:8", ["const:b4a110:8", "const:4:8"]]
+ 00b4a110 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a074 bytes a7430494
+ 00b4a110 bytes b4430494
- 00b4a07c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a07c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a07c bytes 602205f9
+ 00b4a118 bytes 60a205f9
- 00b4a05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a05c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a0f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a05c bytes 682245f9
+ 00b4a0f8 bytes 68a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26e5d73372e710b519bae25f9a82252"></a>

### [`00b4a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md) → [`00b4a12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a12c.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a15c",
      "incomplete_value": true,
      "site": "00b4a15c",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0c0",
      "incomplete_value": true,
      "site": "00b4a0c0",
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
            "const:a40:8"
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
      "definition_site": "00b4a140",
      "incomplete_value": true,
      "site": "00b4a140",
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
      "definition_site": "00b4a0a4",
      "incomplete_value": true,
      "site": "00b4a0a4",
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
      "definition_site": "00b4a148",
      "incomplete_value": false,
      "site": "00b4a154",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0ac",
      "incomplete_value": false,
      "site": "00b4a0b8",
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
            "const:c74:8"
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
      "00b4a13c",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a148",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a15c",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a13c",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a148",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a15c",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md#insn-00b4a0b8) · [`00b4a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md#insn-00b4a0c0) · [`00b4a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md#insn-00b4a0a0)
- 新版 `00b4a154`（命令位置の公開資料なし） · `00b4a15c`（命令位置の公開資料なし） · `00b4a13c`（命令位置の公開資料なし）

~~~diff
- 00b4a0b8 ["INT_ADD", "register:40f0:8", ["const:b4a0b8:8", "const:4:8"]]
- 00b4a0b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a154 ["INT_ADD", "register:40f0:8", ["const:b4a154:8", "const:4:8"]]
+ 00b4a154 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a0b8 bytes 96430494
+ 00b4a154 bytes a3430494
- 00b4a0c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a0c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a0c0 bytes 602205f9
+ 00b4a15c bytes 60a205f9
- 00b4a0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
- 00b4a0a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a13c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
+ 00b4a13c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a0a0 bytes 682245f9
+ 00b4a13c bytes 68a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18d881258ff24e6d7b0a32ea3c9aa2fc"></a>

### [`00b4a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md) → [`00b4a17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a17c.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4a204",
      "incomplete_value": true,
      "site": "00b4a204",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a168",
      "incomplete_value": true,
      "site": "00b4a168",
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
            "const:a48:8"
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
      "definition_site": "00b4a1b0",
      "incomplete_value": true,
      "site": "00b4a1bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a114",
      "incomplete_value": true,
      "site": "00b4a120",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
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
      "00b4a190",
      "READ",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a1b0",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a204",
      "WRITE",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a190",
      "READ",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a1b0",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a204",
      "WRITE",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a120) · [`00b4a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a168) · [`00b4a0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a0f4)
- 新版 `00b4a1bc`（命令位置の公開資料なし） · `00b4a204`（命令位置の公開資料なし） · `00b4a190`（命令位置の公開資料なし）

~~~diff
- 00b4a120 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a120 ["INT_ADD", "register:40f0:8", ["const:b4a120:8", "const:4:8"]]
- 00b4a120 ["CALLIND", null, ["register:0:8"]]
+ 00b4a1bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a1bc ["INT_ADD", "register:40f0:8", ["const:b4a1bc:8", "const:4:8"]]
+ 00b4a1bc ["CALLIND", null, ["register:0:8"]]
- 00b4a120 bytes 00013fd6
+ 00b4a1bc bytes 00013fd6
- 00b4a168 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a168 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a48:8"]]
- 00b4a168 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a204 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a204 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b48:8"]]
+ 00b4a204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a168 bytes a0222939
+ 00b4a204 bytes a0222d39
- 00b4a0f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a48:8"]]
- 00b4a0f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a0f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a190 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b48:8"]]
+ 00b4a190 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a190 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a0f4 bytes a8226939
+ 00b4a190 bytes a8226d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62d57228b1f8f4b4127411958f2c8664"></a>

### [`00b4a17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md) → [`00b4a218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a218.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4a254",
      "incomplete_value": true,
      "site": "00b4a254",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a1b8",
      "incomplete_value": true,
      "site": "00b4a1b8",
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
            "const:a48:8"
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
      "definition_site": "00b4a2a4",
      "incomplete_value": true,
      "site": "00b4a2a4",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a208",
      "incomplete_value": true,
      "site": "00b4a208",
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
            "const:a40:8"
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
      "definition_site": "00b4a230",
      "incomplete_value": true,
      "site": "00b4a230",
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
      "definition_site": "00b4a194",
      "incomplete_value": true,
      "site": "00b4a194",
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
      "00b4a22c",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a238",
      "READ",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a254",
      "WRITE",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a22c",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a238",
      "READ",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a254",
      "WRITE",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a1b8) · [`00b4a204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a204) · [`00b4a208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a208)
- 新版 `00b4a254`（命令位置の公開資料なし） · `00b4a2a0`（命令位置の公開資料なし） · `00b4a2a4`（命令位置の公開資料なし）

~~~diff
- 00b4a1b8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a1b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a1b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a48:8"]]
- 00b4a1b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a254 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a254 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a254 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b48:8"]]
+ 00b4a254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a1b8 bytes bf222939
+ 00b4a254 bytes bf222d39
- 00b4a204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a204 ["INT_ADD", "register:40f0:8", ["const:b4a204:8", "const:4:8"]]
- 00b4a204 ["CALLIND", null, ["register:0:8"]]
+ 00b4a2a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a2a0 ["INT_ADD", "register:40f0:8", ["const:b4a2a0:8", "const:4:8"]]
+ 00b4a2a0 ["CALLIND", null, ["register:0:8"]]
- 00b4a204 bytes 00013fd6
+ 00b4a2a0 bytes 00013fd6
- 00b4a208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
- 00b4a208 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a2a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00b4a2a4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a208 bytes 9f2205f9
+ 00b4a2a4 bytes 9fa205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef9eb43bb04916a1f2d495ad6893d663"></a>

### [`00b4a21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md) → [`00b4a2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a2b8.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a2f8",
      "incomplete_value": true,
      "site": "00b4a2f8",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a25c",
      "incomplete_value": true,
      "site": "00b4a25c",
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
            "const:a40:8"
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
      "definition_site": "00b4a2d4",
      "incomplete_value": true,
      "site": "00b4a2d4",
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
      "definition_site": "00b4a238",
      "incomplete_value": true,
      "site": "00b4a238",
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
      "definition_site": "00b4a2dc",
      "incomplete_value": false,
      "site": "00b4a2f0",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a240",
      "incomplete_value": false,
      "site": "00b4a254",
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
            "const:c74:8"
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
      "00b4a2cc",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a2dc",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a2f8",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a2cc",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a2dc",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a2f8",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a254) · [`00b4a25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a25c) · [`00b4a230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a230)
- 新版 `00b4a2f0`（命令位置の公開資料なし） · `00b4a2f8`（命令位置の公開資料なし） · `00b4a2cc`（命令位置の公開資料なし）

~~~diff
- 00b4a254 ["INT_ADD", "register:40f0:8", ["const:b4a254:8", "const:4:8"]]
- 00b4a254 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a2f0 ["INT_ADD", "register:40f0:8", ["const:b4a2f0:8", "const:4:8"]]
+ 00b4a2f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a254 bytes 2f430494
+ 00b4a2f0 bytes 3c430494
- 00b4a25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
- 00b4a25c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a2f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00b4a2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a25c bytes 802205f9
+ 00b4a2f8 bytes 80a205f9
- 00b4a230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
- 00b4a230 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a2cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00b4a2cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a230 bytes 812245f9
+ 00b4a2cc bytes 81a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997d9ae7cef5a0dc1dad3b5c76bec8b0"></a>

### [`00b4a28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md) → [`00b4a328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a328.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b290.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b360.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4a344",
      "incomplete_value": false,
      "site": "00b4a348",
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
      "definition_site": "00b4a2a8",
      "incomplete_value": false,
      "site": "00b4a2ac",
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
      "definition_site": "00b4a354",
      "incomplete_value": true,
      "site": "00b4a360",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4a2b8",
      "incomplete_value": true,
      "site": "00b4a2c4",
      "value": [
        "LOAD",
        "8",
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
      "00b4a344",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4a354",
      "DATA",
      [
        "storage",
        "01125a50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a344",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4a354",
      "DATA",
      [
        "storage",
        "01125b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2ac) · [`00b4a2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2a8) · [`00b4a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2b4)
- 新版 `00b4a348`（命令位置の公開資料なし） · `00b4a344`（命令位置の公開資料なし） · `00b4a350`（命令位置の公開資料なし）

~~~diff
- 00b4a2ac ["INT_ADD", "register:40f0:8", ["const:b4a2ac:8", "const:4:8"]]
- 00b4a2ac ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4a348 ["INT_ADD", "register:40f0:8", ["const:b4a348:8", "const:4:8"]]
+ 00b4a348 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4a2ac bytes 55430494
+ 00b4a348 bytes 62430494
- 00b4a2a8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4a2a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a2a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a2a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a344 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4a344 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a344 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a344 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a2a8 bytes 009c0d91
+ 00b4a344 bytes 002c0c91
- 00b4a2b4 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00b4a2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a350 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00b4a350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a2b4 bytes 08412991
+ 00b4a350 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50875e7dec451c57bc92ce5daaff4466"></a>

### [`00b4a2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md) → [`00b4a364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a364.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a3a4",
      "incomplete_value": true,
      "site": "00b4a3a4",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a308",
      "incomplete_value": true,
      "site": "00b4a308",
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
            "const:a40:8"
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
      "definition_site": "00b4a380",
      "incomplete_value": true,
      "site": "00b4a380",
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
      "definition_site": "00b4a2e4",
      "incomplete_value": true,
      "site": "00b4a2e4",
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
      "definition_site": "00b4a388",
      "incomplete_value": false,
      "site": "00b4a39c",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2ec",
      "incomplete_value": false,
      "site": "00b4a300",
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
            "const:c74:8"
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
      "00b4a378",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a388",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a4",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a378",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a388",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a4",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a300) · [`00b4a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a308) · [`00b4a2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a2dc)
- 新版 `00b4a39c`（命令位置の公開資料なし） · `00b4a3a4`（命令位置の公開資料なし） · `00b4a378`（命令位置の公開資料なし）

~~~diff
- 00b4a300 ["INT_ADD", "register:40f0:8", ["const:b4a300:8", "const:4:8"]]
- 00b4a300 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a39c ["INT_ADD", "register:40f0:8", ["const:b4a39c:8", "const:4:8"]]
+ 00b4a39c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a300 bytes 04430494
+ 00b4a39c bytes 11430494
- 00b4a308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
- 00b4a308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a3a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00b4a3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a308 bytes 802205f9
+ 00b4a3a4 bytes 80a205f9
- 00b4a2dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
- 00b4a2dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a378 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00b4a378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a2dc bytes 812245f9
+ 00b4a378 bytes 81a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-689e3ed4442c47249c0e2ee2e7993def"></a>

### [`00b4a338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md) → [`00b4a3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a3d4.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4a3f0",
      "incomplete_value": false,
      "site": "00b4a3f4",
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
      "definition_site": "00b4a354",
      "incomplete_value": false,
      "site": "00b4a358",
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
      "definition_site": "00b4a400",
      "incomplete_value": true,
      "site": "00b4a40c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4a364",
      "incomplete_value": true,
      "site": "00b4a370",
      "value": [
        "LOAD",
        "8",
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
      "00b4a3f0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4a400",
      "DATA",
      [
        "storage",
        "01125a60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a3f0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a400",
      "DATA",
      [
        "storage",
        "01125b60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a358) · [`00b4a354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a354) · [`00b4a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a360)
- 新版 `00b4a3f4`（命令位置の公開資料なし） · `00b4a3f0`（命令位置の公開資料なし） · `00b4a3fc`（命令位置の公開資料なし）

~~~diff
- 00b4a358 ["INT_ADD", "register:40f0:8", ["const:b4a358:8", "const:4:8"]]
- 00b4a358 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4a3f4 ["INT_ADD", "register:40f0:8", ["const:b4a3f4:8", "const:4:8"]]
+ 00b4a3f4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4a358 bytes 2a430494
+ 00b4a3f4 bytes 37430494
- 00b4a354 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4a354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a3f0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4a3f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a3f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a3f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a354 bytes 00781491
+ 00b4a3f0 bytes 00341591
- 00b4a360 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00b4a360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a3fc ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00b4a3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a360 bytes 08812991
+ 00b4a3fc bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af5ef2877477fa99ba28dd3ddb37a4b"></a>

### [`00b4a374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md) → [`00b4a410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a410.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b4a43c",
      "incomplete_value": true,
      "site": "00b4a43c",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3a0",
      "incomplete_value": true,
      "site": "00b4a3a0",
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
            "const:a68:8"
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
      "definition_site": "00b4a424",
      "incomplete_value": true,
      "site": "00b4a424",
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
      "definition_site": "00b4a388",
      "incomplete_value": true,
      "site": "00b4a388",
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
      "definition_site": "00b4a430",
      "incomplete_value": false,
      "site": "00b4a434",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a394",
      "incomplete_value": false,
      "site": "00b4a398",
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
            "const:b11:8"
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
      "00b4a420",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a430",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a43c",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a420",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a430",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a43c",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a398) · [`00b4a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a3a0) · [`00b4a384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a384)
- 新版 `00b4a434`（命令位置の公開資料なし） · `00b4a43c`（命令位置の公開資料なし） · `00b4a420`（命令位置の公開資料なし）

~~~diff
- 00b4a398 ["INT_ADD", "register:40f0:8", ["const:b4a398:8", "const:4:8"]]
- 00b4a398 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a434 ["INT_ADD", "register:40f0:8", ["const:b4a434:8", "const:4:8"]]
+ 00b4a434 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a398 bytes de420494
+ 00b4a434 bytes eb420494
- 00b4a3a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a3a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a3a0 bytes 603605f9
+ 00b4a43c bytes 60b605f9
- 00b4a384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a420 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a384 bytes 683645f9
+ 00b4a420 bytes 68b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c2ba183a97fb2febe23df6c0d32a5f"></a>

### [`00b4a3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md) → [`00b4a450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a450.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4a47c",
      "incomplete_value": true,
      "site": "00b4a47c",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3e0",
      "incomplete_value": true,
      "site": "00b4a3e0",
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
            "const:a68:8"
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
      "definition_site": "00b4a464",
      "incomplete_value": true,
      "site": "00b4a464",
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
      "definition_site": "00b4a3c8",
      "incomplete_value": true,
      "site": "00b4a3c8",
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
      "definition_site": "00b4a46c",
      "incomplete_value": false,
      "site": "00b4a474",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3d0",
      "incomplete_value": false,
      "site": "00b4a3d8",
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
            "const:b11:8"
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
      "00b4a460",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a46c",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a47c",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a460",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a46c",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a47c",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3d8) · [`00b4a3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3e0) · [`00b4a3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3c4)
- 新版 `00b4a474`（命令位置の公開資料なし） · `00b4a47c`（命令位置の公開資料なし） · `00b4a460`（命令位置の公開資料なし）

~~~diff
- 00b4a3d8 ["INT_ADD", "register:40f0:8", ["const:b4a3d8:8", "const:4:8"]]
- 00b4a3d8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a474 ["INT_ADD", "register:40f0:8", ["const:b4a474:8", "const:4:8"]]
+ 00b4a474 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a3d8 bytes ce420494
+ 00b4a474 bytes db420494
- 00b4a3e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a3e0 bytes 603605f9
+ 00b4a47c bytes 60b605f9
- 00b4a3c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a3c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a460 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a3c4 bytes 683645f9
+ 00b4a460 bytes 68b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6003c93743ca9cfb5212c6777ea17ac2"></a>

### [`00b4a3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md) → [`00b4a490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a490.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4a4c0",
      "incomplete_value": true,
      "site": "00b4a4c0",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a424",
      "incomplete_value": true,
      "site": "00b4a424",
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
            "const:a68:8"
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
      "definition_site": "00b4a4a4",
      "incomplete_value": true,
      "site": "00b4a4a4",
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
      "definition_site": "00b4a408",
      "incomplete_value": true,
      "site": "00b4a408",
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
      "definition_site": "00b4a4b0",
      "incomplete_value": false,
      "site": "00b4a4b8",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a414",
      "incomplete_value": false,
      "site": "00b4a41c",
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
            "const:b11:8"
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
      "00b4a4a0",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4b0",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a4c0",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a4a0",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4b0",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a4c0",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a41c) · [`00b4a424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a424) · [`00b4a404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a404)
- 新版 `00b4a4b8`（命令位置の公開資料なし） · `00b4a4c0`（命令位置の公開資料なし） · `00b4a4a0`（命令位置の公開資料なし）

~~~diff
- 00b4a41c ["INT_ADD", "register:40f0:8", ["const:b4a41c:8", "const:4:8"]]
- 00b4a41c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a4b8 ["INT_ADD", "register:40f0:8", ["const:b4a4b8:8", "const:4:8"]]
+ 00b4a4b8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a41c bytes bd420494
+ 00b4a4b8 bytes ca420494
- 00b4a424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a424 bytes 603605f9
+ 00b4a4c0 bytes 60b605f9
- 00b4a404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a4a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a4a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a404 bytes 683645f9
+ 00b4a4a0 bytes 68b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa148d35a580cdeee07564cbd906761f"></a>

### [`00b4a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md) → [`00b4a4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a4d4.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a504",
      "incomplete_value": true,
      "site": "00b4a504",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a468",
      "incomplete_value": true,
      "site": "00b4a468",
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
            "const:a68:8"
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
      "definition_site": "00b4a4e8",
      "incomplete_value": true,
      "site": "00b4a4e8",
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
      "definition_site": "00b4a44c",
      "incomplete_value": true,
      "site": "00b4a44c",
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
      "definition_site": "00b4a4f0",
      "incomplete_value": false,
      "site": "00b4a4fc",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a454",
      "incomplete_value": false,
      "site": "00b4a460",
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
            "const:b11:8"
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
      "00b4a4e4",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4f0",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a504",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a4e4",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4f0",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a504",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a460) · [`00b4a468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a468) · [`00b4a448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a448)
- 新版 `00b4a4fc`（命令位置の公開資料なし） · `00b4a504`（命令位置の公開資料なし） · `00b4a4e4`（命令位置の公開資料なし）

~~~diff
- 00b4a460 ["INT_ADD", "register:40f0:8", ["const:b4a460:8", "const:4:8"]]
- 00b4a460 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a4fc ["INT_ADD", "register:40f0:8", ["const:b4a4fc:8", "const:4:8"]]
+ 00b4a4fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a460 bytes ac420494
+ 00b4a4fc bytes b9420494
- 00b4a468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a468 bytes 603605f9
+ 00b4a504 bytes 60b605f9
- 00b4a448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00b4a448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a4e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00b4a4e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a448 bytes 683645f9
+ 00b4a4e4 bytes 68b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d688dfa3e84dda4700274005952d714"></a>

### [`00b4a488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md) → [`00b4a524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a524.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4a5ac",
      "incomplete_value": true,
      "site": "00b4a5ac",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a510",
      "incomplete_value": true,
      "site": "00b4a510",
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
            "const:a70:8"
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
      "definition_site": "00b4a558",
      "incomplete_value": true,
      "site": "00b4a564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4bc",
      "incomplete_value": true,
      "site": "00b4a4c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a68:8"
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
      "00b4a538",
      "READ",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a558",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5ac",
      "WRITE",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a538",
      "READ",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a558",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5ac",
      "WRITE",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a4c8) · [`00b4a510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a510) · [`00b4a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a49c)
- 新版 `00b4a564`（命令位置の公開資料なし） · `00b4a5ac`（命令位置の公開資料なし） · `00b4a538`（命令位置の公開資料なし）

~~~diff
- 00b4a4c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a4c8 ["INT_ADD", "register:40f0:8", ["const:b4a4c8:8", "const:4:8"]]
- 00b4a4c8 ["CALLIND", null, ["register:0:8"]]
+ 00b4a564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a564 ["INT_ADD", "register:40f0:8", ["const:b4a564:8", "const:4:8"]]
+ 00b4a564 ["CALLIND", null, ["register:0:8"]]
- 00b4a4c8 bytes 00013fd6
+ 00b4a564 bytes 00013fd6
- 00b4a510 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a510 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a70:8"]]
- 00b4a510 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a5ac ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a5ac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b70:8"]]
+ 00b4a5ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a510 bytes a0c22939
+ 00b4a5ac bytes a0c22d39
- 00b4a49c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
- 00b4a49c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a49c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a538 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b70:8"]]
+ 00b4a538 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a538 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a49c bytes a8c26939
+ 00b4a538 bytes a8c26d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c009997b0d321fe0e6fb0712aa197f"></a>

### [`00b4a524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md) → [`00b4a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a5c0.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4a5fc",
      "incomplete_value": true,
      "site": "00b4a5fc",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a560",
      "incomplete_value": true,
      "site": "00b4a560",
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
            "const:a70:8"
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
      "definition_site": "00b4a64c",
      "incomplete_value": true,
      "site": "00b4a64c",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a5b0",
      "incomplete_value": true,
      "site": "00b4a5b0",
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
            "const:a68:8"
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
      "definition_site": "00b4a5d8",
      "incomplete_value": true,
      "site": "00b4a5d8",
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
      "definition_site": "00b4a53c",
      "incomplete_value": true,
      "site": "00b4a53c",
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
      "00b4a5d4",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5e0",
      "READ",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a5fc",
      "WRITE",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a5d4",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5e0",
      "READ",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a5fc",
      "WRITE",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a560) · [`00b4a5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a5ac) · [`00b4a5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a5b0)
- 新版 `00b4a5fc`（命令位置の公開資料なし） · `00b4a648`（命令位置の公開資料なし） · `00b4a64c`（命令位置の公開資料なし）

~~~diff
- 00b4a560 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a560 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a560 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a70:8"]]
- 00b4a560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a5fc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a5fc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a5fc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b70:8"]]
+ 00b4a5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a560 bytes bfc22939
+ 00b4a5fc bytes bfc22d39
- 00b4a5ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a5ac ["INT_ADD", "register:40f0:8", ["const:b4a5ac:8", "const:4:8"]]
- 00b4a5ac ["CALLIND", null, ["register:0:8"]]
+ 00b4a648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a648 ["INT_ADD", "register:40f0:8", ["const:b4a648:8", "const:4:8"]]
+ 00b4a648 ["CALLIND", null, ["register:0:8"]]
- 00b4a5ac bytes 00013fd6
+ 00b4a648 bytes 00013fd6
- 00b4a5b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b4a5b0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a5b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a64c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
+ 00b4a64c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a64c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a5b0 bytes 9f3605f9
+ 00b4a64c bytes 9fb605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3e2a35df0a31e54b2a78c3010f328e"></a>

### [`00b4a5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md) → [`00b4a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a660.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a6a0",
      "incomplete_value": true,
      "site": "00b4a6a0",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a604",
      "incomplete_value": true,
      "site": "00b4a604",
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
            "const:a68:8"
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
      "definition_site": "00b4a67c",
      "incomplete_value": true,
      "site": "00b4a67c",
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
      "definition_site": "00b4a5e0",
      "incomplete_value": true,
      "site": "00b4a5e0",
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
      "definition_site": "00b4a684",
      "incomplete_value": false,
      "site": "00b4a698",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a5e8",
      "incomplete_value": false,
      "site": "00b4a5fc",
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
            "const:b11:8"
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
      "00b4a674",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a684",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a6a0",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a674",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a684",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a6a0",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a5fc) · [`00b4a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a604) · [`00b4a5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a5d8)
- 新版 `00b4a698`（命令位置の公開資料なし） · `00b4a6a0`（命令位置の公開資料なし） · `00b4a674`（命令位置の公開資料なし）

~~~diff
- 00b4a5fc ["INT_ADD", "register:40f0:8", ["const:b4a5fc:8", "const:4:8"]]
- 00b4a5fc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a698 ["INT_ADD", "register:40f0:8", ["const:b4a698:8", "const:4:8"]]
+ 00b4a698 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a5fc bytes 45420494
+ 00b4a698 bytes 52420494
- 00b4a604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b4a604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a6a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
+ 00b4a6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a604 bytes 803605f9
+ 00b4a6a0 bytes 80b605f9
- 00b4a5d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b4a5d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a674 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
+ 00b4a674 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a5d8 bytes 813645f9
+ 00b4a674 bytes 81b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf6f1d19ad9865b7c0a705d1b7f166a"></a>

### [`00b4a634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md) → [`00b4a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a6d0.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4a6ec",
      "incomplete_value": false,
      "site": "00b4a6f0",
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
      "definition_site": "00b4a650",
      "incomplete_value": false,
      "site": "00b4a654",
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
      "definition_site": "00b4a6fc",
      "incomplete_value": true,
      "site": "00b4a708",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4a660",
      "incomplete_value": true,
      "site": "00b4a66c",
      "value": [
        "LOAD",
        "8",
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
      "00b4a6ec",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4a6fc",
      "DATA",
      [
        "storage",
        "01125a78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a6ec",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4a6fc",
      "DATA",
      [
        "storage",
        "01125b78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a654) · [`00b4a650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a650) · [`00b4a65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a65c)
- 新版 `00b4a6f0`（命令位置の公開資料なし） · `00b4a6ec`（命令位置の公開資料なし） · `00b4a6f8`（命令位置の公開資料なし）

~~~diff
- 00b4a654 ["INT_ADD", "register:40f0:8", ["const:b4a654:8", "const:4:8"]]
- 00b4a654 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4a6f0 ["INT_ADD", "register:40f0:8", ["const:b4a6f0:8", "const:4:8"]]
+ 00b4a6f0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4a654 bytes 6b420494
+ 00b4a6f0 bytes 78420494
- 00b4a650 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4a650 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a650 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a650 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6ec ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4a6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a650 bytes 009c0d91
+ 00b4a6ec bytes 002c0c91
- 00b4a65c ["COPY", "tmp:0:8", ["const:a78:8"]]
- 00b4a65c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a65c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a65c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a6f8 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00b4a6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a65c bytes 08e12991
+ 00b4a6f8 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353a53636e7d008f5d3acb71e3bc924f"></a>

### [`00b4a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md) → [`00b4a70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a70c.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a74c",
      "incomplete_value": true,
      "site": "00b4a74c",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6b0",
      "incomplete_value": true,
      "site": "00b4a6b0",
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
            "const:a68:8"
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
      "definition_site": "00b4a728",
      "incomplete_value": true,
      "site": "00b4a728",
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
      "definition_site": "00b4a68c",
      "incomplete_value": true,
      "site": "00b4a68c",
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
      "definition_site": "00b4a730",
      "incomplete_value": false,
      "site": "00b4a744",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a694",
      "incomplete_value": false,
      "site": "00b4a6a8",
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
            "const:b11:8"
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
      "00b4a720",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a730",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a74c",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a720",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a730",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4a74c",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a6a8) · [`00b4a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a6b0) · [`00b4a684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a684)
- 新版 `00b4a744`（命令位置の公開資料なし） · `00b4a74c`（命令位置の公開資料なし） · `00b4a720`（命令位置の公開資料なし）

~~~diff
- 00b4a6a8 ["INT_ADD", "register:40f0:8", ["const:b4a6a8:8", "const:4:8"]]
- 00b4a6a8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a744 ["INT_ADD", "register:40f0:8", ["const:b4a744:8", "const:4:8"]]
+ 00b4a744 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a6a8 bytes 1a420494
+ 00b4a744 bytes 27420494
- 00b4a6b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b4a6b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a74c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
+ 00b4a74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a6b0 bytes 803605f9
+ 00b4a74c bytes 80b605f9
- 00b4a684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00b4a684 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
+ 00b4a720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a684 bytes 813645f9
+ 00b4a720 bytes 81b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31272444fdc0bb92439cb1a01dcbecec"></a>

### [`00b4a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md) → [`00b4a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a77c.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4a798",
      "incomplete_value": false,
      "site": "00b4a79c",
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
      "definition_site": "00b4a6fc",
      "incomplete_value": false,
      "site": "00b4a700",
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
      "definition_site": "00b4a7a8",
      "incomplete_value": true,
      "site": "00b4a7b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4a70c",
      "incomplete_value": true,
      "site": "00b4a718",
      "value": [
        "LOAD",
        "8",
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
      "00b4a798",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4a7a8",
      "DATA",
      [
        "storage",
        "01125a88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a798",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a7a8",
      "DATA",
      [
        "storage",
        "01125b88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a700) · [`00b4a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a6fc) · [`00b4a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a708)
- 新版 `00b4a79c`（命令位置の公開資料なし） · `00b4a798`（命令位置の公開資料なし） · `00b4a7a4`（命令位置の公開資料なし）

~~~diff
- 00b4a700 ["INT_ADD", "register:40f0:8", ["const:b4a700:8", "const:4:8"]]
- 00b4a700 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4a79c ["INT_ADD", "register:40f0:8", ["const:b4a79c:8", "const:4:8"]]
+ 00b4a79c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4a700 bytes 40420494
+ 00b4a79c bytes 4d420494
- 00b4a6fc ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4a6fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a6fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a6fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a798 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4a798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a6fc bytes 00781491
+ 00b4a798 bytes 00341591
- 00b4a708 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00b4a708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a7a4 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00b4a7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a708 bytes 08212a91
+ 00b4a7a4 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30b295f08d8add0f9a7e3c630090f03e"></a>

### [`00b4a71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md) → [`00b4a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7b8.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

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
      "definition_site": "00b4a7e4",
      "incomplete_value": true,
      "site": "00b4a7e4",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a748",
      "incomplete_value": true,
      "site": "00b4a748",
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
            "const:a90:8"
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
      "definition_site": "00b4a7cc",
      "incomplete_value": true,
      "site": "00b4a7cc",
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
      "definition_site": "00b4a730",
      "incomplete_value": true,
      "site": "00b4a730",
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
      "definition_site": "00b4a7d8",
      "incomplete_value": false,
      "site": "00b4a7dc",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a73c",
      "incomplete_value": false,
      "site": "00b4a740",
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
            "const:c76:8"
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
      "00b4a7c8",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7d8",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a7e4",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a7c8",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7d8",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4a7e4",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a740) · [`00b4a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a748) · [`00b4a72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a72c)
- 新版 `00b4a7dc`（命令位置の公開資料なし） · `00b4a7e4`（命令位置の公開資料なし） · `00b4a7c8`（命令位置の公開資料なし）

~~~diff
- 00b4a740 ["INT_ADD", "register:40f0:8", ["const:b4a740:8", "const:4:8"]]
- 00b4a740 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a7dc ["INT_ADD", "register:40f0:8", ["const:b4a7dc:8", "const:4:8"]]
+ 00b4a7dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a740 bytes f4410494
+ 00b4a7dc bytes 01420494
- 00b4a748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a748 bytes 604a05f9
+ 00b4a7e4 bytes 60ca05f9
- 00b4a72c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a72c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a7c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a7c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a72c bytes 684a45f9
+ 00b4a7c8 bytes 68ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-048361940d1d9391024e1d03ff6e8d97"></a>

### [`00b4a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md) → [`00b4a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7f8.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4a824",
      "incomplete_value": true,
      "site": "00b4a824",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a788",
      "incomplete_value": true,
      "site": "00b4a788",
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
            "const:a90:8"
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
      "definition_site": "00b4a80c",
      "incomplete_value": true,
      "site": "00b4a80c",
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
      "definition_site": "00b4a770",
      "incomplete_value": true,
      "site": "00b4a770",
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
      "definition_site": "00b4a814",
      "incomplete_value": false,
      "site": "00b4a81c",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a778",
      "incomplete_value": false,
      "site": "00b4a780",
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
            "const:c76:8"
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
      "00b4a808",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a814",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a824",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a808",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a814",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4a824",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a780) · [`00b4a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a788) · [`00b4a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a76c)
- 新版 `00b4a81c`（命令位置の公開資料なし） · `00b4a824`（命令位置の公開資料なし） · `00b4a808`（命令位置の公開資料なし）

~~~diff
- 00b4a780 ["INT_ADD", "register:40f0:8", ["const:b4a780:8", "const:4:8"]]
- 00b4a780 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a81c ["INT_ADD", "register:40f0:8", ["const:b4a81c:8", "const:4:8"]]
+ 00b4a81c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a780 bytes e4410494
+ 00b4a81c bytes f1410494
- 00b4a788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a788 bytes 604a05f9
+ 00b4a824 bytes 60ca05f9
- 00b4a76c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a76c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a76c bytes 684a45f9
+ 00b4a808 bytes 68ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f3d027eccb2f01e14404365e302c79f"></a>

### [`00b4a79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md) → [`00b4a838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a838.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4a868",
      "incomplete_value": true,
      "site": "00b4a868",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7cc",
      "incomplete_value": true,
      "site": "00b4a7cc",
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
            "const:a90:8"
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
      "definition_site": "00b4a84c",
      "incomplete_value": true,
      "site": "00b4a84c",
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
      "definition_site": "00b4a7b0",
      "incomplete_value": true,
      "site": "00b4a7b0",
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
      "definition_site": "00b4a858",
      "incomplete_value": false,
      "site": "00b4a860",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7bc",
      "incomplete_value": false,
      "site": "00b4a7c4",
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
            "const:c76:8"
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
      "00b4a848",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a858",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a868",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a848",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a858",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4a868",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7c4) · [`00b4a7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7cc) · [`00b4a7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7ac)
- 新版 `00b4a860`（命令位置の公開資料なし） · `00b4a868`（命令位置の公開資料なし） · `00b4a848`（命令位置の公開資料なし）

~~~diff
- 00b4a7c4 ["INT_ADD", "register:40f0:8", ["const:b4a7c4:8", "const:4:8"]]
- 00b4a7c4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a860 ["INT_ADD", "register:40f0:8", ["const:b4a860:8", "const:4:8"]]
+ 00b4a860 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a7c4 bytes d3410494
+ 00b4a860 bytes e0410494
- 00b4a7cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a7cc bytes 604a05f9
+ 00b4a868 bytes 60ca05f9
- 00b4a7ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a7ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a848 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a848 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a7ac bytes 684a45f9
+ 00b4a848 bytes 68ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac8cbda6ee6f811e555a5136177832ec"></a>

### [`00b4a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md) → [`00b4a87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a87c.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a8ac",
      "incomplete_value": true,
      "site": "00b4a8ac",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a810",
      "incomplete_value": true,
      "site": "00b4a810",
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
            "const:a90:8"
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
      "definition_site": "00b4a890",
      "incomplete_value": true,
      "site": "00b4a890",
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
      "definition_site": "00b4a7f4",
      "incomplete_value": true,
      "site": "00b4a7f4",
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
      "definition_site": "00b4a898",
      "incomplete_value": false,
      "site": "00b4a8a4",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7fc",
      "incomplete_value": false,
      "site": "00b4a808",
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
            "const:c76:8"
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
      "00b4a88c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a898",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a8ac",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a88c",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a898",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4a8ac",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a808) · [`00b4a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a810) · [`00b4a7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a7f0)
- 新版 `00b4a8a4`（命令位置の公開資料なし） · `00b4a8ac`（命令位置の公開資料なし） · `00b4a88c`（命令位置の公開資料なし）

~~~diff
- 00b4a808 ["INT_ADD", "register:40f0:8", ["const:b4a808:8", "const:4:8"]]
- 00b4a808 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4a8a4 ["INT_ADD", "register:40f0:8", ["const:b4a8a4:8", "const:4:8"]]
+ 00b4a8a4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a808 bytes c2410494
+ 00b4a8a4 bytes cf410494
- 00b4a810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a810 bytes 604a05f9
+ 00b4a8ac bytes 60ca05f9
- 00b4a7f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
- 00b4a7f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a88c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00b4a88c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a7f0 bytes 684a45f9
+ 00b4a88c bytes 68ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc87f22d7f96074b9d4ad20446d39ee"></a>

### [`00b4a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md) → [`00b4a8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a8cc.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4a954",
      "incomplete_value": true,
      "site": "00b4a954",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a8b8",
      "incomplete_value": true,
      "site": "00b4a8b8",
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
            "const:a98:8"
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
      "definition_site": "00b4a900",
      "incomplete_value": true,
      "site": "00b4a90c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a864",
      "incomplete_value": true,
      "site": "00b4a870",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a90:8"
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
      "00b4a8e0",
      "READ",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a900",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a954",
      "WRITE",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a8e0",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a900",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a954",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a870) · [`00b4a8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a8b8) · [`00b4a844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a844)
- 新版 `00b4a90c`（命令位置の公開資料なし） · `00b4a954`（命令位置の公開資料なし） · `00b4a8e0`（命令位置の公開資料なし）

~~~diff
- 00b4a870 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a870 ["INT_ADD", "register:40f0:8", ["const:b4a870:8", "const:4:8"]]
- 00b4a870 ["CALLIND", null, ["register:0:8"]]
+ 00b4a90c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a90c ["INT_ADD", "register:40f0:8", ["const:b4a90c:8", "const:4:8"]]
+ 00b4a90c ["CALLIND", null, ["register:0:8"]]
- 00b4a870 bytes 00013fd6
+ 00b4a90c bytes 00013fd6
- 00b4a8b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a8b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a98:8"]]
- 00b4a8b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a954 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b98:8"]]
+ 00b4a954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a8b8 bytes a0622a39
+ 00b4a954 bytes a0622e39
- 00b4a844 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a98:8"]]
- 00b4a844 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a844 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a8e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b98:8"]]
+ 00b4a8e0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a8e0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a844 bytes a8626a39
+ 00b4a8e0 bytes a8626e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac80ebff296f6889fa89b7ed7fa35b38"></a>

### [`00b4a8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md) → [`00b4a968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a968.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4a9a4",
      "incomplete_value": true,
      "site": "00b4a9a4",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a908",
      "incomplete_value": true,
      "site": "00b4a908",
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
            "const:a98:8"
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
      "definition_site": "00b4a9f4",
      "incomplete_value": true,
      "site": "00b4a9f4",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a958",
      "incomplete_value": true,
      "site": "00b4a958",
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
            "const:a90:8"
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
      "definition_site": "00b4a980",
      "incomplete_value": true,
      "site": "00b4a980",
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
      "definition_site": "00b4a8e4",
      "incomplete_value": true,
      "site": "00b4a8e4",
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
      "00b4a97c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a988",
      "READ",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a9a4",
      "WRITE",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a97c",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a988",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a9a4",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a908) · [`00b4a954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a954) · [`00b4a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a958)
- 新版 `00b4a9a4`（命令位置の公開資料なし） · `00b4a9f0`（命令位置の公開資料なし） · `00b4a9f4`（命令位置の公開資料なし）

~~~diff
- 00b4a908 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a908 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a908 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a98:8"]]
- 00b4a908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a9a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a9a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a9a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b98:8"]]
+ 00b4a9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a908 bytes bf622a39
+ 00b4a9a4 bytes bf622e39
- 00b4a954 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a954 ["INT_ADD", "register:40f0:8", ["const:b4a954:8", "const:4:8"]]
- 00b4a954 ["CALLIND", null, ["register:0:8"]]
+ 00b4a9f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a9f0 ["INT_ADD", "register:40f0:8", ["const:b4a9f0:8", "const:4:8"]]
+ 00b4a9f0 ["CALLIND", null, ["register:0:8"]]
- 00b4a954 bytes 00013fd6
+ 00b4a9f0 bytes 00013fd6
- 00b4a958 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
- 00b4a958 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a9f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
+ 00b4a9f4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a9f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a958 bytes 9f4a05f9
+ 00b4a9f4 bytes 9fca05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba64553a7e368096541f7d6a4796e4a"></a>

### [`00b4a96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md) → [`00b4aa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa08.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4aa48",
      "incomplete_value": true,
      "site": "00b4aa48",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a9ac",
      "incomplete_value": true,
      "site": "00b4a9ac",
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
            "const:a90:8"
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
      "definition_site": "00b4aa24",
      "incomplete_value": true,
      "site": "00b4aa24",
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
      "definition_site": "00b4a988",
      "incomplete_value": true,
      "site": "00b4a988",
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
      "definition_site": "00b4aa2c",
      "incomplete_value": false,
      "site": "00b4aa40",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a990",
      "incomplete_value": false,
      "site": "00b4a9a4",
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
            "const:c76:8"
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
      "00b4aa1c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa2c",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4aa48",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa1c",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa2c",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4aa48",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a9a4) · [`00b4a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a9ac) · [`00b4a980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a980)
- 新版 `00b4aa40`（命令位置の公開資料なし） · `00b4aa48`（命令位置の公開資料なし） · `00b4aa1c`（命令位置の公開資料なし）

~~~diff
- 00b4a9a4 ["INT_ADD", "register:40f0:8", ["const:b4a9a4:8", "const:4:8"]]
- 00b4a9a4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4aa40 ["INT_ADD", "register:40f0:8", ["const:b4aa40:8", "const:4:8"]]
+ 00b4aa40 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4a9a4 bytes 5b410494
+ 00b4aa40 bytes 68410494
- 00b4a9ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
- 00b4a9ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aa48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
+ 00b4aa48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a9ac bytes 804a05f9
+ 00b4aa48 bytes 80ca05f9
- 00b4a980 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
- 00b4a980 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aa1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
+ 00b4aa1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a980 bytes 814a45f9
+ 00b4aa1c bytes 81ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec0c2fee32ec53b55eb0f920bcdd8e66"></a>

### [`00b4a9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md) → [`00b4aa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa78.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b510.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5e0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4aa94",
      "incomplete_value": false,
      "site": "00b4aa98",
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
      "definition_site": "00b4a9f8",
      "incomplete_value": false,
      "site": "00b4a9fc",
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
      "definition_site": "00b4aaa4",
      "incomplete_value": true,
      "site": "00b4aab0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4aa08",
      "incomplete_value": true,
      "site": "00b4aa14",
      "value": [
        "LOAD",
        "8",
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
      "00b4aa94",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4aaa4",
      "DATA",
      [
        "storage",
        "01125aa0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa94",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4aaa4",
      "DATA",
      [
        "storage",
        "01125ba0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4a9fc) · [`00b4a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4a9f8) · [`00b4aa04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4aa04)
- 新版 `00b4aa98`（命令位置の公開資料なし） · `00b4aa94`（命令位置の公開資料なし） · `00b4aaa0`（命令位置の公開資料なし）

~~~diff
- 00b4a9fc ["INT_ADD", "register:40f0:8", ["const:b4a9fc:8", "const:4:8"]]
- 00b4a9fc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4aa98 ["INT_ADD", "register:40f0:8", ["const:b4aa98:8", "const:4:8"]]
+ 00b4aa98 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4a9fc bytes 81410494
+ 00b4aa98 bytes 8e410494
- 00b4a9f8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b4a9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa94 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4aa94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a9f8 bytes 009c0d91
+ 00b4aa94 bytes 002c0c91
- 00b4aa04 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00b4aa04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aa04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aa04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4aaa0 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00b4aaa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aaa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aaa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4aa04 bytes 08812a91
+ 00b4aaa0 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d990a3651cdef7fc045b57bb28f3f0e4"></a>

### [`00b4aa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md) → [`00b4aab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aab4.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4aaf4",
      "incomplete_value": true,
      "site": "00b4aaf4",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa58",
      "incomplete_value": true,
      "site": "00b4aa58",
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
            "const:a90:8"
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
      "definition_site": "00b4aad0",
      "incomplete_value": true,
      "site": "00b4aad0",
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
      "definition_site": "00b4aa34",
      "incomplete_value": true,
      "site": "00b4aa34",
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
      "definition_site": "00b4aad8",
      "incomplete_value": false,
      "site": "00b4aaec",
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
            "const:cb6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa3c",
      "incomplete_value": false,
      "site": "00b4aa50",
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
            "const:c76:8"
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
      "00b4aac8",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aad8",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf4",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aac8",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aad8",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf4",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa50) · [`00b4aa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa58) · [`00b4aa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa2c)
- 新版 `00b4aaec`（命令位置の公開資料なし） · `00b4aaf4`（命令位置の公開資料なし） · `00b4aac8`（命令位置の公開資料なし）

~~~diff
- 00b4aa50 ["INT_ADD", "register:40f0:8", ["const:b4aa50:8", "const:4:8"]]
- 00b4aa50 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4aaec ["INT_ADD", "register:40f0:8", ["const:b4aaec:8", "const:4:8"]]
+ 00b4aaec ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4aa50 bytes 30410494
+ 00b4aaec bytes 3d410494
- 00b4aa58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
- 00b4aa58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aaf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
+ 00b4aaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aa58 bytes 804a05f9
+ 00b4aaf4 bytes 80ca05f9
- 00b4aa2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
- 00b4aa2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
+ 00b4aac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aa2c bytes 814a45f9
+ 00b4aac8 bytes 81ca45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58185ea797e08854172bb1936617c1d1"></a>

### [`00b4aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md) → [`00b4ab24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab24.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4ab40",
      "incomplete_value": false,
      "site": "00b4ab44",
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
      "definition_site": "00b4aaa4",
      "incomplete_value": false,
      "site": "00b4aaa8",
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
      "definition_site": "00b4ab50",
      "incomplete_value": true,
      "site": "00b4ab5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4aab4",
      "incomplete_value": true,
      "site": "00b4aac0",
      "value": [
        "LOAD",
        "8",
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
      "00b4ab40",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4ab50",
      "DATA",
      [
        "storage",
        "01125ae0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ab40",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4ab50",
      "DATA",
      [
        "storage",
        "01125be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aaa8) · [`00b4aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aaa4) · [`00b4aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aab0)
- 新版 `00b4ab44`（命令位置の公開資料なし） · `00b4ab40`（命令位置の公開資料なし） · `00b4ab4c`（命令位置の公開資料なし）

~~~diff
- 00b4aaa8 ["INT_ADD", "register:40f0:8", ["const:b4aaa8:8", "const:4:8"]]
- 00b4aaa8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4ab44 ["INT_ADD", "register:40f0:8", ["const:b4ab44:8", "const:4:8"]]
+ 00b4ab44 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4aaa8 bytes 56410494
+ 00b4ab44 bytes 63410494
- 00b4aaa4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4aaa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aaa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aaa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ab40 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b4ab40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ab40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ab40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4aaa4 bytes 00781491
+ 00b4ab40 bytes 00341591
- 00b4aab0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00b4aab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ab4c ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00b4ab4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ab4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ab4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4aab0 bytes 08812b91
+ 00b4ab4c bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995b5537c5d251fb9abc435670c220c2"></a>

### [`00b4aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md) → [`00b4ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab60.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4ab8c",
      "incomplete_value": true,
      "site": "00b4ab8c",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aaf0",
      "incomplete_value": true,
      "site": "00b4aaf0",
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
            "const:ae8:8"
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
      "definition_site": "00b4ab74",
      "incomplete_value": true,
      "site": "00b4ab74",
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
      "definition_site": "00b4aad8",
      "incomplete_value": true,
      "site": "00b4aad8",
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
      "definition_site": "00b4ab80",
      "incomplete_value": false,
      "site": "00b4ab84",
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
      "definition_site": "00b4aae4",
      "incomplete_value": false,
      "site": "00b4aae8",
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
      "00b4ab70",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ab8c",
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
      "00b4ab70",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4ab8c",
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

- 旧版 [`00b4aae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aae8) · [`00b4aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aaf0) · [`00b4aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aad4)
- 新版 `00b4ab84`（命令位置の公開資料なし） · `00b4ab8c`（命令位置の公開資料なし） · `00b4ab70`（命令位置の公開資料なし）

~~~diff
- 00b4aae8 ["INT_ADD", "register:40f0:8", ["const:b4aae8:8", "const:4:8"]]
- 00b4aae8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ab84 ["INT_ADD", "register:40f0:8", ["const:b4ab84:8", "const:4:8"]]
+ 00b4ab84 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4aae8 bytes 0a410494
+ 00b4ab84 bytes 17410494
- 00b4aaf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4aaf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4ab8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aaf0 bytes 607605f9
+ 00b4ab8c bytes 60f605f9
- 00b4aad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4aad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4ab70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aad4 bytes 687645f9
+ 00b4ab70 bytes 68f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3aaabff3c6696a125a40b5ecad827ec"></a>

### [`00b4ab04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md) → [`00b4aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aba0.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4abcc",
      "incomplete_value": true,
      "site": "00b4abcc",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab30",
      "incomplete_value": true,
      "site": "00b4ab30",
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
            "const:ae8:8"
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
      "definition_site": "00b4abb4",
      "incomplete_value": true,
      "site": "00b4abb4",
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
      "definition_site": "00b4ab18",
      "incomplete_value": true,
      "site": "00b4ab18",
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
      "definition_site": "00b4abbc",
      "incomplete_value": false,
      "site": "00b4abc4",
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
      "definition_site": "00b4ab20",
      "incomplete_value": false,
      "site": "00b4ab28",
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
      "00b4abb0",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abbc",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4abcc",
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
      "00b4abb0",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abbc",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4abcc",
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

- 旧版 [`00b4ab28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab28) · [`00b4ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab30) · [`00b4ab14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab14)
- 新版 `00b4abc4`（命令位置の公開資料なし） · `00b4abcc`（命令位置の公開資料なし） · `00b4abb0`（命令位置の公開資料なし）

~~~diff
- 00b4ab28 ["INT_ADD", "register:40f0:8", ["const:b4ab28:8", "const:4:8"]]
- 00b4ab28 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4abc4 ["INT_ADD", "register:40f0:8", ["const:b4abc4:8", "const:4:8"]]
+ 00b4abc4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ab28 bytes fa400494
+ 00b4abc4 bytes 07410494
- 00b4ab30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4ab30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4abcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4abcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab30 bytes 607605f9
+ 00b4abcc bytes 60f605f9
- 00b4ab14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4ab14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4abb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4abb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab14 bytes 687645f9
+ 00b4abb0 bytes 68f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cee146c0772a2939f93d799fa425556"></a>

### [`00b4ab44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md) → [`00b4abe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4abe0.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4ac10",
      "incomplete_value": true,
      "site": "00b4ac10",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab74",
      "incomplete_value": true,
      "site": "00b4ab74",
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
            "const:ae8:8"
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
      "definition_site": "00b4abf4",
      "incomplete_value": true,
      "site": "00b4abf4",
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
      "definition_site": "00b4ab58",
      "incomplete_value": true,
      "site": "00b4ab58",
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
      "definition_site": "00b4ac00",
      "incomplete_value": false,
      "site": "00b4ac08",
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
      "definition_site": "00b4ab64",
      "incomplete_value": false,
      "site": "00b4ab6c",
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
      "00b4abf0",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac00",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ac10",
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
      "00b4abf0",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac00",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4ac10",
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

- 旧版 [`00b4ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab6c) · [`00b4ab74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab74) · [`00b4ab54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab54)
- 新版 `00b4ac08`（命令位置の公開資料なし） · `00b4ac10`（命令位置の公開資料なし） · `00b4abf0`（命令位置の公開資料なし）

~~~diff
- 00b4ab6c ["INT_ADD", "register:40f0:8", ["const:b4ab6c:8", "const:4:8"]]
- 00b4ab6c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ac08 ["INT_ADD", "register:40f0:8", ["const:b4ac08:8", "const:4:8"]]
+ 00b4ac08 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ab6c bytes e9400494
+ 00b4ac08 bytes f6400494
- 00b4ab74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4ab74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ac10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4ac10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab74 bytes 607605f9
+ 00b4ac10 bytes 60f605f9
- 00b4ab54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4ab54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4abf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4abf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab54 bytes 687645f9
+ 00b4abf0 bytes 68f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc84fcef44e76cbc4657eaccb171554"></a>

### [`00b4ab88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md) → [`00b4ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac24.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4ac54",
      "incomplete_value": true,
      "site": "00b4ac54",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abb8",
      "incomplete_value": true,
      "site": "00b4abb8",
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
            "const:ae8:8"
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
      "definition_site": "00b4ac38",
      "incomplete_value": true,
      "site": "00b4ac38",
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
      "definition_site": "00b4ab9c",
      "incomplete_value": true,
      "site": "00b4ab9c",
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
      "definition_site": "00b4ac40",
      "incomplete_value": false,
      "site": "00b4ac4c",
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
      "definition_site": "00b4aba4",
      "incomplete_value": false,
      "site": "00b4abb0",
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
      "00b4ac34",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac40",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ac54",
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
      "00b4ac34",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac40",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4ac54",
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

- 旧版 [`00b4abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4abb0) · [`00b4abb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4abb8) · [`00b4ab98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4ab98)
- 新版 `00b4ac4c`（命令位置の公開資料なし） · `00b4ac54`（命令位置の公開資料なし） · `00b4ac34`（命令位置の公開資料なし）

~~~diff
- 00b4abb0 ["INT_ADD", "register:40f0:8", ["const:b4abb0:8", "const:4:8"]]
- 00b4abb0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ac4c ["INT_ADD", "register:40f0:8", ["const:b4ac4c:8", "const:4:8"]]
+ 00b4ac4c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4abb0 bytes d8400494
+ 00b4ac4c bytes e5400494
- 00b4abb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4abb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ac54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4ac54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4abb8 bytes 607605f9
+ 00b4ac54 bytes 60f605f9
- 00b4ab98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
- 00b4ab98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ac34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
+ 00b4ac34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab98 bytes 687645f9
+ 00b4ac34 bytes 68f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05de10570a3972a6902c16246befd8b8"></a>

### [`00b4abd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md) → [`00b4ac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac74.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4acfc",
      "incomplete_value": true,
      "site": "00b4acfc",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac60",
      "incomplete_value": true,
      "site": "00b4ac60",
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
            "const:af0:8"
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
      "definition_site": "00b4aca8",
      "incomplete_value": true,
      "site": "00b4acb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac0c",
      "incomplete_value": true,
      "site": "00b4ac18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
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
      "00b4ac88",
      "READ",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aca8",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acfc",
      "WRITE",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ac88",
      "READ",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aca8",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acfc",
      "WRITE",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4ac18) · [`00b4ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4ac60) · [`00b4abec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4abec)
- 新版 `00b4acb4`（命令位置の公開資料なし） · `00b4acfc`（命令位置の公開資料なし） · `00b4ac88`（命令位置の公開資料なし）

~~~diff
- 00b4ac18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ac18 ["INT_ADD", "register:40f0:8", ["const:b4ac18:8", "const:4:8"]]
- 00b4ac18 ["CALLIND", null, ["register:0:8"]]
+ 00b4acb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4acb4 ["INT_ADD", "register:40f0:8", ["const:b4acb4:8", "const:4:8"]]
+ 00b4acb4 ["CALLIND", null, ["register:0:8"]]
- 00b4ac18 bytes 00013fd6
+ 00b4acb4 bytes 00013fd6
- 00b4ac60 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ac60 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:af0:8"]]
- 00b4ac60 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4acfc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4acfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bf0:8"]]
+ 00b4acfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ac60 bytes a0c22b39
+ 00b4acfc bytes a0c22f39
- 00b4abec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:af0:8"]]
- 00b4abec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4abec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4ac88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bf0:8"]]
+ 00b4ac88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ac88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4abec bytes a8c26b39
+ 00b4ac88 bytes a8c26f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed79f41d17703c0389e7873c25648e0"></a>

### [`00b4ac74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md) → [`00b4ad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ad10.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4ad4c",
      "incomplete_value": true,
      "site": "00b4ad4c",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4acb0",
      "incomplete_value": true,
      "site": "00b4acb0",
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
            "const:af0:8"
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
      "definition_site": "00b4ad9c",
      "incomplete_value": true,
      "site": "00b4ad9c",
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
      "definition_site": "00b4ad00",
      "incomplete_value": true,
      "site": "00b4ad00",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ad28",
      "incomplete_value": true,
      "site": "00b4ad28",
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
      "definition_site": "00b4ac8c",
      "incomplete_value": true,
      "site": "00b4ac8c",
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
      "00b4ad24",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad30",
      "READ",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ad4c",
      "WRITE",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad24",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad30",
      "READ",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ad4c",
      "WRITE",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4acb0) · [`00b4acfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4acfc) · [`00b4ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4ad00)
- 新版 `00b4ad4c`（命令位置の公開資料なし） · `00b4ad98`（命令位置の公開資料なし） · `00b4ad9c`（命令位置の公開資料なし）

~~~diff
- 00b4acb0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4acb0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4acb0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:af0:8"]]
- 00b4acb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4ad4c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4ad4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4ad4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bf0:8"]]
+ 00b4ad4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4acb0 bytes bfc22b39
+ 00b4ad4c bytes bfc22f39
- 00b4acfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4acfc ["INT_ADD", "register:40f0:8", ["const:b4acfc:8", "const:4:8"]]
- 00b4acfc ["CALLIND", null, ["register:0:8"]]
+ 00b4ad98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ad98 ["INT_ADD", "register:40f0:8", ["const:b4ad98:8", "const:4:8"]]
+ 00b4ad98 ["CALLIND", null, ["register:0:8"]]
- 00b4acfc bytes 00013fd6
+ 00b4ad98 bytes 00013fd6
- 00b4ad00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b4ad00 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4ad00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4ad9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00b4ad9c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4ad9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4ad00 bytes 9f7605f9
+ 00b4ad9c bytes 9ff605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8efb9d8fe5d973933a9f49b58e5b4423"></a>

### [`00b4ad14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md) → [`00b4adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4adb0.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4adf0",
      "incomplete_value": true,
      "site": "00b4adf0",
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
      "definition_site": "00b4ad54",
      "incomplete_value": true,
      "site": "00b4ad54",
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
      "definition_site": "00b4adcc",
      "incomplete_value": true,
      "site": "00b4adcc",
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
      "definition_site": "00b4ad30",
      "incomplete_value": true,
      "site": "00b4ad30",
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
      "definition_site": "00b4add4",
      "incomplete_value": false,
      "site": "00b4ade8",
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
      "definition_site": "00b4ad38",
      "incomplete_value": false,
      "site": "00b4ad4c",
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
      "00b4adc4",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4add4",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4adf0",
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
      "00b4adc4",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4add4",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4adf0",
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

- 旧版 [`00b4ad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad4c) · [`00b4ad54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad54) · [`00b4ad28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad28)
- 新版 `00b4ade8`（命令位置の公開資料なし） · `00b4adf0`（命令位置の公開資料なし） · `00b4adc4`（命令位置の公開資料なし）

~~~diff
- 00b4ad4c ["INT_ADD", "register:40f0:8", ["const:b4ad4c:8", "const:4:8"]]
- 00b4ad4c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4ade8 ["INT_ADD", "register:40f0:8", ["const:b4ade8:8", "const:4:8"]]
+ 00b4ade8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4ad4c bytes 71400494
+ 00b4ade8 bytes 7e400494
- 00b4ad54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b4ad54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4adf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00b4adf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ad54 bytes 807605f9
+ 00b4adf0 bytes 80f605f9
- 00b4ad28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b4ad28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4adc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00b4adc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ad28 bytes 817645f9
+ 00b4adc4 bytes 81f645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

