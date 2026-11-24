# v15.7.4 → v16.0.0 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-b612bcbee3a785c20d89cefbb0bee582"></a>

### [`00b96538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96538.md) → [`00c12f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c12f80.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a370.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 58.82% / 新版 58.82%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9655c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c12fa4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9654c",
      "incomplete_value": true,
      "site": "00b96568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
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
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 7
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9655c",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c12fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9655c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96538.md#insn-00b9655c) · [`00b96568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96538.md#insn-00b96568)
- 新版 [`00c12fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c12f80.md#insn-00c12fb0) · [`00c12fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c12f80.md#insn-00c12fa4)

~~~diff
- 00b9655c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b9655c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9655c bytes e80700f9
- 00b96568 ["INT_ADD", "register:40f0:8", ["const:b96568:8", "const:4:8"]]
- 00b96568 ["CALL", null, ["callee:00c5a370:8"]]
+ 00c12fb0 ["INT_ADD", "register:40f0:8", ["const:c12fb0:8", "const:4:8"]]
+ 00c12fb0 ["CALL", null, ["callee:00c5a370:8"]]
- 00b96568 bytes ee1c0194
+ 00c12fb0 bytes f01c0194
+ 00c12fa4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00c12fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c12fa4 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc7562ef7f06a1ce0a0ad1b9ae80e30"></a>

### [`00b96608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md) → [`00c13050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9663c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c13090",
      "incomplete_value": true,
      "site": "00c13098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96648",
      "incomplete_value": true,
      "site": "00b96650",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c13084"
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
      "unmatched:00b9663c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c13090",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c13098",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c13084",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c13090",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c13098",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9663c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md#insn-00b9663c) · [`00b96640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md#insn-00b96640) · [`00b9665c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96608.md#insn-00b9665c)
- 新版 [`00c13088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md#insn-00c13088) · [`00c130a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md#insn-00c130a4)

~~~diff
- 00b9663c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b9663c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b9663c bytes e10b00f9
- 00b96640 ["INT_ADD", "register:40f0:8", ["const:b96640:8", "const:4:8"]]
- 00b96640 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c13088 ["INT_ADD", "register:40f0:8", ["const:c13088:8", "const:4:8"]]
+ 00c13088 ["CALL", null, ["callee:00c57e70:8"]]
- 00b96640 bytes 78130194
+ 00c13088 bytes 7a130194
- 00b9665c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c130a4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b9665c bytes 40010054
+ 00c130a4 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ecca1f7328e7329579805c63cc151d"></a>

### [`00b9681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md) → [`00c13264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.67% / 新版 93.67%

CFGの説明率　旧版 40.00% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c132a4",
      "incomplete_value": true,
      "site": "00c132ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9685c",
      "incomplete_value": true,
      "site": "00b96864",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c132b4",
      "incomplete_value": true,
      "site": "00c132b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9686c",
      "incomplete_value": true,
      "site": "00b96870",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b968b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c132a4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c132ac",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c132b0",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c132a4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c132ac",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c132b0",
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md#insn-00b96894) · [`00b968b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md#insn-00b968b4) · [`00b968bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9681c.md#insn-00b968bc)
- 新版 [`00c132dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md#insn-00c132dc)

~~~diff
- 00b96894 ["INT_ADD", "register:40f0:8", ["const:b96894:8", "const:4:8"]]
- 00b96894 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c132dc ["INT_ADD", "register:40f0:8", ["const:c132dc:8", "const:4:8"]]
+ 00c132dc ["CALL", null, ["callee:00c5dae0:8"]]
- 00b96894 bytes 93290194
+ 00c132dc bytes 012a0194
- 00b968b4 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b968b4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b968b4 bytes 170500b4
- 00b968bc ["INT_ADD", "register:40f0:8", ["const:b968bc:8", "const:4:8"]]
- 00b968bc ["CALL", null, ["ram:bdb440:8"]]
- 00b968bc bytes e1120194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39db3980532538a67c3ff915ca587421"></a>

### [`00b9696c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md) → [`00c133b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c133b4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b969a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b969ac",
      "incomplete_value": true,
      "site": "00b969c4",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b969b0",
      "incomplete_value": true,
      "site": "00b969c4",
      "value": [
        "live",
        "register:40b0:8"
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
      "unmatched:00b969a0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c133e8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b969a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md#insn-00b969a0) · [`00b969c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md#insn-00b969c4) · [`00b96a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9696c.md#insn-00b96a1c)
- 新版 [`00c1340c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c133b4.md#insn-00c1340c)

~~~diff
- 00b969a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b969a0 ["INT_ADD", "register:40f0:8", ["const:b969a0:8", "const:4:8"]]
- 00b969a0 ["CALLIND", null, ["register:0:8"]]
- 00b969a0 bytes 00013fd6
- 00b969c4 ["INT_ADD", "register:40f0:8", ["const:b969c4:8", "const:4:8"]]
- 00b969c4 ["CALL", null, ["callee:00c076f0:8"]]
+ 00c1340c ["INT_ADD", "register:40f0:8", ["const:c1340c:8", "const:4:8"]]
+ 00c1340c ["CALL", null, ["callee:00c076f0:8"]]
- 00b969c4 bytes b9d0ff97
+ 00c1340c bytes b9d0ff97
- 00b96a1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b96a1c ["RETURN", null, ["register:0:8"]]
- 00b96a1c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef618daf33aa6447e9444a03dd8c494"></a>

### [`00b96a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md) → [`00c13468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 10.00% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c134a4",
      "incomplete_value": true,
      "site": "00c134ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b96a5c",
      "incomplete_value": true,
      "site": "00b96a64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c13498"
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
      "unmatched:00b96a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00c134a4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c134ac",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c13498",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00c134a4",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c134ac",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md#insn-00b96a50) · [`00b96a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md#insn-00b96a54) · [`00b96a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md#insn-00b96a70)
- 新版 [`00c1349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md#insn-00c1349c)

~~~diff
- 00b96a50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b96a50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b96a50 bytes e10700f9
- 00b96a54 ["INT_ADD", "register:40f0:8", ["const:b96a54:8", "const:4:8"]]
- 00b96a54 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c1349c ["INT_ADD", "register:40f0:8", ["const:c1349c:8", "const:4:8"]]
+ 00c1349c ["CALL", null, ["callee:00c57e70:8"]]
- 00b96a54 bytes 73120194
+ 00c1349c bytes 75120194
- 00b96a70 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b96a70 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb2eb17bf63a9e969c2fba6a5014fcca"></a>

### [`00b96b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md) → [`00c13584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13584.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b96b50",
      "incomplete_value": true,
      "site": "00b96b68",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b96b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md#insn-00b96b68) · [`00b96b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md#insn-00b96b70)
- 新版 [`00c135b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13584.md#insn-00c135b0) · [`00c135b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13584.md#insn-00c135b8)

~~~diff
- 00b96b68 ["INT_ADD", "register:40f0:8", ["const:b96b68:8", "const:4:8"]]
- 00b96b68 ["CALL", null, ["callee:00c14484:8"]]
+ 00c135b0 ["INT_ADD", "register:40f0:8", ["const:c135b0:8", "const:4:8"]]
+ 00c135b0 ["CALL", null, ["callee:00c14484:8"]]
- 00b96b68 bytes b5030094
+ 00c135b0 bytes b5030094
- 00b96b70 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b96b70 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b96b70 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b96b70 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c135b8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c135b8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c135b8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c135b8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b96b70 bytes 28011037
+ 00c135b8 bytes 28011037
~~~


<a id="compare-2a2a73bde9b24cb38976888e592ceb2e"></a>

### [`00b96ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md) → [`00c135ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md) [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.75% / 新版 90.75%

CFGの説明率　旧版 74.56% / 新版 65.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96bfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c13644"
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
      "unmatched:00b96bf4",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b96bf8",
      "READ",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96bfc",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1363c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c13640",
      "READ",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00c13644",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b96bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md#insn-00b96bfc) · [`00b96c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md#insn-00b96c08) · [`00b96c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md#insn-00b96c30)
- 新版 [`00c13678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md#insn-00c13678)

~~~diff
- 00b96bfc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b96bfc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b96bfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b96bfc bytes ba031ff8
- 00b96c08 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b96c08 bytes 60010054
- 00b96c30 ["INT_ADD", "register:40f0:8", ["const:b96c30:8", "const:4:8"]]
- 00b96c30 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c13678 ["INT_ADD", "register:40f0:8", ["const:c13678:8", "const:4:8"]]
+ 00c13678 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b96c30 bytes ac280194
+ 00c13678 bytes 1a290194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c8f0c23eea0beb0b7f1ab4cd7e7be3a"></a>

### [`00b97224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md) → [`00c13c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13c6c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b97238",
      "incomplete_value": true,
      "site": "00b97250",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b97240",
      "incomplete_value": true,
      "site": "00b97250",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b97244",
      "incomplete_value": true,
      "site": "00b97250",
      "value": [
        "live",
        "register:4020:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b97250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md#insn-00b97250) · [`00b97260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md#insn-00b97260) · [`00b97264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md#insn-00b97264)
- 新版 [`00c13c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13c6c.md#insn-00c13c98) · [`00c13ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13c6c.md#insn-00c13ca8) · [`00c13cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13c6c.md#insn-00c13cac)

~~~diff
- 00b97250 ["INT_ADD", "register:40f0:8", ["const:b97250:8", "const:4:8"]]
- 00b97250 ["CALL", null, ["callee:00c14484:8"]]
+ 00c13c98 ["INT_ADD", "register:40f0:8", ["const:c13c98:8", "const:4:8"]]
+ 00c13c98 ["CALL", null, ["callee:00c14484:8"]]
- 00b97250 bytes fb010094
+ 00c13c98 bytes fb010094
- 00b97260 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b97260 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b97260 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c13ca8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c13ca8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c13ca8 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b97260 bytes 88000054
+ 00c13ca8 bytes 88000054
- 00b97264 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b97264 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b97264 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b97264 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c13cac ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c13cac ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c13cac ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c13cac ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b97264 bytes 68001037
+ 00c13cac bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36ea564b0ad9a206a8fa1234bd10aee6"></a>

### [`00b972e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md) → [`00c13d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d30.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md#insn-00b97314) · [`00b97324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md#insn-00b97324) · [`00b97328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b972e8.md#insn-00b97328)
- 新版 [`00c13d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d30.md#insn-00c13d5c) · [`00c13d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d30.md#insn-00c13d6c) · [`00c13d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d30.md#insn-00c13d70)

~~~diff
- 00b97314 ["INT_ADD", "register:40f0:8", ["const:b97314:8", "const:4:8"]]
- 00b97314 ["CALL", null, ["callee:00c14484:8"]]
+ 00c13d5c ["INT_ADD", "register:40f0:8", ["const:c13d5c:8", "const:4:8"]]
+ 00c13d5c ["CALL", null, ["callee:00c14484:8"]]
- 00b97314 bytes ca010094
+ 00c13d5c bytes ca010094
- 00b97324 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b97324 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b97324 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c13d6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c13d6c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c13d6c ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b97324 bytes 88000054
+ 00c13d6c bytes 88000054
- 00b97328 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b97328 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b97328 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b97328 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c13d70 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c13d70 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c13d70 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c13d70 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b97328 bytes 68001037
+ 00c13d70 bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a68966505b192d1ffc4bb59edaaec8bc"></a>

### [`00b9734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md) → [`00c13d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d94.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b97378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md#insn-00b97378) · [`00b97384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md#insn-00b97384) · [`00b97388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b9734c.md#insn-00b97388)
- 新版 [`00c13dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d94.md#insn-00c13dc0) · [`00c13dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d94.md#insn-00c13dcc) · [`00c13dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13d94.md#insn-00c13dd0)

~~~diff
- 00b97378 ["INT_ADD", "register:40f0:8", ["const:b97378:8", "const:4:8"]]
- 00b97378 ["CALL", null, ["callee:00c14484:8"]]
+ 00c13dc0 ["INT_ADD", "register:40f0:8", ["const:c13dc0:8", "const:4:8"]]
+ 00c13dc0 ["CALL", null, ["callee:00c14484:8"]]
- 00b97378 bytes b1010094
+ 00c13dc0 bytes b1010094
- 00b97384 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b97384 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b97384 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b97384 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
+ 00c13dcc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c13dcc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c13dcc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c13dcc ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
- 00b97384 bytes 8c000054
+ 00c13dcc bytes 8c000054
- 00b97388 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b97388 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b97388 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b97388 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c13dd0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c13dd0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c13dd0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c13dd0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b97388 bytes 68001037
+ 00c13dd0 bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50444dc99ae031dcd2747e3d0745e5dc"></a>

### [`00b973ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b973ac.md) → [`00c13df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13df4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b973d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b973ac.md#insn-00b973d8) · [`00b973f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b973ac.md#insn-00b973f4)
- 新版 [`00c13e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13df4.md#insn-00c13e20) · [`00c13e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13df4.md#insn-00c13e3c)

~~~diff
- 00b973d8 ["INT_ADD", "register:40f0:8", ["const:b973d8:8", "const:4:8"]]
- 00b973d8 ["CALL", null, ["callee:00c14484:8"]]
+ 00c13e20 ["INT_ADD", "register:40f0:8", ["const:c13e20:8", "const:4:8"]]
+ 00c13e20 ["CALL", null, ["callee:00c14484:8"]]
- 00b973d8 bytes 99010094
+ 00c13e20 bytes 99010094
- 00b973f4 ["BRANCH", null, ["local:b4:8"]]
+ 00c13e3c ["BRANCH", null, ["local:b5:8"]]
- 00b973f4 bytes 03000014
+ 00c13e3c bytes 03000014
~~~


<a id="compare-8355c9eddfa3173f098318ec18575747"></a>

### [`00b97658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md) → [`00c140a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c140a0.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 76.92% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b976d8",
      "incomplete_value": true,
      "site": "00b976f0",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c14128",
      "incomplete_value": true,
      "site": "00c14138",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "old": {
      "definition_site": "00b976e0",
      "incomplete_value": true,
      "site": "00b976f0",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b976d4",
      "incomplete_value": true,
      "site": "00b976f0",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b976f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md#insn-00b976f0) · [`00b9768c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md#insn-00b9768c) · [`00b976cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97658.md#insn-00b976cc)
- 新版 [`00c14138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c140a0.md#insn-00c14138) · [`00c140d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c140a0.md#insn-00c140d4) · [`00c14114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c140a0.md#insn-00c14114)

~~~diff
- 00b976f0 ["INT_ADD", "register:40f0:8", ["const:b976f0:8", "const:4:8"]]
- 00b976f0 ["CALL", null, ["callee:00c076f0:8"]]
+ 00c14138 ["INT_ADD", "register:40f0:8", ["const:c14138:8", "const:4:8"]]
+ 00c14138 ["CALL", null, ["callee:00c076f0:8"]]
- 00b976f0 bytes 6ecdff97
+ 00c14138 bytes 6ecdff97
- 00b9768c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9768c ["INT_ADD", "register:40f0:8", ["const:b9768c:8", "const:4:8"]]
- 00b9768c ["CALLIND", null, ["register:0:8"]]
+ 00c140d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c140d4 ["INT_ADD", "register:40f0:8", ["const:c140d4:8", "const:4:8"]]
+ 00c140d4 ["CALLIND", null, ["register:0:8"]]
- 00b9768c bytes 00013fd6
+ 00c140d4 bytes 00013fd6
- 00b976cc ["BRANCH", null, ["local:b8:8"]]
+ 00c14114 ["BRANCH", null, ["local:b9:8"]]
- 00b976cc bytes 17000014
+ 00c14114 bytes 17000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86fdfecd0e37388f127f0942a9a4cee7"></a>

### [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md) → [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) FUN_00c14484

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00b96a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96a20.md) [`00b96b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96b3c.md) [`00b96ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96ba4.md) [`00b97224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97224.md) [`00b97288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97288.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00c13468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md) [`00c13584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13584.md) [`00c135ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md) [`00c13c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13c6c.md) [`00c13cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13cd0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.86% / 新版 80.86%

CFGの説明率　旧版 46.00% / 新版 42.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97a9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97ac4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c144c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b97a8c"
      ]
    ],
    [
      "unmatched:00b97a84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c14510"
      ]
    ],
    [
      "unmatched:00b97a88",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c144f8"
      ]
    ]
  ],
  "added": [
    [
      "00c144c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c144d4"
      ]
    ],
    [
      "00c144cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c14510"
      ]
    ],
    [
      "00c144d0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c144f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97a84) · [`00b97a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97a94) · [`00b97a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md#insn-00b97a9c)

~~~diff
- 00b97a84 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b97a84 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b97a84 bytes 340200b5
- 00b97a94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97a94 ["INT_ADD", "register:40f0:8", ["const:b97a94:8", "const:4:8"]]
- 00b97a94 ["CALLIND", null, ["register:0:8"]]
- 00b97a94 bytes 00013fd6
- 00b97a9c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b97a9c bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598c1df2fd380bb55e09cfed10cf54ed"></a>

### [`00b97d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97d80.md) → [`00c147c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKwSC_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.45% / 新版 80.45%

CFGの説明率　旧版 40.48% / 新版 36.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97ddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97df8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1481c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b97ddc",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b97ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1481c",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c14824",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c14824",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97d80.md#insn-00b97ddc) · [`00b97de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97d80.md#insn-00b97de8) · [`00b97df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97d80.md#insn-00b97df4)

~~~diff
- 00b97ddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b97ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00b97ddc bytes fc0700f9
- 00b97de8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b97de8 bytes 60010054
- 00b97df4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b97df4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b97df4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b97df4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcdbcb032879bf0cd1b90f64ca73de6d"></a>

### [`00b98280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md) → [`00c14cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
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
                "const:2e1000:8"
              ],
              [
                "leaf",
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9829c",
      "incomplete_value": true,
      "site": "00b982a8",
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
                "const:2cf000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
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
      "definition_site": "00b9829c",
      "incomplete_value": true,
      "site": "00b982a8",
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
      "00c14ce4",
      "READ",
      [
        "storage",
        "002cfd80",
        null,
        null
      ]
    ],
    [
      "00c14ce4",
      "READ",
      [
        "storage",
        "002cfd90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c14ce4",
      "READ",
      [
        "storage",
        "002e1938",
        null,
        null
      ]
    ],
    [
      "00c14ce4",
      "READ",
      [
        "storage",
        "002e1948",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md#insn-00b98290) · [`00b98294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md#insn-00b98294) · [`00b982ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98280.md#insn-00b982ac)
- 新版 [`00c14cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md#insn-00c14cd8) · [`00c14cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md#insn-00c14cdc) · [`00c14cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md#insn-00c14cf4)

~~~diff
- 00b98290 ["COPY", "register:4040:8", ["const:2cf000:8"]]
+ 00c14cd8 ["COPY", "register:4040:8", ["const:2e1000:8"]]
- 00b98290 bytes a8b9fff0
+ 00c14cd8 bytes 68b6ffb0
- 00b98294 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00b98294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b98294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b98294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c14cdc ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00c14cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c14cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c14cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b98294 bytes 08013691
+ 00c14cdc bytes 08e12491
- 00b982ac ["INT_ADD", "register:40f0:8", ["const:b982ac:8", "const:4:8"]]
- 00b982ac ["CALL", null, ["callee:00c5e230:8"]]
+ 00c14cf4 ["INT_ADD", "register:40f0:8", ["const:c14cf4:8", "const:4:8"]]
+ 00c14cf4 ["CALL", null, ["callee:00c5e230:8"]]
- 00b982ac bytes e5240194
+ 00c14cf4 bytes 4f250194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98b8d7e151b56b031179b48df3d48aa"></a>

### [`00b98350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md) → [`00c14d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.72% / 新版 82.72%

CFGの説明率　旧版 40.00% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9835c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b98358",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9835c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b98360",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c14da0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c14da4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c14da8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md#insn-00b98358) · [`00b9835c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md#insn-00b9835c) · [`00b98360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98350.md#insn-00b98360)

~~~diff
- 00b98358 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b98358 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b98358 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b98358 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98358 bytes fd7b03a9
- 00b9835c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b9835c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b9835c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b9835c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9835c bytes f85f04a9
- 00b98360 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b98360 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b98360 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b98360 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98360 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57399328b48a078f5e4e90de31cd0d50"></a>

### [`00b98564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md) → [`00c14fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.54% / 新版 83.54%

CFGの説明率　旧版 10.00% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98578"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b98574",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b98578",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b98598",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c14fbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c14fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c14fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md#insn-00b98574) · [`00b98578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md#insn-00b98578) · [`00b98598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98564.md#insn-00b98598)

~~~diff
- 00b98574 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b98574 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b98574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b98574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98574 bytes f65705a9
- 00b98578 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b98578 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b98578 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b98578 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b98578 bytes f44f06a9
- 00b98598 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b98598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b98598 bytes e10b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6230cfa37f3d80c124c783ba68766f44"></a>

### [`00b986b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md) → [`00c150fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c150fc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE15__get_monthnameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98718"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c15160"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b98718"
      ],
      [
        "FALL_THROUGH",
        "00c15160"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c15160",
      "incomplete_value": true,
      "site": "00c15194",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:101:1"
              ]
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              [
                "live",
                "register:100:1"
              ],
              [
                "live",
                "register:103:1"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98718",
      "incomplete_value": true,
      "site": "00b9874c",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SLESS",
              "INT_SBORROW"
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
      "unmatched:00b98718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c15198"
      ]
    ]
  ],
  "added": [
    [
      "00c15160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c15198"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md#insn-00b98718) · [`00b986e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b986b4.md#insn-00b986e8)
- 新版 [`00c15160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c150fc.md#insn-00c15160) · [`00c15130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c150fc.md#insn-00c15130)

~~~diff
- 00b98718 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b98718 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b98718 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b98718 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 00b98718 bytes cc010054
+ 00c15160 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c15160 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c15160 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c15160 ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
+ 00c15160 bytes cc010054
- 00b986e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b986e8 ["INT_ADD", "register:40f0:8", ["const:b986e8:8", "const:4:8"]]
- 00b986e8 ["CALLIND", null, ["register:0:8"]]
+ 00c15130 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c15130 ["INT_ADD", "register:40f0:8", ["const:c15130:8", "const:4:8"]]
+ 00c15130 ["CALLIND", null, ["register:0:8"]]
- 00b986e8 bytes 00013fd6
+ 00c15130 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0480e496ad2fd81518e8c85a48c39a2a"></a>

### [`00b98768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md) → [`00c151b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 30.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c151ec",
      "incomplete_value": true,
      "site": "00c151f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b987a4",
      "incomplete_value": true,
      "site": "00b987ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c151e0"
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
      "unmatched:00b98798",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00c151ec",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c151f4",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c151e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00c151ec",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c151f4",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md#insn-00b98798) · [`00b9879c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md#insn-00b9879c) · [`00b987b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md#insn-00b987b8)
- 新版 [`00c151e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md#insn-00c151e4) · [`00c15200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md#insn-00c15200)

~~~diff
- 00b98798 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b98798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b98798 bytes e10700f9
- 00b9879c ["INT_ADD", "register:40f0:8", ["const:b9879c:8", "const:4:8"]]
- 00b9879c ["CALL", null, ["callee:00c57e70:8"]]
+ 00c151e4 ["INT_ADD", "register:40f0:8", ["const:c151e4:8", "const:4:8"]]
+ 00c151e4 ["CALL", null, ["callee:00c57e70:8"]]
- 00b9879c bytes 210b0194
+ 00c151e4 bytes 230b0194
- 00b987b8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c15200 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b987b8 bytes 60010054
+ 00c15200 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09056aacd62698b9c32b0ccae61d3839"></a>

### [`00b988ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md) → [`00c15334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md) [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.01% / 新版 85.01%

CFGの説明率　旧版 65.79% / 新版 56.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9892c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1538c",
      "incomplete_value": true,
      "site": "00c1538c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b98944",
      "incomplete_value": true,
      "site": "00b98944",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b98b48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9892c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00c15384",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c1538c",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c15374",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00c15384",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1538c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9892c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md#insn-00b9892c) · [`00b98934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md#insn-00b98934) · [`00b98950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md#insn-00b98950)
- 新版 [`00c1537c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md#insn-00c1537c)

~~~diff
- 00b9892c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b9892c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b9892c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9892c bytes a1831ef8
- 00b98934 ["INT_ADD", "register:40f0:8", ["const:b98934:8", "const:4:8"]]
- 00b98934 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c1537c ["INT_ADD", "register:40f0:8", ["const:c1537c:8", "const:4:8"]]
+ 00c1537c ["CALL", null, ["callee:00c57e70:8"]]
- 00b98934 bytes bb0a0194
+ 00c1537c bytes bd0a0194
- 00b98950 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b98950 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f362a01acd204fa17e96589e3e98e88"></a>

### [`00b98fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md) → [`00c15a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a08.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b98fd4",
      "incomplete_value": true,
      "site": "00b98fec",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b98fdc",
      "incomplete_value": true,
      "site": "00b98fec",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b98fe0",
      "incomplete_value": true,
      "site": "00b98fec",
      "value": [
        "live",
        "register:4020:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b98fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md#insn-00b98fec) · [`00b98ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md#insn-00b98ff8) · [`00b98ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md#insn-00b98ffc)
- 新版 [`00c15a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a08.md#insn-00c15a34) · [`00c15a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a08.md#insn-00c15a40) · [`00c15a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a08.md#insn-00c15a44)

~~~diff
- 00b98fec ["INT_ADD", "register:40f0:8", ["const:b98fec:8", "const:4:8"]]
- 00b98fec ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15a34 ["INT_ADD", "register:40f0:8", ["const:c15a34:8", "const:4:8"]]
+ 00c15a34 ["CALL", null, ["callee:00c161c8:8"]]
- 00b98fec bytes e5010094
+ 00c15a34 bytes e5010094
- 00b98ff8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b98ff8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b98ff8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b98ff8 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
+ 00c15a40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c15a40 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c15a40 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c15a40 ["CBRANCH", null, ["local:b5:8", "tmp:2:1"]]
- 00b98ff8 bytes 8c000054
+ 00c15a40 bytes 8c000054
- 00b98ffc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b98ffc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b98ffc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b98ffc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c15a44 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c15a44 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c15a44 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c15a44 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b98ffc bytes 68001037
+ 00c15a44 bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a850f0a2fe743b73d3b372af769b973"></a>

### [`00b99084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md) → [`00c15acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15acc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE18__get_day_year_numERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b99098",
      "incomplete_value": true,
      "site": "00b990b0",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b990a0",
      "incomplete_value": true,
      "site": "00b990b0",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b990b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md#insn-00b990b0) · [`00b990bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md#insn-00b990bc) · [`00b990c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99084.md#insn-00b990c0)
- 新版 [`00c15af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15acc.md#insn-00c15af8) · [`00c15b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15acc.md#insn-00c15b04) · [`00c15b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15acc.md#insn-00c15b08)

~~~diff
- 00b990b0 ["INT_ADD", "register:40f0:8", ["const:b990b0:8", "const:4:8"]]
- 00b990b0 ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15af8 ["INT_ADD", "register:40f0:8", ["const:c15af8:8", "const:4:8"]]
+ 00c15af8 ["CALL", null, ["callee:00c161c8:8"]]
- 00b990b0 bytes b4010094
+ 00c15af8 bytes b4010094
- 00b990bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b990bc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b990bc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b990bc ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
+ 00c15b04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c15b04 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c15b04 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c15b04 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
- 00b990bc bytes 8c000054
+ 00c15b04 bytes 8c000054
- 00b990c0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b990c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b990c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b990c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c15b08 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c15b08 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c15b08 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c15b08 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b990c0 bytes 68001037
+ 00c15b08 bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4245271c34f4fdad752711bcd909665"></a>

### [`00b994e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md) → [`00c15f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f28.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b994f4",
      "incomplete_value": true,
      "site": "00b9950c",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b994fc",
      "incomplete_value": true,
      "site": "00b9950c",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b99500",
      "incomplete_value": true,
      "site": "00b9950c",
      "value": [
        "live",
        "register:4020:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md#insn-00b9950c) · [`00b99518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md#insn-00b99518) · [`00b9951c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b994e0.md#insn-00b9951c)
- 新版 [`00c15f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f28.md#insn-00c15f54) · [`00c15f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f28.md#insn-00c15f60) · [`00c15f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f28.md#insn-00c15f64)

~~~diff
- 00b9950c ["INT_ADD", "register:40f0:8", ["const:b9950c:8", "const:4:8"]]
- 00b9950c ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15f54 ["INT_ADD", "register:40f0:8", ["const:c15f54:8", "const:4:8"]]
+ 00c15f54 ["CALL", null, ["callee:00c161c8:8"]]
- 00b9950c bytes 9d000094
+ 00c15f54 bytes 9d000094
- 00b99518 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b99518 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b99518 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b99518 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
+ 00c15f60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c15f60 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c15f60 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c15f60 ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
- 00b99518 bytes 8c000054
+ 00c15f60 bytes 8c000054
- 00b9951c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b9951c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b9951c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b9951c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c15f64 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c15f64 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c15f64 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c15f64 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b9951c bytes 68001037
+ 00c15f64 bytes 68001037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23dcc27552b1339ff2b182b63e9e3981"></a>

### [`00b99540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99540.md) → [`00c15f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f88.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b99554",
      "incomplete_value": true,
      "site": "00b9956c",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9955c",
      "incomplete_value": true,
      "site": "00b9956c",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b99560",
      "incomplete_value": true,
      "site": "00b9956c",
      "value": [
        "live",
        "register:4020:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9956c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99540.md#insn-00b9956c) · [`00b99574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99540.md#insn-00b99574)
- 新版 [`00c15fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f88.md#insn-00c15fb4) · [`00c15fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15f88.md#insn-00c15fbc)

~~~diff
- 00b9956c ["INT_ADD", "register:40f0:8", ["const:b9956c:8", "const:4:8"]]
- 00b9956c ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15fb4 ["INT_ADD", "register:40f0:8", ["const:c15fb4:8", "const:4:8"]]
+ 00c15fb4 ["CALL", null, ["callee:00c161c8:8"]]
- 00b9956c bytes 85000094
+ 00c15fb4 bytes 85000094
- 00b99574 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
- 00b99574 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b99574 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b99574 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c15fbc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:2:4"]]
+ 00c15fbc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c15fbc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c15fbc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b99574 bytes 68001037
+ 00c15fbc bytes 68001037
~~~


<a id="compare-81ff1d1dc7389275b8b04eea832390dd"></a>

### [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md) → [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) FUN_00c161c8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00b98768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98768.md) [`00b98884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md) [`00b988ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b988ec.md) [`00b98f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md) [`00b98fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98fc0.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00c151b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md) [`00c152cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c152cc.md) [`00c15334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md) [`00c159a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c159a4.md) [`00c15a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a08.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.30% / 新版 69.30%

CFGの説明率　旧版 31.18% / 新版 29.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99a6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c161fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b99804"
      ]
    ],
    [
      "unmatched:00b997cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b99800"
      ]
    ],
    [
      "00c16224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9980c"
      ]
    ]
  ],
  "added": [
    [
      "00c161fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1624c"
      ]
    ],
    [
      "00c16214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16248"
      ]
    ],
    [
      "00c16224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16254"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b997cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b997cc) · [`00b997fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b997fc) · [`00b99800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md#insn-00b99800)

~~~diff
- 00b997cc ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b997cc bytes a0010054
- 00b997fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b997fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b997fc bytes a1feff54
- 00b99800 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b99800 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b99800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b99800 bytes 9f0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a9f9d793587b35fdb248c5d47afb11"></a>

### [`00b99adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99adc.md) → [`00c16524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE3putES4_RNS_8ios_baseEcPK2tmPKcSC_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd930.md) · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5a380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a380.md) · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.34% / 新版 88.34%

CFGの説明率　旧版 65.31% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16574",
      "incomplete_value": true,
      "site": "00c1657c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b99b2c",
      "incomplete_value": true,
      "site": "00b99b34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1655c"
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
      "unmatched:00b99b14",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00c16574",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1657c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1655c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00c16574",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c1657c",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99adc.md#insn-00b99b14) · [`00b99b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99adc.md#insn-00b99b24) · [`00b99b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99adc.md#insn-00b99b40)
- 新版 [`00c1656c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md#insn-00c1656c) · [`00c16588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md#insn-00c16588)

~~~diff
- 00b99b14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b99b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:8"]]
- 00b99b14 bytes e40700f9
- 00b99b24 ["INT_ADD", "register:40f0:8", ["const:b99b24:8", "const:4:8"]]
- 00b99b24 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c1656c ["INT_ADD", "register:40f0:8", ["const:c1656c:8", "const:4:8"]]
+ 00c1656c ["CALL", null, ["callee:00c57e70:8"]]
- 00b99b24 bytes 3f060194
+ 00c1656c bytes 41060194
- 00b99b40 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c16588 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b99b40 bytes 40010054
+ 00c16588 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7568c34c04054c8994cecdb59fbe4519"></a>

### [`00b99d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md) → [`00c167c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c167c4.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPK2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md#insn-00b99dd0) · [`00b99dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md#insn-00b99dd4) · [`00b99de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99d7c.md#insn-00b99de0)
- 新版 [`00c16818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c167c4.md#insn-00c16818) · [`00c1681c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c167c4.md#insn-00c1681c) · [`00c16828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c167c4.md#insn-00c16828)

~~~diff
- 00b99dd0 ["INT_ADD", "register:40f0:8", ["const:b99dd0:8", "const:4:8"]]
- 00b99dd0 ["CALL", null, ["callee:00c5e260:8"]]
+ 00c16818 ["INT_ADD", "register:40f0:8", ["const:c16818:8", "const:4:8"]]
+ 00c16818 ["CALL", null, ["callee:00c5e260:8"]]
- 00b99dd0 bytes 281e0194
+ 00c16818 bytes 921e0194
- 00b99dd4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b99dd4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00c1681c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c1681c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b99dd4 bytes c00200b4
+ 00c1681c bytes c00200b4
- 00b99de0 ["BRANCH", null, ["local:b6:8"]]
+ 00c16828 ["BRANCH", null, ["local:b7:8"]]
- 00b99de0 bytes 0a000014
+ 00c16828 bytes 0a000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c70db70d32cbc911455cfb1b7829f8c"></a>

### [`00b99ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99ebc.md) → [`00c16904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE3putES4_RNS_8ios_baseEwPK2tmPKwSC_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.83% / 新版 86.83%

CFGの説明率　旧版 53.85% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99ecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99ecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99ed0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b99ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b99ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b99ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c16914",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c16918",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c1691c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99ebc.md#insn-00b99ecc) · [`00b99ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99ebc.md#insn-00b99ed0) · [`00b99ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99ebc.md#insn-00b99ed4)

~~~diff
- 00b99ecc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b99ecc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b99ecc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b99ecc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b99ecc bytes fa6705a9
- 00b99ed0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b99ed0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b99ed0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b99ed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b99ed0 bytes f85f06a9
- 00b99ed4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b99ed4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b99ed4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b99ed4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b99ed4 bytes f65707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-835eaded445b8d5d15169c43b9064e28"></a>

### [`00b9a16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md) → [`00c16bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPK2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1680.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 83.33% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a1a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c16bf0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9a194",
      "incomplete_value": true,
      "site": "00b9a1ac",
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
            "const:10:8"
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
      "unmatched:00b9a1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c16bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md#insn-00b9a1a8) · [`00b9a1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a16c.md#insn-00b9a1ac)
- 新版 [`00c16bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md#insn-00c16bf4) · [`00c16bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16bb4.md#insn-00c16bf0)

~~~diff
- 00b9a1a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b9a1a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9a1a8 bytes e80700f9
- 00b9a1ac ["INT_ADD", "register:40f0:8", ["const:b9a1ac:8", "const:4:8"]]
- 00b9a1ac ["CALL", null, ["callee:00c5e270:8"]]
+ 00c16bf4 ["INT_ADD", "register:40f0:8", ["const:c16bf4:8", "const:4:8"]]
+ 00c16bf4 ["CALL", null, ["callee:00c5e270:8"]]
- 00b9a1ac bytes 351d0194
+ 00c16bf4 bytes 9f1d0194
+ 00c16bf0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00c16bf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c16bf0 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a95aff5f7fc33a67e112843541bf360"></a>

### [`00b9a228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md) → [`00c16c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1680.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md) [`00be1690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1690.md)
- 新版 呼出元 1件 [`00c5e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e270.md) · 呼出先 5件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md) [`00c5e280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e280.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 37.50% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c16cac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9a264",
      "WRITE",
      [
        "storage",
        "Stack[-0x25]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9a268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16cbc"
      ]
    ],
    [
      "00c16d48",
      "PARAM",
      [
        "storage",
        "002907d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c16cac",
      "WRITE",
      [
        "storage",
        "Stack[-0x25]",
        null,
        null
      ]
    ],
    [
      "00c16cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16cbc"
      ]
    ],
    [
      "00c16d48",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a264) · [`00b9a268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a268) · [`00b9a288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a228.md#insn-00b9a288)
- 新版 [`00c16cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md#insn-00c16cd0)

~~~diff
- 00b9a264 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b9a264 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b9a264 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:1b:8"]]
- 00b9a264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b9a264 bytes bf6f0039
- 00b9a268 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b9a268 bytes 60000054
- 00b9a288 ["INT_ADD", "register:40f0:8", ["const:b9a288:8", "const:4:8"]]
- 00b9a288 ["CALL", null, ["callee:00c5e260:8"]]
+ 00c16cd0 ["INT_ADD", "register:40f0:8", ["const:c16cd0:8", "const:4:8"]]
+ 00c16cd0 ["CALL", null, ["callee:00c5e260:8"]]
- 00b9a288 bytes fa1c0194
+ 00c16cd0 bytes 641d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26f00f9a992fbc8f759529b6f68a13fe"></a>

### [`00b9a320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a320.md) → [`00c16d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16d68.md) _ZNKSt6__ndk110moneypunctIcLb0EE16do_decimal_pointEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-3d6ad6729f89c450672a8f4500b666bf"></a>

### [`00b9a348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a348.md) → [`00c16d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16d90.md) _ZNKSt6__ndk110moneypunctIcLb0EE14do_curr_symbolEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-d9c2a9567e07c019a0c84c6bdf2153f5"></a>

### [`00b9a3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a3d0.md) → [`00c16e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16e18.md) _ZNKSt6__ndk110moneypunctIcLb1EE14do_curr_symbolEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-1daf082b6b82024a0e890e6afa53e45a"></a>

### [`00b9a478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a478.md) → [`00c16ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md) _ZNKSt6__ndk110moneypunctIwLb0EE16do_negative_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16ecc",
      "incomplete_value": true,
      "site": "00c16ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9a484",
      "incomplete_value": true,
      "site": "00b9a48c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
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
      "00c16ecc",
      "READ",
      [
        "storage",
        "002b28b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c16ecc",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a478.md#insn-00b9a47c) · [`00b9a484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a478.md#insn-00b9a484)
- 新版 [`00c16ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md#insn-00c16ec4) · [`00c16ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md#insn-00c16ecc)

~~~diff
- 00b9a47c ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 00c16ec4 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 00b9a47c bytes c9b8ff90
+ 00c16ec4 bytes 69b5ffb0
- 00b9a484 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8b8:8"]]
- 00b9a484 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9a484 ["COPY", "register:5008:8", ["const:0:8"]]
- 00b9a484 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c16ecc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
+ 00c16ecc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c16ecc ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c16ecc ["COPY", "register:5010:8", ["const:0:8"]]
- 00b9a484 bytes 205d44fd
+ 00c16ecc bytes 20c147fd
~~~


<a id="compare-ea7f0a93a8e0f24f70b9a9e24a25e2f2"></a>

### [`00b9a4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a4d8.md) → [`00c16f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f20.md) _ZNKSt6__ndk110moneypunctIwLb1EE11do_groupingEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-6cdfc2132c139b29fe3a21f7bf83cd09"></a>

### [`00b9a508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a508.md) → [`00c16f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md) _ZNKSt6__ndk110moneypunctIwLb1EE16do_negative_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16f5c",
      "incomplete_value": true,
      "site": "00c16f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9a514",
      "incomplete_value": true,
      "site": "00b9a51c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
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
      "00c16f5c",
      "READ",
      [
        "storage",
        "002b28b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c16f5c",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a508.md#insn-00b9a50c) · [`00b9a514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a508.md#insn-00b9a514)
- 新版 [`00c16f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md#insn-00c16f54) · [`00c16f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md#insn-00c16f5c)

~~~diff
- 00b9a50c ["COPY", "register:4048:8", ["const:2b2000:8"]]
+ 00c16f54 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 00b9a50c bytes c9b8ff90
+ 00c16f54 bytes 69b5ffb0
- 00b9a514 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8b8:8"]]
- 00b9a514 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b9a514 ["COPY", "register:5008:8", ["const:0:8"]]
- 00b9a514 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c16f5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
+ 00c16f5c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c16f5c ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c16f5c ["COPY", "register:5010:8", ["const:0:8"]]
- 00b9a514 bytes 205d44fd
+ 00c16f5c bytes 20c147fd
~~~


<a id="compare-0fd16ebab444d8eafa62c0f340474418"></a>

### [`00b9a628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a628.md) → [`00c17070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17070.md) _ZNKSt6__ndk117moneypunct_bynameIcLb0EE14do_frac_digitsEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-71689740278abcbc24f5f0fccd84ace2"></a>

### [`00b9a694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a694.md) → [`00c170dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c170dc.md) _ZNKSt6__ndk117moneypunct_bynameIcLb1EE14do_curr_symbolEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a694.md#insn-00b9a6c0)
- 新版 [`00c17108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c170dc.md#insn-00c17108)

~~~diff
- 00b9a6c0 48fae117
+ 00c17108 7692e017
~~~


<a id="compare-15d0290a89c1408c7681de95591bd9d8"></a>

### [`00b9a6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a6f4.md) → [`00c1713c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c1713c.md) _ZNKSt6__ndk117moneypunct_bynameIcLb1EE16do_negative_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a6f4.md#insn-00b9a700)
- 新版 [`00c17148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c1713c.md#insn-00c17148)

~~~diff
- 00b9a700 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b9a700 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b9a700 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b9a700 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c17148 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c17148 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c17148 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c17148 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b9a700 bytes ca000037
+ 00c17148 bytes ca000037
~~~


<a id="compare-b9e06a11644ab11466d92a7b7306d18b"></a>

### [`00b9a760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a760.md) → [`00c171a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c171a8.md) _ZNKSt6__ndk117moneypunct_bynameIwLb0EE11do_groupingEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a760.md#insn-00b9a78c)
- 新版 [`00c171d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c171a8.md#insn-00c171d4)

~~~diff
- 00b9a78c 15fae117
+ 00c171d4 4392e017
~~~


<a id="compare-c5ee5b65a630693b70f22bc24a43203e"></a>

### [`00b9a7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a7c0.md) → [`00c17208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17208.md) _ZNKSt6__ndk117moneypunct_bynameIwLb0EE16do_positive_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a7c0.md#insn-00b9a7ec)
- 新版 [`00c17234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17208.md#insn-00c17234)

~~~diff
- 00b9a7ec 3f4cec17
+ 00c17234 1c01eb17
~~~


<a id="compare-34b4ee321b1953d37f64b162547cb5ed"></a>

### [`00b9a85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a85c.md) → [`00c172a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c172a4.md) _ZNKSt6__ndk117moneypunct_bynameIwLb1EE11do_groupingEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a85c.md#insn-00b9a888)
- 新版 [`00c172d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c172a4.md#insn-00c172d0)

~~~diff
- 00b9a888 d6f9e117
+ 00c172d0 0492e017
~~~


<a id="compare-f4de307a8afc95d2dc98ae8293fb9f41"></a>

### [`00b9a8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a8ec.md) → [`00c17334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17334.md) _ZNKSt6__ndk117moneypunct_bynameIwLb1EE16do_negative_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9a8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a8ec.md#insn-00b9a8f8)
- 新版 [`00c17340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17334.md#insn-00c17340)

~~~diff
- 00b9a8f8 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b9a8f8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b9a8f8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b9a8f8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c17340 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c17340 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c17340 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c17340 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b9a8f8 bytes ca000037
+ 00c17340 bytes ca000037
~~~


<a id="compare-dc2e58b3f8f3811796e3c086d5a3ced1"></a>

### [`00b9a940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md) → [`00c17388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.59% / 新版 79.59%

CFGの説明率　旧版 62.90% / 新版 52.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a95c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9a958",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9a95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9a964",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c173a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c173a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c173ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md#insn-00b9a958) · [`00b9a95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md#insn-00b9a95c) · [`00b9a964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md#insn-00b9a964)

~~~diff
- 00b9a958 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9a958 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9a958 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b9a958 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9a958 bytes f65717a9
- 00b9a95c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b9a95c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9a95c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b9a95c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9a95c bytes f44f18a9
- 00b9a964 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b9a964 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b9a964 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9a964 bytes a1831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd09fb5dd20ce9512798397e78a72b82"></a>

### [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) → [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) _ZNSt6__ndk112__do_nothingEPv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 6件 [`00b9a940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a940.md) [`00b9ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md) [`00b9be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md) [`00b9c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md) [`00b9cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md) · 呼出先 0件 
- 新版 呼出元 6件 [`00c17388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md) [`00c176d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md) [`00c188dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) [`00c19224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md) [`00c1956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-97a90c7a3dcd017578aea7c8c8a11633"></a>

### [`00b9ac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md) → [`00c176d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md) _ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIcEERNS_10unique_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be16a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16a0.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00c5e290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e290.md) · 呼出先 11件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.20% / 新版 74.20%

CFGの説明率　旧版 48.76% / 新版 47.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 1件, `unresolved_branch_alignment` 69件, `unresolved_call_alignment` 18件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ad20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9adcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9adcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1771c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9ad24"
      ]
    ],
    [
      "00c17728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9acf8"
      ]
    ],
    [
      "unmatched:00b9ace8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c17774"
      ]
    ]
  ],
  "added": [
    [
      "00c1771c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1776c"
      ]
    ],
    [
      "00c17728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c17740"
      ]
    ],
    [
      "00c17730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c17774"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9ad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md#insn-00b9ad20) · [`00b9adcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md#insn-00b9adcc) · [`00b9adf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac8c.md#insn-00b9adf0)

~~~diff
- 00b9ad20 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b9ad20 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b9ad20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b9ad20 bytes bf0200f9
- 00b9adcc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b9adcc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b9adcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:58:8"]]
- 00b9adcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9adcc bytes e9a305a9
- 00b9adf0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b9adf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9adf0 bytes 480100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0992e0f09f0b5aadf2d64cf48cfaba4"></a>

### [`00b9be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md) → [`00c188dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIcS3_NS_9allocato

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00b9c154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c18b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.82% / 新版 96.82%

CFGの説明率　旧版 84.91% / 新版 80.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bedc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bedc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18940",
      "incomplete_value": true,
      "site": "00c18940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9bef8",
      "incomplete_value": true,
      "site": "00b9bef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
      "unmatched:00b9bec4",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b9bedc",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "unmatched:00b9bedc",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1890c",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c18924",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c18924",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md#insn-00b9bedc) · [`00b9bf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md#insn-00b9bf04) · [`00b9bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md#insn-00b9bf2c)
- 新版 [`00c1894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md#insn-00c1894c) · [`00c18974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md#insn-00c18974)

~~~diff
- 00b9bedc ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b9bedc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b9bedc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b9bedc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9bedc bytes f92303a9
- 00b9bf04 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c1894c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b9bf04 bytes 60010054
+ 00c1894c bytes 60010054
- 00b9bf2c ["INT_ADD", "register:40f0:8", ["const:b9bf2c:8", "const:4:8"]]
- 00b9bf2c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c18974 ["INT_ADD", "register:40f0:8", ["const:c18974:8", "const:4:8"]]
+ 00c18974 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b9bf2c bytes ed130194
+ 00c18974 bytes 5b140194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b5f4529d1b8d62d657e84f4b77ff92"></a>

### [`00b9c154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md) → [`00c18b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md) FUN_00c18b9c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b9be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9b/00b9be94.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c188dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 93.44% / 新版 90.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c1c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c18c10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b9c498",
      "incomplete_value": true,
      "site": "00b9c49c",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00b9c1c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c18c50"
      ]
    ]
  ],
  "added": [
    [
      "00c18c10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c18c50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md#insn-00b9c1c8) · [`00b9c49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c154.md#insn-00b9c49c)
- 新版 [`00c18ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md#insn-00c18ee4) · [`00c18c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md#insn-00c18c10)

~~~diff
- 00b9c1c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9c1c8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b9c1c8 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b9c1c8 bytes 08020054
- 00b9c49c ["INT_ADD", "register:40f0:8", ["const:b9c49c:8", "const:4:8"]]
- 00b9c49c ["CALL", null, ["callee:0043b724:8"]]
+ 00c18ee4 ["INT_ADD", "register:40f0:8", ["const:c18ee4:8", "const:4:8"]]
+ 00c18ee4 ["CALL", null, ["callee:0043b724:8"]]
- 00b9c49c bytes e2f1e197
+ 00c18ee4 bytes 108ae097
+ 00c18c10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c18c10 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c18c10 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 00c18c10 bytes 08020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d3c06516b85e7003baace9517df10e9"></a>

### [`00b9c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c4bc.md) → [`00c18f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18f04.md) _ZNSt6__ndk111__money_getIcE13__gather_infoEbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocato

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be16c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16c0.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2b0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 52.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18f54",
      "incomplete_value": true,
      "site": "00c18f54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9c50c",
      "incomplete_value": true,
      "site": "00b9c50c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:da8:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c52c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c18f50",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00c18f54",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b9c510",
      "READ",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c18f50",
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c18f54",
      "DATA",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c18f58",
      "READ",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c4bc.md#insn-00b9c518) · [`00b9c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c4bc.md#insn-00b9c528) · [`00b9c52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c4bc.md#insn-00b9c52c)

~~~diff
- 00b9c518 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b9c518 bytes 00030054
- 00b9c528 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b9c528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9c528 bytes e80300f9
- 00b9c52c ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:18:8"]]
- 00b9c52c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b9c52c bytes a90f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dd8a84c2d85ea3b21785bd64c7677f5"></a>

### [`00b9c6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c6e4.md) → [`00c1912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1912c.md) _ZNSt6__ndk116__check_groupingERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjS8_Rj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.10% / 新版 84.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9c704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c6e4.md#insn-00b9c704) · [`00b9c708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c6e4.md#insn-00b9c708) · [`00b9c75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c6e4.md#insn-00b9c75c)
- 新版 [`00c1914c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1912c.md#insn-00c1914c) · [`00c19150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1912c.md#insn-00c19150) · [`00c191a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1912c.md#insn-00c191a4)

~~~diff
- 00b9c704 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b9c704 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00c1914c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00c1914c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b9c704 bytes ab060054
+ 00c1914c bytes ab060054
- 00b9c708 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b9c708 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00c19150 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00c19150 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b9c708 bytes 880600b4
+ 00c19150 bytes 880600b4
- 00b9c75c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b9c75c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b9c75c ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
+ 00c191a4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c191a4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c191a4 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b9c75c bytes a9020054
+ 00c191a4 bytes a9020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc27299b57b83683e09c304e307a313"></a>

### [`00b9c7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md) → [`00c19224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.31% / 新版 87.31%

CFGの説明率　旧版 68.33% / 新版 62.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19280",
      "incomplete_value": true,
      "site": "00c19288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9c838",
      "incomplete_value": true,
      "site": "00b9c840",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "unmatched:00b9c80c",
      "READ",
      [
        "storage",
        "00c1bda0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b9c824",
      "DATA",
      [
        "storage",
        "00b9ac84",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "unmatched:00b9c824",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c19254",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c1926c",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1926c",
      "WRITE",
      [
        "storage",
        "Stack[-0x208]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md#insn-00b9c824) · [`00b9c874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md#insn-00b9c874) · [`00b9c8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9c7dc.md#insn-00b9c8ec)
- 新版 [`00c192bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md#insn-00c192bc)

~~~diff
- 00b9c824 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b9c824 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b9c824 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c8:8"]]
- 00b9c824 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9c824 bytes f9a30ca9
- 00b9c874 ["INT_ADD", "register:40f0:8", ["const:b9c874:8", "const:4:8"]]
- 00b9c874 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c192bc ["INT_ADD", "register:40f0:8", ["const:c192bc:8", "const:4:8"]]
+ 00c192bc ["CALL", null, ["callee:00c5dae0:8"]]
- 00b9c874 bytes 9b110194
+ 00c192bc bytes 09120194
- 00b9c8ec ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b9c8ec ["INT_ADD", "tmp:1:8", ["register:8:8", "const:af:8"]]
- 00b9c8ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b9c8ec bytes e8f30ab8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aac6f3904e3d04adc5249396ab05ad79"></a>

### [`00b9cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md) → [`00c1956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md) _ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIwEERNS_10unique_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be16d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16d0.md) · 呼出先 11件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c5e2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2c0.md) · 呼出先 11件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.43% / 新版 61.43%

CFGの説明率　旧版 15.72% / 新版 11.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 5件, `unresolved_branch_alignment` 108件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 19件

アドレスに依存する影響 `branch_value` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9cb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9cb68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9cc50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9cb64",
      "WRITE",
      [
        "storage",
        "Stack[-0x2d0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9cb68",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c4]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9cb6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c19604"
      ]
    ]
  ],
  "added": [
    [
      "00c195ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x2d0]",
        null,
        null
      ]
    ],
    [
      "00c195b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c4]",
        null,
        null
      ]
    ],
    [
      "00c195b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c19604"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9cb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md#insn-00b9cb64) · [`00b9cb68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md#insn-00b9cb68) · [`00b9cc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9c/00b9cb24.md#insn-00b9cc50)

~~~diff
- 00b9cb64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b9cb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4030:8"]]
- 00b9cb64 bytes e62300f9
- 00b9cb68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:4c:8"]]
- 00b9cb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 00b9cb68 bytes e44f00b9
- 00b9cc50 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b9cc50 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b9cc50 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00b9cc50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9cc50 bytes f82300a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed93b82656856d18b34ebca5eee816c9"></a>

### [`00b9de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md) → [`00c1a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1a898.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIwS3_NS_9allocato

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9ac84.md) [`00b9e17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c1abc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.35% / 新版 79.35%

CFGの説明率　旧版 55.00% / 新版 34.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9de54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9de54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9de58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9de54",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9de58",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9de5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1a89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c1a8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c1a8a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9de54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md#insn-00b9de54) · [`00b9de58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md#insn-00b9de58) · [`00b9de5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md#insn-00b9de5c)

~~~diff
- 00b9de54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9de54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9de54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b9de54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9de54 bytes fd7bbaa9
- 00b9de58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b9de58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00b9de58 bytes fc0b00f9
- 00b9de5c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b9de5c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b9de5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b9de5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9de5c bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be1861b27c305f3c01db3e718abf766d"></a>

### [`00b9e49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e49c.md) → [`00c1aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1aee4.md) _ZNSt6__ndk111__money_getIwE13__gather_infoEbRKNS_6localeERNS_10money_base7patternERwS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocato

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be16e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16e0.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2d0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.74% / 新版 71.74%

CFGの説明率　旧版 23.08% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e4b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9e4b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9e4b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9e4c0",
      "READ",
      [
        "storage",
        "Stack[0x0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1aefc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c1af00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c1af08",
      "READ",
      [
        "storage",
        "Stack[0x0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9e4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e49c.md#insn-00b9e4b4) · [`00b9e4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e49c.md#insn-00b9e4b8) · [`00b9e4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e49c.md#insn-00b9e4f8)

~~~diff
- 00b9e4b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9e4b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9e4b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b9e4b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9e4b4 bytes f65706a9
- 00b9e4b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b9e4b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9e4b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b9e4b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9e4b8 bytes f44f07a9
- 00b9e4f8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b9e4f8 bytes 00030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0415662e883b4520dcdecce7dd49ec21"></a>

### [`00b9e6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md) → [`00c1b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEce

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.35% / 新版 79.35%

CFGの説明率　旧版 35.59% / 新版 24.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1b1e4",
      "incomplete_value": true,
      "site": "00c1b1ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9e79c",
      "incomplete_value": true,
      "site": "00b9e7a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9e6f8",
      "PARAM",
      [
        "storage",
        "002a1124",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b9e710",
      "WRITE",
      [
        "storage",
        "Stack[-0x230]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9e714",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5dd00"
      ]
    ]
  ],
  "added": [
    [
      "00c1b140",
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      "00c1b158",
      "WRITE",
      [
        "storage",
        "Stack[-0x230]",
        null,
        null
      ]
    ],
    [
      "00c1b15c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5dd00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9e710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md#insn-00b9e710) · [`00b9e714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md#insn-00b9e714) · [`00b9e71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md#insn-00b9e71c)

~~~diff
- 00b9e710 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b9e710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9e710 bytes e013803d
- 00b9e714 ["INT_ADD", "register:40f0:8", ["const:b9e714:8", "const:4:8"]]
- 00b9e714 ["CALL", null, ["callee:00c5dd00:8"]]
- 00b9e714 bytes 7b0a0194
- 00b9e71c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b9e71c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b9e71c bytes e3020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b97bb8ce9f113b8b242df36896c17f7"></a>

### [`00b9ec3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ec3c.md) → [`00c1b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b684.md) _ZNSt6__ndk111__money_putIcE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocat

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be16f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be16f0.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2e0.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.44% / 新版 77.44%

CFGの説明率　旧版 30.77% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ec4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ec4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ec50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9ec4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9ec50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9ec54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1b694",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c1b698",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c1b69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9ec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ec3c.md#insn-00b9ec4c) · [`00b9ec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ec3c.md#insn-00b9ec50) · [`00b9ec54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ec3c.md#insn-00b9ec54)

~~~diff
- 00b9ec4c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b9ec4c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b9ec4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b9ec4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9ec4c bytes fa6704a9
- 00b9ec50 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b9ec50 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b9ec50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b9ec50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9ec50 bytes f85f05a9
- 00b9ec54 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9ec54 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9ec54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b9ec54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9ec54 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aa1b36aac6d3dcfe1283481f8059503"></a>

### [`00b9ee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md) → [`00c1b898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b898.md) _ZNSt6__ndk111__money_putIcE8__formatEPcRS2_S3_jPKcS5_RKNS_5ctypeIcEEbRKNS_10money_base7patternEccRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1700.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5e2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2f0.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.99% / 新版 87.99%

CFGの説明率　旧版 54.84% / 新版 44.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ef94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ef98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9effc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9ef04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9f004"
      ]
    ],
    [
      "unmatched:00b9ef9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1b9f0"
      ]
    ],
    [
      "unmatched:00b9efb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1bae4"
      ]
    ]
  ],
  "added": [
    [
      "00c1b94c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1ba4c"
      ]
    ],
    [
      "00c1b9e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1b9f0"
      ]
    ],
    [
      "00c1b9f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1bae4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9ef04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9ef04) · [`00b9ef94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9ef94) · [`00b9ef98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9ee50.md#insn-00b9ef98)

~~~diff
- 00b9ef04 ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00b9ef04 bytes 00080054
- 00b9ef94 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b9ef94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 00b9ef94 bytes ac0200f9
- 00b9ef98 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00b9ef98 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b9ef98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b9ef98 bytes 4b010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66addf5a1e72b6980d5dfea8260048f9"></a>

### [`00b9f2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f2bc.md) → [`00c1bd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEcRKNS_12basic_stringIcS3_NS_9allocatorIc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00436790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436790.md) [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.42% / 新版 88.42%

CFGの説明率　旧版 61.11% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1bd54",
      "incomplete_value": true,
      "site": "00c1bd54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9f30c",
      "incomplete_value": true,
      "site": "00b9f30c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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
      "definition_site": "00c1bd5c",
      "incomplete_value": true,
      "site": "00c1bd60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00b9f314",
      "incomplete_value": true,
      "site": "00b9f318",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f388"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1bd4c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1bd54",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1bd58",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1bd4c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c1bd54",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1bd58",
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9f318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f2bc.md#insn-00b9f318) · [`00b9f340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f2bc.md#insn-00b9f340) · [`00b9f388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f2bc.md#insn-00b9f388)
- 新版 [`00c1bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md#insn-00c1bd60) · [`00c1bd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md#insn-00c1bd88)

~~~diff
- 00b9f318 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c1bd60 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b9f318 bytes 60010054
+ 00c1bd60 bytes 60010054
- 00b9f340 ["INT_ADD", "register:40f0:8", ["const:b9f340:8", "const:4:8"]]
- 00b9f340 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c1bd88 ["INT_ADD", "register:40f0:8", ["const:c1bd88:8", "const:4:8"]]
+ 00c1bd88 ["CALL", null, ["callee:00c5dae0:8"]]
- 00b9f340 bytes e8060194
+ 00c1bd88 bytes 56070194
- 00b9f388 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9f388 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b9f388 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b9f388 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:1:8"]]
- 00b9f388 bytes 2915969a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42830727a030c0a0e7e84c1346efcfa0"></a>

### [`00b9f640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f640.md) → [`00c1c088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwe

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.40% / 新版 74.40%

CFGの説明率　旧版 41.07% / 新版 32.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `call_target` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9f658",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9f674",
      "PARAM",
      [
        "storage",
        "002a1124",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b9f688",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1c0a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c1c0bc",
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      "00c1c0d0",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9f658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f640.md#insn-00b9f658) · [`00b9f688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f640.md#insn-00b9f688) · [`00b9f68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9f640.md#insn-00b9f68c)

~~~diff
- 00b9f658 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b9f658 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9f658 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b9f658 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9f658 bytes f44f05a9
- 00b9f688 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9f688 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff88:8"]]
- 00b9f688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b9f688 bytes a88318f8
- 00b9f68c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b9f68c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9f68c bytes e013803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79454f4aba1a813da04ac3dcc1107617"></a>

### [`00b9faf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9faf8.md) → [`00c1c540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c540.md) _ZNSt6__ndk111__money_putIwE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERwS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocat

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1720.md) · 呼出先 4件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 1件 [`00c5e310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e310.md) · 呼出先 4件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.20% / 新版 81.20%

CFGの説明率　旧版 19.23% / 新版 15.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c590",
      "incomplete_value": true,
      "site": "00c1c590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9fb48",
      "incomplete_value": true,
      "site": "00b9fb48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:db8:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9fb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9fb68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1c58c",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1c590",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b9fb4c",
      "READ",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1c58c",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1c590",
      "DATA",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1c594",
      "READ",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9fb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9faf8.md#insn-00b9fb54) · [`00b9fb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9faf8.md#insn-00b9fb64) · [`00b9fb68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9faf8.md#insn-00b9fb68)

~~~diff
- 00b9fb54 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b9fb54 bytes 00030054
- 00b9fb64 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b9fb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9fb64 bytes e80300f9
- 00b9fb68 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:18:8"]]
- 00b9fb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b9fb68 bytes a90f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c5d4f9bb72698a8a947e1a7453b2099"></a>

### [`00ba01a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md) → [`00c1cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.59% / 新版 69.59%

CFGの説明率　旧版 25.00% / 新版 9.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_condition` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba01b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba01b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba01b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba01b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba01b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba01bc",
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
      "00c1cbfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c1cc00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c1cc04",
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

- 旧版 [`00ba01b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md#insn-00ba01b4) · [`00ba01b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md#insn-00ba01b8) · [`00ba01bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md#insn-00ba01bc)

~~~diff
- 00ba01b4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba01b4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba01b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba01b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba01b4 bytes f85f03a9
- 00ba01b8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba01b8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba01b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ba01b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba01b8 bytes f65704a9
- 00ba01bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba01bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba01bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba01bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba01bc bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d1a5e5e27f02d582370f3bb99d41d03"></a>

### [`00ba0538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0538.md) → [`00c1cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cf80.md) _ZNKSt6__ndk18messagesIcE7do_openERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-f5852408dce706648edd17e60f97ec53"></a>

### [`00ba0544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0544.md) → [`00c1cf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cf8c.md) _ZNKSt6__ndk18messagesIcE6do_getEliiRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0544.md#insn-00ba054c)
- 新版 [`00c1cf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cf8c.md#insn-00c1cf94)

~~~diff
- 00ba054c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00ba054c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba054c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba054c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c1cf94 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00c1cf94 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c1cf94 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c1cf94 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba054c bytes c9000037
+ 00c1cf94 bytes c9000037
~~~


<a id="compare-1046c56fa52c5036f73737e2a613f082"></a>

### [`00ba05f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05f4.md) → [`00c1d03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d03c.md) _ZNSt6__ndk114codecvt_bynameIwc9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1760.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e350.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05f4.md#insn-00ba0608)
- 新版 [`00c1d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d03c.md#insn-00c1d050)

~~~diff
- 00ba0608 ["INT_ADD", "register:40f0:8", ["const:ba0608:8", "const:4:8"]]
- 00ba0608 ["CALL", null, ["callee:00c5e350:8"]]
+ 00c1d050 ["INT_ADD", "register:40f0:8", ["const:c1d050:8", "const:4:8"]]
+ 00c1d050 ["CALL", null, ["callee:00c5e350:8"]]
- 00ba0608 bytes 56040194
+ 00c1d050 bytes c0040194
~~~


<a id="compare-1e50314069e16476aca46fc3ceb32eb4"></a>

### [`00ba0628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0628.md) → [`00c1d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d070.md) _ZNSt6__ndk114codecvt_bynameIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e370.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00c1d084",
      "value": [
        "leaf",
        "ram:c5e370:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ba063c",
      "value": [
        "leaf",
        "ram:be1780:8"
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
      "00c1d084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1780"
      ]
    ]
  ],
  "added": [
    [
      "00c1d084",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e370"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0628.md#insn-00ba063c)
- 新版 [`00c1d084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d070.md#insn-00c1d084)

~~~diff
- 00ba063c ["INT_ADD", "register:40f0:8", ["const:ba063c:8", "const:4:8"]]
- 00ba063c ["CALL", null, ["ram:be1780:8"]]
+ 00c1d084 ["INT_ADD", "register:40f0:8", ["const:c1d084:8", "const:4:8"]]
+ 00c1d084 ["CALL", null, ["ram:c5e370:8"]]
- 00ba063c bytes 51040194
+ 00c1d084 bytes bb040194
~~~


<a id="compare-bb1df1f7f4f45b2463af1321393114ce"></a>

### [`00ba065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba065c.md) → [`00c1d0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0a4.md) _ZNSt6__ndk114codecvt_bynameIDic9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e390.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba0670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba065c.md#insn-00ba0670)
- 新版 [`00c1d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0a4.md#insn-00c1d0b8)

~~~diff
- 00ba0670 ["INT_ADD", "register:40f0:8", ["const:ba0670:8", "const:4:8"]]
- 00ba0670 ["CALL", null, ["callee:00c5e390:8"]]
+ 00c1d0b8 ["INT_ADD", "register:40f0:8", ["const:c1d0b8:8", "const:4:8"]]
+ 00c1d0b8 ["CALL", null, ["callee:00c5e390:8"]]
- 00ba0670 bytes 4c040194
+ 00c1d0b8 bytes b6040194
~~~


<a id="compare-9f466471bcb7cdcf9be7e651d951d1a1"></a>

### [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) → [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) FUN_00c1d274

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba2cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md) · 呼出先 12件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c1f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) · 呼出先 12件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 9.74% / 新版 9.74%

CFGの説明率　旧版 0.82% / 新版 0.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 172件, `unresolved_call_alignment` 138件, `unresolved_store_alignment` 212件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 10件, `store_condition` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba0868",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba08d8",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba08e0",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1d2b0",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1d320",
      "READ",
      [
        "storage",
        "00c9b7f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d328",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba0868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md#insn-00ba0868) · [`00ba0880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md#insn-00ba0880) · [`00ba088c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md#insn-00ba088c)

~~~diff
- 00ba0868 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba0868 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba0868 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba0868 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba0868 bytes 092000a9
- 00ba0880 ["INT_ADD", "register:40c8:8", ["register:40c8:8", "const:28:8"]]
- 00ba0880 ["STORE", null, ["const:1b1:8", "register:40c8:8", "register:5000:16"]]
- 00ba0880 bytes 208f823c
- 00ba088c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ba088c ["INT_ADD", "register:4098:8", ["register:4098:8", "const:10:8"]]
- 00ba088c ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00ba088c bytes 790e01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e9cf97178d82dceb60b3d37d355624"></a>

### [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) → [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) FUN_00c1f064

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba808c.md) [`00ba81c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md)
- 新版 呼出元 2件 [`00c24ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md) [`00c24c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md) · 呼出先 43件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.05% / 新版 69.05%

CFGの説明率　旧版 30.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f094",
      "incomplete_value": false,
      "site": "00c1f094",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba264c",
      "incomplete_value": false,
      "site": "00ba264c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba27f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba27f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1f094",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1f124",
      "READ",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ba26e4",
      "READ",
      [
        "storage",
        "010a2ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1f094",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1f124",
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1f12c",
      "READ",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba27f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md#insn-00ba27f8) · [`00ba2864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md#insn-00ba2864) · [`00ba288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md#insn-00ba288c)

~~~diff
- 00ba27f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba27f8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba27f8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba27f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba27f8 bytes 282400a9
- 00ba2864 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba2864 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba2864 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba2864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2864 bytes 282400a9
- 00ba288c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba288c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba288c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba288c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba288c bytes 282400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da363082d87d1e515d1657d30e213be0"></a>

### [`00ba2cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md) → [`00c1f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) _ZNSt6__ndk16locale7classicEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be18d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18d0.md) · 呼出先 3件 [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c5e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4c0.md) · 呼出先 3件 [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 34.48% / 新版 34.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1f784"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2cf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2cec",
      "READ",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ba2cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1f754"
      ]
    ],
    [
      "unmatched:00ba2cf8",
      "DATA",
      [
        "storage",
        "010a2ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1f734",
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1f738",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1f754"
      ]
    ],
    [
      "00c1f740",
      "DATA",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md#insn-00ba2cf0) · [`00ba2d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md#insn-00ba2d14) · [`00ba2d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2cd4.md#insn-00ba2d18)

~~~diff
- 00ba2cf0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ba2cf0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba2cf0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba2cf0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ba2cf0 bytes e8000036
- 00ba2d14 ["INT_ADD", "register:40f0:8", ["const:ba2d14:8", "const:4:8"]]
- 00ba2d14 ["CALL", null, ["callee:00c57a50:8"]]
- 00ba2d14 bytes bbe00094
- 00ba2d18 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00ba2d18 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00ba2d18 bytes e0feff34
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6038c286989147e47266312313297a4"></a>

### [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) → [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) FUN_00c1f7a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 50.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1f7d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2d94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2d84",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba2d88",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba2d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1f7cc",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ],
    [
      "00c1f7d0",
      "DATA",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1f7d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md#insn-00ba2d88) · [`00ba2d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md#insn-00ba2d94) · [`00ba2dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md#insn-00ba2dbc)
- 新版 [`00c1f804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md#insn-00c1f804)

~~~diff
- 00ba2d88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba2d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba2d88 bytes f40700f9
- 00ba2d94 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba2d94 bytes 60010054
- 00ba2dbc ["INT_ADD", "register:40f0:8", ["const:ba2dbc:8", "const:4:8"]]
- 00ba2dbc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c1f804 ["INT_ADD", "register:40f0:8", ["const:c1f804:8", "const:4:8"]]
+ 00c1f804 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba2dbc bytes 49f80094
+ 00c1f804 bytes b7f80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e745288d7a86efc81d388e0f1719ef24"></a>

### [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) → [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) FUN_00c1f8d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 18.75% / 新版 15.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1f8fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2ec0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2eb0",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba2eb4",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba2eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1f8f8",
      "READ",
      [
        "storage",
        "00c9b808",
        null,
        "pointer"
      ]
    ],
    [
      "00c1f8fc",
      "DATA",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1f8fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md#insn-00ba2eb4) · [`00ba2ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md#insn-00ba2ec0) · [`00ba2ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md#insn-00ba2ee8)
- 新版 [`00c1f930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md#insn-00c1f930)

~~~diff
- 00ba2eb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba2eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba2eb4 bytes f40700f9
- 00ba2ec0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba2ec0 bytes 60010054
- 00ba2ee8 ["INT_ADD", "register:40f0:8", ["const:ba2ee8:8", "const:4:8"]]
- 00ba2ee8 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c1f930 ["INT_ADD", "register:40f0:8", ["const:c1f930:8", "const:4:8"]]
+ 00c1f930 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba2ee8 bytes fef70094
+ 00c1f930 bytes 6cf80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6355efd197355cf7062a4fc5b418f82b"></a>

### [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) → [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) FUN_00c1fa00

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.02% / 新版 73.02%

CFGの説明率　旧版 50.00% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba2fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba2fc8",
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
      "00c1fa08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c1fa0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c1fa10",
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

- 旧版 [`00ba2fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md#insn-00ba2fc0) · [`00ba2fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md#insn-00ba2fc4) · [`00ba2fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md#insn-00ba2fc8)

~~~diff
- 00ba2fc0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba2fc0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba2fc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba2fc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2fc0 bytes fd7b02a9
- 00ba2fc4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba2fc4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba2fc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba2fc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2fc4 bytes f65703a9
- 00ba2fc8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba2fc8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba2fc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ba2fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2fc8 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e534f15c9571f690a0ab4988f00ad46"></a>

### [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md) → [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md) FUN_00c1fb2c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba310c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3134"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3108",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba310c",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba310c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1fb50",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fb54",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba310c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md#insn-00ba310c) · [`00ba3118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md#insn-00ba3118) · [`00ba3128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md#insn-00ba3128)

~~~diff
- 00ba310c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba310c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba310c bytes f40700f9
- 00ba3118 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3118 bytes 60010054
- 00ba3128 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba3128 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ba3128 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ba3128 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d3522b4ea3d8687d48c7f4febac5a3"></a>

### [`00ba3210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3210.md) → [`00c1fc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md) FUN_00c1fc58

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1fc80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3234",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3238",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3238",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1fc7c",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fc80",
      "DATA",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fc80",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3210.md#insn-00ba3238) · [`00ba3244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3210.md#insn-00ba3244) · [`00ba326c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3210.md#insn-00ba326c)
- 新版 [`00c1fcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md#insn-00c1fcb4)

~~~diff
- 00ba3238 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3238 bytes f40700f9
- 00ba3244 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3244 bytes 60010054
- 00ba326c ["INT_ADD", "register:40f0:8", ["const:ba326c:8", "const:4:8"]]
- 00ba326c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c1fcb4 ["INT_ADD", "register:40f0:8", ["const:c1fcb4:8", "const:4:8"]]
+ 00c1fcb4 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba326c bytes 1df70094
+ 00c1fcb4 bytes 8bf70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41e3bb2558f8b8fa20c50228cdb7961"></a>

### [`00ba333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba333c.md) → [`00c1fd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md) FUN_00c1fd84

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1fdac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3360",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3364",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3364",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1fda8",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fdac",
      "DATA",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fdac",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba333c.md#insn-00ba3364) · [`00ba3370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba333c.md#insn-00ba3370) · [`00ba3398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba333c.md#insn-00ba3398)
- 新版 [`00c1fde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md#insn-00c1fde0)

~~~diff
- 00ba3364 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3364 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3364 bytes f40700f9
- 00ba3370 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3370 bytes 60010054
- 00ba3398 ["INT_ADD", "register:40f0:8", ["const:ba3398:8", "const:4:8"]]
- 00ba3398 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c1fde0 ["INT_ADD", "register:40f0:8", ["const:c1fde0:8", "const:4:8"]]
+ 00c1fde0 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3398 bytes d2f60094
+ 00c1fde0 bytes 40f70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e512933b54e1001b577398aca05d1560"></a>

### [`00ba3468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3468.md) → [`00c1feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md) FUN_00c1feb0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.60% / 新版 74.60%

CFGの説明率　旧版 68.75% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3490"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba34ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba34b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba348c",
      "READ",
      [
        "storage",
        "00c1bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3490",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3490",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1fed4",
      "READ",
      [
        "storage",
        "00c9b828",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fed8",
      "DATA",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3468.md#insn-00ba3490) · [`00ba349c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3468.md#insn-00ba349c) · [`00ba34ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3468.md#insn-00ba34ac)

~~~diff
- 00ba3490 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3490 bytes f40700f9
- 00ba349c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba349c bytes 60010054
- 00ba34ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba34ac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ba34ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ba34ac bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e95a8b2d27c264d99bc05d88350add58"></a>

### [`00ba3594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md) → [`00c1ffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md) FUN_00c1ffdc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba35bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba35d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba35e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba35b8",
      "READ",
      [
        "storage",
        "00c1be08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba35bc",
      "DATA",
      [
        "storage",
        "010a2b60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba35bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20000",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00c20004",
      "DATA",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20004",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba35bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md#insn-00ba35bc) · [`00ba35c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md#insn-00ba35c8) · [`00ba35d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3594.md#insn-00ba35d8)

~~~diff
- 00ba35bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba35bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba35bc bytes f40700f9
- 00ba35c8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba35c8 bytes 60010054
- 00ba35d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba35d8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ba35d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ba35d8 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd6fc00e68116ee635c40728e7148cb6"></a>

### [`00ba36c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba36c0.md) → [`00c20108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md) FUN_00c20108

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba36e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20130"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba36f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba36e4",
      "READ",
      [
        "storage",
        "00c1be18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba36e8",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba36e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2012c",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c20130",
      "DATA",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20130",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba36e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba36c0.md#insn-00ba36e8) · [`00ba36f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba36c0.md#insn-00ba36f4) · [`00ba371c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba36c0.md#insn-00ba371c)
- 新版 [`00c20164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md#insn-00c20164)

~~~diff
- 00ba36e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba36e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba36e8 bytes f40700f9
- 00ba36f4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba36f4 bytes 60010054
- 00ba371c ["INT_ADD", "register:40f0:8", ["const:ba371c:8", "const:4:8"]]
- 00ba371c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20164 ["INT_ADD", "register:40f0:8", ["const:c20164:8", "const:4:8"]]
+ 00c20164 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba371c bytes f1f50094
+ 00c20164 bytes 5ff60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b641980917b9ed822be71892f51f50"></a>

### [`00ba37ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba37ec.md) → [`00c20234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md) FUN_00c20234

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2025c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3810",
      "READ",
      [
        "storage",
        "00c1be28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3814",
      "DATA",
      [
        "storage",
        "010a2b70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3814",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20258",
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      "00c2025c",
      "DATA",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2025c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba37ec.md#insn-00ba3814) · [`00ba3820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba37ec.md#insn-00ba3820) · [`00ba3848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba37ec.md#insn-00ba3848)
- 新版 [`00c20290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md#insn-00c20290)

~~~diff
- 00ba3814 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3814 bytes f40700f9
- 00ba3820 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3820 bytes 60010054
- 00ba3848 ["INT_ADD", "register:40f0:8", ["const:ba3848:8", "const:4:8"]]
- 00ba3848 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20290 ["INT_ADD", "register:40f0:8", ["const:c20290:8", "const:4:8"]]
+ 00c20290 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3848 bytes a6f50094
+ 00c20290 bytes 14f60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bfd77707f50fdc297a611c1f182ac05"></a>

### [`00ba3918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3918.md) → [`00c20360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md) FUN_00c20360

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20388"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba394c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba393c",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3940",
      "DATA",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3940",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20384",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20388",
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20388",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3918.md#insn-00ba3940) · [`00ba394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3918.md#insn-00ba394c) · [`00ba3974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3918.md#insn-00ba3974)
- 新版 [`00c203bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md#insn-00c203bc)

~~~diff
- 00ba3940 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3940 bytes f40700f9
- 00ba394c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba394c bytes 60010054
- 00ba3974 ["INT_ADD", "register:40f0:8", ["const:ba3974:8", "const:4:8"]]
- 00ba3974 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c203bc ["INT_ADD", "register:40f0:8", ["const:c203bc:8", "const:4:8"]]
+ 00c203bc ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3974 bytes 5bf50094
+ 00c203bc bytes c9f50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a648ed232849af67a47585bb96ebd543"></a>

### [`00ba3a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3a44.md) → [`00c2048c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md) FUN_00c2048c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c204b0",
      "incomplete_value": true,
      "site": "00c204b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3a68",
      "incomplete_value": true,
      "site": "00ba3a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c204bc",
      "incomplete_value": true,
      "site": "00c204c0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba3a74",
      "incomplete_value": true,
      "site": "00ba3a78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c204e4",
      "incomplete_value": true,
      "site": "00c204e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3a9c",
      "incomplete_value": true,
      "site": "00ba3aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "00c204b0",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c204b4",
      "DATA",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c204b8",
      "READ",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c204b0",
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c204b4",
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c204b8",
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3a44.md#insn-00ba3aa0) · [`00ba3a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3a44.md#insn-00ba3a5c) · [`00ba3a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3a44.md#insn-00ba3a68)
- 新版 [`00c204e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204e8) · [`00c204a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204a4) · [`00c204b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204b0)

~~~diff
- 00ba3aa0 ["INT_ADD", "register:40f0:8", ["const:ba3aa0:8", "const:4:8"]]
- 00ba3aa0 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c204e8 ["INT_ADD", "register:40f0:8", ["const:c204e8:8", "const:4:8"]]
+ 00c204e8 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3aa0 bytes 10f50094
+ 00c204e8 bytes 7ef50094
- 00ba3a5c ["COPY", "register:40a0:8", ["const:c1b000:8"]]
+ 00c204a4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00ba3a5c bytes d4030090
+ 00c204a4 bytes d40300f0
- 00ba3a68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00ba3a68 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c204b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00c204b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3a68 bytes 94ce46f9
+ 00c204b0 bytes 94e643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e22faf7bc783af0469a446596dab38"></a>

### [`00ba3b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3b70.md) → [`00c205b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md) FUN_00c205b8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3b98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c205e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3ba4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3b94",
      "READ",
      [
        "storage",
        "00c1bdb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3b98",
      "DATA",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3b98",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c205dc",
      "READ",
      [
        "storage",
        "00c9b7e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c205e0",
      "DATA",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c205e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3b70.md#insn-00ba3b98) · [`00ba3ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3b70.md#insn-00ba3ba4) · [`00ba3bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3b70.md#insn-00ba3bcc)
- 新版 [`00c20614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md#insn-00c20614)

~~~diff
- 00ba3b98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3b98 bytes f40700f9
- 00ba3ba4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3ba4 bytes 60010054
- 00ba3bcc ["INT_ADD", "register:40f0:8", ["const:ba3bcc:8", "const:4:8"]]
- 00ba3bcc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20614 ["INT_ADD", "register:40f0:8", ["const:c20614:8", "const:4:8"]]
+ 00c20614 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3bcc bytes c5f40094
+ 00c20614 bytes 33f50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd3f7044a076baa3fa849c5d7549393"></a>

### [`00ba3c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3c9c.md) → [`00c206e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md) FUN_00c206e4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be18e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18e0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20714",
      "incomplete_value": true,
      "site": "00c20714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ba3ccc",
      "incomplete_value": true,
      "site": "00ba3ccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00c20704",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00c20714",
      "DATA",
      [
        "storage",
        "00c15658",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20704",
      "READ",
      [
        "storage",
        "00c9b998",
        null,
        "pointer"
      ]
    ],
    [
      "00c20714",
      "DATA",
      [
        "storage",
        "00c95000",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3c9c.md#insn-00ba3cb0) · [`00ba3cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3c9c.md#insn-00ba3cbc) · [`00ba3cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3c9c.md#insn-00ba3cc0)
- 新版 [`00c206f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md#insn-00c206f8) · [`00c20704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md#insn-00c20704)

~~~diff
- 00ba3cb0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c206f8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00ba3cb0 bytes c8030090
+ 00c206f8 bytes c80300f0
- 00ba3cbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
- 00ba3cbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
+ 00c20704 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3cbc bytes 08b547f9
+ 00c20704 bytes 08cd44f9
- 00ba3cc0 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba3cc0 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f56e2104687f3660798c86bf13e15b40"></a>

### [`00ba3d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3d80.md) → [`00c207c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md) FUN_00c207c8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3da8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c207f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3da4",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3da8",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3da8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c207ec",
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c207f0",
      "DATA",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c207f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3d80.md#insn-00ba3da8) · [`00ba3db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3d80.md#insn-00ba3db4) · [`00ba3ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3d80.md#insn-00ba3ddc)
- 新版 [`00c20824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md#insn-00c20824)

~~~diff
- 00ba3da8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3da8 bytes f40700f9
- 00ba3db4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3db4 bytes 60010054
- 00ba3ddc ["INT_ADD", "register:40f0:8", ["const:ba3ddc:8", "const:4:8"]]
- 00ba3ddc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20824 ["INT_ADD", "register:40f0:8", ["const:c20824:8", "const:4:8"]]
+ 00c20824 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3ddc bytes 41f40094
+ 00c20824 bytes aff40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ab0c5dfcfa1db8f14051fc7cc0b360"></a>

### [`00ba3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3f90.md) → [`00c209d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md) FUN_00c209d8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20a00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3fb4",
      "READ",
      [
        "storage",
        "00c1bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3fb8",
      "DATA",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba3fb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c209fc",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20a00",
      "DATA",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20a00",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3f90.md#insn-00ba3fb8) · [`00ba3fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3f90.md#insn-00ba3fc4) · [`00ba3fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3f90.md#insn-00ba3fec)
- 新版 [`00c20a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md#insn-00c20a34)

~~~diff
- 00ba3fb8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba3fb8 bytes f40700f9
- 00ba3fc4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba3fc4 bytes 60010054
- 00ba3fec ["INT_ADD", "register:40f0:8", ["const:ba3fec:8", "const:4:8"]]
- 00ba3fec ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20a34 ["INT_ADD", "register:40f0:8", ["const:c20a34:8", "const:4:8"]]
+ 00c20a34 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba3fec bytes bdf30094
+ 00c20a34 bytes 2bf40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed8dca480fe74b66df6a698fe22a723"></a>

### [`00ba40bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba40bc.md) → [`00c20b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md) FUN_00c20b04

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be1900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1900.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20b34",
      "incomplete_value": true,
      "site": "00c20b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ba40ec",
      "incomplete_value": true,
      "site": "00ba40ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00c20b24",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00c20b34",
      "DATA",
      [
        "storage",
        "00c15768",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20b24",
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20b34",
      "DATA",
      [
        "storage",
        "00c95110",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba40d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba40bc.md#insn-00ba40d0) · [`00ba40dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba40bc.md#insn-00ba40dc) · [`00ba40e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba40bc.md#insn-00ba40e0)
- 新版 [`00c20b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md#insn-00c20b18) · [`00c20b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md#insn-00c20b24)

~~~diff
- 00ba40d0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c20b18 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00ba40d0 bytes a80300f0
+ 00c20b18 bytes c80300f0
- 00ba40dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
- 00ba40dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
+ 00c20b24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba40dc bytes 08bd47f9
+ 00c20b24 bytes 08d544f9
- 00ba40e0 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba40e0 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f0767cb88ae812e15110b82b04ddc6"></a>

### [`00ba41a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba41a0.md) → [`00c20be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md) FUN_00c20be8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 62.50% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba41c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20c10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba41d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba41c4",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba41c8",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba41c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20c0c",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20c10",
      "DATA",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba41c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba41a0.md#insn-00ba41c8) · [`00ba41d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba41a0.md#insn-00ba41d4) · [`00ba41fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba41a0.md#insn-00ba41fc)
- 新版 [`00c20c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md#insn-00c20c44)

~~~diff
- 00ba41c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba41c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba41c8 bytes f40700f9
- 00ba41d4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba41d4 bytes 60010054
- 00ba41fc ["INT_ADD", "register:40f0:8", ["const:ba41fc:8", "const:4:8"]]
- 00ba41fc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20c44 ["INT_ADD", "register:40f0:8", ["const:c20c44:8", "const:4:8"]]
+ 00c20c44 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba41fc bytes 39f30094
+ 00c20c44 bytes a7f30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d807145bec4f6d14002b50a3c1dfe32"></a>

### [`00ba42cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba42cc.md) → [`00c20d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md) FUN_00c20d14

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be1910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1910.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e500.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20d44",
      "incomplete_value": true,
      "site": "00c20d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ba42fc",
      "incomplete_value": true,
      "site": "00ba42fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00c20d34",
      "READ",
      [
        "storage",
        "00c1bf80",
        null,
        "pointer"
      ]
    ],
    [
      "00c20d44",
      "DATA",
      [
        "storage",
        "00c157f0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20d34",
      "READ",
      [
        "storage",
        "00c9b9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20d44",
      "DATA",
      [
        "storage",
        "00c95198",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba42e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba42cc.md#insn-00ba42e0) · [`00ba42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba42cc.md#insn-00ba42ec) · [`00ba42f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba42cc.md#insn-00ba42f0)
- 新版 [`00c20d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md#insn-00c20d28) · [`00c20d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md#insn-00c20d34)

~~~diff
- 00ba42e0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c20d28 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00ba42e0 bytes a80300f0
+ 00c20d28 bytes c80300f0
- 00ba42ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
- 00ba42ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
+ 00c20d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba42ec bytes 08c147f9
+ 00c20d34 bytes 08d944f9
- 00ba42f0 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba42f0 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963c46efe76b6b4aabf640be8694089c"></a>

### [`00ba43b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba43b0.md) → [`00c20df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md) FUN_00c20df8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 68.75% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba43d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20e20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba43e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba43d4",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba43d8",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba43d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20e1c",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20e20",
      "DATA",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20e20",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba43d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba43b0.md#insn-00ba43d8) · [`00ba43e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba43b0.md#insn-00ba43e4) · [`00ba440c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba43b0.md#insn-00ba440c)
- 新版 [`00c20e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md#insn-00c20e54)

~~~diff
- 00ba43d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba43d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba43d8 bytes f40700f9
- 00ba43e4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba43e4 bytes 60010054
- 00ba440c ["INT_ADD", "register:40f0:8", ["const:ba440c:8", "const:4:8"]]
- 00ba440c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20e54 ["INT_ADD", "register:40f0:8", ["const:c20e54:8", "const:4:8"]]
+ 00c20e54 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba440c bytes b5f20094
+ 00c20e54 bytes 23f30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1095b07fbad0683074bf99bb0208ab6"></a>

### [`00ba44dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba44dc.md) → [`00c20f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md) FUN_00c20f24

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20f4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4510"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba4500",
      "READ",
      [
        "storage",
        "00c1bec0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba4504",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba4504",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c20f48",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20f4c",
      "DATA",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20f4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba44dc.md#insn-00ba4504) · [`00ba4510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba44dc.md#insn-00ba4510) · [`00ba4538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba44dc.md#insn-00ba4538)
- 新版 [`00c20f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md#insn-00c20f80)

~~~diff
- 00ba4504 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba4504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba4504 bytes f40700f9
- 00ba4510 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba4510 bytes 60010054
- 00ba4538 ["INT_ADD", "register:40f0:8", ["const:ba4538:8", "const:4:8"]]
- 00ba4538 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c20f80 ["INT_ADD", "register:40f0:8", ["const:c20f80:8", "const:4:8"]]
+ 00c20f80 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba4538 bytes 6af20094
+ 00c20f80 bytes d8f20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbcca10fa1b72de8d368c3c099aed4aa"></a>

### [`00ba4608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4608.md) → [`00c21050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md) FUN_00c21050

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 62.50% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c21078"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba463c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba462c",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba4630",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba4630",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c21074",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21078",
      "DATA",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21078",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4608.md#insn-00ba4630) · [`00ba463c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4608.md#insn-00ba463c) · [`00ba4664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4608.md#insn-00ba4664)
- 新版 [`00c210ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md#insn-00c210ac)

~~~diff
- 00ba4630 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba4630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba4630 bytes f40700f9
- 00ba463c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba463c bytes 60010054
- 00ba4664 ["INT_ADD", "register:40f0:8", ["const:ba4664:8", "const:4:8"]]
- 00ba4664 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c210ac ["INT_ADD", "register:40f0:8", ["const:c210ac:8", "const:4:8"]]
+ 00c210ac ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba4664 bytes 1ff20094
+ 00c210ac bytes 8df20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaae247ce530dd1afd08d2ad611d1a3"></a>

### [`00ba4734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4734.md) → [`00c2117c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md) FUN_00c2117c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba475c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c211a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba4758",
      "READ",
      [
        "storage",
        "00c1bee0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba475c",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba475c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c211a0",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00c211a4",
      "DATA",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c211a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba475c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4734.md#insn-00ba475c) · [`00ba4768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4734.md#insn-00ba4768) · [`00ba4790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4734.md#insn-00ba4790)
- 新版 [`00c211d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md#insn-00c211d8)

~~~diff
- 00ba475c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba475c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba475c bytes f40700f9
- 00ba4768 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba4768 bytes 60010054
- 00ba4790 ["INT_ADD", "register:40f0:8", ["const:ba4790:8", "const:4:8"]]
- 00ba4790 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c211d8 ["INT_ADD", "register:40f0:8", ["const:c211d8:8", "const:4:8"]]
+ 00c211d8 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba4790 bytes d4f10094
+ 00c211d8 bytes 42f20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af1c49814dcf34a306d0b18f5b460fdb"></a>

### [`00ba4860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4860.md) → [`00c212a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md) FUN_00c212a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c212d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4894"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba4884",
      "READ",
      [
        "storage",
        "00c1bef0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba4888",
      "DATA",
      [
        "storage",
        "010a2970",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba4888",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c212cc",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      "00c212d0",
      "DATA",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c212d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4860.md#insn-00ba4888) · [`00ba4894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4860.md#insn-00ba4894) · [`00ba48bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4860.md#insn-00ba48bc)
- 新版 [`00c21304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md#insn-00c21304)

~~~diff
- 00ba4888 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba4888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba4888 bytes f40700f9
- 00ba4894 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba4894 bytes 60010054
- 00ba48bc ["INT_ADD", "register:40f0:8", ["const:ba48bc:8", "const:4:8"]]
- 00ba48bc ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c21304 ["INT_ADD", "register:40f0:8", ["const:c21304:8", "const:4:8"]]
+ 00c21304 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba48bc bytes 89f10094
+ 00c21304 bytes f7f10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca0889194c2a1dae3cbc93fc9887e910"></a>

### [`00ba498c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba498c.md) → [`00c213d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md) FUN_00c213d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c213f8",
      "incomplete_value": true,
      "site": "00c213fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba49b0",
      "incomplete_value": true,
      "site": "00ba49b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21404",
      "incomplete_value": true,
      "site": "00c21408",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00ba49bc",
      "incomplete_value": true,
      "site": "00ba49c0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2142c",
      "incomplete_value": true,
      "site": "00c21430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba49e4",
      "incomplete_value": true,
      "site": "00ba49e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
      "00c213f8",
      "READ",
      [
        "storage",
        "00c1bf00",
        null,
        "pointer"
      ]
    ],
    [
      "00c213fc",
      "DATA",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21400",
      "READ",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c213f8",
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      "00c213fc",
      "DATA",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21400",
      "READ",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba49e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba498c.md#insn-00ba49e8) · [`00ba49a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba498c.md#insn-00ba49a4) · [`00ba49b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba498c.md#insn-00ba49b0)
- 新版 [`00c21430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c21430) · [`00c213ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c213ec) · [`00c213f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c213f8)

~~~diff
- 00ba49e8 ["INT_ADD", "register:40f0:8", ["const:ba49e8:8", "const:4:8"]]
- 00ba49e8 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c21430 ["INT_ADD", "register:40f0:8", ["const:c21430:8", "const:4:8"]]
+ 00c21430 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba49e8 bytes 3ef10094
+ 00c21430 bytes acf10094
- 00ba49a4 ["COPY", "register:40a0:8", ["const:c1b000:8"]]
+ 00c213ec ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00ba49a4 bytes b40300f0
+ 00c213ec bytes d40300d0
- 00ba49b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
- 00ba49b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c213f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00c213f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba49b0 bytes 948247f9
+ 00c213f8 bytes 949a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02578d949b0a9ec45a5dcdc6dd28488c"></a>

### [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) → [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) FUN_00c21500

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba8230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8230.md) [`00ba8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md) · 呼出先 40件 [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md)
- 新版 呼出元 2件 [`00c24c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md) [`00c24dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md) · 呼出先 40件 [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.48% / 新版 77.48%

CFGの説明率　旧版 79.31% / 新版 71.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21534",
      "incomplete_value": false,
      "site": "00c21534",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4aec",
      "incomplete_value": false,
      "site": "00ba4aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4c7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21534",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "00c2164c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1840"
      ]
    ],
    [
      "unmatched:00ba4c50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1860"
      ]
    ]
  ],
  "added": [
    [
      "00c21534",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c2164c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e430"
      ]
    ],
    [
      "00c21698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md#insn-00ba4c7c) · [`00ba4ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md#insn-00ba4ce4) · [`00ba4d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md#insn-00ba4d0c)

~~~diff
- 00ba4c7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba4c7c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba4c7c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba4c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4c7c bytes 282400a9
- 00ba4ce4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba4ce4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba4ce4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba4ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4ce4 bytes 282400a9
- 00ba4d0c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba4d0c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba4d0c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00ba4d0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4d0c bytes 282400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7024d6175b5aa072f48f9e9d711a32"></a>

### [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) → [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) FUN_00c21b50

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba83f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md) · 呼出先 33件 [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) [`00ba546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md) [`00ba55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md) [`00ba56f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md) [`00ba5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md)
- 新版 呼出元 1件 [`00c24e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md) · 呼出先 33件 [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c21eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md) [`00c21ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md) [`00c2213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md) [`00c22280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 45.71% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c21b80"
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
      "unmatched:00ba5138",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ba51d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c21c5c"
      ]
    ]
  ],
  "added": [
    [
      "00c21b80",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c21c1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c21c5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md#insn-00ba5138) · [`00ba51d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md#insn-00ba51d4) · [`00ba5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md#insn-00ba5290)
- 新版 [`00c21cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md#insn-00c21cd8)

~~~diff
- 00ba5138 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba5138 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ba5138 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba5138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba5138 bytes 092000a9
- 00ba51d4 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00ba51d4 bytes 00020054
- 00ba5290 ["INT_ADD", "register:40f0:8", ["const:ba5290:8", "const:4:8"]]
- 00ba5290 ["CALL", null, ["callee:00c22a18:8"]]
+ 00c21cd8 ["INT_ADD", "register:40f0:8", ["const:c21cd8:8", "const:4:8"]]
+ 00c21cd8 ["CALL", null, ["callee:00c22a18:8"]]
- 00ba5290 bytes 50030094
+ 00c21cd8 bytes 50030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e188e70513b7d529349492786b113dc"></a>

### [`00ba546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md) → [`00c21eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md) FUN_00c21eb4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba54b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba54bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba5490",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba5494",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba5494",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c21ed8",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ],
    [
      "00c21edc",
      "DATA",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md#insn-00ba5494) · [`00ba54a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md#insn-00ba54a0) · [`00ba54b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md#insn-00ba54b0)

~~~diff
- 00ba5494 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba5494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba5494 bytes f40700f9
- 00ba54a0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba54a0 bytes 60010054
- 00ba54b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba54b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ba54b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ba54b0 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f0eec9f6e86686f8a3a69e5eeefb977"></a>

### [`00ba55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md) → [`00c21ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md) FUN_00c21ff8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.14% / 新版 87.14%

CFGの説明率　旧版 60.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba55d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c22020"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba55e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba55d4",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba55d8",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba55d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2201c",
      "READ",
      [
        "storage",
        "00c9b808",
        null,
        "pointer"
      ]
    ],
    [
      "00c22020",
      "DATA",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22020",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba55d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md#insn-00ba55d8) · [`00ba55e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md#insn-00ba55e4) · [`00ba560c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md#insn-00ba560c)
- 新版 [`00c22054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md#insn-00c22054)

~~~diff
- 00ba55d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba55d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba55d8 bytes f40700f9
- 00ba55e4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba55e4 bytes 60010054
- 00ba560c ["INT_ADD", "register:40f0:8", ["const:ba560c:8", "const:4:8"]]
- 00ba560c ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c22054 ["INT_ADD", "register:40f0:8", ["const:c22054:8", "const:4:8"]]
+ 00c22054 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba560c bytes 35ee0094
+ 00c22054 bytes a3ee0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af36eb85e1eab40325daf643ce8463cc"></a>

### [`00ba56f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md) → [`00c2213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md) FUN_00c2213c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 55.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba571c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c22164"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5728"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba5718",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba571c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba571c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c22160",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c22164",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22164",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba571c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md#insn-00ba571c) · [`00ba5728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md#insn-00ba5728) · [`00ba5750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md#insn-00ba5750)
- 新版 [`00c22198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md#insn-00c22198)

~~~diff
- 00ba571c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba571c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba571c bytes f40700f9
- 00ba5728 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba5728 bytes 60010054
- 00ba5750 ["INT_ADD", "register:40f0:8", ["const:ba5750:8", "const:4:8"]]
- 00ba5750 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c22198 ["INT_ADD", "register:40f0:8", ["const:c22198:8", "const:4:8"]]
+ 00c22198 ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba5750 bytes e4ed0094
+ 00c22198 bytes 52ee0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b8a8423397ea640e77acd888a8d3ba"></a>

### [`00ba5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md) → [`00c22280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md) FUN_00c22280

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 65.00% / 新版 61.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c222a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba586c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba585c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba5860",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00ba5860",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c222a4",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c222a8",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c222a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md#insn-00ba5860) · [`00ba586c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md#insn-00ba586c) · [`00ba5894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md#insn-00ba5894)
- 新版 [`00c222dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md#insn-00c222dc)

~~~diff
- 00ba5860 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba5860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ba5860 bytes f40700f9
- 00ba586c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ba586c bytes 60010054
- 00ba5894 ["INT_ADD", "register:40f0:8", ["const:ba5894:8", "const:4:8"]]
- 00ba5894 ["CALL", null, ["callee:00c5dae0:8"]]
+ 00c222dc ["INT_ADD", "register:40f0:8", ["const:c222dc:8", "const:4:8"]]
+ 00c222dc ["CALL", null, ["callee:00c5dae0:8"]]
- 00ba5894 bytes 93ed0094
+ 00c222dc bytes 01ee0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

