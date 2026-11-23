# v15.7.4 → v16.0.0 · 最優先の変更候補 (55)

[一覧の目次](README.md)

<a id="compare-df959a54bb7e98091ed508645762864d"></a>

### [`00ada154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md) → [`00b39b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39b2c.md) FUN_00b39b2c

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0085ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085ef84.md) · 呼出先 12件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00891f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891f1c.md) · 呼出先 12件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 75.00% / 新版 73.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b39b80",
      "incomplete_value": true,
      "site": "00b39ba0",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:4fb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada1a8",
      "incomplete_value": true,
      "site": "00ada1c8",
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
                "const:ee6:8"
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
      "definition_site": "00b39ba4",
      "incomplete_value": true,
      "site": "00b39bb0",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada1cc",
      "incomplete_value": true,
      "site": "00ada1d8",
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
                "const:57a:8"
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
      "definition_site": "00b39bb4",
      "incomplete_value": true,
      "site": "00b39bb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ada1dc",
      "incomplete_value": true,
      "site": "00ada1dc",
      "value": [
        "LOAD",
        "8",
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
      "00b39b80",
      "READ",
      [
        "storage",
        "002a0ee6",
        null,
        "string"
      ]
    ],
    [
      "00b39ba4",
      "READ",
      [
        "storage",
        "002a357a",
        null,
        "string"
      ]
    ],
    [
      "00b39ba8",
      "READ",
      [
        "storage",
        "002a3587",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b39b80",
      "READ",
      [
        "storage",
        "002b14fb",
        null,
        "string"
      ]
    ],
    [
      "00b39ba4",
      "READ",
      [
        "storage",
        "002b3c54",
        null,
        "string"
      ]
    ],
    [
      "00b39ba8",
      "READ",
      [
        "storage",
        "002b3c61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md#insn-00ada2cc) · [`00ada448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md#insn-00ada448)
- 新版 [`00b39ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39b2c.md#insn-00b39ca4) · [`00b39e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39b2c.md#insn-00b39e20)

~~~diff
- 00ada2cc ["INT_ADD", "register:40f0:8", ["const:ada2cc:8", "const:4:8"]]
- 00ada2cc ["CALL", null, ["callee:00b3afa8:8"]]
+ 00b39ca4 ["INT_ADD", "register:40f0:8", ["const:b39ca4:8", "const:4:8"]]
+ 00b39ca4 ["CALL", null, ["callee:00b3afa8:8"]]
- 00ada2cc bytes c1040094
+ 00b39ca4 bytes c1040094
- 00ada448 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00ada448 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 00ada448 bytes 620200b4
+ 00b39e20 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 00b39e20 ["CBRANCH", null, ["local:b49:8", "tmp:0:1"]]
+ 00b39e20 bytes 620200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a9499ce42fb20dcd9044def3764ab74"></a>

### [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) → [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) FUN_00b39fc8

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0085e130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e130.md) [`0085fc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085fc1c.md) [`008710cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/008710cc.md) [`00879ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879ea8.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 4件 [`008910c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/008910c8.md) [`00892bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md) [`008a426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a426c.md) [`008ad048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad048.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 92.59% / 新版 89.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ada640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ada644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ada648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ada638",
      "READ",
      [
        "storage",
        "00294094",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ada63c",
      "READ",
      [
        "storage",
        "002940a4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ada640",
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
      "00b3a010",
      "READ",
      [
        "storage",
        "002a3923",
        null,
        "string"
      ]
    ],
    [
      "00b3a014",
      "READ",
      [
        "storage",
        "002a3933",
        null,
        "string"
      ]
    ],
    [
      "00b3a018",
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

- 旧版 [`00ada640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada640) · [`00ada644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada644) · [`00ada648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md#insn-00ada648)

~~~diff
- 00ada640 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00ada640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ada640 bytes e01b00f9
- 00ada644 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ada644 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ada644 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00ada644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ada644 bytes 1f600039
- 00ada648 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00ada648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ada648 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdca32caee7f03b45d1d8344420ddb7e"></a>

### [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) → [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) FUN_00b3a190

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0085f63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085f/0085f63c.md) [`00871208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00871/00871208.md) [`00879fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00879/00879fe4.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 3件 [`008925d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008925d4.md) [`008a43a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a43a8.md) [`008ad184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad184.md) · 呼出先 9件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 68.97% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3a1dc",
      "incomplete_value": true,
      "site": "00b3a1f8",
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
                "const:bdf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada804",
      "incomplete_value": true,
      "site": "00ada820",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:23a:8"
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
      "site": "00ada8a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3a27c"
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
      "00b3a1dc",
      "READ",
      [
        "storage",
        "0029523a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ada8a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3a290",
      "PARAM",
      [
        "storage",
        "0109ffd0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3a1dc",
      "READ",
      [
        "storage",
        "002a4bdf",
        null,
        "string"
      ]
    ],
    [
      "00b3a27c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3a290",
      "PARAM",
      [
        "storage",
        "01124e90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ada8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada8a4) · [`00ada8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada8b0) · [`00ada8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md#insn-00ada8c4)
- 新版 [`00b3a29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md#insn-00b3a29c)

~~~diff
- 00ada8a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00ada8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ada8a4 bytes e82300f9
- 00ada8b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ada8b0 ["INT_ADD", "register:40f0:8", ["const:ada8b0:8", "const:4:8"]]
- 00ada8b0 ["CALLIND", null, ["register:0:8"]]
- 00ada8b0 bytes 00013fd6
- 00ada8c4 ["INT_ADD", "register:40f0:8", ["const:ada8c4:8", "const:4:8"]]
- 00ada8c4 ["CALL", null, ["callee:00b3b290:8"]]
+ 00b3a29c ["INT_ADD", "register:40f0:8", ["const:b3a29c:8", "const:4:8"]]
+ 00b3a29c ["CALL", null, ["callee:00b3b290:8"]]
- 00ada8c4 bytes fd030094
+ 00b3a29c bytes fd030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f9dc7f06b0ce40aae4f05fedf7b8e6"></a>

### [`00ada978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md) → [`00b3a350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a350.md) FUN_00b3a350

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 9件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.59% / 新版 86.59%

CFGの説明率　旧版 60.00% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3a394",
      "incomplete_value": true,
      "site": "00b3a3a4",
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
                "const:650:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada9bc",
      "incomplete_value": true,
      "site": "00ada9cc",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "00b3a3a8",
      "incomplete_value": true,
      "site": "00b3a3bc",
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
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ada9d0",
      "incomplete_value": true,
      "site": "00ada9e4",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:23d:8"
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
      "definition_site": "00b3a3a8",
      "incomplete_value": true,
      "site": "00b3a3bc",
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
      "definition_site": "00ada9d0",
      "incomplete_value": true,
      "site": "00ada9e4",
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
      "00b3a394",
      "READ",
      [
        "storage",
        "002b1040",
        null,
        null
      ]
    ],
    [
      "00b3a3a8",
      "READ",
      [
        "storage",
        "0029223d",
        null,
        "string"
      ]
    ],
    [
      "00b3a3a8",
      "READ",
      [
        "storage",
        "0029224d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3a394",
      "READ",
      [
        "storage",
        "002c2650",
        null,
        null
      ]
    ],
    [
      "00b3a3a8",
      "READ",
      [
        "storage",
        "002a184e",
        null,
        "string"
      ]
    ],
    [
      "00b3a3a8",
      "READ",
      [
        "storage",
        "002a185e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adaa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00adaa20) · [`00adaa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00adaa60) · [`00adaa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada978.md#insn-00adaa88)
- 新版 [`00b3a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a350.md#insn-00b3a3f8)

~~~diff
- 00adaa20 ["INT_ADD", "register:40f0:8", ["const:adaa20:8", "const:4:8"]]
- 00adaa20 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b3a3f8 ["INT_ADD", "register:40f0:8", ["const:b3a3f8:8", "const:4:8"]]
+ 00b3a3f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00adaa20 bytes 90010494
+ 00b3a3f8 bytes ae750494
- 00adaa60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adaa60 ["INT_ADD", "register:40f0:8", ["const:adaa60:8", "const:4:8"]]
- 00adaa60 ["CALLIND", null, ["register:0:8"]]
- 00adaa60 bytes 00013fd6
- 00adaa88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adaa88 ["INT_ADD", "register:40f0:8", ["const:adaa88:8", "const:4:8"]]
- 00adaa88 ["CALLIND", null, ["register:0:8"]]
- 00adaa88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89070a12dac68d2022a500254b944bd5"></a>

### [`00adab64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md) → [`00b3a53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a53c.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyGetCurrencyBalance

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 53.85% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3a564",
      "incomplete_value": true,
      "site": "00b3a564",
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
      "definition_site": "00adab8c",
      "incomplete_value": true,
      "site": "00adab8c",
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
      "definition_site": "00b3a580",
      "incomplete_value": true,
      "site": "00b3a580",
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
      "definition_site": "00adaba8",
      "incomplete_value": true,
      "site": "00adaba8",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00adabbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3a560",
      "READ",
      [
        "storage",
        "0109ffc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a578",
      "READ",
      [
        "storage",
        "0109ffc0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adabbc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3a560",
      "READ",
      [
        "storage",
        "01124e80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a578",
      "READ",
      [
        "storage",
        "01124e80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a594",
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

- 旧版 [`00adab8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adab8c) · [`00adaba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adaba8) · [`00adabbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adab64.md#insn-00adabbc)
- 新版 [`00b3a564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a53c.md#insn-00b3a564) · [`00b3a580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a53c.md#insn-00b3a580)

~~~diff
- 00adab8c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00adab8c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b3a564 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b3a564 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00adab8c bytes 280200b4
+ 00b3a564 bytes 280200b4
- 00adaba8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00adaba8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b3a580 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b3a580 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00adaba8 bytes 600200b4
+ 00b3a580 bytes 600200b4
- 00adabbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00adabbc ["INT_ADD", "register:40f0:8", ["const:adabbc:8", "const:4:8"]]
- 00adabbc ["CALLIND", null, ["register:0:8"]]
- 00adabbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb6a95d91efdfed98095a8ba4c0f7bd"></a>

### [`00adac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md) → [`00b3a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a610.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoySpendCurrency

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3a638",
      "incomplete_value": true,
      "site": "00b3a638",
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
      "definition_site": "00adac60",
      "incomplete_value": true,
      "site": "00adac60",
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
      "definition_site": "00b3a654",
      "incomplete_value": true,
      "site": "00b3a654",
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
      "definition_site": "00adac7c",
      "incomplete_value": true,
      "site": "00adac7c",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adacd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3a634",
      "READ",
      [
        "storage",
        "0109fff0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a64c",
      "READ",
      [
        "storage",
        "0109fff0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adacd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3a6e0"
      ]
    ]
  ],
  "added": [
    [
      "00b3a634",
      "READ",
      [
        "storage",
        "01124eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a64c",
      "READ",
      [
        "storage",
        "01124eb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a6ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3a6e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adacd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md#insn-00adacd4) · [`00adac50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adac38.md#insn-00adac50)
- 新版 [`00b3a6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a610.md#insn-00b3a6ac) · [`00b3a628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a610.md#insn-00b3a628)

~~~diff
- 00adacd4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adacd4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00adacd4 bytes a1010054
+ 00b3a6ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b3a6ac ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b3a6ac bytes a1010054
- 00adac50 ["COPY", "register:40a8:8", ["const:109f000:8"]]
+ 00b3a628 ["COPY", "register:40a8:8", ["const:1124000:8"]]
- 00adac50 bytes 352e00b0
+ 00b3a628 bytes 552f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6cdcc80727bef735314652308a97888"></a>

### [`00adadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md) → [`00b3a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestFailure

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b3b3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b3f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3a800",
      "incomplete_value": true,
      "site": "00b3a804",
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
      "definition_site": "00adae28",
      "incomplete_value": true,
      "site": "00adae2c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3a7ec",
      "incomplete_value": false,
      "site": "00b3a7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adae14",
      "incomplete_value": false,
      "site": "00adae1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00b3a7ec",
      "PARAM",
      [
        "storage",
        "0109ff38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b3a7ec",
      "PARAM",
      [
        "storage",
        "01124df8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adae1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adae1c) · [`00adadfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adadfc) · [`00adae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adadcc.md#insn-00adae0c)
- 新版 [`00b3a7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md#insn-00b3a7f4) · [`00b3a7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md#insn-00b3a7d4) · [`00b3a7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a7a4.md#insn-00b3a7e4)

~~~diff
- 00adae1c ["INT_ADD", "register:40f0:8", ["const:adae1c:8", "const:4:8"]]
- 00adae1c ["CALL", null, ["callee:00b3b3f8:8"]]
+ 00b3a7f4 ["INT_ADD", "register:40f0:8", ["const:b3a7f4:8", "const:4:8"]]
+ 00b3a7f4 ["CALL", null, ["callee:00b3b3f8:8"]]
- 00adae1c bytes 01030094
+ 00b3a7f4 bytes 01030094
- 00adadfc ["INT_ADD", "register:40f0:8", ["const:adadfc:8", "const:4:8"]]
- 00adadfc ["CALL", null, ["callee:00589914:8"]]
+ 00b3a7d4 ["INT_ADD", "register:40f0:8", ["const:b3a7d4:8", "const:4:8"]]
+ 00b3a7d4 ["CALL", null, ["callee:00589914:8"]]
- 00adadfc bytes 202fea97
+ 00b3a7d4 bytes 503ce997
- 00adae0c ["INT_ADD", "register:40f0:8", ["const:adae0c:8", "const:4:8"]]
- 00adae0c ["CALL", null, ["callee:00589914:8"]]
+ 00b3a7e4 ["INT_ADD", "register:40f0:8", ["const:b3a7e4:8", "const:4:8"]]
+ 00b3a7e4 ["CALL", null, ["callee:00589914:8"]]
- 00adae0c bytes 1c2fea97
+ 00b3a7e4 bytes 4c3ce997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4560fb903b1c28fd0c88b11c0228e7"></a>

### [`00adaf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md) → [`00b3a970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a970.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementShown

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b3b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 54.55% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3a9b0",
      "incomplete_value": true,
      "site": "00b3a9b4",
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
      "definition_site": "00adafd8",
      "incomplete_value": true,
      "site": "00adafdc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb014"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3a9ec"
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
      "00b3a99c",
      "PARAM",
      [
        "storage",
        "0109ff50",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adb014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aa2c"
      ]
    ]
  ],
  "added": [
    [
      "00b3a99c",
      "PARAM",
      [
        "storage",
        "01124e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3a9ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aa2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adafcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md#insn-00adafcc) · [`00adb014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md#insn-00adb014)
- 新版 [`00b3a9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a970.md#insn-00b3a9a4) · [`00b3a9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a970.md#insn-00b3a9ec)

~~~diff
- 00adafcc ["INT_ADD", "register:40f0:8", ["const:adafcc:8", "const:4:8"]]
- 00adafcc ["CALL", null, ["callee:00b3b4fc:8"]]
+ 00b3a9a4 ["INT_ADD", "register:40f0:8", ["const:b3a9a4:8", "const:4:8"]]
+ 00b3a9a4 ["CALL", null, ["callee:00b3b4fc:8"]]
- 00adafcc bytes d6020094
+ 00b3a9a4 bytes d6020094
- 00adb014 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adb014 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00adb014 bytes 01020054
+ 00b3a9ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b3a9ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b3a9ec bytes 01020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235f1b8ab948e9bac14f46330c94aa30"></a>

### [`00adb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md) → [`00b3aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementDismissed

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00566a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566a7c.md) [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b3b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3aa70",
      "incomplete_value": true,
      "site": "00b3aa74",
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
      "definition_site": "00adb098",
      "incomplete_value": true,
      "site": "00adb09c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3aa5c",
      "incomplete_value": false,
      "site": "00b3aa64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adb084",
      "incomplete_value": false,
      "site": "00adb08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb0b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3aa5c",
      "PARAM",
      [
        "storage",
        "0109ff50",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adb0b4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3aa5c",
      "PARAM",
      [
        "storage",
        "01124e10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3aa8c",
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

- 旧版 [`00adb08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb08c) · [`00adb09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb09c) · [`00adb0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md#insn-00adb0b4)
- 新版 [`00b3aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md#insn-00b3aa64) · [`00b3aa74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md#insn-00b3aa74)

~~~diff
- 00adb08c ["INT_ADD", "register:40f0:8", ["const:adb08c:8", "const:4:8"]]
- 00adb08c ["CALL", null, ["callee:00b3b4fc:8"]]
+ 00b3aa64 ["INT_ADD", "register:40f0:8", ["const:b3aa64:8", "const:4:8"]]
+ 00b3aa64 ["CALL", null, ["callee:00b3b4fc:8"]]
- 00adb08c bytes a6020094
+ 00b3aa64 bytes a6020094
- 00adb09c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b3aa74 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00adb09c bytes e0000054
+ 00b3aa74 bytes e0000054
- 00adb0b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb0b4 ["INT_ADD", "register:40f0:8", ["const:adb0b4:8", "const:4:8"]]
- 00adb0b4 ["CALLIND", null, ["register:0:8"]]
- 00adb0b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2340ed2948e4cde5e6a9e2742539e7b"></a>

### [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) → [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) FUN_00b3aaf4

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ad9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9108.md) [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) · 呼出先 2件 [`00adb11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00b38ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38ae0.md) [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) · 呼出先 2件 [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 3.03% / 新版 3.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb154"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb1b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb1bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adb154",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ab40"
      ]
    ],
    [
      "unmatched:00adb1b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aba0"
      ]
    ],
    [
      "unmatched:00adb1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3abb4"
      ]
    ]
  ],
  "added": [
    [
      "00b3ab2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ab40"
      ]
    ],
    [
      "00b3ab90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aba0"
      ]
    ],
    [
      "00b3ab94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3abb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adb144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md#insn-00adb144) · [`00adb154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md#insn-00adb154) · [`00adb178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb11c.md#insn-00adb178)
- 新版 [`00b3ab1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md#insn-00b3ab1c)

~~~diff
- 00adb144 ["INT_ADD", "register:40f0:8", ["const:adb144:8", "const:4:8"]]
- 00adb144 ["CALL", null, ["local:b0:8"]]
+ 00b3ab1c ["INT_ADD", "register:40f0:8", ["const:b3ab1c:8", "const:4:8"]]
+ 00b3ab1c ["CALL", null, ["local:b0:8"]]
- 00adb144 bytes f6ffff97
+ 00b3ab1c bytes f6ffff97
- 00adb154 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00adb154 bytes a0000054
- 00adb178 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb178 ["INT_ADD", "register:40f0:8", ["const:adb178:8", "const:4:8"]]
- 00adb178 ["CALLIND", null, ["register:0:8"]]
- 00adb178 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a75d8848cfa6338026d5e3120645e40"></a>

### [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) → [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) FUN_00b3abd4

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 2件 [`00ad9110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9110.md) [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) · 呼出先 2件 [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00b38ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38ae8.md) [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) · 呼出先 2件 [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 73.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3abe8",
      "incomplete_value": true,
      "site": "00b3abf0",
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
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3ac6c",
      "incomplete_value": true,
      "site": "00b3ac70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
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
    "old": null,
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00adb218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md#insn-00adb218) · [`00adb298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md#insn-00adb298) · [`00adb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb1fc.md#insn-00adb1fc)
- 新版 [`00b3abf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md#insn-00b3abf0) · [`00b3ac70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md#insn-00b3ac70) · [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md#insn-00b3abd4)

~~~diff
- 00adb218 ["INT_ADD", "register:40f0:8", ["const:adb218:8", "const:4:8"]]
- 00adb218 ["CALL", null, ["local:b0:8"]]
+ 00b3abf0 ["INT_ADD", "register:40f0:8", ["const:b3abf0:8", "const:4:8"]]
+ 00b3abf0 ["CALL", null, ["local:b0:8"]]
- 00adb218 bytes f9ffff97
+ 00b3abf0 bytes f9ffff97
- 00adb298 ["INT_ADD", "register:40f0:8", ["const:adb298:8", "const:4:8"]]
- 00adb298 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00b3ac70 ["INT_ADD", "register:40f0:8", ["const:b3ac70:8", "const:4:8"]]
+ 00b3ac70 ["CALL", null, ["callee:00c57ab0:8"]]
- 00adb298 bytes 72ff0394
+ 00b3ac70 bytes 90730494
- 00adb1fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00adb1fc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b3abd4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b3abd4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00adb1fc bytes 610200b4
+ 00b3abd4 bytes 610200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c25decdd946dc67869ed5186261f51"></a>

### [`00adb2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md) → [`00b3ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3ac84.md) FUN_00b3ac84

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ad9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9b64.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00adb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00b3953c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b3953c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00b3adc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 46.67% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb2dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adb2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb3a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3adc4"
      ]
    ]
  ],
  "added": [
    [
      "00b3ac88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b3acb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b3ad7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3adc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md#insn-00adb2b0) · [`00adb2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md#insn-00adb2dc) · [`00adb3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md#insn-00adb3a4)

~~~diff
- 00adb2b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adb2b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adb2b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00adb2b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adb2b0 bytes fd7b03a9
- 00adb2dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adb2dc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00adb2dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adb2dc bytes a8831ff8
- 00adb3a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00adb3a4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00adb3a4 bytes 41020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e7aa11ee1c2a0cc5eb0445ef865cf0a"></a>

### [`00adb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md) → [`00b3adc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md) FUN_00b3adc8

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adb2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb2ac.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00b3ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3ac84.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 23.08% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb45c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb460"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb46c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adb474",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ],
    [
      "unmatched:00adb490",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ae0c"
      ]
    ]
  ],
  "added": [
    [
      "00b3ae4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ],
    [
      "00b3ae68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ae0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adb45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md#insn-00adb45c) · [`00adb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md#insn-00adb460) · [`00adb46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb3f0.md#insn-00adb46c)

~~~diff
- 00adb45c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00adb45c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adb45c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00adb45c ["COPY", "register:40d0:8", ["tmp:0:8"]]
- 00adb45c bytes 5a01899a
- 00adb460 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adb460 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adb460 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00adb460 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00adb460 bytes 16018b9a
- 00adb46c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00adb46c ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 00adb46c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00adb46c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00adb46c bytes 5733999a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ebdd873e601d1cec0319db6af34f547"></a>

### [`00adb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md) → [`00b3afa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3afa8.md) FUN_00b3afa8

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ada154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada154.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00adb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00b39b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39b2c.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00b3b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b0e0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 33.33% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb6b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3afd8"
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
      "unmatched:00adb600",
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
      "00b3afd8",
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

- 旧版 [`00adb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md#insn-00adb600) · [`00adb604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md#insn-00adb604) · [`00adb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md#insn-00adb6a0)
- 新版 [`00b3afdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3afa8.md#insn-00b3afdc) · [`00b3b078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3afa8.md#insn-00b3b078)

~~~diff
- 00adb600 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adb600 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00adb600 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adb600 bytes a8831ff8
- 00adb604 ["INT_ADD", "register:40f0:8", ["const:adb604:8", "const:4:8"]]
- 00adb604 ["CALL", null, ["callee:00b3b0e0:8"]]
+ 00b3afdc ["INT_ADD", "register:40f0:8", ["const:b3afdc:8", "const:4:8"]]
+ 00b3afdc ["CALL", null, ["callee:00b3b0e0:8"]]
- 00adb604 bytes 41000094
+ 00b3afdc bytes 41000094
- 00adb6a0 ["INT_ADD", "register:40f0:8", ["const:adb6a0:8", "const:4:8"]]
- 00adb6a0 ["CALL", null, ["callee:0043bb64:8"]]
+ 00b3b078 ["INT_ADD", "register:40f0:8", ["const:b3b078:8", "const:4:8"]]
+ 00b3b078 ["CALL", null, ["callee:0043bb64:8"]]
- 00adb6a0 bytes 71f6e497
+ 00b3b078 bytes bb02e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fcfb274751d7f1a6abe9f7af5c92802"></a>

### [`00adb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md) → [`00b3b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b0e0.md) FUN_00b3b0e0

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb5d0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00b3afa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3afa8.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 61.54% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb70c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adb708",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb70c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb710",
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
      "00b3b0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3b0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b3b0e8",
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

- 旧版 [`00adb708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md#insn-00adb708) · [`00adb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md#insn-00adb70c) · [`00adb710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb708.md#insn-00adb710)

~~~diff
- 00adb708 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adb708 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adb708 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00adb708 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00adb708 bytes fd7bbba9
- 00adb70c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00adb70c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00adb70c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00adb70c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adb70c bytes fa6701a9
- 00adb710 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00adb710 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00adb710 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00adb710 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adb710 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c04f9bb460c61cb3b129e321b7a2f0ea"></a>

### [`00adb8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb8b8.md) → [`00b3b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b290.md) FUN_00b3b290

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ada5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) [`00ada7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada7b8.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.91% / 新版 71.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb8d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adb99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3b2b0"
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
      "unmatched:00adb8d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adb8dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b3cc"
      ]
    ],
    [
      "unmatched:00adba00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b3f0"
      ]
    ]
  ],
  "added": [
    [
      "00b3b2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b3b2b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b3cc"
      ]
    ],
    [
      "00b3b3d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b3f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adb8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb8b8.md#insn-00adb8d8) · [`00adb8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb8b8.md#insn-00adb8dc) · [`00adb924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb8b8.md#insn-00adb924)

~~~diff
- 00adb8d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adb8d8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00adb8d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adb8d8 bytes a8831ff8
- 00adb8dc ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00adb8dc bytes c0080054
- 00adb924 ["COPY", "register:0:8", ["register:4040:8"]]
- 00adb924 ["INT_ADD", "register:40f0:8", ["const:adb924:8", "const:4:8"]]
- 00adb924 ["CALLIND", null, ["register:0:8"]]
- 00adb924 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-263b92f4616a64ce22c5f7437da03d20"></a>

### [`00adbb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) → [`00b3b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md) FUN_00b3b4fc

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00adaf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00adaf98.md) [`00adb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adb058.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00b3a970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a970.md) [`00b3aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbbdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbbe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adbbec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ]
  ],
  "added": [
    [
      "00b3b5c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adbbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md#insn-00adbbdc) · [`00adbbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md#insn-00adbbe0) · [`00adbbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md#insn-00adbbe8)

~~~diff
- 00adbbdc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00adbbdc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adbbdc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00adbbdc ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00adbbdc bytes 01018b9a
- 00adbbe0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00adbbe0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00adbbe0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00adbbe0 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00adbbe0 bytes 5701899a
- 00adbbe8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00adbbe8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00adbbe8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00adbbe8 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00adbbe8 bytes e232969a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d6bbe36da2faa5a54f0ea4b62c9e06"></a>

### [`00adbc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md) → [`00b3b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b600.md) _INIT_273

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00569da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00569/00569da8.md) [`0085e2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085e/0085e2f8.md) [`00ad9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad9/00ad9108.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`0058cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058c/0058cc40.md) [`00891290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00891/00891290.md) [`00b38ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 44.29% / 新版 44.29%

CFGの説明率　旧版 27.27% / 新版 18.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 47件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbc2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbc2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adbc30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adbc2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adbc30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adbc34",
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
      "00b3b604",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b3b608",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b3b60c",
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

- 旧版 [`00adbc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md#insn-00adbc2c) · [`00adbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md#insn-00adbc30) · [`00adbc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbc28.md#insn-00adbc34)

~~~diff
- 00adbc2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adbc2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adbc2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00adbc2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adbc2c bytes fd7b0fa9
- 00adbc30 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00adbc30 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00adbc30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00adbc30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adbc30 bytes fc5710a9
- 00adbc34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00adbc34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00adbc34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00adbc34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adbc34 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bcacbea62f5261eb86dd626075d41db"></a>

### [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md) → [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) FUN_00b3ba6c

採用 · 移動量 `+0x5f9d8` · 根拠 `leaf_bytes_and_local_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 82件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a2308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2308.md) [`005a33f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a33f8.md) [`005a3cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3cbc.md) [`005a3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3eb8.md) · 呼出先 0件 
- 新版 呼出元 80件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005c8584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8584.md) [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-b9258d42e4f0f48dac1795347d71ebd7"></a>

### [`00adc16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md) → [`00b3bb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bb44.md) _INIT_274

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 64.41% / 新版 64.41%

CFGの説明率　旧版 51.43% / 新版 48.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc174"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adc170",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adc174",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adc178",
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
      "00b3bb48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b3bb4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b3bb50",
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

- 旧版 [`00adc170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc170) · [`00adc174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc174) · [`00adc178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc16c.md#insn-00adc178)

~~~diff
- 00adc170 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adc170 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adc170 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00adc170 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adc170 bytes fd7b0fa9
- 00adc174 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00adc174 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00adc174 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00adc174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adc174 bytes fc5710a9
- 00adc178 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00adc178 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00adc178 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00adc178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adc178 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d85692889af78493af606da9a9f6199"></a>

### [`00adc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md) → [`00b3c040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c040.md) FUN_00b3c040

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00adc50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc50c.md) [`00adc8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 2件 [`00b3bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bee4.md) [`00b3c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c29c.md) · 呼出先 6件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.44% / 新版 84.44%

CFGの説明率　旧版 65.91% / 新版 61.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc6ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc6b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc6b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adc694",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00adc6ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x13d0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adc6b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c7]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3c06c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "00b3c084",
      "WRITE",
      [
        "storage",
        "Stack[-0x13d0]",
        null,
        null
      ]
    ],
    [
      "00b3c088",
      "WRITE",
      [
        "storage",
        "Stack[-0x13c7]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adc6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc6ac) · [`00adc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc6b0) · [`00adc6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md#insn-00adc6b4)

~~~diff
- 00adc6ac ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00adc6ac ["INT_ADD", "tmp:1:8", ["register:8:8", "const:10:8"]]
- 00adc6ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00adc6ac bytes e9430039
- 00adc6b0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00adc6b0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 00adc6b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00adc6b0 bytes e89301b8
- 00adc6b4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00adc6b4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:11:8"]]
- 00adc6b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00adc6b4 bytes ea1301f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e105fd1af752e50a183642836ccbdddc"></a>

### [`00adc8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md) → [`00b3c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c29c.md) FUN_00b3c29c

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00845f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f8c.md) · 呼出先 7件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00adc668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc668.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00878278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md) · 呼出先 7件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00b3c040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c040.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 55.56% / 新版 60.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adc964"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00adca34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3c33c"
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
      "unmatched:00adc964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c3c4"
      ]
    ],
    [
      "unmatched:00adca34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c490"
      ]
    ]
  ],
  "added": [
    [
      "00b3c33c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c3c4"
      ]
    ],
    [
      "00b3c40c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c490"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adc964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md#insn-00adc964) · [`00adca34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc8c4.md#insn-00adca34)
- 新版 [`00b3c33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c29c.md#insn-00b3c33c)

~~~diff
- 00adc964 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00adc964 bytes 42040054
- 00adca34 ["CBRANCH", null, ["local:b23:8", "register:102:1"]]
- 00adca34 bytes 22040054
+ 00b3c33c ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
+ 00b3c33c bytes 42040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed43c51b69b3258644ad9ff47d0ee28f"></a>

### [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md) → [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md) FUN_00b3c4b4

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 20件 [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`00453c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/00453c78.md) [`0046aa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046aa44.md) [`0046c588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046c/0046c588.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 20件 [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`00476b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476b10.md) [`0048d8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d8dc.md) [`0048f420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048f/0048f420.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 89.47% / 新版 91.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00adcb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md#insn-00adcb00) · [`00adcb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md#insn-00adcb44) · [`00adcb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md#insn-00adcb64)
- 新版 [`00b3c4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md#insn-00b3c4d8) · [`00b3c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md#insn-00b3c51c) · [`00b3c53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md#insn-00b3c53c)

~~~diff
- 00adcb00 ["CBRANCH", null, ["local:b25:8", "register:102:1"]]
+ 00b3c4d8 ["CBRANCH", null, ["local:b24:8", "register:102:1"]]
- 00adcb00 bytes e20d0054
+ 00b3c4d8 bytes e20d0054
- 00adcb44 ["INT_ADD", "register:40f0:8", ["const:adcb44:8", "const:4:8"]]
- 00adcb44 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b3c51c ["INT_ADD", "register:40f0:8", ["const:b3c51c:8", "const:4:8"]]
+ 00b3c51c ["CALL", null, ["callee:00c57a90:8"]]
- 00adcb44 bytes 3ff90394
+ 00b3c51c bytes 5d6d0494
- 00adcb64 ["INT_ADD", "register:40f0:8", ["const:adcb64:8", "const:4:8"]]
- 00adcb64 ["CALL", null, ["callee:00c57c90:8"]]
+ 00b3c53c ["INT_ADD", "register:40f0:8", ["const:b3c53c:8", "const:4:8"]]
+ 00b3c53c ["CALL", null, ["callee:00c57c90:8"]]
- 00adcb64 bytes b7f90394
+ 00b3c53c bytes d56d0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c27853d6780126c5a85f31d0eac11aa9"></a>

### [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md) → [`00b3c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md) FUN_00b3c6b0

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`0064b18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md) [`00654084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`0089d9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089d/0089d9f4.md) [`008f2388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f2/008f2388.md) · 呼出先 16件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`007f8ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f8/007f8ecc.md)
- 新版 呼出元 8件 [`0067146c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00671/0067146c.md) [`0067a364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067a/0067a364.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008d188c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d188c.md) [`00926414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926414.md) · 呼出先 16件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0082e2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082e2e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.25% / 新版 55.25%

CFGの説明率　旧版 5.26% / 新版 3.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 21件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adcd28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adcd80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adcd88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adcd28",
      "DATA",
      [
        "storage",
        "00bf7158",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00adcd5c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00adcd7c",
      "READ",
      [
        "storage",
        "002a9f34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3c700",
      "DATA",
      [
        "storage",
        "00c74280",
        null,
        "pointer"
      ]
    ],
    [
      "00b3c734",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b3c754",
      "READ",
      [
        "storage",
        "002baccd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adcd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00adcd28) · [`00adcd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00adcd80) · [`00adcd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md#insn-00adcd88)

~~~diff
- 00adcd28 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00adcd28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00adcd28 bytes 090000f9
- 00adcd80 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00adcd80 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:29:8"]]
- 00adcd80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00adcd80 bytes e9930278
- 00adcd88 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00adcd88 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:8:8"]]
- 00adcd88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00adcd88 bytes e9230039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db25730c3786d11f8be8ab14cab759e7"></a>

### [`00add328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md) → [`00b3cd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3cd00.md) _INIT_275

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.14% / 新版 75.14%

CFGの説明率　旧版 69.70% / 新版 60.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00add358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00add380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00add38c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00add358",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00add364",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00add380",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3cd30",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b3cd3c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b3cd58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00add358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md#insn-00add358) · [`00add380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md#insn-00add380) · [`00add38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add328.md#insn-00add38c)

~~~diff
- 00add358 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00add358 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00add358 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00add358 bytes a9831ff8
- 00add380 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00add380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00add380 bytes e013813c
- 00add38c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00add38c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 00add38c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00add38c bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a97a09c95c7875c82dd9fb5e4f20697d"></a>

### [`00add6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md) → [`00b3d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d090.md) FUN_00b3d090

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00ade73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md) · 呼出先 1件 [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00b3e114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3e/00b3e114.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00add6ec",
      "incomplete_value": true,
      "site": "00add6fc",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00add6f0",
      "incomplete_value": false,
      "site": "00add6fc",
      "value": [
        "leaf",
        "const:3:8"
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00add724",
      "incomplete_value": true,
      "site": "00add72c",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00add6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md#insn-00add6fc) · [`00add72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md#insn-00add72c) · [`00add77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00add/00add6b8.md#insn-00add77c)
- 新版 [`00b3d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d090.md#insn-00b3d0d4) · [`00b3d104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d090.md#insn-00b3d104) · [`00b3d154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3d090.md#insn-00b3d154)

~~~diff
- 00add6fc ["INT_ADD", "register:40f0:8", ["const:add6fc:8", "const:4:8"]]
- 00add6fc ["CALL", null, ["callee:004878fc:8"]]
+ 00b3d0d4 ["INT_ADD", "register:40f0:8", ["const:b3d0d4:8", "const:4:8"]]
+ 00b3d0d4 ["CALL", null, ["callee:004878fc:8"]]
- 00add6fc bytes da1ce697
+ 00b3d0d4 bytes 0a2ae597
- 00add72c ["INT_ADD", "register:40f0:8", ["const:add72c:8", "const:4:8"]]
- 00add72c ["CALL", null, ["callee:004878fc:8"]]
+ 00b3d104 ["INT_ADD", "register:40f0:8", ["const:b3d104:8", "const:4:8"]]
+ 00b3d104 ["CALL", null, ["callee:004878fc:8"]]
- 00add72c bytes ce1ce697
+ 00b3d104 bytes fe29e597
- 00add77c ["INT_ADD", "register:40f0:8", ["const:add77c:8", "const:4:8"]]
- 00add77c ["CALL", null, ["callee:004878fc:8"]]
+ 00b3d154 ["INT_ADD", "register:40f0:8", ["const:b3d154:8", "const:4:8"]]
+ 00b3d154 ["CALL", null, ["callee:004878fc:8"]]
- 00add77c bytes ba1ce697
+ 00b3d154 bytes ea29e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634c447f8dde5c1db09a192e4a7b5637"></a>

### [`00ade73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md) → [`00b3e114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3e/00b3e114.md) FUN_00b3e114

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.35% / 新版 76.35%

CFGの説明率　旧版 39.02% / 新版 34.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ade750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ade750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ade770"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ade750",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ade770",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ade774",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ]
  ],
  "added": [
    [
      "00b3e128",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b3e148",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b3e14c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ade750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade750) · [`00ade770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade770) · [`00ade774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade73c.md#insn-00ade774)

~~~diff
- 00ade750 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ade750 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ade750 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ade750 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ade750 bytes f44f05a9
- 00ade770 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ade770 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ade770 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ade770 bytes a8831ff8
- 00ade774 ["INT_ADD", "register:40f0:8", ["const:ade774:8", "const:4:8"]]
- 00ade774 ["CALL", null, ["callee:00487de0:8"]]
- 00ade774 bytes f519e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49647bd6bc286113cb05a7e90ea46c55"></a>

### [`00ade9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md) → [`00b3e3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3e/00b3e3ac.md) FUN_00b3e3ac

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`008f06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008f0/008f06a0.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)
- 新版 呼出元 3件 [`006788a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00678/006788a0.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`0092472c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.16% / 新版 62.16%

CFGの説明率　旧版 34.89% / 新版 35.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 8件, `call_target` 3件, `store_value` 2件, `unresolved_branch_alignment` 39件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 55件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adecac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adecc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aded20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adea28",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00adea28",
      "PARAM",
      [
        "storage",
        "0109e4b8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00adea3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006fdbdc"
      ]
    ]
  ],
  "added": [
    [
      "00b3e400",
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      "00b3e400",
      "PARAM",
      [
        "storage",
        "011232e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b3e414",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00727cdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adecac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00adecac) · [`00adecc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00adecc8) · [`00aded20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade9d4.md#insn-00aded20)

~~~diff
- 00adecac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
- 00adecac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00adecac bytes 286d03f9
- 00adecc8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:6e8:8"]]
- 00adecc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00adecc8 bytes 287703f9
- 00aded20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00aded20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aded20 bytes e03300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d21b22f68882ad38456ecbeb9859313"></a>

### [`00adf6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md) → [`00b3f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f0bc.md) FUN_00b3f0bc

採用 · 移動量 `+0x5f9d8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade338.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dd10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.03% / 新版 84.03%

CFGの説明率　旧版 63.16% / 新版 59.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf88c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf890"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adf89c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3f13c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ade338"
      ]
    ],
    [
      "unmatched:00adf784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f170"
      ]
    ],
    [
      "unmatched:00adf898",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00adf8a4"
      ]
    ]
  ],
  "added": [
    [
      "00b3f13c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3dd10"
      ]
    ],
    [
      "00b3f15c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f170"
      ]
    ],
    [
      "00b3f270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f27c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adf764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md#insn-00adf764) · [`00adf784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md#insn-00adf784) · [`00adf7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adf6e4.md#insn-00adf7c4)
- 新版 [`00b3f13c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f0bc.md#insn-00b3f13c) · [`00b3f19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f0bc.md#insn-00b3f19c)

~~~diff
- 00adf764 ["INT_ADD", "register:40f0:8", ["const:adf764:8", "const:4:8"]]
- 00adf764 ["CALL", null, ["ram:ade338:8"]]
+ 00b3f13c ["INT_ADD", "register:40f0:8", ["const:b3f13c:8", "const:4:8"]]
+ 00b3f13c ["CALL", null, ["ram:b3dd10:8"]]
- 00adf764 bytes f5faff97
+ 00b3f13c bytes f5faff97
- 00adf784 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00adf784 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00adf784 bytes a80000b5
- 00adf7c4 ["INT_ADD", "register:40f0:8", ["const:adf7c4:8", "const:4:8"]]
- 00adf7c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b3f19c ["INT_ADD", "register:40f0:8", ["const:b3f19c:8", "const:4:8"]]
+ 00b3f19c ["CALL", null, ["callee:00c57a90:8"]]
- 00adf7c4 bytes 1fee0394
+ 00b3f19c bytes 3d620494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146c3ff8cdc1a200829acb102060b567"></a>

### [`00adfa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md) → [`00b3f3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f3dc.md) FUN_00b3f3dc

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3f3f0",
      "incomplete_value": false,
      "site": "00b3f3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adfa18",
      "incomplete_value": false,
      "site": "00adfa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "00b3f3f4",
      "DATA",
      [
        "storage",
        "00c0f9c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b3f3f4",
      "DATA",
      [
        "storage",
        "00c8f0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md#insn-00adfa10) · [`00adfa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md#insn-00adfa14) · [`00adfa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa04.md#insn-00adfa18)
- 新版 [`00b3f3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f3dc.md#insn-00b3f3e8) · [`00b3f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f3dc.md#insn-00b3f3ec) · [`00b3f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f3dc.md#insn-00b3f3f0)

~~~diff
- 00adfa10 ["INT_ADD", "register:40f0:8", ["const:adfa10:8", "const:4:8"]]
- 00adfa10 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b3f3e8 ["INT_ADD", "register:40f0:8", ["const:b3f3e8:8", "const:4:8"]]
+ 00b3f3e8 ["CALL", null, ["callee:00c57a90:8"]]
- 00adfa10 bytes 8ced0394
+ 00b3f3e8 bytes aa610494
- 00adfa14 ["COPY", "register:4040:8", ["const:c0f000:8"]]
+ 00b3f3ec ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00adfa14 bytes 88090090
+ 00b3f3ec bytes 880a0090
- 00adfa18 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00adfa18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00adfa18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00adfa18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b3f3f0 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00b3f3f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b3f3f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b3f3f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00adfa18 bytes 08212791
+ 00b3f3f0 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b53f30d7271896e857f1fc1015bca4c0"></a>

### [`00adfa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa28.md) → [`00b3f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f400.md) FUN_00b3f400

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00b3f404",
      "incomplete_value": false,
      "site": "00b3f408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00adfa2c",
      "incomplete_value": false,
      "site": "00adfa30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "00b3f408",
      "DATA",
      [
        "storage",
        "00c0f9c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b3f408",
      "DATA",
      [
        "storage",
        "00c8f0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa28.md#insn-00adfa28) · [`00adfa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa28.md#insn-00adfa2c)
- 新版 [`00b3f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f400.md#insn-00b3f400) · [`00b3f404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f400.md#insn-00b3f404)

~~~diff
- 00adfa28 ["COPY", "register:4040:8", ["const:c0f000:8"]]
+ 00b3f400 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00adfa28 bytes 88090090
+ 00b3f400 bytes 880a0090
- 00adfa2c ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00adfa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00adfa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00adfa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b3f404 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00b3f404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b3f404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b3f404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00adfa2c bytes 08212791
+ 00b3f404 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5460cee243322c80f5c044ba0616789"></a>

### [`00adfbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbd8.md) → [`00b3f5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f5b0.md) FUN_00b3f5b0

採用 · 移動量 `+0x5f9d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00467c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c58.md) [`00886014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/00886014.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md) [`008b9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9254.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfc0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3f5f4",
      "incomplete_value": true,
      "site": "00b3f60c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3f600",
      "incomplete_value": false,
      "site": "00b3f60c",
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
            "const:a58:8"
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
      "unmatched:00adfc0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467aec"
      ]
    ],
    [
      "unmatched:00adfc1c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00adfc28",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00b3f5e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467aec"
      ]
    ],
    [
      "00b3f5f4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3f600",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00adfc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbd8.md#insn-00adfc0c) · [`00adfc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbd8.md#insn-00adfc34) · [`00adfc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfbd8.md#insn-00adfc40)
- 新版 [`00b3f60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f5b0.md#insn-00b3f60c) · [`00b3f618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f5b0.md#insn-00b3f618)

~~~diff
- 00adfc0c ["INT_ADD", "register:40f0:8", ["const:adfc0c:8", "const:4:8"]]
- 00adfc0c ["CALL", null, ["callee:00467aec:8"]]
- 00adfc0c bytes 1294e597
- 00adfc34 ["INT_ADD", "register:40f0:8", ["const:adfc34:8", "const:4:8"]]
- 00adfc34 ["CALL", null, ["callee:00c58210:8"]]
+ 00b3f60c ["INT_ADD", "register:40f0:8", ["const:b3f60c:8", "const:4:8"]]
+ 00b3f60c ["CALL", null, ["callee:00c58210:8"]]
- 00adfc34 bytes e3ee0394
+ 00b3f60c bytes 01630494
- 00adfc40 ["INT_ADD", "register:40f0:8", ["const:adfc40:8", "const:4:8"]]
- 00adfc40 ["CALL", null, ["callee:008b9254:8"]]
+ 00b3f618 ["INT_ADD", "register:40f0:8", ["const:b3f618:8", "const:4:8"]]
+ 00b3f618 ["CALL", null, ["callee:008b9254:8"]]
- 00adfc40 bytes f598f697
+ 00b3f618 bytes 0fe7f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad6dc34d5ff4f1c106f08504810c122"></a>

### [`00adfce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md) → [`00b3f6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f6b8.md) _INIT_276

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.40% / 新版 77.40%

CFGの説明率　旧版 25.64% / 新版 27.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00adfce8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00adfce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adfce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00adfcec",
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
      "00b3f6bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b3f6c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b3f6c4",
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

- 旧版 [`00adfce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adfce4) · [`00adfce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adfce8) · [`00adfcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfce0.md#insn-00adfcec)

~~~diff
- 00adfce4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00adfce4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00adfce4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00adfce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adfce4 bytes fd7b0fa9
- 00adfce8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00adfce8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00adfce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00adfce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adfce8 bytes fc5710a9
- 00adfcec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00adfcec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00adfcec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00adfcec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00adfcec bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7b1e64ba6946ef7a5d39cb0c62ccd5b"></a>

### [`00ae00d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00d8.md) → [`00b3fab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fab0.md) _ZN8firebase9analytics8internal10FutureData6CreateEv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde60.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md)
- 新版 呼出元 1件 [`00c5a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8c0.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b3fae0",
      "incomplete_value": true,
      "site": "00b3fae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0108",
      "incomplete_value": true,
      "site": "00ae0108",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a0:8"
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
      "definition_site": "00b3fac8",
      "incomplete_value": false,
      "site": "00b3facc",
      "value": [
        "leaf",
        "const:3:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0110"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3fad4",
      "READ",
      [
        "storage",
        "00c1b8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b3fae0",
      "WRITE",
      [
        "storage",
        "010a0068",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b3fad4",
      "READ",
      [
        "storage",
        "00c9b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b3fae0",
      "WRITE",
      [
        "storage",
        "01124f28",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae00f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00d8.md#insn-00ae00f4) · [`00ae0110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00d8.md#insn-00ae0110)
- 新版 [`00b3facc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fab0.md#insn-00b3facc) · [`00b3fae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fab0.md#insn-00b3fae8)

~~~diff
- 00ae00f4 ["INT_ADD", "register:40f0:8", ["const:ae00f4:8", "const:4:8"]]
- 00ae00f4 ["CALL", null, ["callee:00c5a840:8"]]
+ 00b3facc ["INT_ADD", "register:40f0:8", ["const:b3facc:8", "const:4:8"]]
+ 00b3facc ["CALL", null, ["callee:00c5a840:8"]]
- 00ae00f4 bytes 3bf70394
+ 00b3facc bytes 5d6b0494
- 00ae0110 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae0110 ["RETURN", null, ["register:0:8"]]
- 00ae0110 bytes c0035fd6
+ 00b3fae8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b3fae8 ["RETURN", null, ["register:0:8"]]
+ 00b3fae8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff4c285df7c1fb13f98a161bdcf8d2a"></a>

### [`00ae0174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md) → [`00b3fb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb4c.md) _ZN8firebase9analytics8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde90.md) · 呼出先 5件 [`00ae0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md) [`00bddd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd70.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00c5a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8f0.md) · 呼出先 5件 [`00b3ff58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff58.md) [`00c5a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7d0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3fb60",
      "incomplete_value": true,
      "site": "00b3fb64",
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
      "definition_site": "00ae0188",
      "incomplete_value": true,
      "site": "00ae018c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3fb5c",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b3fb60",
      "READ",
      [
        "storage",
        "00c24748",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00b3fb60",
      "PARAM",
      [
        "storage",
        "0029853d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3fb5c",
      "READ",
      [
        "storage",
        "00c9b2a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b3fb60",
      "READ",
      [
        "storage",
        "00ca4230",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00b3fb60",
      "PARAM",
      [
        "storage",
        "002a8290",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae018c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md#insn-00ae018c) · [`00ae0180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md#insn-00ae0180) · [`00ae0184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md#insn-00ae0184)
- 新版 [`00b3fb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb4c.md#insn-00b3fb64) · [`00b3fb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb4c.md#insn-00b3fb58) · [`00b3fb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb4c.md#insn-00b3fb5c)

~~~diff
- 00ae018c ["INT_ADD", "register:40f0:8", ["const:ae018c:8", "const:4:8"]]
- 00ae018c ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00b3fb64 ["INT_ADD", "register:40f0:8", ["const:b3fb64:8", "const:4:8"]]
+ 00b3fb64 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00ae018c bytes f9f60394
+ 00b3fb64 bytes 1b6b0494
- 00ae0180 ["COPY", "register:4098:8", ["const:c1b000:8"]]
+ 00b3fb58 ["COPY", "register:4098:8", ["const:c9b000:8"]]
- 00ae0180 bytes d30900f0
+ 00b3fb58 bytes f30a0090
- 00ae0184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00ae0184 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b3fb5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
+ 00b3fb5c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0184 bytes 735644f9
+ 00b3fb5c bytes 735641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218552da57e395cfcd0d5c8812cdc0d5"></a>

### [`00ae04ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md) → [`00b3fe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe84.md) _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md) · 呼出先 1件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md)
- 新版 呼出元 1件 [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) · 呼出先 1件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b3fe94",
      "value": [
        "leaf",
        "ram:b3fe98:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ae04bc",
      "value": [
        "leaf",
        "ram:ae04c0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3fe90",
      "incomplete_value": false,
      "site": "00b3fe94",
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
      "definition_site": "00ae04b8",
      "incomplete_value": false,
      "site": "00ae04bc",
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
      "00b3fe90",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00b3fe94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ae04c0"
      ]
    ]
  ],
  "added": [
    [
      "00b3fe90",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00b3fe94",
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

- 旧版 [`00ae04bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md#insn-00ae04bc) · [`00ae04b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md#insn-00ae04b4) · [`00ae04b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04ac.md#insn-00ae04b8)
- 新版 [`00b3fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe84.md#insn-00b3fe94) · [`00b3fe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe84.md#insn-00b3fe8c) · [`00b3fe90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe84.md#insn-00b3fe90)

~~~diff
- 00ae04bc ["INT_ADD", "register:40f0:8", ["const:ae04bc:8", "const:4:8"]]
- 00ae04bc ["CALL", null, ["ram:ae04c0:8"]]
+ 00b3fe94 ["INT_ADD", "register:40f0:8", ["const:b3fe94:8", "const:4:8"]]
+ 00b3fe94 ["CALL", null, ["ram:b3fe98:8"]]
- 00ae04bc bytes 01000094
+ 00b3fe94 bytes 01000094
- 00ae04b4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00b3fe8c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00ae04b4 bytes 20befff0
+ 00b3fe8c bytes c0bbff90
- 00ae04b8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00ae04b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae04b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae04b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b3fe90 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00b3fe90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b3fe90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b3fe90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae04b8 bytes 00740e91
+ 00b3fe90 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e92bdd8edc0f7ef6a73673f66e6fbfa"></a>

### [`00ae0540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0540.md) → [`00b3ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff18.md) _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdded0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdded0.md)
- 新版 呼出元 1件 [`00c5a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a930.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a930.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0540.md#insn-00ae0540) · [`00ae055c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0540.md#insn-00ae055c) · [`00ae0568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0540.md#insn-00ae0568)
- 新版 [`00b3ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff18.md#insn-00b3ff18) · [`00b3ff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff18.md#insn-00b3ff34) · [`00b3ff40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff18.md#insn-00b3ff40)

~~~diff
- 00ae0540 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae0540 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b3ff18 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b3ff18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae0540 bytes e10100b4
+ 00b3ff18 bytes e10100b4
- 00ae055c ["INT_ADD", "register:40f0:8", ["const:ae055c:8", "const:4:8"]]
- 00ae055c ["CALL", null, ["callee:00c5a930:8"]]
+ 00b3ff34 ["INT_ADD", "register:40f0:8", ["const:b3ff34:8", "const:4:8"]]
+ 00b3ff34 ["CALL", null, ["callee:00c5a930:8"]]
- 00ae055c bytes 5df60394
+ 00b3ff34 bytes 7f6a0494
- 00ae0568 ["INT_ADD", "register:40f0:8", ["const:ae0568:8", "const:4:8"]]
- 00ae0568 ["CALL", null, ["callee:00c5a930:8"]]
+ 00b3ff40 ["INT_ADD", "register:40f0:8", ["const:b3ff40:8", "const:4:8"]]
+ 00b3ff40 ["CALL", null, ["callee:00c5a930:8"]]
- 00ae0568 bytes 5af60394
+ 00b3ff40 bytes 7c6a0494
~~~


<a id="compare-b23f1b25dee97645bfd551f2e27b4392"></a>

### [`00ae0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md) → [`00b3ff58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff58.md) FUN_00b3ff58

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ae0174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0174.md) · 呼出先 3件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bdde80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00b3fb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb4c.md) · 呼出先 3件 [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5a8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b3ff64",
      "incomplete_value": false,
      "site": "00b3ff68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:bf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae058c",
      "incomplete_value": false,
      "site": "00ae0590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:24e:8"
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
      "00b3ff64",
      "PARAM",
      [
        "storage",
        "0029524e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3ff64",
      "PARAM",
      [
        "storage",
        "002a4bf3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae0590) · [`00ae0588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae0588) · [`00ae058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0580.md#insn-00ae058c)
- 新版 [`00b3ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff58.md#insn-00b3ff68) · [`00b3ff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff58.md#insn-00b3ff60) · [`00b3ff64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff58.md#insn-00b3ff64)

~~~diff
- 00ae0590 ["INT_ADD", "register:40f0:8", ["const:ae0590:8", "const:4:8"]]
- 00ae0590 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b3ff68 ["INT_ADD", "register:40f0:8", ["const:b3ff68:8", "const:4:8"]]
+ 00b3ff68 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00ae0590 bytes 2cf60394
+ 00b3ff68 bytes 4e6a0494
- 00ae0588 ["COPY", "register:4000:8", ["const:295000:8"]]
+ 00b3ff60 ["COPY", "register:4000:8", ["const:2a4000:8"]]
- 00ae0588 bytes a0bdffb0
+ 00b3ff60 bytes 20bbffb0
- 00ae058c ["COPY", "tmp:0:8", ["const:24e:8"]]
- 00ae058c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae058c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae058c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b3ff64 ["COPY", "tmp:0:8", ["const:bf3:8"]]
+ 00b3ff64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b3ff64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b3ff64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae058c bytes 00380991
+ 00b3ff64 bytes 00cc2f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c116a99f89c7ddcfca54d36d77d5606"></a>

### [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md) → [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) _INIT_277

採用 · 移動量 `+0x5f9d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ae0070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0070.md) [`00ae00a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae00a4.md) [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b3fa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md) [`00b3fa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md) [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md)

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
      "definition_site": "00b3ffa4",
      "incomplete_value": false,
      "site": "00b3ffa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "definition_site": "00b3ffa4",
      "incomplete_value": false,
      "site": "00b3ffa4",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
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
            "const:53d:8"
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
      "definition_site": "00b3ffa4",
      "incomplete_value": false,
      "site": "00b3ffa4",
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
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:f08:8"
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
      "definition_site": "00ae05cc",
      "incomplete_value": false,
      "site": "00ae05cc",
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
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "00b3ff94",
      "PARAM",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ffa4",
      "WRITE",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ffa4",
      "DATA",
      [
        "storage",
        "0029853d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b3ff94",
      "PARAM",
      [
        "storage",
        "01124f08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ffa4",
      "WRITE",
      [
        "storage",
        "01124f08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ffa4",
      "DATA",
      [
        "storage",
        "002a8290",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05ac) · [`00ae05b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05b0) · [`00ae05b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae05ac.md#insn-00ae05b4)
- 新版 [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ff84) · [`00b3ff88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ff88) · [`00b3ff8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ff8c)

~~~diff
- 00ae05ac ["COPY", "register:4000:8", ["const:10a0000:8"]]
+ 00b3ff84 ["COPY", "register:4000:8", ["const:1124000:8"]]
- 00ae05ac bytes 002e0090
+ 00b3ff84 bytes 202f00b0
- 00ae05b0 ["COPY", "register:4040:8", ["const:298000:8"]]
+ 00b3ff88 ["COPY", "register:4040:8", ["const:2a8000:8"]]
- 00ae05b0 bytes c8bdff90
+ 00b3ff88 bytes 48bbffb0
- 00ae05b4 ["COPY", "register:4048:8", ["const:ae0000:8"]]
+ 00b3ff8c ["COPY", "register:4048:8", ["const:b3f000:8"]]
- 00ae05b4 bytes 09000090
+ 00b3ff8c bytes 09000090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09db45712888dfac23c272f8af3e471a"></a>

### [`00ae061c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md) → [`00b3fff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fff4.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40020",
      "incomplete_value": true,
      "site": "00b40020",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0648",
      "incomplete_value": true,
      "site": "00ae0648",
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
            "const:70:8"
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
      "definition_site": "00b40008",
      "incomplete_value": true,
      "site": "00b40008",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0630",
      "incomplete_value": true,
      "site": "00ae0630",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b40010",
      "incomplete_value": false,
      "site": "00b40018",
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
            "const:fd3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0638",
      "incomplete_value": false,
      "site": "00ae0640",
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
      "00b40004",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40010",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00b40020",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40004",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40010",
      "PARAM",
      [
        "storage",
        "002a6fd3",
        null,
        "string"
      ]
    ],
    [
      "00b40020",
      "WRITE",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae0640) · [`00ae0648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae0648) · [`00ae0628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae061c.md#insn-00ae0628)
- 新版 [`00b40018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fff4.md#insn-00b40018) · [`00b40020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fff4.md#insn-00b40020) · [`00b40000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fff4.md#insn-00b40000)

~~~diff
- 00ae0640 ["INT_ADD", "register:40f0:8", ["const:ae0640:8", "const:4:8"]]
- 00ae0640 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40018 ["INT_ADD", "register:40f0:8", ["const:b40018:8", "const:4:8"]]
+ 00b40018 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0640 bytes 94f60394
+ 00b40018 bytes be6a0494
- 00ae0648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
- 00ae0648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40020 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f30:8"]]
+ 00b40020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0648 bytes 603a00f9
+ 00b40020 bytes 609a07f9
- 00ae0628 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40000 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0628 bytes 132e0090
+ 00b40000 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37263473e053b4dd6df2237174021676"></a>

### [`00ae065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md) → [`00b40034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40034.md) _ZN8firebase9analytics9analytics10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ae068c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40064"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b40048",
      "incomplete_value": true,
      "site": "00b40048",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0670",
      "incomplete_value": true,
      "site": "00ae0670",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b40044",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae0690"
      ]
    ],
    [
      "unmatched:00ae067c",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40044",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40068"
      ]
    ],
    [
      "00b40054",
      "PARAM",
      [
        "storage",
        "002a6fd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae0684) · [`00ae068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae068c) · [`00ae069c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae065c.md#insn-00ae069c)

~~~diff
- 00ae0684 ["INT_ADD", "register:40f0:8", ["const:ae0684:8", "const:4:8"]]
- 00ae0684 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0684 bytes 83f60394
- 00ae068c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
- 00ae068c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae068c bytes 603a00f9
- 00ae069c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae069c ["RETURN", null, ["register:0:8"]]
- 00ae069c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d123cbf738214d2d37a94a9411a6f447"></a>

### [`00ae06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md) → [`00b40078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40078.md) _ZN8firebase9analytics9analytics10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae06a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae06a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae06a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae06a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae06a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40088",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40078",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4007c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40088",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae06a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06a0) · [`00ae06a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06a4) · [`00ae06b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae06a0.md#insn-00ae06b4)
- 新版 [`00b4008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40078.md#insn-00b4008c)

~~~diff
- 00ae06a0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae06a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae06a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae06a0 bytes f30f1ef8
- 00ae06a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae06a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae06a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae06a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae06a4 bytes fd7b01a9
- 00ae06b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae06b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b4008c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4008c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae06b4 bytes 080100b5
+ 00b4008c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2132f96edc7c7d94cdf65cf43f58fb"></a>

### [`00ae075c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md) → [`00b40134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40134.md) _ZN8firebase9analytics9analytics12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 14.29% / 新版 14.29%

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
      "site": "00ae0798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae07b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40170"
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
      "00b40148",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40154",
      "READ",
      [
        "storage",
        "010a0078",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4015c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae079c"
      ]
    ]
  ],
  "added": [
    [
      "00b40148",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40154",
      "READ",
      [
        "storage",
        "01124f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4015c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40174"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae0798) · [`00ae07a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae07a0) · [`00ae07b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae075c.md#insn-00ae07b4)

~~~diff
- 00ae0798 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae0798 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae0798 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:78:8"]]
- 00ae0798 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae0798 bytes bfe20139
- 00ae07a0 ["INT_ADD", "register:40f0:8", ["const:ae07a0:8", "const:4:8"]]
- 00ae07a0 ["CALL", null, ["callee:00c5ab60:8"]]
- 00ae07a0 bytes 50f60394
- 00ae07b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae07b4 ["INT_ADD", "register:40f0:8", ["const:ae07b4:8", "const:4:8"]]
- 00ae07b4 ["CALLIND", null, ["register:0:8"]]
- 00ae07b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f0720611cc276c582632a88a4ae1201"></a>

### [`00ae07cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md) → [`00b401a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b401a4.md) _ZN8firebase9analytics9analytics14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae080c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b401e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae07e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae07e0",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae07e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b401e8"
      ]
    ],
    [
      "unmatched:00ae07f0",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b401b8",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b401c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b401e8"
      ]
    ],
    [
      "00b401c8",
      "PARAM",
      [
        "storage",
        "002a6fd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae07e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae07e8) · [`00ae0804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae0804) · [`00ae080c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae07cc.md#insn-00ae080c)
- 新版 [`00b401dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b401a4.md#insn-00b401dc)

~~~diff
- 00ae07e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae07e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae07e8 bytes 410100b5
- 00ae0804 ["INT_ADD", "register:40f0:8", ["const:ae0804:8", "const:4:8"]]
- 00ae0804 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b401dc ["INT_ADD", "register:40f0:8", ["const:b401dc:8", "const:4:8"]]
+ 00b401dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0804 bytes 23f60394
+ 00b401dc bytes 4d6a0494
- 00ae080c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
- 00ae080c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae080c bytes 803a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3872217d84b6b96956f475d91229daae"></a>

### [`00ae0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md) → [`00b40250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40250.md) _ZN8firebase9analytics9analytics13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ae08b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40290"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0894"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae088c",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae0894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40294"
      ]
    ],
    [
      "unmatched:00ae089c",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40264",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4026c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40294"
      ]
    ],
    [
      "00b40274",
      "PARAM",
      [
        "storage",
        "002a6fd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae0894) · [`00ae08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae08b0) · [`00ae08b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae08b8)
- 新版 [`00b40288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40250.md#insn-00b40288)

~~~diff
- 00ae0894 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae0894 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae0894 bytes 410100b5
- 00ae08b0 ["INT_ADD", "register:40f0:8", ["const:ae08b0:8", "const:4:8"]]
- 00ae08b0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40288 ["INT_ADD", "register:40f0:8", ["const:b40288:8", "const:4:8"]]
+ 00b40288 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae08b0 bytes f8f50394
+ 00b40288 bytes 226a0494
- 00ae08b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
- 00ae08b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae08b8 bytes 803a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1186136fecd875b580179297fd2d4fb"></a>

### [`00ae0924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md) → [`00b402fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402fc.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40328",
      "incomplete_value": true,
      "site": "00b40328",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0950",
      "incomplete_value": true,
      "site": "00ae0950",
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
            "const:e0:8"
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
      "definition_site": "00b40310",
      "incomplete_value": true,
      "site": "00b40310",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0938",
      "incomplete_value": true,
      "site": "00ae0938",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4031c",
      "incomplete_value": false,
      "site": "00b40320",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0944",
      "incomplete_value": false,
      "site": "00ae0948",
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
            "const:e49:8"
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
      "00b4030c",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4031c",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00b40328",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4030c",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4031c",
      "PARAM",
      [
        "storage",
        "002b250a",
        null,
        "string"
      ]
    ],
    [
      "00b40328",
      "WRITE",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0948) · [`00ae0950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0950) · [`00ae0930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0930)
- 新版 [`00b40320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402fc.md#insn-00b40320) · [`00b40328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402fc.md#insn-00b40328) · [`00b40308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402fc.md#insn-00b40308)

~~~diff
- 00ae0948 ["INT_ADD", "register:40f0:8", ["const:ae0948:8", "const:4:8"]]
- 00ae0948 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40320 ["INT_ADD", "register:40f0:8", ["const:b40320:8", "const:4:8"]]
+ 00b40320 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0948 bytes d2f50394
+ 00b40320 bytes fc690494
- 00ae0950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
- 00ae0950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fa0:8"]]
+ 00b40328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0950 bytes 607200f9
+ 00b40328 bytes 60d207f9
- 00ae0930 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40308 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0930 bytes 132e0090
+ 00b40308 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eaea1eb422c04ee800b9781c2784fd7"></a>

### [`00ae0964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md) → [`00b4033c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4033c.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40368",
      "incomplete_value": true,
      "site": "00b40368",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0990",
      "incomplete_value": true,
      "site": "00ae0990",
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
            "const:e0:8"
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
      "definition_site": "00b40350",
      "incomplete_value": true,
      "site": "00b40350",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0978",
      "incomplete_value": true,
      "site": "00ae0978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b40358",
      "incomplete_value": false,
      "site": "00b40360",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0980",
      "incomplete_value": false,
      "site": "00ae0988",
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
            "const:e49:8"
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
      "00b4034c",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40358",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00b40368",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4034c",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40358",
      "PARAM",
      [
        "storage",
        "002b250a",
        null,
        "string"
      ]
    ],
    [
      "00b40368",
      "WRITE",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0988) · [`00ae0990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0990) · [`00ae0970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0970)
- 新版 [`00b40360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4033c.md#insn-00b40360) · [`00b40368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4033c.md#insn-00b40368) · [`00b40348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4033c.md#insn-00b40348)

~~~diff
- 00ae0988 ["INT_ADD", "register:40f0:8", ["const:ae0988:8", "const:4:8"]]
- 00ae0988 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40360 ["INT_ADD", "register:40f0:8", ["const:b40360:8", "const:4:8"]]
+ 00b40360 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0988 bytes c2f50394
+ 00b40360 bytes ec690494
- 00ae0990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
- 00ae0990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40368 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fa0:8"]]
+ 00b40368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0990 bytes 607200f9
+ 00b40368 bytes 60d207f9
- 00ae0970 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40348 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0970 bytes 132e0090
+ 00b40348 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b54549ea13139b9a96bddab2497bb0ae"></a>

### [`00ae09a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md) → [`00b4037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4037c.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b403ac",
      "incomplete_value": true,
      "site": "00b403ac",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09d4",
      "incomplete_value": true,
      "site": "00ae09d4",
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
            "const:e0:8"
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
      "definition_site": "00b40390",
      "incomplete_value": true,
      "site": "00b40390",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09b8",
      "incomplete_value": true,
      "site": "00ae09b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4039c",
      "incomplete_value": false,
      "site": "00b403a4",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09c4",
      "incomplete_value": false,
      "site": "00ae09cc",
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
            "const:e49:8"
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
      "00b4038c",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4039c",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00b403ac",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4038c",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4039c",
      "PARAM",
      [
        "storage",
        "002b250a",
        null,
        "string"
      ]
    ],
    [
      "00b403ac",
      "WRITE",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae09cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09cc) · [`00ae09d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09d4) · [`00ae09b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09b0)
- 新版 [`00b403a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4037c.md#insn-00b403a4) · [`00b403ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4037c.md#insn-00b403ac) · [`00b40388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4037c.md#insn-00b40388)

~~~diff
- 00ae09cc ["INT_ADD", "register:40f0:8", ["const:ae09cc:8", "const:4:8"]]
- 00ae09cc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b403a4 ["INT_ADD", "register:40f0:8", ["const:b403a4:8", "const:4:8"]]
+ 00b403a4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae09cc bytes b1f50394
+ 00b403a4 bytes db690494
- 00ae09d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
- 00ae09d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b403ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fa0:8"]]
+ 00b403ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae09d4 bytes 607200f9
+ 00b403ac bytes 60d207f9
- 00ae09b0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40388 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae09b0 bytes 132e0090
+ 00b40388 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc1bce60ca2388388f2605a53f0200f5"></a>

### [`00ae09e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md) → [`00b403c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b403c0.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae09e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae09ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae09ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae09e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae09ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b403d0",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b403c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b403c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b403d0",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae09e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae09e8) · [`00ae09ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae09ec) · [`00ae09fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae09fc)
- 新版 [`00b403d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b403c0.md#insn-00b403d4)

~~~diff
- 00ae09e8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae09e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae09e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae09e8 bytes f30f1ef8
- 00ae09ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae09ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae09ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae09ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae09ec bytes fd7b01a9
- 00ae09fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae09fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b403d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b403d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae09fc bytes 080100b5
+ 00b403d4 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92535c82e0174abf90626a182bd50b6a"></a>

### [`00ae0a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md) → [`00b40410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40410.md) _ZN8firebase9analytics22analytics_consent_type15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b40468",
      "incomplete_value": true,
      "site": "00b40468",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0a90",
      "incomplete_value": true,
      "site": "00ae0a90",
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
            "const:e8:8"
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
      "definition_site": "00b40444",
      "incomplete_value": true,
      "site": "00b40450",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1124000:8"
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
      "definition_site": "00ae0a6c",
      "incomplete_value": true,
      "site": "00ae0a78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:e0:8"
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
      "00b40424",
      "READ",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40444",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40468",
      "WRITE",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40424",
      "READ",
      [
        "storage",
        "01124fa8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40444",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40468",
      "WRITE",
      [
        "storage",
        "01124fa8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a78) · [`00ae0a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a90) · [`00ae0a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a48)
- 新版 [`00b40450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40410.md#insn-00b40450) · [`00b40468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40410.md#insn-00b40468) · [`00b40420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40410.md#insn-00b40420)

~~~diff
- 00ae0a78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0a78 ["INT_ADD", "register:40f0:8", ["const:ae0a78:8", "const:4:8"]]
- 00ae0a78 ["CALLIND", null, ["register:0:8"]]
+ 00b40450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40450 ["INT_ADD", "register:40f0:8", ["const:b40450:8", "const:4:8"]]
+ 00b40450 ["CALLIND", null, ["register:0:8"]]
- 00ae0a78 bytes 00013fd6
+ 00b40450 bytes 00013fd6
- 00ae0a90 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae0a90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e8:8"]]
- 00ae0a90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b40468 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b40468 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:fa8:8"]]
+ 00b40468 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae0a90 bytes a0a20339
+ 00b40468 bytes a0a23e39
- 00ae0a48 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b40420 ["COPY", "register:40a8:8", ["const:1124000:8"]]
- 00ae0a48 bytes 152e0090
+ 00b40420 bytes 352f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07ec33ef1618915a54e1f17162002480"></a>

### [`00ae0aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md) → [`00b4047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4047c.md) _ZN8firebase9analytics22analytics_consent_type12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b404b8",
      "incomplete_value": true,
      "site": "00b404b8",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0ae0",
      "incomplete_value": true,
      "site": "00ae0ae0",
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
            "const:e8:8"
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
      "definition_site": "00b404d8",
      "incomplete_value": true,
      "site": "00b404d8",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b00",
      "incomplete_value": true,
      "site": "00ae0b00",
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
            "const:e0:8"
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
      "definition_site": "00b40494",
      "incomplete_value": true,
      "site": "00b40494",
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
      "definition_site": "00ae0abc",
      "incomplete_value": true,
      "site": "00ae0abc",
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
      "00b40490",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4049c",
      "READ",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b404b8",
      "WRITE",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40490",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4049c",
      "READ",
      [
        "storage",
        "01124fa8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b404b8",
      "WRITE",
      [
        "storage",
        "01124fa8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0ae0) · [`00ae0afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0afc) · [`00ae0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0b00)
- 新版 [`00b404b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4047c.md#insn-00b404b8) · [`00b404d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4047c.md#insn-00b404d4) · [`00b404d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4047c.md#insn-00b404d8)

~~~diff
- 00ae0ae0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae0ae0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae0ae0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e8:8"]]
- 00ae0ae0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b404b8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b404b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b404b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:fa8:8"]]
+ 00b404b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae0ae0 bytes bfa20339
+ 00b404b8 bytes bfa23e39
- 00ae0afc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0afc ["INT_ADD", "register:40f0:8", ["const:ae0afc:8", "const:4:8"]]
- 00ae0afc ["CALLIND", null, ["register:0:8"]]
+ 00b404d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b404d4 ["INT_ADD", "register:40f0:8", ["const:b404d4:8", "const:4:8"]]
+ 00b404d4 ["CALLIND", null, ["register:0:8"]]
- 00ae0afc bytes 00013fd6
+ 00b404d4 bytes 00013fd6
- 00ae0b00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
- 00ae0b00 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae0b00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b404d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fa0:8"]]
+ 00b404d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b404d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae0b00 bytes 9f7200f9
+ 00b404d8 bytes 9fd207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f60f0702fb3c9fc7c6d4dedca29b2e41"></a>

### [`00ae0b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md) → [`00b404ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b404ec.md) _ZN8firebase9analytics22analytics_consent_type14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4052c",
      "incomplete_value": true,
      "site": "00b4052c",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b54",
      "incomplete_value": true,
      "site": "00ae0b54",
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
            "const:e0:8"
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
      "definition_site": "00b40508",
      "incomplete_value": true,
      "site": "00b40508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b30",
      "incomplete_value": true,
      "site": "00ae0b30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b40510",
      "incomplete_value": false,
      "site": "00b40524",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b38",
      "incomplete_value": false,
      "site": "00ae0b4c",
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
            "const:e49:8"
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
      "00b40500",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40510",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00b4052c",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40500",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40510",
      "PARAM",
      [
        "storage",
        "002b250a",
        null,
        "string"
      ]
    ],
    [
      "00b4052c",
      "WRITE",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b4c) · [`00ae0b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b54) · [`00ae0b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b20)
- 新版 [`00b40524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b404ec.md#insn-00b40524) · [`00b4052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b404ec.md#insn-00b4052c) · [`00b404f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b404ec.md#insn-00b404f8)

~~~diff
- 00ae0b4c ["INT_ADD", "register:40f0:8", ["const:ae0b4c:8", "const:4:8"]]
- 00ae0b4c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40524 ["INT_ADD", "register:40f0:8", ["const:b40524:8", "const:4:8"]]
+ 00b40524 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0b4c bytes 51f50394
+ 00b40524 bytes 7b690494
- 00ae0b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
- 00ae0b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4052c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fa0:8"]]
+ 00b4052c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0b54 bytes 807200f9
+ 00b4052c bytes 80d207f9
- 00ae0b20 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b404f8 ["COPY", "register:40a0:8", ["const:1124000:8"]]
- 00ae0b20 bytes 142e0090
+ 00b404f8 bytes 342f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e9c6fe085a569c727e51d37a24369f4"></a>

### [`00ae0b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md) → [`00b4055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md) _ZN8firebase9analytics22analytics_consent_type11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40578",
      "incomplete_value": false,
      "site": "00b4057c",
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
      "definition_site": "00ae0ba0",
      "incomplete_value": false,
      "site": "00ae0ba4",
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
      "definition_site": "00b40588",
      "incomplete_value": true,
      "site": "00b40594",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0bb0",
      "incomplete_value": true,
      "site": "00ae0bbc",
      "value": [
        "LOAD",
        "8",
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
      "00b40578",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b40588",
      "DATA",
      [
        "storage",
        "010a00f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b40578",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b40588",
      "DATA",
      [
        "storage",
        "01124fb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0ba4) · [`00ae0b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0b9c) · [`00ae0ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0ba0)
- 新版 [`00b4057c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b4057c) · [`00b40574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b40574) · [`00b40578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b40578)

~~~diff
- 00ae0ba4 ["INT_ADD", "register:40f0:8", ["const:ae0ba4:8", "const:4:8"]]
- 00ae0ba4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4057c ["INT_ADD", "register:40f0:8", ["const:b4057c:8", "const:4:8"]]
+ 00b4057c ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae0ba4 bytes 77f50394
+ 00b4057c bytes a1690494
- 00ae0b9c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b40574 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae0b9c bytes c0bdff90
+ 00b40574 bytes 40bbff90
- 00ae0ba0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae0ba0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0ba0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0ba0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b40578 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b40578 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40578 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40578 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0ba0 bytes 001c1591
+ 00b40578 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f26e7fb4567b171856f3ba5405da650b"></a>

### [`00ae0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md) → [`00b40598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40598.md) _ZN8firebase9analytics22analytics_consent_type13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b405d8",
      "incomplete_value": true,
      "site": "00b405d8",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c00",
      "incomplete_value": true,
      "site": "00ae0c00",
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
            "const:e0:8"
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
      "definition_site": "00b405b4",
      "incomplete_value": true,
      "site": "00b405b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0bdc",
      "incomplete_value": true,
      "site": "00ae0bdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b405bc",
      "incomplete_value": false,
      "site": "00b405d0",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0be4",
      "incomplete_value": false,
      "site": "00ae0bf8",
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
            "const:e49:8"
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
      "00b405ac",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b405bc",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00b405d8",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b405ac",
      "READ",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b405bc",
      "PARAM",
      [
        "storage",
        "002b250a",
        null,
        "string"
      ]
    ],
    [
      "00b405d8",
      "WRITE",
      [
        "storage",
        "01124fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0bf8) · [`00ae0c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0c00) · [`00ae0bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0bcc)
- 新版 [`00b405d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40598.md#insn-00b405d0) · [`00b405d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40598.md#insn-00b405d8) · [`00b405a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40598.md#insn-00b405a4)

~~~diff
- 00ae0bf8 ["INT_ADD", "register:40f0:8", ["const:ae0bf8:8", "const:4:8"]]
- 00ae0bf8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b405d0 ["INT_ADD", "register:40f0:8", ["const:b405d0:8", "const:4:8"]]
+ 00b405d0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0bf8 bytes 26f50394
+ 00b405d0 bytes 50690494
- 00ae0c00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
- 00ae0c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b405d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fa0:8"]]
+ 00b405d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0c00 bytes 807200f9
+ 00b405d8 bytes 80d207f9
- 00ae0bcc ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b405a4 ["COPY", "register:40a0:8", ["const:1124000:8"]]
- 00ae0bcc bytes 142e0090
+ 00b405a4 bytes 342f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ea18d22e6c760484135e24f3423a05"></a>

### [`00ae0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md) → [`00b40608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md) _ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40624",
      "incomplete_value": false,
      "site": "00b40628",
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
      "definition_site": "00ae0c4c",
      "incomplete_value": false,
      "site": "00ae0c50",
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
      "definition_site": "00b40634",
      "incomplete_value": true,
      "site": "00b40640",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0c5c",
      "incomplete_value": true,
      "site": "00ae0c68",
      "value": [
        "LOAD",
        "8",
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
      "00b40624",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b40634",
      "DATA",
      [
        "storage",
        "010a00f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40624",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b40634",
      "DATA",
      [
        "storage",
        "01124fb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c50) · [`00ae0c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c48) · [`00ae0c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c4c)
- 新版 [`00b40628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b40628) · [`00b40620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b40620) · [`00b40624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b40624)

~~~diff
- 00ae0c50 ["INT_ADD", "register:40f0:8", ["const:ae0c50:8", "const:4:8"]]
- 00ae0c50 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b40628 ["INT_ADD", "register:40f0:8", ["const:b40628:8", "const:4:8"]]
+ 00b40628 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae0c50 bytes 4cf50394
+ 00b40628 bytes 76690494
- 00ae0c48 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b40620 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae0c48 bytes c0bdffb0
+ 00b40620 bytes 40bbffb0
- 00ae0c4c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae0c4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0c4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0c4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b40624 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b40624 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40624 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40624 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0c4c bytes 00c81791
+ 00b40624 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1890046e009b4dcc1c2a32e6e37a3cb0"></a>

### [`00ae0c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md) → [`00b40644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b40670",
      "incomplete_value": true,
      "site": "00b40670",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c98",
      "incomplete_value": true,
      "site": "00ae0c98",
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
            "const:118:8"
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
      "definition_site": "00b40658",
      "incomplete_value": true,
      "site": "00b40658",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c80",
      "incomplete_value": true,
      "site": "00ae0c80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b40664",
      "incomplete_value": false,
      "site": "00b40668",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c8c",
      "incomplete_value": false,
      "site": "00ae0c90",
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
            "const:d9:8"
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
      "00b40654",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40664",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00b40670",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40654",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40664",
      "PARAM",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b40670",
      "WRITE",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c90) · [`00ae0c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c98) · [`00ae0c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c78)
- 新版 [`00b40668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40668) · [`00b40670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40670) · [`00b40650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40650)

~~~diff
- 00ae0c90 ["INT_ADD", "register:40f0:8", ["const:ae0c90:8", "const:4:8"]]
- 00ae0c90 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40668 ["INT_ADD", "register:40f0:8", ["const:b40668:8", "const:4:8"]]
+ 00b40668 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0c90 bytes 00f50394
+ 00b40668 bytes 2a690494
- 00ae0c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
- 00ae0c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40670 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd8:8"]]
+ 00b40670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0c98 bytes 608e00f9
+ 00b40670 bytes 60ee07f9
- 00ae0c78 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40650 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0c78 bytes 132e0090
+ 00b40650 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a778c078ad8886dbcf6a368b80c8b370"></a>

### [`00ae0cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md) → [`00b40684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b406b0",
      "incomplete_value": true,
      "site": "00b406b0",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cd8",
      "incomplete_value": true,
      "site": "00ae0cd8",
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
            "const:118:8"
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
      "definition_site": "00b40698",
      "incomplete_value": true,
      "site": "00b40698",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cc0",
      "incomplete_value": true,
      "site": "00ae0cc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b406a0",
      "incomplete_value": false,
      "site": "00b406a8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cc8",
      "incomplete_value": false,
      "site": "00ae0cd0",
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
            "const:d9:8"
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
      "00b40694",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00b406a0",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00b406b0",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40694",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b406a0",
      "PARAM",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b406b0",
      "WRITE",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cd0) · [`00ae0cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cd8) · [`00ae0cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cb8)
- 新版 [`00b406a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b406a8) · [`00b406b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b406b0) · [`00b40690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b40690)

~~~diff
- 00ae0cd0 ["INT_ADD", "register:40f0:8", ["const:ae0cd0:8", "const:4:8"]]
- 00ae0cd0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b406a8 ["INT_ADD", "register:40f0:8", ["const:b406a8:8", "const:4:8"]]
+ 00b406a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0cd0 bytes f0f40394
+ 00b406a8 bytes 1a690494
- 00ae0cd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
- 00ae0cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b406b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd8:8"]]
+ 00b406b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0cd8 bytes 608e00f9
+ 00b406b0 bytes 60ee07f9
- 00ae0cb8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b40690 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0cb8 bytes 132e0090
+ 00b40690 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34f07e1a2bb4733b522fea02750643b6"></a>

### [`00ae0cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md) → [`00b406c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b406c4.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b406f4",
      "incomplete_value": true,
      "site": "00b406f4",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d1c",
      "incomplete_value": true,
      "site": "00ae0d1c",
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
            "const:118:8"
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
      "definition_site": "00b406d8",
      "incomplete_value": true,
      "site": "00b406d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d00",
      "incomplete_value": true,
      "site": "00ae0d00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b406e4",
      "incomplete_value": false,
      "site": "00b406ec",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d0c",
      "incomplete_value": false,
      "site": "00ae0d14",
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
            "const:d9:8"
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
      "00b406d4",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00b406e4",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00b406f4",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b406d4",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b406e4",
      "PARAM",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b406f4",
      "WRITE",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0d14) · [`00ae0d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0d1c) · [`00ae0cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0cf8)
- 新版 [`00b406ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b406c4.md#insn-00b406ec) · [`00b406f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b406c4.md#insn-00b406f4) · [`00b406d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b406c4.md#insn-00b406d0)

~~~diff
- 00ae0d14 ["INT_ADD", "register:40f0:8", ["const:ae0d14:8", "const:4:8"]]
- 00ae0d14 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b406ec ["INT_ADD", "register:40f0:8", ["const:b406ec:8", "const:4:8"]]
+ 00b406ec ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0d14 bytes dff40394
+ 00b406ec bytes 09690494
- 00ae0d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
- 00ae0d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b406f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd8:8"]]
+ 00b406f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0d1c bytes 608e00f9
+ 00b406f4 bytes 60ee07f9
- 00ae0cf8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b406d0 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00ae0cf8 bytes 132e0090
+ 00b406d0 bytes 332f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58d5aac3e5b7da70d3e517b989742e7"></a>

### [`00ae0d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md) → [`00b40708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40708.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40738"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4071c",
      "incomplete_value": true,
      "site": "00b4071c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d44",
      "incomplete_value": true,
      "site": "00ae0d44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b40718",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae0d4c",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae0d60",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40718",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40724",
      "PARAM",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b40738",
      "WRITE",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d44) · [`00ae0d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d58) · [`00ae0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d60)
- 新版 [`00b4071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40708.md#insn-00b4071c) · [`00b40730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40708.md#insn-00b40730)

~~~diff
- 00ae0d44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae0d44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4071c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4071c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae0d44 bytes 080100b5
+ 00b4071c bytes 080100b5
- 00ae0d58 ["INT_ADD", "register:40f0:8", ["const:ae0d58:8", "const:4:8"]]
- 00ae0d58 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b40730 ["INT_ADD", "register:40f0:8", ["const:b40730:8", "const:4:8"]]
+ 00b40730 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae0d58 bytes cef40394
+ 00b40730 bytes f8680494
- 00ae0d60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
- 00ae0d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0d60 bytes 608e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4faa495c3f84563f084d68d238053de"></a>

### [`00ae0e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md) → [`00b40834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40834.md) _ZN8firebase9analytics24analytics_consent_status14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0e60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0e5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0e70",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40834",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40838",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40848",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e5c) · [`00ae0e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e60) · [`00ae0e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e78)

~~~diff
- 00ae0e5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae0e5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae0e5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae0e5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae0e5c bytes f44fbea9
- 00ae0e60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae0e60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae0e60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae0e60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0e60 bytes fd7b01a9
- 00ae0e78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae0e78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae0e78 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e9bf263b3617a00736ca423cb1e632"></a>

### [`00ae0f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md) → [`00b408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408e0.md) _ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ae0f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0f0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0f1c",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b408e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b408e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b408f4",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f08) · [`00ae0f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f0c) · [`00ae0f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f24)

~~~diff
- 00ae0f08 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae0f08 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae0f08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae0f08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae0f08 bytes f44fbea9
- 00ae0f0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae0f0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae0f0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae0f0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0f0c bytes fd7b01a9
- 00ae0f24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae0f24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae0f24 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edddad562b7fc9bb76c93ec1dd407899"></a>

### [`00ae0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md) → [`00b40950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40950.md) _ZN8firebase9analytics24analytics_consent_status10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4096c",
      "incomplete_value": false,
      "site": "00b40970",
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
      "definition_site": "00ae0f94",
      "incomplete_value": false,
      "site": "00ae0f98",
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
      "definition_site": "00b4097c",
      "incomplete_value": true,
      "site": "00b40988",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0fa4",
      "incomplete_value": true,
      "site": "00ae0fb0",
      "value": [
        "LOAD",
        "8",
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
      "00b4096c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4097c",
      "DATA",
      [
        "storage",
        "010a0130",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4096c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4097c",
      "DATA",
      [
        "storage",
        "01124ff0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0f98) · [`00ae0f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0f90) · [`00ae0f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0f94)
- 新版 [`00b40970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40950.md#insn-00b40970) · [`00b40968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40950.md#insn-00b40968) · [`00b4096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40950.md#insn-00b4096c)

~~~diff
- 00ae0f98 ["INT_ADD", "register:40f0:8", ["const:ae0f98:8", "const:4:8"]]
- 00ae0f98 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b40970 ["INT_ADD", "register:40f0:8", ["const:b40970:8", "const:4:8"]]
+ 00b40970 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae0f98 bytes 7af40394
+ 00b40970 bytes a4680494
- 00ae0f90 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b40968 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae0f90 bytes c0bdffb0
+ 00b40968 bytes 40bbffb0
- 00ae0f94 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae0f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4096c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4096c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4096c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4096c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0f94 bytes 00c81791
+ 00b4096c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-517049b5fa8ee97bbbf2b74f04404cc0"></a>

### [`00ae0fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md) → [`00b4098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4098c.md) _ZN8firebase9analytics10InitializeERKNS_3AppE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb10.md) · 呼出先 13件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde60.md) [`00bdde90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde90.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md)
- 新版 呼出元 1件 [`00c5a560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a560.md) · 呼出先 13件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) [`00c5a8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8c0.md) [`00c5a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8f0.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.62% / 新版 47.62%

CFGの説明率　旧版 2.04% / 新版 2.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1070"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae10c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0fd0",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae0fd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b409dc"
      ]
    ],
    [
      "unmatched:00ae0fdc",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b409a8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b409ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b409dc"
      ]
    ],
    [
      "00b409b4",
      "READ",
      [
        "storage",
        "00c9b2a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae0fd4) · [`00ae101c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae101c) · [`00ae104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae104c)
- 新版 [`00b409f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4098c.md#insn-00b409f4)

~~~diff
- 00ae0fd4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae0fd4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae0fd4 bytes 880100b4
- 00ae101c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae101c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b409f4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b409f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae101c bytes 880000b4
+ 00b409f4 bytes 880000b4
- 00ae104c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae104c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ae104c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-258efff505fb54b1dcd0a4e338a1cf4e"></a>

### [`00ae12a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae12a8.md) → [`00b40c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40c80.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7a0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.41% / 新版 56.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae12f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae12fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae12fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae12f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae12fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1300",
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
      "00b40cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b40cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b40cd8",
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

- 旧版 [`00ae12f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae12a8.md#insn-00ae12f8) · [`00ae12fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae12a8.md#insn-00ae12fc) · [`00ae1300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae12a8.md#insn-00ae1300)

~~~diff
- 00ae12f8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ae12f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ae12f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae12f8 bytes ab831ef8
- 00ae12fc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ae12fc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ae12fc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ae12fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae12fc bytes a9a33da9
- 00ae1300 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00ae1300 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ae1300 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae1300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1300 bytes acab3ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3620f5f576a282709c85a3bb7d6c02e8"></a>

### [`00ae1344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1344.md) → [`00b40d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md) _ZN8firebase9analytics8internal13IsInitializedEv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdde80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5a8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b40d28",
      "incomplete_value": true,
      "site": "00b40d2c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae1350",
      "incomplete_value": true,
      "site": "00ae1354",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
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
      "00b40d20",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40d20",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1344.md#insn-00ae1344) · [`00ae1348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1344.md#insn-00ae1348)
- 新版 [`00b40d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md#insn-00b40d1c) · [`00b40d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md#insn-00b40d20)

~~~diff
- 00ae1344 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b40d1c ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae1344 bytes e82d00f0
+ 00b40d1c bytes 282f00b0
- 00ae1348 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae1348 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40d20 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b40d20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae1348 bytes 08a140f9
+ 00b40d20 bytes 080140f9
~~~


<a id="compare-4b04bf7c44ebdd24274b4842e22b587c"></a>

### [`00ae1358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md) → [`00b40d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d30.md) _ZN8firebase9analytics9TerminateEv

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) · 呼出先 7件 [`00bdde70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde70.md) [`00bddea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddea0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5a540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a540.md) · 呼出先 7件 [`00c5a8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8d0.md) [`00c5a900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a900.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.53% / 新版 25.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae13b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae13dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae136c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae1370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e84"
      ]
    ],
    [
      "unmatched:00ae1374",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac80"
      ]
    ]
  ],
  "added": [
    [
      "00b40d44",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e84"
      ]
    ],
    [
      "00b40d4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae1370) · [`00ae1374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae1374) · [`00ae1388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae1388)

~~~diff
- 00ae1370 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ae1370 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00ae1370 bytes e00900b4
- 00ae1374 ["INT_ADD", "register:40f0:8", ["const:ae1374:8", "const:4:8"]]
- 00ae1374 ["CALL", null, ["callee:00c5ac80:8"]]
- 00ae1374 bytes a3f30394
- 00ae1388 ["INT_ADD", "register:40f0:8", ["const:ae1388:8", "const:4:8"]]
- 00ae1388 ["CALL", null, ["callee:00c5ab00:8"]]
- 00ae1388 bytes 3ef30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48fdc9ff892bdb30c58bf4363bc22f7b"></a>

### [`00ae14d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md) → [`00b40ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40ea8.md) _ZN8firebase9analytics29SetAnalyticsCollectionEnabledEb

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b40ebc",
      "incomplete_value": true,
      "site": "00b40ebc",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae14e4",
      "incomplete_value": true,
      "site": "00ae14e4",
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
      "definition_site": "00b40ed4",
      "incomplete_value": true,
      "site": "00b40ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae14fc",
      "incomplete_value": true,
      "site": "00ae150c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b40ed8",
      "incomplete_value": true,
      "site": "00b40ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1124000:8"
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
      "definition_site": "00ae1500",
      "incomplete_value": true,
      "site": "00ae150c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:80:8"
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
      "00b40eb8",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ed4",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ed8",
      "READ",
      [
        "storage",
        "010a0080",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40eb8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ed4",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ed8",
      "READ",
      [
        "storage",
        "01124f40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae150c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae150c) · [`00ae14dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae14dc) · [`00ae14e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae14e0)
- 新版 [`00b40ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40ea8.md#insn-00b40ee4) · [`00b40eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40ea8.md#insn-00b40eb4) · [`00b40eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40ea8.md#insn-00b40eb8)

~~~diff
- 00ae150c ["INT_ADD", "register:40f0:8", ["const:ae150c:8", "const:4:8"]]
- 00ae150c ["CALL", null, ["callee:00574cac:8"]]
+ 00b40ee4 ["INT_ADD", "register:40f0:8", ["const:b40ee4:8", "const:4:8"]]
+ 00b40ee4 ["CALL", null, ["callee:00574cac:8"]]
- 00ae150c bytes 42c2e997
+ 00b40ee4 bytes 72cfe897
- 00ae14dc ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b40eb4 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae14dc bytes e82d00f0
+ 00b40eb4 bytes 282f00b0
- 00ae14e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae14e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40eb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b40eb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae14e0 bytes 08a140f9
+ 00b40eb8 bytes 080140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e42b51e491d3c9d47069bc44c38a8ff0"></a>

### [`00ae1534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md) → [`00b40f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40f0c.md) _ZN8firebase9analytics10SetConsentERKNSt6__ndk13mapINS0_11ConsentTypeENS0_13ConsentStatusENS1_4lessIS3_EENS1_9allocatorINS1_4pairIKS3_S4_EEE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5aae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 56.90% / 新版 56.90%

CFGの説明率　旧版 14.04% / 新版 13.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1558"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1640"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae167c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae1554",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae1558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40f98"
      ]
    ],
    [
      "00b40f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae1844"
      ]
    ]
  ],
  "added": [
    [
      "00b40f2c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40f30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40f98"
      ]
    ],
    [
      "00b40f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4121c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae1558) · [`00ae1578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae1578) · [`00ae1624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae1624)
- 新版 [`00b40f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40f0c.md#insn-00b40f50)

~~~diff
- 00ae1558 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae1558 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae1558 bytes 480300b4
- 00ae1578 ["INT_ADD", "register:40f0:8", ["const:ae1578:8", "const:4:8"]]
- 00ae1578 ["CALL", null, ["callee:00c5abb0:8"]]
+ 00b40f50 ["INT_ADD", "register:40f0:8", ["const:b40f50:8", "const:4:8"]]
+ 00b40f50 ["CALL", null, ["callee:00c5abb0:8"]]
- 00ae1578 bytes eef20394
+ 00b40f50 bytes 18670494
- 00ae1624 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1624 ["INT_ADD", "register:40f0:8", ["const:ae1624:8", "const:4:8"]]
- 00ae1624 ["CALLIND", null, ["register:0:8"]]
- 00ae1624 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6733e9d2092019f95efe070dc55b6b7f"></a>

### [`00ae19f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae19f8.md) → [`00b413d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b413d0.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcl

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae19f8.md#insn-00ae1a20) · [`00ae1a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae19f8.md#insn-00ae1a2c) · [`00ae1a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae19f8.md#insn-00ae1a44)
- 新版 [`00b413f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b413d0.md#insn-00b413f8) · [`00b41404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b413d0.md#insn-00b41404) · [`00b4141c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b413d0.md#insn-00b4141c)

~~~diff
- 00ae1a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1a20 ["INT_ADD", "register:40f0:8", ["const:ae1a20:8", "const:4:8"]]
- 00ae1a20 ["CALLIND", null, ["register:0:8"]]
+ 00b413f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b413f8 ["INT_ADD", "register:40f0:8", ["const:b413f8:8", "const:4:8"]]
+ 00b413f8 ["CALLIND", null, ["register:0:8"]]
- 00ae1a20 bytes 00013fd6
+ 00b413f8 bytes 00013fd6
- 00ae1a2c ["INT_ADD", "register:40f0:8", ["const:ae1a2c:8", "const:4:8"]]
- 00ae1a2c ["CALL", null, ["callee:00c5ab90:8"]]
+ 00b41404 ["INT_ADD", "register:40f0:8", ["const:b41404:8", "const:4:8"]]
+ 00b41404 ["CALL", null, ["callee:00c5ab90:8"]]
- 00ae1a2c bytes b9f10394
+ 00b41404 bytes e3650494
- 00ae1a44 ["INT_ADD", "register:40f0:8", ["const:ae1a44:8", "const:4:8"]]
- 00ae1a44 ["CALL", null, ["callee:00574cac:8"]]
+ 00b4141c ["INT_ADD", "register:40f0:8", ["const:b4141c:8", "const:4:8"]]
+ 00b4141c ["CALL", null, ["callee:00574cac:8"]]
- 00ae1a44 bytes f4c0e997
+ 00b4141c bytes 24cee897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cda7994b1db565ea3c0666c8280bdc66"></a>

### [`00ae1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1a70.md) → [`00b41448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41448.md) _ZN8firebase9analytics20AddArrayListToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1a74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae1a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1a74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1a78",
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
      "00b41448",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4144c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b41450",
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

- 旧版 [`00ae1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1a70.md#insn-00ae1a70) · [`00ae1a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1a70.md#insn-00ae1a74) · [`00ae1a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1a70.md#insn-00ae1a78)

~~~diff
- 00ae1a70 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae1a70 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae1a70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae1a70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae1a70 bytes f657bda9
- 00ae1a74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae1a74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae1a74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae1a74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1a74 bytes f44f01a9
- 00ae1a78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae1a78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae1a78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae1a78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1a78 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbba48d58a64164467af6cef96db2bd"></a>

### [`00ae1ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1ae8.md) → [`00b414c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b414c0.md) _ZN8firebase9analytics17AddBundleToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1aec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae1ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1af0",
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
      "00b414c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b414c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b414c8",
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

- 旧版 [`00ae1ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1ae8.md#insn-00ae1ae8) · [`00ae1aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1ae8.md#insn-00ae1aec) · [`00ae1af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1ae8.md#insn-00ae1af0)

~~~diff
- 00ae1ae8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae1ae8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae1ae8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae1ae8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae1ae8 bytes f657bda9
- 00ae1aec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae1aec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae1aec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae1aec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1aec bytes f44f01a9
- 00ae1af0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae1af0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae1af0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae1af0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1af0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2879c4e5e3b12e3c1982de8655c88ad3"></a>

### [`00ae1b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1b60.md) → [`00b41538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41538.md) _ZN8firebase9analytics23VectorOfMapsToArrayListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1b0.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde030.md)
- 新版 呼出元 1件 [`00c5ac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac30.md) · 呼出先 9件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5aab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b41548"
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
      "unmatched:00ae1b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b415a8",
      "PARAM",
      [
        "storage",
        "00295297",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae1be0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41620"
      ]
    ]
  ],
  "added": [
    [
      "00b41548",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b415a8",
      "PARAM",
      [
        "storage",
        "002a4c3c",
        null,
        "string"
      ]
    ],
    [
      "00b415b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41620"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1b60.md#insn-00ae1b70) · [`00ae1be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1b60.md#insn-00ae1be0) · [`00ae1c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1b60.md#insn-00ae1c04)
- 新版 [`00b415dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41538.md#insn-00b415dc)

~~~diff
- 00ae1b70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae1b70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae1b70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ae1b70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1b70 bytes fd7b04a9
- 00ae1be0 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00ae1be0 bytes 40030054
- 00ae1c04 ["INT_ADD", "register:40f0:8", ["const:ae1c04:8", "const:4:8"]]
- 00ae1c04 ["CALL", null, ["callee:00c5ac10:8"]]
+ 00b415dc ["INT_ADD", "register:40f0:8", ["const:b415dc:8", "const:4:8"]]
+ 00b415dc ["CALL", null, ["callee:00c5ac10:8"]]
- 00ae1c04 bytes 63f10394
+ 00b415dc bytes 8d650494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc0787fb6f786ef4e3420621a1188891"></a>

### [`00ae1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1e20.md) → [`00b417f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b417f8.md) _ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1a0.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) [`00bddcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcd0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 1件 [`00c5ac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac20.md) · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md) [`00c5a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 60.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae1f84",
      "incomplete_value": true,
      "site": "00ae1f94",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00ae1e54",
      "DATA",
      [
        "storage",
        "002f59ed",
        "switchD_00ae1e6c::switchdataD_002f59ed",
        "byte"
      ]
    ],
    [
      "unmatched:00ae1ec8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab90"
      ]
    ],
    [
      "unmatched:00ae20fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00574cac"
      ]
    ]
  ],
  "added": [
    [
      "00b4182c",
      "DATA",
      [
        "storage",
        "0030b559",
        "switchD_00b41844::switchdataD_0030b559",
        "byte"
      ]
    ],
    [
      "00b418a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab90"
      ]
    ],
    [
      "00b41ad4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00574cac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1e20.md#insn-00ae1ebc) · [`00ae1ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1e20.md#insn-00ae1ec8) · [`00ae1f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1e20.md#insn-00ae1f94)
- 新版 [`00b4196c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b417f8.md#insn-00b4196c)

~~~diff
- 00ae1ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1ebc ["INT_ADD", "register:40f0:8", ["const:ae1ebc:8", "const:4:8"]]
- 00ae1ebc ["CALLIND", null, ["register:0:8"]]
- 00ae1ebc bytes 00013fd6
- 00ae1ec8 ["INT_ADD", "register:40f0:8", ["const:ae1ec8:8", "const:4:8"]]
- 00ae1ec8 ["CALL", null, ["callee:00c5ab90:8"]]
- 00ae1ec8 bytes 92f00394
- 00ae1f94 ["INT_ADD", "register:40f0:8", ["const:ae1f94:8", "const:4:8"]]
- 00ae1f94 ["CALL", null, ["callee:00574cac:8"]]
+ 00b4196c ["INT_ADD", "register:40f0:8", ["const:b4196c:8", "const:4:8"]]
+ 00b4196c ["CALL", null, ["callee:00574cac:8"]]
- 00ae1f94 bytes a0bfe997
+ 00b4196c bytes d0cce897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b9c38d11c060c5909b6a45f8418c2f8"></a>

### [`00ae2150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md) → [`00b41b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41b28.md) _ZN8firebase9analytics8LogEventEPKcS2_S2_

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 72.16% / 新版 72.16%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae216c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b41b44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41b68",
      "incomplete_value": false,
      "site": "00b41b6c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
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
      "unmatched:00ae2168",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae216c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41c90"
      ]
    ],
    [
      "unmatched:00ae2248",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41b40",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41b44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41c90"
      ]
    ],
    [
      "00b41c20",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae216c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae216c) · [`00ae2194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae2194) · [`00ae21bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae21bc)
- 新版 [`00b41b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41b28.md#insn-00b41b6c)

~~~diff
- 00ae216c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae216c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ae216c bytes 680a00b4
- 00ae2194 ["INT_ADD", "register:40f0:8", ["const:ae2194:8", "const:4:8"]]
- 00ae2194 ["CALL", null, ["callee:00c5ab90:8"]]
+ 00b41b6c ["INT_ADD", "register:40f0:8", ["const:b41b6c:8", "const:4:8"]]
+ 00b41b6c ["CALL", null, ["callee:00c5ab90:8"]]
- 00ae2194 bytes dfef0394
+ 00b41b6c bytes 09640494
- 00ae21bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae21bc ["INT_ADD", "register:40f0:8", ["const:ae21bc:8", "const:4:8"]]
- 00ae21bc ["CALLIND", null, ["register:0:8"]]
- 00ae21bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21f9b7e422bdb77f464ce50e0eca6afd"></a>

### [`00ae22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md) → [`00b41cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41cac.md) _ZN8firebase9analytics8LogEventEPKcS2_d

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.53% / 新版 89.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae22f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b41cc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41d28",
      "incomplete_value": true,
      "site": "00b41d3c",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae22ec",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae22f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41de8"
      ]
    ],
    [
      "unmatched:00ae23a0",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41cc4",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41cc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41de8"
      ]
    ],
    [
      "00b41d78",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae22f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae22f0) · [`00ae2364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae2364) · [`00ae23b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae23b8)
- 新版 [`00b41d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41cac.md#insn-00b41d3c) · [`00b41d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41cac.md#insn-00b41d90)

~~~diff
- 00ae22f0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae22f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae22f0 bytes 080900b4
- 00ae2364 ["INT_ADD", "register:40f0:8", ["const:ae2364:8", "const:4:8"]]
- 00ae2364 ["CALL", null, ["callee:00574cac:8"]]
+ 00b41d3c ["INT_ADD", "register:40f0:8", ["const:b41d3c:8", "const:4:8"]]
+ 00b41d3c ["CALL", null, ["callee:00574cac:8"]]
- 00ae2364 bytes acbee997
+ 00b41d3c bytes dccbe897
- 00ae23b8 ["INT_ADD", "register:40f0:8", ["const:ae23b8:8", "const:4:8"]]
- 00ae23b8 ["CALL", null, ["callee:00574cac:8"]]
+ 00b41d90 ["INT_ADD", "register:40f0:8", ["const:b41d90:8", "const:4:8"]]
+ 00b41d90 ["CALL", null, ["callee:00574cac:8"]]
- 00ae23b8 bytes 97bee997
+ 00b41d90 bytes c7cbe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b89fe815e284b7b608d4068cd0fc16e"></a>

### [`00ae242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md) → [`00b41e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41e04.md) _ZN8firebase9analytics8LogEventEPKcS2_l

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1e0.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 1件 [`00c5ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac60.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2448"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b41e20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b41e28",
      "incomplete_value": true,
      "site": "00b41e34",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
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
      "unmatched:00ae2444",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41f40"
      ]
    ],
    [
      "unmatched:00ae24f8",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41e1c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41e20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41f40"
      ]
    ],
    [
      "00b41ed0",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae2448) · [`00ae245c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae245c) · [`00ae2470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae2470)
- 新版 [`00b41e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41e04.md#insn-00b41e34) · [`00b41e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41e04.md#insn-00b41e48)

~~~diff
- 00ae2448 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae2448 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae2448 bytes 080900b4
- 00ae245c ["INT_ADD", "register:40f0:8", ["const:ae245c:8", "const:4:8"]]
- 00ae245c ["CALL", null, ["callee:00c5ac80:8"]]
+ 00b41e34 ["INT_ADD", "register:40f0:8", ["const:b41e34:8", "const:4:8"]]
+ 00b41e34 ["CALL", null, ["callee:00c5ac80:8"]]
- 00ae245c bytes 69ef0394
+ 00b41e34 bytes 93630494
- 00ae2470 ["INT_ADD", "register:40f0:8", ["const:ae2470:8", "const:4:8"]]
- 00ae2470 ["CALL", null, ["callee:00c5ab90:8"]]
+ 00b41e48 ["INT_ADD", "register:40f0:8", ["const:b41e48:8", "const:4:8"]]
+ 00b41e48 ["CALL", null, ["callee:00c5ab90:8"]]
- 00ae2470 bytes 28ef0394
+ 00b41e48 bytes 52630494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d27553b9adba0f3ca5fa041f06314d7"></a>

### [`00ae2598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2598.md) → [`00b41f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41f70.md) _ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm

採用 · 移動量 `+0x5f9d8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bddb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb40.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 1件 [`00c5a590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a590.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 33.33% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae25b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b41f90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae25c0",
      "incomplete_value": true,
      "site": "00ae25cc",
      "value": [
        "live",
        "register:4040:8"
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
      "unmatched:00ae25b4",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae25b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b420c4"
      ]
    ],
    [
      "00b42024",
      "PARAM",
      [
        "storage",
        "002ad2a8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b41f8c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41f90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b420c4"
      ]
    ],
    [
      "00b42024",
      "PARAM",
      [
        "storage",
        "002be500",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae25b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2598.md#insn-00ae25b8) · [`00ae25cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2598.md#insn-00ae25cc) · [`00ae2690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2598.md#insn-00ae2690)
- 新版 [`00b41fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41f70.md#insn-00b41fa4) · [`00b42068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41f70.md#insn-00b42068)

~~~diff
- 00ae25b8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae25b8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ae25b8 bytes a80900b4
- 00ae25cc ["INT_ADD", "register:40f0:8", ["const:ae25cc:8", "const:4:8"]]
- 00ae25cc ["CALL", null, ["callee:00c5ac80:8"]]
+ 00b41fa4 ["INT_ADD", "register:40f0:8", ["const:b41fa4:8", "const:4:8"]]
+ 00b41fa4 ["CALL", null, ["callee:00c5ac80:8"]]
- 00ae25cc bytes 0def0394
+ 00b41fa4 bytes 37630494
- 00ae2690 ["INT_ADD", "register:40f0:8", ["const:ae2690:8", "const:4:8"]]
- 00ae2690 ["CALL", null, ["callee:00574cac:8"]]
+ 00b42068 ["INT_ADD", "register:40f0:8", ["const:b42068:8", "const:4:8"]]
+ 00b42068 ["CALL", null, ["callee:00574cac:8"]]
- 00ae2690 bytes e1bde997
+ 00b42068 bytes 11cbe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b05dd15c454f422748610dea23a47e"></a>

### [`00ae2720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md) → [`00b4239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4239c.md) _ZN8firebase9analytics25SetDefaultEventParametersEPKNS0_9ParameterEm

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1c0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)
- 新版 呼出元 1件 [`00c5ac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac40.md) · 呼出先 10件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 18.52% / 新版 19.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b423bc",
      "incomplete_value": true,
      "site": "00b423bc",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2740",
      "incomplete_value": true,
      "site": "00ae2740",
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
      "site": "00ae27b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae28a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b423b8",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae285c"
      ]
    ],
    [
      "00b4240c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae285c"
      ]
    ]
  ],
  "added": [
    [
      "00b423b8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b424d8"
      ]
    ],
    [
      "00b4240c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b424d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae2740) · [`00ae27b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae27b0) · [`00ae27c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae27c4)
- 新版 [`00b423bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4239c.md#insn-00b423bc) · [`00b42440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4239c.md#insn-00b42440)

~~~diff
- 00ae2740 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae2740 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b423bc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b423bc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae2740 bytes a80500b4
+ 00b423bc bytes a80500b4
- 00ae27b0 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00ae27b0 bytes a0060054
- 00ae27c4 ["INT_ADD", "register:40f0:8", ["const:ae27c4:8", "const:4:8"]]
- 00ae27c4 ["CALL", null, ["callee:00c5ac20:8"]]
+ 00b42440 ["INT_ADD", "register:40f0:8", ["const:b42440:8", "const:4:8"]]
+ 00b42440 ["CALL", null, ["callee:00c5ac20:8"]]
- 00ae27c4 bytes 77ee0394
+ 00b42440 bytes f8610494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff11509a74b86edc134b61367bacf781"></a>

### [`00ae28e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae28e0.md) → [`00b4255c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4255c.md) _ZN8firebase9analytics25SetDefaultEventParametersERKNSt6__ndk16vectorINS0_9ParameterENS1_9allocatorIS3_EEEE

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac40.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae28f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac40"
      ]
    ]
  ],
  "added": [
    [
      "00b4256c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac40"
      ]
    ]
  ]
}
~~~


<a id="compare-1475cf5974301ca3c63f2bb03653138b"></a>

### [`00ae2910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2910.md) → [`00b4258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4258c.md) _ZN8firebase9analytics52InitiateOnDeviceConversionMeasurementWithPhoneNumberEPKc

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42594",
      "incomplete_value": true,
      "site": "00b42594",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2918",
      "incomplete_value": true,
      "site": "00ae2918",
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
      "00b42590",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425a0",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b42590",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425a0",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2910.md#insn-00ae2910) · [`00ae2914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2910.md#insn-00ae2914) · [`00ae2920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2910.md#insn-00ae2920)
- 新版 [`00b4258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4258c.md#insn-00b4258c) · [`00b42590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4258c.md#insn-00b42590) · [`00b4259c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4258c.md#insn-00b4259c)

~~~diff
- 00ae2910 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b4258c ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae2910 bytes e82d00d0
+ 00b4258c bytes 082f00f0
- 00ae2914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae2914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42590 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b42590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2914 bytes 08a140f9
+ 00b42590 bytes 080140f9
- 00ae2920 ["COPY", "register:4000:8", ["const:293000:8"]]
+ 00b4259c ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 00ae2920 bytes 80bdffb0
+ 00b4259c bytes 00bbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b34db3cdd20f962cf818b038d72fdd1e"></a>

### [`00ae292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae292c.md) → [`00b425a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425a8.md) _ZN8firebase9analytics59InitiateOnDeviceConversionMeasurementWithHashedEmailAddressENSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b425b0",
      "incomplete_value": true,
      "site": "00b425b0",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2934",
      "incomplete_value": true,
      "site": "00ae2934",
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
      "00b425ac",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425bc",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b425ac",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425bc",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae292c.md#insn-00ae292c) · [`00ae2930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae292c.md#insn-00ae2930) · [`00ae293c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae292c.md#insn-00ae293c)
- 新版 [`00b425a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425a8.md#insn-00b425a8) · [`00b425ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425a8.md#insn-00b425ac) · [`00b425b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425a8.md#insn-00b425b8)

~~~diff
- 00ae292c ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b425a8 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae292c bytes e82d00d0
+ 00b425a8 bytes 082f00f0
- 00ae2930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae2930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b425ac ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b425ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2930 bytes 08a140f9
+ 00b425ac bytes 080140f9
- 00ae293c ["COPY", "register:4000:8", ["const:293000:8"]]
+ 00b425b8 ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 00ae293c bytes 80bdffb0
+ 00b425b8 bytes 00bbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9154a1776fb1db21ee80c0395f8c4fd8"></a>

### [`00ae2948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2948.md) → [`00b425c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425c4.md) _ZN8firebase9analytics58InitiateOnDeviceConversionMeasurementWithHashedPhoneNumberENSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b425cc",
      "incomplete_value": true,
      "site": "00b425cc",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2950",
      "incomplete_value": true,
      "site": "00ae2950",
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
      "00b425c8",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425d8",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b425c8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b425d8",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2948.md#insn-00ae2948) · [`00ae294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2948.md#insn-00ae294c) · [`00ae2958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2948.md#insn-00ae2958)
- 新版 [`00b425c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425c4.md#insn-00b425c4) · [`00b425c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425c4.md#insn-00b425c8) · [`00b425d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425c4.md#insn-00b425d4)

~~~diff
- 00ae2948 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b425c4 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae2948 bytes e82d00d0
+ 00b425c4 bytes 082f00f0
- 00ae294c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae294c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b425c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b425c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae294c bytes 08a140f9
+ 00b425c8 bytes 080140f9
- 00ae2958 ["COPY", "register:4000:8", ["const:293000:8"]]
+ 00b425d4 ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 00ae2958 bytes 80bdffb0
+ 00b425d4 bytes 00bbff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aad9412433e323b269611b4329a960f"></a>

### [`00ae2964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md) → [`00b425e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425e0.md) _ZN8firebase9analytics15SetUserPropertyEPKcS2_

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.23% / 新版 89.23%

CFGの説明率　旧版 69.23% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b425fc",
      "incomplete_value": true,
      "site": "00b425fc",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2980",
      "incomplete_value": true,
      "site": "00ae2980",
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
      "definition_site": "00b42670",
      "incomplete_value": true,
      "site": "00b42684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae29f4",
      "incomplete_value": true,
      "site": "00ae2a08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42674",
      "incomplete_value": true,
      "site": "00b42684",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1124000:8"
              ],
              [
                "leaf",
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae29f8",
      "incomplete_value": true,
      "site": "00ae2a08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b425f8",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42658",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00b42670",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b425f8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42658",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ],
    [
      "00b42670",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae2a08) · [`00ae2a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae2a28) · [`00ae2a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae2a40)
- 新版 [`00b42684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425e0.md#insn-00b42684) · [`00b426a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b425e0.md#insn-00b426a4)

~~~diff
- 00ae2a08 ["INT_ADD", "register:40f0:8", ["const:ae2a08:8", "const:4:8"]]
- 00ae2a08 ["CALL", null, ["callee:00574cac:8"]]
+ 00b42684 ["INT_ADD", "register:40f0:8", ["const:b42684:8", "const:4:8"]]
+ 00b42684 ["CALL", null, ["callee:00574cac:8"]]
- 00ae2a08 bytes 03bde997
+ 00b42684 bytes 8ac9e897
- 00ae2a28 ["INT_ADD", "register:40f0:8", ["const:ae2a28:8", "const:4:8"]]
- 00ae2a28 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b426a4 ["INT_ADD", "register:40f0:8", ["const:b426a4:8", "const:4:8"]]
+ 00b426a4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00ae2a28 bytes 06ed0394
+ 00b426a4 bytes 7f600494
- 00ae2a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae2a40 ["INT_ADD", "register:40f0:8", ["const:ae2a40:8", "const:4:8"]]
- 00ae2a40 ["CALLIND", null, ["register:0:8"]]
- 00ae2a40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75feee94418746c214365618554bd0d4"></a>

### [`00ae2a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md) → [`00b426e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b426e4.md) _ZN8firebase9analytics9SetUserIdEPKc

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb30.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5a580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a580.md) · 呼出先 5件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.25% / 新版 79.25%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2a6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae2a68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2a70",
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
      "00b426e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b426e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b426ec",
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

- 旧版 [`00ae2a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2a68) · [`00ae2a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2a6c) · [`00ae2a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2a70)

~~~diff
- 00ae2a68 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae2a68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae2a68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae2a68 bytes f50f1df8
- 00ae2a6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae2a6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae2a6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae2a6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2a6c bytes f44f01a9
- 00ae2a70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae2a70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae2a70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae2a70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2a70 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7800f902b7bb4b47761905077c7686a"></a>

### [`00ae2b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md) → [`00b427b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b427b8.md) _ZN8firebase9analytics25SetSessionTimeoutDurationEl

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb20.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 1件 [`00c5a570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a570.md) · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2b50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b427cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b427e4",
      "incomplete_value": true,
      "site": "00b427f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2b68",
      "incomplete_value": true,
      "site": "00ae2b78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:148:8"
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
      "unmatched:00ae2b4c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42808"
      ]
    ],
    [
      "unmatched:00ae2b68",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b427c8",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b427cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42808"
      ]
    ],
    [
      "00b427e4",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md#insn-00ae2b50) · [`00ae2b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md#insn-00ae2b78)
- 新版 [`00b427f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b427b8.md#insn-00b427f4) · [`00b427cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b427b8.md#insn-00b427cc)

~~~diff
- 00ae2b50 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae2b50 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae2b50 bytes e80100b4
- 00ae2b78 ["INT_ADD", "register:40f0:8", ["const:ae2b78:8", "const:4:8"]]
- 00ae2b78 ["CALL", null, ["callee:00574cac:8"]]
+ 00b427f4 ["INT_ADD", "register:40f0:8", ["const:b427f4:8", "const:4:8"]]
+ 00b427f4 ["CALL", null, ["callee:00574cac:8"]]
- 00ae2b78 bytes a7bce997
+ 00b427f4 bytes 2ec9e897
+ 00b427cc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b427cc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b427cc bytes e80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c49d8f392bdfac70bed410f4888576"></a>

### [`00ae2ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md) → [`00b4281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4281c.md) _ZN8firebase9analytics18ResetAnalyticsDataEv

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42830",
      "incomplete_value": true,
      "site": "00b42830",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae2bb4",
      "incomplete_value": true,
      "site": "00ae2bb4",
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
      "definition_site": "00b42840",
      "incomplete_value": true,
      "site": "00b4284c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2bc4",
      "incomplete_value": true,
      "site": "00ae2bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42844",
      "incomplete_value": true,
      "site": "00b4284c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1124000:8"
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
    "old": {
      "definition_site": "00ae2bc8",
      "incomplete_value": true,
      "site": "00ae2bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:b0:8"
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
      "00b4282c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42840",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42844",
      "READ",
      [
        "storage",
        "010a00b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4282c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42840",
      "READ",
      [
        "storage",
        "01125008",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42844",
      "READ",
      [
        "storage",
        "01124f70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bd0) · [`00ae2bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bac) · [`00ae2bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bb0)
- 新版 [`00b4284c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4281c.md#insn-00b4284c) · [`00b42828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4281c.md#insn-00b42828) · [`00b4282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b4281c.md#insn-00b4282c)

~~~diff
- 00ae2bd0 ["INT_ADD", "register:40f0:8", ["const:ae2bd0:8", "const:4:8"]]
- 00ae2bd0 ["CALL", null, ["callee:00574cac:8"]]
+ 00b4284c ["INT_ADD", "register:40f0:8", ["const:b4284c:8", "const:4:8"]]
+ 00b4284c ["CALL", null, ["callee:00574cac:8"]]
- 00ae2bd0 bytes 91bce997
+ 00b4284c bytes 18c9e897
- 00ae2bac ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b42828 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00ae2bac bytes e82d00d0
+ 00b42828 bytes 082f00f0
- 00ae2bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 00ae2bb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4282c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b4282c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2bb0 bytes 00a140f9
+ 00b4282c bytes 000140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eda5cd12c88764ac254988af2152686e"></a>

### [`00ae2c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md) → [`00b42888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42888.md) _ZN8firebase9analytics22GetAnalyticsInstanceIdEv

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00ae3374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3374.md) [`00ae3e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b43164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43164.md) [`00b43b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.29% / 新版 87.29%

CFGの説明率　旧版 22.73% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b428ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2c3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae2c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2c38",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2c3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae2d38"
      ]
    ]
  ],
  "added": [
    [
      "00b428ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b428b4",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b428b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b429b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2c30) · [`00ae2c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2c3c) · [`00ae2c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2c78)
- 新版 [`00b428f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42888.md#insn-00b428f4)

~~~diff
- 00ae2c30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ae2c30 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae2c30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae2c30 bytes a9831cf8
- 00ae2c3c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ae2c3c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae2c3c bytes e00700b4
- 00ae2c78 ["INT_ADD", "register:40f0:8", ["const:ae2c78:8", "const:4:8"]]
- 00ae2c78 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00b428f4 ["INT_ADD", "register:40f0:8", ["const:b428f4:8", "const:4:8"]]
+ 00b428f4 ["CALL", null, ["callee:00c5aa40:8"]]
- 00ae2c78 bytes d2ec0394
+ 00b428f4 bytes 53600494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de7d7856956d769ffa498c8488f3339"></a>

### [`00ae2e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md) → [`00b42adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42adc.md) _ZN8firebase9analytics32GetAnalyticsInstanceIdLastResultEv

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1d0.md) · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)
- 新版 呼出元 1件 [`00c5ac50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac50.md) · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 54.76% / 新版 54.76%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae2e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2e68",
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
      "00b42adc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b42ae0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b42ae4",
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

- 旧版 [`00ae2e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2e60) · [`00ae2e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2e64) · [`00ae2e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2e68)

~~~diff
- 00ae2e60 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae2e60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae2e60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae2e60 bytes f50f1df8
- 00ae2e64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae2e64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae2e64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae2e64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2e64 bytes f44f01a9
- 00ae2e68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae2e68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae2e68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae2e68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2e68 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f75932800d401251039eaf304f45aa1d"></a>

### [`00ae2fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md) → [`00b42c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42c50.md) _ZN8firebase9analytics12GetSessionIdEv

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00ae3a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md) [`00ae3e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e44.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 19件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b436c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md) [`00b43bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bc8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.19% / 新版 83.19%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3004"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b42c80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42ca8",
      "incomplete_value": true,
      "site": "00b42cac",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00ae3000",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae3004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42d58"
      ]
    ],
    [
      "unmatched:00ae301c",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b42c7c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42c80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42d58"
      ]
    ],
    [
      "00b42c98",
      "READ",
      [
        "storage",
        "00c9b2c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae3004) · [`00ae3030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae3030) · [`00ae3044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae3044)
- 新版 [`00b42cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42c50.md#insn-00b42cac)

~~~diff
- 00ae3004 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00ae3004 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae3004 bytes c90600b4
- 00ae3030 ["INT_ADD", "register:40f0:8", ["const:ae3030:8", "const:4:8"]]
- 00ae3030 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00b42cac ["INT_ADD", "register:40f0:8", ["const:b42cac:8", "const:4:8"]]
+ 00b42cac ["CALL", null, ["callee:00c5aa40:8"]]
- 00ae3030 bytes e4eb0394
+ 00b42cac bytes 655f0494
- 00ae3044 ["INT_ADD", "register:40f0:8", ["const:ae3044:8", "const:4:8"]]
- 00ae3044 ["CALL", null, ["ram:bddc40:8"]]
- 00ae3044 bytes ffea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c452d787e0ef0a6eed1417245a965dd"></a>

### [`00ae31fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae31fc.md) → [`00b42e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42e78.md) _ZN8firebase6FutureIlEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf50.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5a9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9c0.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

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
      "site": "00b42e98",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ae321c",
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
      "00b42e98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00b42e98",
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

- 旧版 [`00ae321c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae31fc.md#insn-00ae321c) · [`00ae3230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae31fc.md#insn-00ae3230) · [`00ae3244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae31fc.md#insn-00ae3244)
- 新版 [`00b42e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42e78.md#insn-00b42e98) · [`00b42eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42e78.md#insn-00b42eac) · [`00b42ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42e78.md#insn-00b42ec0)

~~~diff
- 00ae321c ["INT_ADD", "register:40f0:8", ["const:ae321c:8", "const:4:8"]]
- 00ae321c ["CALL", null, ["ram:bdde10:8"]]
+ 00b42e98 ["INT_ADD", "register:40f0:8", ["const:b42e98:8", "const:4:8"]]
+ 00b42e98 ["CALL", null, ["ram:c5a870:8"]]
- 00ae321c bytes fdea0394
+ 00b42e98 bytes 765e0494
- 00ae3230 ["INT_ADD", "register:40f0:8", ["const:ae3230:8", "const:4:8"]]
- 00ae3230 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b42eac ["INT_ADD", "register:40f0:8", ["const:b42eac:8", "const:4:8"]]
+ 00b42eac ["CALL", null, ["callee:00c5aa00:8"]]
- 00ae3230 bytes 54eb0394
+ 00b42eac bytes d55e0494
- 00ae3244 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae3244 ["INT_ADD", "register:40f0:8", ["const:ae3244:8", "const:4:8"]]
- 00ae3244 ["CALLIND", null, ["register:0:8"]]
+ 00b42ec0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b42ec0 ["INT_ADD", "register:40f0:8", ["const:b42ec0:8", "const:4:8"]]
+ 00b42ec0 ["CALLIND", null, ["register:0:8"]]
- 00ae3244 bytes 00013fd6
+ 00b42ec0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d631c637721b9150804d30dac2e09275"></a>

### [`00ae329c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md) → [`00b42f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42f18.md) _ZN8firebase9analytics22GetSessionIdLastResultEv

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `reordered`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8b0.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.81% / 新版 73.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae32ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b42f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42f34",
      "incomplete_value": true,
      "site": "00b42f34",
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
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00ae32b8",
      "incomplete_value": true,
      "site": "00ae32b8",
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
      "00b42f2c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae32e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00ae32f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00b42f2c",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00b42f70",
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

- 旧版 [`00ae32cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae32cc) · [`00ae32e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae32e4) · [`00ae32ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae32ec)
- 新版 [`00b42f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42f18.md#insn-00b42f48)

~~~diff
- 00ae32cc ["INT_ADD", "register:40f0:8", ["const:ae32cc:8", "const:4:8"]]
- 00ae32cc ["CALL", null, ["callee:00c5a600:8"]]
+ 00b42f48 ["INT_ADD", "register:40f0:8", ["const:b42f48:8", "const:4:8"]]
+ 00b42f48 ["CALL", null, ["callee:00c5a600:8"]]
- 00ae32cc bytes 55ea0394
+ 00b42f48 bytes ae5d0494
- 00ae32e4 ["INT_ADD", "register:40f0:8", ["const:ae32e4:8", "const:4:8"]]
- 00ae32e4 ["CALL", null, ["ram:bdde10:8"]]
- 00ae32e4 bytes cbea0394
- 00ae32ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00ae32ec ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae32ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae32ec bytes 7f1600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ddcee279b533c47592e46bad5042d74"></a>

### [`00ae3598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md) → [`00b43388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0x5fdf0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bddf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf00.md) · 呼出先 11件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5a960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a960.md) · 呼出先 11件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae35b8",
      "incomplete_value": true,
      "site": "00ae35cc",
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
            "const:8:8"
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
    "new": null,
    "old": {
      "definition_site": "00ae35d0",
      "incomplete_value": true,
      "site": "00ae35d8",
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
            "register:40a0:8"
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
      "definition_site": "00b433f4",
      "incomplete_value": false,
      "site": "00b433f8",
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
      "definition_site": "00ae3604",
      "incomplete_value": false,
      "site": "00ae3608",
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
      "unmatched:00ae3604",
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
      "00b433f4",
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

- 旧版 [`00ae35cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae35cc) · [`00ae35d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae35d8) · [`00ae3608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae3608)
- 新版 [`00b433bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b433bc) · [`00b433c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b433c8) · [`00b433f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43388.md#insn-00b433f8)

~~~diff
- 00ae35cc ["INT_ADD", "register:40f0:8", ["const:ae35cc:8", "const:4:8"]]
- 00ae35cc ["CALL", null, ["callee:00c5a600:8"]]
+ 00b433bc ["INT_ADD", "register:40f0:8", ["const:b433bc:8", "const:4:8"]]
+ 00b433bc ["CALL", null, ["callee:00c5a600:8"]]
- 00ae35cc bytes 95e90394
+ 00b433bc bytes 915c0494
- 00ae35d8 ["INT_ADD", "register:40f0:8", ["const:ae35d8:8", "const:4:8"]]
- 00ae35d8 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00b433c8 ["INT_ADD", "register:40f0:8", ["const:b433c8:8", "const:4:8"]]
+ 00b433c8 ["CALL", null, ["callee:00c5aa80:8"]]
- 00ae35d8 bytes 8aea0394
+ 00b433c8 bytes ae5d0494
- 00ae3608 ["INT_ADD", "register:40f0:8", ["const:ae3608:8", "const:4:8"]]
- 00ae3608 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b433f8 ["INT_ADD", "register:40f0:8", ["const:b433f8:8", "const:4:8"]]
+ 00b433f8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae3608 bytes deea0394
+ 00b433f8 bytes 025e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-180fbc75a63d23fab6ff96beb67e0912"></a>

### [`00ae36d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae36d8.md) → [`00b434c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0x5fdf0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md)
- 新版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 78.26% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae3770",
      "incomplete_value": true,
      "site": "00ae3780",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00ae376c",
      "incomplete_value": true,
      "site": "00ae3780",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "live",
            "register:4008:8"
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
    "new": null,
    "old": {
      "definition_site": "00ae3774",
      "incomplete_value": false,
      "site": "00ae3780",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 1,
    "slot": 5
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae36d8.md#insn-00ae3780) · [`00ae374c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae36d8.md#insn-00ae374c) · [`00ae3758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae36d8.md#insn-00ae3758)
- 新版 [`00b43570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b43570) · [`00b4353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b4353c) · [`00b43548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b434c8.md#insn-00b43548)

~~~diff
- 00ae3780 ["INT_ADD", "register:40f0:8", ["const:ae3780:8", "const:4:8"]]
- 00ae3780 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b43570 ["INT_ADD", "register:40f0:8", ["const:b43570:8", "const:4:8"]]
+ 00b43570 ["CALL", null, ["callee:00c5aca0:8"]]
- 00ae3780 bytes a8ea0394
+ 00b43570 bytes cc5d0494
- 00ae374c ["INT_ADD", "register:40f0:8", ["const:ae374c:8", "const:4:8"]]
- 00ae374c ["CALL", null, ["callee:00c57b40:8"]]
+ 00b4353c ["INT_ADD", "register:40f0:8", ["const:b4353c:8", "const:4:8"]]
+ 00b4353c ["CALL", null, ["callee:00c57b40:8"]]
- 00ae374c bytes 69de0394
+ 00b4353c bytes 81510494
- 00ae3758 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00ae3758 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ae3758 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ae3758 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b43548 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b43548 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b43548 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b43548 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ae3758 bytes 88010037
+ 00b43548 bytes 88010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8fd7a73baedf94ff510f994d845debb"></a>

### [`00ae37a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae37a0.md) → [`00b43590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0x5fdf0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde210.md)
- 新版 呼出元 1件 [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 15.15% / 新版 16.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae38ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae38ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4369c"
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
      "00b43668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae3890"
      ]
    ],
    [
      "unmatched:00ae388c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c00"
      ]
    ],
    [
      "unmatched:00ae3894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43690"
      ]
    ]
  ],
  "added": [
    [
      "00b43668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43680"
      ]
    ],
    [
      "00b4367c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c00"
      ]
    ],
    [
      "00b43684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae37a0.md#insn-00ae3818) · [`00ae3858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae37a0.md#insn-00ae3858) · [`00ae386c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae37a0.md#insn-00ae386c)
- 新版 [`00b43648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md#insn-00b43648) · [`00b4365c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43590.md#insn-00b4365c)

~~~diff
- 00ae3818 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ae3818 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ae3818 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ae3818 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ae3818 bytes 2831889a
- 00ae3858 ["INT_ADD", "register:40f0:8", ["const:ae3858:8", "const:4:8"]]
- 00ae3858 ["CALL", null, ["callee:00c57c00:8"]]
+ 00b43648 ["INT_ADD", "register:40f0:8", ["const:b43648:8", "const:4:8"]]
+ 00b43648 ["CALL", null, ["callee:00c57c00:8"]]
- 00ae3858 bytes 56de0394
+ 00b43648 bytes 6e510494
- 00ae386c ["INT_ADD", "register:40f0:8", ["const:ae386c:8", "const:4:8"]]
- 00ae386c ["CALL", null, ["callee:00c57c00:8"]]
+ 00b4365c ["INT_ADD", "register:40f0:8", ["const:b4365c:8", "const:4:8"]]
+ 00b4365c ["CALL", null, ["callee:00c57c00:8"]]
- 00ae386c bytes 51de0394
+ 00b4365c bytes 69510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-610d39faf76cf6e8ade6dd24f01fdc7b"></a>

### [`00ae38d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae38d8.md) → [`00b42ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42ff0.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0x5f718` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.32% / 新版 62.32%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae38dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae38dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae38e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae38dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae38e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae38e4",
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
      "00b42ff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b42ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b42ffc",
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

- 旧版 [`00ae38dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae38d8.md#insn-00ae38dc) · [`00ae38e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae38d8.md#insn-00ae38e0) · [`00ae38e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae38d8.md#insn-00ae38e4)

~~~diff
- 00ae38dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae38dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae38dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae38dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae38dc bytes f65702a9
- 00ae38e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae38e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae38e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ae38e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae38e0 bytes f44f03a9
- 00ae38e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae38e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae38e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ae38e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae38e4 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56409889c6ab8abb98e4b59686bff808"></a>

### [`00ae3a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md) → [`00b436c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md) FUN_00b436c8

採用 · 移動量 `+0x5fc7c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00ae2fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)
- 新版 呼出元 1件 [`00b42c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b42/00b42c50.md) · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.21% / 新版 87.21%

CFGの説明率　旧版 44.44% / 新版 34.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3ab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3b38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3ab4",
      "PARAM",
      [
        "storage",
        "002922d8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae3ad4",
      "PARAM",
      [
        "storage",
        "0029a6d7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae3b08",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b43730",
      "PARAM",
      [
        "storage",
        "002a18e9",
        null,
        "string"
      ]
    ],
    [
      "00b43750",
      "PARAM",
      [
        "storage",
        "002aa644",
        null,
        "string"
      ]
    ],
    [
      "00b43784",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3ab4) · [`00ae3adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3adc) · [`00ae3af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3af0)
- 新版 [`00b43758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md#insn-00b43758) · [`00b4376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b436c8.md#insn-00b4376c)

~~~diff
- 00ae3ab4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ae3ab4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ae3ab4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae3ab4 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00ae3ab4 bytes 0301969a
- 00ae3adc ["INT_ADD", "register:40f0:8", ["const:ae3adc:8", "const:4:8"]]
- 00ae3adc ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b43758 ["INT_ADD", "register:40f0:8", ["const:b43758:8", "const:4:8"]]
+ 00b43758 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00ae3adc bytes d9e80394
+ 00b43758 bytes 525c0494
- 00ae3af0 ["INT_ADD", "register:40f0:8", ["const:ae3af0:8", "const:4:8"]]
- 00ae3af0 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b4376c ["INT_ADD", "register:40f0:8", ["const:b4376c:8", "const:4:8"]]
+ 00b4376c ["CALL", null, ["callee:00c5aad0:8"]]
- 00ae3af0 bytes 58e90394
+ 00b4376c bytes d95c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c7367c26ce19c214bb460aa5485975"></a>

### [`00ae3bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md) → [`00b43840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf30.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5a990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a990.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.56% / 新版 83.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3c28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b438a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3c20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3c28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b438b4"
      ]
    ],
    [
      "unmatched:00ae3c30",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae3ca4",
      "READ",
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
      "00b438a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b438b4"
      ]
    ],
    [
      "00b438ac",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "00b43920",
      "READ",
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

- 旧版 [`00ae3c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3c20) · [`00ae3c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3c28) · [`00ae3c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3c34)
- 新版 [`00b438b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43840.md#insn-00b438b0)

~~~diff
- 00ae3c20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae3c20 ["INT_ADD", "register:40f0:8", ["const:ae3c20:8", "const:4:8"]]
- 00ae3c20 ["CALLIND", null, ["register:0:8"]]
- 00ae3c20 bytes 00013fd6
- 00ae3c28 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ae3c28 bytes 80000054
- 00ae3c34 ["INT_ADD", "register:40f0:8", ["const:ae3c34:8", "const:4:8"]]
- 00ae3c34 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b438b0 ["INT_ADD", "register:40f0:8", ["const:b438b0:8", "const:4:8"]]
+ 00b438b0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae3c34 bytes 53e90394
+ 00b438b0 bytes d45c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eedd466c2b9c48b5913a97689743e33b"></a>

### [`00ae3ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md) → [`00b43964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_i

採用 · 移動量 `+0x5fc7c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bddf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf10.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5a970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a970.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 22.22% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3d4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b439c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3d44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b439d8"
      ]
    ],
    [
      "unmatched:00ae3d54",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae3d44",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b439c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b439d8"
      ]
    ],
    [
      "00b439d0",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "00b439c0",
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

- 旧版 [`00ae3d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d44) · [`00ae3d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d4c) · [`00ae3d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d58)
- 新版 [`00b439d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43964.md#insn-00b439d4)

~~~diff
- 00ae3d44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae3d44 ["INT_ADD", "register:40f0:8", ["const:ae3d44:8", "const:4:8"]]
- 00ae3d44 ["CALLIND", null, ["register:0:8"]]
- 00ae3d44 bytes 00013fd6
- 00ae3d4c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00ae3d4c bytes 80000054
- 00ae3d58 ["INT_ADD", "register:40f0:8", ["const:ae3d58:8", "const:4:8"]]
- 00ae3d58 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b439d4 ["INT_ADD", "register:40f0:8", ["const:b439d4:8", "const:4:8"]]
+ 00b439d4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae3d58 bytes 0ae90394
+ 00b439d4 bytes 8b5c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e987c4dbe0b674abb249dc3adf56ffa2"></a>

### [`00ae3e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md) → [`00b43bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43bd4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf20.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5a980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a980.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3e50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3e54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3e50",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3e54",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3e58",
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
      "00b43bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b43bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b43bdc",
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

- 旧版 [`00ae3e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3e50) · [`00ae3e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3e54) · [`00ae3e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3e58)

~~~diff
- 00ae3e50 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ae3e50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ae3e50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae3e50 bytes f90f1bf8
- 00ae3e54 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae3e54 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae3e54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae3e54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3e54 bytes f85f01a9
- 00ae3e58 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae3e58 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae3e58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae3e58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3e58 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c08fcfd79a9ea7f22b649d6bd06baae"></a>

### [`00ae3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md) → [`00b43d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md) · 呼出先 8件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md) · 呼出先 8件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 86.89% / 新版 86.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b43d64",
      "incomplete_value": true,
      "site": "00b43d64",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "definition_site": "00ae3fe0",
      "incomplete_value": true,
      "site": "00ae3fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "site": "00b43d78",
      "value": [
        "leaf",
        "ram:c5a880:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ae3ff4",
      "value": [
        "leaf",
        "ram:bdde20:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43db4",
      "incomplete_value": false,
      "site": "00b43dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4030",
      "incomplete_value": false,
      "site": "00ae403c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:161:8"
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
      "00b43d58",
      "READ",
      [
        "storage",
        "00c1b8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b43d60",
      "READ",
      [
        "storage",
        "010a0158",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b43d78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde20"
      ]
    ]
  ],
  "added": [
    [
      "00b43d58",
      "READ",
      [
        "storage",
        "00c9b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b43d60",
      "READ",
      [
        "storage",
        "01125018",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b43d78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a880"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae3ff4) · [`00ae403c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae403c) · [`00ae4060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae4060)
- 新版 [`00b43d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43d78) · [`00b43dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43dc0) · [`00b43de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43d28.md#insn-00b43de4)

~~~diff
- 00ae3ff4 ["INT_ADD", "register:40f0:8", ["const:ae3ff4:8", "const:4:8"]]
- 00ae3ff4 ["CALL", null, ["ram:bdde20:8"]]
+ 00b43d78 ["INT_ADD", "register:40f0:8", ["const:b43d78:8", "const:4:8"]]
+ 00b43d78 ["CALL", null, ["ram:c5a880:8"]]
- 00ae3ff4 bytes 8be70394
+ 00b43d78 bytes c25a0494
- 00ae403c ["INT_ADD", "register:40f0:8", ["const:ae403c:8", "const:4:8"]]
- 00ae403c ["CALL", null, ["callee:00c5ad50:8"]]
+ 00b43dc0 ["INT_ADD", "register:40f0:8", ["const:b43dc0:8", "const:4:8"]]
+ 00b43dc0 ["CALL", null, ["callee:00c5ad50:8"]]
- 00ae403c bytes a5e80394
+ 00b43dc0 bytes e45b0494
- 00ae4060 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4060 ["INT_ADD", "register:40f0:8", ["const:ae4060:8", "const:4:8"]]
- 00ae4060 ["CALLIND", null, ["register:0:8"]]
+ 00b43de4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b43de4 ["INT_ADD", "register:40f0:8", ["const:b43de4:8", "const:4:8"]]
+ 00b43de4 ["CALLIND", null, ["register:0:8"]]
- 00ae4060 bytes 00013fd6
+ 00b43de4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

