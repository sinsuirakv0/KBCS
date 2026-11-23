# v15.7.4 → v16.0.0 · 最優先の変更候補 (65)

[一覧の目次](README.md)

<a id="compare-a8bad74a334565dc9886bcd2674d3d72"></a>

### [`00b4f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md) → [`00bbd624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md) _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE

採用 · 移動量 `+0x6e52c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0550.md) · 呼出先 13件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d140.md) · 呼出先 13件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, branch_count, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, unresolved_call_alignment

命令の説明率　旧版 46.50% / 新版 47.43%

CFGの説明率　旧版 13.07% / 新版 14.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `branch_value` 1件, `call_argument_candidate` 17件, `call_target` 1件, `store_condition` 2件, `store_count` 1件, `unresolved_call_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f108"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f108"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f10c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4f108",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4f10c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4f118",
      "WRITE",
      [
        "storage",
        "Stack[-0x338]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbd634",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbd638",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bbd65c",
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

- 旧版 [`00b4f108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md#insn-00b4f108) · [`00b4f10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md#insn-00b4f10c) · [`00b4f118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md#insn-00b4f118)

~~~diff
- 00b4f108 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4f108 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4f108 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4f108 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4f108 bytes f44f04a9
- 00b4f10c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4f10c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4f10c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4f10c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4f10c bytes fd7b05a9
- 00b4f118 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b4f118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4f118 bytes e00700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b29aa455e2141227472f8b54e0c280f"></a>

### [`00b524ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524ec.md) → [`00bc0e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e50.md) _ZN8firebase13remote_config10FutureData6CreateEv

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc0e80",
      "incomplete_value": true,
      "site": "00bc0e80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5251c",
      "incomplete_value": true,
      "site": "00b5251c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc0e68",
      "incomplete_value": false,
      "site": "00bc0e6c",
      "value": [
        "leaf",
        "const:7:8"
      ]
    },
    "old": {
      "definition_site": "00b52504",
      "incomplete_value": false,
      "site": "00b52508",
      "value": [
        "leaf",
        "const:6:8"
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
      "00bc0e74",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0e80",
      "WRITE",
      [
        "storage",
        "010a1170",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc0e74",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0e80",
      "WRITE",
      [
        "storage",
        "01126030",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524ec.md#insn-00b52508) · [`00b524fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524ec.md#insn-00b524fc) · [`00b52504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524ec.md#insn-00b52504)
- 新版 `00bc0e6c`（命令位置の公開資料なし） · `00bc0e60`（命令位置の公開資料なし） · `00bc0e68`（命令位置の公開資料なし）

~~~diff
- 00b52508 ["INT_ADD", "register:40f0:8", ["const:b52508:8", "const:4:8"]]
- 00b52508 ["CALL", null, ["callee:00c5a840:8"]]
+ 00bc0e6c ["INT_ADD", "register:40f0:8", ["const:bc0e6c:8", "const:4:8"]]
+ 00bc0e6c ["CALL", null, ["callee:00c5a840:8"]]
- 00b52508 bytes 362e0294
+ 00bc0e6c bytes 75660294
- 00b524fc ["INT_ADD", "register:40f0:8", ["const:b524fc:8", "const:4:8"]]
- 00b524fc ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc0e60 ["INT_ADD", "register:40f0:8", ["const:bc0e60:8", "const:4:8"]]
+ 00bc0e60 ["CALL", null, ["callee:00c57a90:8"]]
- 00b524fc bytes d1220294
+ 00bc0e60 bytes 0c5b0294
- 00b52504 ["COPY", "register:4008:8", ["const:6:8"]]
+ 00bc0e68 ["COPY", "register:4008:8", ["const:7:8"]]
- 00b52504 bytes c1008052
+ 00bc0e68 bytes e1008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc74407f04fa3a8ab40efeaaa650dc57"></a>

### [`00b5253c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b5253c.md) → [`00bc0ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0ea0.md) _ZN8firebase13remote_config10FutureData7DestroyEv

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc0eb8",
      "incomplete_value": true,
      "site": "00bc0eb8",
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
              "LOAD"
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
      "definition_site": "00b52554",
      "incomplete_value": true,
      "site": "00b52554",
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
              "LOAD"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc0ec0",
      "value": [
        "leaf",
        "ram:c5a850:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5255c",
      "value": [
        "leaf",
        "ram:bdddf0:8"
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
      "00bc0eb0",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0eb4",
      "READ",
      [
        "storage",
        "010a1170",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00bc0ec0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdddf0"
      ]
    ]
  ],
  "added": [
    [
      "00bc0eb0",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0eb4",
      "READ",
      [
        "storage",
        "01126030",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00bc0ec0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a850"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5255c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b5253c.md#insn-00b5255c) · [`00b52548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b5253c.md#insn-00b52548) · [`00b5254c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b5253c.md#insn-00b5254c)
- 新版 `00bc0ec0`（命令位置の公開資料なし） · `00bc0eac`（命令位置の公開資料なし） · `00bc0eb0`（命令位置の公開資料なし）

~~~diff
- 00b5255c ["INT_ADD", "register:40f0:8", ["const:b5255c:8", "const:4:8"]]
- 00b5255c ["CALL", null, ["ram:bdddf0:8"]]
+ 00bc0ec0 ["INT_ADD", "register:40f0:8", ["const:bc0ec0:8", "const:4:8"]]
+ 00bc0ec0 ["CALL", null, ["ram:c5a850:8"]]
- 00b5255c bytes 252e0294
+ 00bc0ec0 bytes 64660294
- 00b52548 ["COPY", "register:40a0:8", ["const:c1b000:8"]]
+ 00bc0eac ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00b52548 bytes 540600b0
+ 00bc0eac bytes d40600f0
- 00b5254c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
- 00b5254c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc0eb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:518:8"]]
+ 00bc0eb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5254c bytes 947645f9
+ 00bc0eb0 bytes 948e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-909668c482a5af66ba4b7b30e404ba0b"></a>

### [`00b52588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md) → [`00bc0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0eec.md) _INIT_287

採用 · 移動量 `+0x6e964` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b524e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524e0.md) [`00b524e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524e8.md) [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc0e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e44.md) [`00bc0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e4c.md) [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:86f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:10:8"
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
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:150:8"
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
      "00bc0efc",
      "PARAM",
      [
        "storage",
        "010a1150",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc0f0c",
      "WRITE",
      [
        "storage",
        "010a1150",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc0f0c",
      "DATA",
      [
        "storage",
        "0029986f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0efc",
      "PARAM",
      [
        "storage",
        "01126010",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc0f0c",
      "WRITE",
      [
        "storage",
        "01126010",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc0f0c",
      "DATA",
      [
        "storage",
        "002a9748",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md#insn-00b52588) · [`00b5258c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md#insn-00b5258c) · [`00b52590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md#insn-00b52590)
- 新版 `00bc0eec`（命令位置の公開資料なし） · `00bc0ef0`（命令位置の公開資料なし） · `00bc0ef4`（命令位置の公開資料なし）

~~~diff
- 00b52588 ["COPY", "register:4000:8", ["const:10a1000:8"]]
+ 00bc0eec ["COPY", "register:4000:8", ["const:1126000:8"]]
- 00b52588 bytes 602a00f0
+ 00bc0eec bytes 202b00d0
- 00b5258c ["COPY", "register:4040:8", ["const:299000:8"]]
+ 00bc0ef0 ["COPY", "register:4040:8", ["const:2a9000:8"]]
- 00b5258c bytes 28bafff0
+ 00bc0ef0 bytes 48b7ffb0
- 00b52590 ["COPY", "register:4048:8", ["const:b52000:8"]]
+ 00bc0ef4 ["COPY", "register:4048:8", ["const:bc0000:8"]]
- 00b52590 bytes 09000090
+ 00bc0ef4 bytes 09000090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8382651d3ac4f202d032e665e4ab4a76"></a>

### [`00b525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md) → [`00bc0f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddce0.md) · 呼出先 11件 [`00b52cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md)
- 新版 呼出元 1件 [`00c5a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a730.md) · 呼出先 11件 [`00bc163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 53.57% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc0f60",
      "incomplete_value": true,
      "site": "00bc0f60",
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
      "definition_site": "00b525fc",
      "incomplete_value": true,
      "site": "00b525fc",
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
      "definition_site": "00bc0f44",
      "incomplete_value": true,
      "site": "00bc0f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b525e0",
      "incomplete_value": true,
      "site": "00b525e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b00:8"
              ]
            ]
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
      "definition_site": "00bc0fa0",
      "incomplete_value": true,
      "site": "00bc0fa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "00bc0f3c",
      "READ",
      [
        "storage",
        "00c1bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0f44",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc0f4c",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bc0f3c",
      "READ",
      [
        "storage",
        "00c9b530",
        null,
        "pointer"
      ]
    ],
    [
      "00bc0f44",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc0f4c",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b525e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md#insn-00b525e4) · [`00b52640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md#insn-00b52640) · [`00b52660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md#insn-00b52660)
- 新版 `00bc0f48`（命令位置の公開資料なし） · `00bc0fa4`（命令位置の公開資料なし） · `00bc0fc4`（命令位置の公開資料なし）

~~~diff
- 00b525e4 ["INT_ADD", "register:40f0:8", ["const:b525e4:8", "const:4:8"]]
- 00b525e4 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc0f48 ["INT_ADD", "register:40f0:8", ["const:bc0f48:8", "const:4:8"]]
+ 00bc0f48 ["CALL", null, ["callee:00c5a600:8"]]
- 00b525e4 bytes 8f2d0294
+ 00bc0f48 bytes ae650294
- 00b52640 ["INT_ADD", "register:40f0:8", ["const:b52640:8", "const:4:8"]]
- 00b52640 ["CALL", null, ["callee:00c5a610:8"]]
+ 00bc0fa4 ["INT_ADD", "register:40f0:8", ["const:bc0fa4:8", "const:4:8"]]
+ 00bc0fa4 ["CALL", null, ["callee:00c5a610:8"]]
- 00b52640 bytes 7c2d0294
+ 00bc0fa4 bytes 9b650294
- 00b52660 ["INT_ADD", "register:40f0:8", ["const:b52660:8", "const:4:8"]]
- 00b52660 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc0fc4 ["INT_ADD", "register:40f0:8", ["const:bc0fc4:8", "const:4:8"]]
+ 00bc0fc4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b52660 bytes c82e0294
+ 00bc0fc4 bytes 0f670294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04d47612434c0ecf65f32b901ae6e1c"></a>

### [`00b52814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52814.md) → [`00bc1178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1178.md) _ZN8firebase13remote_config12RemoteConfig16FindRemoteConfigEPNS_3AppE

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc11a0",
      "incomplete_value": true,
      "site": "00bc11a0",
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
      "definition_site": "00b5283c",
      "incomplete_value": true,
      "site": "00b5283c",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52864"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc11c8"
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
      "00bc118c",
      "READ",
      [
        "storage",
        "00c1bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bc118c",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1198",
      "READ",
      [
        "storage",
        "00c1bb08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc118c",
      "READ",
      [
        "storage",
        "00c9b530",
        null,
        "pointer"
      ]
    ],
    [
      "00bc118c",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1198",
      "READ",
      [
        "storage",
        "00c9b538",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5282c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52814.md#insn-00b5282c) · [`00b5283c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52814.md#insn-00b5283c) · [`00b52864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52814.md#insn-00b52864)
- 新版 `00bc1190`（命令位置の公開資料なし） · `00bc11a0`（命令位置の公開資料なし）

~~~diff
- 00b5282c ["INT_ADD", "register:40f0:8", ["const:b5282c:8", "const:4:8"]]
- 00b5282c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc1190 ["INT_ADD", "register:40f0:8", ["const:bc1190:8", "const:4:8"]]
+ 00bc1190 ["CALL", null, ["callee:00c5a600:8"]]
- 00b5282c bytes fd2c0294
+ 00bc1190 bytes 1c650294
- 00b5283c ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b5283c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bc11a0 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00bc11a0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5283c bytes ca0100b4
+ 00bc11a0 bytes ca0100b4
- 00b52864 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b52864 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52910ae69aabe3450e49283b3f5de024"></a>

### [`00b528a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b528a8.md) → [`00bc120c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc120c.md) _ZN8firebase13remote_config12RemoteConfig14DeleteInternalEv

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06d0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2b0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 73.33% / 新版 81.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1270",
      "incomplete_value": true,
      "site": "00bc1270",
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
      "definition_site": "00b5290c",
      "incomplete_value": true,
      "site": "00b5290c",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52948"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc12ac"
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
      "00bc1220",
      "READ",
      [
        "storage",
        "00c1bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1220",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1268",
      "READ",
      [
        "storage",
        "00c1bb08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc1220",
      "READ",
      [
        "storage",
        "00c9b530",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1220",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1268",
      "READ",
      [
        "storage",
        "00c9b538",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b528c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b528a8.md#insn-00b528c0) · [`00b528f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b528a8.md#insn-00b528f0) · [`00b528f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b528a8.md#insn-00b528f8)
- 新版 `00bc1224`（命令位置の公開資料なし） · `00bc1254`（命令位置の公開資料なし） · `00bc125c`（命令位置の公開資料なし）

~~~diff
- 00b528c0 ["INT_ADD", "register:40f0:8", ["const:b528c0:8", "const:4:8"]]
- 00b528c0 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc1224 ["INT_ADD", "register:40f0:8", ["const:bc1224:8", "const:4:8"]]
+ 00bc1224 ["CALL", null, ["callee:00c5a600:8"]]
- 00b528c0 bytes d82c0294
+ 00bc1224 bytes f7640294
- 00b528f0 ["INT_ADD", "register:40f0:8", ["const:b528f0:8", "const:4:8"]]
- 00b528f0 ["CALL", null, ["callee:00c5d480:8"]]
+ 00bc1254 ["INT_ADD", "register:40f0:8", ["const:bc1254:8", "const:4:8"]]
+ 00bc1254 ["CALL", null, ["callee:00c5d480:8"]]
- 00b528f0 bytes e4370294
+ 00bc1254 bytes 8b700294
- 00b528f8 ["INT_ADD", "register:40f0:8", ["const:b528f8:8", "const:4:8"]]
- 00b528f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bc125c ["INT_ADD", "register:40f0:8", ["const:bc125c:8", "const:4:8"]]
+ 00bc125c ["CALL", null, ["callee:00c57ab0:8"]]
- 00b528f8 bytes da210294
+ 00bc125c bytes 155a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-247a32104b662ac5f8c2c12c8936137e"></a>

### [`00b529f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b529f4.md) → [`00bc1358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1358.md) _ZN8firebase13remote_config12RemoteConfigC2EPNS_3AppE

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be0870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0870.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d470.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1378",
      "incomplete_value": false,
      "site": "00bc137c",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52a14",
      "incomplete_value": false,
      "site": "00b52a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:ed7:8"
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
      "00bc1378",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1378",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b529f4.md#insn-00b52a18) · [`00b52a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b529f4.md#insn-00b52a10) · [`00b52a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b529f4.md#insn-00b52a14)
- 新版 `00bc137c`（命令位置の公開資料なし） · `00bc1374`（命令位置の公開資料なし） · `00bc1378`（命令位置の公開資料なし）

~~~diff
- 00b52a18 ["INT_ADD", "register:40f0:8", ["const:b52a18:8", "const:4:8"]]
- 00b52a18 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc137c ["INT_ADD", "register:40f0:8", ["const:bc137c:8", "const:4:8"]]
+ 00bc137c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b52a18 bytes da2d0294
+ 00bc137c bytes 21660294
- 00b52a10 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bc1374 ["COPY", "register:4000:8", ["const:2b2000:8"]]
- 00b52a10 bytes 60bafff0
+ 00bc1374 bytes 80b7ffb0
- 00b52a14 ["COPY", "tmp:0:8", ["const:ed7:8"]]
- 00b52a14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52a14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52a14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1378 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00bc1378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52a14 bytes 005c3b91
+ 00bc1378 bytes 00601691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58001610a04fc2add83d2cca00ad849"></a>

### [`00b52a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52a7c.md) → [`00bc13e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc13e0.md) _ZN8firebase13remote_config12RemoteConfig27EnsureInitializedLastResultEv

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be07c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3c0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52a80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d3c0"
      ]
    ]
  ],
  "added": [
    [
      "00bc13e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d3c0"
      ]
    ]
  ]
}
~~~


<a id="compare-10ecf76ac12a499bc9be971f16feb6d6"></a>

### [`00b52aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52aa4.md) → [`00bc1408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1408.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0x6e964` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0760.md) [`00be07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d350.md) [`00c5d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3e0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52aa4.md#insn-00b52abc)
- 新版 `00bc1420`（命令位置の公開資料なし）

~~~diff
- 00b52abc ["INT_ADD", "register:40f0:8", ["const:b52abc:8", "const:4:8"]]
- 00b52abc ["CALL", null, ["callee:00c5d350:8"]]
+ 00bc1420 ["INT_ADD", "register:40f0:8", ["const:bc1420:8", "const:4:8"]]
+ 00bc1420 ["CALL", null, ["callee:00c5d350:8"]]
- 00b52abc bytes 29370294
+ 00bc1420 bytes cc6f0294
~~~


<a id="compare-fb7596fc402d73977b7c3358aef02636"></a>

### [`00b52cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md) → [`00bc163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md) FUN_00bc163c

採用 · 移動量 `+0x6e974` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md) · 呼出先 2件 [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00be06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06d0.md)
- 新版 呼出元 1件 [`00bc0f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md) · 呼出先 2件 [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1654",
      "incomplete_value": false,
      "site": "00bc165c",
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
            "const:191:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52ce0",
      "incomplete_value": false,
      "site": "00b52ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f6b:8"
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
      "00bc1654",
      "PARAM",
      [
        "storage",
        "0029bf6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1654",
      "PARAM",
      [
        "storage",
        "002ac191",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md#insn-00b52ce8) · [`00b52cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md#insn-00b52cdc) · [`00b52ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md#insn-00b52ce0)
- 新版 `00bc165c`（命令位置の公開資料なし） · `00bc1650`（命令位置の公開資料なし） · `00bc1654`（命令位置の公開資料なし）

~~~diff
- 00b52ce8 ["INT_ADD", "register:40f0:8", ["const:b52ce8:8", "const:4:8"]]
- 00b52ce8 ["CALL", null, ["callee:00c5a9e0:8"]]
+ 00bc165c ["INT_ADD", "register:40f0:8", ["const:bc165c:8", "const:4:8"]]
+ 00bc165c ["CALL", null, ["callee:00c5a9e0:8"]]
- 00b52ce8 bytes 9e2c0294
+ 00bc165c bytes e1640294
- 00b52cdc ["COPY", "register:4000:8", ["const:29b000:8"]]
+ 00bc1650 ["COPY", "register:4000:8", ["const:2ac000:8"]]
- 00b52cdc bytes 40baffb0
+ 00bc1650 bytes 40b7fff0
- 00b52ce0 ["COPY", "tmp:0:8", ["const:f6b:8"]]
- 00b52ce0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52ce0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52ce0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1654 ["COPY", "tmp:0:8", ["const:191:8"]]
+ 00bc1654 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1654 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1654 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52ce0 bytes 00ac3d91
+ 00bc1654 bytes 00440691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a07b57dfb2a018815c0d974ff5b4dd"></a>

### [`00b52da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52da8.md) → [`00bc171c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc171c.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1748",
      "incomplete_value": true,
      "site": "00bc1748",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52dd4",
      "incomplete_value": true,
      "site": "00b52dd4",
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
            "const:1b8:8"
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
      "definition_site": "00bc1730",
      "incomplete_value": true,
      "site": "00bc1730",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b52dbc",
      "incomplete_value": true,
      "site": "00b52dbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc173c",
      "incomplete_value": false,
      "site": "00bc1740",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52dc8",
      "incomplete_value": false,
      "site": "00b52dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc172c",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc173c",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc1748",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc172c",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc173c",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1748",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52da8.md#insn-00b52dcc) · [`00b52dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52da8.md#insn-00b52dd4) · [`00b52db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52da8.md#insn-00b52db4)
- 新版 `00bc1740`（命令位置の公開資料なし） · `00bc1748`（命令位置の公開資料なし） · `00bc1728`（命令位置の公開資料なし）

~~~diff
- 00b52dcc ["INT_ADD", "register:40f0:8", ["const:b52dcc:8", "const:4:8"]]
- 00b52dcc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1740 ["INT_ADD", "register:40f0:8", ["const:bc1740:8", "const:4:8"]]
+ 00bc1740 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b52dcc bytes b12c0294
+ 00bc1740 bytes f4640294
- 00b52dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
- 00b52dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00bc1748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52dd4 bytes 60de00f9
+ 00bc1748 bytes 603e00f9
- 00b52db4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1728 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b52db4 bytes 732a00f0
+ 00bc1728 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5430c2484b9932fdbb8d3e0f37e44eaf"></a>

### [`00b52de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52de8.md) → [`00bc175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc175c.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1788",
      "incomplete_value": true,
      "site": "00bc1788",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e14",
      "incomplete_value": true,
      "site": "00b52e14",
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
            "const:1b8:8"
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
      "definition_site": "00bc1770",
      "incomplete_value": true,
      "site": "00bc1770",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b52dfc",
      "incomplete_value": true,
      "site": "00b52dfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1778",
      "incomplete_value": false,
      "site": "00bc1780",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e04",
      "incomplete_value": false,
      "site": "00b52e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc176c",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1778",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc1788",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc176c",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1778",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1788",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52de8.md#insn-00b52e0c) · [`00b52e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52de8.md#insn-00b52e14) · [`00b52df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52de8.md#insn-00b52df4)
- 新版 `00bc1780`（命令位置の公開資料なし） · `00bc1788`（命令位置の公開資料なし） · `00bc1768`（命令位置の公開資料なし）

~~~diff
- 00b52e0c ["INT_ADD", "register:40f0:8", ["const:b52e0c:8", "const:4:8"]]
- 00b52e0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1780 ["INT_ADD", "register:40f0:8", ["const:bc1780:8", "const:4:8"]]
+ 00bc1780 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b52e0c bytes a12c0294
+ 00bc1780 bytes e4640294
- 00b52e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
- 00b52e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00bc1788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52e14 bytes 60de00f9
+ 00bc1788 bytes 603e00f9
- 00b52df4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1768 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b52df4 bytes 732a00f0
+ 00bc1768 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f5cb1e3dcec6cae0527223572d3bef"></a>

### [`00b52e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e28.md) → [`00bc179c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc179c.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc17cc",
      "incomplete_value": true,
      "site": "00bc17cc",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e58",
      "incomplete_value": true,
      "site": "00b52e58",
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
            "const:1b8:8"
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
      "definition_site": "00bc17b0",
      "incomplete_value": true,
      "site": "00bc17b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b52e3c",
      "incomplete_value": true,
      "site": "00b52e3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc17bc",
      "incomplete_value": false,
      "site": "00bc17c4",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e48",
      "incomplete_value": false,
      "site": "00b52e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc17ac",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc17bc",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc17cc",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc17ac",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc17bc",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc17cc",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e28.md#insn-00b52e50) · [`00b52e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e28.md#insn-00b52e58) · [`00b52e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e28.md#insn-00b52e34)
- 新版 `00bc17c4`（命令位置の公開資料なし） · `00bc17cc`（命令位置の公開資料なし） · `00bc17a8`（命令位置の公開資料なし）

~~~diff
- 00b52e50 ["INT_ADD", "register:40f0:8", ["const:b52e50:8", "const:4:8"]]
- 00b52e50 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc17c4 ["INT_ADD", "register:40f0:8", ["const:bc17c4:8", "const:4:8"]]
+ 00bc17c4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b52e50 bytes 902c0294
+ 00bc17c4 bytes d3640294
- 00b52e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
- 00b52e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc17cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00bc17cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52e58 bytes 60de00f9
+ 00bc17cc bytes 603e00f9
- 00b52e34 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc17a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b52e34 bytes 732a00f0
+ 00bc17a8 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d0a591cb75730961c76175349f2bc07"></a>

### [`00b52e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e6c.md) → [`00bc17e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc17e0.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1810",
      "incomplete_value": true,
      "site": "00bc1810",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e9c",
      "incomplete_value": true,
      "site": "00b52e9c",
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
            "const:1b8:8"
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
      "definition_site": "00bc17f4",
      "incomplete_value": true,
      "site": "00bc17f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b52e80",
      "incomplete_value": true,
      "site": "00b52e80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc17fc",
      "incomplete_value": false,
      "site": "00bc1808",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e88",
      "incomplete_value": false,
      "site": "00b52e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc17f0",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc17fc",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc1810",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc17f0",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc17fc",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1810",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e6c.md#insn-00b52e94) · [`00b52e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e6c.md#insn-00b52e9c) · [`00b52e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e6c.md#insn-00b52e78)
- 新版 `00bc1808`（命令位置の公開資料なし） · `00bc1810`（命令位置の公開資料なし） · `00bc17ec`（命令位置の公開資料なし）

~~~diff
- 00b52e94 ["INT_ADD", "register:40f0:8", ["const:b52e94:8", "const:4:8"]]
- 00b52e94 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1808 ["INT_ADD", "register:40f0:8", ["const:bc1808:8", "const:4:8"]]
+ 00bc1808 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b52e94 bytes 7f2c0294
+ 00bc1808 bytes c2640294
- 00b52e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
- 00b52e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00bc1810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52e9c bytes 60de00f9
+ 00bc1810 bytes 603e00f9
- 00b52e78 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc17ec ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b52e78 bytes 732a00f0
+ 00bc17ec bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a5262967dd56d270edf6a1f6c3ee39d"></a>

### [`00b52ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52ebc.md) → [`00bc1830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1830.md) _ZN8firebase13remote_config8internal6config15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1888",
      "incomplete_value": true,
      "site": "00bc1888",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f14",
      "incomplete_value": true,
      "site": "00b52f14",
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
            "const:1c0:8"
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
      "definition_site": "00bc1864",
      "incomplete_value": true,
      "site": "00bc1870",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52ef0",
      "incomplete_value": true,
      "site": "00b52efc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:1b8:8"
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
      "00bc1844",
      "READ",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1864",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1888",
      "WRITE",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1844",
      "READ",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1864",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1888",
      "WRITE",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52ebc.md#insn-00b52efc) · [`00b52f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52ebc.md#insn-00b52f14) · [`00b52ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52ebc.md#insn-00b52ecc)
- 新版 `00bc1870`（命令位置の公開資料なし） · `00bc1888`（命令位置の公開資料なし） · `00bc1840`（命令位置の公開資料なし）

~~~diff
- 00b52efc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52efc ["INT_ADD", "register:40f0:8", ["const:b52efc:8", "const:4:8"]]
- 00b52efc ["CALLIND", null, ["register:0:8"]]
+ 00bc1870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1870 ["INT_ADD", "register:40f0:8", ["const:bc1870:8", "const:4:8"]]
+ 00bc1870 ["CALLIND", null, ["register:0:8"]]
- 00b52efc bytes 00013fd6
+ 00bc1870 bytes 00013fd6
- 00b52f14 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b52f14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1c0:8"]]
- 00b52f14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc1888 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc1888 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:80:8"]]
+ 00bc1888 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b52f14 bytes a0020739
+ 00bc1888 bytes a0020239
- 00b52ecc ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc1840 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b52ecc bytes 752a00f0
+ 00bc1840 bytes 352b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be906bbaede3d48175b684046c2d46cf"></a>

### [`00b52f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f28.md) → [`00bc189c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc189c.md) _ZN8firebase13remote_config8internal6config12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bc18d8",
      "incomplete_value": true,
      "site": "00bc18d8",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f64",
      "incomplete_value": true,
      "site": "00b52f64",
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
            "const:1c0:8"
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
      "definition_site": "00bc18f8",
      "incomplete_value": true,
      "site": "00bc18f8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f84",
      "incomplete_value": true,
      "site": "00b52f84",
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
            "const:1b8:8"
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
      "definition_site": "00bc18b4",
      "incomplete_value": true,
      "site": "00bc18b4",
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
      "definition_site": "00b52f40",
      "incomplete_value": true,
      "site": "00b52f40",
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
      "00bc18b0",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc18bc",
      "READ",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc18d8",
      "WRITE",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc18b0",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc18bc",
      "READ",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc18d8",
      "WRITE",
      [
        "storage",
        "01126080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f28.md#insn-00b52f64) · [`00b52f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f28.md#insn-00b52f80) · [`00b52f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f28.md#insn-00b52f84)
- 新版 `00bc18d8`（命令位置の公開資料なし） · `00bc18f4`（命令位置の公開資料なし） · `00bc18f8`（命令位置の公開資料なし）

~~~diff
- 00b52f64 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b52f64 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b52f64 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1c0:8"]]
- 00b52f64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc18d8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc18d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc18d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:80:8"]]
+ 00bc18d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b52f64 bytes bf020739
+ 00bc18d8 bytes bf020239
- 00b52f80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52f80 ["INT_ADD", "register:40f0:8", ["const:b52f80:8", "const:4:8"]]
- 00b52f80 ["CALLIND", null, ["register:0:8"]]
+ 00bc18f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc18f4 ["INT_ADD", "register:40f0:8", ["const:bc18f4:8", "const:4:8"]]
+ 00bc18f4 ["CALLIND", null, ["register:0:8"]]
- 00b52f80 bytes 00013fd6
+ 00bc18f4 bytes 00013fd6
- 00b52f84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
- 00b52f84 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b52f84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc18f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00bc18f8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc18f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b52f84 bytes 9fde00f9
+ 00bc18f8 bytes 9f3e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95777971fd9e010d5ccd2bdbad0730dd"></a>

### [`00b52f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f98.md) → [`00bc190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc190c.md) _ZN8firebase13remote_config8internal6config14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc194c",
      "incomplete_value": true,
      "site": "00bc194c",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52fd8",
      "incomplete_value": true,
      "site": "00b52fd8",
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
            "const:1b8:8"
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
      "definition_site": "00bc1928",
      "incomplete_value": true,
      "site": "00bc1928",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b52fb4",
      "incomplete_value": true,
      "site": "00b52fb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1930",
      "incomplete_value": false,
      "site": "00bc1944",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52fbc",
      "incomplete_value": false,
      "site": "00b52fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc1920",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1930",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc194c",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1920",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1930",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc194c",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f98.md#insn-00b52fd0) · [`00b52fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f98.md#insn-00b52fd8) · [`00b52fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f98.md#insn-00b52fa4)
- 新版 `00bc1944`（命令位置の公開資料なし） · `00bc194c`（命令位置の公開資料なし） · `00bc1918`（命令位置の公開資料なし）

~~~diff
- 00b52fd0 ["INT_ADD", "register:40f0:8", ["const:b52fd0:8", "const:4:8"]]
- 00b52fd0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1944 ["INT_ADD", "register:40f0:8", ["const:bc1944:8", "const:4:8"]]
+ 00bc1944 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b52fd0 bytes 302c0294
+ 00bc1944 bytes 73640294
- 00b52fd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
- 00b52fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc194c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00bc194c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52fd8 bytes 80de00f9
+ 00bc194c bytes 803e00f9
- 00b52fa4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc1918 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b52fa4 bytes 742a00f0
+ 00bc1918 bytes 342b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4049aeb64f2a9354052164999d8f4339"></a>

### [`00b53008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53008.md) → [`00bc197c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc197c.md) _ZN8firebase13remote_config8internal6config11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, call_argument_candidate, comparison, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1990",
      "incomplete_value": true,
      "site": "00bc1990",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:4000:4"
              ],
              [
                "leaf",
                "const:12:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5301c",
      "incomplete_value": true,
      "site": "00b5301c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:4000:4"
              ],
              [
                "leaf",
                "const:11:4"
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
      "definition_site": "00bc1998",
      "incomplete_value": false,
      "site": "00bc199c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53024",
      "incomplete_value": false,
      "site": "00b53028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc19a8",
      "incomplete_value": true,
      "site": "00bc19b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53034",
      "incomplete_value": true,
      "site": "00b53040",
      "value": [
        "LOAD",
        "8",
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
      "00bc1998",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc19a8",
      "DATA",
      [
        "storage",
        "010a11c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1998",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc19a8",
      "DATA",
      [
        "storage",
        "01126088",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53008.md#insn-00b53028) · [`00b53018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53008.md#insn-00b53018) · [`00b53020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53008.md#insn-00b53020)
- 新版 `00bc199c`（命令位置の公開資料なし） · `00bc198c`（命令位置の公開資料なし） · `00bc1994`（命令位置の公開資料なし）

~~~diff
- 00b53028 ["INT_ADD", "register:40f0:8", ["const:b53028:8", "const:4:8"]]
- 00b53028 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc199c ["INT_ADD", "register:40f0:8", ["const:bc199c:8", "const:4:8"]]
+ 00bc199c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53028 bytes 562c0294
+ 00bc199c bytes 99640294
- 00b53018 ["COPY", "tmp:0:4", ["const:11:4"]]
- 00b53018 ["INT_LESSEQUAL", "register:105:1", ["const:11:4", "register:4000:4"]]
- 00b53018 ["INT_SBORROW", "register:106:1", ["register:4000:4", "const:11:4"]]
- 00b53018 ["INT_SUB", "tmp:1:4", ["register:4000:4", "tmp:0:4"]]
+ 00bc198c ["COPY", "tmp:0:4", ["const:12:4"]]
+ 00bc198c ["INT_LESSEQUAL", "register:105:1", ["const:12:4", "register:4000:4"]]
+ 00bc198c ["INT_SBORROW", "register:106:1", ["register:4000:4", "const:12:4"]]
+ 00bc198c ["INT_SUB", "tmp:1:4", ["register:4000:4", "tmp:0:4"]]
- 00b53018 bytes 1f440071
+ 00bc198c bytes 1f480071
- 00b53020 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc1994 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b53020 bytes 20baffb0
+ 00bc1994 bytes 20b7fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef2648daf874acaa8d0b79b2ab7e71f9"></a>

### [`00b53044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53044.md) → [`00bc19b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc19b8.md) _ZN8firebase13remote_config8internal6config13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc19f8",
      "incomplete_value": true,
      "site": "00bc19f8",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53084",
      "incomplete_value": true,
      "site": "00b53084",
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
            "const:1b8:8"
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
      "definition_site": "00bc19d4",
      "incomplete_value": true,
      "site": "00bc19d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53060",
      "incomplete_value": true,
      "site": "00b53060",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc19dc",
      "incomplete_value": false,
      "site": "00bc19f0",
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
            "const:656:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53068",
      "incomplete_value": false,
      "site": "00b5307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:a:8"
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
      "00bc19cc",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc19dc",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00bc19f8",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc19cc",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc19dc",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc19f8",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5307c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53044.md#insn-00b5307c) · [`00b53084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53044.md#insn-00b53084) · [`00b53050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53044.md#insn-00b53050)
- 新版 `00bc19f0`（命令位置の公開資料なし） · `00bc19f8`（命令位置の公開資料なし） · `00bc19c4`（命令位置の公開資料なし）

~~~diff
- 00b5307c ["INT_ADD", "register:40f0:8", ["const:b5307c:8", "const:4:8"]]
- 00b5307c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc19f0 ["INT_ADD", "register:40f0:8", ["const:bc19f0:8", "const:4:8"]]
+ 00bc19f0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5307c bytes 052c0294
+ 00bc19f0 bytes 48640294
- 00b53084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
- 00b53084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc19f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00bc19f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53084 bytes 80de00f9
+ 00bc19f8 bytes 803e00f9
- 00b53050 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc19c4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b53050 bytes 742a00d0
+ 00bc19c4 bytes 342b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ae869ccc7af3fd544246e43578c431"></a>

### [`00b530b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530b4.md) → [`00bc1a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a28.md) _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc1a44",
      "incomplete_value": false,
      "site": "00bc1a48",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b530d0",
      "incomplete_value": false,
      "site": "00b530d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bc1a54",
      "incomplete_value": true,
      "site": "00bc1a60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b530e0",
      "incomplete_value": true,
      "site": "00b530ec",
      "value": [
        "LOAD",
        "8",
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
      "00bc1a44",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bc1a54",
      "DATA",
      [
        "storage",
        "010a1250",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1a44",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc1a54",
      "DATA",
      [
        "storage",
        "01126118",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b530d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530b4.md#insn-00b530d4) · [`00b530cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530b4.md#insn-00b530cc) · [`00b530d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530b4.md#insn-00b530d0)
- 新版 `00bc1a48`（命令位置の公開資料なし） · `00bc1a40`（命令位置の公開資料なし） · `00bc1a44`（命令位置の公開資料なし）

~~~diff
- 00b530d4 ["INT_ADD", "register:40f0:8", ["const:b530d4:8", "const:4:8"]]
- 00b530d4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc1a48 ["INT_ADD", "register:40f0:8", ["const:bc1a48:8", "const:4:8"]]
+ 00bc1a48 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b530d4 bytes 2b2c0294
+ 00bc1a48 bytes 6e640294
- 00b530cc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bc1a40 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b530cc bytes 20baffd0
+ 00bc1a40 bytes 40b7ff90
- 00b530d0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b530d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b530d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b530d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a44 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bc1a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b530d0 bytes 00c81791
+ 00bc1a44 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e95dce2654645811d46ded9ba1a2e982"></a>

### [`00b530f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530f0.md) → [`00bc1a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1a64.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1a90",
      "incomplete_value": true,
      "site": "00bc1a90",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5311c",
      "incomplete_value": true,
      "site": "00b5311c",
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
            "const:258:8"
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
      "definition_site": "00bc1a78",
      "incomplete_value": true,
      "site": "00bc1a78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53104",
      "incomplete_value": true,
      "site": "00b53104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1a84",
      "incomplete_value": false,
      "site": "00bc1a88",
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
            "const:c8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53110",
      "incomplete_value": false,
      "site": "00b53114",
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
            "const:6e1:8"
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
      "00bc1a74",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1a84",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ],
    [
      "00bc1a90",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1a74",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1a84",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1a90",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530f0.md#insn-00b53114) · [`00b5311c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530f0.md#insn-00b5311c) · [`00b530fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530f0.md#insn-00b530fc)
- 新版 `00bc1a88`（命令位置の公開資料なし） · `00bc1a90`（命令位置の公開資料なし） · `00bc1a70`（命令位置の公開資料なし）

~~~diff
- 00b53114 ["INT_ADD", "register:40f0:8", ["const:b53114:8", "const:4:8"]]
- 00b53114 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1a88 ["INT_ADD", "register:40f0:8", ["const:bc1a88:8", "const:4:8"]]
+ 00bc1a88 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53114 bytes df2b0294
+ 00bc1a88 bytes 22640294
- 00b5311c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b5311c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1a90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
+ 00bc1a90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5311c bytes 602e01f9
+ 00bc1a90 bytes 609200f9
- 00b530fc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1a70 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b530fc bytes 732a00d0
+ 00bc1a70 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa6e69638b517475384a714203f276e"></a>

### [`00b53130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53130.md) → [`00bc1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1ad0",
      "incomplete_value": true,
      "site": "00bc1ad0",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5315c",
      "incomplete_value": true,
      "site": "00b5315c",
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
            "const:258:8"
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
      "definition_site": "00bc1ab8",
      "incomplete_value": true,
      "site": "00bc1ab8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53144",
      "incomplete_value": true,
      "site": "00b53144",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1ac0",
      "incomplete_value": false,
      "site": "00bc1ac8",
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
            "const:c8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5314c",
      "incomplete_value": false,
      "site": "00b53154",
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
            "const:6e1:8"
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
      "00bc1ab4",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ac0",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ],
    [
      "00bc1ad0",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1ab4",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ac0",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1ad0",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53130.md#insn-00b53154) · [`00b5315c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53130.md#insn-00b5315c) · [`00b5313c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53130.md#insn-00b5313c)
- 新版 `00bc1ac8`（命令位置の公開資料なし） · `00bc1ad0`（命令位置の公開資料なし） · `00bc1ab0`（命令位置の公開資料なし）

~~~diff
- 00b53154 ["INT_ADD", "register:40f0:8", ["const:b53154:8", "const:4:8"]]
- 00b53154 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1ac8 ["INT_ADD", "register:40f0:8", ["const:bc1ac8:8", "const:4:8"]]
+ 00bc1ac8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53154 bytes cf2b0294
+ 00bc1ac8 bytes 12640294
- 00b5315c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b5315c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
+ 00bc1ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5315c bytes 602e01f9
+ 00bc1ad0 bytes 609200f9
- 00b5313c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1ab0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5313c bytes 732a00d0
+ 00bc1ab0 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5a65320c7b33bc17d422babb690557f"></a>

### [`00b53170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53170.md) → [`00bc1ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ae4.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1b14",
      "incomplete_value": true,
      "site": "00bc1b14",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b531a0",
      "incomplete_value": true,
      "site": "00b531a0",
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
            "const:258:8"
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
      "definition_site": "00bc1af8",
      "incomplete_value": true,
      "site": "00bc1af8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b53184",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1b04",
      "incomplete_value": false,
      "site": "00bc1b0c",
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
            "const:c8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53190",
      "incomplete_value": false,
      "site": "00b53198",
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
            "const:6e1:8"
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
      "00bc1af4",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1b04",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ],
    [
      "00bc1b14",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1af4",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1b04",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1b14",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53170.md#insn-00b53198) · [`00b531a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53170.md#insn-00b531a0) · [`00b5317c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53170.md#insn-00b5317c)
- 新版 `00bc1b0c`（命令位置の公開資料なし） · `00bc1b14`（命令位置の公開資料なし） · `00bc1af0`（命令位置の公開資料なし）

~~~diff
- 00b53198 ["INT_ADD", "register:40f0:8", ["const:b53198:8", "const:4:8"]]
- 00b53198 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1b0c ["INT_ADD", "register:40f0:8", ["const:bc1b0c:8", "const:4:8"]]
+ 00bc1b0c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53198 bytes be2b0294
+ 00bc1b0c bytes 01640294
- 00b531a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b531a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:120:8"]]
+ 00bc1b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b531a0 bytes 602e01f9
+ 00bc1b14 bytes 609200f9
- 00b5317c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1af0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5317c bytes 732a00d0
+ 00bc1af0 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d36b3d15f2edd465867073dfba14ba3"></a>

### [`00b531b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b531b4.md) → [`00bc1b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b28.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00b531e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1b58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1b3c",
      "incomplete_value": true,
      "site": "00bc1b3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b531c8",
      "incomplete_value": true,
      "site": "00b531c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc1b38",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b531d0",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b531e4",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b38",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1b44",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1b58",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b531c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b531b4.md#insn-00b531c8) · [`00b531dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b531b4.md#insn-00b531dc) · [`00b531e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b531b4.md#insn-00b531e4)
- 新版 `00bc1b3c`（命令位置の公開資料なし） · `00bc1b50`（命令位置の公開資料なし）

~~~diff
- 00b531c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b531c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1b3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1b3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b531c8 bytes 080100b5
+ 00bc1b3c bytes 080100b5
- 00b531dc ["INT_ADD", "register:40f0:8", ["const:b531dc:8", "const:4:8"]]
- 00b531dc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1b50 ["INT_ADD", "register:40f0:8", ["const:bc1b50:8", "const:4:8"]]
+ 00bc1b50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b531dc bytes ad2b0294
+ 00bc1b50 bytes f0630294
- 00b531e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
- 00b531e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b531e4 bytes 602e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6b369ea739e42d54080df3c45dd77e"></a>

### [`00b53204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53204.md) → [`00bc1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b78.md) _ZN8firebase13remote_config8internal12config_value15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1bd0",
      "incomplete_value": true,
      "site": "00bc1bd0",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5325c",
      "incomplete_value": true,
      "site": "00b5325c",
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
            "const:260:8"
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
      "definition_site": "00bc1bac",
      "incomplete_value": true,
      "site": "00bc1bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53238",
      "incomplete_value": true,
      "site": "00b53244",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:258:8"
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
      "00bc1b8c",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1bac",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1bd0",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b8c",
      "READ",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1bac",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1bd0",
      "WRITE",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53204.md#insn-00b53244) · [`00b5325c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53204.md#insn-00b5325c) · [`00b53214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53204.md#insn-00b53214)
- 新版 `00bc1bb8`（命令位置の公開資料なし） · `00bc1bd0`（命令位置の公開資料なし） · `00bc1b88`（命令位置の公開資料なし）

~~~diff
- 00b53244 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53244 ["INT_ADD", "register:40f0:8", ["const:b53244:8", "const:4:8"]]
- 00b53244 ["CALLIND", null, ["register:0:8"]]
+ 00bc1bb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1bb8 ["INT_ADD", "register:40f0:8", ["const:bc1bb8:8", "const:4:8"]]
+ 00bc1bb8 ["CALLIND", null, ["register:0:8"]]
- 00b53244 bytes 00013fd6
+ 00bc1bb8 bytes 00013fd6
- 00b5325c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5325c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
- 00b5325c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc1bd0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc1bd0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:128:8"]]
+ 00bc1bd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5325c bytes a0820939
+ 00bc1bd0 bytes a0a20439
- 00b53214 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc1b88 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b53214 bytes 752a00d0
+ 00bc1b88 bytes 352b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cb94fa24fcd27b4e07c2b8a4675b4ce"></a>

### [`00b53270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53270.md) → [`00bc1be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1be4.md) _ZN8firebase13remote_config8internal12config_value12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bc1c20",
      "incomplete_value": true,
      "site": "00bc1c20",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b532ac",
      "incomplete_value": true,
      "site": "00b532ac",
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
            "const:260:8"
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
      "definition_site": "00bc1c40",
      "incomplete_value": true,
      "site": "00bc1c40",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b532cc",
      "incomplete_value": true,
      "site": "00b532cc",
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
            "const:258:8"
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
      "definition_site": "00bc1bfc",
      "incomplete_value": true,
      "site": "00bc1bfc",
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
      "definition_site": "00b53288",
      "incomplete_value": true,
      "site": "00b53288",
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
      "00bc1bf8",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c04",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1c20",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1bf8",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c04",
      "READ",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1c20",
      "WRITE",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b532ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53270.md#insn-00b532ac) · [`00b532c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53270.md#insn-00b532c8) · [`00b532cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53270.md#insn-00b532cc)
- 新版 `00bc1c20`（命令位置の公開資料なし） · `00bc1c3c`（命令位置の公開資料なし） · `00bc1c40`（命令位置の公開資料なし）

~~~diff
- 00b532ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b532ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b532ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:260:8"]]
- 00b532ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc1c20 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc1c20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc1c20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:128:8"]]
+ 00bc1c20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b532ac bytes bf820939
+ 00bc1c20 bytes bfa20439
- 00b532c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b532c8 ["INT_ADD", "register:40f0:8", ["const:b532c8:8", "const:4:8"]]
- 00b532c8 ["CALLIND", null, ["register:0:8"]]
+ 00bc1c3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1c3c ["INT_ADD", "register:40f0:8", ["const:bc1c3c:8", "const:4:8"]]
+ 00bc1c3c ["CALLIND", null, ["register:0:8"]]
- 00b532c8 bytes 00013fd6
+ 00bc1c3c bytes 00013fd6
- 00b532cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b532cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b532cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc1c40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:120:8"]]
+ 00bc1c40 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc1c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b532cc bytes 9f2e01f9
+ 00bc1c40 bytes 9f9200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d30211de11d8a191d20aa9be33dc7532"></a>

### [`00b532e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b532e0.md) → [`00bc1c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1c54.md) _ZN8firebase13remote_config8internal12config_value14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00bc1c94",
      "incomplete_value": true,
      "site": "00bc1c94",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53320",
      "incomplete_value": true,
      "site": "00b53320",
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
            "const:258:8"
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
      "definition_site": "00bc1c70",
      "incomplete_value": true,
      "site": "00bc1c70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b532fc",
      "incomplete_value": true,
      "site": "00b532fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1c78",
      "incomplete_value": false,
      "site": "00bc1c8c",
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
            "const:c8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53304",
      "incomplete_value": false,
      "site": "00b53318",
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
            "const:6e1:8"
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
      "00bc1c68",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c78",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ],
    [
      "00bc1c94",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c68",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c78",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ],
    [
      "00bc1c94",
      "WRITE",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b532e0.md#insn-00b53318) · [`00b53320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b532e0.md#insn-00b53320) · [`00b532ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b532e0.md#insn-00b532ec)
- 新版 `00bc1c8c`（命令位置の公開資料なし） · `00bc1c94`（命令位置の公開資料なし） · `00bc1c60`（命令位置の公開資料なし）

~~~diff
- 00b53318 ["INT_ADD", "register:40f0:8", ["const:b53318:8", "const:4:8"]]
- 00b53318 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1c8c ["INT_ADD", "register:40f0:8", ["const:bc1c8c:8", "const:4:8"]]
+ 00bc1c8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53318 bytes 5e2b0294
+ 00bc1c8c bytes a1630294
- 00b53320 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b53320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1c94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:120:8"]]
+ 00bc1c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53320 bytes 802e01f9
+ 00bc1c94 bytes 809200f9
- 00b532ec ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc1c60 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b532ec bytes 742a00d0
+ 00bc1c60 bytes 342b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73bc5c8639da946ee0935e40811d0c7"></a>

### [`00b5338c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5338c.md) → [`00bc1d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d00.md) _ZN8firebase13remote_config8internal12config_value13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b533cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1d40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b533a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b533a0",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b533a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1d44"
      ]
    ],
    [
      "unmatched:00b533b0",
      "PARAM",
      [
        "storage",
        "002b06e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1d14",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1d44"
      ]
    ],
    [
      "00bc1d24",
      "PARAM",
      [
        "storage",
        "002c1c8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b533a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5338c.md#insn-00b533a8) · [`00b533c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5338c.md#insn-00b533c4) · [`00b533cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5338c.md#insn-00b533cc)
- 新版 `00bc1d38`（命令位置の公開資料なし）

~~~diff
- 00b533a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b533a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b533a8 bytes 410100b5
- 00b533c4 ["INT_ADD", "register:40f0:8", ["const:b533c4:8", "const:4:8"]]
- 00b533c4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1d38 ["INT_ADD", "register:40f0:8", ["const:bc1d38:8", "const:4:8"]]
+ 00bc1d38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b533c4 bytes 332b0294
+ 00bc1d38 bytes 76630294
- 00b533cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
- 00b533cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b533cc bytes 802e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-428b3725852043c51007d3693c9a3344"></a>

### [`00b53438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md) → [`00bc1dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dac.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53464"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1dd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1dc0",
      "incomplete_value": true,
      "site": "00bc1dc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5344c",
      "incomplete_value": true,
      "site": "00b5344c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc1dbc",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53458",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5345c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bc1dbc",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1dcc",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc1dd0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md#insn-00b5344c) · [`00b5345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md#insn-00b5345c) · [`00b53464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md#insn-00b53464)
- 新版 `00bc1dc0`（命令位置の公開資料なし）

~~~diff
- 00b5344c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5344c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1dc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1dc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5344c bytes e80000b5
+ 00bc1dc0 bytes e80000b5
- 00b5345c ["INT_ADD", "register:40f0:8", ["const:b5345c:8", "const:4:8"]]
- 00b5345c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5345c bytes 0d2b0294
- 00b53464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
- 00b53464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53464 bytes 605201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7584f538f5b59ffa136167c48afc55e5"></a>

### [`00b53478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md) → [`00bc1dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1dec.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5347c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5347c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53478",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5347c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1dfc",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1dec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc1df0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1dfc",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md#insn-00b53478) · [`00b5347c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md#insn-00b5347c) · [`00b5348c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md#insn-00b5348c)
- 新版 `00bc1e00`（命令位置の公開資料なし）

~~~diff
- 00b53478 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b53478 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53478 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53478 bytes f30f1ef8
- 00b5347c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5347c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5347c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5347c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5347c bytes fd7b01a9
- 00b5348c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5348c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1e00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1e00 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5348c bytes e80000b5
+ 00bc1e00 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c67537d65f8f9f80783116a001c649e"></a>

### [`00b534b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534b8.md) → [`00bc1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e2c.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1e5c",
      "incomplete_value": true,
      "site": "00bc1e5c",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534e8",
      "incomplete_value": true,
      "site": "00b534e8",
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
            "const:2a0:8"
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
      "definition_site": "00bc1e40",
      "incomplete_value": true,
      "site": "00bc1e40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b534cc",
      "incomplete_value": true,
      "site": "00b534cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1e4c",
      "incomplete_value": false,
      "site": "00bc1e54",
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
            "const:30c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534d8",
      "incomplete_value": false,
      "site": "00b534e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00bc1e3c",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e4c",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00bc1e5c",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1e3c",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e4c",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc1e5c",
      "WRITE",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b534e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534b8.md#insn-00b534e0) · [`00b534e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534b8.md#insn-00b534e8) · [`00b534c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534b8.md#insn-00b534c4)
- 新版 `00bc1e54`（命令位置の公開資料なし） · `00bc1e5c`（命令位置の公開資料なし） · `00bc1e38`（命令位置の公開資料なし）

~~~diff
- 00b534e0 ["INT_ADD", "register:40f0:8", ["const:b534e0:8", "const:4:8"]]
- 00b534e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1e54 ["INT_ADD", "register:40f0:8", ["const:bc1e54:8", "const:4:8"]]
+ 00bc1e54 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b534e0 bytes ec2a0294
+ 00bc1e54 bytes 2f630294
- 00b534e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
- 00b534e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
+ 00bc1e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b534e8 bytes 605201f9
+ 00bc1e5c bytes 60b600f9
- 00b534c4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1e38 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b534c4 bytes 732a00d0
+ 00bc1e38 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a06b65e56c115281d579d7e825172a"></a>

### [`00b534fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534fc.md) → [`00bc1e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1e70.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc1ea0",
      "incomplete_value": true,
      "site": "00bc1ea0",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5352c",
      "incomplete_value": true,
      "site": "00b5352c",
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
            "const:2a0:8"
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
      "definition_site": "00bc1e84",
      "incomplete_value": true,
      "site": "00bc1e84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53510",
      "incomplete_value": true,
      "site": "00b53510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1e8c",
      "incomplete_value": false,
      "site": "00bc1e98",
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
            "const:30c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53518",
      "incomplete_value": false,
      "site": "00b53524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00bc1e80",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e8c",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00bc1ea0",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1e80",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1e8c",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc1ea0",
      "WRITE",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534fc.md#insn-00b53524) · [`00b5352c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534fc.md#insn-00b5352c) · [`00b53508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534fc.md#insn-00b53508)
- 新版 `00bc1e98`（命令位置の公開資料なし） · `00bc1ea0`（命令位置の公開資料なし） · `00bc1e7c`（命令位置の公開資料なし）

~~~diff
- 00b53524 ["INT_ADD", "register:40f0:8", ["const:b53524:8", "const:4:8"]]
- 00b53524 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1e98 ["INT_ADD", "register:40f0:8", ["const:bc1e98:8", "const:4:8"]]
+ 00bc1e98 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53524 bytes db2a0294
+ 00bc1e98 bytes 1e630294
- 00b5352c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
- 00b5352c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:168:8"]]
+ 00bc1ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5352c bytes 605201f9
+ 00bc1ea0 bytes 60b600f9
- 00b53508 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc1e7c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53508 bytes 732a00d0
+ 00bc1e7c bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ae2dc8056fe6147df56e2970c316f4"></a>

### [`00b5354c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5354c.md) → [`00bc1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1ec0.md) _ZN8firebase13remote_config8internal11config_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b535a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1f18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5358c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1ed4",
      "READ",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1ee0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b535a8"
      ]
    ],
    [
      "unmatched:00b53580",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1ed4",
      "READ",
      [
        "storage",
        "01126170",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1ee0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1f1c"
      ]
    ],
    [
      "00bc1ef4",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5358c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5354c.md#insn-00b5358c) · [`00b53598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5354c.md#insn-00b53598) · [`00b535a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5354c.md#insn-00b535a4)
- 新版 `00bc1f0c`（命令位置の公開資料なし）

~~~diff
- 00b5358c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5358c ["INT_ADD", "register:40f0:8", ["const:b5358c:8", "const:4:8"]]
- 00b5358c ["CALLIND", null, ["register:0:8"]]
- 00b5358c bytes 00013fd6
- 00b53598 ["INT_ADD", "register:40f0:8", ["const:b53598:8", "const:4:8"]]
- 00b53598 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00bc1f0c ["INT_ADD", "register:40f0:8", ["const:bc1f0c:8", "const:4:8"]]
+ 00bc1f0c ["CALL", null, ["callee:00c5ab60:8"]]
- 00b53598 bytes d22a0294
+ 00bc1f0c bytes 15630294
- 00b535a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b535a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2a8:8"]]
- 00b535a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b535a4 bytes a0a20a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af0e2d61984973355499b3b032cf49e3"></a>

### [`00b535b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b535b8.md) → [`00bc1f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f2c.md) _ZN8firebase13remote_config8internal11config_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b535f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1f68"
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
      "00bc1f40",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f4c",
      "READ",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b535f8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1f40",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f4c",
      "READ",
      [
        "storage",
        "01126170",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1f6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b535d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b535b8.md#insn-00b535d0) · [`00b535f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b535b8.md#insn-00b535f4) · [`00b535fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b535b8.md#insn-00b535fc)
- 新版 `00bc1f44`（命令位置の公開資料なし）

~~~diff
- 00b535d0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b535d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc1f44 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc1f44 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b535d0 bytes 410200b4
+ 00bc1f44 bytes 410200b4
- 00b535f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b535f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b535f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2a8:8"]]
- 00b535f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b535f4 bytes bfa20a39
- 00b535fc ["INT_ADD", "register:40f0:8", ["const:b535fc:8", "const:4:8"]]
- 00b535fc ["CALL", null, ["callee:00c5ab60:8"]]
- 00b535fc bytes b92a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aedf63f05f40156c874f2da173ea3d7"></a>

### [`00b53628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53628.md) → [`00bc1f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1f9c.md) _ZN8firebase13remote_config8internal11config_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53668"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1fdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53644"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5363c",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53644",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1fe0"
      ]
    ],
    [
      "unmatched:00b5364c",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1fb0",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1fb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1fe0"
      ]
    ],
    [
      "00bc1fc0",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53628.md#insn-00b53644) · [`00b53660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53628.md#insn-00b53660) · [`00b53668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53628.md#insn-00b53668)
- 新版 `00bc1fd4`（命令位置の公開資料なし）

~~~diff
- 00b53644 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53644 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53644 bytes 410100b5
- 00b53660 ["INT_ADD", "register:40f0:8", ["const:b53660:8", "const:4:8"]]
- 00b53660 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc1fd4 ["INT_ADD", "register:40f0:8", ["const:bc1fd4:8", "const:4:8"]]
+ 00bc1fd4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53660 bytes 8c2a0294
+ 00bc1fd4 bytes cf620294
- 00b53668 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
- 00b53668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53668 bytes 805201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec7da123cdb801f37ade401c4aa8d6e"></a>

### [`00b53698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53698.md) → [`00bc200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc200c.md) _ZN8firebase13remote_config8internal11config_info11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc2028",
      "incomplete_value": false,
      "site": "00bc202c",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b536b4",
      "incomplete_value": false,
      "site": "00b536b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc2038",
      "incomplete_value": true,
      "site": "00bc2044",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b536c4",
      "incomplete_value": true,
      "site": "00b536d0",
      "value": [
        "LOAD",
        "8",
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
      "00bc2028",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc2038",
      "DATA",
      [
        "storage",
        "010a12b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2028",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc2038",
      "DATA",
      [
        "storage",
        "01126178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b536b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53698.md#insn-00b536b8) · [`00b536b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53698.md#insn-00b536b0) · [`00b536b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53698.md#insn-00b536b4)
- 新版 `00bc202c`（命令位置の公開資料なし） · `00bc2024`（命令位置の公開資料なし） · `00bc2028`（命令位置の公開資料なし）

~~~diff
- 00b536b8 ["INT_ADD", "register:40f0:8", ["const:b536b8:8", "const:4:8"]]
- 00b536b8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc202c ["INT_ADD", "register:40f0:8", ["const:bc202c:8", "const:4:8"]]
+ 00bc202c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b536b8 bytes b22a0294
+ 00bc202c bytes f5620294
- 00b536b0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc2024 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b536b0 bytes 20baffb0
+ 00bc2024 bytes 20b7ffd0
- 00b536b4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b536b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b536b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b536b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2028 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bc2028 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2028 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2028 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b536b4 bytes 001c1591
+ 00bc2028 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96ac15db59ed9f9f612429b0e4feef36"></a>

### [`00b536d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b536d4.md) → [`00bc2048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2048.md) _ZN8firebase13remote_config8internal11config_info13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2088",
      "incomplete_value": true,
      "site": "00bc2088",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53714",
      "incomplete_value": true,
      "site": "00b53714",
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
            "const:2a0:8"
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
      "definition_site": "00bc2064",
      "incomplete_value": true,
      "site": "00bc2064",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b536f0",
      "incomplete_value": true,
      "site": "00b536f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc206c",
      "incomplete_value": false,
      "site": "00bc2080",
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
            "const:30c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b536f8",
      "incomplete_value": false,
      "site": "00b5370c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00bc205c",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc206c",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00bc2088",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc205c",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc206c",
      "PARAM",
      [
        "storage",
        "002a730c",
        null,
        "string"
      ]
    ],
    [
      "00bc2088",
      "WRITE",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5370c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b536d4.md#insn-00b5370c) · [`00b53714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b536d4.md#insn-00b53714) · [`00b536e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b536d4.md#insn-00b536e0)
- 新版 `00bc2080`（命令位置の公開資料なし） · `00bc2088`（命令位置の公開資料なし） · `00bc2054`（命令位置の公開資料なし）

~~~diff
- 00b5370c ["INT_ADD", "register:40f0:8", ["const:b5370c:8", "const:4:8"]]
- 00b5370c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2080 ["INT_ADD", "register:40f0:8", ["const:bc2080:8", "const:4:8"]]
+ 00bc2080 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5370c bytes 612a0294
+ 00bc2080 bytes a4620294
- 00b53714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
- 00b53714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2088 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:168:8"]]
+ 00bc2088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53714 bytes 805201f9
+ 00bc2088 bytes 80b600f9
- 00b536e0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc2054 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b536e0 bytes 742a00d0
+ 00bc2054 bytes 342b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da62d7073cf3e0cd846ce2eccc121476"></a>

### [`00b53780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53780.md) → [`00bc20f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20f4.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b537ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2120"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2108",
      "incomplete_value": true,
      "site": "00bc2108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53794",
      "incomplete_value": true,
      "site": "00b53794",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc2104",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2108",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b537b0"
      ]
    ],
    [
      "unmatched:00b537a0",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2104",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2108",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2124"
      ]
    ],
    [
      "00bc2114",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b537a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53780.md#insn-00b537a4) · [`00b537ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53780.md#insn-00b537ac) · [`00b537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53780.md#insn-00b537bc)

~~~diff
- 00b537a4 ["INT_ADD", "register:40f0:8", ["const:b537a4:8", "const:4:8"]]
- 00b537a4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b537a4 bytes 3b2a0294
- 00b537ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
- 00b537ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b537ac bytes 606a01f9
- 00b537bc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b537bc ["RETURN", null, ["register:0:8"]]
- 00b537bc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2960de7219f20dad4b4efef5a19ba296"></a>

### [`00b537c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b537c0.md) → [`00bc2134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2134.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2160",
      "incomplete_value": true,
      "site": "00bc2160",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537ec",
      "incomplete_value": true,
      "site": "00b537ec",
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
            "const:2d0:8"
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
      "definition_site": "00bc2148",
      "incomplete_value": true,
      "site": "00bc2148",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b537d4",
      "incomplete_value": true,
      "site": "00b537d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2150",
      "incomplete_value": false,
      "site": "00bc2158",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537dc",
      "incomplete_value": false,
      "site": "00b537e4",
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
            "const:f3e:8"
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
      "00bc2144",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2150",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00bc2160",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2144",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2150",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ],
    [
      "00bc2160",
      "WRITE",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b537e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b537c0.md#insn-00b537e4) · [`00b537ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b537c0.md#insn-00b537ec) · [`00b537cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b537c0.md#insn-00b537cc)
- 新版 `00bc2158`（命令位置の公開資料なし） · `00bc2160`（命令位置の公開資料なし） · `00bc2140`（命令位置の公開資料なし）

~~~diff
- 00b537e4 ["INT_ADD", "register:40f0:8", ["const:b537e4:8", "const:4:8"]]
- 00b537e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2158 ["INT_ADD", "register:40f0:8", ["const:bc2158:8", "const:4:8"]]
+ 00bc2158 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b537e4 bytes 2b2a0294
+ 00bc2158 bytes 6e620294
- 00b537ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
- 00b537ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:198:8"]]
+ 00bc2160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b537ec bytes 606a01f9
+ 00bc2160 bytes 60ce00f9
- 00b537cc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2140 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b537cc bytes 732a00d0
+ 00bc2140 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab936c1cf74bbf241c4a54b642bd14a"></a>

### [`00b53844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53844.md) → [`00bc21b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc21b8.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53848"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53844",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53848",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53854",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc21b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc21bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc21c8",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53844.md#insn-00b53844) · [`00b53848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53844.md#insn-00b53848) · [`00b53858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53844.md#insn-00b53858)

~~~diff
- 00b53844 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b53844 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53844 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53844 bytes f30f1ef8
- 00b53848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53848 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53848 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53848 bytes fd7b01a9
- 00b53858 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53858 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53858 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57131f0c5d0cbe3c84dad50e9f8d98e6"></a>

### [`00b53894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53894.md) → [`00bc2208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2208.md) _ZN8firebase13remote_config8internal15config_settings15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2260",
      "incomplete_value": true,
      "site": "00bc2260",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b538ec",
      "incomplete_value": true,
      "site": "00b538ec",
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
            "const:2d8:8"
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
      "definition_site": "00bc223c",
      "incomplete_value": true,
      "site": "00bc2248",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:198:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b538c8",
      "incomplete_value": true,
      "site": "00b538d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:2d0:8"
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
      "00bc221c",
      "READ",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc223c",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2260",
      "WRITE",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc221c",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc223c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2260",
      "WRITE",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b538d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53894.md#insn-00b538d4) · [`00b538ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53894.md#insn-00b538ec) · [`00b538a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53894.md#insn-00b538a4)
- 新版 `00bc2248`（命令位置の公開資料なし） · `00bc2260`（命令位置の公開資料なし） · `00bc2218`（命令位置の公開資料なし）

~~~diff
- 00b538d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b538d4 ["INT_ADD", "register:40f0:8", ["const:b538d4:8", "const:4:8"]]
- 00b538d4 ["CALLIND", null, ["register:0:8"]]
+ 00bc2248 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2248 ["INT_ADD", "register:40f0:8", ["const:bc2248:8", "const:4:8"]]
+ 00bc2248 ["CALLIND", null, ["register:0:8"]]
- 00b538d4 bytes 00013fd6
+ 00bc2248 bytes 00013fd6
- 00b538ec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b538ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2d8:8"]]
- 00b538ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2260 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2260 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1a0:8"]]
+ 00bc2260 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b538ec bytes a0620b39
+ 00bc2260 bytes a0820639
- 00b538a4 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc2218 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b538a4 bytes 752a00d0
+ 00bc2218 bytes 352b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618563acba5f2d45bab9621a6c6aa392"></a>

### [`00b53900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53900.md) → [`00bc2274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2274.md) _ZN8firebase13remote_config8internal15config_settings12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bc22b0",
      "incomplete_value": true,
      "site": "00bc22b0",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5393c",
      "incomplete_value": true,
      "site": "00b5393c",
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
            "const:2d8:8"
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
      "definition_site": "00bc22d0",
      "incomplete_value": true,
      "site": "00bc22d0",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5395c",
      "incomplete_value": true,
      "site": "00b5395c",
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
            "const:2d0:8"
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
      "definition_site": "00bc228c",
      "incomplete_value": true,
      "site": "00bc228c",
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
      "definition_site": "00b53918",
      "incomplete_value": true,
      "site": "00b53918",
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
      "00bc2288",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2294",
      "READ",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc22b0",
      "WRITE",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2288",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2294",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc22b0",
      "WRITE",
      [
        "storage",
        "011261a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5393c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53900.md#insn-00b5393c) · [`00b53958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53900.md#insn-00b53958) · [`00b5395c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53900.md#insn-00b5395c)
- 新版 `00bc22b0`（命令位置の公開資料なし） · `00bc22cc`（命令位置の公開資料なし） · `00bc22d0`（命令位置の公開資料なし）

~~~diff
- 00b5393c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5393c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5393c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2d8:8"]]
- 00b5393c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc22b0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc22b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc22b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1a0:8"]]
+ 00bc22b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5393c bytes bf620b39
+ 00bc22b0 bytes bf820639
- 00b53958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53958 ["INT_ADD", "register:40f0:8", ["const:b53958:8", "const:4:8"]]
- 00b53958 ["CALLIND", null, ["register:0:8"]]
+ 00bc22cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc22cc ["INT_ADD", "register:40f0:8", ["const:bc22cc:8", "const:4:8"]]
+ 00bc22cc ["CALLIND", null, ["register:0:8"]]
- 00b53958 bytes 00013fd6
+ 00bc22cc bytes 00013fd6
- 00b5395c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
- 00b5395c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5395c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc22d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:198:8"]]
+ 00bc22d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc22d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5395c bytes 9f6a01f9
+ 00bc22d0 bytes 9fce00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802f9baa20b199aba4fa343ba85daa92"></a>

### [`00b53970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53970.md) → [`00bc22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc22e4.md) _ZN8firebase13remote_config8internal15config_settings14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b53970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53974"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53970",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53974",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53984",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc22e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc22e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc22f8",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53970.md#insn-00b53970) · [`00b53974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53970.md#insn-00b53974) · [`00b5398c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53970.md#insn-00b5398c)

~~~diff
- 00b53970 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53970 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53970 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53970 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53970 bytes f44fbea9
- 00b53974 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53974 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53974 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53974 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53974 bytes fd7b01a9
- 00b5398c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5398c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5398c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09cb3b0387100407fca5641be12ea60a"></a>

### [`00b539e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b539e0.md) → [`00bc2354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2354.md) _ZN8firebase13remote_config8internal15config_settings11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc2370",
      "incomplete_value": false,
      "site": "00bc2374",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539fc",
      "incomplete_value": false,
      "site": "00b53a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc2380",
      "incomplete_value": true,
      "site": "00bc238c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53a0c",
      "incomplete_value": true,
      "site": "00b53a18",
      "value": [
        "LOAD",
        "8",
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
      "00bc2370",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc2380",
      "DATA",
      [
        "storage",
        "010a12e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2370",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc2380",
      "DATA",
      [
        "storage",
        "011261a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b539e0.md#insn-00b53a00) · [`00b539f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b539e0.md#insn-00b539f8) · [`00b539fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b539e0.md#insn-00b539fc)
- 新版 `00bc2374`（命令位置の公開資料なし） · `00bc236c`（命令位置の公開資料なし） · `00bc2370`（命令位置の公開資料なし）

~~~diff
- 00b53a00 ["INT_ADD", "register:40f0:8", ["const:b53a00:8", "const:4:8"]]
- 00b53a00 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc2374 ["INT_ADD", "register:40f0:8", ["const:bc2374:8", "const:4:8"]]
+ 00bc2374 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53a00 bytes e0290294
+ 00bc2374 bytes 23620294
- 00b539f8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc236c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b539f8 bytes 20baffb0
+ 00bc236c bytes 20b7ffd0
- 00b539fc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b539fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b539fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b539fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2370 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bc2370 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2370 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2370 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b539fc bytes 001c1591
+ 00bc2370 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdaa9393ce2335a4d91084843935863c"></a>

### [`00b53a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a1c.md) → [`00bc2390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2390.md) _ZN8firebase13remote_config8internal15config_settings13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc23d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53a38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53a30",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53a38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc23d4"
      ]
    ],
    [
      "unmatched:00b53a40",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc23a4",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc23d4"
      ]
    ],
    [
      "00bc23b4",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a1c.md#insn-00b53a38) · [`00b53a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a1c.md#insn-00b53a54) · [`00b53a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a1c.md#insn-00b53a5c)
- 新版 `00bc23c8`（命令位置の公開資料なし）

~~~diff
- 00b53a38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53a38 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53a38 bytes 410100b5
- 00b53a54 ["INT_ADD", "register:40f0:8", ["const:b53a54:8", "const:4:8"]]
- 00b53a54 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc23c8 ["INT_ADD", "register:40f0:8", ["const:bc23c8:8", "const:4:8"]]
+ 00bc23c8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53a54 bytes 8f290294
+ 00bc23c8 bytes d2610294
- 00b53a5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
- 00b53a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53a5c bytes 806a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ef1b801989f555d32e37847e11626d"></a>

### [`00b53a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a8c.md) → [`00bc2400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2400.md) _ZN8firebase13remote_config8internal15config_settings10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc241c",
      "incomplete_value": false,
      "site": "00bc2420",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53aa8",
      "incomplete_value": false,
      "site": "00b53aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bc242c",
      "incomplete_value": true,
      "site": "00bc2438",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53ab8",
      "incomplete_value": true,
      "site": "00b53ac4",
      "value": [
        "LOAD",
        "8",
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
      "00bc241c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bc242c",
      "DATA",
      [
        "storage",
        "010a12f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc241c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc242c",
      "DATA",
      [
        "storage",
        "011261b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a8c.md#insn-00b53aac) · [`00b53aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a8c.md#insn-00b53aa4) · [`00b53aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a8c.md#insn-00b53aa8)
- 新版 `00bc2420`（命令位置の公開資料なし） · `00bc2418`（命令位置の公開資料なし） · `00bc241c`（命令位置の公開資料なし）

~~~diff
- 00b53aac ["INT_ADD", "register:40f0:8", ["const:b53aac:8", "const:4:8"]]
- 00b53aac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc2420 ["INT_ADD", "register:40f0:8", ["const:bc2420:8", "const:4:8"]]
+ 00bc2420 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53aac bytes b5290294
+ 00bc2420 bytes f8610294
- 00b53aa4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bc2418 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b53aa4 bytes 20baffd0
+ 00bc2418 bytes 20b7fff0
- 00b53aa8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b53aa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53aa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53aa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc241c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bc241c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc241c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc241c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53aa8 bytes 00c81791
+ 00bc241c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b30394b68a28bbfa7b246e9d97d980"></a>

### [`00b53ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ac8.md) → [`00bc243c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc243c.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2468",
      "incomplete_value": true,
      "site": "00bc2468",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53af4",
      "incomplete_value": true,
      "site": "00b53af4",
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
            "const:2f8:8"
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
      "definition_site": "00bc2450",
      "incomplete_value": true,
      "site": "00bc2450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53adc",
      "incomplete_value": true,
      "site": "00b53adc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc245c",
      "incomplete_value": false,
      "site": "00bc2460",
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
            "const:b9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ae8",
      "incomplete_value": false,
      "site": "00b53aec",
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
            "const:f07:8"
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
      "00bc244c",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc245c",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00bc2468",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc244c",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc245c",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ],
    [
      "00bc2468",
      "WRITE",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ac8.md#insn-00b53aec) · [`00b53af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ac8.md#insn-00b53af4) · [`00b53ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ac8.md#insn-00b53ad4)
- 新版 `00bc2460`（命令位置の公開資料なし） · `00bc2468`（命令位置の公開資料なし） · `00bc2448`（命令位置の公開資料なし）

~~~diff
- 00b53aec ["INT_ADD", "register:40f0:8", ["const:b53aec:8", "const:4:8"]]
- 00b53aec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2460 ["INT_ADD", "register:40f0:8", ["const:bc2460:8", "const:4:8"]]
+ 00bc2460 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53aec bytes 69290294
+ 00bc2460 bytes ac610294
- 00b53af4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b53af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1c0:8"]]
+ 00bc2468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53af4 bytes 607e01f9
+ 00bc2468 bytes 60e200f9
- 00b53ad4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2448 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53ad4 bytes 732a00d0
+ 00bc2448 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b600f1b86e61b35c6e14377f93794a5d"></a>

### [`00b53b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b08.md) → [`00bc247c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc247c.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc24a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2490",
      "incomplete_value": true,
      "site": "00bc2490",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53b1c",
      "incomplete_value": true,
      "site": "00b53b1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc248c",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2490",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53b38"
      ]
    ],
    [
      "unmatched:00b53b24",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc248c",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2490",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24ac"
      ]
    ],
    [
      "00bc2498",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b08.md#insn-00b53b2c) · [`00b53b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b08.md#insn-00b53b34) · [`00b53b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b08.md#insn-00b53b44)

~~~diff
- 00b53b2c ["INT_ADD", "register:40f0:8", ["const:b53b2c:8", "const:4:8"]]
- 00b53b2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53b2c bytes 59290294
- 00b53b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b53b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53b34 bytes 607e01f9
- 00b53b44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53b44 ["RETURN", null, ["register:0:8"]]
- 00b53b44 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab49aee31262cd012d4f217534a0867c"></a>

### [`00b53b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b48.md) → [`00bc24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc24bc.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc24ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc24d0",
      "incomplete_value": true,
      "site": "00bc24d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc24cc",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc24d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53b7c"
      ]
    ],
    [
      "unmatched:00b53b68",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc24cc",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc24d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24f0"
      ]
    ],
    [
      "00bc24dc",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b48.md#insn-00b53b70) · [`00b53b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b48.md#insn-00b53b78) · [`00b53b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b48.md#insn-00b53b88)

~~~diff
- 00b53b70 ["INT_ADD", "register:40f0:8", ["const:b53b70:8", "const:4:8"]]
- 00b53b70 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53b70 bytes 48290294
- 00b53b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b53b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53b78 bytes 607e01f9
- 00b53b88 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53b88 ["RETURN", null, ["register:0:8"]]
- 00b53b88 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f9f51866d18847eb9606387ea61534"></a>

### [`00b53b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b8c.md) → [`00bc2500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2500.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b53bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2530"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2514",
      "incomplete_value": true,
      "site": "00bc2514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53ba0",
      "incomplete_value": true,
      "site": "00b53ba0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bc2510",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53ba8",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53bbc",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2510",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc251c",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ],
    [
      "00bc2530",
      "WRITE",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b8c.md#insn-00b53ba0) · [`00b53bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b8c.md#insn-00b53bb4) · [`00b53bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b8c.md#insn-00b53bbc)
- 新版 `00bc2514`（命令位置の公開資料なし） · `00bc2528`（命令位置の公開資料なし）

~~~diff
- 00b53ba0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53ba0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc2514 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2514 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53ba0 bytes 080100b5
+ 00bc2514 bytes 080100b5
- 00b53bb4 ["INT_ADD", "register:40f0:8", ["const:b53bb4:8", "const:4:8"]]
- 00b53bb4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2528 ["INT_ADD", "register:40f0:8", ["const:bc2528:8", "const:4:8"]]
+ 00bc2528 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53bb4 bytes 37290294
+ 00bc2528 bytes 7a610294
- 00b53bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b53bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53bbc bytes 607e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e4087a32046da2cc198dc9749b08beb"></a>

### [`00b53c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53c48.md) → [`00bc25bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc25bc.md) _ZN8firebase13remote_config8internal23config_settings_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc25f8"
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
      "00bc25d0",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53ca8"
      ]
    ],
    [
      "00bc25dc",
      "READ",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc25d0",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc261c"
      ]
    ],
    [
      "00bc25dc",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53c48.md#insn-00b53c60) · [`00b53c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53c48.md#insn-00b53c84) · [`00b53c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53c48.md#insn-00b53c8c)
- 新版 `00bc25d4`（命令位置の公開資料なし）

~~~diff
- 00b53c60 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53c60 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc25d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc25d4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b53c60 bytes 410200b4
+ 00bc25d4 bytes 410200b4
- 00b53c84 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53c84 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53c84 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:300:8"]]
- 00b53c84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53c84 bytes bf020c39
- 00b53c8c ["INT_ADD", "register:40f0:8", ["const:b53c8c:8", "const:4:8"]]
- 00b53c8c ["CALL", null, ["callee:00c5ab60:8"]]
- 00b53c8c bytes 15290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8075d842b165fdda5ef26a2e716646a7"></a>

### [`00b53cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53cb8.md) → [`00bc262c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc262c.md) _ZN8firebase13remote_config8internal23config_settings_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b53cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc266c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53cd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53ccc",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53cd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2670"
      ]
    ],
    [
      "unmatched:00b53cdc",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2640",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2670"
      ]
    ],
    [
      "00bc2650",
      "PARAM",
      [
        "storage",
        "002b9b9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53cb8.md#insn-00b53cd4) · [`00b53cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53cb8.md#insn-00b53cf0) · [`00b53cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53cb8.md#insn-00b53cf8)
- 新版 `00bc2664`（命令位置の公開資料なし）

~~~diff
- 00b53cd4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53cd4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53cd4 bytes 410100b5
- 00b53cf0 ["INT_ADD", "register:40f0:8", ["const:b53cf0:8", "const:4:8"]]
- 00b53cf0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2664 ["INT_ADD", "register:40f0:8", ["const:bc2664:8", "const:4:8"]]
+ 00bc2664 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53cf0 bytes e8280294
+ 00bc2664 bytes 2b610294
- 00b53cf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00b53cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53cf8 bytes 807e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40e9af41381f29157850e8b6c372024e"></a>

### [`00b53d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d64.md) → [`00bc26d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc26d8.md) _ZN8firebase13remote_config8internal23config_settings_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b53d64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53d68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53d78",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc26d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc26dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc26ec",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d64.md#insn-00b53d64) · [`00b53d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d64.md#insn-00b53d68) · [`00b53d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d64.md#insn-00b53d80)

~~~diff
- 00b53d64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53d64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53d64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53d64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53d64 bytes f44fbea9
- 00b53d68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53d68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53d68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53d68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53d68 bytes fd7b01a9
- 00b53d80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53d80 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53d80 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9777272181caba58bcf2bf2910dbed74"></a>

### [`00b53e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md) → [`00bc2acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2acc.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2af8",
      "incomplete_value": true,
      "site": "00bc2af8",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e3c",
      "incomplete_value": true,
      "site": "00b53e3c",
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
            "const:330:8"
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
      "definition_site": "00bc2ae0",
      "incomplete_value": true,
      "site": "00bc2ae0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53e24",
      "incomplete_value": true,
      "site": "00b53e24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2aec",
      "incomplete_value": false,
      "site": "00bc2af0",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e30",
      "incomplete_value": false,
      "site": "00b53e34",
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
            "const:f51:8"
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
      "00bc2adc",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2aec",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00bc2af8",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2adc",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2aec",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2af8",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md#insn-00b53e34) · [`00b53e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md#insn-00b53e3c) · [`00b53e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md#insn-00b53e1c)
- 新版 `00bc2af0`（命令位置の公開資料なし） · `00bc2af8`（命令位置の公開資料なし） · `00bc2ad8`（命令位置の公開資料なし）

~~~diff
- 00b53e34 ["INT_ADD", "register:40f0:8", ["const:b53e34:8", "const:4:8"]]
- 00b53e34 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2af0 ["INT_ADD", "register:40f0:8", ["const:bc2af0:8", "const:4:8"]]
+ 00bc2af0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53e34 bytes 97280294
+ 00bc2af0 bytes 08600294
- 00b53e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b53e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
+ 00bc2af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53e3c bytes 609a01f9
+ 00bc2af8 bytes 601e01f9
- 00b53e1c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2ad8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53e1c bytes 732a00d0
+ 00bc2ad8 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebdbd3b576fc9bb2ed393e6ac81dfc46"></a>

### [`00b53e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e50.md) → [`00bc2b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b0c.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2b38",
      "incomplete_value": true,
      "site": "00bc2b38",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e7c",
      "incomplete_value": true,
      "site": "00b53e7c",
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
            "const:330:8"
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
      "definition_site": "00bc2b20",
      "incomplete_value": true,
      "site": "00bc2b20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53e64",
      "incomplete_value": true,
      "site": "00b53e64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2b28",
      "incomplete_value": false,
      "site": "00bc2b30",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e6c",
      "incomplete_value": false,
      "site": "00b53e74",
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
            "const:f51:8"
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
      "00bc2b1c",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b28",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00bc2b38",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b1c",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b28",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2b38",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e50.md#insn-00b53e74) · [`00b53e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e50.md#insn-00b53e7c) · [`00b53e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e50.md#insn-00b53e5c)
- 新版 `00bc2b30`（命令位置の公開資料なし） · `00bc2b38`（命令位置の公開資料なし） · `00bc2b18`（命令位置の公開資料なし）

~~~diff
- 00b53e74 ["INT_ADD", "register:40f0:8", ["const:b53e74:8", "const:4:8"]]
- 00b53e74 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2b30 ["INT_ADD", "register:40f0:8", ["const:bc2b30:8", "const:4:8"]]
+ 00bc2b30 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53e74 bytes 87280294
+ 00bc2b30 bytes f85f0294
- 00b53e7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b53e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
+ 00bc2b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53e7c bytes 609a01f9
+ 00bc2b38 bytes 601e01f9
- 00b53e5c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2b18 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53e5c bytes 732a00d0
+ 00bc2b18 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24419643b440f65e8392dad8ea9e2c24"></a>

### [`00b53e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e90.md) → [`00bc2b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b4c.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2b7c",
      "incomplete_value": true,
      "site": "00bc2b7c",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ec0",
      "incomplete_value": true,
      "site": "00b53ec0",
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
            "const:330:8"
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
      "definition_site": "00bc2b60",
      "incomplete_value": true,
      "site": "00bc2b60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53ea4",
      "incomplete_value": true,
      "site": "00b53ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2b6c",
      "incomplete_value": false,
      "site": "00bc2b74",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53eb0",
      "incomplete_value": false,
      "site": "00b53eb8",
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
            "const:f51:8"
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
      "00bc2b5c",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b6c",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00bc2b7c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b5c",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b6c",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2b7c",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e90.md#insn-00b53eb8) · [`00b53ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e90.md#insn-00b53ec0) · [`00b53e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e90.md#insn-00b53e9c)
- 新版 `00bc2b74`（命令位置の公開資料なし） · `00bc2b7c`（命令位置の公開資料なし） · `00bc2b58`（命令位置の公開資料なし）

~~~diff
- 00b53eb8 ["INT_ADD", "register:40f0:8", ["const:b53eb8:8", "const:4:8"]]
- 00b53eb8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2b74 ["INT_ADD", "register:40f0:8", ["const:bc2b74:8", "const:4:8"]]
+ 00bc2b74 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53eb8 bytes 76280294
+ 00bc2b74 bytes e75f0294
- 00b53ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b53ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
+ 00bc2b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53ec0 bytes 609a01f9
+ 00bc2b7c bytes 601e01f9
- 00b53e9c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2b58 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53e9c bytes 732a00d0
+ 00bc2b58 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a5917699cace7a8d558956da90eba1"></a>

### [`00b53ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ed4.md) → [`00bc2b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2b90.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2bc0",
      "incomplete_value": true,
      "site": "00bc2bc0",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f04",
      "incomplete_value": true,
      "site": "00b53f04",
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
            "const:330:8"
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
      "definition_site": "00bc2ba4",
      "incomplete_value": true,
      "site": "00bc2ba4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b53ee8",
      "incomplete_value": true,
      "site": "00b53ee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2bac",
      "incomplete_value": false,
      "site": "00bc2bb8",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ef0",
      "incomplete_value": false,
      "site": "00b53efc",
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
            "const:f51:8"
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
      "00bc2ba0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2bac",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00bc2bc0",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ba0",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2bac",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ],
    [
      "00bc2bc0",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ed4.md#insn-00b53efc) · [`00b53f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ed4.md#insn-00b53f04) · [`00b53ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ed4.md#insn-00b53ee0)
- 新版 `00bc2bb8`（命令位置の公開資料なし） · `00bc2bc0`（命令位置の公開資料なし） · `00bc2b9c`（命令位置の公開資料なし）

~~~diff
- 00b53efc ["INT_ADD", "register:40f0:8", ["const:b53efc:8", "const:4:8"]]
- 00b53efc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2bb8 ["INT_ADD", "register:40f0:8", ["const:bc2bb8:8", "const:4:8"]]
+ 00bc2bb8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53efc bytes 65280294
+ 00bc2bb8 bytes d65f0294
- 00b53f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b53f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:238:8"]]
+ 00bc2bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53f04 bytes 609a01f9
+ 00bc2bc0 bytes 601e01f9
- 00b53ee0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2b9c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b53ee0 bytes 732a00d0
+ 00bc2b9c bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653ffa73d8c81ba000d3f1b572aaf891"></a>

### [`00b53f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f24.md) → [`00bc2be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2be0.md) _ZN8firebase13remote_config8internal19throttled_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2c38",
      "incomplete_value": true,
      "site": "00bc2c38",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f7c",
      "incomplete_value": true,
      "site": "00b53f7c",
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
            "const:338:8"
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
      "definition_site": "00bc2c14",
      "incomplete_value": true,
      "site": "00bc2c20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:238:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f58",
      "incomplete_value": true,
      "site": "00b53f64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:330:8"
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
      "00bc2bf4",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2c14",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c38",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2bf4",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2c14",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2c38",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f24.md#insn-00b53f64) · [`00b53f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f24.md#insn-00b53f7c) · [`00b53f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f24.md#insn-00b53f34)
- 新版 `00bc2c20`（命令位置の公開資料なし） · `00bc2c38`（命令位置の公開資料なし） · `00bc2bf0`（命令位置の公開資料なし）

~~~diff
- 00b53f64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53f64 ["INT_ADD", "register:40f0:8", ["const:b53f64:8", "const:4:8"]]
- 00b53f64 ["CALLIND", null, ["register:0:8"]]
+ 00bc2c20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2c20 ["INT_ADD", "register:40f0:8", ["const:bc2c20:8", "const:4:8"]]
+ 00bc2c20 ["CALLIND", null, ["register:0:8"]]
- 00b53f64 bytes 00013fd6
+ 00bc2c20 bytes 00013fd6
- 00b53f7c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53f7c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:338:8"]]
- 00b53f7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2c38 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2c38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:240:8"]]
+ 00bc2c38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53f7c bytes a0e20c39
+ 00bc2c38 bytes a0020939
- 00b53f34 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc2bf0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b53f34 bytes 752a00d0
+ 00bc2bf0 bytes 352b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a92d1faa2f9fd55c452c162fd540881e"></a>

### [`00b54000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md) → [`00bc2cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2cbc.md) _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b54040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2cfc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5401c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54014",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5401c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2d00"
      ]
    ],
    [
      "unmatched:00b54024",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2cd0",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2d00"
      ]
    ],
    [
      "00bc2ce0",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5401c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md#insn-00b5401c) · [`00b54038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md#insn-00b54038) · [`00b54040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md#insn-00b54040)
- 新版 `00bc2cf4`（命令位置の公開資料なし）

~~~diff
- 00b5401c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5401c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5401c bytes 410100b5
- 00b54038 ["INT_ADD", "register:40f0:8", ["const:b54038:8", "const:4:8"]]
- 00b54038 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2cf4 ["INT_ADD", "register:40f0:8", ["const:bc2cf4:8", "const:4:8"]]
+ 00bc2cf4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54038 bytes 16280294
+ 00bc2cf4 bytes 875f0294
- 00b54040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b54040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54040 bytes 809a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ff8d526b042d63f0d98d04d2b5495e"></a>

### [`00b540ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b540ac.md) → [`00bc2d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d68.md) _ZN8firebase13remote_config8internal19throttled_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b540ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2da8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b540c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b540c0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b540c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2dac"
      ]
    ],
    [
      "unmatched:00b540d0",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2d7c",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2dac"
      ]
    ],
    [
      "00bc2d8c",
      "PARAM",
      [
        "storage",
        "002b9be8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b540c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b540ac.md#insn-00b540c8) · [`00b540e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b540ac.md#insn-00b540e4) · [`00b540ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b540ac.md#insn-00b540ec)
- 新版 `00bc2da0`（命令位置の公開資料なし）

~~~diff
- 00b540c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b540c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b540c8 bytes 410100b5
- 00b540e4 ["INT_ADD", "register:40f0:8", ["const:b540e4:8", "const:4:8"]]
- 00b540e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2da0 ["INT_ADD", "register:40f0:8", ["const:bc2da0:8", "const:4:8"]]
+ 00bc2da0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b540e4 bytes eb270294
+ 00bc2da0 bytes 5c5f0294
- 00b540ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b540ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b540ec bytes 809a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19ae9913748a10b51c5ce0e9adbaf358"></a>

### [`00b54158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54158.md) → [`00bc2e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e14.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2e40",
      "incomplete_value": true,
      "site": "00bc2e40",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54184",
      "incomplete_value": true,
      "site": "00b54184",
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
            "const:350:8"
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
      "definition_site": "00bc2e28",
      "incomplete_value": true,
      "site": "00bc2e28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5416c",
      "incomplete_value": true,
      "site": "00b5416c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2e34",
      "incomplete_value": false,
      "site": "00bc2e38",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54178",
      "incomplete_value": false,
      "site": "00b5417c",
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
            "const:32d:8"
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
      "00bc2e24",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e34",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00bc2e40",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e24",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e34",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc2e40",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54158.md#insn-00b5417c) · [`00b54184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54158.md#insn-00b54184) · [`00b54164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54158.md#insn-00b54164)
- 新版 `00bc2e38`（命令位置の公開資料なし） · `00bc2e40`（命令位置の公開資料なし） · `00bc2e20`（命令位置の公開資料なし）

~~~diff
- 00b5417c ["INT_ADD", "register:40f0:8", ["const:b5417c:8", "const:4:8"]]
- 00b5417c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2e38 ["INT_ADD", "register:40f0:8", ["const:bc2e38:8", "const:4:8"]]
+ 00bc2e38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5417c bytes c5270294
+ 00bc2e38 bytes 365f0294
- 00b54184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00bc2e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54184 bytes 60aa01f9
+ 00bc2e40 bytes 602e01f9
- 00b54164 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2e20 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b54164 bytes 732a00b0
+ 00bc2e20 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba81d3ef47d6254fc6ee4e4cd801def"></a>

### [`00b54198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54198.md) → [`00bc2e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e54.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2e80",
      "incomplete_value": true,
      "site": "00bc2e80",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541c4",
      "incomplete_value": true,
      "site": "00b541c4",
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
            "const:350:8"
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
      "definition_site": "00bc2e68",
      "incomplete_value": true,
      "site": "00bc2e68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b541ac",
      "incomplete_value": true,
      "site": "00b541ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2e70",
      "incomplete_value": false,
      "site": "00bc2e78",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541b4",
      "incomplete_value": false,
      "site": "00b541bc",
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
            "const:32d:8"
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
      "00bc2e64",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e70",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00bc2e80",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e64",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e70",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc2e80",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b541bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54198.md#insn-00b541bc) · [`00b541c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54198.md#insn-00b541c4) · [`00b541a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54198.md#insn-00b541a4)
- 新版 `00bc2e78`（命令位置の公開資料なし） · `00bc2e80`（命令位置の公開資料なし） · `00bc2e60`（命令位置の公開資料なし）

~~~diff
- 00b541bc ["INT_ADD", "register:40f0:8", ["const:b541bc:8", "const:4:8"]]
- 00b541bc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2e78 ["INT_ADD", "register:40f0:8", ["const:bc2e78:8", "const:4:8"]]
+ 00bc2e78 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b541bc bytes b5270294
+ 00bc2e78 bytes 265f0294
- 00b541c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b541c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00bc2e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b541c4 bytes 60aa01f9
+ 00bc2e80 bytes 602e01f9
- 00b541a4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2e60 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b541a4 bytes 732a00b0
+ 00bc2e60 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925fe849a82baa8cbdbc07b502927f1c"></a>

### [`00b541d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b541d8.md) → [`00bc2e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2e94.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b541d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b541dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b541dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b541d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b541dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2ea4",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2ea4",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b541d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b541d8.md#insn-00b541d8) · [`00b541dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b541d8.md#insn-00b541dc) · [`00b541ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b541d8.md#insn-00b541ec)
- 新版 `00bc2ea8`（命令位置の公開資料なし）

~~~diff
- 00b541d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b541d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b541d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b541d8 bytes f30f1ef8
- 00b541dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b541dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b541dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b541dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b541dc bytes fd7b01a9
- 00b541ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b541ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc2ea8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2ea8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b541ec bytes 080100b5
+ 00bc2ea8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-329a2a131e30d69261e1f91f9c9c389b"></a>

### [`00b5421c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5421c.md) → [`00bc2ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2ed8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc2f08",
      "incomplete_value": true,
      "site": "00bc2f08",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5424c",
      "incomplete_value": true,
      "site": "00b5424c",
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
            "const:350:8"
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
      "definition_site": "00bc2eec",
      "incomplete_value": true,
      "site": "00bc2eec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b54230",
      "incomplete_value": true,
      "site": "00b54230",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc2ef4",
      "incomplete_value": false,
      "site": "00bc2f00",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54238",
      "incomplete_value": false,
      "site": "00b54244",
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
            "const:32d:8"
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
      "00bc2ee8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ef4",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00bc2f08",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ee8",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ef4",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc2f08",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5421c.md#insn-00b54244) · [`00b5424c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5421c.md#insn-00b5424c) · [`00b54228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5421c.md#insn-00b54228)
- 新版 `00bc2f00`（命令位置の公開資料なし） · `00bc2f08`（命令位置の公開資料なし） · `00bc2ee4`（命令位置の公開資料なし）

~~~diff
- 00b54244 ["INT_ADD", "register:40f0:8", ["const:b54244:8", "const:4:8"]]
- 00b54244 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc2f00 ["INT_ADD", "register:40f0:8", ["const:bc2f00:8", "const:4:8"]]
+ 00bc2f00 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54244 bytes 93270294
+ 00bc2f00 bytes 045f0294
- 00b5424c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b5424c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2f08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00bc2f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5424c bytes 60aa01f9
+ 00bc2f08 bytes 602e01f9
- 00b54228 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc2ee4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b54228 bytes 732a00b0
+ 00bc2ee4 bytes 332b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ea45b8735a23302a9b9e1364e2d72c"></a>

### [`00b5426c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5426c.md) → [`00bc2f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f28.md) _ZN8firebase13remote_config8internal26jni_config_update_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2f80",
      "incomplete_value": true,
      "site": "00bc2f80",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b542c4",
      "incomplete_value": true,
      "site": "00b542c4",
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
            "const:358:8"
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
      "definition_site": "00bc2f5c",
      "incomplete_value": true,
      "site": "00bc2f68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:258:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b542a0",
      "incomplete_value": true,
      "site": "00b542ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "00bc2f3c",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2f5c",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f80",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2f3c",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2f5c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f80",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b542ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5426c.md#insn-00b542ac) · [`00b542c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5426c.md#insn-00b542c4) · [`00b5427c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5426c.md#insn-00b5427c)
- 新版 `00bc2f68`（命令位置の公開資料なし） · `00bc2f80`（命令位置の公開資料なし） · `00bc2f38`（命令位置の公開資料なし）

~~~diff
- 00b542ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b542ac ["INT_ADD", "register:40f0:8", ["const:b542ac:8", "const:4:8"]]
- 00b542ac ["CALLIND", null, ["register:0:8"]]
+ 00bc2f68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2f68 ["INT_ADD", "register:40f0:8", ["const:bc2f68:8", "const:4:8"]]
+ 00bc2f68 ["CALLIND", null, ["register:0:8"]]
- 00b542ac bytes 00013fd6
+ 00bc2f68 bytes 00013fd6
- 00b542c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b542c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:358:8"]]
- 00b542c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2f80 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2f80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
+ 00bc2f80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b542c4 bytes a0620d39
+ 00bc2f80 bytes a0820939
- 00b5427c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc2f38 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b5427c bytes 752a00b0
+ 00bc2f38 bytes 352b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8028fd5ab28b8acc08cc63ebd0f4b50"></a>

### [`00b542d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b542d8.md) → [`00bc2f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f94.md) _ZN8firebase13remote_config8internal26jni_config_update_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2fd0"
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
      "00bc2fa8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2fb4",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b54318"
      ]
    ]
  ],
  "added": [
    [
      "00bc2fa8",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2fb4",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2fd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b542f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b542d8.md#insn-00b542f0) · [`00b54310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b542d8.md#insn-00b54310) · [`00b54314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b542d8.md#insn-00b54314)
- 新版 `00bc2fac`（命令位置の公開資料なし）

~~~diff
- 00b542f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b542f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bc2fac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc2fac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b542f0 bytes 410200b4
+ 00bc2fac bytes 410200b4
- 00b54310 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54310 ["INT_ADD", "register:40f0:8", ["const:b54310:8", "const:4:8"]]
- 00b54310 ["CALLIND", null, ["register:0:8"]]
- 00b54310 bytes 00013fd6
- 00b54314 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54314 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54314 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
- 00b54314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54314 bytes bf620d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e744c989d38690382ddda2845b9e2f"></a>

### [`00b54348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54348.md) → [`00bc3004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3004.md) _ZN8firebase13remote_config8internal26jni_config_update_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00bc3044",
      "incomplete_value": true,
      "site": "00bc3044",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54388",
      "incomplete_value": true,
      "site": "00b54388",
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
            "const:350:8"
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
      "definition_site": "00bc3020",
      "incomplete_value": true,
      "site": "00bc3020",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b54364",
      "incomplete_value": true,
      "site": "00b54364",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc3028",
      "incomplete_value": false,
      "site": "00bc303c",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5436c",
      "incomplete_value": false,
      "site": "00b54380",
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
            "const:32d:8"
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
      "00bc3018",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3028",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00bc3044",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3018",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3028",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ],
    [
      "00bc3044",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54348.md#insn-00b54380) · [`00b54388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54348.md#insn-00b54388) · [`00b54354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54348.md#insn-00b54354)
- 新版 `00bc303c`（命令位置の公開資料なし） · `00bc3044`（命令位置の公開資料なし） · `00bc3010`（命令位置の公開資料なし）

~~~diff
- 00b54380 ["INT_ADD", "register:40f0:8", ["const:b54380:8", "const:4:8"]]
- 00b54380 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc303c ["INT_ADD", "register:40f0:8", ["const:bc303c:8", "const:4:8"]]
+ 00bc303c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54380 bytes 44270294
+ 00bc303c bytes b55e0294
- 00b54388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b54388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3044 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00bc3044 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54388 bytes 80aa01f9
+ 00bc3044 bytes 802e01f9
- 00b54354 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc3010 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b54354 bytes 742a00b0
+ 00bc3010 bytes 142b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c900971d95de43271f604ac5fd1f993"></a>

### [`00b543b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543b8.md) → [`00bc3074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3074.md) _ZN8firebase13remote_config8internal26jni_config_update_listener11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc3090",
      "incomplete_value": false,
      "site": "00bc3094",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b543d4",
      "incomplete_value": false,
      "site": "00b543d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc30a0",
      "incomplete_value": true,
      "site": "00bc30ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b543e4",
      "incomplete_value": true,
      "site": "00b543f0",
      "value": [
        "LOAD",
        "8",
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
      "00bc3090",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc30a0",
      "DATA",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3090",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc30a0",
      "DATA",
      [
        "storage",
        "01126268",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b543d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543b8.md#insn-00b543d8) · [`00b543d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543b8.md#insn-00b543d0) · [`00b543d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543b8.md#insn-00b543d4)
- 新版 `00bc3094`（命令位置の公開資料なし） · `00bc308c`（命令位置の公開資料なし） · `00bc3090`（命令位置の公開資料なし）

~~~diff
- 00b543d8 ["INT_ADD", "register:40f0:8", ["const:b543d8:8", "const:4:8"]]
- 00b543d8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc3094 ["INT_ADD", "register:40f0:8", ["const:bc3094:8", "const:4:8"]]
+ 00bc3094 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b543d8 bytes 6a270294
+ 00bc3094 bytes db5e0294
- 00b543d0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc308c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b543d0 bytes 20baff90
+ 00bc308c bytes 20b7ffb0
- 00b543d4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b543d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b543d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b543d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3090 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bc3090 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3090 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3090 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b543d4 bytes 001c1591
+ 00bc3090 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f283d83b18884055054a1cd8868ff32"></a>

### [`00b543f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543f4.md) → [`00bc30b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc30b0.md) _ZN8firebase13remote_config8internal26jni_config_update_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b54434"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc30f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54410"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54408",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54410",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc30f4"
      ]
    ],
    [
      "unmatched:00b54418",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc30c4",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc30cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc30f4"
      ]
    ],
    [
      "00bc30d4",
      "PARAM",
      [
        "storage",
        "002b6e1e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543f4.md#insn-00b54410) · [`00b5442c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543f4.md#insn-00b5442c) · [`00b54434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543f4.md#insn-00b54434)
- 新版 `00bc30e8`（命令位置の公開資料なし）

~~~diff
- 00b54410 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b54410 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b54410 bytes 410100b5
- 00b5442c ["INT_ADD", "register:40f0:8", ["const:b5442c:8", "const:4:8"]]
- 00b5442c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc30e8 ["INT_ADD", "register:40f0:8", ["const:bc30e8:8", "const:4:8"]]
+ 00bc30e8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5442c bytes 19270294
+ 00bc30e8 bytes 8a5e0294
- 00b54434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b54434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54434 bytes 80aa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca85c8cea52b018e7f9901c64071e0e"></a>

### [`00b544e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544e0.md) → [`00bc319c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc319c.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b544e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b544e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b544e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b544e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b544e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc31ac",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc319c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc31a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc31ac",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b544e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544e0.md#insn-00b544e0) · [`00b544e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544e0.md#insn-00b544e4) · [`00b544f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544e0.md#insn-00b544f4)
- 新版 `00bc31b0`（命令位置の公開資料なし）

~~~diff
- 00b544e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b544e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b544e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b544e0 bytes f30f1ef8
- 00b544e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b544e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b544e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b544e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b544e4 bytes fd7b01a9
- 00b544f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b544f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc31b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc31b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b544f4 bytes e80000b5
+ 00bc31b0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfcc3f2139968f909a2a0b3e7a7864b1"></a>

### [`00b54520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54520.md) → [`00bc31dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc31dc.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc320c",
      "incomplete_value": true,
      "site": "00bc320c",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54550",
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
            "const:370:8"
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
      "definition_site": "00bc31f0",
      "incomplete_value": true,
      "site": "00bc31f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc31fc",
      "incomplete_value": false,
      "site": "00bc3204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54540",
      "incomplete_value": false,
      "site": "00b54548",
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
            "const:179:8"
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
      "00bc31ec",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31fc",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ],
    [
      "00bc320c",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc31ec",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31fc",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "00bc320c",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54520.md#insn-00b54548) · [`00b54550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54520.md#insn-00b54550) · [`00b5452c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54520.md#insn-00b5452c)
- 新版 `00bc3204`（命令位置の公開資料なし） · `00bc320c`（命令位置の公開資料なし） · `00bc31e8`（命令位置の公開資料なし）

~~~diff
- 00b54548 ["INT_ADD", "register:40f0:8", ["const:b54548:8", "const:4:8"]]
- 00b54548 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3204 ["INT_ADD", "register:40f0:8", ["const:bc3204:8", "const:4:8"]]
+ 00bc3204 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54548 bytes d2260294
+ 00bc3204 bytes 435e0294
- 00b54550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
- 00b54550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc320c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
+ 00bc320c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54550 bytes 60ba01f9
+ 00bc320c bytes 603e01f9
- 00b5452c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc31e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5452c bytes 732a00b0
+ 00bc31e8 bytes 132b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d2e9b811088c6d080ab7fe263bb7b9"></a>

### [`00b54564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54564.md) → [`00bc3220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3220.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc3250",
      "incomplete_value": true,
      "site": "00bc3250",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54594",
      "incomplete_value": true,
      "site": "00b54594",
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
            "const:370:8"
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
      "definition_site": "00bc3234",
      "incomplete_value": true,
      "site": "00bc3234",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b54578",
      "incomplete_value": true,
      "site": "00b54578",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc323c",
      "incomplete_value": false,
      "site": "00bc3248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54580",
      "incomplete_value": false,
      "site": "00b5458c",
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
            "const:179:8"
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
      "00bc3230",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc323c",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ],
    [
      "00bc3250",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3230",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc323c",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ],
    [
      "00bc3250",
      "WRITE",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5458c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54564.md#insn-00b5458c) · [`00b54594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54564.md#insn-00b54594) · [`00b54570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54564.md#insn-00b54570)
- 新版 `00bc3248`（命令位置の公開資料なし） · `00bc3250`（命令位置の公開資料なし） · `00bc322c`（命令位置の公開資料なし）

~~~diff
- 00b5458c ["INT_ADD", "register:40f0:8", ["const:b5458c:8", "const:4:8"]]
- 00b5458c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3248 ["INT_ADD", "register:40f0:8", ["const:bc3248:8", "const:4:8"]]
+ 00bc3248 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5458c bytes c1260294
+ 00bc3248 bytes 325e0294
- 00b54594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
- 00b54594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
+ 00bc3250 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54594 bytes 60ba01f9
+ 00bc3250 bytes 603e01f9
- 00b54570 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc322c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b54570 bytes 732a00b0
+ 00bc322c bytes 132b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-647ef2d8040c0ce15ba15e3e825e7638"></a>

### [`00b545b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b545b4.md) → [`00bc3270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3270.md) _ZN8firebase13remote_config8internal13config_update15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5460c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc32c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc32a4",
      "incomplete_value": true,
      "site": "00bc32b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:278:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b545e8",
      "incomplete_value": true,
      "site": "00b545f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:370:8"
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
      "00bc3284",
      "READ",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b545e8",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5460c",
      "WRITE",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3284",
      "READ",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc32a4",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32c8",
      "WRITE",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b545f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b545b4.md#insn-00b545f4) · [`00b5460c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b545b4.md#insn-00b5460c)
- 新版 `00bc32b0`（命令位置の公開資料なし） · `00bc32c8`（命令位置の公開資料なし）

~~~diff
- 00b545f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b545f4 ["INT_ADD", "register:40f0:8", ["const:b545f4:8", "const:4:8"]]
- 00b545f4 ["CALLIND", null, ["register:0:8"]]
+ 00bc32b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc32b0 ["INT_ADD", "register:40f0:8", ["const:bc32b0:8", "const:4:8"]]
+ 00bc32b0 ["CALLIND", null, ["register:0:8"]]
- 00b545f4 bytes 00013fd6
+ 00bc32b0 bytes 00013fd6
- 00b5460c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5460c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:378:8"]]
- 00b5460c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5460c bytes a0e20d39
+ 00bc32c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc32c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:280:8"]]
+ 00bc32c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc32c8 bytes a0020a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db3dd9ddb4d0b11967d3c0b80f676294"></a>

### [`00b54620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54620.md) → [`00bc32dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc32dc.md) _ZN8firebase13remote_config8internal13config_update12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00b5465c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3338",
      "incomplete_value": true,
      "site": "00bc3338",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5467c",
      "incomplete_value": true,
      "site": "00b5467c",
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
            "const:370:8"
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
      "site": "00bc3318"
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
      "00bc32f0",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32fc",
      "READ",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b5465c",
      "WRITE",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc32f0",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32fc",
      "READ",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3318",
      "WRITE",
      [
        "storage",
        "01126280",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54620.md#insn-00b54638) · [`00b54658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54620.md#insn-00b54658) · [`00b5465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54620.md#insn-00b5465c)
- 新版 `00bc32f4`（命令位置の公開資料なし）

~~~diff
- 00b54638 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b54638 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc32f4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc32f4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b54638 bytes 410200b4
+ 00bc32f4 bytes 410200b4
- 00b54658 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54658 ["INT_ADD", "register:40f0:8", ["const:b54658:8", "const:4:8"]]
- 00b54658 ["CALLIND", null, ["register:0:8"]]
- 00b54658 bytes 00013fd6
- 00b5465c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5465c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5465c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:378:8"]]
- 00b5465c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5465c bytes bfe20d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4163d4560bd7db31f16d890eecece700"></a>

### [`00b54690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54690.md) → [`00bc334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc334c.md) _ZN8firebase13remote_config8internal13config_update14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b546d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc338c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b546ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b546a4",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b546ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3390"
      ]
    ],
    [
      "unmatched:00b546b4",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3360",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3368",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3390"
      ]
    ],
    [
      "00bc3370",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b546ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54690.md#insn-00b546ac) · [`00b546c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54690.md#insn-00b546c8) · [`00b546d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54690.md#insn-00b546d0)
- 新版 `00bc3384`（命令位置の公開資料なし）

~~~diff
- 00b546ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b546ac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b546ac bytes 410100b5
- 00b546c8 ["INT_ADD", "register:40f0:8", ["const:b546c8:8", "const:4:8"]]
- 00b546c8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3384 ["INT_ADD", "register:40f0:8", ["const:bc3384:8", "const:4:8"]]
+ 00bc3384 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b546c8 bytes 72260294
+ 00bc3384 bytes e35d0294
- 00b546d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
- 00b546d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b546d0 bytes 80ba01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f6dd6bdd331870d83027cb3d1bbbe6a"></a>

### [`00b54700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54700.md) → [`00bc33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33bc.md) _ZN8firebase13remote_config8internal13config_update11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc33d8",
      "incomplete_value": false,
      "site": "00bc33dc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5471c",
      "incomplete_value": false,
      "site": "00b54720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc33e8",
      "incomplete_value": true,
      "site": "00bc33f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5472c",
      "incomplete_value": true,
      "site": "00b54738",
      "value": [
        "LOAD",
        "8",
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
      "00bc33d8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc33e8",
      "DATA",
      [
        "storage",
        "010a1380",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc33d8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc33e8",
      "DATA",
      [
        "storage",
        "01126288",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54700.md#insn-00b54720) · [`00b54718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54700.md#insn-00b54718) · [`00b5471c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54700.md#insn-00b5471c)
- 新版 `00bc33dc`（命令位置の公開資料なし） · `00bc33d4`（命令位置の公開資料なし） · `00bc33d8`（命令位置の公開資料なし）

~~~diff
- 00b54720 ["INT_ADD", "register:40f0:8", ["const:b54720:8", "const:4:8"]]
- 00b54720 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc33dc ["INT_ADD", "register:40f0:8", ["const:bc33dc:8", "const:4:8"]]
+ 00bc33dc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b54720 bytes 98260294
+ 00bc33dc bytes 095e0294
- 00b54718 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc33d4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b54718 bytes 20baff90
+ 00bc33d4 bytes 20b7ffb0
- 00b5471c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5471c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5471c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5471c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc33d8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bc33d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc33d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc33d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5471c bytes 001c1591
+ 00bc33d8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7934df88c2b560beda44294977ccc7"></a>

### [`00b5473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5473c.md) → [`00bc33f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc33f8.md) _ZN8firebase13remote_config8internal13config_update13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b5477c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3438"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54750",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54758",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc343c"
      ]
    ],
    [
      "unmatched:00b54760",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc340c",
      "READ",
      [
        "storage",
        "01126278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc343c"
      ]
    ],
    [
      "00bc341c",
      "PARAM",
      [
        "storage",
        "002bc09c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5473c.md#insn-00b54758) · [`00b54774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5473c.md#insn-00b54774) · [`00b5477c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5473c.md#insn-00b5477c)
- 新版 `00bc3430`（命令位置の公開資料なし）

~~~diff
- 00b54758 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b54758 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b54758 bytes 410100b5
- 00b54774 ["INT_ADD", "register:40f0:8", ["const:b54774:8", "const:4:8"]]
- 00b54774 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3430 ["INT_ADD", "register:40f0:8", ["const:bc3430:8", "const:4:8"]]
+ 00bc3430 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54774 bytes 47260294
+ 00bc3430 bytes b85d0294
- 00b5477c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
- 00b5477c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5477c bytes 80ba01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0318875b36ceaa9a67f9ccb9f16e530"></a>

### [`00b547ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547ac.md) → [`00bc3468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3468.md) _ZN8firebase13remote_config8internal13config_update10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc3484",
      "incomplete_value": false,
      "site": "00bc3488",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547c8",
      "incomplete_value": false,
      "site": "00b547cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bc3494",
      "incomplete_value": true,
      "site": "00bc34a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b547d8",
      "incomplete_value": true,
      "site": "00b547e4",
      "value": [
        "LOAD",
        "8",
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
      "00bc3484",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bc3494",
      "DATA",
      [
        "storage",
        "010a1388",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc3484",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc3494",
      "DATA",
      [
        "storage",
        "01126290",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b547cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547ac.md#insn-00b547cc) · [`00b547c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547ac.md#insn-00b547c4) · [`00b547c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547ac.md#insn-00b547c8)
- 新版 `00bc3488`（命令位置の公開資料なし） · `00bc3480`（命令位置の公開資料なし） · `00bc3484`（命令位置の公開資料なし）

~~~diff
- 00b547cc ["INT_ADD", "register:40f0:8", ["const:b547cc:8", "const:4:8"]]
- 00b547cc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc3488 ["INT_ADD", "register:40f0:8", ["const:bc3488:8", "const:4:8"]]
+ 00bc3488 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b547cc bytes 6d260294
+ 00bc3488 bytes de5d0294
- 00b547c4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bc3480 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b547c4 bytes 20baffb0
+ 00bc3480 bytes 20b7ffd0
- 00b547c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b547c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b547c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b547c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3484 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bc3484 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3484 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3484 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b547c8 bytes 00c81791
+ 00bc3484 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aedaee7f64ab630a423e18d3f9314d7c"></a>

### [`00b547e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547e8.md) → [`00bc34a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc34a4.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc34d0",
      "incomplete_value": true,
      "site": "00bc34d0",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54814",
      "incomplete_value": true,
      "site": "00b54814",
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
            "const:390:8"
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
      "definition_site": "00bc34b8",
      "incomplete_value": true,
      "site": "00bc34b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b547fc",
      "incomplete_value": true,
      "site": "00b547fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc34c4",
      "incomplete_value": false,
      "site": "00bc34c8",
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
            "const:762:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54808",
      "incomplete_value": false,
      "site": "00b5480c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:889:8"
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
      "00bc34b4",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc34c4",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00bc34d0",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc34b4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc34c4",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "00bc34d0",
      "WRITE",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5480c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547e8.md#insn-00b5480c) · [`00b54814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547e8.md#insn-00b54814) · [`00b547f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547e8.md#insn-00b547f4)
- 新版 `00bc34c8`（命令位置の公開資料なし） · `00bc34d0`（命令位置の公開資料なし） · `00bc34b0`（命令位置の公開資料なし）

~~~diff
- 00b5480c ["INT_ADD", "register:40f0:8", ["const:b5480c:8", "const:4:8"]]
- 00b5480c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc34c8 ["INT_ADD", "register:40f0:8", ["const:bc34c8:8", "const:4:8"]]
+ 00bc34c8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5480c bytes 21260294
+ 00bc34c8 bytes 925d0294
- 00b54814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00b54814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc34d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
+ 00bc34d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54814 bytes 60ca01f9
+ 00bc34d0 bytes 604e01f9
- 00b547f4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc34b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b547f4 bytes 732a00b0
+ 00bc34b0 bytes 132b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc48cc9f5daf43ccd73e842cd1ad76b"></a>

### [`00b54868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54868.md) → [`00bc3524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3524.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b54868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5486c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5486c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54868",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5486c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc3534",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3524",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc3528",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc3534",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54868.md#insn-00b54868) · [`00b5486c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54868.md#insn-00b5486c) · [`00b5487c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54868.md#insn-00b5487c)
- 新版 `00bc3538`（命令位置の公開資料なし）

~~~diff
- 00b54868 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b54868 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b54868 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b54868 bytes f30f1ef8
- 00b5486c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5486c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5486c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5486c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5486c bytes fd7b01a9
- 00b5487c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5487c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc3538 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc3538 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5487c bytes 080100b5
+ 00bc3538 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-796ce360e936e76ec4359b06248a7c68"></a>

### [`00b548ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548ac.md) → [`00bc3568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3568.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc3598",
      "incomplete_value": true,
      "site": "00bc3598",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548dc",
      "incomplete_value": true,
      "site": "00b548dc",
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
            "const:390:8"
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
      "definition_site": "00bc357c",
      "incomplete_value": true,
      "site": "00bc357c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b548c0",
      "incomplete_value": true,
      "site": "00b548c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc3584",
      "incomplete_value": false,
      "site": "00bc3590",
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
            "const:762:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548c8",
      "incomplete_value": false,
      "site": "00b548d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:889:8"
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
      "00bc3578",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3584",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00bc3598",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3578",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3584",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "00bc3598",
      "WRITE",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b548d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548ac.md#insn-00b548d4) · [`00b548dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548ac.md#insn-00b548dc) · [`00b548b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548ac.md#insn-00b548b8)
- 新版 `00bc3590`（命令位置の公開資料なし） · `00bc3598`（命令位置の公開資料なし） · `00bc3574`（命令位置の公開資料なし）

~~~diff
- 00b548d4 ["INT_ADD", "register:40f0:8", ["const:b548d4:8", "const:4:8"]]
- 00b548d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3590 ["INT_ADD", "register:40f0:8", ["const:bc3590:8", "const:4:8"]]
+ 00bc3590 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b548d4 bytes ef250294
+ 00bc3590 bytes 605d0294
- 00b548dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00b548dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3598 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:298:8"]]
+ 00bc3598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b548dc bytes 60ca01f9
+ 00bc3598 bytes 604e01f9
- 00b548b8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bc3574 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b548b8 bytes 732a00b0
+ 00bc3574 bytes 132b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7eae483b41e1891439e2578977026a"></a>

### [`00b548fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548fc.md) → [`00bc35b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc35b8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc3610",
      "incomplete_value": true,
      "site": "00bc3610",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54954",
      "incomplete_value": true,
      "site": "00b54954",
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
            "const:398:8"
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
      "definition_site": "00bc35ec",
      "incomplete_value": true,
      "site": "00bc35f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:298:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54930",
      "incomplete_value": true,
      "site": "00b5493c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "00bc35cc",
      "READ",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc35ec",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3610",
      "WRITE",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc35cc",
      "READ",
      [
        "storage",
        "011262a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc35ec",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3610",
      "WRITE",
      [
        "storage",
        "011262a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5493c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548fc.md#insn-00b5493c) · [`00b54954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548fc.md#insn-00b54954) · [`00b5490c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548fc.md#insn-00b5490c)
- 新版 `00bc35f8`（命令位置の公開資料なし） · `00bc3610`（命令位置の公開資料なし） · `00bc35c8`（命令位置の公開資料なし）

~~~diff
- 00b5493c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5493c ["INT_ADD", "register:40f0:8", ["const:b5493c:8", "const:4:8"]]
- 00b5493c ["CALLIND", null, ["register:0:8"]]
+ 00bc35f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc35f8 ["INT_ADD", "register:40f0:8", ["const:bc35f8:8", "const:4:8"]]
+ 00bc35f8 ["CALLIND", null, ["register:0:8"]]
- 00b5493c bytes 00013fd6
+ 00bc35f8 bytes 00013fd6
- 00b54954 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b54954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:398:8"]]
- 00b54954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc3610 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc3610 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2a0:8"]]
+ 00bc3610 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b54954 bytes a0620e39
+ 00bc3610 bytes a0820a39
- 00b5490c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bc35c8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b5490c bytes 752a00b0
+ 00bc35c8 bytes 152b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca791b86c5a733bd8d16039e68ae99c"></a>

### [`00b549d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b549d8.md) → [`00bc3694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3694.md) _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b54a18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc36d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b549f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b549ec",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b549f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc36d8"
      ]
    ],
    [
      "unmatched:00b549fc",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc36a8",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc36b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc36d8"
      ]
    ],
    [
      "00bc36b8",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b549f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b549d8.md#insn-00b549f4) · [`00b54a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b549d8.md#insn-00b54a10) · [`00b54a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b549d8.md#insn-00b54a18)
- 新版 `00bc36cc`（命令位置の公開資料なし）

~~~diff
- 00b549f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b549f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b549f4 bytes 410100b5
- 00b54a10 ["INT_ADD", "register:40f0:8", ["const:b54a10:8", "const:4:8"]]
- 00b54a10 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc36cc ["INT_ADD", "register:40f0:8", ["const:bc36cc:8", "const:4:8"]]
+ 00bc36cc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54a10 bytes a0250294
+ 00bc36cc bytes 115d0294
- 00b54a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
- 00b54a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54a18 bytes 80ca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6051a471d0c0ddafe2953bae56686369"></a>

### [`00b54a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a48.md) → [`00bc3704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3704.md) _ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc3720",
      "incomplete_value": false,
      "site": "00bc3724",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54a64",
      "incomplete_value": false,
      "site": "00b54a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00bc3730",
      "incomplete_value": true,
      "site": "00bc373c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54a74",
      "incomplete_value": true,
      "site": "00b54a80",
      "value": [
        "LOAD",
        "8",
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
      "00bc3720",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bc3730",
      "DATA",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3720",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc3730",
      "DATA",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a48.md#insn-00b54a68) · [`00b54a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a48.md#insn-00b54a60) · [`00b54a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a48.md#insn-00b54a64)
- 新版 `00bc3724`（命令位置の公開資料なし） · `00bc371c`（命令位置の公開資料なし） · `00bc3720`（命令位置の公開資料なし）

~~~diff
- 00b54a68 ["INT_ADD", "register:40f0:8", ["const:b54a68:8", "const:4:8"]]
- 00b54a68 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc3724 ["INT_ADD", "register:40f0:8", ["const:bc3724:8", "const:4:8"]]
+ 00bc3724 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b54a68 bytes c6250294
+ 00bc3724 bytes 375d0294
- 00b54a60 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bc371c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b54a60 bytes 20baff90
+ 00bc371c bytes 20b7ffb0
- 00b54a64 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b54a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3720 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bc3720 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3720 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3720 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54a64 bytes 001c1591
+ 00bc3720 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b73ffb97ad7445fb24afefdbb852f7"></a>

### [`00b54a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a84.md) → [`00bc3740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3740.md) _ZN8firebase13remote_config8internal35config_update_listener_registration13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bc3780",
      "incomplete_value": true,
      "site": "00bc3780",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54ac4",
      "incomplete_value": true,
      "site": "00b54ac4",
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
            "const:390:8"
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
      "definition_site": "00bc375c",
      "incomplete_value": true,
      "site": "00bc375c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b54aa0",
      "incomplete_value": true,
      "site": "00b54aa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc3764",
      "incomplete_value": false,
      "site": "00bc3778",
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
            "const:762:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54aa8",
      "incomplete_value": false,
      "site": "00b54abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:889:8"
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
      "00bc3754",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3764",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00bc3780",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3754",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3764",
      "PARAM",
      [
        "storage",
        "002a9762",
        null,
        "string"
      ]
    ],
    [
      "00bc3780",
      "WRITE",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a84.md#insn-00b54abc) · [`00b54ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a84.md#insn-00b54ac4) · [`00b54a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a84.md#insn-00b54a90)
- 新版 `00bc3778`（命令位置の公開資料なし） · `00bc3780`（命令位置の公開資料なし） · `00bc374c`（命令位置の公開資料なし）

~~~diff
- 00b54abc ["INT_ADD", "register:40f0:8", ["const:b54abc:8", "const:4:8"]]
- 00b54abc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bc3778 ["INT_ADD", "register:40f0:8", ["const:bc3778:8", "const:4:8"]]
+ 00bc3778 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b54abc bytes 75250294
+ 00bc3778 bytes e65c0294
- 00b54ac4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
- 00b54ac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:298:8"]]
+ 00bc3780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54ac4 bytes 80ca01f9
+ 00bc3780 bytes 804e01f9
- 00b54a90 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bc374c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b54a90 bytes 742a00b0
+ 00bc374c bytes 142b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdaa3a83ef499e6eee5c01fd786d6356"></a>

### [`00b54af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54af4.md) → [`00bc37b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37b0.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bc37cc",
      "incomplete_value": false,
      "site": "00bc37d0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54b10",
      "incomplete_value": false,
      "site": "00b54b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bc37dc",
      "incomplete_value": true,
      "site": "00bc37e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54b20",
      "incomplete_value": true,
      "site": "00b54b2c",
      "value": [
        "LOAD",
        "8",
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
      "00bc37cc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bc37dc",
      "DATA",
      [
        "storage",
        "010a13a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc37cc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc37dc",
      "DATA",
      [
        "storage",
        "011262b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54af4.md#insn-00b54b14) · [`00b54b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54af4.md#insn-00b54b0c) · [`00b54b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54af4.md#insn-00b54b10)
- 新版 `00bc37d0`（命令位置の公開資料なし） · `00bc37c8`（命令位置の公開資料なし） · `00bc37cc`（命令位置の公開資料なし）

~~~diff
- 00b54b14 ["INT_ADD", "register:40f0:8", ["const:b54b14:8", "const:4:8"]]
- 00b54b14 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc37d0 ["INT_ADD", "register:40f0:8", ["const:bc37d0:8", "const:4:8"]]
+ 00bc37d0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b54b14 bytes 9b250294
+ 00bc37d0 bytes 0c5d0294
- 00b54b0c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bc37c8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b54b0c bytes 20baffb0
+ 00bc37c8 bytes 20b7ffd0
- 00b54b10 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b54b10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54b10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54b10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc37cc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bc37cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc37cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc37cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54b10 bytes 00c81791
+ 00bc37cc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1799a8aa511fffa5b2c6003974836487"></a>

### [`00b54b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54b38.md) → [`00bc37f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc37f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE

採用 · 移動量 `+0x6ecbc` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0870.md) · 呼出先 22件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d470.md) · 呼出先 22件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, branch_count, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_count, store_destination, store_value

命令の説明率　旧版 46.05% / 新版 43.01%

CFGの説明率　旧版 23.97% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 4件, `call_argument_candidate` 28件, `call_count` 5件, `store_count` 3件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54bb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54b98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde20"
      ]
    ],
    [
      "00bc385c",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b54bc0",
      "DATA",
      [
        "storage",
        "010a13b0",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bc3854",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a880"
      ]
    ],
    [
      "00bc385c",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "00bc387c",
      "DATA",
      [
        "storage",
        "011262b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54b38.md#insn-00b54bb4) · [`00b54bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54b38.md#insn-00b54bb8) · [`00b54bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54b38.md#insn-00b54bbc)

~~~diff
- 00b54bb4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:30:8"]]
- 00b54bb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54bb4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54bb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b54bb4 bytes 408301ad
- 00b54bb8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:10:8"]]
- 00b54bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54bb8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54bb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b54bb8 bytes 408300ad
- 00b54bbc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b54bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b54bbc bytes 4003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-296cacb2ee588e984930e0f5e323e0b8"></a>

### [`00b55744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55744.md) → [`00bc44b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc44b0.md) _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev

採用 · 移動量 `+0x6ed6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0930.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d530.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.90% / 新版 61.90%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55744",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55748",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5574c",
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
      "00bc44b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc44b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc44b8",
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

- 旧版 [`00b55744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55744.md#insn-00b55744) · [`00b55748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55744.md#insn-00b55748) · [`00b5574c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55744.md#insn-00b5574c)

~~~diff
- 00b55744 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b55744 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b55744 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b55744 bytes f50f1df8
- 00b55748 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55748 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55748 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b55748 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55748 bytes f44f01a9
- 00b5574c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5574c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5574c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5574c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5574c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c5e49fa1a6d30475a726d4372b0ba14"></a>

### [`00b557b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b557b4.md) → [`00bc4520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4520.md) FUN_00bc4520

採用 · 移動量 `+0x6ed6c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b557c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b557b4.md#insn-00b557c8) · [`00b557d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b557b4.md#insn-00b557d8) · [`00b557e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b557b4.md#insn-00b557e4)
- 新版 `00bc4534`（命令位置の公開資料なし） · `00bc4544`（命令位置の公開資料なし） · `00bc4550`（命令位置の公開資料なし）

~~~diff
- 00b557c8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b557c8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00bc4534 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00bc4534 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b557c8 bytes 540200b4
+ 00bc4534 bytes 540200b4
- 00b557d8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 00bc4544 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b557d8 bytes 40020054
+ 00bc4544 bytes 40020054
- 00b557e4 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b557e4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b557e4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b557e4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00bc4550 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00bc4550 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00bc4550 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00bc4550 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b557e4 bytes c9000037
+ 00bc4550 bytes c9000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c99244155658eae5af82e7516609e985"></a>

### [`00b55838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55838.md) → [`00bc45a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc45a4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0x6ed6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0880.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddd0.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d480.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 74.36% / 新版 82.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b558e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc4650"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc45c4",
      "incomplete_value": true,
      "site": "00bc45c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4098:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b558e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc46a0"
      ]
    ],
    [
      "00bc46a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc50"
      ]
    ],
    [
      "00bc46ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdddd0"
      ]
    ]
  ],
  "added": [
    [
      "00bc4650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc46a0"
      ]
    ],
    [
      "00bc46a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a6a0"
      ]
    ],
    [
      "00bc46ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a830"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55838.md#insn-00b5585c) · [`00b558e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55838.md#insn-00b558e4) · [`00b55938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55838.md#insn-00b55938)
- 新版 `00bc45c8`（命令位置の公開資料なし） · `00bc46a4`（命令位置の公開資料なし）

~~~diff
- 00b5585c ["INT_ADD", "register:40f0:8", ["const:b5585c:8", "const:4:8"]]
- 00b5585c ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc45c8 ["INT_ADD", "register:40f0:8", ["const:bc45c8:8", "const:4:8"]]
+ 00bc45c8 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5585c bytes 69220294
+ 00bc45c8 bytes ae590294
- 00b558e4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b558e4 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00b558e4 bytes 950200b4
- 00b55938 ["INT_ADD", "register:40f0:8", ["const:b55938:8", "const:4:8"]]
- 00b55938 ["CALL", null, ["ram:bddc50:8"]]
+ 00bc46a4 ["INT_ADD", "register:40f0:8", ["const:bc46a4:8", "const:4:8"]]
+ 00bc46a4 ["CALL", null, ["ram:c5a6a0:8"]]
- 00b55938 bytes c6200294
+ 00bc46a4 bytes ff570294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b09c498b6c4406f828653a66d9cd6bf"></a>

### [`00b559a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b559a8.md) → [`00bc4714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4714.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv

採用 · 移動量 `+0x6ed6c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0800.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md)
- 新版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d400.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md)

変更の種類 branch_condition_or_target, branch_count, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, store_destination, store_value

命令の説明率　旧版 32.27% / 新版 29.71%

CFGの説明率　旧版 17.28% / 新版 18.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 2件, `call_argument_candidate` 1件, `call_count` 3件, `store_count` 2件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4748",
      "incomplete_value": true,
      "site": "00bc4748",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b559dc",
      "incomplete_value": true,
      "site": "00b559dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
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
      "definition_site": "00bc4748",
      "incomplete_value": true,
      "site": "00bc4748",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b559dc",
      "incomplete_value": true,
      "site": "00b559dc",
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
            "const:4:8"
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
    "new": null,
    "old": {
      "site": "00b55a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4734",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4744",
      "PARAM",
      [
        "storage",
        "010a13b4",
        null,
        null
      ]
    ],
    [
      "00bc4748",
      "DATA",
      [
        "storage",
        "010a13b0",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bc4734",
      "READ",
      [
        "storage",
        "00c9b578",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4744",
      "PARAM",
      [
        "storage",
        "011262bc",
        null,
        null
      ]
    ],
    [
      "00bc4748",
      "DATA",
      [
        "storage",
        "011262b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b559a8.md#insn-00b55a5c) · [`00b55a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b559a8.md#insn-00b55a7c) · [`00b55aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b559a8.md#insn-00b55aa8)

~~~diff
- 00b55a5c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b55a5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b55a5c ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:358:8"]]
- 00b55a5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b55a5c bytes df620d39
- 00b55a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b55a7c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b55a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b55a7c bytes 9faa01f9
- 00b55aa8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b55aa8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b55aa8 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:1c0:8"]]
- 00b55aa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b55aa8 bytes df020739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c8c1667e0b022f3f212525fda1a546"></a>

### [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) → [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md) · 呼出先 6件 [`00b55e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00bc52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md) · 呼出先 6件 [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.46% / 新版 77.46%

CFGの説明率　旧版 60.00% / 新版 65.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55d54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55d58",
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
      "00bc4b08",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bc4b0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc4b10",
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

- 旧版 [`00b55d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md#insn-00b55d50) · [`00b55d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md#insn-00b55d54) · [`00b55d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md#insn-00b55d58)

~~~diff
- 00b55d50 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b55d50 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b55d50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b55d50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55d50 bytes f85f05a9
- 00b55d54 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b55d54 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b55d54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b55d54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55d54 bytes f65706a9
- 00b55d58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b55d58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b55d58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b55d58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55d58 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d6e648673e95f2040719a37e745c7e"></a>

### [`00b55e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md) → [`00bc4c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4c34.md) FUN_00bc4c34

採用 · 移動量 `+0x6edb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) [`00b5984c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b5984c.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 2件 [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) [`00bc8d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8d4c.md) · 呼出先 4件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 59.18% / 新版 59.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc4ca8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ea8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55e98",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55eb4",
      "READ",
      [
        "storage",
        "010a12b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc4c8c",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc4c50",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc4c6c",
      "READ",
      [
        "storage",
        "01126178",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc4c8c",
      "READ",
      [
        "storage",
        "01126180",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md#insn-00b55ea8) · [`00b55ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md#insn-00b55ec0) · [`00b55ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md#insn-00b55ef0)
- 新版 `00bc4c78`（命令位置の公開資料なし）

~~~diff
- 00b55ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55ea8 ["INT_ADD", "register:40f0:8", ["const:b55ea8:8", "const:4:8"]]
- 00b55ea8 ["CALLIND", null, ["register:0:8"]]
- 00b55ea8 bytes 00013fd6
- 00b55ec0 ["INT_ADD", "register:40f0:8", ["const:b55ec0:8", "const:4:8"]]
- 00b55ec0 ["CALL", null, ["callee:0058f55c:8"]]
+ 00bc4c78 ["INT_ADD", "register:40f0:8", ["const:bc4c78:8", "const:4:8"]]
+ 00bc4c78 ["CALL", null, ["callee:0058f55c:8"]]
- 00b55ec0 bytes 015ae897
+ 00bc4c78 bytes 392ae797
- 00b55ef0 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
- 00b55ef0 bytes 22010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab398dbce2c259e522550cb614d6a47d"></a>

### [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) → [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b56820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md) [`00b56b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bde460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde460.md)
- 新版 呼出元 2件 [`00bc55d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md) [`00bc5904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aee0.md)

変更の種類 branch_condition_or_target, call, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 52.17% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc4d2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55f74",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bc4d7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b55fe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc4db4"
      ]
    ]
  ],
  "added": [
    [
      "00bc4d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bc4d7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bc4d9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc4db4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md#insn-00b55f74) · [`00b55fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md#insn-00b55fc4) · [`00b55fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md#insn-00b55fe4)
- 新版 `00bc4d7c`（命令位置の公開資料なし）

~~~diff
- 00b55f74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b55f74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b55f74 bytes e80f00f9
- 00b55fc4 ["INT_ADD", "register:40f0:8", ["const:b55fc4:8", "const:4:8"]]
- 00b55fc4 ["CALL", null, ["ram:bddc40:8"]]
+ 00bc4d7c ["INT_ADD", "register:40f0:8", ["const:bc4d7c:8", "const:4:8"]]
+ 00bc4d7c ["CALL", null, ["ram:c5a690:8"]]
- 00b55fc4 bytes 1f1f0294
+ 00bc4d7c bytes 45560294
- 00b55fe4 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b55fe4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b55fe4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b55fe4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b55fe4 bytes c9000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-773715c6cad537a7c2d69325e39a0456"></a>

### [`00b56070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md) → [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) _ZN8firebase13remote_config8internal20CompleteVoidCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b58108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md) [`00be08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08c0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md)
- 新版 呼出元 3件 [`00bc6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md) [`00bc7314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7314.md) [`00c5d4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4c0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.13% / 新版 72.13%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56078"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56074",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56078",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5607c",
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
      "00bc4e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bc4e30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc4e34",
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

- 旧版 [`00b56074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md#insn-00b56074) · [`00b56078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md#insn-00b56078) · [`00b5607c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md#insn-00b5607c)

~~~diff
- 00b56074 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b56074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b56074 bytes f71300f9
- 00b56078 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56078 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56078 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b56078 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56078 bytes f65703a9
- 00b5607c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5607c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5607c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5607c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5607c bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ebf058c39824567db3e31bae1046525"></a>

### [`00b564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md) → [`00bc52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc52ac.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17EnsureInitializedEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0750.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) [`00b5a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d340.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4b04.md) [`00bc97ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.52% / 新版 89.52%

CFGの説明率　旧版 91.67% / 新版 75.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b564f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b564fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b564fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b564f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b564fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56500",
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
      "00bc52b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bc52b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bc52b8",
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

- 旧版 [`00b564f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md#insn-00b564f8) · [`00b564fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md#insn-00b564fc) · [`00b56500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md#insn-00b56500)

~~~diff
- 00b564f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b564f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b564f8 bytes fb2b00f9
- 00b564fc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b564fc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b564fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b564fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b564fc bytes fa6706a9
- 00b56500 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b56500 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b56500 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b56500 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56500 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea255116f66418275915a9741f756c31"></a>

### [`00b56790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md) → [`00bc5548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5548.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27EnsureInitializedLastResultEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07c0.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3c0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b567d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc5588"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5570",
      "incomplete_value": true,
      "site": "00bc5574",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
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
      "unmatched:00b567c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b567d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bc5580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bc5590",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b567bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md#insn-00b567bc) · [`00b567c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md#insn-00b567c8) · [`00b567d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56790.md#insn-00b567d0)
- 新版 `00bc5574`（命令位置の公開資料なし）

~~~diff
- 00b567bc ["INT_ADD", "register:40f0:8", ["const:b567bc:8", "const:4:8"]]
- 00b567bc ["CALL", null, ["callee:00c5a610:8"]]
+ 00bc5574 ["INT_ADD", "register:40f0:8", ["const:bc5574:8", "const:4:8"]]
+ 00bc5574 ["CALL", null, ["callee:00c5a610:8"]]
- 00b567bc bytes 1d1d0294
+ 00bc5574 bytes 27540294
- 00b567c8 ["INT_ADD", "register:40f0:8", ["const:b567c8:8", "const:4:8"]]
- 00b567c8 ["CALL", null, ["ram:bdde10:8"]]
- 00b567c8 bytes 921d0294
- 00b567d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b567d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b567d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b567d0 bytes 7f1600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-277e73f792030e6244a62ce8c76a0b71"></a>

### [`00b56820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md) → [`00bc55d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal8ActivateEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0840.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) [`00b5a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d440.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) [`00bc99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 11.11% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56828"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56824",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56828",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5682c",
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
      "00bc55dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bc55e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bc55e4",
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

- 旧版 [`00b56824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md#insn-00b56824) · [`00b56828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md#insn-00b56828) · [`00b5682c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md#insn-00b5682c)

~~~diff
- 00b56824 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b56824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b56824 bytes fb2b00f9
- 00b56828 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b56828 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b56828 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b56828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56828 bytes fa6706a9
- 00b5682c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5682c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5682c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b5682c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5682c bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc816d84d6803fcf09ad8f4984b01e46"></a>

### [`00b56abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md) → [`00bc5874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5874.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal18ActivateLastResultEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0780.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d370.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "00bc58ac",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b56af4",
      "value": [
        "leaf",
        "ram:bdde10:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc58bc",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b56b04",
      "value": [
        "leaf",
        "ram:bddf90:8"
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
      "00bc58ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bc58bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bc58ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bc58bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md#insn-00b56af4) · [`00b56b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md#insn-00b56b04) · [`00b56adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56abc.md#insn-00b56adc)
- 新版 `00bc58ac`（命令位置の公開資料なし） · `00bc58bc`（命令位置の公開資料なし） · `00bc5894`（命令位置の公開資料なし）

~~~diff
- 00b56af4 ["INT_ADD", "register:40f0:8", ["const:b56af4:8", "const:4:8"]]
- 00b56af4 ["CALL", null, ["ram:bdde10:8"]]
+ 00bc58ac ["INT_ADD", "register:40f0:8", ["const:bc58ac:8", "const:4:8"]]
+ 00bc58ac ["CALL", null, ["ram:c5a870:8"]]
- 00b56af4 bytes c71c0294
+ 00bc58ac bytes f1530294
- 00b56b04 ["INT_ADD", "register:40f0:8", ["const:b56b04:8", "const:4:8"]]
- 00b56b04 ["CALL", null, ["ram:bddf90:8"]]
+ 00bc58bc ["INT_ADD", "register:40f0:8", ["const:bc58bc:8", "const:4:8"]]
+ 00bc58bc ["CALL", null, ["ram:c5aa10:8"]]
- 00b56b04 bytes 231d0294
+ 00bc58bc bytes 55540294
- 00b56adc ["INT_ADD", "register:40f0:8", ["const:b56adc:8", "const:4:8"]]
- 00b56adc ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc5894 ["INT_ADD", "register:40f0:8", ["const:bc5894:8", "const:4:8"]]
+ 00bc5894 ["CALL", null, ["callee:00c5a600:8"]]
- 00b56adc bytes 511c0294
+ 00bc5894 bytes 5b530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

