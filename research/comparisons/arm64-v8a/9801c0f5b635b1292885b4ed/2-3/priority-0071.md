# v16.0.1 → v16.0.2 · 最優先の変更候補 (71)

[一覧の目次](README.md)

<a id="compare-c543a1a1dd917b9192bbdb6194475b09"></a>

### [`00b459a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b459a8.md) → [`00b45a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45a44.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b459a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b459a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b459ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b459a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b459ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b459bc",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45a44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45a48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45a58",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b459a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b459a8.md#insn-00b459a8) · [`00b459ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b459a8.md#insn-00b459ac) · [`00b459c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b459a8.md#insn-00b459c4)

~~~diff
- 00b459a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b459a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b459a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b459a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b459a8 bytes f44fbea9
- 00b459ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b459ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b459ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b459ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b459ac bytes fd7b01a9
- 00b459c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b459c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b459c4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91eb5e9286110088dbead69d4f84591d"></a>

### [`00b45b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md) → [`00b45bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45bb4.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b45b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45be4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45bc8",
      "incomplete_value": true,
      "site": "00b45bc8",
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
      "definition_site": "00b45b2c",
      "incomplete_value": true,
      "site": "00b45b2c",
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
      "00b45bc4",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45b4c"
      ]
    ],
    [
      "unmatched:00b45b34",
      "PARAM",
      [
        "storage",
        "002bada3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45bc4",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45be8"
      ]
    ],
    [
      "00b45bd0",
      "PARAM",
      [
        "storage",
        "002bad4f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md#insn-00b45b2c) · [`00b45b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md#insn-00b45b40) · [`00b45b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b18.md#insn-00b45b48)
- 新版 `00b45bc8`（命令位置の公開資料なし） · `00b45bdc`（命令位置の公開資料なし）

~~~diff
- 00b45b2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45b2c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b45bc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45b2c bytes 080100b5
+ 00b45bc8 bytes 080100b5
- 00b45b40 ["INT_ADD", "register:40f0:8", ["const:b45b40:8", "const:4:8"]]
- 00b45b40 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45bdc ["INT_ADD", "register:40f0:8", ["const:b45bdc:8", "const:4:8"]]
+ 00b45bdc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45b40 bytes f4540494
+ 00b45bdc bytes 01550494
- 00b45b48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6b0:8"]]
- 00b45b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45b48 bytes 605a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1116bb5acfb07d5aa96e9cd89d65f95"></a>

### [`00b45ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ca4.md) → [`00b45d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45d40.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b45ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ca8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45cb8",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45d54",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ca4.md#insn-00b45ca4) · [`00b45ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ca4.md#insn-00b45ca8) · [`00b45cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ca4.md#insn-00b45cc0)

~~~diff
- 00b45ca4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45ca4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45ca4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45ca4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45ca4 bytes f44fbea9
- 00b45ca8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45ca8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45ca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45ca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45ca8 bytes fd7b01a9
- 00b45cc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45cc0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b45cc0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4932697388db3559edb1d59d4d21e8"></a>

### [`00b45d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d50.md) → [`00b45dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45dec.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45d54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45d64",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45dec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45df0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45e00",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d50.md#insn-00b45d50) · [`00b45d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d50.md#insn-00b45d54) · [`00b45d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d50.md#insn-00b45d6c)

~~~diff
- 00b45d50 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45d50 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45d50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45d50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45d50 bytes f44fbea9
- 00b45d54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45d54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45d54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45d54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45d54 bytes fd7b01a9
- 00b45d6c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45d6c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b45d6c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23d65157e8582b85830da0089d65619"></a>

### [`00b45e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45e7c.md) → [`00b45f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f18.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 9.09% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45f48",
      "incomplete_value": true,
      "site": "00b45f48",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45eac",
      "incomplete_value": true,
      "site": "00b45eac",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b45f58"
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
      "unmatched:00b45e8c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45eb0"
      ]
    ],
    [
      "unmatched:00b45e9c",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45f28",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45f4c"
      ]
    ],
    [
      "00b45f38",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45e7c.md#insn-00b45eac) · [`00b45ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45e7c.md#insn-00b45ebc)
- 新版 `00b45f48`（命令位置の公開資料なし） · `00b45f58`（命令位置の公開資料なし）

~~~diff
- 00b45eac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00b45eac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d8:8"]]
+ 00b45f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45eac bytes 606e03f9
+ 00b45f48 bytes 60ee03f9
- 00b45ebc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b45ebc ["RETURN", null, ["register:0:8"]]
- 00b45ebc bytes c0035fd6
+ 00b45f58 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b45f58 ["RETURN", null, ["register:0:8"]]
+ 00b45f58 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c3e5a5a44f4fdb05ddc9ad2a9adc87"></a>

### [`00b45ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md) → [`00b45f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45f5c.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45f8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ed4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45ed0",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45ed4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45ef4"
      ]
    ],
    [
      "unmatched:00b45edc",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45f6c",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45f90"
      ]
    ],
    [
      "00b45f78",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md#insn-00b45ed4) · [`00b45ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md#insn-00b45ee8) · [`00b45ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45ec0.md#insn-00b45ef0)
- 新版 `00b45f84`（命令位置の公開資料なし）

~~~diff
- 00b45ed4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45ed4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b45ed4 bytes 080100b5
- 00b45ee8 ["INT_ADD", "register:40f0:8", ["const:b45ee8:8", "const:4:8"]]
- 00b45ee8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45f84 ["INT_ADD", "register:40f0:8", ["const:b45f84:8", "const:4:8"]]
+ 00b45f84 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45ee8 bytes 0a540494
+ 00b45f84 bytes 17540494
- 00b45ef0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 00b45ef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45ef0 bytes 606e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f07e8d17c95eb23ade0a9b6d30ad945"></a>

### [`00b45f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md) → [`00b45fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45fac.md) _ZN8firebase4util3log15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 27.27% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45f14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45f18",
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
      "00b45fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b45fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45fb4",
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

- 旧版 [`00b45f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md#insn-00b45f10) · [`00b45f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md#insn-00b45f14) · [`00b45f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45f10.md#insn-00b45f18)

~~~diff
- 00b45f10 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b45f10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b45f10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45f10 bytes f50f1df8
- 00b45f14 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45f14 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45f14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45f14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45f14 bytes f44f01a9
- 00b45f18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45f18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45f18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b45f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45f18 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cb78e74a2b243c8edf8e4ee88535268"></a>

### [`00b4604c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md) → [`00b460e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b460e8.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00b4608c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46128"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46060",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4612c"
      ]
    ],
    [
      "unmatched:00b46070",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b460fc",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4612c"
      ]
    ],
    [
      "00b4610c",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md#insn-00b46068) · [`00b46084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md#insn-00b46084) · [`00b4608c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4604c.md#insn-00b4608c)
- 新版 `00b46120`（命令位置の公開資料なし）

~~~diff
- 00b46068 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46068 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46068 bytes 410100b5
- 00b46084 ["INT_ADD", "register:40f0:8", ["const:b46084:8", "const:4:8"]]
- 00b46084 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46120 ["INT_ADD", "register:40f0:8", ["const:b46120:8", "const:4:8"]]
+ 00b46120 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46084 bytes a3530494
+ 00b46120 bytes b0530494
- 00b4608c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00b4608c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4608c bytes 806e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0012bdf2fe1a97adf219c8ce73f3c95b"></a>

### [`00b460f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460f8.md) → [`00b46194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46194.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b461d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4610c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46114",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b461d8"
      ]
    ],
    [
      "unmatched:00b4611c",
      "PARAM",
      [
        "storage",
        "002bbdb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b461a8",
      "READ",
      [
        "storage",
        "011257d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b461d8"
      ]
    ],
    [
      "00b461b8",
      "PARAM",
      [
        "storage",
        "002bbd63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460f8.md#insn-00b46114) · [`00b46130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460f8.md#insn-00b46130) · [`00b46138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460f8.md#insn-00b46138)
- 新版 `00b461cc`（命令位置の公開資料なし）

~~~diff
- 00b46114 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46114 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b46114 bytes 410100b5
- 00b46130 ["INT_ADD", "register:40f0:8", ["const:b46130:8", "const:4:8"]]
- 00b46130 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b461cc ["INT_ADD", "register:40f0:8", ["const:b461cc:8", "const:4:8"]]
+ 00b461cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46130 bytes 78530494
+ 00b461cc bytes 85530494
- 00b46138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6d8:8"]]
- 00b46138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46138 bytes 806e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d67b07cc0b56157e82f8670fbdfd2e"></a>

### [`00b46168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46168.md) → [`00b46204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46204.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b46220",
      "incomplete_value": false,
      "site": "00b46224",
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
      "definition_site": "00b46184",
      "incomplete_value": false,
      "site": "00b46188",
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
      "definition_site": "00b46230",
      "incomplete_value": true,
      "site": "00b4623c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b46194",
      "incomplete_value": true,
      "site": "00b461a0",
      "value": [
        "LOAD",
        "8",
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
      "00b46220",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b46230",
      "DATA",
      [
        "storage",
        "011256f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46220",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b46230",
      "DATA",
      [
        "storage",
        "011257f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46168.md#insn-00b46188) · [`00b46184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46168.md#insn-00b46184) · [`00b46190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46168.md#insn-00b46190)
- 新版 `00b46224`（命令位置の公開資料なし） · `00b46220`（命令位置の公開資料なし） · `00b4622c`（命令位置の公開資料なし）

~~~diff
- 00b46188 ["INT_ADD", "register:40f0:8", ["const:b46188:8", "const:4:8"]]
- 00b46188 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b46224 ["INT_ADD", "register:40f0:8", ["const:b46224:8", "const:4:8"]]
+ 00b46224 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b46188 bytes 9e530494
+ 00b46224 bytes ab530494
- 00b46184 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b46184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46220 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b46220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46184 bytes 00781491
+ 00b46220 bytes 00341591
- 00b46190 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 00b46190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4622c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b4622c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4622c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4622c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46190 bytes 08c11b91
+ 00b4622c bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7fc3a7314c6a7a489ea27135198f589"></a>

### [`00b461a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md) → [`00b46240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46240.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b4626c",
      "incomplete_value": true,
      "site": "00b4626c",
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
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b461d0",
      "incomplete_value": true,
      "site": "00b461d0",
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
            "const:6f8:8"
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
      "definition_site": "00b46254",
      "incomplete_value": true,
      "site": "00b46254",
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
      "definition_site": "00b461b8",
      "incomplete_value": true,
      "site": "00b461b8",
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
      "definition_site": "00b46260",
      "incomplete_value": false,
      "site": "00b46264",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b461c4",
      "incomplete_value": false,
      "site": "00b461c8",
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
            "const:30d:8"
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
      "00b46250",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46260",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ],
    [
      "00b4626c",
      "WRITE",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46250",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46260",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b4626c",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b461c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md#insn-00b461c8) · [`00b461d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md#insn-00b461d0) · [`00b461b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461a4.md#insn-00b461b4)
- 新版 `00b46264`（命令位置の公開資料なし） · `00b4626c`（命令位置の公開資料なし） · `00b46250`（命令位置の公開資料なし）

~~~diff
- 00b461c8 ["INT_ADD", "register:40f0:8", ["const:b461c8:8", "const:4:8"]]
- 00b461c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46264 ["INT_ADD", "register:40f0:8", ["const:b46264:8", "const:4:8"]]
+ 00b46264 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b461c8 bytes 52530494
+ 00b46264 bytes 5f530494
- 00b461d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
- 00b461d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4626c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
+ 00b4626c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b461d0 bytes 607e03f9
+ 00b4626c bytes 60fe03f9
- 00b461b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
- 00b461b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
+ 00b46250 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b461b4 bytes 687e43f9
+ 00b46250 bytes 68fe43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95d4344b19489ebf76926347c332776"></a>

### [`00b461e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md) → [`00b46280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46280.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00b46210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b462ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46294",
      "incomplete_value": true,
      "site": "00b46294",
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
      "definition_site": "00b461f8",
      "incomplete_value": true,
      "site": "00b461f8",
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
      "00b46290",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46200",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46208",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b46290",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4629c",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b462a4",
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

- 旧版 [`00b461f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md#insn-00b461f8) · [`00b46208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md#insn-00b46208) · [`00b46210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b461e4.md#insn-00b46210)
- 新版 `00b46294`（命令位置の公開資料なし）

~~~diff
- 00b461f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b461f8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46294 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46294 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b461f8 bytes e80000b5
+ 00b46294 bytes e80000b5
- 00b46208 ["INT_ADD", "register:40f0:8", ["const:b46208:8", "const:4:8"]]
- 00b46208 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46208 bytes 42530494
- 00b46210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
- 00b46210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46210 bytes 607e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83af8640633b2f1993b33c0ee1ac2b84"></a>

### [`00b46224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46224.md) → [`00b462c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b462c0.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b46254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b462f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b462d4",
      "incomplete_value": true,
      "site": "00b462d4",
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
      "definition_site": "00b46238",
      "incomplete_value": true,
      "site": "00b46238",
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
      "00b462d0",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46244",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4624c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b462d0",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b462e0",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b462e8",
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

- 旧版 [`00b46238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46224.md#insn-00b46238) · [`00b4624c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46224.md#insn-00b4624c) · [`00b46254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46224.md#insn-00b46254)
- 新版 `00b462d4`（命令位置の公開資料なし）

~~~diff
- 00b46238 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46238 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b462d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b462d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46238 bytes 080100b5
+ 00b462d4 bytes 080100b5
- 00b4624c ["INT_ADD", "register:40f0:8", ["const:b4624c:8", "const:4:8"]]
- 00b4624c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4624c bytes 31530494
- 00b46254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
- 00b46254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46254 bytes 607e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aae9bd98824a5823cd9f6129284ee5d"></a>

### [`00b46268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md) → [`00b46304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46304.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b46268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4626c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4626c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46268",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4626c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46314",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46304",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46308",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46314",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md#insn-00b46268) · [`00b4626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md#insn-00b4626c) · [`00b4627c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46268.md#insn-00b4627c)
- 新版 `00b46318`（命令位置の公開資料なし）

~~~diff
- 00b46268 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b46268 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b46268 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b46268 bytes f30f1ef8
- 00b4626c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4626c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4626c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4626c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4626c bytes fd7b01a9
- 00b4627c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4627c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46318 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46318 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4627c bytes 080100b5
+ 00b46318 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c965a432cc4e27d686d707e8f846c7bf"></a>

### [`00b462b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md) → [`00b46354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46354.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b463dc",
      "incomplete_value": true,
      "site": "00b463dc",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46340",
      "incomplete_value": true,
      "site": "00b46340",
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
            "const:700:8"
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
      "definition_site": "00b46388",
      "incomplete_value": true,
      "site": "00b46394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b462ec",
      "incomplete_value": true,
      "site": "00b462f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f8:8"
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
      "00b46368",
      "READ",
      [
        "storage",
        "01125700",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46388",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463dc",
      "WRITE",
      [
        "storage",
        "01125700",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46368",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46388",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b463dc",
      "WRITE",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b462f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md#insn-00b462f8) · [`00b46340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md#insn-00b46340) · [`00b462cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b462b8.md#insn-00b462cc)
- 新版 `00b46394`（命令位置の公開資料なし） · `00b463dc`（命令位置の公開資料なし） · `00b46368`（命令位置の公開資料なし）

~~~diff
- 00b462f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b462f8 ["INT_ADD", "register:40f0:8", ["const:b462f8:8", "const:4:8"]]
- 00b462f8 ["CALLIND", null, ["register:0:8"]]
+ 00b46394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46394 ["INT_ADD", "register:40f0:8", ["const:b46394:8", "const:4:8"]]
+ 00b46394 ["CALLIND", null, ["register:0:8"]]
- 00b462f8 bytes 00013fd6
+ 00b46394 bytes 00013fd6
- 00b46340 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46340 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:700:8"]]
- 00b46340 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b463dc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b463dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:800:8"]]
+ 00b463dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46340 bytes a0021c39
+ 00b463dc bytes a0022039
- 00b462cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:700:8"]]
- 00b462cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b462cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46368 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:800:8"]]
+ 00b46368 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46368 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b462cc bytes a8025c39
+ 00b46368 bytes a8026039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c065bd91ed20e19b72c3a912618915"></a>

### [`00b46354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46354.md) → [`00b463f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b463f0.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4647c",
      "incomplete_value": true,
      "site": "00b4647c",
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
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b463e0",
      "incomplete_value": true,
      "site": "00b463e0",
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
            "const:6f8:8"
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
      "site": "00b4642c"
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
      "00b46404",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46410",
      "READ",
      [
        "storage",
        "01125700",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b46390",
      "WRITE",
      [
        "storage",
        "01125700",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46404",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46410",
      "READ",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4642c",
      "WRITE",
      [
        "storage",
        "01125800",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46354.md#insn-00b46390) · [`00b463c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46354.md#insn-00b463c8) · [`00b463dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46354.md#insn-00b463dc)
- 新版 `00b46478`（命令位置の公開資料なし）

~~~diff
- 00b46390 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46390 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46390 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:700:8"]]
- 00b46390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46390 bytes bf021c39
- 00b463c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b463c8 ["INT_ADD", "register:40f0:8", ["const:b463c8:8", "const:4:8"]]
- 00b463c8 ["CALLIND", null, ["register:0:8"]]
- 00b463c8 bytes 00013fd6
- 00b463dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b463dc ["INT_ADD", "register:40f0:8", ["const:b463dc:8", "const:4:8"]]
- 00b463dc ["CALLIND", null, ["register:0:8"]]
+ 00b46478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46478 ["INT_ADD", "register:40f0:8", ["const:b46478:8", "const:4:8"]]
+ 00b46478 ["CALLIND", null, ["register:0:8"]]
- 00b463dc bytes 00013fd6
+ 00b46478 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f78b52ce85ee6b895f519045a5184de5"></a>

### [`00b463f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md) → [`00b46490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46490.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b46434"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b464d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46410"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46408",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46410",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b464d4"
      ]
    ],
    [
      "unmatched:00b46418",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b464a4",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b464ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b464d4"
      ]
    ],
    [
      "00b464b4",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md#insn-00b46410) · [`00b4642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md#insn-00b4642c) · [`00b46434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b463f4.md#insn-00b46434)
- 新版 `00b464c8`（命令位置の公開資料なし）

~~~diff
- 00b46410 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46410 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46410 bytes 410100b5
- 00b4642c ["INT_ADD", "register:40f0:8", ["const:b4642c:8", "const:4:8"]]
- 00b4642c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b464c8 ["INT_ADD", "register:40f0:8", ["const:b464c8:8", "const:4:8"]]
+ 00b464c8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4642c bytes b9520494
+ 00b464c8 bytes c6520494
- 00b46434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
- 00b46434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46434 bytes 807e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-168ea1d4b4ef1a01ab07dfe5e6182231"></a>

### [`00b46464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md) → [`00b46500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46500.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4651c",
      "incomplete_value": false,
      "site": "00b46520",
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
      "definition_site": "00b46480",
      "incomplete_value": false,
      "site": "00b46484",
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
      "definition_site": "00b4652c",
      "incomplete_value": true,
      "site": "00b46538",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b46490",
      "incomplete_value": true,
      "site": "00b4649c",
      "value": [
        "LOAD",
        "8",
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
      "00b4651c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4652c",
      "DATA",
      [
        "storage",
        "01125708",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4651c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4652c",
      "DATA",
      [
        "storage",
        "01125808",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md#insn-00b46484) · [`00b46480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md#insn-00b46480) · [`00b4648c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md#insn-00b4648c)
- 新版 `00b46520`（命令位置の公開資料なし） · `00b4651c`（命令位置の公開資料なし） · `00b46528`（命令位置の公開資料なし）

~~~diff
- 00b46484 ["INT_ADD", "register:40f0:8", ["const:b46484:8", "const:4:8"]]
- 00b46484 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b46520 ["INT_ADD", "register:40f0:8", ["const:b46520:8", "const:4:8"]]
+ 00b46520 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b46484 bytes df520494
+ 00b46520 bytes ec520494
- 00b46480 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b46480 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46480 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46480 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4651c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4651c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4651c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4651c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46480 bytes 009c0d91
+ 00b4651c bytes 002c0c91
- 00b4648c ["COPY", "tmp:0:8", ["const:708:8"]]
- 00b4648c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4648c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4648c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b46528 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00b46528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4648c bytes 08211c91
+ 00b46528 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4da1acc951b1bc55a33eec4db6ed020"></a>

### [`00b464a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md) → [`00b4653c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b4653c.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4657c",
      "incomplete_value": true,
      "site": "00b4657c",
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
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b464e0",
      "incomplete_value": true,
      "site": "00b464e0",
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
            "const:6f8:8"
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
      "definition_site": "00b46558",
      "incomplete_value": true,
      "site": "00b46558",
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
      "definition_site": "00b464bc",
      "incomplete_value": true,
      "site": "00b464bc",
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
      "definition_site": "00b46560",
      "incomplete_value": false,
      "site": "00b46574",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b464c4",
      "incomplete_value": false,
      "site": "00b464d8",
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
            "const:30d:8"
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
      "00b46550",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46560",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ],
    [
      "00b4657c",
      "WRITE",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46550",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46560",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b4657c",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b464d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464d8) · [`00b464e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464e0) · [`00b464b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b464a0.md#insn-00b464b4)
- 新版 `00b46574`（命令位置の公開資料なし） · `00b4657c`（命令位置の公開資料なし） · `00b46550`（命令位置の公開資料なし）

~~~diff
- 00b464d8 ["INT_ADD", "register:40f0:8", ["const:b464d8:8", "const:4:8"]]
- 00b464d8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46574 ["INT_ADD", "register:40f0:8", ["const:b46574:8", "const:4:8"]]
+ 00b46574 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b464d8 bytes 8e520494
+ 00b46574 bytes 9b520494
- 00b464e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
- 00b464e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4657c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
+ 00b4657c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b464e0 bytes 807e03f9
+ 00b4657c bytes 80fe03f9
- 00b464b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
- 00b464b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
+ 00b46550 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b464b4 bytes 817e43f9
+ 00b46550 bytes 81fe43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa763d1e56a3b2089f824f15bd5f5a93"></a>

### [`00b4654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md) → [`00b465e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465e8.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b46614",
      "incomplete_value": true,
      "site": "00b46614",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46578",
      "incomplete_value": true,
      "site": "00b46578",
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
            "const:728:8"
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
      "definition_site": "00b465fc",
      "incomplete_value": true,
      "site": "00b465fc",
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
      "definition_site": "00b46560",
      "incomplete_value": true,
      "site": "00b46560",
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
      "definition_site": "00b46608",
      "incomplete_value": false,
      "site": "00b4660c",
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
            "const:cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4656c",
      "incomplete_value": false,
      "site": "00b46570",
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
            "const:121:8"
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
      "00b465f8",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46608",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b46614",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b465f8",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46608",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b46614",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b46570) · [`00b46578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b46578) · [`00b4655c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4654c.md#insn-00b4655c)
- 新版 `00b4660c`（命令位置の公開資料なし） · `00b46614`（命令位置の公開資料なし） · `00b465f8`（命令位置の公開資料なし）

~~~diff
- 00b46570 ["INT_ADD", "register:40f0:8", ["const:b46570:8", "const:4:8"]]
- 00b46570 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4660c ["INT_ADD", "register:40f0:8", ["const:b4660c:8", "const:4:8"]]
+ 00b4660c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46570 bytes 68520494
+ 00b4660c bytes 75520494
- 00b46578 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b46578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00b46614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46578 bytes 609603f9
+ 00b46614 bytes 601604f9
- 00b4655c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b4655c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b465f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00b465f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4655c bytes 689643f9
+ 00b465f8 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211ddff8c9a4bffafd933eaf64ca04d9"></a>

### [`00b4658c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md) → [`00b46628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46628.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b46654",
      "incomplete_value": true,
      "site": "00b46654",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b465b8",
      "incomplete_value": true,
      "site": "00b465b8",
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
            "const:728:8"
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
      "definition_site": "00b4663c",
      "incomplete_value": true,
      "site": "00b4663c",
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
      "definition_site": "00b465a0",
      "incomplete_value": true,
      "site": "00b465a0",
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
      "definition_site": "00b46644",
      "incomplete_value": false,
      "site": "00b4664c",
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
            "const:cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b465a8",
      "incomplete_value": false,
      "site": "00b465b0",
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
            "const:121:8"
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
      "00b46638",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46644",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b46654",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46638",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46644",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b46654",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b465b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b465b0) · [`00b465b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b465b8) · [`00b4659c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4658c.md#insn-00b4659c)
- 新版 `00b4664c`（命令位置の公開資料なし） · `00b46654`（命令位置の公開資料なし） · `00b46638`（命令位置の公開資料なし）

~~~diff
- 00b465b0 ["INT_ADD", "register:40f0:8", ["const:b465b0:8", "const:4:8"]]
- 00b465b0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4664c ["INT_ADD", "register:40f0:8", ["const:b4664c:8", "const:4:8"]]
+ 00b4664c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b465b0 bytes 58520494
+ 00b4664c bytes 65520494
- 00b465b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b465b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00b46654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b465b8 bytes 609603f9
+ 00b46654 bytes 601604f9
- 00b4659c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b4659c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00b46638 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4659c bytes 689643f9
+ 00b46638 bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8385a37b33c58236ba5cf23cf0af0dd"></a>

### [`00b465cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md) → [`00b46668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46668.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00b465fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46698"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4667c",
      "incomplete_value": true,
      "site": "00b4667c",
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
      "definition_site": "00b465e0",
      "incomplete_value": true,
      "site": "00b465e0",
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
      "00b46678",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4667c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46600"
      ]
    ],
    [
      "unmatched:00b465ec",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46678",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4667c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4669c"
      ]
    ],
    [
      "00b46688",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b465f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md#insn-00b465f4) · [`00b465fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md#insn-00b465fc) · [`00b4660c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b465cc.md#insn-00b4660c)

~~~diff
- 00b465f4 ["INT_ADD", "register:40f0:8", ["const:b465f4:8", "const:4:8"]]
- 00b465f4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b465f4 bytes 47520494
- 00b465fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b465fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b465fc bytes 609603f9
- 00b4660c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4660c ["RETURN", null, ["register:0:8"]]
- 00b4660c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a56954c591bed4b4553ebe731292c4"></a>

### [`00b46610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md) → [`00b466ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466ac.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b46640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b466dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b466c0",
      "incomplete_value": true,
      "site": "00b466c0",
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
      "definition_site": "00b46624",
      "incomplete_value": true,
      "site": "00b46624",
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
      "00b466bc",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46644"
      ]
    ],
    [
      "unmatched:00b4662c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b466bc",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b466c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b466e0"
      ]
    ],
    [
      "00b466c8",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md#insn-00b46638) · [`00b46640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md#insn-00b46640) · [`00b46650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46610.md#insn-00b46650)
- 新版 `00b466d4`（命令位置の公開資料なし）

~~~diff
- 00b46638 ["INT_ADD", "register:40f0:8", ["const:b46638:8", "const:4:8"]]
- 00b46638 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b466d4 ["INT_ADD", "register:40f0:8", ["const:b466d4:8", "const:4:8"]]
+ 00b466d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46638 bytes 36520494
+ 00b466d4 bytes 43520494
- 00b46640 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 00b46640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46640 bytes 609603f9
- 00b46650 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46650 ["RETURN", null, ["register:0:8"]]
- 00b46650 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d90b07601f55668ccb5239e059976638"></a>

### [`00b46660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md) → [`00b466fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466fc.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46660",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46664",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46668",
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
      "00b466fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b46700",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46704",
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

- 旧版 [`00b46660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md#insn-00b46660) · [`00b46664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md#insn-00b46664) · [`00b46668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46660.md#insn-00b46668)

~~~diff
- 00b46660 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b46660 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b46660 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b46660 bytes f50f1df8
- 00b46664 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b46664 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b46664 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b46664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46664 bytes f44f01a9
- 00b46668 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b46668 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b46668 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b46668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46668 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-def562f508050f173a4a3db76d564408"></a>

### [`00b466fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md) → [`00b46798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46798.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b466fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46700"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b466fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46700",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46704",
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
      "00b46798",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4679c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b467a0",
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

- 旧版 [`00b466fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md#insn-00b466fc) · [`00b46700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md#insn-00b46700) · [`00b46704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b466fc.md#insn-00b46704)

~~~diff
- 00b466fc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b466fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b466fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b466fc bytes f50f1df8
- 00b46700 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b46700 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b46700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b46700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46700 bytes f44f01a9
- 00b46704 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b46704 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b46704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b46704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46704 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fdaf1de82860c2bdba20808da3f0965"></a>

### [`00b4679c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md) → [`00b46838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46838.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b46878",
      "incomplete_value": true,
      "site": "00b46878",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b467dc",
      "incomplete_value": true,
      "site": "00b467dc",
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
            "const:728:8"
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
      "definition_site": "00b46854",
      "incomplete_value": true,
      "site": "00b46854",
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
      "definition_site": "00b467b8",
      "incomplete_value": true,
      "site": "00b467b8",
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
      "definition_site": "00b4685c",
      "incomplete_value": false,
      "site": "00b46870",
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
            "const:cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b467c0",
      "incomplete_value": false,
      "site": "00b467d4",
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
            "const:121:8"
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
      "00b4684c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4685c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ],
    [
      "00b46878",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4684c",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4685c",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b46878",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b467d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467d4) · [`00b467dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467dc) · [`00b467b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4679c.md#insn-00b467b0)
- 新版 `00b46870`（命令位置の公開資料なし） · `00b46878`（命令位置の公開資料なし） · `00b4684c`（命令位置の公開資料なし）

~~~diff
- 00b467d4 ["INT_ADD", "register:40f0:8", ["const:b467d4:8", "const:4:8"]]
- 00b467d4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46870 ["INT_ADD", "register:40f0:8", ["const:b46870:8", "const:4:8"]]
+ 00b46870 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b467d4 bytes cf510494
+ 00b46870 bytes dc510494
- 00b467dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b467dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00b46878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b467dc bytes 809603f9
+ 00b46878 bytes 801604f9
- 00b467b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b467b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4684c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00b4684c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b467b0 bytes 819643f9
+ 00b4684c bytes 811644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-124800766b0cced3d146ef633d0f2ebc"></a>

### [`00b4680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md) → [`00b468a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468a8.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b468c4",
      "incomplete_value": false,
      "site": "00b468c8",
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
      "definition_site": "00b46828",
      "incomplete_value": false,
      "site": "00b4682c",
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
      "definition_site": "00b468d4",
      "incomplete_value": true,
      "site": "00b468e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b46838",
      "incomplete_value": true,
      "site": "00b46844",
      "value": [
        "LOAD",
        "8",
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
      "00b468c4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b468d4",
      "DATA",
      [
        "storage",
        "01125738",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b468c4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b468d4",
      "DATA",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4682c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b4682c) · [`00b46828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b46828) · [`00b46834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b4680c.md#insn-00b46834)
- 新版 `00b468c8`（命令位置の公開資料なし） · `00b468c4`（命令位置の公開資料なし） · `00b468d0`（命令位置の公開資料なし）

~~~diff
- 00b4682c ["INT_ADD", "register:40f0:8", ["const:b4682c:8", "const:4:8"]]
- 00b4682c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b468c8 ["INT_ADD", "register:40f0:8", ["const:b468c8:8", "const:4:8"]]
+ 00b468c8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4682c bytes f5510494
+ 00b468c8 bytes 02520494
- 00b46828 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b46828 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46828 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46828 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b468c4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b468c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b468c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b468c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46828 bytes 009c0d91
+ 00b468c4 bytes 002c0c91
- 00b46834 ["COPY", "tmp:0:8", ["const:738:8"]]
- 00b46834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b468d0 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00b468d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b468d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b468d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46834 bytes 08e11c91
+ 00b468d0 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f75f344a52b9100f1b30187c75cda98d"></a>

### [`00b46848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md) → [`00b468e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468e4.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00b46888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46924"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46864"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4685c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46928"
      ]
    ],
    [
      "unmatched:00b4686c",
      "PARAM",
      [
        "storage",
        "002bd121",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b468f8",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46928"
      ]
    ],
    [
      "00b46908",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md#insn-00b46864) · [`00b46880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md#insn-00b46880) · [`00b46888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46848.md#insn-00b46888)
- 新版 `00b4691c`（命令位置の公開資料なし）

~~~diff
- 00b46864 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46864 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46864 bytes 410100b5
- 00b46880 ["INT_ADD", "register:40f0:8", ["const:b46880:8", "const:4:8"]]
- 00b46880 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4691c ["INT_ADD", "register:40f0:8", ["const:b4691c:8", "const:4:8"]]
+ 00b4691c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46880 bytes a4510494
+ 00b4691c bytes b1510494
- 00b46888 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
- 00b46888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46888 bytes 809603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34b16f9670fe0d76095068d104e52db"></a>

### [`00b468b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md) → [`00b46954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46954.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b46970",
      "incomplete_value": false,
      "site": "00b46974",
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
      "definition_site": "00b468d4",
      "incomplete_value": false,
      "site": "00b468d8",
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
      "definition_site": "00b46980",
      "incomplete_value": true,
      "site": "00b4698c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b468e4",
      "incomplete_value": true,
      "site": "00b468f0",
      "value": [
        "LOAD",
        "8",
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
      "00b46970",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b46980",
      "DATA",
      [
        "storage",
        "01125748",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46970",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b46980",
      "DATA",
      [
        "storage",
        "01125848",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md#insn-00b468d8) · [`00b468d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md#insn-00b468d4) · [`00b468e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md#insn-00b468e0)
- 新版 `00b46974`（命令位置の公開資料なし） · `00b46970`（命令位置の公開資料なし） · `00b4697c`（命令位置の公開資料なし）

~~~diff
- 00b468d8 ["INT_ADD", "register:40f0:8", ["const:b468d8:8", "const:4:8"]]
- 00b468d8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b46974 ["INT_ADD", "register:40f0:8", ["const:b46974:8", "const:4:8"]]
+ 00b46974 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b468d8 bytes ca510494
+ 00b46974 bytes d7510494
- 00b468d4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b468d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b468d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b468d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46970 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b46970 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46970 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46970 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b468d4 bytes 00781491
+ 00b46970 bytes 00341591
- 00b468e0 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00b468e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b468e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b468e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4697c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00b4697c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4697c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4697c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b468e0 bytes 08211d91
+ 00b4697c bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3114d3da6dcda55a7a159607a28303fe"></a>

### [`00b468f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md) → [`00b46990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46990.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

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
      "site": "00b468f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b468f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b468f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b468f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b468f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b469a0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46990",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46994",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b469a0",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b468f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md#insn-00b468f4) · [`00b468f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md#insn-00b468f8) · [`00b46908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468f4.md#insn-00b46908)
- 新版 `00b469a4`（命令位置の公開資料なし）

~~~diff
- 00b468f4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b468f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b468f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b468f4 bytes f30f1ef8
- 00b468f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b468f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b468f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b468f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b468f8 bytes fd7b01a9
- 00b46908 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46908 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b469a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b469a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46908 bytes e80000b5
+ 00b469a4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6918e287268172473799856ca8fb7222"></a>

### [`00b46934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md) → [`00b469d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b469d0.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00b469fc",
      "incomplete_value": true,
      "site": "00b469fc",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46960",
      "incomplete_value": true,
      "site": "00b46960",
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
            "const:750:8"
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
      "definition_site": "00b469e4",
      "incomplete_value": true,
      "site": "00b469e4",
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
      "definition_site": "00b46948",
      "incomplete_value": true,
      "site": "00b46948",
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
      "definition_site": "00b469ec",
      "incomplete_value": false,
      "site": "00b469f4",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46950",
      "incomplete_value": false,
      "site": "00b46958",
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
            "const:534:8"
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
      "00b469e0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b469ec",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b469fc",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b469e0",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b469ec",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b469fc",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md#insn-00b46958) · [`00b46960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md#insn-00b46960) · [`00b46944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46934.md#insn-00b46944)
- 新版 `00b469f4`（命令位置の公開資料なし） · `00b469fc`（命令位置の公開資料なし） · `00b469e0`（命令位置の公開資料なし）

~~~diff
- 00b46958 ["INT_ADD", "register:40f0:8", ["const:b46958:8", "const:4:8"]]
- 00b46958 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b469f4 ["INT_ADD", "register:40f0:8", ["const:b469f4:8", "const:4:8"]]
+ 00b469f4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46958 bytes 6e510494
+ 00b469f4 bytes 7b510494
- 00b46960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b46960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b469fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b469fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46960 bytes 60aa03f9
+ 00b469fc bytes 602a04f9
- 00b46944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b46944 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b469e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00b469e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46944 bytes 68aa43f9
+ 00b469e0 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4070cf5e26f39d9a70629464b4e8a295"></a>

### [`00b46974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md) → [`00b46a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a10.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b469a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46a40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46a24",
      "incomplete_value": true,
      "site": "00b46a24",
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
      "definition_site": "00b46988",
      "incomplete_value": true,
      "site": "00b46988",
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
      "00b46a20",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46994",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4699c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b46a20",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a30",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b46a38",
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

- 旧版 [`00b46988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md#insn-00b46988) · [`00b4699c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md#insn-00b4699c) · [`00b469a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46974.md#insn-00b469a4)
- 新版 `00b46a24`（命令位置の公開資料なし）

~~~diff
- 00b46988 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46988 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46a24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46a24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46988 bytes 080100b5
+ 00b46a24 bytes 080100b5
- 00b4699c ["INT_ADD", "register:40f0:8", ["const:b4699c:8", "const:4:8"]]
- 00b4699c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4699c bytes 5d510494
- 00b469a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b469a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b469a4 bytes 60aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a526c49fe1ebb7696fe1f0e8a8cff49"></a>

### [`00b469b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md) → [`00b46a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a54.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b469e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46a84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46a68",
      "incomplete_value": true,
      "site": "00b46a68",
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
      "definition_site": "00b469cc",
      "incomplete_value": true,
      "site": "00b469cc",
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
      "00b46a64",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b469d4",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b469e8",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46a64",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a70",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b46a84",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b469cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md#insn-00b469cc) · [`00b469e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md#insn-00b469e0) · [`00b469e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b469b8.md#insn-00b469e8)
- 新版 `00b46a68`（命令位置の公開資料なし） · `00b46a7c`（命令位置の公開資料なし）

~~~diff
- 00b469cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b469cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46a68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46a68 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b469cc bytes 080100b5
+ 00b46a68 bytes 080100b5
- 00b469e0 ["INT_ADD", "register:40f0:8", ["const:b469e0:8", "const:4:8"]]
- 00b469e0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46a7c ["INT_ADD", "register:40f0:8", ["const:b46a7c:8", "const:4:8"]]
+ 00b46a7c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b469e0 bytes 4c510494
+ 00b46a7c bytes 59510494
- 00b469e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b469e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b469e8 bytes 60aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483d829008417730189fa17b581d69e3"></a>

### [`00b46a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46a08.md) → [`00b46aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46aa4.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46a0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46a08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46a10",
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
      "00b46aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b46aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46aac",
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

- 旧版 [`00b46a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46a08.md#insn-00b46a08) · [`00b46a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46a08.md#insn-00b46a0c) · [`00b46a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46a08.md#insn-00b46a10)

~~~diff
- 00b46a08 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b46a08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b46a08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b46a08 bytes f50f1df8
- 00b46a0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b46a0c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b46a0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b46a0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46a0c bytes f44f01a9
- 00b46a10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b46a10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b46a10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b46a10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46a10 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb0feafac91f3638d2fc6bae147e3536"></a>

### [`00b46b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md) → [`00b46be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46be0.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b46c20",
      "incomplete_value": true,
      "site": "00b46c20",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46b84",
      "incomplete_value": true,
      "site": "00b46b84",
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
            "const:750:8"
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
      "definition_site": "00b46bfc",
      "incomplete_value": true,
      "site": "00b46bfc",
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
      "definition_site": "00b46b60",
      "incomplete_value": true,
      "site": "00b46b60",
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
      "definition_site": "00b46c04",
      "incomplete_value": false,
      "site": "00b46c18",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46b68",
      "incomplete_value": false,
      "site": "00b46b7c",
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
            "const:534:8"
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
      "00b46bf4",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c04",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b46c20",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46bf4",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c04",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b46c20",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b7c) · [`00b46b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b84) · [`00b46b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46b44.md#insn-00b46b58)
- 新版 `00b46c18`（命令位置の公開資料なし） · `00b46c20`（命令位置の公開資料なし） · `00b46bf4`（命令位置の公開資料なし）

~~~diff
- 00b46b7c ["INT_ADD", "register:40f0:8", ["const:b46b7c:8", "const:4:8"]]
- 00b46b7c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46c18 ["INT_ADD", "register:40f0:8", ["const:b46c18:8", "const:4:8"]]
+ 00b46c18 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46b7c bytes e5500494
+ 00b46c18 bytes f2500494
- 00b46b84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b46b84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b46c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46b84 bytes 80aa03f9
+ 00b46c20 bytes 802a04f9
- 00b46b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b46b58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46bf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b46bf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46b58 bytes 81aa43f9
+ 00b46bf4 bytes 812a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e90eb68b8698de33f0ad4177547bd7e"></a>

### [`00b46bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md) → [`00b46c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c50.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b46c6c",
      "incomplete_value": false,
      "site": "00b46c70",
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
      "definition_site": "00b46bd0",
      "incomplete_value": false,
      "site": "00b46bd4",
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
      "definition_site": "00b46c7c",
      "incomplete_value": true,
      "site": "00b46c88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b46be0",
      "incomplete_value": true,
      "site": "00b46bec",
      "value": [
        "LOAD",
        "8",
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
      "00b46c6c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b46c7c",
      "DATA",
      [
        "storage",
        "01125760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46c6c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b46c7c",
      "DATA",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md#insn-00b46bd4) · [`00b46bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md#insn-00b46bd0) · [`00b46bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md#insn-00b46bdc)
- 新版 `00b46c70`（命令位置の公開資料なし） · `00b46c6c`（命令位置の公開資料なし） · `00b46c78`（命令位置の公開資料なし）

~~~diff
- 00b46bd4 ["INT_ADD", "register:40f0:8", ["const:b46bd4:8", "const:4:8"]]
- 00b46bd4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b46c70 ["INT_ADD", "register:40f0:8", ["const:b46c70:8", "const:4:8"]]
+ 00b46c70 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b46bd4 bytes 0b510494
+ 00b46c70 bytes 18510494
- 00b46bd0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b46bd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46bd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46bd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46c6c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b46c6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46c6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46c6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46bd0 bytes 009c0d91
+ 00b46c6c bytes 002c0c91
- 00b46bdc ["COPY", "tmp:0:8", ["const:760:8"]]
- 00b46bdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b46bdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b46bdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b46c78 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00b46c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b46c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b46bdc bytes 08811d91
+ 00b46c78 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ab61064c4f867e9d80ca7e38cd32185"></a>

### [`00b46bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md) → [`00b46c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c8c.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b46ccc",
      "incomplete_value": true,
      "site": "00b46ccc",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46c30",
      "incomplete_value": true,
      "site": "00b46c30",
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
            "const:750:8"
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
      "definition_site": "00b46ca8",
      "incomplete_value": true,
      "site": "00b46ca8",
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
      "definition_site": "00b46c0c",
      "incomplete_value": true,
      "site": "00b46c0c",
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
      "definition_site": "00b46cb0",
      "incomplete_value": false,
      "site": "00b46cc4",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46c14",
      "incomplete_value": false,
      "site": "00b46c28",
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
            "const:534:8"
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
      "00b46ca0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb0",
      "PARAM",
      [
        "storage",
        "002b0534",
        null,
        "string"
      ]
    ],
    [
      "00b46ccc",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46ca0",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb0",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b46ccc",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md#insn-00b46c28) · [`00b46c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md#insn-00b46c30) · [`00b46c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bf0.md#insn-00b46c04)
- 新版 `00b46cc4`（命令位置の公開資料なし） · `00b46ccc`（命令位置の公開資料なし） · `00b46ca0`（命令位置の公開資料なし）

~~~diff
- 00b46c28 ["INT_ADD", "register:40f0:8", ["const:b46c28:8", "const:4:8"]]
- 00b46c28 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46cc4 ["INT_ADD", "register:40f0:8", ["const:b46cc4:8", "const:4:8"]]
+ 00b46cc4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46c28 bytes ba500494
+ 00b46cc4 bytes c7500494
- 00b46c30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b46c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b46ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46c30 bytes 80aa03f9
+ 00b46ccc bytes 802a04f9
- 00b46c04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b46c04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46ca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00b46ca0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46c04 bytes 81aa43f9
+ 00b46ca0 bytes 812a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f689dc53f4eeb481446fb63a34f0aa86"></a>

### [`00b46c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c9c.md) → [`00b46d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d38.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b46cc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46d64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46d4c",
      "incomplete_value": true,
      "site": "00b46d4c",
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
      "definition_site": "00b46cb0",
      "incomplete_value": true,
      "site": "00b46cb0",
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
      "00b46d48",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46cbc",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46cc0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b46d48",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d58",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b46d5c",
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

- 旧版 [`00b46cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c9c.md#insn-00b46cb0) · [`00b46cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c9c.md#insn-00b46cc0) · [`00b46cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c9c.md#insn-00b46cc8)
- 新版 `00b46d4c`（命令位置の公開資料なし）

~~~diff
- 00b46cb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46cb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46d4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46d4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b46cb0 bytes e80000b5
+ 00b46d4c bytes e80000b5
- 00b46cc0 ["INT_ADD", "register:40f0:8", ["const:b46cc0:8", "const:4:8"]]
- 00b46cc0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46cc0 bytes 94500494
- 00b46cc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b46cc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46cc8 bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c0128c7cbdda1d25e210595a515db2d"></a>

### [`00b46cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md) → [`00b46d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d78.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "site": "00b46d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46da4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46d8c",
      "incomplete_value": true,
      "site": "00b46d8c",
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
      "definition_site": "00b46cf0",
      "incomplete_value": true,
      "site": "00b46cf0",
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
      "00b46d88",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46d0c"
      ]
    ],
    [
      "unmatched:00b46cf8",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46d88",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46da8"
      ]
    ],
    [
      "00b46d94",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46d00) · [`00b46d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46d08) · [`00b46d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46cdc.md#insn-00b46d18)

~~~diff
- 00b46d00 ["INT_ADD", "register:40f0:8", ["const:b46d00:8", "const:4:8"]]
- 00b46d00 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46d00 bytes 84500494
- 00b46d08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b46d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46d08 bytes 60c203f9
- 00b46d18 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46d18 ["RETURN", null, ["register:0:8"]]
- 00b46d18 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c9e7f77f674448cdaf3e0ac673cbdd"></a>

### [`00b46d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d1c.md) → [`00b46db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46db8.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00b46d4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46de8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46dcc",
      "incomplete_value": true,
      "site": "00b46dcc",
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
      "definition_site": "00b46d30",
      "incomplete_value": true,
      "site": "00b46d30",
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
      "00b46dc8",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46d50"
      ]
    ],
    [
      "unmatched:00b46d3c",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46dc8",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46dec"
      ]
    ],
    [
      "00b46dd8",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d1c.md#insn-00b46d44) · [`00b46d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d1c.md#insn-00b46d4c) · [`00b46d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d1c.md#insn-00b46d5c)

~~~diff
- 00b46d44 ["INT_ADD", "register:40f0:8", ["const:b46d44:8", "const:4:8"]]
- 00b46d44 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46d44 bytes 73500494
- 00b46d4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b46d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46d4c bytes 60c203f9
- 00b46d5c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46d5c ["RETURN", null, ["register:0:8"]]
- 00b46d5c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ce4238bb2871ba0f1622f0205a8e585"></a>

### [`00b46d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md) → [`00b46dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46dfc.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46e2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46e10",
      "incomplete_value": true,
      "site": "00b46e10",
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
      "definition_site": "00b46d74",
      "incomplete_value": true,
      "site": "00b46d74",
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
      "00b46e0c",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46d94"
      ]
    ],
    [
      "unmatched:00b46d7c",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46e0c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46e30"
      ]
    ],
    [
      "00b46e18",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md#insn-00b46d74) · [`00b46d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md#insn-00b46d88) · [`00b46d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d60.md#insn-00b46d90)
- 新版 `00b46e10`（命令位置の公開資料なし） · `00b46e24`（命令位置の公開資料なし）

~~~diff
- 00b46d74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46d74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46e10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46e10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46d74 bytes 080100b5
+ 00b46e10 bytes 080100b5
- 00b46d88 ["INT_ADD", "register:40f0:8", ["const:b46d88:8", "const:4:8"]]
- 00b46d88 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46e24 ["INT_ADD", "register:40f0:8", ["const:b46e24:8", "const:4:8"]]
+ 00b46e24 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46d88 bytes 62500494
+ 00b46e24 bytes 6f500494
- 00b46d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b46d90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46d90 bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3989b81f5b387ac4a671dc9ecf67a500"></a>

### [`00b46db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md) → [`00b46e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46e4c.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b46ed4",
      "incomplete_value": true,
      "site": "00b46ed4",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e38",
      "incomplete_value": true,
      "site": "00b46e38",
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
            "const:788:8"
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
      "definition_site": "00b46e80",
      "incomplete_value": true,
      "site": "00b46e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46de4",
      "incomplete_value": true,
      "site": "00b46df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:780:8"
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
      "00b46e60",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e80",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ed4",
      "WRITE",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46e60",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e80",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ed4",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46df0) · [`00b46e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46e38) · [`00b46dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46db0.md#insn-00b46dc4)
- 新版 `00b46e8c`（命令位置の公開資料なし） · `00b46ed4`（命令位置の公開資料なし） · `00b46e60`（命令位置の公開資料なし）

~~~diff
- 00b46df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46df0 ["INT_ADD", "register:40f0:8", ["const:b46df0:8", "const:4:8"]]
- 00b46df0 ["CALLIND", null, ["register:0:8"]]
+ 00b46e8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46e8c ["INT_ADD", "register:40f0:8", ["const:b46e8c:8", "const:4:8"]]
+ 00b46e8c ["CALLIND", null, ["register:0:8"]]
- 00b46df0 bytes 00013fd6
+ 00b46e8c bytes 00013fd6
- 00b46e38 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46e38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
- 00b46e38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b46ed4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b46ed4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:888:8"]]
+ 00b46ed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46e38 bytes a0221e39
+ 00b46ed4 bytes a0222239
- 00b46dc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
- 00b46dc4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b46dc4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b46e60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:888:8"]]
+ 00b46e60 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b46e60 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b46dc4 bytes a8225e39
+ 00b46e60 bytes a8226239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7efd39515b3ad276396b18eb57d8ce6"></a>

### [`00b46e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md) → [`00b46ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ee8.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b46f24",
      "incomplete_value": true,
      "site": "00b46f24",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e88",
      "incomplete_value": true,
      "site": "00b46e88",
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
            "const:788:8"
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
      "definition_site": "00b46f74",
      "incomplete_value": true,
      "site": "00b46f74",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ed8",
      "incomplete_value": true,
      "site": "00b46ed8",
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
            "const:780:8"
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
      "definition_site": "00b46f00",
      "incomplete_value": true,
      "site": "00b46f00",
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
      "definition_site": "00b46e64",
      "incomplete_value": true,
      "site": "00b46e64",
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
      "00b46efc",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f08",
      "READ",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46f24",
      "WRITE",
      [
        "storage",
        "01125788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46efc",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46f08",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46f24",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46e88) · [`00b46ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46ed4) · [`00b46ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46e4c.md#insn-00b46ed8)
- 新版 `00b46f24`（命令位置の公開資料なし） · `00b46f70`（命令位置の公開資料なし） · `00b46f74`（命令位置の公開資料なし）

~~~diff
- 00b46e88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46e88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46e88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
- 00b46e88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46f24 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46f24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:888:8"]]
+ 00b46f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46e88 bytes bf221e39
+ 00b46f24 bytes bf222239
- 00b46ed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46ed4 ["INT_ADD", "register:40f0:8", ["const:b46ed4:8", "const:4:8"]]
- 00b46ed4 ["CALLIND", null, ["register:0:8"]]
+ 00b46f70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46f70 ["INT_ADD", "register:40f0:8", ["const:b46f70:8", "const:4:8"]]
+ 00b46f70 ["CALLIND", null, ["register:0:8"]]
- 00b46ed4 bytes 00013fd6
+ 00b46f70 bytes 00013fd6
- 00b46ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b46ed8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46ed8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b46f74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b46f74 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b46f74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46ed8 bytes 9fc203f9
+ 00b46f74 bytes 9f4204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2973041edcc803b8e666ee574615d064"></a>

### [`00b46eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md) → [`00b46f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46f88.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b46fc8",
      "incomplete_value": true,
      "site": "00b46fc8",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f2c",
      "incomplete_value": true,
      "site": "00b46f2c",
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
            "const:780:8"
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
      "definition_site": "00b46fa4",
      "incomplete_value": true,
      "site": "00b46fa4",
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
      "definition_site": "00b46f08",
      "incomplete_value": true,
      "site": "00b46f08",
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
      "definition_site": "00b46fac",
      "incomplete_value": false,
      "site": "00b46fc0",
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
            "const:a02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f10",
      "incomplete_value": false,
      "site": "00b46f24",
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
            "const:a56:8"
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
      "00b46f9c",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46fac",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ],
    [
      "00b46fc8",
      "WRITE",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46f9c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46fac",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b46fc8",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md#insn-00b46f24) · [`00b46f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md#insn-00b46f2c) · [`00b46f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46eec.md#insn-00b46f00)
- 新版 `00b46fc0`（命令位置の公開資料なし） · `00b46fc8`（命令位置の公開資料なし） · `00b46f9c`（命令位置の公開資料なし）

~~~diff
- 00b46f24 ["INT_ADD", "register:40f0:8", ["const:b46f24:8", "const:4:8"]]
- 00b46f24 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b46fc0 ["INT_ADD", "register:40f0:8", ["const:b46fc0:8", "const:4:8"]]
+ 00b46fc0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46f24 bytes fb4f0494
+ 00b46fc0 bytes 08500494
- 00b46f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b46f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46fc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b46fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46f2c bytes 80c203f9
+ 00b46fc8 bytes 804204f9
- 00b46f00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b46f00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46f9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
+ 00b46f9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46f00 bytes 81c243f9
+ 00b46f9c bytes 814244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7767a0ad9d0fac26b68a38e08a12d7"></a>

### [`00b46f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md) → [`00b47034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47034.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b46fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47074"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46fb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46fac",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47078"
      ]
    ],
    [
      "unmatched:00b46fbc",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47048",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47078"
      ]
    ],
    [
      "00b47058",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md#insn-00b46fb4) · [`00b46fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md#insn-00b46fd0) · [`00b46fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f98.md#insn-00b46fd8)
- 新版 `00b4706c`（命令位置の公開資料なし）

~~~diff
- 00b46fb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b46fb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46fb4 bytes 410100b5
- 00b46fd0 ["INT_ADD", "register:40f0:8", ["const:b46fd0:8", "const:4:8"]]
- 00b46fd0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4706c ["INT_ADD", "register:40f0:8", ["const:b4706c:8", "const:4:8"]]
+ 00b4706c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b46fd0 bytes d04f0494
+ 00b4706c bytes dd4f0494
- 00b46fd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b46fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46fd8 bytes 80c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4f739c5cdb3e30337092db05423549"></a>

### [`00b47044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47044.md) → [`00b470e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470e0.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_call_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4710c",
      "incomplete_value": true,
      "site": "00b4710c",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47070",
      "incomplete_value": true,
      "site": "00b47070",
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
            "const:7a8:8"
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
      "definition_site": "00b470f4",
      "incomplete_value": true,
      "site": "00b470f4",
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
      "definition_site": "00b47058",
      "incomplete_value": true,
      "site": "00b47058",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b470f0",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47064",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b47068",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b470f0",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47100",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b47104",
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

- 旧版 [`00b47068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47044.md#insn-00b47068) · [`00b47070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47044.md#insn-00b47070)
- 新版 `00b4710c`（命令位置の公開資料なし） · `00b47104`（命令位置の公開資料なし）

~~~diff
- 00b47068 ["INT_ADD", "register:40f0:8", ["const:b47068:8", "const:4:8"]]
- 00b47068 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47068 bytes aa4f0494
- 00b47070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00b47070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4710c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4710c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47070 bytes 60d603f9
+ 00b4710c bytes 605604f9
+ 00b47104 ["INT_ADD", "register:40f0:8", ["const:b47104:8", "const:4:8"]]
+ 00b47104 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47104 bytes b74f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a4c3c576a42d1c865b2f4c4ff60824"></a>

### [`00b47084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47084.md) → [`00b47120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47120.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4714c",
      "incomplete_value": true,
      "site": "00b4714c",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b470b0",
      "incomplete_value": true,
      "site": "00b470b0",
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
            "const:7a8:8"
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
      "definition_site": "00b47134",
      "incomplete_value": true,
      "site": "00b47134",
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
      "definition_site": "00b47098",
      "incomplete_value": true,
      "site": "00b47098",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b470a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47130",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b470a0",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b470a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b47130",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4713c",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b47144",
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

- 旧版 [`00b470a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47084.md#insn-00b470a8) · [`00b470b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47084.md#insn-00b470b0)
- 新版 `00b4714c`（命令位置の公開資料なし） · `00b47144`（命令位置の公開資料なし）

~~~diff
- 00b470a8 ["INT_ADD", "register:40f0:8", ["const:b470a8:8", "const:4:8"]]
- 00b470a8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b470a8 bytes 9a4f0494
- 00b470b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00b470b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4714c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b4714c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b470b0 bytes 60d603f9
+ 00b4714c bytes 605604f9
+ 00b47144 ["INT_ADD", "register:40f0:8", ["const:b47144:8", "const:4:8"]]
+ 00b47144 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47144 bytes a74f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8769dd0426e1f70ce413fde3941508b7"></a>

### [`00b470c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md) → [`00b47160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47160.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b470f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47190"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47174",
      "incomplete_value": true,
      "site": "00b47174",
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
      "definition_site": "00b470d8",
      "incomplete_value": true,
      "site": "00b470d8",
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
      "00b47170",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b470e4",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b470ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b47170",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47180",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b47188",
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

- 旧版 [`00b470d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md#insn-00b470d8) · [`00b470ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md#insn-00b470ec) · [`00b470f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b470c4.md#insn-00b470f4)
- 新版 `00b47174`（命令位置の公開資料なし）

~~~diff
- 00b470d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b470d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47174 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47174 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b470d8 bytes 080100b5
+ 00b47174 bytes 080100b5
- 00b470ec ["INT_ADD", "register:40f0:8", ["const:b470ec:8", "const:4:8"]]
- 00b470ec ["CALL", null, ["callee:00c5afe0:8"]]
- 00b470ec bytes 894f0494
- 00b470f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00b470f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b470f4 bytes 60d603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5557e219e4016e543d5b55ddb967b0e"></a>

### [`00b47108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md) → [`00b471a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471a4.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b471d4",
      "incomplete_value": true,
      "site": "00b471d4",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47138",
      "incomplete_value": true,
      "site": "00b47138",
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
            "const:7a8:8"
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
      "definition_site": "00b471b8",
      "incomplete_value": true,
      "site": "00b471b8",
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
      "definition_site": "00b4711c",
      "incomplete_value": true,
      "site": "00b4711c",
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
      "definition_site": "00b471c0",
      "incomplete_value": false,
      "site": "00b471cc",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47124",
      "incomplete_value": false,
      "site": "00b47130",
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
            "const:8bd:8"
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
      "00b471b4",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b471c0",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b471d4",
      "WRITE",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b471b4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b471c0",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b471d4",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47130) · [`00b47138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47138) · [`00b47118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47108.md#insn-00b47118)
- 新版 `00b471cc`（命令位置の公開資料なし） · `00b471d4`（命令位置の公開資料なし） · `00b471b4`（命令位置の公開資料なし）

~~~diff
- 00b47130 ["INT_ADD", "register:40f0:8", ["const:b47130:8", "const:4:8"]]
- 00b47130 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b471cc ["INT_ADD", "register:40f0:8", ["const:b471cc:8", "const:4:8"]]
+ 00b471cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47130 bytes 784f0494
+ 00b471cc bytes 854f0494
- 00b47138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00b47138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b471d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b471d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47138 bytes 60d603f9
+ 00b471d4 bytes 605604f9
- 00b47118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00b47118 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b471b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00b471b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47118 bytes 68d643f9
+ 00b471b4 bytes 685644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f87d1dc15b1f04335b5ea58123e3358"></a>

### [`00b47158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md) → [`00b471f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471f4.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4727c",
      "incomplete_value": true,
      "site": "00b4727c",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b471e0",
      "incomplete_value": true,
      "site": "00b471e0",
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
            "const:7b0:8"
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
      "definition_site": "00b47228",
      "incomplete_value": true,
      "site": "00b47234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4718c",
      "incomplete_value": true,
      "site": "00b47198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
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
      "00b47208",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47228",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4727c",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47208",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47228",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4727c",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md#insn-00b47198) · [`00b471e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md#insn-00b471e0) · [`00b4716c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47158.md#insn-00b4716c)
- 新版 `00b47234`（命令位置の公開資料なし） · `00b4727c`（命令位置の公開資料なし） · `00b47208`（命令位置の公開資料なし）

~~~diff
- 00b47198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47198 ["INT_ADD", "register:40f0:8", ["const:b47198:8", "const:4:8"]]
- 00b47198 ["CALLIND", null, ["register:0:8"]]
+ 00b47234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47234 ["INT_ADD", "register:40f0:8", ["const:b47234:8", "const:4:8"]]
+ 00b47234 ["CALLIND", null, ["register:0:8"]]
- 00b47198 bytes 00013fd6
+ 00b47234 bytes 00013fd6
- 00b471e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b471e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7b0:8"]]
- 00b471e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4727c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4727c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b4727c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b471e0 bytes a0c21e39
+ 00b4727c bytes a0c22239
- 00b4716c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b0:8"]]
- 00b4716c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4716c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b47208 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b47208 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b47208 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4716c bytes a8c25e39
+ 00b47208 bytes a8c26239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10913b789ddaff9e77934a485e93558c"></a>

### [`00b471f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md) → [`00b47290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47290.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b472cc",
      "incomplete_value": true,
      "site": "00b472cc",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47230",
      "incomplete_value": true,
      "site": "00b47230",
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
            "const:7b0:8"
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
      "definition_site": "00b4731c",
      "incomplete_value": true,
      "site": "00b4731c",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47280",
      "incomplete_value": true,
      "site": "00b47280",
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
            "const:7a8:8"
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
      "definition_site": "00b472a8",
      "incomplete_value": true,
      "site": "00b472a8",
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
      "definition_site": "00b4720c",
      "incomplete_value": true,
      "site": "00b4720c",
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
      "00b472a4",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b472b0",
      "READ",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b472cc",
      "WRITE",
      [
        "storage",
        "011257b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b472a4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b472b0",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b472cc",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b47230) · [`00b4727c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b4727c) · [`00b47280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b471f4.md#insn-00b47280)
- 新版 `00b472cc`（命令位置の公開資料なし） · `00b47318`（命令位置の公開資料なし） · `00b4731c`（命令位置の公開資料なし）

~~~diff
- 00b47230 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47230 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47230 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7b0:8"]]
- 00b47230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b472cc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b472cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b472cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
+ 00b472cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47230 bytes bfc21e39
+ 00b472cc bytes bfc22239
- 00b4727c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4727c ["INT_ADD", "register:40f0:8", ["const:b4727c:8", "const:4:8"]]
- 00b4727c ["CALLIND", null, ["register:0:8"]]
+ 00b47318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47318 ["INT_ADD", "register:40f0:8", ["const:b47318:8", "const:4:8"]]
+ 00b47318 ["CALLIND", null, ["register:0:8"]]
- 00b4727c bytes 00013fd6
+ 00b47318 bytes 00013fd6
- 00b47280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00b47280 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4731c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b4731c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4731c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47280 bytes 9fd603f9
+ 00b4731c bytes 9f5604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9235f5e4cce4f4ab7b29fce5f3138f7"></a>

### [`00b47294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47294.md) → [`00b47330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47330.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47370",
      "incomplete_value": true,
      "site": "00b47370",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b472d4",
      "incomplete_value": true,
      "site": "00b472d4",
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
            "const:7a8:8"
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
      "definition_site": "00b4734c",
      "incomplete_value": true,
      "site": "00b4734c",
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
      "definition_site": "00b472b0",
      "incomplete_value": true,
      "site": "00b472b0",
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
      "definition_site": "00b47354",
      "incomplete_value": false,
      "site": "00b47368",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b472b8",
      "incomplete_value": false,
      "site": "00b472cc",
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
            "const:8bd:8"
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
      "00b47344",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47354",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b47370",
      "WRITE",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47344",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47354",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b47370",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b472cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47294.md#insn-00b472cc) · [`00b472d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47294.md#insn-00b472d4) · [`00b472a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47294.md#insn-00b472a8)
- 新版 `00b47368`（命令位置の公開資料なし） · `00b47370`（命令位置の公開資料なし） · `00b47344`（命令位置の公開資料なし）

~~~diff
- 00b472cc ["INT_ADD", "register:40f0:8", ["const:b472cc:8", "const:4:8"]]
- 00b472cc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47368 ["INT_ADD", "register:40f0:8", ["const:b47368:8", "const:4:8"]]
+ 00b47368 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b472cc bytes 114f0494
+ 00b47368 bytes 1e4f0494
- 00b472d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00b472d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b47370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b472d4 bytes 80d603f9
+ 00b47370 bytes 805604f9
- 00b472a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00b472a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b47344 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b472a8 bytes 81d643f9
+ 00b47344 bytes 815644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86172eef1bb6b3434bc70ce889686151"></a>

### [`00b47304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md) → [`00b473a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473a0.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b473bc",
      "incomplete_value": false,
      "site": "00b473c0",
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
      "definition_site": "00b47320",
      "incomplete_value": false,
      "site": "00b47324",
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
      "definition_site": "00b473cc",
      "incomplete_value": true,
      "site": "00b473d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47330",
      "incomplete_value": true,
      "site": "00b4733c",
      "value": [
        "LOAD",
        "8",
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
      "00b473bc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b473cc",
      "DATA",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b473bc",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b473cc",
      "DATA",
      [
        "storage",
        "011258b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b47324) · [`00b47320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b47320) · [`00b4732c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47304.md#insn-00b4732c)
- 新版 `00b473c0`（命令位置の公開資料なし） · `00b473bc`（命令位置の公開資料なし） · `00b473c8`（命令位置の公開資料なし）

~~~diff
- 00b47324 ["INT_ADD", "register:40f0:8", ["const:b47324:8", "const:4:8"]]
- 00b47324 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b473c0 ["INT_ADD", "register:40f0:8", ["const:b473c0:8", "const:4:8"]]
+ 00b473c0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b47324 bytes 374f0494
+ 00b473c0 bytes 444f0494
- 00b47320 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b47320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b473bc ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b473bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b473bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b473bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47320 bytes 009c0d91
+ 00b473bc bytes 002c0c91
- 00b4732c ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00b4732c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4732c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4732c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b473c8 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00b473c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b473c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b473c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4732c bytes 08e11e91
+ 00b473c8 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da073ee78db2dd010532755a7c0b105e"></a>

### [`00b47340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md) → [`00b473dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473dc.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4741c",
      "incomplete_value": true,
      "site": "00b4741c",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47380",
      "incomplete_value": true,
      "site": "00b47380",
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
            "const:7a8:8"
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
      "definition_site": "00b473f8",
      "incomplete_value": true,
      "site": "00b473f8",
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
      "definition_site": "00b4735c",
      "incomplete_value": true,
      "site": "00b4735c",
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
      "definition_site": "00b47400",
      "incomplete_value": false,
      "site": "00b47414",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47364",
      "incomplete_value": false,
      "site": "00b47378",
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
            "const:8bd:8"
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
      "00b473f0",
      "READ",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47400",
      "PARAM",
      [
        "storage",
        "002b58bd",
        null,
        "string"
      ]
    ],
    [
      "00b4741c",
      "WRITE",
      [
        "storage",
        "011257a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b473f0",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47400",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b4741c",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47378) · [`00b47380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47380) · [`00b47354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47340.md#insn-00b47354)
- 新版 `00b47414`（命令位置の公開資料なし） · `00b4741c`（命令位置の公開資料なし） · `00b473f0`（命令位置の公開資料なし）

~~~diff
- 00b47378 ["INT_ADD", "register:40f0:8", ["const:b47378:8", "const:4:8"]]
- 00b47378 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47414 ["INT_ADD", "register:40f0:8", ["const:b47414:8", "const:4:8"]]
+ 00b47414 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47378 bytes e64e0494
+ 00b47414 bytes f34e0494
- 00b47380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00b47380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4741c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b4741c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47380 bytes 80d603f9
+ 00b4741c bytes 805604f9
- 00b47354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00b47354 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b473f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00b473f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47354 bytes 81d643f9
+ 00b473f0 bytes 815644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50087750745b8f9efd0a36e569ada8cb"></a>

### [`00b473b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md) → [`00b4744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4744c.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b47468",
      "incomplete_value": false,
      "site": "00b4746c",
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
      "definition_site": "00b473cc",
      "incomplete_value": false,
      "site": "00b473d0",
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
      "definition_site": "00b47478",
      "incomplete_value": true,
      "site": "00b47484",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b473dc",
      "incomplete_value": true,
      "site": "00b473e8",
      "value": [
        "LOAD",
        "8",
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
      "00b47468",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47478",
      "DATA",
      [
        "storage",
        "011257c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47468",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b47478",
      "DATA",
      [
        "storage",
        "011258c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b473d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473d0) · [`00b473cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473cc) · [`00b473d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473b0.md#insn-00b473d8)
- 新版 `00b4746c`（命令位置の公開資料なし） · `00b47468`（命令位置の公開資料なし） · `00b47474`（命令位置の公開資料なし）

~~~diff
- 00b473d0 ["INT_ADD", "register:40f0:8", ["const:b473d0:8", "const:4:8"]]
- 00b473d0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4746c ["INT_ADD", "register:40f0:8", ["const:b4746c:8", "const:4:8"]]
+ 00b4746c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b473d0 bytes 0c4f0494
+ 00b4746c bytes 194f0494
- 00b473cc ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b473cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b473cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b473cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47468 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b47468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b473cc bytes 00781491
+ 00b47468 bytes 00341591
- 00b473d8 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00b473d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b473d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b473d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47474 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00b47474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b473d8 bytes 08011f91
+ 00b47474 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f666a4ca0f1b48a47d4c7cfab7578e"></a>

### [`00b473ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md) → [`00b47488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47488.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00b474b4",
      "incomplete_value": true,
      "site": "00b474b4",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47418",
      "incomplete_value": true,
      "site": "00b47418",
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
            "const:7c8:8"
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
      "definition_site": "00b4749c",
      "incomplete_value": true,
      "site": "00b4749c",
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
      "definition_site": "00b47400",
      "incomplete_value": true,
      "site": "00b47400",
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
      "definition_site": "00b474a8",
      "incomplete_value": false,
      "site": "00b474ac",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4740c",
      "incomplete_value": false,
      "site": "00b47410",
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
            "const:5d1:8"
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
      "00b47498",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474a8",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b474b4",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47498",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474a8",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b474b4",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b47410) · [`00b47418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b47418) · [`00b473fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b473ec.md#insn-00b473fc)
- 新版 `00b474ac`（命令位置の公開資料なし） · `00b474b4`（命令位置の公開資料なし） · `00b47498`（命令位置の公開資料なし）

~~~diff
- 00b47410 ["INT_ADD", "register:40f0:8", ["const:b47410:8", "const:4:8"]]
- 00b47410 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b474ac ["INT_ADD", "register:40f0:8", ["const:b474ac:8", "const:4:8"]]
+ 00b474ac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47410 bytes c04e0494
+ 00b474ac bytes cd4e0494
- 00b47418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b47418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b474b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b474b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47418 bytes 60e603f9
+ 00b474b4 bytes 606604f9
- 00b473fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b473fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47498 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b47498 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b473fc bytes 68e643f9
+ 00b47498 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd2c022a812ea526a21767dec02cbce"></a>

### [`00b4742c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md) → [`00b474c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b474c8.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b474f4",
      "incomplete_value": true,
      "site": "00b474f4",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47458",
      "incomplete_value": true,
      "site": "00b47458",
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
            "const:7c8:8"
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
      "definition_site": "00b474dc",
      "incomplete_value": true,
      "site": "00b474dc",
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
      "definition_site": "00b47440",
      "incomplete_value": true,
      "site": "00b47440",
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
      "definition_site": "00b474e4",
      "incomplete_value": false,
      "site": "00b474ec",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47448",
      "incomplete_value": false,
      "site": "00b47450",
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
            "const:5d1:8"
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
      "00b474d8",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474e4",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b474f4",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b474d8",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b474e4",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b474f4",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b47450) · [`00b47458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b47458) · [`00b4743c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4742c.md#insn-00b4743c)
- 新版 `00b474ec`（命令位置の公開資料なし） · `00b474f4`（命令位置の公開資料なし） · `00b474d8`（命令位置の公開資料なし）

~~~diff
- 00b47450 ["INT_ADD", "register:40f0:8", ["const:b47450:8", "const:4:8"]]
- 00b47450 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b474ec ["INT_ADD", "register:40f0:8", ["const:b474ec:8", "const:4:8"]]
+ 00b474ec ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47450 bytes b04e0494
+ 00b474ec bytes bd4e0494
- 00b47458 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b47458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b474f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b474f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47458 bytes 60e603f9
+ 00b474f4 bytes 606604f9
- 00b4743c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b4743c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b474d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b474d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4743c bytes 68e643f9
+ 00b474d8 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3c8de77f148a2d2967048d39d926c7"></a>

### [`00b4746c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md) → [`00b47508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47508.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b47538",
      "incomplete_value": true,
      "site": "00b47538",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4749c",
      "incomplete_value": true,
      "site": "00b4749c",
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
            "const:7c8:8"
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
      "definition_site": "00b4751c",
      "incomplete_value": true,
      "site": "00b4751c",
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
      "definition_site": "00b47480",
      "incomplete_value": true,
      "site": "00b47480",
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
      "definition_site": "00b47528",
      "incomplete_value": false,
      "site": "00b47530",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4748c",
      "incomplete_value": false,
      "site": "00b47494",
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
            "const:5d1:8"
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
      "00b47518",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47528",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b47538",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47518",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47528",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b47538",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b47494) · [`00b4749c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b4749c) · [`00b4747c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4746c.md#insn-00b4747c)
- 新版 `00b47530`（命令位置の公開資料なし） · `00b47538`（命令位置の公開資料なし） · `00b47518`（命令位置の公開資料なし）

~~~diff
- 00b47494 ["INT_ADD", "register:40f0:8", ["const:b47494:8", "const:4:8"]]
- 00b47494 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47530 ["INT_ADD", "register:40f0:8", ["const:b47530:8", "const:4:8"]]
+ 00b47530 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47494 bytes 9f4e0494
+ 00b47530 bytes ac4e0494
- 00b4749c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b4749c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b47538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4749c bytes 60e603f9
+ 00b47538 bytes 606604f9
- 00b4747c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b4747c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b47518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4747c bytes 68e643f9
+ 00b47518 bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e95cee3ccdd0ec707bc0bb6001d3594"></a>

### [`00b474b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md) → [`00b4754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4754c.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4757c",
      "incomplete_value": true,
      "site": "00b4757c",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474e0",
      "incomplete_value": true,
      "site": "00b474e0",
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
            "const:7c8:8"
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
      "definition_site": "00b47560",
      "incomplete_value": true,
      "site": "00b47560",
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
      "definition_site": "00b474c4",
      "incomplete_value": true,
      "site": "00b474c4",
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
      "definition_site": "00b47568",
      "incomplete_value": false,
      "site": "00b47574",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474cc",
      "incomplete_value": false,
      "site": "00b474d8",
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
            "const:5d1:8"
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
      "00b4755c",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47568",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b4757c",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4755c",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47568",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b4757c",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b474d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474d8) · [`00b474e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474e0) · [`00b474c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b474b0.md#insn-00b474c0)
- 新版 `00b47574`（命令位置の公開資料なし） · `00b4757c`（命令位置の公開資料なし） · `00b4755c`（命令位置の公開資料なし）

~~~diff
- 00b474d8 ["INT_ADD", "register:40f0:8", ["const:b474d8:8", "const:4:8"]]
- 00b474d8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47574 ["INT_ADD", "register:40f0:8", ["const:b47574:8", "const:4:8"]]
+ 00b47574 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b474d8 bytes 8e4e0494
+ 00b47574 bytes 9b4e0494
- 00b474e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b474e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4757c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b4757c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b474e0 bytes 60e603f9
+ 00b4757c bytes 606604f9
- 00b474c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b474c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4755c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00b4755c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b474c0 bytes 68e643f9
+ 00b4755c bytes 686644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc63f8073dfcf1b56190de5426151f9"></a>

### [`00b47500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md) → [`00b4759c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4759c.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b47624",
      "incomplete_value": true,
      "site": "00b47624",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47588",
      "incomplete_value": true,
      "site": "00b47588",
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
            "const:7d0:8"
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
      "definition_site": "00b475d0",
      "incomplete_value": true,
      "site": "00b475dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47534",
      "incomplete_value": true,
      "site": "00b47540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
      "00b475b0",
      "READ",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b475d0",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47624",
      "WRITE",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b475b0",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b475d0",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47624",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47540) · [`00b47588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47588) · [`00b47514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47500.md#insn-00b47514)
- 新版 `00b475dc`（命令位置の公開資料なし） · `00b47624`（命令位置の公開資料なし） · `00b475b0`（命令位置の公開資料なし）

~~~diff
- 00b47540 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47540 ["INT_ADD", "register:40f0:8", ["const:b47540:8", "const:4:8"]]
- 00b47540 ["CALLIND", null, ["register:0:8"]]
+ 00b475dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b475dc ["INT_ADD", "register:40f0:8", ["const:b475dc:8", "const:4:8"]]
+ 00b475dc ["CALLIND", null, ["register:0:8"]]
- 00b47540 bytes 00013fd6
+ 00b475dc bytes 00013fd6
- 00b47588 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47588 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d0:8"]]
- 00b47588 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47624 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47624 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b47624 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47588 bytes a0421f39
+ 00b47624 bytes a0422339
- 00b47514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d0:8"]]
- 00b47514 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b47514 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b475b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b475b0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b475b0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b47514 bytes a8425f39
+ 00b475b0 bytes a8426339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118c5ed476badddf21d2299fff8b0aa2"></a>

### [`00b4759c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md) → [`00b47638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47638.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b47674",
      "incomplete_value": true,
      "site": "00b47674",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b475d8",
      "incomplete_value": true,
      "site": "00b475d8",
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
            "const:7d0:8"
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
      "definition_site": "00b476c4",
      "incomplete_value": true,
      "site": "00b476c4",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47628",
      "incomplete_value": true,
      "site": "00b47628",
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
            "const:7c8:8"
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
      "definition_site": "00b47650",
      "incomplete_value": true,
      "site": "00b47650",
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
      "definition_site": "00b475b4",
      "incomplete_value": true,
      "site": "00b475b4",
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
      "00b4764c",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47658",
      "READ",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47674",
      "WRITE",
      [
        "storage",
        "011257d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4764c",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47658",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47674",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b475d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b475d8) · [`00b47624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b47624) · [`00b47628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4759c.md#insn-00b47628)
- 新版 `00b47674`（命令位置の公開資料なし） · `00b476c0`（命令位置の公開資料なし） · `00b476c4`（命令位置の公開資料なし）

~~~diff
- 00b475d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b475d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b475d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d0:8"]]
- 00b475d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47674 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47674 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47674 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d0:8"]]
+ 00b47674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b475d8 bytes bf421f39
+ 00b47674 bytes bf422339
- 00b47624 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47624 ["INT_ADD", "register:40f0:8", ["const:b47624:8", "const:4:8"]]
- 00b47624 ["CALLIND", null, ["register:0:8"]]
+ 00b476c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b476c0 ["INT_ADD", "register:40f0:8", ["const:b476c0:8", "const:4:8"]]
+ 00b476c0 ["CALLIND", null, ["register:0:8"]]
- 00b47624 bytes 00013fd6
+ 00b476c0 bytes 00013fd6
- 00b47628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b47628 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b476c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b476c4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b476c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47628 bytes 9fe603f9
+ 00b476c4 bytes 9f6604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec2aea36f857f4e410ae03be45c88f7b"></a>

### [`00b4763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md) → [`00b476d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b476d8.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47718",
      "incomplete_value": true,
      "site": "00b47718",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4767c",
      "incomplete_value": true,
      "site": "00b4767c",
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
            "const:7c8:8"
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
      "definition_site": "00b476f4",
      "incomplete_value": true,
      "site": "00b476f4",
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
      "definition_site": "00b47658",
      "incomplete_value": true,
      "site": "00b47658",
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
      "definition_site": "00b476fc",
      "incomplete_value": false,
      "site": "00b47710",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47660",
      "incomplete_value": false,
      "site": "00b47674",
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
            "const:5d1:8"
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
      "00b476ec",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b476fc",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b47718",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b476ec",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b476fc",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b47718",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b47674) · [`00b4767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b4767c) · [`00b47650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b4763c.md#insn-00b47650)
- 新版 `00b47710`（命令位置の公開資料なし） · `00b47718`（命令位置の公開資料なし） · `00b476ec`（命令位置の公開資料なし）

~~~diff
- 00b47674 ["INT_ADD", "register:40f0:8", ["const:b47674:8", "const:4:8"]]
- 00b47674 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47710 ["INT_ADD", "register:40f0:8", ["const:b47710:8", "const:4:8"]]
+ 00b47710 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47674 bytes 274e0494
+ 00b47710 bytes 344e0494
- 00b4767c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b4767c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b47718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4767c bytes 80e603f9
+ 00b47718 bytes 806604f9
- 00b47650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b47650 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b476ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b476ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47650 bytes 81e643f9
+ 00b476ec bytes 816644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63b1b109e296a6b7368142c6864f57a"></a>

### [`00b476ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md) → [`00b47748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47748.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b550.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b620.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b47764",
      "incomplete_value": false,
      "site": "00b47768",
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
      "definition_site": "00b476c8",
      "incomplete_value": false,
      "site": "00b476cc",
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
      "definition_site": "00b47774",
      "incomplete_value": true,
      "site": "00b47780",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b476d8",
      "incomplete_value": true,
      "site": "00b476e4",
      "value": [
        "LOAD",
        "8",
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
      "00b47764",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b47774",
      "DATA",
      [
        "storage",
        "011257d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47764",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b47774",
      "DATA",
      [
        "storage",
        "011258d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b476cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476cc) · [`00b476c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476c8) · [`00b476d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476ac.md#insn-00b476d4)
- 新版 `00b47768`（命令位置の公開資料なし） · `00b47764`（命令位置の公開資料なし） · `00b47770`（命令位置の公開資料なし）

~~~diff
- 00b476cc ["INT_ADD", "register:40f0:8", ["const:b476cc:8", "const:4:8"]]
- 00b476cc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b47768 ["INT_ADD", "register:40f0:8", ["const:b47768:8", "const:4:8"]]
+ 00b47768 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b476cc bytes 4d4e0494
+ 00b47768 bytes 5a4e0494
- 00b476c8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b476c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b476c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b476c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47764 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b47764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b476c8 bytes 009c0d91
+ 00b47764 bytes 002c0c91
- 00b476d4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00b476d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b476d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b476d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47770 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00b47770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b476d4 bytes 08611f91
+ 00b47770 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c0ae2699e96682fcd6c342f6dbd989"></a>

### [`00b476e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md) → [`00b47784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47784.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b477c4",
      "incomplete_value": true,
      "site": "00b477c4",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47728",
      "incomplete_value": true,
      "site": "00b47728",
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
            "const:7c8:8"
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
      "definition_site": "00b477a0",
      "incomplete_value": true,
      "site": "00b477a0",
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
      "definition_site": "00b47704",
      "incomplete_value": true,
      "site": "00b47704",
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
      "definition_site": "00b477a8",
      "incomplete_value": false,
      "site": "00b477bc",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4770c",
      "incomplete_value": false,
      "site": "00b47720",
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
            "const:5d1:8"
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
      "00b47798",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477a8",
      "PARAM",
      [
        "storage",
        "002be5d1",
        null,
        "string"
      ]
    ],
    [
      "00b477c4",
      "WRITE",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47798",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477a8",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b477c4",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b47720) · [`00b47728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b47728) · [`00b476fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b476e8.md#insn-00b476fc)
- 新版 `00b477bc`（命令位置の公開資料なし） · `00b477c4`（命令位置の公開資料なし） · `00b47798`（命令位置の公開資料なし）

~~~diff
- 00b47720 ["INT_ADD", "register:40f0:8", ["const:b47720:8", "const:4:8"]]
- 00b47720 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b477bc ["INT_ADD", "register:40f0:8", ["const:b477bc:8", "const:4:8"]]
+ 00b477bc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47720 bytes fc4d0494
+ 00b477bc bytes 094e0494
- 00b47728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b47728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b477c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b477c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47728 bytes 80e603f9
+ 00b477c4 bytes 806604f9
- 00b476fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b476fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00b47798 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b476fc bytes 81e643f9
+ 00b47798 bytes 816644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d68742fb47ebfa207f27917f4b2ba575"></a>

### [`00b47758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md) → [`00b477f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b477f4.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b47810",
      "incomplete_value": false,
      "site": "00b47814",
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
      "definition_site": "00b47774",
      "incomplete_value": false,
      "site": "00b47778",
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
      "definition_site": "00b47820",
      "incomplete_value": true,
      "site": "00b4782c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47784",
      "incomplete_value": true,
      "site": "00b47790",
      "value": [
        "LOAD",
        "8",
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
      "00b47810",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b47820",
      "DATA",
      [
        "storage",
        "01125828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47810",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b47820",
      "DATA",
      [
        "storage",
        "01125928",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47778) · [`00b47774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47774) · [`00b47780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47758.md#insn-00b47780)
- 新版 `00b47814`（命令位置の公開資料なし） · `00b47810`（命令位置の公開資料なし） · `00b4781c`（命令位置の公開資料なし）

~~~diff
- 00b47778 ["INT_ADD", "register:40f0:8", ["const:b47778:8", "const:4:8"]]
- 00b47778 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b47814 ["INT_ADD", "register:40f0:8", ["const:b47814:8", "const:4:8"]]
+ 00b47814 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b47778 bytes 224e0494
+ 00b47814 bytes 2f4e0494
- 00b47774 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b47774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47810 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b47810 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47810 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47810 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47774 bytes 00781491
+ 00b47810 bytes 00341591
- 00b47780 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00b47780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4781c ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00b4781c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4781c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4781c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47780 bytes 08a12091
+ 00b4781c bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-092d6b9c30598d5d327c9623afee9d82"></a>

### [`00b47794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md) → [`00b47830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47830.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b4785c",
      "incomplete_value": true,
      "site": "00b4785c",
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
    "old": {
      "definition_site": "00b477c0",
      "incomplete_value": true,
      "site": "00b477c0",
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
            "const:830:8"
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
      "definition_site": "00b47844",
      "incomplete_value": true,
      "site": "00b47844",
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
      "definition_site": "00b477a8",
      "incomplete_value": true,
      "site": "00b477a8",
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
      "definition_site": "00b47850",
      "incomplete_value": false,
      "site": "00b47854",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477b4",
      "incomplete_value": false,
      "site": "00b477b8",
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
            "const:114:8"
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
      "00b47840",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47850",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b4785c",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47840",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47850",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b4785c",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b477b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477b8) · [`00b477c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477c0) · [`00b477a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47794.md#insn-00b477a4)
- 新版 `00b47854`（命令位置の公開資料なし） · `00b4785c`（命令位置の公開資料なし） · `00b47840`（命令位置の公開資料なし）

~~~diff
- 00b477b8 ["INT_ADD", "register:40f0:8", ["const:b477b8:8", "const:4:8"]]
- 00b477b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47854 ["INT_ADD", "register:40f0:8", ["const:b47854:8", "const:4:8"]]
+ 00b47854 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b477b8 bytes d64d0494
+ 00b47854 bytes e34d0494
- 00b477c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b477c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4785c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b4785c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b477c0 bytes 601a04f9
+ 00b4785c bytes 609a04f9
- 00b477a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b477a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b47840 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b477a4 bytes 681a44f9
+ 00b47840 bytes 689a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff481dda3f6c0b36caadc6d2a5c91943"></a>

### [`00b477d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md) → [`00b47870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47870.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4789c",
      "incomplete_value": true,
      "site": "00b4789c",
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
    "old": {
      "definition_site": "00b47800",
      "incomplete_value": true,
      "site": "00b47800",
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
            "const:830:8"
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
      "definition_site": "00b47884",
      "incomplete_value": true,
      "site": "00b47884",
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
      "definition_site": "00b477e8",
      "incomplete_value": true,
      "site": "00b477e8",
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
      "definition_site": "00b4788c",
      "incomplete_value": false,
      "site": "00b47894",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477f0",
      "incomplete_value": false,
      "site": "00b477f8",
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
            "const:114:8"
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
      "00b47880",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4788c",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b4789c",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47880",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4788c",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b4789c",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b477f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b477f8) · [`00b47800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b47800) · [`00b477e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b477d4.md#insn-00b477e4)
- 新版 `00b47894`（命令位置の公開資料なし） · `00b4789c`（命令位置の公開資料なし） · `00b47880`（命令位置の公開資料なし）

~~~diff
- 00b477f8 ["INT_ADD", "register:40f0:8", ["const:b477f8:8", "const:4:8"]]
- 00b477f8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47894 ["INT_ADD", "register:40f0:8", ["const:b47894:8", "const:4:8"]]
+ 00b47894 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b477f8 bytes c64d0494
+ 00b47894 bytes d34d0494
- 00b47800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b47800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4789c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b4789c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47800 bytes 601a04f9
+ 00b4789c bytes 609a04f9
- 00b477e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b477e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b47880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b477e4 bytes 681a44f9
+ 00b47880 bytes 689a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0da6f95cc221753f15d9cae89b60644"></a>

### [`00b47814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md) → [`00b478b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478b0.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b478e0",
      "incomplete_value": true,
      "site": "00b478e0",
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
    "old": {
      "definition_site": "00b47844",
      "incomplete_value": true,
      "site": "00b47844",
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
            "const:830:8"
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
      "definition_site": "00b478c4",
      "incomplete_value": true,
      "site": "00b478c4",
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
      "definition_site": "00b47828",
      "incomplete_value": true,
      "site": "00b47828",
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
      "definition_site": "00b478d0",
      "incomplete_value": false,
      "site": "00b478d8",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47834",
      "incomplete_value": false,
      "site": "00b4783c",
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
            "const:114:8"
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
      "00b478c0",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478d0",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b478e0",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b478c0",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478d0",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b478e0",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4783c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b4783c) · [`00b47844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b47844) · [`00b47824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47814.md#insn-00b47824)
- 新版 `00b478d8`（命令位置の公開資料なし） · `00b478e0`（命令位置の公開資料なし） · `00b478c0`（命令位置の公開資料なし）

~~~diff
- 00b4783c ["INT_ADD", "register:40f0:8", ["const:b4783c:8", "const:4:8"]]
- 00b4783c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b478d8 ["INT_ADD", "register:40f0:8", ["const:b478d8:8", "const:4:8"]]
+ 00b478d8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4783c bytes b54d0494
+ 00b478d8 bytes c24d0494
- 00b47844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b47844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b478e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b478e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47844 bytes 601a04f9
+ 00b478e0 bytes 609a04f9
- 00b47824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b47824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b478c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b478c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47824 bytes 681a44f9
+ 00b478c0 bytes 689a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e112b9f5de0788982569bd16d1aad83"></a>

### [`00b47858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md) → [`00b478f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478f4.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47924",
      "incomplete_value": true,
      "site": "00b47924",
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
    "old": {
      "definition_site": "00b47888",
      "incomplete_value": true,
      "site": "00b47888",
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
            "const:830:8"
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
      "definition_site": "00b47908",
      "incomplete_value": true,
      "site": "00b47908",
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
      "definition_site": "00b4786c",
      "incomplete_value": true,
      "site": "00b4786c",
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
      "definition_site": "00b47910",
      "incomplete_value": false,
      "site": "00b4791c",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47874",
      "incomplete_value": false,
      "site": "00b47880",
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
            "const:114:8"
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
      "00b47904",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47910",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47924",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47904",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47910",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b47924",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47880) · [`00b47888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47888) · [`00b47868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47858.md#insn-00b47868)
- 新版 `00b4791c`（命令位置の公開資料なし） · `00b47924`（命令位置の公開資料なし） · `00b47904`（命令位置の公開資料なし）

~~~diff
- 00b47880 ["INT_ADD", "register:40f0:8", ["const:b47880:8", "const:4:8"]]
- 00b47880 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4791c ["INT_ADD", "register:40f0:8", ["const:b4791c:8", "const:4:8"]]
+ 00b4791c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47880 bytes a44d0494
+ 00b4791c bytes b14d0494
- 00b47888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b47888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b47924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47888 bytes 601a04f9
+ 00b47924 bytes 609a04f9
- 00b47868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00b47868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00b47904 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47868 bytes 681a44f9
+ 00b47904 bytes 689a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c580fe8b39aff20a169810ece2cce00a"></a>

### [`00b478a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md) → [`00b47944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47944.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b479cc",
      "incomplete_value": true,
      "site": "00b479cc",
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
    "old": {
      "definition_site": "00b47930",
      "incomplete_value": true,
      "site": "00b47930",
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
            "const:838:8"
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
      "definition_site": "00b47978",
      "incomplete_value": true,
      "site": "00b47984",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00b478dc",
      "incomplete_value": true,
      "site": "00b478e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "00b47958",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47978",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479cc",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47958",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47978",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479cc",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b478e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b478e8) · [`00b47930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b47930) · [`00b478bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b478a8.md#insn-00b478bc)
- 新版 `00b47984`（命令位置の公開資料なし） · `00b479cc`（命令位置の公開資料なし） · `00b47958`（命令位置の公開資料なし）

~~~diff
- 00b478e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b478e8 ["INT_ADD", "register:40f0:8", ["const:b478e8:8", "const:4:8"]]
- 00b478e8 ["CALLIND", null, ["register:0:8"]]
+ 00b47984 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47984 ["INT_ADD", "register:40f0:8", ["const:b47984:8", "const:4:8"]]
+ 00b47984 ["CALLIND", null, ["register:0:8"]]
- 00b478e8 bytes 00013fd6
+ 00b47984 bytes 00013fd6
- 00b47930 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47930 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
- 00b47930 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b479cc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b479cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:938:8"]]
+ 00b479cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47930 bytes a0e22039
+ 00b479cc bytes a0e22439
- 00b478bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
- 00b478bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b478bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b47958 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:938:8"]]
+ 00b47958 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b47958 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b478bc bytes a8e26039
+ 00b47958 bytes a8e26439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8887fb45e42ae464fc12803667ef762"></a>

### [`00b47944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md) → [`00b479e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b479e0.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b47a1c",
      "incomplete_value": true,
      "site": "00b47a1c",
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
    "old": {
      "definition_site": "00b47980",
      "incomplete_value": true,
      "site": "00b47980",
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
            "const:838:8"
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
      "definition_site": "00b47a6c",
      "incomplete_value": true,
      "site": "00b47a6c",
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
    "old": {
      "definition_site": "00b479d0",
      "incomplete_value": true,
      "site": "00b479d0",
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
            "const:830:8"
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
      "definition_site": "00b479f8",
      "incomplete_value": true,
      "site": "00b479f8",
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
      "definition_site": "00b4795c",
      "incomplete_value": true,
      "site": "00b4795c",
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
      "00b479f4",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a00",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47a1c",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b479f4",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a00",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47a1c",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b47980) · [`00b479cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b479cc) · [`00b479d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47944.md#insn-00b479d0)
- 新版 `00b47a1c`（命令位置の公開資料なし） · `00b47a68`（命令位置の公開資料なし） · `00b47a6c`（命令位置の公開資料なし）

~~~diff
- 00b47980 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47980 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47980 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
- 00b47980 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47a1c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47a1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47a1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:938:8"]]
+ 00b47a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47980 bytes bfe22039
+ 00b47a1c bytes bfe22439
- 00b479cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b479cc ["INT_ADD", "register:40f0:8", ["const:b479cc:8", "const:4:8"]]
- 00b479cc ["CALLIND", null, ["register:0:8"]]
+ 00b47a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47a68 ["INT_ADD", "register:40f0:8", ["const:b47a68:8", "const:4:8"]]
+ 00b47a68 ["CALLIND", null, ["register:0:8"]]
- 00b479cc bytes 00013fd6
+ 00b47a68 bytes 00013fd6
- 00b479d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b479d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b479d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47a6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00b47a6c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b479d0 bytes 9f1a04f9
+ 00b47a6c bytes 9f9a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89955793ca906594d6e571aa83a1f3ec"></a>

### [`00b479e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md) → [`00b47a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47a80.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47ac0",
      "incomplete_value": true,
      "site": "00b47ac0",
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
    "old": {
      "definition_site": "00b47a24",
      "incomplete_value": true,
      "site": "00b47a24",
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
            "const:830:8"
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
      "definition_site": "00b47a9c",
      "incomplete_value": true,
      "site": "00b47a9c",
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
      "definition_site": "00b47a00",
      "incomplete_value": true,
      "site": "00b47a00",
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
      "definition_site": "00b47aa4",
      "incomplete_value": false,
      "site": "00b47ab8",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a08",
      "incomplete_value": false,
      "site": "00b47a1c",
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
            "const:114:8"
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
      "00b47a94",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47aa4",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47ac0",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47a94",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47aa4",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b47ac0",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b47a1c) · [`00b47a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b47a24) · [`00b479f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b479e4.md#insn-00b479f8)
- 新版 `00b47ab8`（命令位置の公開資料なし） · `00b47ac0`（命令位置の公開資料なし） · `00b47a94`（命令位置の公開資料なし）

~~~diff
- 00b47a1c ["INT_ADD", "register:40f0:8", ["const:b47a1c:8", "const:4:8"]]
- 00b47a1c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47ab8 ["INT_ADD", "register:40f0:8", ["const:b47ab8:8", "const:4:8"]]
+ 00b47ab8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47a1c bytes 3d4d0494
+ 00b47ab8 bytes 4a4d0494
- 00b47a24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b47a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00b47ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47a24 bytes 801a04f9
+ 00b47ac0 bytes 809a04f9
- 00b479f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b479f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00b47a94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b479f8 bytes 811a44f9
+ 00b47a94 bytes 819a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9848236d5a927d7294b86dc1e282f5"></a>

### [`00b47a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md) → [`00b47af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47af0.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aeb0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af80.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b47b0c",
      "incomplete_value": false,
      "site": "00b47b10",
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
      "definition_site": "00b47a70",
      "incomplete_value": false,
      "site": "00b47a74",
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
      "definition_site": "00b47b1c",
      "incomplete_value": true,
      "site": "00b47b28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b47a80",
      "incomplete_value": true,
      "site": "00b47a8c",
      "value": [
        "LOAD",
        "8",
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
      "00b47b0c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b47b1c",
      "DATA",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47b0c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b47b1c",
      "DATA",
      [
        "storage",
        "01125940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a74) · [`00b47a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a70) · [`00b47a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a54.md#insn-00b47a7c)
- 新版 `00b47b10`（命令位置の公開資料なし） · `00b47b0c`（命令位置の公開資料なし） · `00b47b18`（命令位置の公開資料なし）

~~~diff
- 00b47a74 ["INT_ADD", "register:40f0:8", ["const:b47a74:8", "const:4:8"]]
- 00b47a74 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b47b10 ["INT_ADD", "register:40f0:8", ["const:b47b10:8", "const:4:8"]]
+ 00b47b10 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b47a74 bytes 634d0494
+ 00b47b10 bytes 704d0494
- 00b47a70 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b47a70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47a70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47a70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47b0c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b47b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47a70 bytes 009c0d91
+ 00b47b0c bytes 002c0c91
- 00b47a7c ["COPY", "tmp:0:8", ["const:840:8"]]
- 00b47a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b47a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b47a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b47b18 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00b47b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b47b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b47a7c bytes 08012191
+ 00b47b18 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eadc6410bebe4fc961592a3b5f2ca88"></a>

### [`00b47a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md) → [`00b47b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b2c.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47b6c",
      "incomplete_value": true,
      "site": "00b47b6c",
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
    "old": {
      "definition_site": "00b47ad0",
      "incomplete_value": true,
      "site": "00b47ad0",
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
            "const:830:8"
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
      "definition_site": "00b47b48",
      "incomplete_value": true,
      "site": "00b47b48",
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
      "definition_site": "00b47aac",
      "incomplete_value": true,
      "site": "00b47aac",
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
      "definition_site": "00b47b50",
      "incomplete_value": false,
      "site": "00b47b64",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ab4",
      "incomplete_value": false,
      "site": "00b47ac8",
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
            "const:114:8"
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
      "00b47b40",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b50",
      "PARAM",
      [
        "storage",
        "002a7114",
        null,
        "string"
      ]
    ],
    [
      "00b47b6c",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47b40",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b50",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b47b6c",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47ac8) · [`00b47ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47ad0) · [`00b47aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47a90.md#insn-00b47aa4)
- 新版 `00b47b64`（命令位置の公開資料なし） · `00b47b6c`（命令位置の公開資料なし） · `00b47b40`（命令位置の公開資料なし）

~~~diff
- 00b47ac8 ["INT_ADD", "register:40f0:8", ["const:b47ac8:8", "const:4:8"]]
- 00b47ac8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47b64 ["INT_ADD", "register:40f0:8", ["const:b47b64:8", "const:4:8"]]
+ 00b47b64 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47ac8 bytes 124d0494
+ 00b47b64 bytes 1f4d0494
- 00b47ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b47ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00b47b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ad0 bytes 801a04f9
+ 00b47b6c bytes 809a04f9
- 00b47aa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00b47aa4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00b47b40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47aa4 bytes 811a44f9
+ 00b47b40 bytes 819a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2a585f470c6011a12b6c7580ff0c71"></a>

### [`00b47b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b3c.md) → [`00b47bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47bd8.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00b47b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47c04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47bec",
      "incomplete_value": true,
      "site": "00b47bec",
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
      "definition_site": "00b47b50",
      "incomplete_value": true,
      "site": "00b47b50",
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
      "00b47be8",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b47b6c"
      ]
    ],
    [
      "unmatched:00b47b5c",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47be8",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47c08"
      ]
    ],
    [
      "00b47bf8",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b3c.md#insn-00b47b60) · [`00b47b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b3c.md#insn-00b47b68) · [`00b47b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b3c.md#insn-00b47b78)

~~~diff
- 00b47b60 ["INT_ADD", "register:40f0:8", ["const:b47b60:8", "const:4:8"]]
- 00b47b60 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47b60 bytes ec4c0494
- 00b47b68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47b68 bytes 603204f9
- 00b47b78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b47b78 ["RETURN", null, ["register:0:8"]]
- 00b47b78 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba8b2b73ea86b6f76cfde01c9453f968"></a>

### [`00b47b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md) → [`00b47c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c18.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b47c44",
      "incomplete_value": true,
      "site": "00b47c44",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ba8",
      "incomplete_value": true,
      "site": "00b47ba8",
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
            "const:860:8"
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
      "definition_site": "00b47c2c",
      "incomplete_value": true,
      "site": "00b47c2c",
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
      "definition_site": "00b47b90",
      "incomplete_value": true,
      "site": "00b47b90",
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
      "definition_site": "00b47c34",
      "incomplete_value": false,
      "site": "00b47c3c",
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
            "const:76a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b98",
      "incomplete_value": false,
      "site": "00b47ba0",
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
            "const:7be:8"
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
      "00b47c28",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c34",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47c44",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47c28",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c34",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b47c44",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47ba0) · [`00b47ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47ba8) · [`00b47b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47b7c.md#insn-00b47b8c)
- 新版 `00b47c3c`（命令位置の公開資料なし） · `00b47c44`（命令位置の公開資料なし） · `00b47c28`（命令位置の公開資料なし）

~~~diff
- 00b47ba0 ["INT_ADD", "register:40f0:8", ["const:b47ba0:8", "const:4:8"]]
- 00b47ba0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47c3c ["INT_ADD", "register:40f0:8", ["const:b47c3c:8", "const:4:8"]]
+ 00b47c3c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47ba0 bytes dc4c0494
+ 00b47c3c bytes e94c0494
- 00b47ba8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ba8 bytes 603204f9
+ 00b47c44 bytes 60b204f9
- 00b47b8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47b8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47c28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47c28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47b8c bytes 683244f9
+ 00b47c28 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d960ada6b0fee7e157183c6205643dd"></a>

### [`00b47bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md) → [`00b47c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c58.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b47c88",
      "incomplete_value": true,
      "site": "00b47c88",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47bec",
      "incomplete_value": true,
      "site": "00b47bec",
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
            "const:860:8"
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
      "definition_site": "00b47c6c",
      "incomplete_value": true,
      "site": "00b47c6c",
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
      "definition_site": "00b47bd0",
      "incomplete_value": true,
      "site": "00b47bd0",
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
      "definition_site": "00b47c78",
      "incomplete_value": false,
      "site": "00b47c80",
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
            "const:76a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47bdc",
      "incomplete_value": false,
      "site": "00b47be4",
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
            "const:7be:8"
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
      "00b47c68",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c78",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47c88",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47c68",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c78",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b47c88",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47be4) · [`00b47bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47bec) · [`00b47bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47bbc.md#insn-00b47bcc)
- 新版 `00b47c80`（命令位置の公開資料なし） · `00b47c88`（命令位置の公開資料なし） · `00b47c68`（命令位置の公開資料なし）

~~~diff
- 00b47be4 ["INT_ADD", "register:40f0:8", ["const:b47be4:8", "const:4:8"]]
- 00b47be4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47c80 ["INT_ADD", "register:40f0:8", ["const:b47c80:8", "const:4:8"]]
+ 00b47c80 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47be4 bytes cb4c0494
+ 00b47c80 bytes d84c0494
- 00b47bec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47bec bytes 603204f9
+ 00b47c88 bytes 60b204f9
- 00b47bcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47bcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47bcc bytes 683244f9
+ 00b47c68 bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa2b609719b40b89444cd15a31282c0"></a>

### [`00b47c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md) → [`00b47c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c9c.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47ccc",
      "incomplete_value": true,
      "site": "00b47ccc",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c30",
      "incomplete_value": true,
      "site": "00b47c30",
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
            "const:860:8"
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
      "definition_site": "00b47cb0",
      "incomplete_value": true,
      "site": "00b47cb0",
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
      "definition_site": "00b47c14",
      "incomplete_value": true,
      "site": "00b47c14",
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
      "definition_site": "00b47cb8",
      "incomplete_value": false,
      "site": "00b47cc4",
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
            "const:76a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c1c",
      "incomplete_value": false,
      "site": "00b47c28",
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
            "const:7be:8"
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
      "00b47cac",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47cb8",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47ccc",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47cac",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47cb8",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b47ccc",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c28) · [`00b47c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c30) · [`00b47c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c00.md#insn-00b47c10)
- 新版 `00b47cc4`（命令位置の公開資料なし） · `00b47ccc`（命令位置の公開資料なし） · `00b47cac`（命令位置の公開資料なし）

~~~diff
- 00b47c28 ["INT_ADD", "register:40f0:8", ["const:b47c28:8", "const:4:8"]]
- 00b47c28 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47cc4 ["INT_ADD", "register:40f0:8", ["const:b47cc4:8", "const:4:8"]]
+ 00b47cc4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47c28 bytes ba4c0494
+ 00b47cc4 bytes c74c0494
- 00b47c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47c30 bytes 603204f9
+ 00b47ccc bytes 60b204f9
- 00b47c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b47c10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00b47cac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47c10 bytes 683244f9
+ 00b47cac bytes 68b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c692072ca7f9143421fb532ca507167e"></a>

### [`00b47c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md) → [`00b47cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47cec.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47d74",
      "incomplete_value": true,
      "site": "00b47d74",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47cd8",
      "incomplete_value": true,
      "site": "00b47cd8",
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
            "const:868:8"
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
      "site": "00b47c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47ccc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47d00",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b47c84",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d74",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47d00",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47d20",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d74",
      "WRITE",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md#insn-00b47c90) · [`00b47ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md#insn-00b47ccc) · [`00b47cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47c50.md#insn-00b47cd8)
- 新版 `00b47d74`（命令位置の公開資料なし）

~~~diff
- 00b47c90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47c90 ["INT_ADD", "register:40f0:8", ["const:b47c90:8", "const:4:8"]]
- 00b47c90 ["CALLIND", null, ["register:0:8"]]
- 00b47c90 bytes 00013fd6
- 00b47ccc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47ccc ["INT_ADD", "register:40f0:8", ["const:b47ccc:8", "const:4:8"]]
- 00b47ccc ["CALLIND", null, ["register:0:8"]]
- 00b47ccc bytes 00013fd6
- 00b47cd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47cd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:868:8"]]
- 00b47cd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47d74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47d74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:968:8"]]
+ 00b47d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47cd8 bytes a0a22139
+ 00b47d74 bytes a0a22539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ae1e965ace555510f3d5a6390c09817"></a>

### [`00b47cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md) → [`00b47d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47d88.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47dc4",
      "incomplete_value": true,
      "site": "00b47dc4",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47d28",
      "incomplete_value": true,
      "site": "00b47d28",
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
            "const:868:8"
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
      "site": "00b47d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47e14"
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
      "00b47d9c",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47d04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e18"
      ]
    ],
    [
      "00b47da8",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47d9c",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e18"
      ]
    ],
    [
      "00b47da8",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md#insn-00b47d04) · [`00b47d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md#insn-00b47d28) · [`00b47d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47cec.md#insn-00b47d50)
- 新版 `00b47dc4`（命令位置の公開資料なし）

~~~diff
- 00b47d04 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b47d04 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b47d04 bytes c10300b4
- 00b47d28 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47d28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47d28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:868:8"]]
- 00b47d28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47dc4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47dc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47dc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
+ 00b47dc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47d28 bytes bfa22139
+ 00b47dc4 bytes bfa22539
- 00b47d50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47d50 ["INT_ADD", "register:40f0:8", ["const:b47d50:8", "const:4:8"]]
- 00b47d50 ["CALLIND", null, ["register:0:8"]]
- 00b47d50 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4bb3d06776c70ffbb3db954373f99d"></a>

### [`00b47d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md) → [`00b47e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e28.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00b47dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47e68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47da8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47da0",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47da8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e6c"
      ]
    ],
    [
      "unmatched:00b47db0",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47e3c",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47e44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e6c"
      ]
    ],
    [
      "00b47e4c",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md#insn-00b47da8) · [`00b47dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md#insn-00b47dc4) · [`00b47dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47d8c.md#insn-00b47dcc)
- 新版 `00b47e60`（命令位置の公開資料なし）

~~~diff
- 00b47da8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b47da8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b47da8 bytes 410100b5
- 00b47dc4 ["INT_ADD", "register:40f0:8", ["const:b47dc4:8", "const:4:8"]]
- 00b47dc4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47e60 ["INT_ADD", "register:40f0:8", ["const:b47e60:8", "const:4:8"]]
+ 00b47e60 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47dc4 bytes 534c0494
+ 00b47e60 bytes 604c0494
- 00b47dcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b47dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47dcc bytes 803204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-991eab230912c63be12b092d79539d52"></a>

### [`00b47e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md) → [`00b47ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47ed4.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47f14",
      "incomplete_value": true,
      "site": "00b47f14",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e78",
      "incomplete_value": true,
      "site": "00b47e78",
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
            "const:860:8"
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
      "definition_site": "00b47ef0",
      "incomplete_value": true,
      "site": "00b47ef0",
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
      "definition_site": "00b47e54",
      "incomplete_value": true,
      "site": "00b47e54",
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
      "definition_site": "00b47ef8",
      "incomplete_value": false,
      "site": "00b47f0c",
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
            "const:76a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e5c",
      "incomplete_value": false,
      "site": "00b47e70",
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
            "const:7be:8"
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
      "00b47ee8",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ef8",
      "PARAM",
      [
        "storage",
        "002bf7be",
        null,
        "string"
      ]
    ],
    [
      "00b47f14",
      "WRITE",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47ee8",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ef8",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b47f14",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e70) · [`00b47e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e78) · [`00b47e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47e38.md#insn-00b47e4c)
- 新版 `00b47f0c`（命令位置の公開資料なし） · `00b47f14`（命令位置の公開資料なし） · `00b47ee8`（命令位置の公開資料なし）

~~~diff
- 00b47e70 ["INT_ADD", "register:40f0:8", ["const:b47e70:8", "const:4:8"]]
- 00b47e70 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47f0c ["INT_ADD", "register:40f0:8", ["const:b47f0c:8", "const:4:8"]]
+ 00b47f0c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47e70 bytes 284c0494
+ 00b47f0c bytes 354c0494
- 00b47e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b47e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b47f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47e78 bytes 803204f9
+ 00b47f14 bytes 80b204f9
- 00b47e4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b47e4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00b47ee8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47e4c bytes 813244f9
+ 00b47ee8 bytes 81b244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ac22296afa3ef2d470aac56a587783"></a>

### [`00b47ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ee4.md) → [`00b47f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f80.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b47f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47fac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47f94",
      "incomplete_value": true,
      "site": "00b47f94",
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
      "definition_site": "00b47ef8",
      "incomplete_value": true,
      "site": "00b47ef8",
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
      "00b47f90",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47f04",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b47f08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b47f90",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fa0",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b47fa4",
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

- 旧版 [`00b47ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ee4.md#insn-00b47ef8) · [`00b47f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ee4.md#insn-00b47f08) · [`00b47f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ee4.md#insn-00b47f10)
- 新版 `00b47f94`（命令位置の公開資料なし）

~~~diff
- 00b47ef8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b47ef8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47f94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47f94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b47ef8 bytes e80000b5
+ 00b47f94 bytes e80000b5
- 00b47f08 ["INT_ADD", "register:40f0:8", ["const:b47f08:8", "const:4:8"]]
- 00b47f08 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47f08 bytes 024c0494
- 00b47f10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47f10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f10 bytes 604204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88d51c93a1780d76498c33db4554a37"></a>

### [`00b47f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md) → [`00b47fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47fc0.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00b47fec",
      "incomplete_value": true,
      "site": "00b47fec",
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
    "old": {
      "definition_site": "00b47f50",
      "incomplete_value": true,
      "site": "00b47f50",
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
            "const:880:8"
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
      "definition_site": "00b47fd4",
      "incomplete_value": true,
      "site": "00b47fd4",
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
      "definition_site": "00b47f38",
      "incomplete_value": true,
      "site": "00b47f38",
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
      "definition_site": "00b47fdc",
      "incomplete_value": false,
      "site": "00b47fe4",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47f40",
      "incomplete_value": false,
      "site": "00b47f48",
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
            "const:3fc:8"
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
      "00b47fd0",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fdc",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b47fec",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47fd0",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fdc",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b47fec",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f48) · [`00b47f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f50) · [`00b47f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f24.md#insn-00b47f34)
- 新版 `00b47fe4`（命令位置の公開資料なし） · `00b47fec`（命令位置の公開資料なし） · `00b47fd0`（命令位置の公開資料なし）

~~~diff
- 00b47f48 ["INT_ADD", "register:40f0:8", ["const:b47f48:8", "const:4:8"]]
- 00b47f48 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b47fe4 ["INT_ADD", "register:40f0:8", ["const:b47fe4:8", "const:4:8"]]
+ 00b47fe4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47f48 bytes f24b0494
+ 00b47fe4 bytes ff4b0494
- 00b47f50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47fec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b47fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f50 bytes 604204f9
+ 00b47fec bytes 60c204f9
- 00b47f34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47fd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b47fd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47f34 bytes 684244f9
+ 00b47fd0 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976e78b2d445be377301261c031da8a5"></a>

### [`00b47f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md) → [`00b48000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48000.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48030",
      "incomplete_value": true,
      "site": "00b48030",
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
    "old": {
      "definition_site": "00b47f94",
      "incomplete_value": true,
      "site": "00b47f94",
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
            "const:880:8"
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
      "definition_site": "00b48014",
      "incomplete_value": true,
      "site": "00b48014",
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
      "definition_site": "00b47f78",
      "incomplete_value": true,
      "site": "00b47f78",
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
      "definition_site": "00b48020",
      "incomplete_value": false,
      "site": "00b48028",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47f84",
      "incomplete_value": false,
      "site": "00b47f8c",
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
            "const:3fc:8"
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
      "00b48010",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48020",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b48030",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48010",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48020",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b48030",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f8c) · [`00b47f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f94) · [`00b47f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47f64.md#insn-00b47f74)
- 新版 `00b48028`（命令位置の公開資料なし） · `00b48030`（命令位置の公開資料なし） · `00b48010`（命令位置の公開資料なし）

~~~diff
- 00b47f8c ["INT_ADD", "register:40f0:8", ["const:b47f8c:8", "const:4:8"]]
- 00b47f8c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48028 ["INT_ADD", "register:40f0:8", ["const:b48028:8", "const:4:8"]]
+ 00b48028 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47f8c bytes e14b0494
+ 00b48028 bytes ee4b0494
- 00b47f94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b48030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f94 bytes 604204f9
+ 00b48030 bytes 60c204f9
- 00b47f74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47f74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b48010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47f74 bytes 684244f9
+ 00b48010 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc9aed5fcedad7cf0400f35a1a843aa"></a>

### [`00b47fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md) → [`00b48044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48044.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48074",
      "incomplete_value": true,
      "site": "00b48074",
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
    "old": {
      "definition_site": "00b47fd8",
      "incomplete_value": true,
      "site": "00b47fd8",
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
            "const:880:8"
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
      "definition_site": "00b48058",
      "incomplete_value": true,
      "site": "00b48058",
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
      "definition_site": "00b47fbc",
      "incomplete_value": true,
      "site": "00b47fbc",
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
      "definition_site": "00b48060",
      "incomplete_value": false,
      "site": "00b4806c",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fc4",
      "incomplete_value": false,
      "site": "00b47fd0",
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
            "const:3fc:8"
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
      "00b48054",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48060",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b48074",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48054",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48060",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b48074",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fd0) · [`00b47fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fd8) · [`00b47fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47fa8.md#insn-00b47fb8)
- 新版 `00b4806c`（命令位置の公開資料なし） · `00b48074`（命令位置の公開資料なし） · `00b48054`（命令位置の公開資料なし）

~~~diff
- 00b47fd0 ["INT_ADD", "register:40f0:8", ["const:b47fd0:8", "const:4:8"]]
- 00b47fd0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4806c ["INT_ADD", "register:40f0:8", ["const:b4806c:8", "const:4:8"]]
+ 00b4806c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b47fd0 bytes d04b0494
+ 00b4806c bytes dd4b0494
- 00b47fd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b48074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47fd8 bytes 604204f9
+ 00b48074 bytes 60c204f9
- 00b47fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b47fb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
+ 00b48054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47fb8 bytes 684244f9
+ 00b48054 bytes 68c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758720bcf2e0c693112c5987231d17cd"></a>

### [`00b47ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md) → [`00b48094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48094.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4811c",
      "incomplete_value": true,
      "site": "00b4811c",
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
    "old": {
      "definition_site": "00b48080",
      "incomplete_value": true,
      "site": "00b48080",
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
            "const:888:8"
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
      "definition_site": "00b480c8",
      "incomplete_value": true,
      "site": "00b480d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4802c",
      "incomplete_value": true,
      "site": "00b48038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b480a8",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b480c8",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4811c",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b480a8",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b480c8",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4811c",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md#insn-00b48038) · [`00b48080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md#insn-00b48080) · [`00b4800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ff8.md#insn-00b4800c)
- 新版 `00b480d4`（命令位置の公開資料なし） · `00b4811c`（命令位置の公開資料なし） · `00b480a8`（命令位置の公開資料なし）

~~~diff
- 00b48038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48038 ["INT_ADD", "register:40f0:8", ["const:b48038:8", "const:4:8"]]
- 00b48038 ["CALLIND", null, ["register:0:8"]]
+ 00b480d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b480d4 ["INT_ADD", "register:40f0:8", ["const:b480d4:8", "const:4:8"]]
+ 00b480d4 ["CALLIND", null, ["register:0:8"]]
- 00b48038 bytes 00013fd6
+ 00b480d4 bytes 00013fd6
- 00b48080 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48080 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:888:8"]]
- 00b48080 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4811c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4811c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:988:8"]]
+ 00b4811c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48080 bytes a0222239
+ 00b4811c bytes a0222639
- 00b4800c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:888:8"]]
- 00b4800c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4800c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b480a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:988:8"]]
+ 00b480a8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b480a8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4800c bytes a8226239
+ 00b480a8 bytes a8226639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b760b6fa3a7698d9ebdd28c62da0d0a0"></a>

### [`00b48094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md) → [`00b48130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48130.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4816c",
      "incomplete_value": true,
      "site": "00b4816c",
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
    "old": {
      "definition_site": "00b480d0",
      "incomplete_value": true,
      "site": "00b480d0",
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
            "const:888:8"
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
      "definition_site": "00b481bc",
      "incomplete_value": true,
      "site": "00b481bc",
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
    "old": {
      "definition_site": "00b48120",
      "incomplete_value": true,
      "site": "00b48120",
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
            "const:880:8"
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
      "definition_site": "00b48148",
      "incomplete_value": true,
      "site": "00b48148",
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
      "definition_site": "00b480ac",
      "incomplete_value": true,
      "site": "00b480ac",
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
      "00b48144",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48150",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4816c",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48144",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48150",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4816c",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b480d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b480d0) · [`00b4811c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b4811c) · [`00b48120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48094.md#insn-00b48120)
- 新版 `00b4816c`（命令位置の公開資料なし） · `00b481b8`（命令位置の公開資料なし） · `00b481bc`（命令位置の公開資料なし）

~~~diff
- 00b480d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b480d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b480d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:888:8"]]
- 00b480d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4816c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4816c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4816c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
+ 00b4816c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b480d0 bytes bf222239
+ 00b4816c bytes bf222639
- 00b4811c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4811c ["INT_ADD", "register:40f0:8", ["const:b4811c:8", "const:4:8"]]
- 00b4811c ["CALLIND", null, ["register:0:8"]]
+ 00b481b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b481b8 ["INT_ADD", "register:40f0:8", ["const:b481b8:8", "const:4:8"]]
+ 00b481b8 ["CALLIND", null, ["register:0:8"]]
- 00b4811c bytes 00013fd6
+ 00b481b8 bytes 00013fd6
- 00b48120 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b48120 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b48120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b481bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b481bc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b481bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b48120 bytes 9f4204f9
+ 00b481bc bytes 9fc204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92aba1963bc6f0da1d87b1f01587a50e"></a>

### [`00b48134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md) → [`00b481d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b481d0.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48210",
      "incomplete_value": true,
      "site": "00b48210",
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
    "old": {
      "definition_site": "00b48174",
      "incomplete_value": true,
      "site": "00b48174",
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
            "const:880:8"
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
      "definition_site": "00b481ec",
      "incomplete_value": true,
      "site": "00b481ec",
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
      "definition_site": "00b48150",
      "incomplete_value": true,
      "site": "00b48150",
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
      "definition_site": "00b481f4",
      "incomplete_value": false,
      "site": "00b48208",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48158",
      "incomplete_value": false,
      "site": "00b4816c",
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
            "const:3fc:8"
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
      "00b481e4",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b481f4",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b48210",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b481e4",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b481f4",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b48210",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4816c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b4816c) · [`00b48174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b48174) · [`00b48148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48134.md#insn-00b48148)
- 新版 `00b48208`（命令位置の公開資料なし） · `00b48210`（命令位置の公開資料なし） · `00b481e4`（命令位置の公開資料なし）

~~~diff
- 00b4816c ["INT_ADD", "register:40f0:8", ["const:b4816c:8", "const:4:8"]]
- 00b4816c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48208 ["INT_ADD", "register:40f0:8", ["const:b48208:8", "const:4:8"]]
+ 00b48208 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4816c bytes 694b0494
+ 00b48208 bytes 764b0494
- 00b48174 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b48174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b48210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48174 bytes 804204f9
+ 00b48210 bytes 80c204f9
- 00b48148 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b48148 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b481e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b481e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48148 bytes 814244f9
+ 00b481e4 bytes 81c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db58bedcdfa04c940f443859e6b0e1d"></a>

### [`00b481a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md) → [`00b48240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48240.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2c0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b390.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4825c",
      "incomplete_value": false,
      "site": "00b48260",
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
      "definition_site": "00b481c0",
      "incomplete_value": false,
      "site": "00b481c4",
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
      "definition_site": "00b4826c",
      "incomplete_value": true,
      "site": "00b48278",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b481d0",
      "incomplete_value": true,
      "site": "00b481dc",
      "value": [
        "LOAD",
        "8",
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
      "00b4825c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4826c",
      "DATA",
      [
        "storage",
        "01125890",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4825c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4826c",
      "DATA",
      [
        "storage",
        "01125990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b481c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481c4) · [`00b481c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481c0) · [`00b481cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481a4.md#insn-00b481cc)
- 新版 `00b48260`（命令位置の公開資料なし） · `00b4825c`（命令位置の公開資料なし） · `00b48268`（命令位置の公開資料なし）

~~~diff
- 00b481c4 ["INT_ADD", "register:40f0:8", ["const:b481c4:8", "const:4:8"]]
- 00b481c4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b48260 ["INT_ADD", "register:40f0:8", ["const:b48260:8", "const:4:8"]]
+ 00b48260 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b481c4 bytes 8f4b0494
+ 00b48260 bytes 9c4b0494
- 00b481c0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b481c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b481c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b481c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4825c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4825c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4825c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4825c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b481c0 bytes 009c0d91
+ 00b4825c bytes 002c0c91
- 00b481cc ["COPY", "tmp:0:8", ["const:890:8"]]
- 00b481cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b481cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b481cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b48268 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 00b48268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b481cc bytes 08412291
+ 00b48268 bytes 08412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac1dc4acd38f412531440f6c936f401"></a>

### [`00b481e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md) → [`00b4827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4827c.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b482bc",
      "incomplete_value": true,
      "site": "00b482bc",
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
    "old": {
      "definition_site": "00b48220",
      "incomplete_value": true,
      "site": "00b48220",
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
            "const:880:8"
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
      "definition_site": "00b48298",
      "incomplete_value": true,
      "site": "00b48298",
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
      "definition_site": "00b481fc",
      "incomplete_value": true,
      "site": "00b481fc",
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
      "definition_site": "00b482a0",
      "incomplete_value": false,
      "site": "00b482b4",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48204",
      "incomplete_value": false,
      "site": "00b48218",
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
            "const:3fc:8"
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
      "00b48290",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482a0",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ],
    [
      "00b482bc",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48290",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482a0",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b482bc",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b48218) · [`00b48220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b48220) · [`00b481f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b481e0.md#insn-00b481f4)
- 新版 `00b482b4`（命令位置の公開資料なし） · `00b482bc`（命令位置の公開資料なし） · `00b48290`（命令位置の公開資料なし）

~~~diff
- 00b48218 ["INT_ADD", "register:40f0:8", ["const:b48218:8", "const:4:8"]]
- 00b48218 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b482b4 ["INT_ADD", "register:40f0:8", ["const:b482b4:8", "const:4:8"]]
+ 00b482b4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48218 bytes 3e4b0494
+ 00b482b4 bytes 4b4b0494
- 00b48220 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b48220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b482bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b482bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48220 bytes 804204f9
+ 00b482bc bytes 80c204f9
- 00b481f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b481f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
+ 00b48290 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b481f4 bytes 814244f9
+ 00b48290 bytes 81c244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f21afce1da1dd95afc858f6a4dcd6d"></a>

### [`00b48250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md) → [`00b482ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b482ec.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48308",
      "incomplete_value": false,
      "site": "00b4830c",
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
      "definition_site": "00b4826c",
      "incomplete_value": false,
      "site": "00b48270",
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
      "definition_site": "00b48318",
      "incomplete_value": true,
      "site": "00b48324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4827c",
      "incomplete_value": true,
      "site": "00b48288",
      "value": [
        "LOAD",
        "8",
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
      "00b48308",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b48318",
      "DATA",
      [
        "storage",
        "011258a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48308",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b48318",
      "DATA",
      [
        "storage",
        "011259a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b48270) · [`00b4826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b4826c) · [`00b48278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48250.md#insn-00b48278)
- 新版 `00b4830c`（命令位置の公開資料なし） · `00b48308`（命令位置の公開資料なし） · `00b48314`（命令位置の公開資料なし）

~~~diff
- 00b48270 ["INT_ADD", "register:40f0:8", ["const:b48270:8", "const:4:8"]]
- 00b48270 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b4830c ["INT_ADD", "register:40f0:8", ["const:b4830c:8", "const:4:8"]]
+ 00b4830c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b48270 bytes 644b0494
+ 00b4830c bytes 714b0494
- 00b4826c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b4826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48308 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b48308 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48308 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48308 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4826c bytes 00781491
+ 00b48308 bytes 00341591
- 00b48278 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00b48278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b48314 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00b48314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48278 bytes 08812291
+ 00b48314 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598f7dc71db60c0811d12f7cbe047c6a"></a>

### [`00b4828c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md) → [`00b48328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48328.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00b482b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48354"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4833c",
      "incomplete_value": true,
      "site": "00b4833c",
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
      "definition_site": "00b482a0",
      "incomplete_value": true,
      "site": "00b482a0",
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
      "00b48338",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b482ac",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b482b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b48338",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48348",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b4834c",
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

- 旧版 [`00b482a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b482a0) · [`00b482b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b482b0) · [`00b482b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4828c.md#insn-00b482b8)
- 新版 `00b4833c`（命令位置の公開資料なし）

~~~diff
- 00b482a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b482a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4833c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4833c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b482a0 bytes e80000b5
+ 00b4833c bytes e80000b5
- 00b482b0 ["INT_ADD", "register:40f0:8", ["const:b482b0:8", "const:4:8"]]
- 00b482b0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b482b0 bytes 184b0494
- 00b482b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b482b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b482b8 bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-347de7774331321263e0cc37a7f32ec1"></a>

### [`00b482cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md) → [`00b48368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48368.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00b482f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48394"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4837c",
      "incomplete_value": true,
      "site": "00b4837c",
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
      "definition_site": "00b482e0",
      "incomplete_value": true,
      "site": "00b482e0",
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
      "00b48378",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b482e8",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b482f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b48378",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48384",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b4838c",
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

- 旧版 [`00b482e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482e0) · [`00b482f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482f0) · [`00b482f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b482cc.md#insn-00b482f8)
- 新版 `00b4837c`（命令位置の公開資料なし）

~~~diff
- 00b482e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b482e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4837c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4837c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b482e0 bytes e80000b5
+ 00b4837c bytes e80000b5
- 00b482f0 ["INT_ADD", "register:40f0:8", ["const:b482f0:8", "const:4:8"]]
- 00b482f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b482f0 bytes 084b0494
- 00b482f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b482f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b482f8 bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eab29b04a7915c9ed3c5b4debbd5b77"></a>

### [`00b4830c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md) → [`00b483a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483a8.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b4833c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b483d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b483bc",
      "incomplete_value": true,
      "site": "00b483bc",
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
      "definition_site": "00b48320",
      "incomplete_value": true,
      "site": "00b48320",
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
      "00b483b8",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4832c",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48334",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b483b8",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b483c8",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b483d0",
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

- 旧版 [`00b48320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md#insn-00b48320) · [`00b48334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md#insn-00b48334) · [`00b4833c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4830c.md#insn-00b4833c)
- 新版 `00b483bc`（命令位置の公開資料なし）

~~~diff
- 00b48320 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48320 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b483bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b483bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48320 bytes 080100b5
+ 00b483bc bytes 080100b5
- 00b48334 ["INT_ADD", "register:40f0:8", ["const:b48334:8", "const:4:8"]]
- 00b48334 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48334 bytes f74a0494
- 00b4833c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4833c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4833c bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2672d5898633c73b09a24a6db3280ccc"></a>

### [`00b48350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md) → [`00b483ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483ec.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4841c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48360",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b48364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48384"
      ]
    ],
    [
      "unmatched:00b4836c",
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
      "00b483fc",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48400",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48420"
      ]
    ],
    [
      "00b48408",
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

- 旧版 [`00b48364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md#insn-00b48364) · [`00b48378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md#insn-00b48378) · [`00b48380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48350.md#insn-00b48380)
- 新版 `00b48414`（命令位置の公開資料なし）

~~~diff
- 00b48364 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b48364 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b48364 bytes 080100b5
- 00b48378 ["INT_ADD", "register:40f0:8", ["const:b48378:8", "const:4:8"]]
- 00b48378 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b48414 ["INT_ADD", "register:40f0:8", ["const:b48414:8", "const:4:8"]]
+ 00b48414 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48378 bytes e64a0494
+ 00b48414 bytes f34a0494
- 00b48380 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b48380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48380 bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c0a40408e649635fc1c6619f8dc1c1"></a>

### [`00b483a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b483a0.md) → [`00b4843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4843c.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b483a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b483a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b483a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b483a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b483a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b483a8",
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
      "00b4843c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b48440",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48444",
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

- 旧版 [`00b483a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b483a0.md#insn-00b483a0) · [`00b483a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b483a0.md#insn-00b483a4) · [`00b483a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b483a0.md#insn-00b483a8)

~~~diff
- 00b483a0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b483a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b483a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b483a0 bytes f50f1df8
- 00b483a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b483a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b483a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b483a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b483a4 bytes f44f01a9
- 00b483a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b483a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b483a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b483a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b483a8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af443fc6a95b8fd307ff7c6e64515153"></a>

### [`00b4843c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md) → [`00b484d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b484d8.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 20.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48564",
      "incomplete_value": true,
      "site": "00b48564",
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
    "old": {
      "definition_site": "00b484c8",
      "incomplete_value": true,
      "site": "00b484c8",
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
            "const:8a8:8"
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
      "site": "00b48514"
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
      "00b484ec",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b484f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b484cc"
      ]
    ],
    [
      "00b484f8",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b484ec",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b484f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48568"
      ]
    ],
    [
      "00b484f8",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b48454) · [`00b48478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b48478) · [`00b48488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4843c.md#insn-00b48488)
- 新版 `00b484f0`（命令位置の公開資料なし）

~~~diff
- 00b48454 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b48454 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b484f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b484f0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b48454 bytes c10300b4
+ 00b484f0 bytes c10300b4
- 00b48478 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48478 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48478 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
- 00b48478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48478 bytes bfc22239
- 00b48488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48488 ["INT_ADD", "register:40f0:8", ["const:b48488:8", "const:4:8"]]
- 00b48488 ["CALLIND", null, ["register:0:8"]]
- 00b48488 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e66585688bba51d09c68a5a27b14aa4"></a>

### [`00b484dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md) → [`00b48578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48578.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b485b8",
      "incomplete_value": true,
      "site": "00b485b8",
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
    "old": {
      "definition_site": "00b4851c",
      "incomplete_value": true,
      "site": "00b4851c",
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
            "const:8a8:8"
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
      "definition_site": "00b48594",
      "incomplete_value": true,
      "site": "00b48594",
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
      "definition_site": "00b484f8",
      "incomplete_value": true,
      "site": "00b484f8",
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
      "definition_site": "00b4859c",
      "incomplete_value": false,
      "site": "00b485b0",
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
            "const:947:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48500",
      "incomplete_value": false,
      "site": "00b48514",
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
            "const:99b:8"
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
      "00b4858c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4859c",
      "PARAM",
      [
        "storage",
        "002b999b",
        null,
        "string"
      ]
    ],
    [
      "00b485b8",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4858c",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4859c",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b485b8",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md#insn-00b48514) · [`00b4851c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md#insn-00b4851c) · [`00b484f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b484dc.md#insn-00b484f0)
- 新版 `00b485b0`（命令位置の公開資料なし） · `00b485b8`（命令位置の公開資料なし） · `00b4858c`（命令位置の公開資料なし）

~~~diff
- 00b48514 ["INT_ADD", "register:40f0:8", ["const:b48514:8", "const:4:8"]]
- 00b48514 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b485b0 ["INT_ADD", "register:40f0:8", ["const:b485b0:8", "const:4:8"]]
+ 00b485b0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b48514 bytes 7f4a0494
+ 00b485b0 bytes 8c4a0494
- 00b4851c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4851c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b485b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b485b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4851c bytes 805604f9
+ 00b485b8 bytes 80d604f9
- 00b484f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b484f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4858c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00b4858c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b484f0 bytes 815644f9
+ 00b4858c bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c7f2869c600c2a1b0ff731a55d6f4ff"></a>

### [`00b4854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md) → [`00b485e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b485e8.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b48604",
      "incomplete_value": false,
      "site": "00b48608",
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
      "definition_site": "00b48568",
      "incomplete_value": false,
      "site": "00b4856c",
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
      "definition_site": "00b48614",
      "incomplete_value": true,
      "site": "00b48620",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b48578",
      "incomplete_value": true,
      "site": "00b48584",
      "value": [
        "LOAD",
        "8",
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
      "00b48604",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b48614",
      "DATA",
      [
        "storage",
        "011258b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48604",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48614",
      "DATA",
      [
        "storage",
        "011259b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4856c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md#insn-00b4856c) · [`00b48568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md#insn-00b48568) · [`00b48574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md#insn-00b48574)
- 新版 `00b48608`（命令位置の公開資料なし） · `00b48604`（命令位置の公開資料なし） · `00b48610`（命令位置の公開資料なし）

~~~diff
- 00b4856c ["INT_ADD", "register:40f0:8", ["const:b4856c:8", "const:4:8"]]
- 00b4856c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b48608 ["INT_ADD", "register:40f0:8", ["const:b48608:8", "const:4:8"]]
+ 00b48608 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4856c bytes a54a0494
+ 00b48608 bytes b24a0494
- 00b48568 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b48568 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48568 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48568 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48604 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b48604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48568 bytes 009c0d91
+ 00b48604 bytes 002c0c91
- 00b48574 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00b48574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b48574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b48574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b48610 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00b48610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b48610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b48574 bytes 08e12291
+ 00b48610 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

