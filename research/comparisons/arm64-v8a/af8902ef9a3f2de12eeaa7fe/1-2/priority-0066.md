# v15.7.4 → v16.0.0 · 最優先の変更候補 (66)

[一覧の目次](README.md)

<a id="compare-13ea5509c7124e1905a2907ce1cb1c51"></a>

### [`00b56b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md) → [`00bc5904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0740.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) [`00b5a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d320.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) [`00bc99a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.35% / 新版 94.35%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5948",
      "incomplete_value": true,
      "site": "00bc595c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:590:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56b90",
      "incomplete_value": true,
      "site": "00b56ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc5970",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b56bb8",
      "value": [
        "leaf",
        "ram:bddc40:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5984",
      "incomplete_value": true,
      "site": "00bc598c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56bcc",
      "incomplete_value": true,
      "site": "00b56bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
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
      "00bc5948",
      "READ",
      [
        "storage",
        "00c1bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5948",
      "PARAM",
      [
        "storage",
        "00b5a4a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bc5948",
      "READ",
      [
        "storage",
        "00c9b590",
        null,
        "pointer"
      ]
    ],
    [
      "00bc5948",
      "PARAM",
      [
        "storage",
        "00bc99a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00bc5970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md#insn-00b56ba4) · [`00b56bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md#insn-00b56bb8) · [`00b56bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md#insn-00b56bd4)
- 新版 [`00bc595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc595c) · [`00bc5970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc5970) · [`00bc598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md#insn-00bc598c)

~~~diff
- 00b56ba4 ["INT_ADD", "register:40f0:8", ["const:b56ba4:8", "const:4:8"]]
- 00b56ba4 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bc595c ["INT_ADD", "register:40f0:8", ["const:bc595c:8", "const:4:8"]]
+ 00bc595c ["CALL", null, ["callee:00c5aa40:8"]]
- 00b56ba4 bytes 071d0294
+ 00bc595c bytes 39540294
- 00b56bb8 ["INT_ADD", "register:40f0:8", ["const:b56bb8:8", "const:4:8"]]
- 00b56bb8 ["CALL", null, ["ram:bddc40:8"]]
+ 00bc5970 ["INT_ADD", "register:40f0:8", ["const:bc5970:8", "const:4:8"]]
+ 00bc5970 ["CALL", null, ["ram:c5a690:8"]]
- 00b56bb8 bytes 221c0294
+ 00bc5970 bytes 48530294
- 00b56bd4 ["INT_ADD", "register:40f0:8", ["const:b56bd4:8", "const:4:8"]]
- 00b56bd4 ["CALL", null, ["callee:004977f4:8"]]
+ 00bc598c ["INT_ADD", "register:40f0:8", ["const:bc598c:8", "const:4:8"]]
+ 00bc598c ["CALL", null, ["callee:004977f4:8"]]
- 00b56bd4 bytes 6277e497
+ 00bc598c bytes 9a47e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0307526a7fc66ab1f3b7005c269ec76"></a>

### [`00b56e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56e78.md) → [`00bc5c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5c30.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal5FetchEm

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07e0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b56178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56178.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3e0.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4f30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.99% / 新版 86.99%

CFGの説明率　旧版 28.95% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b56e8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b56e88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56e8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b56e90",
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
      "00bc5c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc5c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc5c48",
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

- 旧版 [`00b56e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56e78.md#insn-00b56e88) · [`00b56e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56e78.md#insn-00b56e8c) · [`00b56e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56e78.md#insn-00b56e90)

~~~diff
- 00b56e88 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b56e88 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b56e88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b56e88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56e88 bytes f65708a9
- 00b56e8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b56e8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b56e8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b56e8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56e8c bytes f44f09a9
- 00b56e90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b56e90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b56e90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b56e90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b56e90 bytes fd7b0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c29ff4db821607f0861ce87e5f704d"></a>

### [`00b57110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md) → [`00bc5ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5ec8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal15FetchLastResultEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0720.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5d300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d300.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b57110",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b57114",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b57118",
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
      "00bc5ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc5ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc5ed0",
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

- 旧版 [`00b57110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md#insn-00b57110) · [`00b57114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md#insn-00b57114) · [`00b57118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57110.md#insn-00b57118)

~~~diff
- 00b57110 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b57110 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b57110 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b57110 bytes f50f1df8
- 00b57114 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b57114 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b57114 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b57114 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b57114 bytes f44f01a9
- 00b57118 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b57118 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b57118 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b57118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b57118 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1673233b7749a96ee31c5a6f280f66"></a>

### [`00b571a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md) → [`00bc5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEi

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0710.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5d2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2f0.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc5fbc",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b57204",
      "value": [
        "leaf",
        "ram:bddc40:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5fd0",
      "incomplete_value": true,
      "site": "00bc5fdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57218",
      "incomplete_value": true,
      "site": "00b57224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc6000",
      "incomplete_value": false,
      "site": "00bc6014",
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
            "const:b7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57248",
      "incomplete_value": false,
      "site": "00b5725c",
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
            "const:5a5:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5fbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "00bc5fd0",
      "READ",
      [
        "storage",
        "010a11e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6000",
      "PARAM",
      [
        "storage",
        "002af5a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc5fbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bc5fd0",
      "READ",
      [
        "storage",
        "011260a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6000",
      "PARAM",
      [
        "storage",
        "002c0b7b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md#insn-00b57204) · [`00b57224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md#insn-00b57224) · [`00b5725c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md#insn-00b5725c)
- 新版 [`00bc5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc5fbc) · [`00bc5fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc5fdc) · [`00bc6014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5f58.md#insn-00bc6014)

~~~diff
- 00b57204 ["INT_ADD", "register:40f0:8", ["const:b57204:8", "const:4:8"]]
- 00b57204 ["CALL", null, ["ram:bddc40:8"]]
+ 00bc5fbc ["INT_ADD", "register:40f0:8", ["const:bc5fbc:8", "const:4:8"]]
+ 00bc5fbc ["CALL", null, ["ram:c5a690:8"]]
- 00b57204 bytes 8f1a0294
+ 00bc5fbc bytes b5510294
- 00b57224 ["INT_ADD", "register:40f0:8", ["const:b57224:8", "const:4:8"]]
- 00b57224 ["CALL", null, ["callee:004977f4:8"]]
+ 00bc5fdc ["INT_ADD", "register:40f0:8", ["const:bc5fdc:8", "const:4:8"]]
+ 00bc5fdc ["CALL", null, ["callee:004977f4:8"]]
- 00b57224 bytes ce75e497
+ 00bc5fdc bytes 0646e397
- 00b5725c ["INT_ADD", "register:40f0:8", ["const:b5725c:8", "const:4:8"]]
- 00b5725c ["CALL", null, ["callee:00c5a9a0:8"]]
+ 00bc6014 ["INT_ADD", "register:40f0:8", ["const:bc6014:8", "const:4:8"]]
+ 00bc6014 ["CALL", null, ["callee:00c5a9a0:8"]]
- 00b5725c bytes e91e0294
+ 00bc6014 bytes 63520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc55f0e93c3298c329d9d4d2fdf7dc9e"></a>

### [`00b57438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md) → [`00bc61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_21ConfigKeyValueVariantEm

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0700.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2e0.md) · 呼出先 33件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.68% / 新版 95.68%

CFGの説明率　旧版 63.11% / 新版 70.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b579d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc6790"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc625c",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b574a4",
      "value": [
        "leaf",
        "ram:bddc40:8"
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
      "00bc625c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b57530",
      "DATA",
      [
        "storage",
        "002f8b4a",
        "switchD_00b57538::switchdataD_002f8b4a",
        "byte"
      ]
    ],
    [
      "00bc64c4",
      "PARAM",
      [
        "storage",
        "0029898b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc625c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bc62e8",
      "DATA",
      [
        "storage",
        "0030e95a",
        "switchD_00bc62f0::switchdataD_0030e95a",
        "byte"
      ]
    ],
    [
      "00bc64c4",
      "PARAM",
      [
        "storage",
        "002a8749",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b574a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md#insn-00b574a4) · [`00b57710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md#insn-00b57710) · [`00b577e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md#insn-00b577e0)
- 新版 [`00bc625c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc625c) · [`00bc64c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc64c8) · [`00bc6598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc61f0.md#insn-00bc6598)

~~~diff
- 00b574a4 ["INT_ADD", "register:40f0:8", ["const:b574a4:8", "const:4:8"]]
- 00b574a4 ["CALL", null, ["ram:bddc40:8"]]
+ 00bc625c ["INT_ADD", "register:40f0:8", ["const:bc625c:8", "const:4:8"]]
+ 00bc625c ["CALL", null, ["ram:c5a690:8"]]
- 00b574a4 bytes e7190294
+ 00bc625c bytes 0d510294
- 00b57710 ["INT_ADD", "register:40f0:8", ["const:b57710:8", "const:4:8"]]
- 00b57710 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc64c8 ["INT_ADD", "register:40f0:8", ["const:bc64c8:8", "const:4:8"]]
+ 00bc64c8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b57710 bytes cc190294
+ 00bc64c8 bytes f6500294
- 00b577e0 ["INT_ADD", "register:40f0:8", ["const:b577e0:8", "const:4:8"]]
- 00b577e0 ["CALL", null, ["callee:00c5b1c0:8"]]
+ 00bc6598 ["INT_ADD", "register:40f0:8", ["const:bc6598:8", "const:4:8"]]
+ 00bc6598 ["CALL", null, ["callee:00c5b1c0:8"]]
- 00b577e0 bytes d81b0294
+ 00bc6598 bytes 0a530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259cbbd4c07219017069f454ae2864f6"></a>

### [`00b57b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md) → [`00bc6904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06f0.md) · 呼出先 21件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2d0.md) · 呼出先 21件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4fb0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 78.69% / 新版 84.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bc6970",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b57bb8",
      "value": [
        "leaf",
        "ram:bddc40:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57c18"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc69f0",
      "incomplete_value": true,
      "site": "00bc6a04",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc6970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "00bc6af8",
      "READ",
      [
        "storage",
        "010a11f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6b2c",
      "PARAM",
      [
        "storage",
        "002af5a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc6970",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bc6af8",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc6b2c",
      "PARAM",
      [
        "storage",
        "002c0b7b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md#insn-00b57bb8) · [`00b57c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md#insn-00b57c18) · [`00b57c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md#insn-00b57c4c)
- 新版 [`00bc6970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md#insn-00bc6970) · [`00bc6a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6904.md#insn-00bc6a04)

~~~diff
- 00b57bb8 ["INT_ADD", "register:40f0:8", ["const:b57bb8:8", "const:4:8"]]
- 00b57bb8 ["CALL", null, ["ram:bddc40:8"]]
+ 00bc6970 ["INT_ADD", "register:40f0:8", ["const:bc6970:8", "const:4:8"]]
+ 00bc6970 ["CALL", null, ["ram:c5a690:8"]]
- 00b57bb8 bytes 22180294
+ 00bc6970 bytes 484f0294
- 00b57c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b57c18 ["INT_ADD", "register:40f0:8", ["const:b57c18:8", "const:4:8"]]
- 00b57c18 ["CALLIND", null, ["register:0:8"]]
- 00b57c18 bytes 00013fd6
- 00b57c4c ["INT_ADD", "register:40f0:8", ["const:b57c4c:8", "const:4:8"]]
- 00b57c4c ["CALL", null, ["callee:004977f4:8"]]
+ 00bc6a04 ["INT_ADD", "register:40f0:8", ["const:bc6a04:8", "const:4:8"]]
+ 00bc6a04 ["CALL", null, ["callee:004977f4:8"]]
- 00b57c4c bytes 4473e497
+ 00bc6a04 bytes 7c43e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c70c4580eb619f5c078e535d41a1228"></a>

### [`00b58078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md) → [`00bc6e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal21SetDefaultsLastResultEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0790.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d380.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

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
      "site": "00bc6e68",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b580b0",
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
      "site": "00bc6e78",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b580c0",
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
      "00bc6e68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bc6e78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bc6e68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bc6e78",
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

- 旧版 [`00b580b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md#insn-00b580b0) · [`00b580c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md#insn-00b580c0) · [`00b58098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58078.md#insn-00b58098)
- 新版 [`00bc6e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e68) · [`00bc6e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e78) · [`00bc6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6e30.md#insn-00bc6e50)

~~~diff
- 00b580b0 ["INT_ADD", "register:40f0:8", ["const:b580b0:8", "const:4:8"]]
- 00b580b0 ["CALL", null, ["ram:bdde10:8"]]
+ 00bc6e68 ["INT_ADD", "register:40f0:8", ["const:bc6e68:8", "const:4:8"]]
+ 00bc6e68 ["CALL", null, ["ram:c5a870:8"]]
- 00b580b0 bytes 58170294
+ 00bc6e68 bytes 824e0294
- 00b580c0 ["INT_ADD", "register:40f0:8", ["const:b580c0:8", "const:4:8"]]
- 00b580c0 ["CALL", null, ["ram:bddf90:8"]]
+ 00bc6e78 ["INT_ADD", "register:40f0:8", ["const:bc6e78:8", "const:4:8"]]
+ 00bc6e78 ["CALL", null, ["ram:c5aa10:8"]]
- 00b580c0 bytes b4170294
+ 00bc6e78 bytes e64e0294
- 00b58098 ["INT_ADD", "register:40f0:8", ["const:b58098:8", "const:4:8"]]
- 00b58098 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc6e50 ["INT_ADD", "register:40f0:8", ["const:bc6e50:8", "const:4:8"]]
+ 00bc6e50 ["CALL", null, ["callee:00c5a600:8"]]
- 00b58098 bytes e2160294
+ 00bc6e50 bytes ec4d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14960d8c7a0ec7ae9ffd356f76a90096"></a>

### [`00b58108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md) → [`00bc6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17SetConfigSettingsENS0_14ConfigSettingsE

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0770.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b56070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c5d360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d360.md) · 呼出先 15件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 5.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 23件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58144"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b582c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b582c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58144",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58170",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b58184",
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
      "00bc6efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00bc6f28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bc6f3c",
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

- 旧版 [`00b58144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md#insn-00b58144) · [`00b5815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md#insn-00b5815c) · [`00b58170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md#insn-00b58170)
- 新版 [`00bc6f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc6/00bc6ec0.md#insn-00bc6f14)

~~~diff
- 00b58144 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b58144 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b58144 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b58144 bytes a8831af8
- 00b5815c ["INT_ADD", "register:40f0:8", ["const:b5815c:8", "const:4:8"]]
- 00b5815c ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bc6f14 ["INT_ADD", "register:40f0:8", ["const:bc6f14:8", "const:4:8"]]
+ 00bc6f14 ["CALL", null, ["callee:00c5aa40:8"]]
- 00b5815c bytes 99170294
+ 00bc6f14 bytes cb4e0294
- 00b58170 ["INT_ADD", "register:40f0:8", ["const:b58170:8", "const:4:8"]]
- 00b58170 ["CALL", null, ["ram:bddc40:8"]]
- 00b58170 bytes b4160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6adad4986075e35dedd893dc1f6b7d"></a>

### [`00b584cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md) → [`00bc7284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal27SetConfigSettingsLastResultEv

採用 · 移動量 `+0x6edb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be07d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07d0.md) · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3d0.md) · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

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
      "site": "00bc72bc",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b58504",
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
      "site": "00bc72cc",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b58514",
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
      "00bc72bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bc72cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bc72bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bc72cc",
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

- 旧版 [`00b58504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md#insn-00b58504) · [`00b58514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md#insn-00b58514) · [`00b584ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b584cc.md#insn-00b584ec)
- 新版 [`00bc72bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72bc) · [`00bc72cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72cc) · [`00bc72a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7284.md#insn-00bc72a4)

~~~diff
- 00b58504 ["INT_ADD", "register:40f0:8", ["const:b58504:8", "const:4:8"]]
- 00b58504 ["CALL", null, ["ram:bdde10:8"]]
+ 00bc72bc ["INT_ADD", "register:40f0:8", ["const:bc72bc:8", "const:4:8"]]
+ 00bc72bc ["CALL", null, ["ram:c5a870:8"]]
- 00b58504 bytes 43160294
+ 00bc72bc bytes 6d4d0294
- 00b58514 ["INT_ADD", "register:40f0:8", ["const:b58514:8", "const:4:8"]]
- 00b58514 ["CALL", null, ["ram:bddf90:8"]]
+ 00bc72cc ["INT_ADD", "register:40f0:8", ["const:bc72cc:8", "const:4:8"]]
+ 00bc72cc ["CALL", null, ["ram:c5aa10:8"]]
- 00b58514 bytes 9f160294
+ 00bc72cc bytes d14d0294
- 00b584ec ["INT_ADD", "register:40f0:8", ["const:b584ec:8", "const:4:8"]]
- 00b584ec ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc72a4 ["INT_ADD", "register:40f0:8", ["const:bc72a4:8", "const:4:8"]]
+ 00bc72a4 ["CALL", null, ["callee:00c5a600:8"]]
- 00b584ec bytes cd150294
+ 00bc72a4 bytes d74c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d581ad172a903020a0d531a35cc45d3"></a>

### [`00b5855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b5855c.md) → [`00bc7a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17GetConfigSettingsEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0760.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d350.md) · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

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
      "definition_site": "00bc7a84",
      "incomplete_value": true,
      "site": "00bc7a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58584",
      "incomplete_value": true,
      "site": "00b5858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
            ]
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
      "definition_site": "00bc7aa0",
      "incomplete_value": true,
      "site": "00bc7aac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:188:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b585a0",
      "incomplete_value": true,
      "site": "00b585ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7ac4",
      "incomplete_value": true,
      "site": "00bc7ad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b585c4",
      "incomplete_value": true,
      "site": "00b585d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
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
      "00bc7a84",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7aa0",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7ac4",
      "READ",
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
      "00bc7a84",
      "READ",
      [
        "storage",
        "01126100",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7aa0",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7ac4",
      "READ",
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

- 旧版 [`00b5858c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b5855c.md#insn-00b5858c) · [`00b585ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b5855c.md#insn-00b585ac) · [`00b585d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b5855c.md#insn-00b585d0)
- 新版 [`00bc7a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7a8c) · [`00bc7aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7aac) · [`00bc7ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7a5c.md#insn-00bc7ad0)

~~~diff
- 00b5858c ["INT_ADD", "register:40f0:8", ["const:b5858c:8", "const:4:8"]]
- 00b5858c ["CALL", null, ["callee:004977f4:8"]]
+ 00bc7a8c ["INT_ADD", "register:40f0:8", ["const:bc7a8c:8", "const:4:8"]]
+ 00bc7a8c ["CALL", null, ["callee:004977f4:8"]]
- 00b5858c bytes f470e497
+ 00bc7a8c bytes 5a3fe397
- 00b585ac ["INT_ADD", "register:40f0:8", ["const:b585ac:8", "const:4:8"]]
- 00b585ac ["CALL", null, ["callee:004977f4:8"]]
+ 00bc7aac ["INT_ADD", "register:40f0:8", ["const:bc7aac:8", "const:4:8"]]
+ 00bc7aac ["CALL", null, ["callee:004977f4:8"]]
- 00b585ac bytes ec70e497
+ 00bc7aac bytes 523fe397
- 00b585d0 ["INT_ADD", "register:40f0:8", ["const:b585d0:8", "const:4:8"]]
- 00b585d0 ["CALL", null, ["callee:0058f55c:8"]]
+ 00bc7ad0 ["INT_ADD", "register:40f0:8", ["const:bc7ad0:8", "const:4:8"]]
+ 00bc7ad0 ["CALL", null, ["callee:0058f55c:8"]]
- 00b585d0 bytes 3d50e897
+ 00bc7ad0 bytes a31ee797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a0bc263d36fe1c737e8b1c13320974"></a>

### [`00b58644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md) → [`00bc7b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be06e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06e0.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5d2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2c0.md) · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7b88",
      "incomplete_value": true,
      "site": "00bc7b98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:150:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58688",
      "incomplete_value": true,
      "site": "00b58698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:288:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7be0",
      "incomplete_value": false,
      "site": "00bc7bec",
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
            "const:c09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b586e0",
      "incomplete_value": false,
      "site": "00b586ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7be4",
      "incomplete_value": false,
      "site": "00bc7bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:852:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b586e4",
      "incomplete_value": false,
      "site": "00b586ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:871:8"
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
      "00bc7b88",
      "READ",
      [
        "storage",
        "010a1288",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7be0",
      "PARAM",
      [
        "storage",
        "002915f0",
        null,
        "string"
      ]
    ],
    [
      "00bc7be4",
      "PARAM",
      [
        "storage",
        "0029a871",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc7b88",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7be0",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc7be4",
      "PARAM",
      [
        "storage",
        "002aa852",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md#insn-00b58698) · [`00b586ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md#insn-00b586ec) · [`00b58734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md#insn-00b58734)
- 新版 [`00bc7b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md#insn-00bc7b98) · [`00bc7bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md#insn-00bc7bec)

~~~diff
- 00b58698 ["INT_ADD", "register:40f0:8", ["const:b58698:8", "const:4:8"]]
- 00b58698 ["CALL", null, ["callee:00497a08:8"]]
+ 00bc7b98 ["INT_ADD", "register:40f0:8", ["const:bc7b98:8", "const:4:8"]]
+ 00bc7b98 ["CALL", null, ["callee:00497a08:8"]]
- 00b58698 bytes 3671e497
+ 00bc7b98 bytes 9c3fe397
- 00b586ec ["INT_ADD", "register:40f0:8", ["const:b586ec:8", "const:4:8"]]
- 00b586ec ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc7bec ["INT_ADD", "register:40f0:8", ["const:bc7bec:8", "const:4:8"]]
+ 00bc7bec ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b586ec bytes d5150294
+ 00bc7bec bytes 2d4b0294
- 00b58734 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b58734 ["RETURN", null, ["register:0:8"]]
- 00b58734 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b217be4a3286fbda6271315f08aee028"></a>

### [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) → [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) FUN_00bc7c38

採用 · 移動量 `+0x6f500` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b58644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md) [`00b588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md) [`00b589e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md) [`00b58ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md) [`00b58c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 5件 [`00bc7b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7b44.md) [`00bc7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md) [`00bc7ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md) [`00bc7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md) [`00bc8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md) · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 71.43% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5873c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58738",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5873c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58740",
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
      "00bc7c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bc7c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc7c40",
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

- 旧版 [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md#insn-00b58738) · [`00b5873c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md#insn-00b5873c) · [`00b58740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md#insn-00b58740)

~~~diff
- 00b58738 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b58738 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b58738 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b58738 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58738 bytes f85fbca9
- 00b5873c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5873c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5873c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5873c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5873c bytes f65701a9
- 00b58740 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58740 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58740 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a0a5290233525987a62feed93b7f61"></a>

### [`00b588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md) → [`00bc7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetLongEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0830.md) · 呼出先 4件 [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d430.md) · 呼出先 4件 [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

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
      "definition_site": "00bc7e34",
      "incomplete_value": true,
      "site": "00bc7e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:130:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58934",
      "incomplete_value": true,
      "site": "00b58944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:268:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7e8c",
      "incomplete_value": false,
      "site": "00bc7e98",
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
            "const:c09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5898c",
      "incomplete_value": false,
      "site": "00b58998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7e90",
      "incomplete_value": false,
      "site": "00bc7e98",
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
            "const:b22:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58990",
      "incomplete_value": false,
      "site": "00b58998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:536:8"
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
      "00bc7e34",
      "READ",
      [
        "storage",
        "010a1268",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7e8c",
      "PARAM",
      [
        "storage",
        "002915f0",
        null,
        "string"
      ]
    ],
    [
      "00bc7e90",
      "PARAM",
      [
        "storage",
        "00291536",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc7e34",
      "READ",
      [
        "storage",
        "01126130",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7e8c",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc7e90",
      "PARAM",
      [
        "storage",
        "002a0b22",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md#insn-00b58944) · [`00b58998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md#insn-00b58998) · [`00b58914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md#insn-00b58914)
- 新版 [`00bc7e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e44) · [`00bc7e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e98) · [`00bc7e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7df0.md#insn-00bc7e14)

~~~diff
- 00b58944 ["INT_ADD", "register:40f0:8", ["const:b58944:8", "const:4:8"]]
- 00b58944 ["CALL", null, ["callee:0058f55c:8"]]
+ 00bc7e44 ["INT_ADD", "register:40f0:8", ["const:bc7e44:8", "const:4:8"]]
+ 00bc7e44 ["CALL", null, ["callee:0058f55c:8"]]
- 00b58944 bytes 604fe897
+ 00bc7e44 bytes c61de797
- 00b58998 ["INT_ADD", "register:40f0:8", ["const:b58998:8", "const:4:8"]]
- 00b58998 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc7e98 ["INT_ADD", "register:40f0:8", ["const:bc7e98:8", "const:4:8"]]
+ 00bc7e98 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b58998 bytes 2a150294
+ 00bc7e98 bytes 824a0294
- 00b58914 ["INT_ADD", "register:40f0:8", ["const:b58914:8", "const:4:8"]]
- 00b58914 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc7e14 ["INT_ADD", "register:40f0:8", ["const:bc7e14:8", "const:4:8"]]
+ 00bc7e14 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b58914 bytes 3b160294
+ 00bc7e14 bytes 9b4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87fc3c998244002b143654ca06663643"></a>

### [`00b589e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md) → [`00bc7ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetDoubleEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0850.md) · 呼出先 4件 [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3b0.md)
- 新版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d450.md) · 呼出先 4件 [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "definition_site": "00bc7f28",
      "incomplete_value": true,
      "site": "00bc7f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:138:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58a28",
      "incomplete_value": true,
      "site": "00b58a38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7f80",
      "incomplete_value": false,
      "site": "00bc7f8c",
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
            "const:c09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58a80",
      "incomplete_value": false,
      "site": "00b58a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc7f84",
      "incomplete_value": false,
      "site": "00bc7f8c",
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
            "const:233:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58a84",
      "incomplete_value": false,
      "site": "00b58a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:f19:8"
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
      "00bc7f28",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f80",
      "PARAM",
      [
        "storage",
        "002915f0",
        null,
        "string"
      ]
    ],
    [
      "00bc7f84",
      "PARAM",
      [
        "storage",
        "0029df19",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc7f28",
      "READ",
      [
        "storage",
        "01126138",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc7f80",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc7f84",
      "PARAM",
      [
        "storage",
        "002ae233",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md#insn-00b58a38) · [`00b58a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md#insn-00b58a8c) · [`00b58a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md#insn-00b58a08)
- 新版 [`00bc7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f38) · [`00bc7f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f8c) · [`00bc7f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7ee4.md#insn-00bc7f08)

~~~diff
- 00b58a38 ["INT_ADD", "register:40f0:8", ["const:b58a38:8", "const:4:8"]]
- 00b58a38 ["CALL", null, ["callee:00c5ae30:8"]]
+ 00bc7f38 ["INT_ADD", "register:40f0:8", ["const:bc7f38:8", "const:4:8"]]
+ 00bc7f38 ["CALL", null, ["callee:00c5ae30:8"]]
- 00b58a38 bytes 5e160294
+ 00bc7f38 bytes be4b0294
- 00b58a8c ["INT_ADD", "register:40f0:8", ["const:b58a8c:8", "const:4:8"]]
- 00b58a8c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc7f8c ["INT_ADD", "register:40f0:8", ["const:bc7f8c:8", "const:4:8"]]
+ 00bc7f8c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b58a8c bytes ed140294
+ 00bc7f8c bytes 454a0294
- 00b58a08 ["INT_ADD", "register:40f0:8", ["const:b58a08:8", "const:4:8"]]
- 00b58a08 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc7f08 ["INT_ADD", "register:40f0:8", ["const:bc7f08:8", "const:4:8"]]
+ 00bc7f08 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b58a08 bytes fe150294
+ 00bc7f08 bytes 5e4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465f72b9414f295c55ef530c374f8e03"></a>

### [`00b58ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md) → [`00bc7fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetStringEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0860.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d460.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "definition_site": "00bc804c",
      "incomplete_value": true,
      "site": "00bc8058",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58b4c",
      "incomplete_value": true,
      "site": "00b58b58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:278:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc80b0",
      "incomplete_value": false,
      "site": "00bc80bc",
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
            "const:c09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58bb0",
      "incomplete_value": false,
      "site": "00b58bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc80b4",
      "incomplete_value": false,
      "site": "00bc80bc",
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
            "const:4dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58bb4",
      "incomplete_value": false,
      "site": "00b58bbc",
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
            "const:67e:8"
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
      "00bc804c",
      "READ",
      [
        "storage",
        "010a1278",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc80b0",
      "PARAM",
      [
        "storage",
        "002915f0",
        null,
        "string"
      ]
    ],
    [
      "00bc80b4",
      "PARAM",
      [
        "storage",
        "0029967e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc804c",
      "READ",
      [
        "storage",
        "01126140",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc80b0",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc80b4",
      "PARAM",
      [
        "storage",
        "002a94dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md#insn-00b58b58) · [`00b58bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md#insn-00b58bbc) · [`00b58b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md#insn-00b58b28)
- 新版 [`00bc8058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc8058) · [`00bc80bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc80bc) · [`00bc8028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7fe4.md#insn-00bc8028)

~~~diff
- 00b58b58 ["INT_ADD", "register:40f0:8", ["const:b58b58:8", "const:4:8"]]
- 00b58b58 ["CALL", null, ["callee:004977f4:8"]]
+ 00bc8058 ["INT_ADD", "register:40f0:8", ["const:bc8058:8", "const:4:8"]]
+ 00bc8058 ["CALL", null, ["callee:004977f4:8"]]
- 00b58b58 bytes 816fe497
+ 00bc8058 bytes e73de397
- 00b58bbc ["INT_ADD", "register:40f0:8", ["const:b58bbc:8", "const:4:8"]]
- 00b58bbc ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc80bc ["INT_ADD", "register:40f0:8", ["const:bc80bc:8", "const:4:8"]]
+ 00bc80bc ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b58bbc bytes a1140294
+ 00bc80bc bytes f9490294
- 00b58b28 ["INT_ADD", "register:40f0:8", ["const:b58b28:8", "const:4:8"]]
- 00b58b28 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc8028 ["INT_ADD", "register:40f0:8", ["const:bc8028:8", "const:4:8"]]
+ 00bc8028 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b58b28 bytes b6150294
+ 00bc8028 bytes 164b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e9908243a05e29069ab646818af0d7"></a>

### [`00b58c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md) → [`00bc8154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetDataEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0810.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d410.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bc7c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc7/00bc7c38.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "definition_site": "00bc81bc",
      "incomplete_value": true,
      "site": "00bc81c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58cbc",
      "incomplete_value": true,
      "site": "00b58cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8220",
      "incomplete_value": false,
      "site": "00bc822c",
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
            "const:c09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58d20",
      "incomplete_value": false,
      "site": "00b58d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc8224",
      "incomplete_value": false,
      "site": "00bc822c",
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
    "old": {
      "definition_site": "00b58d24",
      "incomplete_value": false,
      "site": "00b58d2c",
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
            "const:39d:8"
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
      "00bc81bc",
      "READ",
      [
        "storage",
        "010a1280",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8220",
      "PARAM",
      [
        "storage",
        "002915f0",
        null,
        "string"
      ]
    ],
    [
      "00bc8224",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc81bc",
      "READ",
      [
        "storage",
        "01126148",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc8220",
      "PARAM",
      [
        "storage",
        "002a0c09",
        null,
        "string"
      ]
    ],
    [
      "00bc8224",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md#insn-00b58cc8) · [`00b58d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md#insn-00b58d2c) · [`00b58c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md#insn-00b58c98)
- 新版 [`00bc81c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc81c8) · [`00bc822c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc822c) · [`00bc8198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8154.md#insn-00bc8198)

~~~diff
- 00b58cc8 ["INT_ADD", "register:40f0:8", ["const:b58cc8:8", "const:4:8"]]
- 00b58cc8 ["CALL", null, ["callee:004977f4:8"]]
+ 00bc81c8 ["INT_ADD", "register:40f0:8", ["const:bc81c8:8", "const:4:8"]]
+ 00bc81c8 ["CALL", null, ["callee:004977f4:8"]]
- 00b58cc8 bytes 256fe497
+ 00bc81c8 bytes 8b3de397
- 00b58d2c ["INT_ADD", "register:40f0:8", ["const:b58d2c:8", "const:4:8"]]
- 00b58d2c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00bc822c ["INT_ADD", "register:40f0:8", ["const:bc822c:8", "const:4:8"]]
+ 00bc822c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b58d2c bytes 45140294
+ 00bc822c bytes 9d490294
- 00b58c98 ["INT_ADD", "register:40f0:8", ["const:b58c98:8", "const:4:8"]]
- 00b58c98 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc8198 ["INT_ADD", "register:40f0:8", ["const:bc8198:8", "const:4:8"]]
+ 00bc8198 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b58c98 bytes 5a150294
+ 00bc8198 bytes ba4a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed962291e7bdc87c1055206a3aa64786"></a>

### [`00b590b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md) → [`00bc85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal6GetAllEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07f0.md) · 呼出先 26件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`0084c0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`00c5d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d3f0.md) · 呼出先 26件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`0058f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f55c.md) [`0087f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f064.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 68.06% / 新版 61.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b591e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b591e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc86e0"
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
      "00bc8608",
      "READ",
      [
        "storage",
        "010a1228",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b591e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00bc8758",
      "READ",
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
      "00bc8608",
      "READ",
      [
        "storage",
        "011260f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc86e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00bc8758",
      "READ",
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

- 旧版 [`00b59110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md#insn-00b59110) · [`00b59168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md#insn-00b59168) · [`00b591e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md#insn-00b591e0)
- 新版 [`00bc8610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc85b0.md#insn-00bc8610)

~~~diff
- 00b59110 ["INT_ADD", "register:40f0:8", ["const:b59110:8", "const:4:8"]]
- 00b59110 ["CALL", null, ["callee:004977f4:8"]]
+ 00bc8610 ["INT_ADD", "register:40f0:8", ["const:bc8610:8", "const:4:8"]]
+ 00bc8610 ["CALL", null, ["callee:004977f4:8"]]
- 00b59110 bytes 136ee497
+ 00bc8610 bytes 793ce397
- 00b59168 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59168 ["INT_ADD", "register:40f0:8", ["const:b59168:8", "const:4:8"]]
- 00b59168 ["CALLIND", null, ["register:0:8"]]
- 00b59168 bytes 00013fd6
- 00b591e0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b591e0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b591e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b591e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b591e0 bytes fa2301a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-983a1feff210698847fbdefb8f0fcc1c"></a>

### [`00b598cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) → [`00bc8dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc8/00bc8dcc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17Remote

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be07a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07a0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b5a070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a070.md) [`00b5a6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6a8.md) [`00b5a6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6ac.md)
- 新版 呼出元 1件 [`00c5d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d390.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00bc9570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9570.md) [`00bc9ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ba8.md) [`00bc9bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 21.43% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59a88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b599b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ec8"
      ]
    ],
    [
      "unmatched:00b599b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ed4"
      ]
    ],
    [
      "unmatched:00b599c4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ed0"
      ]
    ]
  ],
  "added": [
    [
      "00bc8eb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ec8"
      ]
    ],
    [
      "00bc8eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ed4"
      ]
    ],
    [
      "00bc8ec4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc8ed0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md#insn-00b59980) · [`00b599b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md#insn-00b599b4) · [`00b599b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md#insn-00b599b8)

~~~diff
- 00b59980 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b59980 ["INT_ADD", "register:40f0:8", ["const:b59980:8", "const:4:8"]]
- 00b59980 ["CALLIND", null, ["register:0:8"]]
- 00b59980 bytes 20013fd6
- 00b599b4 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b599b4 bytes a0000054
- 00b599b8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b599b8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b599b8 bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3223bb1f75ca48d75e2665f5eb24cdda"></a>

### [`00b5a09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a09c.md) → [`00bc959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_13remote_config10ConfigInfoEZNS0_26CompleteWithResultInternalIS3_EEvRKNS_12Fut

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be08d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08d0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9608",
      "incomplete_value": false,
      "site": "00bc960c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9610",
      "incomplete_value": true,
      "site": "00bc9620",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9614",
      "incomplete_value": true,
      "site": "00bc9620",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
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
      "unmatched:00b5a108",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9608",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a09c.md#insn-00b5a10c) · [`00b5a120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a09c.md#insn-00b5a120) · [`00b5a0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a09c.md#insn-00b5a0d0)
- 新版 [`00bc960c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md#insn-00bc960c) · [`00bc9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md#insn-00bc9620) · [`00bc95d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc959c.md#insn-00bc95d0)

~~~diff
- 00b5a10c ["INT_ADD", "register:40f0:8", ["const:b5a10c:8", "const:4:8"]]
- 00b5a10c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc960c ["INT_ADD", "register:40f0:8", ["const:bc960c:8", "const:4:8"]]
+ 00bc960c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5a10c bytes 1d100294
+ 00bc960c bytes 7d450294
- 00b5a120 ["INT_ADD", "register:40f0:8", ["const:b5a120:8", "const:4:8"]]
- 00b5a120 ["CALL", null, ["callee:00c5aa70:8"]]
+ 00bc9620 ["INT_ADD", "register:40f0:8", ["const:bc9620:8", "const:4:8"]]
+ 00bc9620 ["CALL", null, ["callee:00c5aa70:8"]]
- 00b5a120 bytes b40f0294
+ 00bc9620 bytes 14450294
- 00b5a0d0 ["INT_ADD", "register:40f0:8", ["const:b5a0d0:8", "const:4:8"]]
- 00b5a0d0 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc95d0 ["INT_ADD", "register:40f0:8", ["const:bc95d0:8", "const:4:8"]]
+ 00bc95d0 ["CALL", null, ["callee:00c5a600:8"]]
- 00b5a0d0 bytes d40e0294
+ 00bc95d0 bytes 0c440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a76de0f0a4f0339418877fd0c0c5eb11"></a>

### [`00b5a1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a1c8.md) → [`00bc96c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIbZNS0_26CompleteWithResultInternalIbEEvRKNS_12FutureHandleEiPKcRKT_EUlPbE_EEvS5_i

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be08e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08e0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4e0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9734",
      "incomplete_value": false,
      "site": "00bc9738",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a234",
      "incomplete_value": false,
      "site": "00b5a238",
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
            "const:467:8"
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
      "00bc9734",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9734",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a1c8.md#insn-00b5a238) · [`00b5a1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a1c8.md#insn-00b5a1fc) · [`00b5a208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a1c8.md#insn-00b5a208)
- 新版 [`00bc9738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc9738) · [`00bc96fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc96fc) · [`00bc9708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc96c8.md#insn-00bc9708)

~~~diff
- 00b5a238 ["INT_ADD", "register:40f0:8", ["const:b5a238:8", "const:4:8"]]
- 00b5a238 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc9738 ["INT_ADD", "register:40f0:8", ["const:bc9738:8", "const:4:8"]]
+ 00bc9738 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5a238 bytes d20f0294
+ 00bc9738 bytes 32450294
- 00b5a1fc ["INT_ADD", "register:40f0:8", ["const:b5a1fc:8", "const:4:8"]]
- 00b5a1fc ["CALL", null, ["callee:00c5a600:8"]]
+ 00bc96fc ["INT_ADD", "register:40f0:8", ["const:bc96fc:8", "const:4:8"]]
+ 00bc96fc ["CALL", null, ["callee:00c5a600:8"]]
- 00b5a1fc bytes 890e0294
+ 00bc96fc bytes c1430294
- 00b5a208 ["INT_ADD", "register:40f0:8", ["const:b5a208:8", "const:4:8"]]
- 00b5a208 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00bc9708 ["INT_ADD", "register:40f0:8", ["const:bc9708:8", "const:4:8"]]
+ 00bc9708 ["CALL", null, ["callee:00c5aa80:8"]]
- 00b5a208 bytes 7e0f0294
+ 00bc9708 bytes de440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1821da19548c7312df65da1cb3440d6d"></a>

### [`00b5a2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2f8.md) → [`00bc97f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc97f8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiP

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be08f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08f0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d4f0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a2fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a2f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a2fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a300",
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
      "00bc97f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bc97fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc9800",
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

- 旧版 [`00b5a2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2f8.md#insn-00b5a2f8) · [`00b5a2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2f8.md#insn-00b5a2fc) · [`00b5a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2f8.md#insn-00b5a300)

~~~diff
- 00b5a2f8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5a2f8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5a2f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5a2f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a2f8 bytes f85fbca9
- 00b5a2fc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5a2fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5a2fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a2fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a2fc bytes f65701a9
- 00b5a300 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a300 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a300 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a300 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ba751375b8d8bc12a221965dfea57ac"></a>

### [`00b5a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a400.md) → [`00bc9900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0910.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5d510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d510.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "site": "00bc9920",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5a420",
      "value": [
        "leaf",
        "ram:bdde10:8"
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
      "00bc9920",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00bc9920",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a400.md#insn-00b5a420) · [`00b5a434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a400.md#insn-00b5a434) · [`00b5a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a400.md#insn-00b5a448)
- 新版 [`00bc9920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md#insn-00bc9920) · [`00bc9934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md#insn-00bc9934) · [`00bc9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md#insn-00bc9948)

~~~diff
- 00b5a420 ["INT_ADD", "register:40f0:8", ["const:b5a420:8", "const:4:8"]]
- 00b5a420 ["CALL", null, ["ram:bdde10:8"]]
+ 00bc9920 ["INT_ADD", "register:40f0:8", ["const:bc9920:8", "const:4:8"]]
+ 00bc9920 ["CALL", null, ["ram:c5a870:8"]]
- 00b5a420 bytes 7c0e0294
+ 00bc9920 bytes d4430294
- 00b5a434 ["INT_ADD", "register:40f0:8", ["const:b5a434:8", "const:4:8"]]
- 00b5a434 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc9934 ["INT_ADD", "register:40f0:8", ["const:bc9934:8", "const:4:8"]]
+ 00bc9934 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5a434 bytes d30e0294
+ 00bc9934 bytes 33440294
- 00b5a448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5a448 ["INT_ADD", "register:40f0:8", ["const:b5a448:8", "const:4:8"]]
- 00b5a448 ["CALLIND", null, ["register:0:8"]]
+ 00bc9948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc9948 ["INT_ADD", "register:40f0:8", ["const:bc9948:8", "const:4:8"]]
+ 00bc9948 ["CALLIND", null, ["register:0:8"]]
- 00b5a448 bytes 00013fd6
+ 00bc9948 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e05e27d92c3a6d2fbce985eb30d877"></a>

### [`00b5a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4ac.md) → [`00bc99ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc99ac.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0900.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d500.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a4b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a4ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a4b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a4b4",
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
      "00bc99ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bc99b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc99b4",
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

- 旧版 [`00b5a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4ac.md#insn-00b5a4ac) · [`00b5a4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4ac.md#insn-00b5a4b0) · [`00b5a4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4ac.md#insn-00b5a4b4)

~~~diff
- 00b5a4ac ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5a4ac ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5a4ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5a4ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a4ac bytes f85fbca9
- 00b5a4b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5a4b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5a4b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a4b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a4b0 bytes f65701a9
- 00b5a4b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a4b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a4b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5a4b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a4b4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86445c1d942a6d9ffd0ed36b8e5242cc"></a>

### [`00b5a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a658.md) → [`00bc9b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md) FUN_00bc9b58

採用 · 移動量 `+0x6f500` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00bc9b74",
      "incomplete_value": false,
      "site": "00bc9b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c91000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a674",
      "incomplete_value": false,
      "site": "00b5a678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00bc9b78",
      "DATA",
      [
        "storage",
        "00c11a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9b78",
      "DATA",
      [
        "storage",
        "00c91428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a658.md#insn-00b5a66c) · [`00b5a670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a658.md#insn-00b5a670) · [`00b5a674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a658.md#insn-00b5a674)
- 新版 [`00bc9b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md#insn-00bc9b6c) · [`00bc9b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md#insn-00bc9b70) · [`00bc9b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b58.md#insn-00bc9b74)

~~~diff
- 00b5a66c ["INT_ADD", "register:40f0:8", ["const:b5a66c:8", "const:4:8"]]
- 00b5a66c ["CALL", null, ["callee:00c57a90:8"]]
+ 00bc9b6c ["INT_ADD", "register:40f0:8", ["const:bc9b6c:8", "const:4:8"]]
+ 00bc9b6c ["CALL", null, ["callee:00c57a90:8"]]
- 00b5a66c bytes 75020294
+ 00bc9b6c bytes c9370294
- 00b5a670 ["COPY", "register:4040:8", ["const:c11000:8"]]
+ 00bc9b70 ["COPY", "register:4040:8", ["const:c91000:8"]]
- 00b5a670 bytes a80500f0
+ 00bc9b70 bytes 48060090
- 00b5a674 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00b5a674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9b74 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00bc9b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5a674 bytes 08012a91
+ 00bc9b74 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb8c613c5b073d942a910d613f7c2b4"></a>

### [`00b5a6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6b0.md) → [`00bc9bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md) FUN_00bc9bb0

採用 · 移動量 `+0x6f500` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9bcc",
      "incomplete_value": true,
      "site": "00bc9bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a6cc",
      "incomplete_value": true,
      "site": "00b5a6d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
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
      "definition_site": "00bc9be8",
      "incomplete_value": false,
      "site": "00bc9bec",
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
            "const:b5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a6e8",
      "incomplete_value": false,
      "site": "00b5a6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:44b:8"
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
      "unmatched:00b5a6cc",
      "READ",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5a6e8",
      "PARAM",
      [
        "storage",
        "0029244b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc9bcc",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc9be8",
      "PARAM",
      [
        "storage",
        "002a1b5b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6b0.md#insn-00b5a6d4) · [`00b5a6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6b0.md#insn-00b5a6ec) · [`00b5a6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6b0.md#insn-00b5a6c0)
- 新版 [`00bc9bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bd4) · [`00bc9bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bec) · [`00bc9bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9bb0.md#insn-00bc9bc0)

~~~diff
- 00b5a6d4 ["INT_ADD", "register:40f0:8", ["const:b5a6d4:8", "const:4:8"]]
- 00b5a6d4 ["CALL", null, ["callee:00574cac:8"]]
+ 00bc9bd4 ["INT_ADD", "register:40f0:8", ["const:bc9bd4:8", "const:4:8"]]
+ 00bc9bd4 ["CALL", null, ["callee:00574cac:8"]]
- 00b5a6d4 bytes d0dde797
+ 00bc9bd4 bytes 36ace697
- 00b5a6ec ["INT_ADD", "register:40f0:8", ["const:b5a6ec:8", "const:4:8"]]
- 00b5a6ec ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc9bec ["INT_ADD", "register:40f0:8", ["const:bc9bec:8", "const:4:8"]]
+ 00bc9bec ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5a6ec bytes a50e0294
+ 00bc9bec bytes 05440294
- 00b5a6c0 ["INT_ADD", "register:40f0:8", ["const:b5a6c0:8", "const:4:8"]]
- 00b5a6c0 ["CALL", null, ["callee:00c5af40:8"]]
+ 00bc9bc0 ["INT_ADD", "register:40f0:8", ["const:bc9bc0:8", "const:4:8"]]
+ 00bc9bc0 ["CALL", null, ["callee:00c5af40:8"]]
- 00b5a6c0 bytes 800f0294
+ 00bc9bc0 bytes e0440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fe82a22884bce736e7d0c8ae24ce2d0"></a>

### [`00b5a84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a84c.md) → [`00bc9d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d4c.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EPNS0_8internal40ConfigUpdateListenerRegistrationInternalE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0680.md) · 呼出先 2件 [`00b5aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aa38.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md)
- 新版 呼出元 1件 [`00c5d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d260.md) · 呼出先 2件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9d5c",
      "incomplete_value": true,
      "site": "00bc9d5c",
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
      "definition_site": "00b5a85c",
      "incomplete_value": true,
      "site": "00b5a85c",
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
      "00bc9d50",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9d5c",
      "DATA",
      [
        "storage",
        "00c11b00",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b5a878",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bc9d50",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9d5c",
      "DATA",
      [
        "storage",
        "00c914a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bc9d78",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a84c.md#insn-00b5a84c) · [`00b5a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a84c.md#insn-00b5a850) · [`00b5a860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a84c.md#insn-00b5a860)
- 新版 [`00bc9d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d4c.md#insn-00bc9d4c) · [`00bc9d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d4c.md#insn-00bc9d50) · [`00bc9d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9d4c.md#insn-00bc9d60)

~~~diff
- 00b5a84c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 00bc9d4c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00b5a84c bytes 090600b0
+ 00bc9d4c bytes 890600d0
- 00b5a850 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:af8:8"]]
- 00b5a850 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc9d50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:528:8"]]
+ 00bc9d50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a850 bytes 297d45f9
+ 00bc9d50 bytes 299542f9
- 00b5a860 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5a860 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc9d60 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc9d60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5a860 bytes 410100b4
+ 00bc9d60 bytes 410100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a826d04bfd8e3ab52527ab290ebc31be"></a>

### [`00b5a920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a920.md) → [`00bc9e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSERKS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b5aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aa38.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a934"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc9e34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9e64",
      "incomplete_value": true,
      "site": "00bc9e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a964",
      "incomplete_value": true,
      "site": "00b5a970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
              ]
            ]
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
      "unmatched:00b5a934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9e74"
      ]
    ],
    [
      "00bc9e64",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9e64",
      "PARAM",
      [
        "storage",
        "00b5aa38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc9e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc9e74"
      ]
    ],
    [
      "00bc9e64",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9e64",
      "PARAM",
      [
        "storage",
        "00bc9f38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a920.md#insn-00b5a934) · [`00b5a970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a920.md#insn-00b5a970)
- 新版 [`00bc9e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md#insn-00bc9e70) · [`00bc9e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e20.md#insn-00bc9e34)

~~~diff
- 00b5a934 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b5a934 bytes 00020054
- 00b5a970 ["INT_ADD", "register:40f0:8", ["const:b5a970:8", "const:4:8"]]
- 00b5a970 ["CALL", null, ["callee:00c5a800:8"]]
+ 00bc9e70 ["INT_ADD", "register:40f0:8", ["const:bc9e70:8", "const:4:8"]]
+ 00bc9e70 ["CALL", null, ["callee:00c5a800:8"]]
- 00b5a970 bytes 0c0d0294
+ 00bc9e70 bytes 64420294
+ 00bc9e34 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00bc9e34 bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff39646054c4cccd060d5422c7bdd9e9"></a>

### [`00b5a984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a984.md) → [`00bc9e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationaSEOS1_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b5aa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aa38.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 54.55% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5a9bc",
      "incomplete_value": true,
      "site": "00b5a9c4",
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
            "const:138:8"
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
    "new": null,
    "old": {
      "definition_site": "00b5a9c0",
      "incomplete_value": true,
      "site": "00b5a9c4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc9edc",
      "incomplete_value": true,
      "site": "00bc9ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:520:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a9dc",
      "incomplete_value": true,
      "site": "00b5a9e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af0:8"
              ]
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
      "00bc9edc",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9edc",
      "PARAM",
      [
        "storage",
        "00b5aa38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc9edc",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ],
    [
      "00bc9edc",
      "PARAM",
      [
        "storage",
        "00bc9f38",
        "_ZN8firebase13remote_config9CleanupFnINS0_32ConfigUpdateListenerRegistrationENS0_8internal20RemoteConfigInternalEE7CleanupEPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a984.md#insn-00b5a9c4) · [`00b5a9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a984.md#insn-00b5a9e8) · [`00b5a9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a984.md#insn-00b5a9f8)
- 新版 [`00bc9ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md#insn-00bc9ec4) · [`00bc9ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9e84.md#insn-00bc9ee8)

~~~diff
- 00b5a9c4 ["INT_ADD", "register:40f0:8", ["const:b5a9c4:8", "const:4:8"]]
- 00b5a9c4 ["CALL", null, ["callee:00c5a810:8"]]
+ 00bc9ec4 ["INT_ADD", "register:40f0:8", ["const:bc9ec4:8", "const:4:8"]]
+ 00bc9ec4 ["CALL", null, ["callee:00c5a810:8"]]
- 00b5a9c4 bytes fb0c0294
+ 00bc9ec4 bytes 53420294
- 00b5a9e8 ["INT_ADD", "register:40f0:8", ["const:b5a9e8:8", "const:4:8"]]
- 00b5a9e8 ["CALL", null, ["callee:00c5a800:8"]]
+ 00bc9ee8 ["INT_ADD", "register:40f0:8", ["const:bc9ee8:8", "const:4:8"]]
+ 00bc9ee8 ["CALL", null, ["callee:00c5a800:8"]]
- 00b5a9e8 bytes ee0c0294
+ 00bc9ee8 bytes 46420294
- 00b5a9f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5a9f8 ["RETURN", null, ["register:0:8"]]
- 00b5a9f8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff749a9d06bf004a637d1896cf0ef3a"></a>

### [`00b5abbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md) → [`00bca0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb70.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)
- 新版 呼出元 1件 [`00c5a5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5c0.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 76.92% / 新版 81.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ad8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca28c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bca108",
      "incomplete_value": true,
      "site": "00bca108",
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
      "definition_site": "00b5ac08",
      "incomplete_value": true,
      "site": "00b5ac08",
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
      "00bca0d8",
      "READ",
      [
        "storage",
        "00c1bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00bca0e4",
      "READ",
      [
        "storage",
        "010a1418",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca0f0",
      "READ",
      [
        "storage",
        "010a1418",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bca0d8",
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca0e4",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca0f0",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5abec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md#insn-00b5abec) · [`00b5ac08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md#insn-00b5ac08) · [`00b5ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md#insn-00b5ac1c)
- 新版 [`00bca0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md#insn-00bca0ec) · [`00bca108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0bc.md#insn-00bca108)

~~~diff
- 00b5abec ["INT_ADD", "register:40f0:8", ["const:b5abec:8", "const:4:8"]]
- 00b5abec ["CALL", null, ["callee:00c5a600:8"]]
+ 00bca0ec ["INT_ADD", "register:40f0:8", ["const:bca0ec:8", "const:4:8"]]
+ 00bca0ec ["CALL", null, ["callee:00c5a600:8"]]
- 00b5abec bytes 0d0c0294
+ 00bca0ec bytes 45410294
- 00b5ac08 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5ac08 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bca108 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bca108 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5ac08 bytes c90100b4
+ 00bca108 bytes c90100b4
- 00b5ac1c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b5ac1c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b5ac1c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b5ac1c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b5ac1c bytes 0831899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0193b4680bff7dbcf02194ede75740d"></a>

### [`00b5ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md) → [`00bca368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) _ZN8firebase4auth4AuthC1EPNS_3AppEPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a90.md) · 呼出先 10件 [`00b5c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md)
- 新版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d690.md) · 呼出先 10件 [`00bcb984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca430"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5aeb8",
      "PARAM",
      [
        "storage",
        "0029f0bf",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5aedc",
      "PARAM",
      [
        "storage",
        "002ab1ac",
        null,
        null
      ]
    ],
    [
      "00bca440",
      "PARAM",
      [
        "storage",
        "00b5c484",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca3b8",
      "PARAM",
      [
        "storage",
        "002af4d2",
        null,
        "string"
      ]
    ],
    [
      "00bca3dc",
      "PARAM",
      [
        "storage",
        "002bc0cf",
        null,
        null
      ]
    ],
    [
      "00bca440",
      "PARAM",
      [
        "storage",
        "00bcb984",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5aebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md#insn-00b5aebc) · [`00b5aed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md#insn-00b5aed4) · [`00b5aee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md#insn-00b5aee8)
- 新版 [`00bca3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca3bc) · [`00bca3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca3d4) · [`00bca3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md#insn-00bca3e8)

~~~diff
- 00b5aebc ["INT_ADD", "register:40f0:8", ["const:b5aebc:8", "const:4:8"]]
- 00b5aebc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bca3bc ["INT_ADD", "register:40f0:8", ["const:bca3bc:8", "const:4:8"]]
+ 00bca3bc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5aebc bytes b10c0294
+ 00bca3bc bytes 11420294
- 00b5aed4 ["INT_ADD", "register:40f0:8", ["const:b5aed4:8", "const:4:8"]]
- 00b5aed4 ["CALL", null, ["callee:00c5d640:8"]]
+ 00bca3d4 ["INT_ADD", "register:40f0:8", ["const:bca3d4:8", "const:4:8"]]
+ 00bca3d4 ["CALL", null, ["callee:00c5d640:8"]]
- 00b5aed4 bytes db160294
+ 00bca3d4 bytes 9b4c0294
- 00b5aee8 ["INT_ADD", "register:40f0:8", ["const:b5aee8:8", "const:4:8"]]
- 00b5aee8 ["CALL", null, ["callee:00c5b960:8"]]
+ 00bca3e8 ["INT_ADD", "register:40f0:8", ["const:bca3e8:8", "const:4:8"]]
+ 00bca3e8 ["CALL", null, ["callee:00c5b960:8"]]
- 00b5aee8 bytes f20f0294
+ 00bca3e8 bytes 5e450294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c266b841e33a0e564d4c6af4070b9644"></a>

### [`00b5af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5af8c.md) → [`00bca48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca48c.md) _ZN8firebase4auth8AuthDataC2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0aa0.md) · 呼出先 3件 [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) [`00be09b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09b0.md)
- 新版 呼出元 1件 [`00c5d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6a0.md) · 呼出先 3件 [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md) [`00c5d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5b0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bca4d8",
      "incomplete_value": true,
      "site": "00bca4d8",
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
      "definition_site": "00b5afd8",
      "incomplete_value": true,
      "site": "00b5afd8",
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
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca544"
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
      "00bca4c0",
      "READ",
      [
        "storage",
        "00c1bb90",
        null,
        "pointer"
      ]
    ],
    [
      "00bca4d8",
      "DATA",
      [
        "storage",
        "00c12b00",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "unmatched:00b5b004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be09b0"
      ]
    ]
  ],
  "added": [
    [
      "00bca4c0",
      "READ",
      [
        "storage",
        "00c9b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca4d8",
      "DATA",
      [
        "storage",
        "00c924a8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bca504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5d5b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5af8c.md#insn-00b5b004) · [`00b5b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5af8c.md#insn-00b5b014) · [`00b5b024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5af8c.md#insn-00b5b024)

~~~diff
- 00b5b004 ["INT_ADD", "register:40f0:8", ["const:b5b004:8", "const:4:8"]]
- 00b5b004 ["CALL", null, ["ram:be09b0:8"]]
- 00b5b004 bytes 6b160294
- 00b5b014 ["INT_ADD", "register:40f0:8", ["const:b5b014:8", "const:4:8"]]
- 00b5b014 ["CALL", null, ["ram:bdde20:8"]]
- 00b5b014 bytes 830b0294
- 00b5b024 ["INT_ADD", "register:40f0:8", ["const:b5b024:8", "const:4:8"]]
- 00b5b024 ["CALL", null, ["ram:bdde20:8"]]
- 00b5b024 bytes 7f0b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333d529c621fbc89b5065b2efffde647"></a>

### [`00b5b114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b114.md) → [`00bca614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md) _ZN8firebase4auth4Auth14DeleteInternalEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a30.md) · 呼出先 14件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md) · 呼出先 14件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.27% / 新版 99.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bca6a8",
      "incomplete_value": true,
      "site": "00bca6ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
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
      "definition_site": "00b5b1a8",
      "incomplete_value": true,
      "site": "00b5b1ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca634",
      "incomplete_value": true,
      "site": "00bca638",
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
      "definition_site": "00b5b134",
      "incomplete_value": true,
      "site": "00b5b138",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca720",
      "incomplete_value": false,
      "site": "00bca728",
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
            "const:b49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b220",
      "incomplete_value": false,
      "site": "00b5b228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:607:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bca628",
      "READ",
      [
        "storage",
        "00c1bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00bca630",
      "READ",
      [
        "storage",
        "010a1418",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca69c",
      "READ",
      [
        "storage",
        "00c1bb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca628",
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bca630",
      "READ",
      [
        "storage",
        "01126320",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00bca69c",
      "READ",
      [
        "storage",
        "00c9b5a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b114.md#insn-00b5b138) · [`00b5b228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b114.md#insn-00b5b228) · [`00b5b124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b114.md#insn-00b5b124)
- 新版 [`00bca638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca638) · [`00bca728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca728) · [`00bca624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca614.md#insn-00bca624)

~~~diff
- 00b5b138 ["INT_ADD", "register:40f0:8", ["const:b5b138:8", "const:4:8"]]
- 00b5b138 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bca638 ["INT_ADD", "register:40f0:8", ["const:bca638:8", "const:4:8"]]
+ 00bca638 ["CALL", null, ["callee:00c5a600:8"]]
- 00b5b138 bytes ba0a0294
+ 00bca638 bytes f23f0294
- 00b5b228 ["INT_ADD", "register:40f0:8", ["const:b5b228:8", "const:4:8"]]
- 00b5b228 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bca728 ["INT_ADD", "register:40f0:8", ["const:bca728:8", "const:4:8"]]
+ 00bca728 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b5b228 bytes 220c0294
+ 00bca728 bytes 82410294
- 00b5b124 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bca624 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b5b124 bytes 08060090
+ 00bca624 bytes 880600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7b9917c41abbbc8781e74184a62dcba"></a>

### [`00b5b370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b370.md) → [`00bca870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md) _ZN8firebase4auth8AuthDataD2Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ab0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00be09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09a0.md)
- 新版 呼出元 1件 [`00c5d6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6b0.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5d5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5a0.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bca8d4",
      "value": [
        "leaf",
        "ram:c5a6a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5b3d4",
      "value": [
        "leaf",
        "ram:bddc50:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bca8dc",
      "value": [
        "leaf",
        "ram:c5a6a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5b3dc",
      "value": [
        "leaf",
        "ram:bddc50:8"
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
      "site": "00bca8e4",
      "value": [
        "leaf",
        "ram:c5a6a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5b3e4",
      "value": [
        "leaf",
        "ram:bddc50:8"
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
      "00bca8d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc50"
      ]
    ],
    [
      "00bca8dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc50"
      ]
    ],
    [
      "00bca8e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc50"
      ]
    ]
  ],
  "added": [
    [
      "00bca8d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a6a0"
      ]
    ],
    [
      "00bca8dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a6a0"
      ]
    ],
    [
      "00bca8e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a6a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b370.md#insn-00b5b3d4) · [`00b5b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b370.md#insn-00b5b3dc) · [`00b5b3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b370.md#insn-00b5b3e4)
- 新版 [`00bca8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca8d4) · [`00bca8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca8dc) · [`00bca8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca870.md#insn-00bca8e4)

~~~diff
- 00b5b3d4 ["INT_ADD", "register:40f0:8", ["const:b5b3d4:8", "const:4:8"]]
- 00b5b3d4 ["CALL", null, ["ram:bddc50:8"]]
+ 00bca8d4 ["INT_ADD", "register:40f0:8", ["const:bca8d4:8", "const:4:8"]]
+ 00bca8d4 ["CALL", null, ["ram:c5a6a0:8"]]
- 00b5b3d4 bytes 1f0a0294
+ 00bca8d4 bytes 733f0294
- 00b5b3dc ["INT_ADD", "register:40f0:8", ["const:b5b3dc:8", "const:4:8"]]
- 00b5b3dc ["CALL", null, ["ram:bddc50:8"]]
+ 00bca8dc ["INT_ADD", "register:40f0:8", ["const:bca8dc:8", "const:4:8"]]
+ 00bca8dc ["CALL", null, ["ram:c5a6a0:8"]]
- 00b5b3dc bytes 1d0a0294
+ 00bca8dc bytes 713f0294
- 00b5b3e4 ["INT_ADD", "register:40f0:8", ["const:b5b3e4:8", "const:4:8"]]
- 00b5b3e4 ["CALL", null, ["ram:bddc50:8"]]
+ 00bca8e4 ["INT_ADD", "register:40f0:8", ["const:bca8e4:8", "const:4:8"]]
+ 00bca8e4 ["CALL", null, ["ram:c5a6a0:8"]]
- 00b5b3e4 bytes 1b0a0294
+ 00bca8e4 bytes 6f3f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35120bcc0518880cb02dda72d1bf0da7"></a>

### [`00b5b4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4d4.md) → [`00bca9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md) _ZN8firebase4auth4Auth3appEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a80.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca9f0",
      "incomplete_value": false,
      "site": "00bca9f4",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b4f0",
      "incomplete_value": false,
      "site": "00b5b4f4",
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
            "const:7c:8"
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
      "00bca9f0",
      "PARAM",
      [
        "storage",
        "002a107c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bca9f0",
      "PARAM",
      [
        "storage",
        "002b16c8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4d4.md#insn-00b5b4f4) · [`00b5b4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4d4.md#insn-00b5b4ec) · [`00b5b4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4d4.md#insn-00b5b4f0)
- 新版 [`00bca9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md#insn-00bca9f4) · [`00bca9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md#insn-00bca9ec) · [`00bca9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9d4.md#insn-00bca9f0)

~~~diff
- 00b5b4f4 ["INT_ADD", "register:40f0:8", ["const:b5b4f4:8", "const:4:8"]]
- 00b5b4f4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bca9f4 ["INT_ADD", "register:40f0:8", ["const:bca9f4:8", "const:4:8"]]
+ 00bca9f4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5b4f4 bytes 230b0294
+ 00bca9f4 bytes 83400294
- 00b5b4ec ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bca9ec ["COPY", "register:4000:8", ["const:2b1000:8"]]
- 00b5b4ec bytes 20baffd0
+ 00bca9ec bytes 20b7fff0
- 00b5b4f0 ["COPY", "tmp:0:8", ["const:7c:8"]]
- 00b5b4f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b4f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b4f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bca9f0 ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 00bca9f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bca9f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bca9f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5b4f0 bytes 00f00191
+ 00bca9f0 bytes 00201b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fea2bfaa0b4950a158f97bc0db699d51"></a>

### [`00b5b50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md) → [`00bcaa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be0af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0af0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcab84",
      "incomplete_value": false,
      "site": "00bcab88",
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
            "const:c2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b684",
      "incomplete_value": false,
      "site": "00b5b688",
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
            "const:f8a:8"
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
      "00bcab84",
      "PARAM",
      [
        "storage",
        "002a7f8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcab84",
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md#insn-00b5b688) · [`00b5b548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md#insn-00b5b548) · [`00b5b5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md#insn-00b5b5cc)
- 新版 [`00bcab88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcab88) · [`00bcaa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcaa48) · [`00bcaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaa0c.md#insn-00bcaacc)

~~~diff
- 00b5b688 ["INT_ADD", "register:40f0:8", ["const:b5b688:8", "const:4:8"]]
- 00b5b688 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcab88 ["INT_ADD", "register:40f0:8", ["const:bcab88:8", "const:4:8"]]
+ 00bcab88 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5b688 bytes be0a0294
+ 00bcab88 bytes 1e400294
- 00b5b548 ["INT_ADD", "register:40f0:8", ["const:b5b548:8", "const:4:8"]]
- 00b5b548 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcaa48 ["INT_ADD", "register:40f0:8", ["const:bcaa48:8", "const:4:8"]]
+ 00bcaa48 ["CALL", null, ["callee:00c5a600:8"]]
- 00b5b548 bytes b6090294
+ 00bcaa48 bytes ee3e0294
- 00b5b5cc ["INT_ADD", "register:40f0:8", ["const:b5b5cc:8", "const:4:8"]]
- 00b5b5cc ["CALL", null, ["callee:00c5d6f0:8"]]
+ 00bcaacc ["INT_ADD", "register:40f0:8", ["const:bcaacc:8", "const:4:8"]]
+ 00bcaacc ["CALL", null, ["callee:00c5d6f0:8"]]
- 00b5b5cc bytes 49150294
+ 00bcaacc bytes 094b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d43daa303f7d6cef0453c970139b580"></a>

### [`00b5b6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md) → [`00bcabdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be09e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 79.63% / 新版 82.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b804"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b878"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcad04"
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
      "unmatched:00b5b804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcad1c"
      ]
    ],
    [
      "00bcad5c",
      "PARAM",
      [
        "storage",
        "002a7f8a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5b878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcad94"
      ]
    ]
  ],
  "added": [
    [
      "00bcad04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcad1c"
      ]
    ],
    [
      "00bcad5c",
      "PARAM",
      [
        "storage",
        "002b8c2c",
        null,
        "string"
      ]
    ],
    [
      "00bcad78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcad94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md#insn-00b5b804) · [`00b5b860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md#insn-00b5b860) · [`00b5b878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md#insn-00b5b878)
- 新版 [`00bcad60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcabdc.md#insn-00bcad60)

~~~diff
- 00b5b804 ["CBRANCH", null, ["local:b26:8", "register:101:1"]]
- 00b5b804 bytes c0000054
- 00b5b860 ["INT_ADD", "register:40f0:8", ["const:b5b860:8", "const:4:8"]]
- 00b5b860 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcad60 ["INT_ADD", "register:40f0:8", ["const:bcad60:8", "const:4:8"]]
+ 00bcad60 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5b860 bytes 480a0294
+ 00bcad60 bytes a83f0294
- 00b5b878 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5b878 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 00b5b878 bytes e1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92fa1dbb95b38d6500c768e9373233a4"></a>

### [`00b5b9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md) → [`00bcaec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcaec8.md) _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a60.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a00.md)
- 新版 呼出元 1件 [`00c5d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d600.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.07% / 新版 79.07%

CFGの説明率　旧版 51.43% / 新版 43.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b9cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b9c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b9cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b9d0",
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
      "00bcaec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcaecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcaed0",
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

- 旧版 [`00b5b9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md#insn-00b5b9c8) · [`00b5b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md#insn-00b5b9cc) · [`00b5b9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md#insn-00b5b9d0)

~~~diff
- 00b5b9c8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5b9c8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5b9c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5b9c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5b9c8 bytes f85fbca9
- 00b5b9cc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5b9cc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b9cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5b9cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b9cc bytes f65701a9
- 00b5b9d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b9d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b9d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5b9d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b9d0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4053e780476c15c836373a737ed8360a"></a>

### [`00b5bbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bbb4.md) → [`00bcb0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md) _ZN8firebase4auth15IdTokenListenerD1Ev

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d660.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb0d4",
      "incomplete_value": true,
      "site": "00bcb0d4",
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
      "definition_site": "00b5bbd4",
      "incomplete_value": true,
      "site": "00b5bbd4",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bc10"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcb110"
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
      "00bcb0c4",
      "READ",
      [
        "storage",
        "00c1bb80",
        null,
        "pointer"
      ]
    ],
    [
      "00bcb0d4",
      "DATA",
      [
        "storage",
        "00c11b58",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bcb0c4",
      "READ",
      [
        "storage",
        "00c9b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcb0d4",
      "DATA",
      [
        "storage",
        "00c91500",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bbb4.md#insn-00b5bc10) · [`00b5bbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bbb4.md#insn-00b5bbc0)
- 新版 [`00bcb110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md#insn-00bcb110) · [`00bcb0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb0b4.md#insn-00bcb0c0)

~~~diff
- 00b5bc10 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5bc10 ["RETURN", null, ["register:0:8"]]
- 00b5bc10 bytes c0035fd6
+ 00bcb110 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcb110 ["RETURN", null, ["register:0:8"]]
+ 00bcb110 bytes c0035fd6
- 00b5bbc0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bcb0c0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b5bbc0 bytes 08060090
+ 00bcb0c0 bytes 88060090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1880310049cccac3001b4e3bef0437f"></a>

### [`00b5bc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bc2c.md) → [`00bcb12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb12c.md) _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a10.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 1件 [`00c5d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d610.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.79% / 新版 90.79%

CFGの説明率　旧版 72.41% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bc30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bc30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bc34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5bc30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5bc34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5bc38",
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
      "00bcb130",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb134",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcb138",
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

- 旧版 [`00b5bc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bc2c.md#insn-00b5bc30) · [`00b5bc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bc2c.md#insn-00b5bc34) · [`00b5bc38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bc2c.md#insn-00b5bc38)

~~~diff
- 00b5bc30 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5bc30 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5bc30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5bc30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5bc30 bytes f65702a9
- 00b5bc34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5bc34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5bc34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5bc34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5bc34 bytes f44f03a9
- 00b5bc38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5bc38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5bc38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5bc38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5bc38 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8f85d22e99aae1140a248a4cfef687"></a>

### [`00b5be54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5be54.md) → [`00bcb354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be09f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09f0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 1件 [`00c5d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 76.67% / 新版 82.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bf14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcb414"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb384",
      "incomplete_value": true,
      "site": "00bcb390",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b5bea4",
      "PARAM",
      [
        "storage",
        "002965d8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5bf14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb450"
      ]
    ]
  ],
  "added": [
    [
      "00bcb3a4",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00bcb414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5be90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5be54.md#insn-00b5be90) · [`00b5bea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5be54.md#insn-00b5bea8) · [`00b5bf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5be54.md#insn-00b5bf14)
- 新版 [`00bcb390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md#insn-00bcb390) · [`00bcb3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb354.md#insn-00bcb3a8)

~~~diff
- 00b5be90 ["INT_ADD", "register:40f0:8", ["const:b5be90:8", "const:4:8"]]
- 00b5be90 ["CALL", null, ["callee:00c5d6e0:8"]]
+ 00bcb390 ["INT_ADD", "register:40f0:8", ["const:bcb390:8", "const:4:8"]]
+ 00bcb390 ["CALL", null, ["callee:00c5d6e0:8"]]
- 00b5be90 bytes 14130294
+ 00bcb390 bytes d4480294
- 00b5bea8 ["INT_ADD", "register:40f0:8", ["const:b5bea8:8", "const:4:8"]]
- 00b5bea8 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bcb3a8 ["INT_ADD", "register:40f0:8", ["const:bcb3a8:8", "const:4:8"]]
+ 00bcb3a8 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b5bea8 bytes 02090294
+ 00bcb3a8 bytes 623e0294
- 00b5bf14 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b5bf14 bytes e0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cee12935ba07fd327086a7e03244e572"></a>

### [`00b5c07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c07c.md) → [`00bcb57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md) _ZNK8firebase4auth4Auth32FetchProvidersForEmailLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

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
      "site": "00bcb5b4",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5c0b4",
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
      "site": "00bcb5c4",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5c0c4",
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
      "00bcb5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bcb5c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bcb5b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bcb5c4",
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

- 旧版 [`00b5c0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c07c.md#insn-00b5c0b4) · [`00b5c0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c07c.md#insn-00b5c0c4) · [`00b5c09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c07c.md#insn-00b5c09c)
- 新版 [`00bcb5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb5b4) · [`00bcb5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb5c4) · [`00bcb59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb57c.md#insn-00bcb59c)

~~~diff
- 00b5c0b4 ["INT_ADD", "register:40f0:8", ["const:b5c0b4:8", "const:4:8"]]
- 00b5c0b4 ["CALL", null, ["ram:bdde10:8"]]
+ 00bcb5b4 ["INT_ADD", "register:40f0:8", ["const:bcb5b4:8", "const:4:8"]]
+ 00bcb5b4 ["CALL", null, ["ram:c5a870:8"]]
- 00b5c0b4 bytes 57070294
+ 00bcb5b4 bytes af3c0294
- 00b5c0c4 ["INT_ADD", "register:40f0:8", ["const:b5c0c4:8", "const:4:8"]]
- 00b5c0c4 ["CALL", null, ["ram:bddf90:8"]]
+ 00bcb5c4 ["INT_ADD", "register:40f0:8", ["const:bcb5c4:8", "const:4:8"]]
+ 00bcb5c4 ["CALL", null, ["ram:c5aa10:8"]]
- 00b5c0c4 bytes b3070294
+ 00bcb5c4 bytes 133d0294
- 00b5c09c ["INT_ADD", "register:40f0:8", ["const:b5c09c:8", "const:4:8"]]
- 00b5c09c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcb59c ["INT_ADD", "register:40f0:8", ["const:bcb59c:8", "const:4:8"]]
+ 00bcb59c ["CALL", null, ["callee:00c5a600:8"]]
- 00b5c09c bytes e1060294
+ 00bcb59c bytes 193c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd312233ec3f02472d0a4cf165392f21"></a>

### [`00b5c10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c10c.md) → [`00bcb60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md) _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c14c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcb64c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb628",
      "incomplete_value": true,
      "site": "00bcb62c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c128",
      "incomplete_value": true,
      "site": "00b5c12c",
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
              [
                "live",
                "register:4000:8"
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
      "unmatched:00b5c144",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b5c154",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bcb644",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bcb654",
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

- 旧版 [`00b5c12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c10c.md#insn-00b5c12c) · [`00b5c144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c10c.md#insn-00b5c144) · [`00b5c14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c10c.md#insn-00b5c14c)
- 新版 [`00bcb62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb60c.md#insn-00bcb62c)

~~~diff
- 00b5c12c ["INT_ADD", "register:40f0:8", ["const:b5c12c:8", "const:4:8"]]
- 00b5c12c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcb62c ["INT_ADD", "register:40f0:8", ["const:bcb62c:8", "const:4:8"]]
+ 00bcb62c ["CALL", null, ["callee:00c5a600:8"]]
- 00b5c12c bytes bd060294
+ 00bcb62c bytes f53b0294
- 00b5c144 ["INT_ADD", "register:40f0:8", ["const:b5c144:8", "const:4:8"]]
- 00b5c144 ["CALL", null, ["ram:bdde10:8"]]
- 00b5c144 bytes 33070294
- 00b5c14c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b5c14c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5c14c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5c14c bytes 7f1600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0175b28759d4e9463d472ea5c1086814"></a>

### [`00b5c19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c19c.md) → [`00bcb69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c19c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c1a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c19c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c1a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c1a4",
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
      "00bcb69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcb6a4",
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

- 旧版 [`00b5c19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c19c.md#insn-00b5c19c) · [`00b5c1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c19c.md#insn-00b5c1a0) · [`00b5c1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c19c.md#insn-00b5c1a4)

~~~diff
- 00b5c19c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c19c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c19c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c19c bytes f50f1df8
- 00b5c1a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c1a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c1a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c1a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c1a0 bytes f44f01a9
- 00b5c1a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c1a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c1a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c1a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c1a4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0212e5b07085ab205b31b03aa6211080"></a>

### [`00b5c2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md) → [`00bcb7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb7bc.md) _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcb7fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c2f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c2f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b5c304",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bcb7f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bcb804",
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

- 旧版 [`00b5c2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md#insn-00b5c2f4) · [`00b5c2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md#insn-00b5c2fc) · [`00b5c304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c2bc.md#insn-00b5c304)

~~~diff
- 00b5c2f4 ["INT_ADD", "register:40f0:8", ["const:b5c2f4:8", "const:4:8"]]
- 00b5c2f4 ["CALL", null, ["ram:bdde10:8"]]
- 00b5c2f4 bytes c7060294
- 00b5c2fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b5c2fc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5c2fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5c2fc bytes 7f1600f9
- 00b5c304 ["INT_ADD", "register:40f0:8", ["const:b5c304:8", "const:4:8"]]
- 00b5c304 ["CALL", null, ["ram:bddf90:8"]]
- 00b5c304 bytes 23070294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21354840314cb3786b186174d6e17dd5"></a>

### [`00b5c3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md) → [`00bcb8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md) _ZNK8firebase4auth4Auth40CreateUserWithEmailAndPasswordLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

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
      "site": "00bcb914",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5c414",
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
      "site": "00bcb924",
      "value": [
        "leaf",
        "ram:c5aa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5c424",
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
      "00bcb914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "00bcb924",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00bcb914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00bcb924",
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

- 旧版 [`00b5c414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md#insn-00b5c414) · [`00b5c424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md#insn-00b5c424) · [`00b5c3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c3dc.md#insn-00b5c3fc)
- 新版 [`00bcb914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb914) · [`00bcb924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb924) · [`00bcb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb8dc.md#insn-00bcb8fc)

~~~diff
- 00b5c414 ["INT_ADD", "register:40f0:8", ["const:b5c414:8", "const:4:8"]]
- 00b5c414 ["CALL", null, ["ram:bdde10:8"]]
+ 00bcb914 ["INT_ADD", "register:40f0:8", ["const:bcb914:8", "const:4:8"]]
+ 00bcb914 ["CALL", null, ["ram:c5a870:8"]]
- 00b5c414 bytes 7f060294
+ 00bcb914 bytes d73b0294
- 00b5c424 ["INT_ADD", "register:40f0:8", ["const:b5c424:8", "const:4:8"]]
- 00b5c424 ["CALL", null, ["ram:bddf90:8"]]
+ 00bcb924 ["INT_ADD", "register:40f0:8", ["const:bcb924:8", "const:4:8"]]
+ 00bcb924 ["CALL", null, ["ram:c5aa10:8"]]
- 00b5c424 bytes db060294
+ 00bcb924 bytes 3b3c0294
- 00b5c3fc ["INT_ADD", "register:40f0:8", ["const:b5c3fc:8", "const:4:8"]]
- 00b5c3fc ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcb8fc ["INT_ADD", "register:40f0:8", ["const:bcb8fc:8", "const:4:8"]]
+ 00bcb8fc ["CALL", null, ["callee:00c5a600:8"]]
- 00b5c3fc bytes 09060294
+ 00bcb8fc bytes 413b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-160124ff05fa58a8dd8c8c4139e0c27c"></a>

### [`00b5c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md) → [`00bcb984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) FUN_00bcb984

採用 · 移動量 `+0x6f500` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b5ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md) · 呼出先 2件 [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00be0a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a30.md)
- 新版 呼出元 1件 [`00bca368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca368.md) · 呼出先 2件 [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5d630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d630.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb99c",
      "incomplete_value": false,
      "site": "00bcb9a8",
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
            "const:b8f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c49c",
      "incomplete_value": false,
      "site": "00b5c4a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:279:8"
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
      "00bcb99c",
      "PARAM",
      [
        "storage",
        "00294279",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb99c",
      "PARAM",
      [
        "storage",
        "002a3b8f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md#insn-00b5c4a8) · [`00b5c498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md#insn-00b5c498) · [`00b5c49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md#insn-00b5c49c)
- 新版 [`00bcb9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md#insn-00bcb9a8) · [`00bcb998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md#insn-00bcb998) · [`00bcb99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md#insn-00bcb99c)

~~~diff
- 00b5c4a8 ["INT_ADD", "register:40f0:8", ["const:b5c4a8:8", "const:4:8"]]
- 00b5c4a8 ["CALL", null, ["callee:00c5a9e0:8"]]
+ 00bcb9a8 ["INT_ADD", "register:40f0:8", ["const:bcb9a8:8", "const:4:8"]]
+ 00bcb9a8 ["CALL", null, ["callee:00c5a9e0:8"]]
- 00b5c4a8 bytes ae060294
+ 00bcb9a8 bytes 0e3c0294
- 00b5c498 ["COPY", "register:4000:8", ["const:294000:8"]]
+ 00bcb998 ["COPY", "register:4000:8", ["const:2a3000:8"]]
- 00b5c498 bytes c0b9ff90
+ 00bcb998 bytes c0b6ff90
- 00b5c49c ["COPY", "tmp:0:8", ["const:279:8"]]
- 00b5c49c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c49c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c49c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcb99c ["COPY", "tmp:0:8", ["const:b8f:8"]]
+ 00bcb99c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcb99c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcb99c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c49c bytes 00e40991
+ 00bcb99c bytes 003c2e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6b24f09debd7185948192d181e216e"></a>

### [`00b5c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md) → [`00bcb9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md) _ZNSt6__ndk16__treeINS_12__value_typeIPN8firebase3AppEPNS2_4auth4AuthEEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ac0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ac0.md)
- 新版 呼出元 1件 [`00c5d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5c4d0",
      "incomplete_value": true,
      "site": "00b5c4d8",
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
            "register:4008:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md#insn-00b5c4d8) · [`00b5c4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md#insn-00b5c4bc) · [`00b5c4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4bc.md#insn-00b5c4e4)
- 新版 [`00bcb9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9d8) · [`00bcb9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9bc) · [`00bcb9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb9bc.md#insn-00bcb9e4)

~~~diff
- 00b5c4d8 ["INT_ADD", "register:40f0:8", ["const:b5c4d8:8", "const:4:8"]]
- 00b5c4d8 ["CALL", null, ["callee:00c5d6c0:8"]]
+ 00bcb9d8 ["INT_ADD", "register:40f0:8", ["const:bcb9d8:8", "const:4:8"]]
+ 00bcb9d8 ["CALL", null, ["callee:00c5d6c0:8"]]
- 00b5c4d8 bytes 7a110294
+ 00bcb9d8 bytes 3a470294
- 00b5c4bc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5c4bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bcb9bc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcb9bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5c4bc bytes e10100b4
+ 00bcb9bc bytes e10100b4
- 00b5c4e4 ["INT_ADD", "register:40f0:8", ["const:b5c4e4:8", "const:4:8"]]
- 00b5c4e4 ["CALL", null, ["callee:00c5d6c0:8"]]
+ 00bcb9e4 ["INT_ADD", "register:40f0:8", ["const:bcb9e4:8", "const:4:8"]]
+ 00bcb9e4 ["CALL", null, ["callee:00c5d6c0:8"]]
- 00b5c4e4 bytes 77110294
+ 00bcb9e4 bytes 37470294
~~~


<a id="compare-4415be2b7432586b80c0e6511044c3c3"></a>

### [`00b5c5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md) → [`00bcbaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b10.md) · 呼出先 5件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d710.md) · 呼出先 5件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 47.06% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c624"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c688"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcbb24"
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
      "unmatched:00b5c624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbbe4"
      ]
    ],
    [
      "unmatched:00b5c65c",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5c660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ae04c0"
      ]
    ]
  ],
  "added": [
    [
      "00bcbb24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbbe4"
      ]
    ],
    [
      "00bcbb5c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "00bcbb60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3fe98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md#insn-00b5c624) · [`00b5c660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md#insn-00b5c660) · [`00b5c688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md#insn-00b5c688)

~~~diff
- 00b5c624 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5c624 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b5c624 bytes 090600b5
- 00b5c660 ["INT_ADD", "register:40f0:8", ["const:b5c660:8", "const:4:8"]]
- 00b5c660 ["CALL", null, ["ram:ae04c0:8"]]
- 00b5c660 bytes 980ffe97
- 00b5c688 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b5c688 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b5c688 bytes ab000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63edda289fcbeefba9e98193a1b61a35"></a>

### [`00b5c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md) → [`00bcbbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ad0.md) · 呼出先 5件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d6d0.md) · 呼出先 5件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c77c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcbc7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcbc54",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ],
    [
      "00bcbc58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ae04c0"
      ]
    ],
    [
      "unmatched:00b5c780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbc94"
      ]
    ]
  ],
  "added": [
    [
      "00bcbc54",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "00bcbc58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3fe98"
      ]
    ],
    [
      "00bcbc80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcbc94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md#insn-00b5c758) · [`00b5c77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md#insn-00b5c77c) · [`00b5c780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md#insn-00b5c780)
- 新版 [`00bcbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbbec.md#insn-00bcbc58)

~~~diff
- 00b5c758 ["INT_ADD", "register:40f0:8", ["const:b5c758:8", "const:4:8"]]
- 00b5c758 ["CALL", null, ["ram:ae04c0:8"]]
+ 00bcbc58 ["INT_ADD", "register:40f0:8", ["const:bcbc58:8", "const:4:8"]]
+ 00bcbc58 ["CALL", null, ["ram:b3fe98:8"]]
- 00b5c758 bytes 5a0ffe97
+ 00bcbc58 bytes 90d0fd97
- 00b5c77c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5c77c ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b5c77c ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:8:8"]]
- 00b5c77c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5c77c bytes 088700f8
- 00b5c780 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b5c780 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b5c780 bytes ab000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43147e795b10430e6f508d751c01f9f1"></a>

### [`00b5c7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md) → [`00bcbce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbce4.md) _INIT_290

採用 · 移動量 `+0x6f500` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5aba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aba8.md) [`00b5abb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abb0.md) [`00b5abb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abb4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bca0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0a8.md) [`00bca0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b0.md) [`00bca0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca0b4.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_argument_candidate, call_target, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 62.16% / 新版 62.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c800",
      "PARAM",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5c810",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5c810",
      "DATA",
      [
        "storage",
        "002ab1a7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcbd00",
      "PARAM",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbd10",
      "WRITE",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbd10",
      "DATA",
      [
        "storage",
        "002bc0ca",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md#insn-00b5c810) · [`00b5c814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md#insn-00b5c814) · [`00b5c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md#insn-00b5c818)

~~~diff
- 00b5c810 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5c810 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b5c810 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00b5c810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c810 bytes 082400a9
- 00b5c814 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b5c814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b5c814 bytes 0a0800f9
- 00b5c818 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5c818 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5c818 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00b5c818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5c818 bytes 1f600039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d85c0f4fbec391f3eafde2f97d0ee7e"></a>

### [`00b5c8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md) → [`00bcbda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5a0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md#insn-00b5c8c4) · [`00b5c8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md#insn-00b5c8d4) · [`00b5c8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c8a8.md#insn-00b5c8f0)
- 新版 [`00bcbdc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md#insn-00bcbdc4) · [`00bcbdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md#insn-00bcbdd4) · [`00bcbdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md#insn-00bcbdf0)

~~~diff
- 00b5c8c4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00bcbdc4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b5c8c4 bytes 60020054
+ 00bcbdc4 bytes 60020054
- 00b5c8d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b5c8d4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcbdd4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bcbdd4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5c8d4 bytes 400100b5
+ 00bcbdd4 bytes 400100b5
- 00b5c8f0 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
+ 00bcbdf0 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00b5c8f0 bytes 02010054
+ 00bcbdf0 bytes 02010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea31c0e0e9900b48769f24b968503d5f"></a>

### [`00b5c9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md) → [`00bcbee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcbf10",
      "incomplete_value": true,
      "site": "00bcbf10",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca10",
      "incomplete_value": true,
      "site": "00b5ca10",
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
            "const:420:8"
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
      "definition_site": "00bcbef8",
      "incomplete_value": true,
      "site": "00bcbef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5c9f8",
      "incomplete_value": true,
      "site": "00b5c9f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcbf04",
      "incomplete_value": false,
      "site": "00bcbf08",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca04",
      "incomplete_value": false,
      "site": "00b5ca08",
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
            "const:fd6:8"
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
      "00bcbef4",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf04",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bcbf10",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcbef4",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf04",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcbf10",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md#insn-00b5ca08) · [`00b5ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md#insn-00b5ca10) · [`00b5c9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md#insn-00b5c9f0)
- 新版 [`00bcbf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbf08) · [`00bcbf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbf10) · [`00bcbef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbee4.md#insn-00bcbef0)

~~~diff
- 00b5ca08 ["INT_ADD", "register:40f0:8", ["const:b5ca08:8", "const:4:8"]]
- 00b5ca08 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcbf08 ["INT_ADD", "register:40f0:8", ["const:bcbf08:8", "const:4:8"]]
+ 00bcbf08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5ca08 bytes a2050294
+ 00bcbf08 bytes 023b0294
- 00b5ca10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
- 00b5ca10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcbf10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcbf10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca10 bytes 601202f9
+ 00bcbf10 bytes 609601f9
- 00b5c9f0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcbef0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5c9f0 bytes 332a00b0
+ 00bcbef0 bytes d32a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb47af488984e3873756d79fadf237e"></a>

### [`00b5ca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca24.md) → [`00bcbf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcbf50",
      "incomplete_value": true,
      "site": "00bcbf50",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca50",
      "incomplete_value": true,
      "site": "00b5ca50",
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
            "const:420:8"
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
      "definition_site": "00bcbf38",
      "incomplete_value": true,
      "site": "00bcbf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5ca38",
      "incomplete_value": true,
      "site": "00b5ca38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcbf40",
      "incomplete_value": false,
      "site": "00bcbf48",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca40",
      "incomplete_value": false,
      "site": "00b5ca48",
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
            "const:fd6:8"
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
      "00bcbf34",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf40",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bcbf50",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcbf34",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf40",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcbf50",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca24.md#insn-00b5ca48) · [`00b5ca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca24.md#insn-00b5ca50) · [`00b5ca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca24.md#insn-00b5ca30)
- 新版 [`00bcbf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf48) · [`00bcbf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf50) · [`00bcbf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf24.md#insn-00bcbf30)

~~~diff
- 00b5ca48 ["INT_ADD", "register:40f0:8", ["const:b5ca48:8", "const:4:8"]]
- 00b5ca48 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcbf48 ["INT_ADD", "register:40f0:8", ["const:bcbf48:8", "const:4:8"]]
+ 00bcbf48 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5ca48 bytes 92050294
+ 00bcbf48 bytes f23a0294
- 00b5ca50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
- 00b5ca50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcbf50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcbf50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca50 bytes 601202f9
+ 00bcbf50 bytes 609601f9
- 00b5ca30 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcbf30 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5ca30 bytes 332a00b0
+ 00bcbf30 bytes d32a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c13d9f309ba1a58d71e75eefb1285b31"></a>

### [`00b5ca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca64.md) → [`00bcbf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcbf94",
      "incomplete_value": true,
      "site": "00bcbf94",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca94",
      "incomplete_value": true,
      "site": "00b5ca94",
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
            "const:420:8"
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
      "definition_site": "00bcbf78",
      "incomplete_value": true,
      "site": "00bcbf78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5ca78",
      "incomplete_value": true,
      "site": "00b5ca78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcbf84",
      "incomplete_value": false,
      "site": "00bcbf8c",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca84",
      "incomplete_value": false,
      "site": "00b5ca8c",
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
            "const:fd6:8"
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
      "00bcbf74",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf84",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bcbf94",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcbf74",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbf84",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcbf94",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca64.md#insn-00b5ca8c) · [`00b5ca94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca64.md#insn-00b5ca94) · [`00b5ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca64.md#insn-00b5ca70)
- 新版 [`00bcbf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf8c) · [`00bcbf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf94) · [`00bcbf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbf64.md#insn-00bcbf70)

~~~diff
- 00b5ca8c ["INT_ADD", "register:40f0:8", ["const:b5ca8c:8", "const:4:8"]]
- 00b5ca8c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcbf8c ["INT_ADD", "register:40f0:8", ["const:bcbf8c:8", "const:4:8"]]
+ 00bcbf8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5ca8c bytes 81050294
+ 00bcbf8c bytes e13a0294
- 00b5ca94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
- 00b5ca94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcbf94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcbf94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca94 bytes 601202f9
+ 00bcbf94 bytes 609601f9
- 00b5ca70 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcbf70 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5ca70 bytes 332a00b0
+ 00bcbf70 bytes d32a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3984014534fc7391625cfcedba4bc71"></a>

### [`00b5caa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md) → [`00bcbfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcbfd8",
      "incomplete_value": true,
      "site": "00bcbfd8",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cad8",
      "incomplete_value": true,
      "site": "00b5cad8",
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
            "const:420:8"
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
      "definition_site": "00bcbfbc",
      "incomplete_value": true,
      "site": "00bcbfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cabc",
      "incomplete_value": true,
      "site": "00b5cabc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcbfc4",
      "incomplete_value": false,
      "site": "00bcbfd0",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cac4",
      "incomplete_value": false,
      "site": "00b5cad0",
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
            "const:fd6:8"
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
      "00bcbfb8",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbfc4",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bcbfd8",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcbfb8",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcbfc4",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcbfd8",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md#insn-00b5cad0) · [`00b5cad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md#insn-00b5cad8) · [`00b5cab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md#insn-00b5cab4)
- 新版 [`00bcbfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfd0) · [`00bcbfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfd8) · [`00bcbfb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfa8.md#insn-00bcbfb4)

~~~diff
- 00b5cad0 ["INT_ADD", "register:40f0:8", ["const:b5cad0:8", "const:4:8"]]
- 00b5cad0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcbfd0 ["INT_ADD", "register:40f0:8", ["const:bcbfd0:8", "const:4:8"]]
+ 00bcbfd0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cad0 bytes 70050294
+ 00bcbfd0 bytes d03a0294
- 00b5cad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
- 00b5cad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcbfd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00bcbfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cad8 bytes 601202f9
+ 00bcbfd8 bytes 609601f9
- 00b5cab4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcbfb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5cab4 bytes 332a00b0
+ 00bcbfb4 bytes d32a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf9f18b667b32122232a941be88aa03"></a>

### [`00b5caf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md) → [`00bcbff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cb50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc050"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcc02c",
      "incomplete_value": true,
      "site": "00bcc038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb2c",
      "incomplete_value": true,
      "site": "00b5cb38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
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
      "00bcc00c",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b5cb2c",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5cb50",
      "WRITE",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc00c",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc02c",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc050",
      "WRITE",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md#insn-00b5cb38) · [`00b5cb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md#insn-00b5cb44) · [`00b5cb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md#insn-00b5cb50)
- 新版 [`00bcc038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md#insn-00bcc038) · [`00bcc044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbff8.md#insn-00bcc044)

~~~diff
- 00b5cb38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cb38 ["INT_ADD", "register:40f0:8", ["const:b5cb38:8", "const:4:8"]]
- 00b5cb38 ["CALLIND", null, ["register:0:8"]]
+ 00bcc038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc038 ["INT_ADD", "register:40f0:8", ["const:bcc038:8", "const:4:8"]]
+ 00bcc038 ["CALLIND", null, ["register:0:8"]]
- 00b5cb38 bytes 00013fd6
+ 00bcc038 bytes 00013fd6
- 00b5cb44 ["INT_ADD", "register:40f0:8", ["const:b5cb44:8", "const:4:8"]]
- 00b5cb44 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00bcc044 ["INT_ADD", "register:40f0:8", ["const:bcc044:8", "const:4:8"]]
+ 00bcc044 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b5cb44 bytes 67050294
+ 00bcc044 bytes c73a0294
- 00b5cb50 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5cb50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:428:8"]]
- 00b5cb50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5cb50 bytes a0a21039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e867c1356f7dc9f26c845de207ad13d1"></a>

### [`00b5cb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cb64.md) → [`00bcc064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00bcc0a0",
      "incomplete_value": true,
      "site": "00bcc0a0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cba0",
      "incomplete_value": true,
      "site": "00b5cba0",
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
            "const:428:8"
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
      "definition_site": "00bcc0c0",
      "incomplete_value": true,
      "site": "00bcc0c0",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbc0",
      "incomplete_value": true,
      "site": "00b5cbc0",
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
            "const:420:8"
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
      "definition_site": "00bcc07c",
      "incomplete_value": true,
      "site": "00bcc07c",
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
      "definition_site": "00b5cb7c",
      "incomplete_value": true,
      "site": "00b5cb7c",
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
      "00bcc078",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc084",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc0a0",
      "WRITE",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc078",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc084",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc0a0",
      "WRITE",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cb64.md#insn-00b5cba0) · [`00b5cbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cb64.md#insn-00b5cbbc) · [`00b5cbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cb64.md#insn-00b5cbc0)
- 新版 [`00bcc0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0a0) · [`00bcc0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0bc) · [`00bcc0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc064.md#insn-00bcc0c0)

~~~diff
- 00b5cba0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5cba0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5cba0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:428:8"]]
- 00b5cba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bcc0a0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bcc0a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bcc0a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
+ 00bcc0a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5cba0 bytes bfa21039
+ 00bcc0a0 bytes bfc20c39
- 00b5cbbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cbbc ["INT_ADD", "register:40f0:8", ["const:b5cbbc:8", "const:4:8"]]
- 00b5cbbc ["CALLIND", null, ["register:0:8"]]
+ 00bcc0bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc0bc ["INT_ADD", "register:40f0:8", ["const:bcc0bc:8", "const:4:8"]]
+ 00bcc0bc ["CALLIND", null, ["register:0:8"]]
- 00b5cbbc bytes 00013fd6
+ 00bcc0bc bytes 00013fd6
- 00b5cbc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
- 00b5cbc0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b5cbc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bcc0c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcc0c0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bcc0c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b5cbc0 bytes 9f1202f9
+ 00bcc0c0 bytes 9f9601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb9773f603edcc3ab2205a4af93bfae"></a>

### [`00b5cbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cbd4.md) → [`00bcc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc114",
      "incomplete_value": true,
      "site": "00bcc114",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc14",
      "incomplete_value": true,
      "site": "00b5cc14",
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
            "const:420:8"
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
      "definition_site": "00bcc0f0",
      "incomplete_value": true,
      "site": "00bcc0f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cbf0",
      "incomplete_value": true,
      "site": "00b5cbf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc0f8",
      "incomplete_value": false,
      "site": "00bcc10c",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbf8",
      "incomplete_value": false,
      "site": "00b5cc0c",
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
            "const:fd6:8"
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
      "00bcc0e8",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc0f8",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00bcc114",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc0e8",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc0f8",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00bcc114",
      "WRITE",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cbd4.md#insn-00b5cc0c) · [`00b5cc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cbd4.md#insn-00b5cc14) · [`00b5cbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cbd4.md#insn-00b5cbe0)
- 新版 [`00bcc10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc10c) · [`00bcc114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc114) · [`00bcc0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc0d4.md#insn-00bcc0e0)

~~~diff
- 00b5cc0c ["INT_ADD", "register:40f0:8", ["const:b5cc0c:8", "const:4:8"]]
- 00b5cc0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc10c ["INT_ADD", "register:40f0:8", ["const:bcc10c:8", "const:4:8"]]
+ 00bcc10c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cc0c bytes 21050294
+ 00bcc10c bytes 813a0294
- 00b5cc14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
- 00b5cc14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc114 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00bcc114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cc14 bytes 801202f9
+ 00bcc114 bytes 809601f9
- 00b5cbe0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bcc0e0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b5cbe0 bytes 342a00b0
+ 00bcc0e0 bytes d42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b7ebc57a3e276a125a117bfd6db3a8b"></a>

### [`00b5cc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc44.md) → [`00bcc144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc160",
      "incomplete_value": false,
      "site": "00bcc164",
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
      "definition_site": "00b5cc60",
      "incomplete_value": false,
      "site": "00b5cc64",
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
      "definition_site": "00bcc170",
      "incomplete_value": true,
      "site": "00bcc17c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5cc70",
      "incomplete_value": true,
      "site": "00b5cc7c",
      "value": [
        "LOAD",
        "8",
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
      "00bcc160",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bcc170",
      "DATA",
      [
        "storage",
        "010a1430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc160",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bcc170",
      "DATA",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc44.md#insn-00b5cc64) · [`00b5cc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc44.md#insn-00b5cc5c) · [`00b5cc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc44.md#insn-00b5cc60)
- 新版 [`00bcc164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc164) · [`00bcc15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc15c) · [`00bcc160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc144.md#insn-00bcc160)

~~~diff
- 00b5cc64 ["INT_ADD", "register:40f0:8", ["const:b5cc64:8", "const:4:8"]]
- 00b5cc64 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcc164 ["INT_ADD", "register:40f0:8", ["const:bcc164:8", "const:4:8"]]
+ 00bcc164 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5cc64 bytes 47050294
+ 00bcc164 bytes a73a0294
- 00b5cc5c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bcc15c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b5cc5c bytes e0b9ff90
+ 00bcc15c bytes e0b6ff90
- 00b5cc60 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5cc60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc160 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bcc160 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc160 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc160 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cc60 bytes 001c1591
+ 00bcc160 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c47d3466406762c54a3c807a3fc8228"></a>

### [`00b5cc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc80.md) → [`00bcc180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b5ccc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc1c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cc9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5cc94",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5cc9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc1c4"
      ]
    ],
    [
      "unmatched:00b5cca4",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc194",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc19c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc1c4"
      ]
    ],
    [
      "00bcc1a4",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc80.md#insn-00b5cc9c) · [`00b5ccb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc80.md#insn-00b5ccb8) · [`00b5ccc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc80.md#insn-00b5ccc0)
- 新版 [`00bcc1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc180.md#insn-00bcc1b8)

~~~diff
- 00b5cc9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5cc9c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5cc9c bytes 410100b5
- 00b5ccb8 ["INT_ADD", "register:40f0:8", ["const:b5ccb8:8", "const:4:8"]]
- 00b5ccb8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc1b8 ["INT_ADD", "register:40f0:8", ["const:bcc1b8:8", "const:4:8"]]
+ 00bcc1b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5ccb8 bytes f6040294
+ 00bcc1b8 bytes 563a0294
- 00b5ccc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
- 00b5ccc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ccc0 bytes 801202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91dfd16e89743c56b59f5bfa5917bdaa"></a>

### [`00b5cd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd2c.md) → [`00bcc22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc258",
      "incomplete_value": true,
      "site": "00bcc258",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd58",
      "incomplete_value": true,
      "site": "00b5cd58",
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
            "const:4c8:8"
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
      "definition_site": "00bcc240",
      "incomplete_value": true,
      "site": "00bcc240",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cd40",
      "incomplete_value": true,
      "site": "00b5cd40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc24c",
      "incomplete_value": false,
      "site": "00bcc250",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd4c",
      "incomplete_value": false,
      "site": "00b5cd50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
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
      "00bcc23c",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc24c",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00bcc258",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc23c",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc24c",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc258",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd2c.md#insn-00b5cd50) · [`00b5cd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd2c.md#insn-00b5cd58) · [`00b5cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd2c.md#insn-00b5cd38)
- 新版 [`00bcc250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc250) · [`00bcc258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc258) · [`00bcc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc22c.md#insn-00bcc238)

~~~diff
- 00b5cd50 ["INT_ADD", "register:40f0:8", ["const:b5cd50:8", "const:4:8"]]
- 00b5cd50 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc250 ["INT_ADD", "register:40f0:8", ["const:bcc250:8", "const:4:8"]]
+ 00bcc250 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cd50 bytes d0040294
+ 00bcc250 bytes 303a0294
- 00b5cd58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00b5cd58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc258 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd58 bytes 606602f9
+ 00bcc258 bytes 60ea01f9
- 00b5cd38 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc238 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5cd38 bytes 332a00b0
+ 00bcc238 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4d2b2e15c11ffc86b38385d342babbc"></a>

### [`00b5cd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd6c.md) → [`00bcc26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc298",
      "incomplete_value": true,
      "site": "00bcc298",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd98",
      "incomplete_value": true,
      "site": "00b5cd98",
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
            "const:4c8:8"
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
      "definition_site": "00bcc280",
      "incomplete_value": true,
      "site": "00bcc280",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cd80",
      "incomplete_value": true,
      "site": "00b5cd80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc288",
      "incomplete_value": false,
      "site": "00bcc290",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd88",
      "incomplete_value": false,
      "site": "00b5cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
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
      "00bcc27c",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc288",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00bcc298",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc27c",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc288",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc298",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd6c.md#insn-00b5cd90) · [`00b5cd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd6c.md#insn-00b5cd98) · [`00b5cd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd6c.md#insn-00b5cd78)
- 新版 [`00bcc290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc290) · [`00bcc298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc298) · [`00bcc278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc26c.md#insn-00bcc278)

~~~diff
- 00b5cd90 ["INT_ADD", "register:40f0:8", ["const:b5cd90:8", "const:4:8"]]
- 00b5cd90 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc290 ["INT_ADD", "register:40f0:8", ["const:bcc290:8", "const:4:8"]]
+ 00bcc290 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cd90 bytes c0040294
+ 00bcc290 bytes 203a0294
- 00b5cd98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00b5cd98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd98 bytes 606602f9
+ 00bcc298 bytes 60ea01f9
- 00b5cd78 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc278 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5cd78 bytes 332a00b0
+ 00bcc278 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12c56503cc2c1a062e41ef365a33724"></a>

### [`00b5cdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md) → [`00bcc2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc2dc",
      "incomplete_value": true,
      "site": "00bcc2dc",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cddc",
      "incomplete_value": true,
      "site": "00b5cddc",
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
            "const:4c8:8"
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
      "definition_site": "00bcc2c0",
      "incomplete_value": true,
      "site": "00bcc2c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cdc0",
      "incomplete_value": true,
      "site": "00b5cdc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc2cc",
      "incomplete_value": false,
      "site": "00bcc2d4",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cdcc",
      "incomplete_value": false,
      "site": "00b5cdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
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
      "00bcc2bc",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc2cc",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00bcc2dc",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc2bc",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc2cc",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc2dc",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md#insn-00b5cdd4) · [`00b5cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md#insn-00b5cddc) · [`00b5cdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md#insn-00b5cdb8)
- 新版 [`00bcc2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2d4) · [`00bcc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2dc) · [`00bcc2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md#insn-00bcc2b8)

~~~diff
- 00b5cdd4 ["INT_ADD", "register:40f0:8", ["const:b5cdd4:8", "const:4:8"]]
- 00b5cdd4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc2d4 ["INT_ADD", "register:40f0:8", ["const:bcc2d4:8", "const:4:8"]]
+ 00bcc2d4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cdd4 bytes af040294
+ 00bcc2d4 bytes 0f3a0294
- 00b5cddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00b5cddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d0:8"]]
+ 00bcc2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cddc bytes 606602f9
+ 00bcc2dc bytes 60ea01f9
- 00b5cdb8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc2b8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5cdb8 bytes 332a00b0
+ 00bcc2b8 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd604adc9d5597e28da612402ab371c"></a>

### [`00b5cdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdf0.md) → [`00bcc2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00b5ce20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc320"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ce04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcc300",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5ce04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc324"
      ]
    ],
    [
      "unmatched:00b5ce0c",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc300",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc324"
      ]
    ],
    [
      "00bcc30c",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ce04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdf0.md#insn-00b5ce04) · [`00b5ce18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdf0.md#insn-00b5ce18) · [`00b5ce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdf0.md#insn-00b5ce20)
- 新版 [`00bcc318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2f0.md#insn-00bcc318)

~~~diff
- 00b5ce04 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5ce04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5ce04 bytes 080100b5
- 00b5ce18 ["INT_ADD", "register:40f0:8", ["const:b5ce18:8", "const:4:8"]]
- 00b5ce18 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc318 ["INT_ADD", "register:40f0:8", ["const:bcc318:8", "const:4:8"]]
+ 00bcc318 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5ce18 bytes 9e040294
+ 00bcc318 bytes fe390294
- 00b5ce20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00b5ce20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ce20 bytes 606602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1913cb384b97455b9268fd13115c056"></a>

### [`00b5ce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md) → [`00bcc340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00bcc398",
      "incomplete_value": true,
      "site": "00bcc398",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce98",
      "incomplete_value": true,
      "site": "00b5ce98",
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
            "const:4d0:8"
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
      "definition_site": "00bcc374",
      "incomplete_value": true,
      "site": "00bcc380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce74",
      "incomplete_value": true,
      "site": "00b5ce80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
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
      "00bcc354",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc374",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc398",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc354",
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc374",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc398",
      "WRITE",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ce80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md#insn-00b5ce80) · [`00b5ce98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md#insn-00b5ce98) · [`00b5ce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md#insn-00b5ce50)
- 新版 [`00bcc380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md#insn-00bcc380) · [`00bcc398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md#insn-00bcc398) · [`00bcc350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc340.md#insn-00bcc350)

~~~diff
- 00b5ce80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ce80 ["INT_ADD", "register:40f0:8", ["const:b5ce80:8", "const:4:8"]]
- 00b5ce80 ["CALLIND", null, ["register:0:8"]]
+ 00bcc380 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc380 ["INT_ADD", "register:40f0:8", ["const:bcc380:8", "const:4:8"]]
+ 00bcc380 ["CALLIND", null, ["register:0:8"]]
- 00b5ce80 bytes 00013fd6
+ 00bcc380 bytes 00013fd6
- 00b5ce98 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5ce98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d0:8"]]
- 00b5ce98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bcc398 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bcc398 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3d8:8"]]
+ 00bcc398 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5ce98 bytes a0421339
+ 00bcc398 bytes a0620f39
- 00b5ce50 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bcc350 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b5ce50 bytes 352a00b0
+ 00bcc350 bytes d52a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af1b57bddb23032aa3d5c20e10d9898"></a>

### [`00b5ceac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md) → [`00bcc3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcc408",
      "incomplete_value": true,
      "site": "00bcc408",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf08",
      "incomplete_value": true,
      "site": "00b5cf08",
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
            "const:4c8:8"
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
      "site": "00bcc3e8"
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
      "00bcc3c0",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3cc",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b5cee8",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc3c0",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc3cc",
      "READ",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bcc3e8",
      "WRITE",
      [
        "storage",
        "011263d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md#insn-00b5cec4) · [`00b5cee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md#insn-00b5cee8) · [`00b5cf04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md#insn-00b5cf04)
- 新版 [`00bcc3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md#insn-00bcc3c4) · [`00bcc404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md#insn-00bcc404)

~~~diff
- 00b5cec4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5cec4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcc3c4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bcc3c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5cec4 bytes 410200b4
+ 00bcc3c4 bytes 410200b4
- 00b5cee8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5cee8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5cee8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d0:8"]]
- 00b5cee8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5cee8 bytes bf421339
- 00b5cf04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cf04 ["INT_ADD", "register:40f0:8", ["const:b5cf04:8", "const:4:8"]]
- 00b5cf04 ["CALLIND", null, ["register:0:8"]]
+ 00bcc404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc404 ["INT_ADD", "register:40f0:8", ["const:bcc404:8", "const:4:8"]]
+ 00bcc404 ["CALLIND", null, ["register:0:8"]]
- 00b5cf04 bytes 00013fd6
+ 00bcc404 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f7201f043af597b87cde5fdf28b2cd"></a>

### [`00b5cf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf1c.md) → [`00bcc41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc45c",
      "incomplete_value": true,
      "site": "00bcc45c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf5c",
      "incomplete_value": true,
      "site": "00b5cf5c",
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
            "const:4c8:8"
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
      "definition_site": "00bcc438",
      "incomplete_value": true,
      "site": "00bcc438",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cf38",
      "incomplete_value": true,
      "site": "00b5cf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc440",
      "incomplete_value": false,
      "site": "00bcc454",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cf40",
      "incomplete_value": false,
      "site": "00b5cf54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
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
      "00bcc430",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc440",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00bcc45c",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc430",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc440",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc45c",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf1c.md#insn-00b5cf54) · [`00b5cf5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf1c.md#insn-00b5cf5c) · [`00b5cf28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf1c.md#insn-00b5cf28)
- 新版 [`00bcc454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc454) · [`00bcc45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc45c) · [`00bcc428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc41c.md#insn-00bcc428)

~~~diff
- 00b5cf54 ["INT_ADD", "register:40f0:8", ["const:b5cf54:8", "const:4:8"]]
- 00b5cf54 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc454 ["INT_ADD", "register:40f0:8", ["const:bcc454:8", "const:4:8"]]
+ 00bcc454 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5cf54 bytes 4f040294
+ 00bcc454 bytes af390294
- 00b5cf5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00b5cf5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc45c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
+ 00bcc45c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cf5c bytes 806602f9
+ 00bcc45c bytes 80ea01f9
- 00b5cf28 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bcc428 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b5cf28 bytes 342a00b0
+ 00bcc428 bytes d42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a74c9ae41bef91bc97718b95f488ba20"></a>

### [`00b5cf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf8c.md) → [`00bcc48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc4a8",
      "incomplete_value": false,
      "site": "00bcc4ac",
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
      "definition_site": "00b5cfa8",
      "incomplete_value": false,
      "site": "00b5cfac",
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
      "definition_site": "00bcc4b8",
      "incomplete_value": true,
      "site": "00bcc4c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5cfb8",
      "incomplete_value": true,
      "site": "00b5cfc4",
      "value": [
        "LOAD",
        "8",
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
      "00bcc4a8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bcc4b8",
      "DATA",
      [
        "storage",
        "010a14d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc4a8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bcc4b8",
      "DATA",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cfac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf8c.md#insn-00b5cfac) · [`00b5cfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf8c.md#insn-00b5cfa4) · [`00b5cfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf8c.md#insn-00b5cfa8)
- 新版 [`00bcc4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4ac) · [`00bcc4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4a4) · [`00bcc4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc48c.md#insn-00bcc4a8)

~~~diff
- 00b5cfac ["INT_ADD", "register:40f0:8", ["const:b5cfac:8", "const:4:8"]]
- 00b5cfac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcc4ac ["INT_ADD", "register:40f0:8", ["const:bcc4ac:8", "const:4:8"]]
+ 00bcc4ac ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5cfac bytes 75040294
+ 00bcc4ac bytes d5390294
- 00b5cfa4 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bcc4a4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b5cfa4 bytes e0b9ff90
+ 00bcc4a4 bytes e0b6ff90
- 00b5cfa8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5cfa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cfa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cfa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc4a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bcc4a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc4a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc4a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cfa8 bytes 001c1591
+ 00bcc4a8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-952f65d01e48a0775d31a2b8f6bd78f4"></a>

### [`00b5cfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cfc8.md) → [`00bcc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc508",
      "incomplete_value": true,
      "site": "00bcc508",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d008",
      "incomplete_value": true,
      "site": "00b5d008",
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
            "const:4c8:8"
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
      "definition_site": "00bcc4e4",
      "incomplete_value": true,
      "site": "00bcc4e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5cfe4",
      "incomplete_value": true,
      "site": "00b5cfe4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc4ec",
      "incomplete_value": false,
      "site": "00bcc500",
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
            "const:bf5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfec",
      "incomplete_value": false,
      "site": "00b5d000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
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
      "00bcc4dc",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc4ec",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00bcc508",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc4dc",
      "READ",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc4ec",
      "PARAM",
      [
        "storage",
        "002a2bf5",
        null,
        "string"
      ]
    ],
    [
      "00bcc508",
      "WRITE",
      [
        "storage",
        "011263d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cfc8.md#insn-00b5d000) · [`00b5d008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cfc8.md#insn-00b5d008) · [`00b5cfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cfc8.md#insn-00b5cfd4)
- 新版 [`00bcc500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc500) · [`00bcc508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc508) · [`00bcc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc4c8.md#insn-00bcc4d4)

~~~diff
- 00b5d000 ["INT_ADD", "register:40f0:8", ["const:b5d000:8", "const:4:8"]]
- 00b5d000 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc500 ["INT_ADD", "register:40f0:8", ["const:bcc500:8", "const:4:8"]]
+ 00bcc500 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d000 bytes 24040294
+ 00bcc500 bytes 84390294
- 00b5d008 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00b5d008 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d0:8"]]
+ 00bcc508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d008 bytes 806602f9
+ 00bcc508 bytes 80ea01f9
- 00b5cfd4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bcc4d4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b5cfd4 bytes 342a00b0
+ 00bcc4d4 bytes d42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0ac88363a731e706567b38025eabda"></a>

### [`00b5d074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d074.md) → [`00bcc574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc5a0",
      "incomplete_value": true,
      "site": "00bcc5a0",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d0a0",
      "incomplete_value": true,
      "site": "00b5d0a0",
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
            "const:4e8:8"
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
      "definition_site": "00bcc588",
      "incomplete_value": true,
      "site": "00bcc588",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d088",
      "incomplete_value": true,
      "site": "00b5d088",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc594",
      "incomplete_value": false,
      "site": "00bcc598",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d094",
      "incomplete_value": false,
      "site": "00b5d098",
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
            "const:16c:8"
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
      "00bcc584",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc594",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00bcc5a0",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc584",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc594",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      "00bcc5a0",
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d074.md#insn-00b5d098) · [`00b5d0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d074.md#insn-00b5d0a0) · [`00b5d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d074.md#insn-00b5d080)
- 新版 [`00bcc598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc598) · [`00bcc5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc5a0) · [`00bcc580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc574.md#insn-00bcc580)

~~~diff
- 00b5d098 ["INT_ADD", "register:40f0:8", ["const:b5d098:8", "const:4:8"]]
- 00b5d098 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc598 ["INT_ADD", "register:40f0:8", ["const:bcc598:8", "const:4:8"]]
+ 00bcc598 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d098 bytes fe030294
+ 00bcc598 bytes 5e390294
- 00b5d0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00b5d0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcc5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d0a0 bytes 607602f9
+ 00bcc5a0 bytes 60fa01f9
- 00b5d080 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc580 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5d080 bytes 332a0090
+ 00bcc580 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b81cfb90afd9f28237486dda330463c"></a>

### [`00b5d0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0f4.md) → [`00bcc5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc624",
      "incomplete_value": true,
      "site": "00bcc624",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d124",
      "incomplete_value": true,
      "site": "00b5d124",
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
            "const:4e8:8"
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
      "definition_site": "00bcc608",
      "incomplete_value": true,
      "site": "00bcc608",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d108",
      "incomplete_value": true,
      "site": "00b5d108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc614",
      "incomplete_value": false,
      "site": "00bcc61c",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d114",
      "incomplete_value": false,
      "site": "00b5d11c",
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
            "const:16c:8"
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
      "00bcc604",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc614",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00bcc624",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc604",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc614",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      "00bcc624",
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0f4.md#insn-00b5d11c) · [`00b5d124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0f4.md#insn-00b5d124) · [`00b5d100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0f4.md#insn-00b5d100)
- 新版 [`00bcc61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc61c) · [`00bcc624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc624) · [`00bcc600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5f4.md#insn-00bcc600)

~~~diff
- 00b5d11c ["INT_ADD", "register:40f0:8", ["const:b5d11c:8", "const:4:8"]]
- 00b5d11c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc61c ["INT_ADD", "register:40f0:8", ["const:bcc61c:8", "const:4:8"]]
+ 00bcc61c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d11c bytes dd030294
+ 00bcc61c bytes 3d390294
- 00b5d124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00b5d124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcc624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d124 bytes 607602f9
+ 00bcc624 bytes 60fa01f9
- 00b5d100 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc600 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5d100 bytes 332a0090
+ 00bcc600 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15fdc3ab0244105a61c6bfc18fdd0d5"></a>

### [`00b5d138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d138.md) → [`00bcc638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc668",
      "incomplete_value": true,
      "site": "00bcc668",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d168",
      "incomplete_value": true,
      "site": "00b5d168",
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
            "const:4e8:8"
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
      "definition_site": "00bcc64c",
      "incomplete_value": true,
      "site": "00bcc64c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d14c",
      "incomplete_value": true,
      "site": "00b5d14c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc654",
      "incomplete_value": false,
      "site": "00bcc660",
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
            "const:b9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d154",
      "incomplete_value": false,
      "site": "00b5d160",
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
            "const:16c:8"
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
      "00bcc648",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc654",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00bcc668",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc648",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc654",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ],
    [
      "00bcc668",
      "WRITE",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d138.md#insn-00b5d160) · [`00b5d168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d138.md#insn-00b5d168) · [`00b5d144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d138.md#insn-00b5d144)
- 新版 [`00bcc660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc660) · [`00bcc668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc668) · [`00bcc644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc638.md#insn-00bcc644)

~~~diff
- 00b5d160 ["INT_ADD", "register:40f0:8", ["const:b5d160:8", "const:4:8"]]
- 00b5d160 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc660 ["INT_ADD", "register:40f0:8", ["const:bcc660:8", "const:4:8"]]
+ 00bcc660 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d160 bytes cc030294
+ 00bcc660 bytes 2c390294
- 00b5d168 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00b5d168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc668 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00bcc668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d168 bytes 607602f9
+ 00bcc668 bytes 60fa01f9
- 00b5d144 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc644 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5d144 bytes 332a0090
+ 00bcc644 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d5ee18de9ce432e624bad686402e76"></a>

### [`00b5d188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d188.md) → [`00bcc688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d18c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d18c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d188",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d18c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d190",
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
      "00bcc688",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcc68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc690",
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

- 旧版 [`00b5d188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d188.md#insn-00b5d188) · [`00b5d18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d188.md#insn-00b5d18c) · [`00b5d190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d188.md#insn-00b5d190)

~~~diff
- 00b5d188 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5d188 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5d188 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d188 bytes f50f1df8
- 00b5d18c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d18c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d18c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d18c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d18c bytes f44f01a9
- 00b5d190 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d190 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d190 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5d190 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d190 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7dd6c0fc69dba310a92925d78a4b7ed"></a>

### [`00b5d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d1f4.md) → [`00bcc6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc6f4.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

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
      "site": "00b5d230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc730"
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
      "00bcc708",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc70c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d254"
      ]
    ],
    [
      "00bcc714",
      "READ",
      [
        "storage",
        "010a14f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcc708",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc70c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc754"
      ]
    ],
    [
      "00bcc714",
      "READ",
      [
        "storage",
        "011263f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d1f4.md#insn-00b5d230) · [`00b5d238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d1f4.md#insn-00b5d238) · [`00b5d24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d1f4.md#insn-00b5d24c)

~~~diff
- 00b5d230 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d230 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d230 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4f0:8"]]
- 00b5d230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d230 bytes bfc21339
- 00b5d238 ["INT_ADD", "register:40f0:8", ["const:b5d238:8", "const:4:8"]]
- 00b5d238 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b5d238 bytes aa030294
- 00b5d24c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d24c ["INT_ADD", "register:40f0:8", ["const:b5d24c:8", "const:4:8"]]
- 00b5d24c ["CALLIND", null, ["register:0:8"]]
- 00b5d24c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acf09d3a5c942926114a5ebf45de1da3"></a>

### [`00b5d264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d264.md) → [`00bcc764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b5d2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc7a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d280"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d278",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc7a8"
      ]
    ],
    [
      "unmatched:00b5d288",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc778",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc7a8"
      ]
    ],
    [
      "00bcc788",
      "PARAM",
      [
        "storage",
        "002b5b9a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d264.md#insn-00b5d280) · [`00b5d29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d264.md#insn-00b5d29c) · [`00b5d2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d264.md#insn-00b5d2a4)
- 新版 [`00bcc79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md#insn-00bcc79c)

~~~diff
- 00b5d280 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d280 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d280 bytes 410100b5
- 00b5d29c ["INT_ADD", "register:40f0:8", ["const:b5d29c:8", "const:4:8"]]
- 00b5d29c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc79c ["INT_ADD", "register:40f0:8", ["const:bcc79c:8", "const:4:8"]]
+ 00bcc79c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d29c bytes 7d030294
+ 00bcc79c bytes dd380294
- 00b5d2a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00b5d2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d2a4 bytes 807602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a94b2fb78c87fe9ba13ab84f9f56654"></a>

### [`00b5d2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d2d4.md) → [`00bcc7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc7f0",
      "incomplete_value": false,
      "site": "00bcc7f4",
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
      "definition_site": "00b5d2f0",
      "incomplete_value": false,
      "site": "00b5d2f4",
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
      "definition_site": "00bcc800",
      "incomplete_value": true,
      "site": "00bcc80c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d300",
      "incomplete_value": true,
      "site": "00b5d30c",
      "value": [
        "LOAD",
        "8",
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
      "00bcc7f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bcc800",
      "DATA",
      [
        "storage",
        "010a14f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc7f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bcc800",
      "DATA",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d2d4.md#insn-00b5d2f4) · [`00b5d2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d2d4.md#insn-00b5d2ec) · [`00b5d2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d2d4.md#insn-00b5d2f0)
- 新版 [`00bcc7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md#insn-00bcc7f4) · [`00bcc7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md#insn-00bcc7ec) · [`00bcc7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md#insn-00bcc7f0)

~~~diff
- 00b5d2f4 ["INT_ADD", "register:40f0:8", ["const:b5d2f4:8", "const:4:8"]]
- 00b5d2f4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcc7f4 ["INT_ADD", "register:40f0:8", ["const:bcc7f4:8", "const:4:8"]]
+ 00bcc7f4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5d2f4 bytes a3030294
+ 00bcc7f4 bytes 03390294
- 00b5d2ec ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bcc7ec ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b5d2ec bytes c0b9fff0
+ 00bcc7ec bytes e0b6ff90
- 00b5d2f0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5d2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc7f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bcc7f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc7f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc7f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d2f0 bytes 001c1591
+ 00bcc7f0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ae080336c2fa2f271f518d0a58e3a9"></a>

### [`00b5d310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d310.md) → [`00bcc810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc810.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b5d310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d310",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d314",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d324",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc814",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc824",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d310.md#insn-00b5d310) · [`00b5d314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d310.md#insn-00b5d314) · [`00b5d32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d310.md#insn-00b5d32c)

~~~diff
- 00b5d310 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d310 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d310 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5d310 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d310 bytes f44fbea9
- 00b5d314 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d314 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d314 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d314 bytes fd7b01a9
- 00b5d32c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d32c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5d32c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bbced76ef545f4597613fa03b155c8e"></a>

### [`00b5d380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d380.md) → [`00bcc880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc89c",
      "incomplete_value": false,
      "site": "00bcc8a0",
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
      "definition_site": "00b5d39c",
      "incomplete_value": false,
      "site": "00b5d3a0",
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
      "definition_site": "00bcc8ac",
      "incomplete_value": true,
      "site": "00bcc8b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d3ac",
      "incomplete_value": true,
      "site": "00b5d3b8",
      "value": [
        "LOAD",
        "8",
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
      "00bcc89c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bcc8ac",
      "DATA",
      [
        "storage",
        "010a1508",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcc89c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bcc8ac",
      "DATA",
      [
        "storage",
        "01126410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d380.md#insn-00b5d3a0) · [`00b5d398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d380.md#insn-00b5d398) · [`00b5d39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d380.md#insn-00b5d39c)
- 新版 [`00bcc8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc8a0) · [`00bcc898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc898) · [`00bcc89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md#insn-00bcc89c)

~~~diff
- 00b5d3a0 ["INT_ADD", "register:40f0:8", ["const:b5d3a0:8", "const:4:8"]]
- 00b5d3a0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcc8a0 ["INT_ADD", "register:40f0:8", ["const:bcc8a0:8", "const:4:8"]]
+ 00bcc8a0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5d3a0 bytes 78030294
+ 00bcc8a0 bytes d8380294
- 00b5d398 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bcc898 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b5d398 bytes e0b9ff90
+ 00bcc898 bytes e0b6ffb0
- 00b5d39c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b5d39c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d39c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d39c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcc89c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bcc89c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc89c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcc89c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d39c bytes 00c81791
+ 00bcc89c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-466aa54fd6bf3e068fd21efd849de657"></a>

### [`00b5d3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md) → [`00bcc8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b5d3e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc8e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc8d0",
      "incomplete_value": true,
      "site": "00bcc8d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d3d0",
      "incomplete_value": true,
      "site": "00b5d3d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bcc8cc",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc8d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d3ec"
      ]
    ],
    [
      "unmatched:00b5d3dc",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc8cc",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc8d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc8ec"
      ]
    ],
    [
      "00bcc8dc",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md#insn-00b5d3d0) · [`00b5d3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md#insn-00b5d3e0) · [`00b5d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md#insn-00b5d3e8)
- 新版 [`00bcc8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md#insn-00bcc8d0)

~~~diff
- 00b5d3d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5d3d0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bcc8d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcc8d0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d3d0 bytes e80000b5
+ 00bcc8d0 bytes e80000b5
- 00b5d3e0 ["INT_ADD", "register:40f0:8", ["const:b5d3e0:8", "const:4:8"]]
- 00b5d3e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d3e0 bytes 2c030294
- 00b5d3e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
- 00b5d3e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d3e8 bytes 608a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c2f79da9a244c7ed6adcd41a08d87bb"></a>

### [`00b5d43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d43c.md) → [`00bcc93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bcc96c",
      "incomplete_value": true,
      "site": "00bcc96c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d46c",
      "incomplete_value": true,
      "site": "00b5d46c",
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
            "const:510:8"
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
      "definition_site": "00bcc950",
      "incomplete_value": true,
      "site": "00bcc950",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d450",
      "incomplete_value": true,
      "site": "00b5d450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bcc95c",
      "incomplete_value": false,
      "site": "00bcc964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:8bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d45c",
      "incomplete_value": false,
      "site": "00b5d464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:8dc:8"
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
      "00bcc94c",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc95c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00bcc96c",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc94c",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc95c",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ],
    [
      "00bcc96c",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d43c.md#insn-00b5d464) · [`00b5d46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d43c.md#insn-00b5d46c) · [`00b5d448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d43c.md#insn-00b5d448)
- 新版 [`00bcc964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc964) · [`00bcc96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc96c) · [`00bcc948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc93c.md#insn-00bcc948)

~~~diff
- 00b5d464 ["INT_ADD", "register:40f0:8", ["const:b5d464:8", "const:4:8"]]
- 00b5d464 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc964 ["INT_ADD", "register:40f0:8", ["const:bcc964:8", "const:4:8"]]
+ 00bcc964 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d464 bytes 0b030294
+ 00bcc964 bytes 6b380294
- 00b5d46c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
- 00b5d46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bcc96c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bcc96c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d46c bytes 608a02f9
+ 00bcc96c bytes 600e02f9
- 00b5d448 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bcc948 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b5d448 bytes 332a0090
+ 00bcc948 bytes d32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce3b84c1f118f5d5a67c678585c0a368"></a>

### [`00b5d480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d480.md) → [`00bcc980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b5d4b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcc9b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bcc994",
      "incomplete_value": true,
      "site": "00bcc994",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b5d494",
      "incomplete_value": true,
      "site": "00b5d494",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bcc990",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d4b4"
      ]
    ],
    [
      "unmatched:00b5d49c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcc990",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcc994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc9b4"
      ]
    ],
    [
      "00bcc99c",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d480.md#insn-00b5d4a8) · [`00b5d4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d480.md#insn-00b5d4b0) · [`00b5d4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d480.md#insn-00b5d4c0)
- 新版 [`00bcc9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc980.md#insn-00bcc9a8)

~~~diff
- 00b5d4a8 ["INT_ADD", "register:40f0:8", ["const:b5d4a8:8", "const:4:8"]]
- 00b5d4a8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bcc9a8 ["INT_ADD", "register:40f0:8", ["const:bcc9a8:8", "const:4:8"]]
+ 00bcc9a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d4a8 bytes fa020294
+ 00bcc9a8 bytes 5a380294
- 00b5d4b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
- 00b5d4b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d4b0 bytes 608a02f9
- 00b5d4c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5d4c0 ["RETURN", null, ["register:0:8"]]
- 00b5d4c0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1452eade6f8ffcb55294e617160ef6f4"></a>

### [`00b5d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d4d0.md) → [`00bcc9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc9d0.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d4d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d4d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d4d8",
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
      "00bcc9d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcc9d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc9d8",
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

- 旧版 [`00b5d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d4d0.md#insn-00b5d4d0) · [`00b5d4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d4d0.md#insn-00b5d4d4) · [`00b5d4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d4d0.md#insn-00b5d4d8)

~~~diff
- 00b5d4d0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5d4d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5d4d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d4d0 bytes f50f1df8
- 00b5d4d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d4d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d4d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d4d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d4d4 bytes f44f01a9
- 00b5d4d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d4d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d4d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5d4d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d4d8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328442f7b77a52e8f33bafc81606a261"></a>

### [`00b5d53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md) → [`00bcca3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcca3c.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d53c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d540"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d53c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d540",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d544",
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
      "00bcca3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcca40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcca44",
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

- 旧版 [`00b5d53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md#insn-00b5d53c) · [`00b5d540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md#insn-00b5d540) · [`00b5d544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md#insn-00b5d544)

~~~diff
- 00b5d53c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5d53c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5d53c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d53c bytes f50f1df8
- 00b5d540 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d540 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d540 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d540 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d540 bytes f44f01a9
- 00b5d544 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d544 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d544 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5d544 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d544 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ffc83cd070217d39c05442e1ade0dc"></a>

### [`00b5d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md) → [`00bccaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b5d5ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccaec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d5c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d5c0",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d5c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccaf0"
      ]
    ],
    [
      "unmatched:00b5d5d0",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccac0",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccac8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccaf0"
      ]
    ],
    [
      "00bccad0",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md#insn-00b5d5c8) · [`00b5d5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md#insn-00b5d5e4) · [`00b5d5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md#insn-00b5d5ec)
- 新版 [`00bccae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccaac.md#insn-00bccae4)

~~~diff
- 00b5d5c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d5c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5d5c8 bytes 410100b5
- 00b5d5e4 ["INT_ADD", "register:40f0:8", ["const:b5d5e4:8", "const:4:8"]]
- 00b5d5e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bccae4 ["INT_ADD", "register:40f0:8", ["const:bccae4:8", "const:4:8"]]
+ 00bccae4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d5e4 bytes ab020294
+ 00bccae4 bytes 0b380294
- 00b5d5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
- 00b5d5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d5ec bytes 808a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3b7ae26a7f282298e9878b0f5ff9d70"></a>

### [`00b5d61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md) → [`00bccb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bccb38",
      "incomplete_value": false,
      "site": "00bccb3c",
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
      "definition_site": "00b5d638",
      "incomplete_value": false,
      "site": "00b5d63c",
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
      "definition_site": "00bccb48",
      "incomplete_value": true,
      "site": "00bccb54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d648",
      "incomplete_value": true,
      "site": "00b5d654",
      "value": [
        "LOAD",
        "8",
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
      "00bccb38",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bccb48",
      "DATA",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bccb38",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bccb48",
      "DATA",
      [
        "storage",
        "01126428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md#insn-00b5d63c) · [`00b5d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md#insn-00b5d634) · [`00b5d638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md#insn-00b5d638)
- 新版 [`00bccb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md#insn-00bccb3c) · [`00bccb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md#insn-00bccb34) · [`00bccb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md#insn-00bccb38)

~~~diff
- 00b5d63c ["INT_ADD", "register:40f0:8", ["const:b5d63c:8", "const:4:8"]]
- 00b5d63c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bccb3c ["INT_ADD", "register:40f0:8", ["const:bccb3c:8", "const:4:8"]]
+ 00bccb3c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5d63c bytes d1020294
+ 00bccb3c bytes 31380294
- 00b5d634 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bccb34 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b5d634 bytes c0b9fff0
+ 00bccb34 bytes e0b6ff90
- 00b5d638 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b5d638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bccb38 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bccb38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bccb38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bccb38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d638 bytes 001c1591
+ 00bccb38 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2354596f7d00a83de7dd74a0afa6e2"></a>

### [`00b5d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d658.md) → [`00bccb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b5d698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccb98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d674"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d66c",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccb9c"
      ]
    ],
    [
      "unmatched:00b5d67c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccb6c",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccb74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccb9c"
      ]
    ],
    [
      "00bccb7c",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d658.md#insn-00b5d674) · [`00b5d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d658.md#insn-00b5d690) · [`00b5d698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d658.md#insn-00b5d698)
- 新版 [`00bccb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb58.md#insn-00bccb90)

~~~diff
- 00b5d674 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d674 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d674 bytes 410100b5
- 00b5d690 ["INT_ADD", "register:40f0:8", ["const:b5d690:8", "const:4:8"]]
- 00b5d690 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bccb90 ["INT_ADD", "register:40f0:8", ["const:bccb90:8", "const:4:8"]]
+ 00bccb90 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d690 bytes 80020294
+ 00bccb90 bytes e0370294
- 00b5d698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
- 00b5d698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d698 bytes 808a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70fc01c6c949d5766abe84a18a0e7bdf"></a>

### [`00b5d704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d704.md) → [`00bccc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccc04.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c40.md) · 呼出先 3件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d840.md) · 呼出先 3件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 2.94% / 新版 3.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d7a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d720",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5d72c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d754"
      ]
    ],
    [
      "unmatched:00b5d734",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccc20",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccc2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccc54"
      ]
    ],
    [
      "00bccc34",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d704.md#insn-00b5d72c) · [`00b5d748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d704.md#insn-00b5d748) · [`00b5d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d704.md#insn-00b5d750)

~~~diff
- 00b5d72c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5d72c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5d72c bytes 410100b5
- 00b5d748 ["INT_ADD", "register:40f0:8", ["const:b5d748:8", "const:4:8"]]
- 00b5d748 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b5d748 bytes 52020294
- 00b5d750 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:420:8"]]
- 00b5d750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d750 bytes c01202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c30bb3b2e2c4450a9f62245d91c80cba"></a>

### [`00b5d934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d934.md) → [`00bcce34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcce34.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c60.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d860.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 15.29% / 新版 15.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d9bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcce48",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcce50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d994"
      ]
    ],
    [
      "unmatched:00b5d958",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bcce48",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcce50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcce94"
      ]
    ],
    [
      "00bcce58",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d934.md#insn-00b5d95c) · [`00b5d96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d934.md#insn-00b5d96c) · [`00b5d970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d934.md#insn-00b5d970)

~~~diff
- 00b5d95c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b5d95c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5d95c bytes c8000034
- 00b5d96c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d96c ["INT_ADD", "register:40f0:8", ["const:b5d96c:8", "const:4:8"]]
- 00b5d96c ["CALLIND", null, ["register:0:8"]]
- 00b5d96c bytes 00013fd6
- 00b5d970 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d970 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d970 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:428:8"]]
- 00b5d970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d970 bytes bfa21039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0855608f613bb2401c87de6d1829a21"></a>

### [`00b5da88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5da88.md) → [`00bccf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccfa0",
      "incomplete_value": true,
      "site": "00bccfa4",
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
            "register:4000:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bccfc0",
      "incomplete_value": true,
      "site": "00bccfc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:340:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dac0",
      "incomplete_value": true,
      "site": "00b5dac8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd000",
      "incomplete_value": false,
      "site": "00bcd008",
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
            "const:c49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5db00",
      "incomplete_value": false,
      "site": "00b5db08",
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
            "const:fa7:8"
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
      "00bccfc0",
      "READ",
      [
        "storage",
        "010a1438",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5db00",
      "PARAM",
      [
        "storage",
        "002a7fa7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccfc0",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd000",
      "PARAM",
      [
        "storage",
        "002b8c49",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5daa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5da88.md#insn-00b5daa4) · [`00b5dac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5da88.md#insn-00b5dac8) · [`00b5db08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5da88.md#insn-00b5db08)
- 新版 [`00bccfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bccfa4) · [`00bccfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bccfc8) · [`00bcd008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccf88.md#insn-00bcd008)

~~~diff
- 00b5daa4 ["INT_ADD", "register:40f0:8", ["const:b5daa4:8", "const:4:8"]]
- 00b5daa4 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bccfa4 ["INT_ADD", "register:40f0:8", ["const:bccfa4:8", "const:4:8"]]
+ 00bccfa4 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5daa4 bytes d7010294
+ 00bccfa4 bytes 37370294
- 00b5dac8 ["INT_ADD", "register:40f0:8", ["const:b5dac8:8", "const:4:8"]]
- 00b5dac8 ["CALL", null, ["callee:004977f4:8"]]
+ 00bccfc8 ["INT_ADD", "register:40f0:8", ["const:bccfc8:8", "const:4:8"]]
+ 00bccfc8 ["CALL", null, ["callee:004977f4:8"]]
- 00b5dac8 bytes a55be497
+ 00bccfc8 bytes 0b2ae397
- 00b5db08 ["INT_ADD", "register:40f0:8", ["const:b5db08:8", "const:4:8"]]
- 00b5db08 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bcd008 ["INT_ADD", "register:40f0:8", ["const:bcd008:8", "const:4:8"]]
+ 00bcd008 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b5db08 bytes ea010294
+ 00bcd008 bytes 4a370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c14af6a271d7bc7c81e3e3efac1d0fa1"></a>

### [`00b5db44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5db44.md) → [`00bcd044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5db78"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd084",
      "incomplete_value": true,
      "site": "00bcd098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5db84",
      "incomplete_value": true,
      "site": "00b5db98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcd078"
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
      "unmatched:00b5db84",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5db78",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcd084",
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd078",
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

- 旧版 [`00b5db78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5db44.md#insn-00b5db78) · [`00b5db98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5db44.md#insn-00b5db98)
- 新版 [`00bcd098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md#insn-00bcd098) · [`00bcd078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd044.md#insn-00bcd078)

~~~diff
- 00b5db78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5db78 ["INT_ADD", "register:40f0:8", ["const:b5db78:8", "const:4:8"]]
- 00b5db78 ["CALLIND", null, ["register:0:8"]]
- 00b5db78 bytes 00013fd6
- 00b5db98 ["INT_ADD", "register:40f0:8", ["const:b5db98:8", "const:4:8"]]
- 00b5db98 ["CALL", null, ["callee:00574cac:8"]]
+ 00bcd098 ["INT_ADD", "register:40f0:8", ["const:bcd098:8", "const:4:8"]]
+ 00bcd098 ["CALL", null, ["callee:00574cac:8"]]
- 00b5db98 bytes 9fd0e797
+ 00bcd098 bytes 059fe697
+ 00bcd078 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcd078 ["INT_ADD", "register:40f0:8", ["const:bcd078:8", "const:4:8"]]
+ 00bcd078 ["CALLIND", null, ["register:0:8"]]
+ 00bcd078 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfaa93514dec713f07b8722d2bbfffe0"></a>

### [`00b5dbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dbc4.md) → [`00bcd0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd0c4.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c20.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb210.md) [`00bdca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca50.md)
- 新版 呼出元 1件 [`00c5d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) [`00c594a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c594a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dbcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5dbc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5dbcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5dbd0",
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
      "00bcd0c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcd0cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcd0d0",
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

- 旧版 [`00b5dbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dbc4.md#insn-00b5dbc8) · [`00b5dbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dbc4.md#insn-00b5dbcc) · [`00b5dbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dbc4.md#insn-00b5dbd0)

~~~diff
- 00b5dbc8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5dbc8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5dbc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5dbc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dbc8 bytes f65702a9
- 00b5dbcc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5dbcc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5dbcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5dbcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dbcc bytes f44f03a9
- 00b5dbd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5dbd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5dbd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5dbd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5dbd0 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0d7a97eccf16f7615f835dc8352455a"></a>

### [`00b5dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dd2c.md) → [`00bcd22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd22c.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be09d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09d0.md) · 呼出先 21件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md)
- 新版 呼出元 1件 [`00c5d5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5d0.md) · 呼出先 21件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.92% / 新版 86.92%

CFGの説明率　旧版 51.61% / 新版 51.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dd50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5dd70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5de04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5dd50",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bcd25c",
      "READ",
      [
        "storage",
        "010a1538",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00b5dd70",
      "WRITE",
      [
        "storage",
        "010a1538",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bcd250",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bcd25c",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined4"
      ]
    ],
    [
      "00bcd270",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dd2c.md#insn-00b5dd50) · [`00b5dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dd2c.md#insn-00b5dd70) · [`00b5dd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dd2c.md#insn-00b5dd74)

~~~diff
- 00b5dd50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b5dd50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5dd50 bytes e81f00f9
- 00b5dd70 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:538:8"]]
- 00b5dd70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b5dd70 bytes e83a05b9
- 00b5dd74 ["INT_ADD", "register:40f0:8", ["const:b5dd74:8", "const:4:8"]]
- 00b5dd74 ["CALL", null, ["callee:00c5baf0:8"]]
- 00b5dd74 bytes b3040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-202ba64d1e90e33c1e84a1ebe7077d78"></a>

### [`00b5df68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5df68.md) → [`00bcd468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a40.md) · 呼出先 6件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00be0c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c20.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)
- 新版 呼出元 1件 [`00c5d640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d640.md) · 呼出先 6件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d820.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd48c",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5df8c",
      "incomplete_value": true,
      "site": "00b5df9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
              ]
            ]
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
      "definition_site": "00bcd490",
      "incomplete_value": true,
      "site": "00bcd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:400:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5df90",
      "incomplete_value": true,
      "site": "00b5df9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
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
      "definition_site": "00bcd4ac",
      "incomplete_value": true,
      "site": "00bcd4bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dfac",
      "incomplete_value": true,
      "site": "00b5dfbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
              ]
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
      "unmatched:00b5df8c",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5df90",
      "READ",
      [
        "storage",
        "010a14f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5dfac",
      "READ",
      [
        "storage",
        "010a1458",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd48c",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd490",
      "READ",
      [
        "storage",
        "01126400",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd4ac",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5df68.md#insn-00b5df9c) · [`00b5dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5df68.md#insn-00b5dfbc) · [`00b5dfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5df68.md#insn-00b5dfe8)
- 新版 [`00bcd49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd49c) · [`00bcd4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd4bc) · [`00bcd4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd468.md#insn-00bcd4e8)

~~~diff
- 00b5df9c ["INT_ADD", "register:40f0:8", ["const:b5df9c:8", "const:4:8"]]
- 00b5df9c ["CALL", null, ["callee:005896b4:8"]]
+ 00bcd49c ["INT_ADD", "register:40f0:8", ["const:bcd49c:8", "const:4:8"]]
+ 00bcd49c ["CALL", null, ["callee:005896b4:8"]]
- 00b5df9c bytes 2022e897
+ 00bcd49c bytes 86f0e697
- 00b5dfbc ["INT_ADD", "register:40f0:8", ["const:b5dfbc:8", "const:4:8"]]
- 00b5dfbc ["CALL", null, ["callee:00574cac:8"]]
+ 00bcd4bc ["INT_ADD", "register:40f0:8", ["const:bcd4bc:8", "const:4:8"]]
+ 00bcd4bc ["CALL", null, ["callee:00574cac:8"]]
- 00b5dfbc bytes 96cfe797
+ 00bcd4bc bytes fc9de697
- 00b5dfe8 ["INT_ADD", "register:40f0:8", ["const:b5dfe8:8", "const:4:8"]]
- 00b5dfe8 ["CALL", null, ["callee:005896b4:8"]]
+ 00bcd4e8 ["INT_ADD", "register:40f0:8", ["const:bcd4e8:8", "const:4:8"]]
+ 00bcd4e8 ["CALL", null, ["callee:005896b4:8"]]
- 00b5dfe8 bytes 0d22e897
+ 00bcd4e8 bytes 73f0e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e16eb546bcde38d6c3bcf45bea20b4a"></a>

### [`00b5e030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md) → [`00bcd530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a50.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5d650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d650.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 87.36% / 新版 87.36%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bcd638",
      "incomplete_value": true,
      "site": "00bcd638",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e138",
      "incomplete_value": true,
      "site": "00b5e138",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd580",
      "incomplete_value": true,
      "site": "00bcd588",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd578",
      "incomplete_value": true,
      "site": "00bcd588",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b5e07c",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5e098",
      "READ",
      [
        "storage",
        "010a1460",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5e0b4",
      "READ",
      [
        "storage",
        "010a1528",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcd57c",
      "READ",
      [
        "storage",
        "01126408",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd598",
      "READ",
      [
        "storage",
        "01126368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcd5b4",
      "READ",
      [
        "storage",
        "01126430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md#insn-00b5e088) · [`00b5e0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md#insn-00b5e0a8) · [`00b5e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md#insn-00b5e0c0)
- 新版 [`00bcd588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd588) · [`00bcd5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd5a8) · [`00bcd5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd530.md#insn-00bcd5c0)

~~~diff
- 00b5e088 ["INT_ADD", "register:40f0:8", ["const:b5e088:8", "const:4:8"]]
- 00b5e088 ["CALL", null, ["callee:00574cac:8"]]
+ 00bcd588 ["INT_ADD", "register:40f0:8", ["const:bcd588:8", "const:4:8"]]
+ 00bcd588 ["CALL", null, ["callee:00574cac:8"]]
- 00b5e088 bytes 63cfe797
+ 00bcd588 bytes c99de697
- 00b5e0a8 ["INT_ADD", "register:40f0:8", ["const:b5e0a8:8", "const:4:8"]]
- 00b5e0a8 ["CALL", null, ["callee:00574cac:8"]]
+ 00bcd5a8 ["INT_ADD", "register:40f0:8", ["const:bcd5a8:8", "const:4:8"]]
+ 00bcd5a8 ["CALL", null, ["callee:00574cac:8"]]
- 00b5e0a8 bytes 5bcfe797
+ 00bcd5a8 bytes c19de697
- 00b5e0c0 ["INT_ADD", "register:40f0:8", ["const:b5e0c0:8", "const:4:8"]]
- 00b5e0c0 ["CALL", null, ["callee:00574cac:8"]]
+ 00bcd5c0 ["INT_ADD", "register:40f0:8", ["const:bcd5c0:8", "const:4:8"]]
+ 00bcd5c0 ["CALL", null, ["callee:00574cac:8"]]
- 00b5e0c0 bytes 55cfe797
+ 00bcd5c0 bytes bb9de697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8b99cec6a6c831b733c812fac0d24d"></a>

### [`00b5e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e18c.md) → [`00bcd68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd68c.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0990.md) · 呼出先 5件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bdf040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf040.md) [`00be0a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a80.md)
- 新版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d590.md) · 呼出先 5件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baf0.md) [`00c5d680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d680.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

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
      "site": "00b5e18c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e190"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e18c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e190",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e194",
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
      "00bcd68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcd690",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcd694",
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

- 旧版 [`00b5e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e18c.md#insn-00b5e18c) · [`00b5e190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e18c.md#insn-00b5e190) · [`00b5e194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e18c.md#insn-00b5e194)

~~~diff
- 00b5e18c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5e18c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5e18c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5e18c bytes f50f1df8
- 00b5e190 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5e190 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5e190 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5e190 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e190 bytes f44f01a9
- 00b5e194 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5e194 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5e194 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5e194 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e194 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc44dea5085a0c1c249edad7f49f4da3"></a>

### [`00b5e244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e244.md) → [`00bcd744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md) _ZN8firebase4auth41JniIdTokenListener_nativeOnIdTokenChangedEP7_JNIEnvP8_jobjectl

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be09f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09f0.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5f0.md) [`00c5d830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d830.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e244.md#insn-00b5e25c) · [`00b5e268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e244.md#insn-00b5e268) · [`00b5e270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e244.md#insn-00b5e270)
- 新版 [`00bcd75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd75c) · [`00bcd768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd768) · [`00bcd770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd744.md#insn-00bcd770)

~~~diff
- 00b5e25c ["INT_ADD", "register:40f0:8", ["const:b5e25c:8", "const:4:8"]]
- 00b5e25c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcd75c ["INT_ADD", "register:40f0:8", ["const:bcd75c:8", "const:4:8"]]
+ 00bcd75c ["CALL", null, ["callee:00c5a600:8"]]
- 00b5e25c bytes 71fe0194
+ 00bcd75c bytes a9330294
- 00b5e268 ["INT_ADD", "register:40f0:8", ["const:b5e268:8", "const:4:8"]]
- 00b5e268 ["CALL", null, ["callee:00c5a610:8"]]
+ 00bcd768 ["INT_ADD", "register:40f0:8", ["const:bcd768:8", "const:4:8"]]
+ 00bcd768 ["CALL", null, ["callee:00c5a610:8"]]
- 00b5e268 bytes 72fe0194
+ 00bcd768 bytes aa330294
- 00b5e270 ["INT_ADD", "register:40f0:8", ["const:b5e270:8", "const:4:8"]]
- 00b5e270 ["CALL", null, ["callee:00c5d830:8"]]
+ 00bcd770 ["INT_ADD", "register:40f0:8", ["const:bcd770:8", "const:4:8"]]
+ 00bcd770 ["CALL", null, ["callee:00c5d830:8"]]
- 00b5e270 bytes 700a0294
+ 00bcd770 bytes 30400294
~~~


<a id="compare-17596e33acd2dd66a85abe76c6c07c05"></a>

### [`00b5e288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md) → [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b5e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md) [`00b5ff78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5ff78.md) [`00b60104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60104.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcda8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) [`00bcf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md) [`00bcf604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf604.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcd8a8",
      "incomplete_value": false,
      "site": "00bcd8a8",
      "value": [
        "leaf",
        "const:bcda8c:8"
      ]
    },
    "old": {
      "definition_site": "00b5e3a8",
      "incomplete_value": false,
      "site": "00b5e3a8",
      "value": [
        "leaf",
        "const:b5e58c:8"
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcd91c"
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
      "00bcd7d8",
      "READ",
      [
        "storage",
        "00c1bbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcd7d8",
      "PARAM",
      [
        "storage",
        "00b5ff78",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00b5e300",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bcd7d8",
      "READ",
      [
        "storage",
        "00c9b5f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bcd7d8",
      "PARAM",
      [
        "storage",
        "00bcf478",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv",
        null
      ]
    ],
    [
      "00bcd800",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md#insn-00b5e2ec) · [`00b5e300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md#insn-00b5e300) · [`00b5e340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md#insn-00b5e340)
- 新版 [`00bcd7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md#insn-00bcd7ec) · [`00bcd840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md#insn-00bcd840)

~~~diff
- 00b5e2ec ["INT_ADD", "register:40f0:8", ["const:b5e2ec:8", "const:4:8"]]
- 00b5e2ec ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bcd7ec ["INT_ADD", "register:40f0:8", ["const:bcd7ec:8", "const:4:8"]]
+ 00bcd7ec ["CALL", null, ["callee:00c5aa40:8"]]
- 00b5e2ec bytes 35ff0194
+ 00bcd7ec bytes 95340294
- 00b5e300 ["INT_ADD", "register:40f0:8", ["const:b5e300:8", "const:4:8"]]
- 00b5e300 ["CALL", null, ["ram:bddc40:8"]]
- 00b5e300 bytes 50fe0194
- 00b5e340 ["INT_ADD", "register:40f0:8", ["const:b5e340:8", "const:4:8"]]
- 00b5e340 ["CALL", null, ["callee:004977f4:8"]]
+ 00bcd840 ["INT_ADD", "register:40f0:8", ["const:bcd840:8", "const:4:8"]]
+ 00bcd840 ["CALL", null, ["callee:004977f4:8"]]
- 00b5e340 bytes 8759e497
+ 00bcd840 bytes ed27e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a767e1589b4666c7b46dbb7520b360"></a>

### [`00b5e488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e488.md) → [`00bcd988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ce0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bd0.md)
- 新版 呼出元 1件 [`00c5d8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8e0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 15.38% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e528"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcda28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcd9b8",
      "incomplete_value": true,
      "site": "00bcd9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e4b8",
      "incomplete_value": true,
      "site": "00b5e4bc",
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
                "const:70:8"
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
      "unmatched:00b5e504",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b5e528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcda54"
      ]
    ]
  ],
  "added": [
    [
      "00bcda04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bcda28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcda54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e488.md#insn-00b5e4bc) · [`00b5e504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e488.md#insn-00b5e504) · [`00b5e528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e488.md#insn-00b5e528)
- 新版 [`00bcd9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md#insn-00bcd9bc)

~~~diff
- 00b5e4bc ["INT_ADD", "register:40f0:8", ["const:b5e4bc:8", "const:4:8"]]
- 00b5e4bc ["CALL", null, ["callee:00c5d910:8"]]
+ 00bcd9bc ["INT_ADD", "register:40f0:8", ["const:bcd9bc:8", "const:4:8"]]
+ 00bcd9bc ["CALL", null, ["callee:00c5d910:8"]]
- 00b5e4bc bytes 150a0294
+ 00bcd9bc bytes d53f0294
- 00b5e504 ["INT_ADD", "register:40f0:8", ["const:b5e504:8", "const:4:8"]]
- 00b5e504 ["CALL", null, ["ram:bddc40:8"]]
- 00b5e504 bytes cffd0194
- 00b5e528 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e528 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b5e528 bytes 61010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90181b5ee744e92b5eb295a0e2a5f8c"></a>

### [`00b5e58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md) → [`00bcda8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) FUN_00bcda8c

採用 · 移動量 `+0x6f500` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5e288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e288.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.45% / 新版 80.45%

CFGの説明率　旧版 26.39% / 新版 40.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e594"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e590",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e594",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e598",
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
      "00bcda90",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bcda94",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcda98",
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

- 旧版 [`00b5e590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md#insn-00b5e590) · [`00b5e594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md#insn-00b5e594) · [`00b5e598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md#insn-00b5e598)

~~~diff
- 00b5e590 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b5e590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b5e590 bytes fb1300f9
- 00b5e594 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5e594 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5e594 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5e594 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e594 bytes fa6703a9
- 00b5e598 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5e598 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5e598 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5e598 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e598 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a272a24c55d312982ee81c219dc5d4e"></a>

### [`00b5e7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md) → [`00bcdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.49% / 新版 74.49%

CFGの説明率　旧版 11.76% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e7a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e7a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e7ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcdca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bcdca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bcdcac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md#insn-00b5e7a4) · [`00b5e7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md#insn-00b5e7a8) · [`00b5e7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md#insn-00b5e7ac)

~~~diff
- 00b5e7a4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5e7a4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5e7a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5e7a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e7a4 bytes fa6703a9
- 00b5e7a8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5e7a8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5e7a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5e7a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e7a8 bytes f85f04a9
- 00b5e7ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5e7ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5e7ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5e7ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5e7ac bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

