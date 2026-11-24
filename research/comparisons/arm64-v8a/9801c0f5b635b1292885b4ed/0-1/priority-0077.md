# v15.7.4 → v16.0.0 · 最優先の変更候補 (77)

[一覧の目次](README.md)

<a id="compare-d55c1e8224f781edb121f7b25534da33"></a>

### [`00bba844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md) → [`00c3728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md) __cxa_guard_release

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)
- 新版 呼出元 1件 [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 60.98% / 新版 60.98%

CFGの説明率　旧版 6.25% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c372b0",
      "incomplete_value": false,
      "site": "00c372b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "definition_site": "00c372c8",
      "incomplete_value": false,
      "site": "00c372cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba880",
      "incomplete_value": false,
      "site": "00bba884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00c372dc",
      "incomplete_value": false,
      "site": "00c372e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
      "unmatched:00bba868",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00c372c8",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00c372d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bba8c0"
      ]
    ]
  ],
  "added": [
    [
      "00c372b0",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c372c8",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c372d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c37308"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md#insn-00bba86c) · [`00bba884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md#insn-00bba884) · [`00bba898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md#insn-00bba898)
- 新版 [`00c372b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372b4) · [`00c372cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372cc) · [`00c372e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md#insn-00c372e0)

~~~diff
- 00bba86c ["INT_ADD", "register:40f0:8", ["const:bba86c:8", "const:4:8"]]
- 00bba86c ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00c372b4 ["INT_ADD", "register:40f0:8", ["const:c372b4:8", "const:4:8"]]
+ 00c372b4 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00bba86c bytes ed8f0094
+ 00c372b4 bytes fb8f0094
- 00bba884 ["INT_ADD", "register:40f0:8", ["const:bba884:8", "const:4:8"]]
- 00bba884 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00c372cc ["INT_ADD", "register:40f0:8", ["const:c372cc:8", "const:4:8"]]
+ 00c372cc ["CALL", null, ["callee:00c5b2b0:8"]]
- 00bba884 bytes eb8f0094
+ 00c372cc bytes f98f0094
- 00bba898 ["INT_ADD", "register:40f0:8", ["const:bba898:8", "const:4:8"]]
- 00bba898 ["CALL", null, ["callee:00c5ddc0:8"]]
+ 00c372e0 ["INT_ADD", "register:40f0:8", ["const:c372e0:8", "const:4:8"]]
+ 00c372e0 ["CALL", null, ["callee:00c5ddc0:8"]]
- 00bba898 bytes 4a9a0094
+ 00c372e0 bytes b89a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21fc96b3b9d76800a2b798ad5f9090c7"></a>

### [`00bba8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md) → [`00c37334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md) __cxa_guard_abort

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb140.md) · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md) [`00be11c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11c0.md)
- 新版 呼出元 1件 [`00c57b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b90.md) · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md) [`00c5ddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 44.74% / 新版 44.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba8f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba8f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba8f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bba8f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba8f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba904",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37338",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3733c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c3734c",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md#insn-00bba8f0) · [`00bba8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md#insn-00bba8f4) · [`00bba908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md#insn-00bba908)
- 新版 [`00c37350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md#insn-00c37350)

~~~diff
- 00bba8f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bba8f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bba8f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bba8f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bba8f0 bytes fd7bbea9
- 00bba8f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bba8f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bba8f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bba8f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bba8f4 bytes f44f01a9
- 00bba908 ["INT_ADD", "register:40f0:8", ["const:bba908:8", "const:4:8"]]
- 00bba908 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00c37350 ["INT_ADD", "register:40f0:8", ["const:c37350:8", "const:4:8"]]
+ 00c37350 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00bba908 bytes c68f0094
+ 00c37350 bytes d48f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-425037af09b345c345821c03a662ada4"></a>

### [`00bba988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md) → [`00c373d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md) FUN_00c373d0

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c373e8",
      "incomplete_value": false,
      "site": "00c373ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba9a0",
      "incomplete_value": false,
      "site": "00bba9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c37410"
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
      "unmatched:00bba9a0",
      "PARAM",
      [
        "storage",
        "010a3700",
        null,
        null
      ]
    ],
    [
      "00c373f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bba9bc"
      ]
    ],
    [
      "unmatched:00bba9c4",
      "PARAM",
      [
        "storage",
        "002917e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c373e8",
      "PARAM",
      [
        "storage",
        "01128608",
        null,
        null
      ]
    ],
    [
      "00c373f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c37404"
      ]
    ],
    [
      "00c3740c",
      "PARAM",
      [
        "storage",
        "002a0dfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md#insn-00bba9a4) · [`00bba9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md#insn-00bba9b8) · [`00bba9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md#insn-00bba9c8)
- 新版 [`00c373ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md#insn-00c373ec)

~~~diff
- 00bba9a4 ["INT_ADD", "register:40f0:8", ["const:bba9a4:8", "const:4:8"]]
- 00bba9a4 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00c373ec ["INT_ADD", "register:40f0:8", ["const:c373ec:8", "const:4:8"]]
+ 00c373ec ["CALL", null, ["callee:00c5b2b0:8"]]
- 00bba9a4 bytes a38f0094
+ 00c373ec bytes b18f0094
- 00bba9b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bba9b8 ["RETURN", null, ["register:0:8"]]
- 00bba9b8 bytes c0035fd6
- 00bba9c8 ["INT_ADD", "register:40f0:8", ["const:bba9c8:8", "const:4:8"]]
- 00bba9c8 ["CALL", null, ["callee:00c37be4:8"]]
- 00bba9c8 bytes f5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2dfe596bb972ecabf8020e0cf32e9fe"></a>

### [`00bba9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md) → [`00c3742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md) _ZSt9terminatev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md) [`00bd4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fe4.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 1件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) · 呼出先 5件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) [`00c51a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a2c.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 20.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3744c",
      "incomplete_value": true,
      "site": "00c37450",
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
      "definition_site": "00bbaa04",
      "incomplete_value": true,
      "site": "00bbaa08",
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
            "register:4040:8"
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
      "unmatched:00bbaa00",
      "READ",
      [
        "storage",
        "00c1c000",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbaa04",
      "READ",
      [
        "storage",
        "00c24990",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "unmatched:00bbaa04",
      "PARAM",
      [
        "storage",
        "00bbaab4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37448",
      "READ",
      [
        "storage",
        "00c9ba30",
        null,
        "pointer"
      ]
    ],
    [
      "00c3744c",
      "READ",
      [
        "storage",
        "00ca4470",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "00c3744c",
      "PARAM",
      [
        "storage",
        "00c374fc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md#insn-00bbaa08) · [`00bba9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md#insn-00bba9ec) · [`00bba9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md#insn-00bba9f0)
- 新版 [`00c37450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md#insn-00c37450) · [`00c37434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md#insn-00c37434) · [`00c37438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md#insn-00c37438)

~~~diff
- 00bbaa08 ["INT_ADD", "register:40f0:8", ["const:bbaa08:8", "const:4:8"]]
- 00bbaa08 ["CALL", null, ["callee:00c374b8:8"]]
+ 00c37450 ["INT_ADD", "register:40f0:8", ["const:c37450:8", "const:4:8"]]
+ 00c37450 ["CALL", null, ["callee:00c374b8:8"]]
- 00bbaa08 bytes 1a000094
+ 00c37450 bytes 1a000094
- 00bba9ec ["INT_ADD", "register:40f0:8", ["const:bba9ec:8", "const:4:8"]]
- 00bba9ec ["CALL", null, ["callee:00c5e9a0:8"]]
+ 00c37434 ["INT_ADD", "register:40f0:8", ["const:c37434:8", "const:4:8"]]
+ 00c37434 ["CALL", null, ["callee:00c5e9a0:8"]]
- 00bba9ec bytes fd9c0094
+ 00c37434 bytes 5b9d0094
- 00bba9f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bba9f0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c37438 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c37438 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bba9f0 bytes 600000b4
+ 00c37438 bytes 600000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b53e4116f1bc3c3c3f7fd2e9caba54ea"></a>

### [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) → [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) FUN_00c3746c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bbaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)
- 新版 呼出元 2件 [`00c37488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md) [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37480",
      "incomplete_value": true,
      "site": "00c37484",
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
            "const:dfa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaa38",
      "incomplete_value": false,
      "site": "00bbaa3c",
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
            "const:613:8"
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
      "unmatched:00bbaa38",
      "PARAM",
      [
        "storage",
        "00293613",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37480",
      "PARAM",
      [
        "storage",
        "002a2dfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md#insn-00bbaa3c) · [`00bbaa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md#insn-00bbaa30) · [`00bbaa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md#insn-00bbaa34)
- 新版 [`00c37484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c37484) · [`00c37478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c37478) · [`00c3747c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md#insn-00c3747c)

~~~diff
- 00bbaa3c ["INT_ADD", "register:40f0:8", ["const:bbaa3c:8", "const:4:8"]]
- 00bbaa3c ["CALL", null, ["callee:00c37be4:8"]]
+ 00c37484 ["INT_ADD", "register:40f0:8", ["const:c37484:8", "const:4:8"]]
+ 00c37484 ["CALL", null, ["callee:00c37be4:8"]]
- 00bbaa3c bytes d8010094
+ 00c37484 bytes d8010094
- 00bbaa30 ["COPY", "register:0:8", ["register:4000:8"]]
- 00bbaa30 ["INT_ADD", "register:40f0:8", ["const:bbaa30:8", "const:4:8"]]
- 00bbaa30 ["CALLIND", null, ["register:0:8"]]
+ 00c37478 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c37478 ["INT_ADD", "register:40f0:8", ["const:c37478:8", "const:4:8"]]
+ 00c37478 ["CALLIND", null, ["register:0:8"]]
- 00bbaa30 bytes 00003fd6
+ 00c37478 bytes 00003fd6
- 00bbaa34 ["COPY", "register:4000:8", ["const:293000:8"]]
+ 00c3747c ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 00bbaa34 bytes c0b6ffb0
+ 00c3747c bytes 40b3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e76c3f269da7be6b34197a3b90651f"></a>

### [`00bbaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) → [`00c37488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md) _ZSt10unexpectedv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) [`00bbac00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) [`00c37648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaa44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaa44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3748c"
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
      "unmatched:00bbaa44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37498",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00c3749c",
      "READ",
      [
        "storage",
        "00c24998",
        "__cxa_unexpected_handler",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3748c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37498",
      "READ",
      [
        "storage",
        "00c9ba28",
        null,
        "pointer"
      ]
    ],
    [
      "00c3749c",
      "READ",
      [
        "storage",
        "00ca4478",
        "__cxa_unexpected_handler",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md#insn-00bbaa44) · [`00bbaa58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md#insn-00bbaa58)
- 新版 [`00c374a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md#insn-00c374a0) · [`00c3748c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md#insn-00c3748c)

~~~diff
- 00bbaa44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbaa44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbaa44 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbaa44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbaa44 bytes fd7bbfa9
- 00bbaa58 ["INT_ADD", "register:40f0:8", ["const:bbaa58:8", "const:4:8"]]
- 00bbaa58 ["CALL", null, ["callee:00c3746c:8"]]
+ 00c374a0 ["INT_ADD", "register:40f0:8", ["const:c374a0:8", "const:4:8"]]
+ 00c374a0 ["CALL", null, ["callee:00c3746c:8"]]
- 00bbaa58 bytes f3ffff97
+ 00c374a0 bytes f3ffff97
+ 00c3748c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c3748c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c3748c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c3748c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c3748c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-473004bd00d3d917f9da6171928b9e64"></a>

### [`00bbaa5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md) → [`00c374a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md) _ZSt13get_terminatev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e10.md) · 呼出先 1件 [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md)
- 新版 呼出元 1件 [`00c5e9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9d0.md) · 呼出先 1件 [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c374b0",
      "incomplete_value": true,
      "site": "00c374b4",
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
      "definition_site": "00bbaa68",
      "incomplete_value": true,
      "site": "00bbaa6c",
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
              [
                "leaf",
                "const:c1c000:8"
              ]
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
      "00c374ac",
      "READ",
      [
        "storage",
        "00c1c000",
        null,
        "pointer"
      ]
    ],
    [
      "00c374b0",
      "READ",
      [
        "storage",
        "00c24990",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "00c374b0",
      "DATA",
      [
        "storage",
        "00bbaab4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c374ac",
      "READ",
      [
        "storage",
        "00c9ba30",
        null,
        "pointer"
      ]
    ],
    [
      "00c374b0",
      "READ",
      [
        "storage",
        "00ca4470",
        "__cxa_terminate_handler",
        "pointer"
      ]
    ],
    [
      "00c374b0",
      "DATA",
      [
        "storage",
        "00c374fc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md#insn-00bbaa60) · [`00bbaa64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md#insn-00bbaa64)
- 新版 [`00c374a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md#insn-00c374a8) · [`00c374ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md#insn-00c374ac)

~~~diff
- 00bbaa60 ["COPY", "register:4040:8", ["const:c1c000:8"]]
+ 00c374a8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bbaa60 bytes 080300d0
+ 00c374a8 bytes 28030090
- 00bbaa64 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bbaa64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c374ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
+ 00c374ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbaa64 bytes 080140f9
+ 00c374ac bytes 081945f9
~~~


<a id="compare-194e233662c3dee12906d4b3b0d4dda8"></a>

### [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) → [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) FUN_00c374b8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`00bba9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md) [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) [`00bd5708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md) · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)
- 新版 呼出元 8件 [`00c3742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md) [`00c51bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md) [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) [`00c52150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md) · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaa74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaa74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c374bc"
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
      "unmatched:00bbaa74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c374cc",
      "PARAM",
      [
        "storage",
        "00298ac4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c374bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c374cc",
      "PARAM",
      [
        "storage",
        "002a8882",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md#insn-00bbaa74) · [`00bbaa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md#insn-00bbaa88)
- 新版 [`00c374d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md#insn-00c374d0) · [`00c374bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md#insn-00c374bc)

~~~diff
- 00bbaa74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbaa74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbaa74 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbaa74 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbaa74 bytes fd7bbfa9
- 00bbaa88 ["INT_ADD", "register:40f0:8", ["const:bbaa88:8", "const:4:8"]]
- 00bbaa88 ["CALL", null, ["callee:00c37be4:8"]]
+ 00c374d0 ["INT_ADD", "register:40f0:8", ["const:c374d0:8", "const:4:8"]]
+ 00c374d0 ["CALL", null, ["callee:00c37be4:8"]]
- 00bbaa88 bytes c5010094
+ 00c374d0 bytes c5010094
+ 00c374bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c374bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c374bc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c374bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c374bc bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e740a8f7cb7b9f7e59c8b72f300a976"></a>

### [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md) → [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) FUN_00c374fc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bba9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9e4.md) [`00bbaa5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa5c.md) [`00bbac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac54.md) · 呼出先 6件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fe4.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 3件 [`00c3742c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3742c.md) [`00c374a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374a4.md) [`00c3769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3769c.md) · 呼出先 6件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c37f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c51a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a2c.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.75% / 新版 65.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaabc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbaab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbaabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbaac0",
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
      "00c37500",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c37504",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37508",
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

- 旧版 [`00bbaab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md#insn-00bbaab8) · [`00bbaabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md#insn-00bbaabc) · [`00bbaac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md#insn-00bbaac0)

~~~diff
- 00bbaab8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbaab8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbaab8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbaab8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbaab8 bytes fd7bbda9
- 00bbaabc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbaabc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bbaabc bytes f50b00f9
- 00bbaac0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbaac0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbaac0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbaac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbaac0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec5162b9c5b3372c6c0d3c235e6eb0c5"></a>

### [`00bbacac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbacac.md) → [`00c376f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c376f4.md) &lt;EXTERNAL&gt;::free

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbacb0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ],
  "added": [
    [
      "00c376f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ]
}
~~~


<a id="compare-fef07a9ba35b3d9a9e7e349dab0c37fe"></a>

### [`00bbacbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbacbc.md) → [`00c37704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37704.md) __cxa_get_globals

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md) · 呼出先 1件 [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 1件 [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md) · 呼出先 1件 [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbacc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbacc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c37708"
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
      "unmatched:00bbacc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37714",
      "PARAM",
      [
        "storage",
        "00c249a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37708",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37714",
      "PARAM",
      [
        "storage",
        "00ca4488",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbacc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbacbc.md#insn-00bbacc0) · [`00bbacd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbacbc.md#insn-00bbacd0)
- 新版 [`00c37718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37704.md#insn-00c37718) · [`00c37708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37704.md#insn-00c37708)

~~~diff
- 00bbacc0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbacc0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbacc0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbacc0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbacc0 bytes fd7bbfa9
- 00bbacd0 ["INT_ADD", "register:40f0:8", ["const:bbacd0:8", "const:4:8"]]
- 00bbacd0 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00c37718 ["INT_ADD", "register:40f0:8", ["const:c37718:8", "const:4:8"]]
+ 00c37718 ["CALL", null, ["callee:00c59ef0:8"]]
- 00bbacd0 bytes f4890094
+ 00c37718 bytes f6890094
+ 00c37708 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37708 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37708 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c37708 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37708 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4b4d751032a0ea6e049ac5c0094013"></a>

### [`00bbace0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md) → [`00c37728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37728.md) __cxa_get_globals_fast

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md) · 呼出先 1件 [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md)
- 新版 呼出元 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md) · 呼出先 1件 [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbace4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbace4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3772c"
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
      "unmatched:00bbace4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37738",
      "PARAM",
      [
        "storage",
        "00c249a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3772c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37738",
      "PARAM",
      [
        "storage",
        "00ca4488",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbace4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md#insn-00bbace4) · [`00bbacf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md#insn-00bbacf4) · [`00bbad00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md#insn-00bbad00)
- 新版 [`00c3773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37728.md#insn-00c3773c)

~~~diff
- 00bbace4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbace4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbace4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbace4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbace4 bytes fd7bbfa9
- 00bbacf4 ["INT_ADD", "register:40f0:8", ["const:bbacf4:8", "const:4:8"]]
- 00bbacf4 ["CALL", null, ["callee:00c59ef0:8"]]
+ 00c3773c ["INT_ADD", "register:40f0:8", ["const:c3773c:8", "const:4:8"]]
+ 00c3773c ["CALL", null, ["callee:00c59ef0:8"]]
- 00bbacf4 bytes eb890094
+ 00c3773c bytes ed890094
- 00bbad00 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbad00 ["RETURN", null, ["register:0:8"]]
- 00bbad00 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e86ff2b42afdf6266bdc957fc12c40"></a>

### [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) → [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) _ZNSt20bad_array_new_lengthD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 50件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) [`0048df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) · 呼出先 0件 
- 新版 呼出元 50件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004afbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004af/004afbd0.md) [`004b0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b0df4.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-9dd1d05bc0de03852fbcb03c448920f6"></a>

### [`00bbae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae20.md) → [`00c37868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37868.md) _ZNSt20bad_array_new_lengthD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c40.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbae34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae20.md#insn-00bbae34)
- 新版 [`00c3787c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37868.md#insn-00c3787c)

~~~diff
- 00bbae34 ["INT_ADD", "register:40f0:8", ["const:bbae34:8", "const:4:8"]]
- 00bbae34 ["CALL", null, ["callee:00c57c40:8"]]
+ 00c3787c ["INT_ADD", "register:40f0:8", ["const:c3787c:8", "const:4:8"]]
+ 00c3787c ["CALL", null, ["callee:00c57c40:8"]]
- 00bbae34 bytes ef800094
+ 00c3787c bytes f1800094
~~~


<a id="compare-c242615ff8053c692cfc4dfce9de3f83"></a>

### [`00bbae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md) → [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) _ZNSt12out_of_rangeD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bdb0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0b0.md) · 呼出先 3件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 10件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c57b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b00.md) · 呼出先 3件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbae60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbae64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbae74",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c378a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c378ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c378bc",
      "READ",
      [
        "storage",
        "00c9b690",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbae60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md#insn-00bbae60) · [`00bbae64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md#insn-00bbae64) · [`00bbae84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae5c.md#insn-00bbae84)

~~~diff
- 00bbae60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbae60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbae60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbae60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbae60 bytes fd7bbea9
- 00bbae64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbae64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbae64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbae64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbae64 bytes f44f01a9
- 00bbae84 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bbae84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbae84 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06000d9928a73ce9445b1cd0ab926494"></a>

### [`00bbaeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeb4.md) → [`00c378fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378fc.md) _ZNSt11logic_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea20.md)

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
      "site": "00c37910",
      "value": [
        "leaf",
        "ram:c5ea20:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bbaec8",
      "value": [
        "leaf",
        "ram:be1e60:8"
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
      "00c37910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1e60"
      ]
    ]
  ],
  "added": [
    [
      "00c37910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5ea20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeb4.md#insn-00bbaec8)
- 新版 [`00c37910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378fc.md#insn-00c37910)

~~~diff
- 00bbaec8 ["INT_ADD", "register:40f0:8", ["const:bbaec8:8", "const:4:8"]]
- 00bbaec8 ["CALL", null, ["ram:be1e60:8"]]
+ 00c37910 ["INT_ADD", "register:40f0:8", ["const:c37910:8", "const:4:8"]]
+ 00c37910 ["CALL", null, ["ram:c5ea20:8"]]
- 00bbaec8 bytes e69b0094
+ 00c37910 bytes 449c0094
~~~


<a id="compare-23a60e65c13e9c8ae4ae64c6701af549"></a>

### [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) → [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) _ZNSt13runtime_errorD2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md) [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) [`00bdda70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda70.md) [`00be0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f70.md) · 呼出先 3件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb490.md)
- 新版 呼出元 8件 [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md) [`00bf0688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md) [`00c5a4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4c0.md) [`00c5db70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db70.md) · 呼出先 3件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaf14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3795c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbaf10",
      "incomplete_value": true,
      "site": "00bbaf1c",
      "value": [
        "INT_SUB",
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
            "const:8:8"
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
      "unmatched:00bbaf04",
      "READ",
      [
        "storage",
        "00c1bc68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbaf14",
      "DATA",
      [
        "storage",
        "00c16958",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c3794c",
      "READ",
      [
        "storage",
        "00c9b698",
        null,
        "pointer"
      ]
    ],
    [
      "00c3795c",
      "DATA",
      [
        "storage",
        "00c96300",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md#insn-00bbaf14) · [`00bbaf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md#insn-00bbaf1c)
- 新版 [`00c37964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md#insn-00c37964) · [`00c3795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md#insn-00c3795c)

~~~diff
- 00bbaf14 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bbaf14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbaf14 bytes 080000f9
- 00bbaf1c ["INT_ADD", "register:40f0:8", ["const:bbaf1c:8", "const:4:8"]]
- 00bbaf1c ["CALL", null, ["callee:00c53880:8"]]
+ 00c37964 ["INT_ADD", "register:40f0:8", ["const:c37964:8", "const:4:8"]]
+ 00c37964 ["CALL", null, ["callee:00c53880:8"]]
- 00bbaf1c bytes c56f0094
+ 00c37964 bytes c76f0094
+ 00c3795c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00c3795c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c3795c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f912a14040894b38db8e38f49bfeb2f"></a>

### [`00bbaf7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf7c.md) → [`00c379c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md) _ZNSt12domain_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea30.md)

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
      "site": "00c379d8",
      "value": [
        "leaf",
        "ram:c5ea30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bbaf90",
      "value": [
        "leaf",
        "ram:be1e70:8"
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
      "00c379d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1e70"
      ]
    ]
  ],
  "added": [
    [
      "00c379d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5ea30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf7c.md#insn-00bbaf90)
- 新版 [`00c379d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md#insn-00c379d8)

~~~diff
- 00bbaf90 ["INT_ADD", "register:40f0:8", ["const:bbaf90:8", "const:4:8"]]
- 00bbaf90 ["CALL", null, ["ram:be1e70:8"]]
+ 00c379d8 ["INT_ADD", "register:40f0:8", ["const:c379d8:8", "const:4:8"]]
+ 00c379d8 ["CALL", null, ["ram:c5ea30:8"]]
- 00bbaf90 bytes b89b0094
+ 00c379d8 bytes 169c0094
~~~


<a id="compare-5e2f282b1ce4c21aebfb00b0a1b703ee"></a>

### [`00bbafa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafa8.md) → [`00c379f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379f0.md) _ZNSt16invalid_argumentD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd30.md)

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
      "site": "00c37a04",
      "value": [
        "leaf",
        "ram:c5dd30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bbafbc",
      "value": [
        "leaf",
        "ram:be1130:8"
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
      "00c37a04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1130"
      ]
    ]
  ],
  "added": [
    [
      "00c37a04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dd30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafa8.md#insn-00bbafbc)
- 新版 [`00c37a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379f0.md#insn-00c37a04)

~~~diff
- 00bbafbc ["INT_ADD", "register:40f0:8", ["const:bbafbc:8", "const:4:8"]]
- 00bbafbc ["CALL", null, ["ram:be1130:8"]]
+ 00c37a04 ["INT_ADD", "register:40f0:8", ["const:c37a04:8", "const:4:8"]]
+ 00c37a04 ["CALL", null, ["ram:c5dd30:8"]]
- 00bbafbc bytes 5d980094
+ 00c37a04 bytes cb980094
~~~


<a id="compare-5f8ced4ad4466b2b08234f2b55aa37d8"></a>

### [`00bbb02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb02c.md) → [`00c37a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a74.md) _ZNSt11range_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4c0.md)

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
      "site": "00c37a88",
      "value": [
        "leaf",
        "ram:c5a4c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bbb040",
      "value": [
        "leaf",
        "ram:bdda70:8"
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
      "00c37a88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdda70"
      ]
    ]
  ],
  "added": [
    [
      "00c37a88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a4c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb02c.md#insn-00bbb040)
- 新版 [`00c37a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a74.md#insn-00c37a88)

~~~diff
- 00bbb040 ["INT_ADD", "register:40f0:8", ["const:bbb040:8", "const:4:8"]]
- 00bbb040 ["CALL", null, ["ram:bdda70:8"]]
+ 00c37a88 ["INT_ADD", "register:40f0:8", ["const:c37a88:8", "const:4:8"]]
+ 00c37a88 ["CALL", null, ["ram:c5a4c0:8"]]
- 00bbb040 bytes 8c8a0094
+ 00c37a88 bytes 8e8a0094
~~~


<a id="compare-82a9c84f2624f719609226bbfef2b9ac"></a>

### [`00bbb058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb058.md) → [`00c37aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37aa0.md) _ZNSt14overflow_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5db70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db70.md)

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
      "site": "00c37ab4",
      "value": [
        "leaf",
        "ram:c5db70:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bbb06c",
      "value": [
        "leaf",
        "ram:be0f70:8"
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
      "00c37ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0f70"
      ]
    ]
  ],
  "added": [
    [
      "00c37ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5db70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb058.md#insn-00bbb06c)
- 新版 [`00c37ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37aa0.md#insn-00c37ab4)

~~~diff
- 00bbb06c ["INT_ADD", "register:40f0:8", ["const:bbb06c:8", "const:4:8"]]
- 00bbb06c ["CALL", null, ["ram:be0f70:8"]]
+ 00c37ab4 ["INT_ADD", "register:40f0:8", ["const:c37ab4:8", "const:4:8"]]
+ 00c37ab4 ["CALL", null, ["ram:c5db70:8"]]
- 00bbb06c bytes c1970094
+ 00c37ab4 bytes 2f980094
~~~


<a id="compare-0b87c5ea423401b613362bab5f954575"></a>

### [`00bbb0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0b8.md) → [`00c37b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b00.md) _ZNSt9type_infoD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ea0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea60.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0b8.md#insn-00bbb0cc)
- 新版 [`00c37b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b00.md#insn-00c37b14)

~~~diff
- 00bbb0cc ["INT_ADD", "register:40f0:8", ["const:bbb0cc:8", "const:4:8"]]
- 00bbb0cc ["CALL", null, ["callee:00c5ea60:8"]]
+ 00c37b14 ["INT_ADD", "register:40f0:8", ["const:c37b14:8", "const:4:8"]]
+ 00c37b14 ["CALL", null, ["callee:00c5ea60:8"]]
- 00bbb0cc bytes 759b0094
+ 00c37b14 bytes d39b0094
~~~


<a id="compare-7c947ca160113c7573fb0cd5b66e49ce"></a>

### [`00bbb104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb104.md) → [`00c37b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b4c.md) _ZNSt8bad_castD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e090.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb104.md#insn-00bbb118)
- 新版 [`00c37b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b4c.md#insn-00c37b60)

~~~diff
- 00bbb118 ["INT_ADD", "register:40f0:8", ["const:bbb118:8", "const:4:8"]]
- 00bbb118 ["CALL", null, ["callee:00c5e090:8"]]
+ 00c37b60 ["INT_ADD", "register:40f0:8", ["const:c37b60:8", "const:4:8"]]
+ 00c37b60 ["CALL", null, ["callee:00c5e090:8"]]
- 00bbb118 bytes de980094
+ 00c37b60 bytes 4c990094
~~~


<a id="compare-398da9feda3782ca676d9803bb732b3c"></a>

### [`00bbb18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb18c.md) → [`00c37bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37bd4.md) _ZNKSt10bad_typeid4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c37bdc",
      "incomplete_value": false,
      "site": "00c37be0",
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
            "const:a9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb194",
      "incomplete_value": false,
      "site": "00bbb198",
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
            "const:775:8"
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
      "00c37bdc",
      "DATA",
      [
        "storage",
        "002ad775",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37bdc",
      "DATA",
      [
        "storage",
        "002bea9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb18c.md#insn-00bbb190) · [`00bbb194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb18c.md#insn-00bbb194)
- 新版 [`00c37bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37bd4.md#insn-00c37bd8) · [`00c37bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37bd4.md#insn-00c37bdc)

~~~diff
- 00bbb190 ["COPY", "register:4000:8", ["const:2ad000:8"]]
+ 00c37bd8 ["COPY", "register:4000:8", ["const:2be000:8"]]
- 00bbb190 bytes 80b7ffd0
+ 00c37bd8 bytes 20b4fff0
- 00bbb194 ["COPY", "tmp:0:8", ["const:775:8"]]
- 00bbb194 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb194 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb194 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c37bdc ["COPY", "tmp:0:8", ["const:a9b:8"]]
+ 00c37bdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37bdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c37bdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbb194 bytes 00d41d91
+ 00c37bdc bytes 006c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c888e8e33bec416e1db819d7f07491e"></a>

### [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) → [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) FUN_00c37be4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 22件 [`00bba700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba700.md) [`00bba844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba844.md) [`00bba8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba8ec.md) [`00bba988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba988.md) [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) · 呼出先 10件 [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md) [`00bdd430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd430.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1710.md) [`00be1eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1eb0.md)
- 新版 呼出元 22件 [`00c37148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37148.md) [`00c3728c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3728c.md) [`00c37334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37334.md) [`00c373d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c373d0.md) [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) · 呼出先 10件 [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md) [`00c59e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e80.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5e300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e300.md) [`00c5ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea70.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37c18",
      "incomplete_value": false,
      "site": "00c37c44",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb1d0",
      "incomplete_value": false,
      "site": "00bbb1fc",
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
            "const:7a4:8"
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
      "definition_site": "00c37c40",
      "incomplete_value": true,
      "site": "00c37c44",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb1f8",
      "incomplete_value": true,
      "site": "00bbb1fc",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37c88",
      "incomplete_value": false,
      "site": "00c37c8c",
      "value": [
        "leaf",
        "const:a:8"
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
      "unmatched:00bbb1d0",
      "PARAM",
      [
        "storage",
        "002af7a4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bbb1f4",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbb1f8",
      "PARAM",
      [
        "storage",
        "010a58b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37c18",
      "PARAM",
      [
        "storage",
        "002c0dc8",
        null,
        "string"
      ]
    ],
    [
      "00c37c3c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c37c40",
      "PARAM",
      [
        "storage",
        "0112a8f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md#insn-00bbb1fc) · [`00bbb244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md#insn-00bbb244) · [`00bbb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md#insn-00bbb280)
- 新版 [`00c37c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37c44) · [`00c37c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37c8c) · [`00c37cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md#insn-00c37cc8)

~~~diff
- 00bbb1fc ["INT_ADD", "register:40f0:8", ["const:bbb1fc:8", "const:4:8"]]
- 00bbb1fc ["CALL", null, ["callee:00c59e20:8"]]
+ 00c37c44 ["INT_ADD", "register:40f0:8", ["const:c37c44:8", "const:4:8"]]
+ 00c37c44 ["CALL", null, ["callee:00c59e20:8"]]
- 00bbb1fc bytes 75880094
+ 00c37c44 bytes 77880094
- 00bbb244 ["INT_ADD", "register:40f0:8", ["const:bbb244:8", "const:4:8"]]
- 00bbb244 ["CALL", null, ["callee:00c59e80:8"]]
+ 00c37c8c ["INT_ADD", "register:40f0:8", ["const:c37c8c:8", "const:4:8"]]
+ 00c37c8c ["CALL", null, ["callee:00c59e80:8"]]
- 00bbb244 bytes 7b880094
+ 00c37c8c bytes 7d880094
- 00bbb280 ["INT_ADD", "register:40f0:8", ["const:bbb280:8", "const:4:8"]]
- 00bbb280 ["CALL", null, ["callee:00c5ea90:8"]]
+ 00c37cc8 ["INT_ADD", "register:40f0:8", ["const:c37cc8:8", "const:4:8"]]
+ 00c37cc8 ["CALL", null, ["callee:00c5ea90:8"]]
- 00bbb280 bytes 149b0094
+ 00c37cc8 bytes 729b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfc5c98c86d0310dceaef1b9ab433be"></a>

### [`00bbb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2a0.md) → [`00c37ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ce8.md) _ZNSt9type_infoD2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb2a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ea50"
      ]
    ]
  ],
  "added": [
    [
      "00c37cec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ea50"
      ]
    ]
  ]
}
~~~


<a id="compare-37e6e9eb019208839a2c3cfa8f0c3423"></a>

### [`00bbb2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2c0.md) → [`00c37d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d08.md) FUN_00c37d08

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2c0.md#insn-00bbb2d4)
- 新版 [`00c37d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d08.md#insn-00c37d1c)

~~~diff
- 00bbb2d4 ["INT_ADD", "register:40f0:8", ["const:bbb2d4:8", "const:4:8"]]
- 00bbb2d4 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37d1c ["INT_ADD", "register:40f0:8", ["const:c37d1c:8", "const:4:8"]]
+ 00c37d1c ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb2d4 bytes ef9a0094
+ 00c37d1c bytes 4d9b0094
~~~


<a id="compare-632688b80c6f13047b541efe1fed756d"></a>

### [`00bbb2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2ec.md) → [`00c37d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d34.md) FUN_00c37d34

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb2ec.md#insn-00bbb300)
- 新版 [`00c37d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d34.md#insn-00c37d48)

~~~diff
- 00bbb300 ["INT_ADD", "register:40f0:8", ["const:bbb300:8", "const:4:8"]]
- 00bbb300 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37d48 ["INT_ADD", "register:40f0:8", ["const:c37d48:8", "const:4:8"]]
+ 00c37d48 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb300 bytes e49a0094
+ 00c37d48 bytes 429b0094
~~~


<a id="compare-ea15d982c5b00779fed96602f1b8a20b"></a>

### [`00bbb344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb344.md) → [`00c37d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d8c.md) FUN_00c37d8c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb344.md#insn-00bbb358)
- 新版 [`00c37da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d8c.md#insn-00c37da0)

~~~diff
- 00bbb358 ["INT_ADD", "register:40f0:8", ["const:bbb358:8", "const:4:8"]]
- 00bbb358 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37da0 ["INT_ADD", "register:40f0:8", ["const:c37da0:8", "const:4:8"]]
+ 00c37da0 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb358 bytes ce9a0094
+ 00c37da0 bytes 2c9b0094
~~~


<a id="compare-46c8bf6482d92e5c6d3ff27ca176f5a8"></a>

### [`00bbb39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb39c.md) → [`00c37de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37de4.md) FUN_00c37de4

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb39c.md#insn-00bbb3b0)
- 新版 [`00c37df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37de4.md#insn-00c37df8)

~~~diff
- 00bbb3b0 ["INT_ADD", "register:40f0:8", ["const:bbb3b0:8", "const:4:8"]]
- 00bbb3b0 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37df8 ["INT_ADD", "register:40f0:8", ["const:c37df8:8", "const:4:8"]]
+ 00c37df8 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb3b0 bytes b89a0094
+ 00c37df8 bytes 169b0094
~~~


<a id="compare-ebf4b599e7be9562d77fef79df7341fa"></a>

### [`00bbb3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3c8.md) → [`00c37e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e10.md) FUN_00c37e10

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3c8.md#insn-00bbb3dc)
- 新版 [`00c37e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e10.md#insn-00c37e24)

~~~diff
- 00bbb3dc ["INT_ADD", "register:40f0:8", ["const:bbb3dc:8", "const:4:8"]]
- 00bbb3dc ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37e24 ["INT_ADD", "register:40f0:8", ["const:c37e24:8", "const:4:8"]]
+ 00c37e24 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb3dc bytes ad9a0094
+ 00c37e24 bytes 0b9b0094
~~~


<a id="compare-ded1b856498653e7f0d204f3f017463e"></a>

### [`00bbb3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3f4.md) → [`00c37e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e3c.md) FUN_00c37e3c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb3f4.md#insn-00bbb408)
- 新版 [`00c37e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e3c.md#insn-00c37e50)

~~~diff
- 00bbb408 ["INT_ADD", "register:40f0:8", ["const:bbb408:8", "const:4:8"]]
- 00bbb408 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37e50 ["INT_ADD", "register:40f0:8", ["const:c37e50:8", "const:4:8"]]
+ 00c37e50 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb408 bytes a29a0094
+ 00c37e50 bytes 009b0094
~~~


<a id="compare-251b0645df430628f08d6272ee4d70f0"></a>

### [`00bbb44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb44c.md) → [`00c37e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e94.md) FUN_00c37e94

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb44c.md#insn-00bbb460)
- 新版 [`00c37ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e94.md#insn-00c37ea8)

~~~diff
- 00bbb460 ["INT_ADD", "register:40f0:8", ["const:bbb460:8", "const:4:8"]]
- 00bbb460 ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37ea8 ["INT_ADD", "register:40f0:8", ["const:c37ea8:8", "const:4:8"]]
+ 00c37ea8 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb460 bytes 8c9a0094
+ 00c37ea8 bytes ea9a0094
~~~


<a id="compare-34dbdd87cb8df7d40e8d5edbb2097185"></a>

### [`00bbb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md) → [`00c37f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md) FUN_00c37f08

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaab4.md) · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`00c374fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374fc.md) · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.49% / 新版 69.49%

CFGの説明率　旧版 14.29% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c37f28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c37f4c",
      "incomplete_value": true,
      "site": "00c37f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb504",
      "incomplete_value": true,
      "site": "00bbb508",
      "value": [
        "live",
        "register:4040:8"
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
      "unmatched:00bbb4e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c37fbc"
      ]
    ],
    [
      "unmatched:00bbb4f0",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbb4f4",
      "READ",
      [
        "storage",
        "00c1c050",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c37f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c37fbc"
      ]
    ],
    [
      "00c37f38",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c37f3c",
      "READ",
      [
        "storage",
        "00c9ba80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md#insn-00bbb4e0) · [`00bbb508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md#insn-00bbb508) · [`00bbb554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb4c0.md#insn-00bbb554)
- 新版 [`00c37f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md#insn-00c37f50) · [`00c37f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37f08.md#insn-00c37f9c)

~~~diff
- 00bbb4e0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00bbb4e0 bytes a0040054
- 00bbb508 ["INT_ADD", "register:40f0:8", ["const:bbb508:8", "const:4:8"]]
- 00bbb508 ["CALL", null, ["callee:00c58210:8"]]
+ 00c37f50 ["INT_ADD", "register:40f0:8", ["const:c37f50:8", "const:4:8"]]
+ 00c37f50 ["CALL", null, ["callee:00c58210:8"]]
- 00bbb508 bytes ae800094
+ 00c37f50 bytes b0800094
- 00bbb554 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb554 ["INT_ADD", "register:40f0:8", ["const:bbb554:8", "const:4:8"]]
- 00bbb554 ["CALLIND", null, ["register:0:8"]]
+ 00c37f9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c37f9c ["INT_ADD", "register:40f0:8", ["const:c37f9c:8", "const:4:8"]]
+ 00c37f9c ["CALLIND", null, ["register:0:8"]]
- 00bbb554 bytes 00013fd6
+ 00c37f9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5109ce1a3e7b248db371427e4d4e1332"></a>

### [`00bbb8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb8d4.md) → [`00c3831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c3831c.md) FUN_00c3831c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 30.36% / 新版 35.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbba40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb8e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38378"
      ]
    ],
    [
      "unmatched:00bbb92c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38404"
      ]
    ]
  ],
  "added": [
    [
      "00c3832c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c38350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38378"
      ]
    ],
    [
      "00c38374",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38404"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb8d4.md#insn-00bbb8e4) · [`00bbb908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb8d4.md#insn-00bbb908) · [`00bbb9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb8d4.md#insn-00bbb9dc)

~~~diff
- 00bbb8e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbb8e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbb8e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbb8e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbb8e4 bytes f44f03a9
- 00bbb908 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00bbb908 bytes 40010054
- 00bbb9dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb9dc ["INT_ADD", "register:40f0:8", ["const:bbb9dc:8", "const:4:8"]]
- 00bbb9dc ["CALLIND", null, ["register:0:8"]]
- 00bbb9dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-778f8ce2994dc64850c16aaa30fd01e8"></a>

### [`00bbbaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbaa4.md) → [`00c384ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md) FUN_00c384ec

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 40.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbbac8",
      "incomplete_value": true,
      "site": "00bbbad0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbbacc",
      "incomplete_value": true,
      "site": "00bbbad0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3854c",
      "incomplete_value": true,
      "site": "00c38550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbb04",
      "incomplete_value": true,
      "site": "00bbbb08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "00c38538",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "00c3853c",
      "READ",
      [
        "storage",
        "00c1c058",
        null,
        "pointer"
      ]
    ],
    [
      "00c3853c",
      "PARAM",
      [
        "storage",
        "00c16c40",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38538",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c3853c",
      "READ",
      [
        "storage",
        "00c9ba88",
        null,
        "pointer"
      ]
    ],
    [
      "00c3853c",
      "PARAM",
      [
        "storage",
        "00c965e8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbaa4.md#insn-00bbbad0) · [`00bbbb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbaa4.md#insn-00bbbb08) · [`00bbbb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbaa4.md#insn-00bbbb4c)
- 新版 [`00c38518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md#insn-00c38518) · [`00c38550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c384ec.md#insn-00c38550)

~~~diff
- 00bbbad0 ["INT_ADD", "register:40f0:8", ["const:bbbad0:8", "const:4:8"]]
- 00bbbad0 ["CALL", null, ["callee:00c5b450:8"]]
+ 00c38518 ["INT_ADD", "register:40f0:8", ["const:c38518:8", "const:4:8"]]
+ 00c38518 ["CALL", null, ["callee:00c5b450:8"]]
- 00bbbad0 bytes c08b0094
+ 00c38518 bytes ce8b0094
- 00bbbb08 ["INT_ADD", "register:40f0:8", ["const:bbbb08:8", "const:4:8"]]
- 00bbbb08 ["CALL", null, ["callee:00c58210:8"]]
+ 00c38550 ["INT_ADD", "register:40f0:8", ["const:c38550:8", "const:4:8"]]
+ 00c38550 ["CALL", null, ["callee:00c58210:8"]]
- 00bbbb08 bytes 2e7f0094
+ 00c38550 bytes 307f0094
- 00bbbb4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbbb4c ["RETURN", null, ["register:0:8"]]
- 00bbbb4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-764ee4b3fd79ca19bde3cbf0855e2f0d"></a>

### [`00bbbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) → [`00c38598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md) FUN_00c38598

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbbe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) [`00bbbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c38854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) [`00c38948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 79.43% / 新版 79.43%

CFGの説明率　旧版 38.33% / 新版 38.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c385c4",
      "incomplete_value": true,
      "site": "00c385c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00bbbb7c",
      "incomplete_value": true,
      "site": "00bbbb80",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbc08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbc30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c385c0",
      "READ",
      [
        "storage",
        "00c1c060",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbbbe0",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbbbe0",
      "PARAM",
      [
        "storage",
        "00c16c10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c385c0",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00c38628",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38628",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md#insn-00bbbbec) · [`00bbbc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md#insn-00bbbc08) · [`00bbbc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md#insn-00bbbc24)
- 新版 [`00c38634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md#insn-00c38634) · [`00c3866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md#insn-00c3866c)

~~~diff
- 00bbbbec ["INT_ADD", "register:40f0:8", ["const:bbbbec:8", "const:4:8"]]
- 00bbbbec ["CALL", null, ["callee:00c58210:8"]]
+ 00c38634 ["INT_ADD", "register:40f0:8", ["const:c38634:8", "const:4:8"]]
+ 00c38634 ["CALL", null, ["callee:00c58210:8"]]
- 00bbbbec bytes f57e0094
+ 00c38634 bytes f77e0094
- 00bbbc08 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bbbc08 bytes 40fdff54
- 00bbbc24 ["INT_ADD", "register:40f0:8", ["const:bbbc24:8", "const:4:8"]]
- 00bbbc24 ["CALL", null, ["callee:00c58210:8"]]
+ 00c3866c ["INT_ADD", "register:40f0:8", ["const:c3866c:8", "const:4:8"]]
+ 00c3866c ["CALL", null, ["callee:00c58210:8"]]
- 00bbbc24 bytes e77e0094
+ 00c3866c bytes e97e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a05f047102c7bc22ac48cd473ba37de"></a>

### [`00bbbe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) → [`00c38854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) FUN_00c38854

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) · 呼出先 2件 [`00bbbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`00c38598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md) · 呼出先 2件 [`00c38948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 52.63% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbbea8",
      "incomplete_value": true,
      "site": "00bbbeb8",
      "value": [
        "live",
        "register:40b0:8"
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
      "definition_site": "00bbbeac",
      "incomplete_value": true,
      "site": "00bbbeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbbeb0",
      "incomplete_value": true,
      "site": "00bbbeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
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
      "unmatched:00bbbe30",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbbe34",
      "READ",
      [
        "storage",
        "00c1c068",
        null,
        "pointer"
      ]
    ],
    [
      "00c3888c",
      "PARAM",
      [
        "storage",
        "00c16c10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c38878",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c3887c",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00c3888c",
      "PARAM",
      [
        "storage",
        "00c965b8",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbeb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md#insn-00bbbeb8) · [`00bbbe24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md#insn-00bbbe24) · [`00bbbe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md#insn-00bbbe28)
- 新版 [`00c38900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md#insn-00c38900) · [`00c3886c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md#insn-00c3886c) · [`00c38870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md#insn-00c38870)

~~~diff
- 00bbbeb8 ["INT_ADD", "register:40f0:8", ["const:bbbeb8:8", "const:4:8"]]
- 00bbbeb8 ["CALL", null, ["callee:00c58210:8"]]
+ 00c38900 ["INT_ADD", "register:40f0:8", ["const:c38900:8", "const:4:8"]]
+ 00c38900 ["CALL", null, ["callee:00c58210:8"]]
- 00bbbeb8 bytes 427e0094
+ 00c38900 bytes 447e0094
- 00bbbe24 ["COPY", "register:40a0:8", ["const:c1c000:8"]]
+ 00c3886c ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00bbbe24 bytes 140300b0
+ 00c3886c bytes 140300f0
- 00bbbe28 ["COPY", "register:40a8:8", ["const:c1c000:8"]]
+ 00c38870 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
- 00bbbe28 bytes 150300b0
+ 00c38870 bytes 150300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-792bd44476ac59996884ba234f777a60"></a>

### [`00bbbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) → [`00c38948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md) FUN_00c38948

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) [`00bbbe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) · 呼出先 1件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 2件 [`00c38598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38598.md) [`00c38854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) · 呼出先 1件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 41.67% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3897c",
      "incomplete_value": true,
      "site": "00c38980",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
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
      "unmatched:00bbbf24",
      "READ",
      [
        "storage",
        "00c1c048",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbbf28",
      "READ",
      [
        "storage",
        "00c1c080",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbbf28",
      "PARAM",
      [
        "storage",
        "00c16c88",
        "_ZTIN10__cxxabiv129__pointer_to_member_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c3896c",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00c38970",
      "READ",
      [
        "storage",
        "00c9bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00c38970",
      "PARAM",
      [
        "storage",
        "00c96630",
        "_ZTIN10__cxxabiv129__pointer_to_member_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbf38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md#insn-00bbbf38) · [`00bbbf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md#insn-00bbbf18) · [`00bbbf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md#insn-00bbbf1c)
- 新版 [`00c38980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md#insn-00c38980) · [`00c38960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md#insn-00c38960) · [`00c38964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38948.md#insn-00c38964)

~~~diff
- 00bbbf38 ["INT_ADD", "register:40f0:8", ["const:bbbf38:8", "const:4:8"]]
- 00bbbf38 ["CALL", null, ["callee:00c58210:8"]]
+ 00c38980 ["INT_ADD", "register:40f0:8", ["const:c38980:8", "const:4:8"]]
+ 00c38980 ["CALL", null, ["callee:00c58210:8"]]
- 00bbbf38 bytes 227e0094
+ 00c38980 bytes 247e0094
- 00bbbf18 ["COPY", "register:4040:8", ["const:c1c000:8"]]
+ 00c38960 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bbbf18 bytes 080300b0
+ 00c38960 bytes 080300f0
- 00bbbf1c ["COPY", "register:4010:8", ["const:c1c000:8"]]
+ 00c38964 ["COPY", "register:4010:8", ["const:c9b000:8"]]
- 00bbbf1c bytes 020300b0
+ 00c38964 bytes 020300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d66f6137d5b3f1fec982eef529f564be"></a>

### [`00bbbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md) → [`00c389e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md) FUN_00c389e8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 65.93% / 新版 65.93%

CFGの説明率　旧版 30.77% / 新版 32.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbfa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbfa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbfa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbbfa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbfa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbfac",
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
      "00c389ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c389f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c389f4",
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

- 旧版 [`00bbbfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md#insn-00bbbfa4) · [`00bbbfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md#insn-00bbbfa8) · [`00bbbfac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md#insn-00bbbfac)

~~~diff
- 00bbbfa4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbbfa4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbbfa4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbbfa4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbbfa4 bytes fd7bbda9
- 00bbbfa8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbbfa8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbbfa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbbfa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbfa8 bytes f65701a9
- 00bbbfac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbbfac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbbfac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbbfac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbfac bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5760dfa3a74479b1db5701399f46a33f"></a>

### [`00bbc10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc10c.md) → [`00c38b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md) FUN_00c38b54

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.71% / 新版 87.71%

CFGの説明率　旧版 42.86% / 新版 46.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc1ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc1e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c38bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbc1ec"
      ]
    ],
    [
      "unmatched:00bbc1ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38e94"
      ]
    ],
    [
      "unmatched:00bbc1e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38bc8"
      ]
    ]
  ],
  "added": [
    [
      "00c38bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38c34"
      ]
    ],
    [
      "00c38bf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38e94"
      ]
    ],
    [
      "00c38c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c38bc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc10c.md#insn-00bbc15c) · [`00bbc1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc10c.md#insn-00bbc1ac) · [`00bbc1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc10c.md#insn-00bbc1e8)
- 新版 [`00c38ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38b54.md#insn-00c38ba4)

~~~diff
- 00bbc15c ["INT_ADD", "register:40f0:8", ["const:bbc15c:8", "const:4:8"]]
- 00bbc15c ["CALL", null, ["callee:00c5b450:8"]]
+ 00c38ba4 ["INT_ADD", "register:40f0:8", ["const:c38ba4:8", "const:4:8"]]
+ 00c38ba4 ["CALL", null, ["callee:00c5b450:8"]]
- 00bbc15c bytes 1d8a0094
+ 00c38ba4 bytes 2b8a0094
- 00bbc1ac ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bbc1ac ["CBRANCH", null, ["local:b68:8", "tmp:0:1"]]
- 00bbc1ac bytes 08150034
- 00bbc1e8 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00bbc1e8 bytes c0fcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28a01c41d19ccc83aa175d41f22c4534"></a>

### [`00bbc4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc4bc.md) → [`00c38f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38f04.md) FUN_00c38f04

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 37.78% / 新版 40.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc4c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc4c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc4c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc4c8",
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
      "00c38f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c38f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c38f10",
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

- 旧版 [`00bbc4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc4bc.md#insn-00bbc4c0) · [`00bbc4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc4bc.md#insn-00bbc4c4) · [`00bbc4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc4bc.md#insn-00bbc4c8)

~~~diff
- 00bbc4c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbc4c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbc4c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bbc4c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbc4c0 bytes fd7bbca9
- 00bbc4c4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbc4c4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbc4c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbc4c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc4c4 bytes f85f01a9
- 00bbc4c8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc4c8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc4c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbc4c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc4c8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772b41542b03a72ab5bf853b4c3249d0"></a>

### [`00bbc66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc66c.md) → [`00c390b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c390b4.md) FUN_00c390b4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 48.65% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc6e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc6f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc728"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc6e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39194"
      ]
    ],
    [
      "unmatched:00bbc6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c391c4"
      ]
    ],
    [
      "unmatched:00bbc728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39188"
      ]
    ]
  ],
  "added": [
    [
      "00c3912c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39194"
      ]
    ],
    [
      "00c3913c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c391c4"
      ]
    ],
    [
      "00c39170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39188"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc66c.md#insn-00bbc6b0) · [`00bbc6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc66c.md#insn-00bbc6e4) · [`00bbc6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbc66c.md#insn-00bbc6f4)
- 新版 [`00c390f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c390b4.md#insn-00c390f8)

~~~diff
- 00bbc6b0 ["INT_ADD", "register:40f0:8", ["const:bbc6b0:8", "const:4:8"]]
- 00bbc6b0 ["CALL", null, ["callee:00c5b450:8"]]
+ 00c390f8 ["INT_ADD", "register:40f0:8", ["const:c390f8:8", "const:4:8"]]
+ 00c390f8 ["CALL", null, ["callee:00c5b450:8"]]
- 00bbc6b0 bytes c8880094
+ 00c390f8 bytes d6880094
- 00bbc6e4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00bbc6e4 bytes 40030054
- 00bbc6f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbc6f4 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00bbc6f4 bytes 41040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e851b63d68e29393c85b13c8b950029"></a>

### [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) → [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) __cxa_demangle

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e30.md) · 呼出先 10件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5e9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9f0.md) · 呼出先 10件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.17% / 新版 80.17%

CFGの説明率　旧版 42.41% / 新版 46.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `store_condition` 5件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbcc20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbcc24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbcc28",
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
      "00c39668",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3966c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c39670",
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

- 旧版 [`00bbcc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md#insn-00bbcc20) · [`00bbcc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md#insn-00bbcc24) · [`00bbcc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md#insn-00bbcc28)

~~~diff
- 00bbcc20 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbcc20 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbcc20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbcc20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbcc20 bytes f85f03a9
- 00bbcc24 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbcc24 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbcc24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bbcc24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbcc24 bytes f65704a9
- 00bbcc28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbcc28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbcc28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bbcc28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbcc28 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bcb256d4ce2ebbc467780b5bd1a20d"></a>

### [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) → [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) FUN_00c39cf0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 7.69% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c39d10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39d18",
      "incomplete_value": true,
      "site": "00c39d20",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00bbd2c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39d28"
      ]
    ]
  ],
  "added": [
    [
      "00c39d10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c39d28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md#insn-00bbd2c8) · [`00bbd2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md#insn-00bbd2d8)
- 新版 [`00c39d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md#insn-00c39d20) · [`00c39d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md#insn-00c39d10)

~~~diff
- 00bbd2c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbd2c8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbd2c8 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00bbd2c8 bytes c8000054
- 00bbd2d8 ["INT_ADD", "register:40f0:8", ["const:bbd2d8:8", "const:4:8"]]
- 00bbd2d8 ["CALL", null, ["callee:00c57c50:8"]]
+ 00c39d20 ["INT_ADD", "register:40f0:8", ["const:c39d20:8", "const:4:8"]]
+ 00c39d20 ["CALL", null, ["callee:00c57c50:8"]]
- 00bbd2d8 bytes ca770094
+ 00c39d20 bytes cc770094
+ 00c39d10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c39d10 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c39d10 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00c39d10 bytes c8000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcff9b304300f6a65e0db2d874abbaec"></a>

### [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) → [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) FUN_00c39d50

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00bbcc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbc/00bbcc10.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 31件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bbdda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdda8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md)
- 新版 呼出元 5件 [`00c39658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39658.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 31件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c3a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a7f0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.57% / 新版 82.57%

CFGの説明率　旧版 37.38% / 新版 42.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 2件, `return_value_candidate` 1件, `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd310",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd314",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd318",
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
      "00c39d58",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c39d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c39d60",
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

- 旧版 [`00bbd310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md#insn-00bbd310) · [`00bbd314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md#insn-00bbd314) · [`00bbd318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md#insn-00bbd318)

~~~diff
- 00bbd310 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbd310 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbd310 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00bbd310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd310 bytes fd7b10a9
- 00bbd314 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bbd314 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bbd314 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00bbd314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd314 bytes fc6f11a9
- 00bbd318 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bbd318 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bbd318 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00bbd318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd318 bytes fa6712a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772e5a44e64a09592ed8734dce22d16f"></a>

### [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) → [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) FUN_00c3a764

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc93c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 5.00% / 新版 5.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbdd94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3a7dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbdd30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbdd30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7a0"
      ]
    ],
    [
      "unmatched:00bbdd3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7a0"
      ]
    ],
    [
      "unmatched:00bbdd5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7b8"
      ]
    ]
  ],
  "added": [
    [
      "00c3a778",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7a0"
      ]
    ],
    [
      "00c3a784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7a0"
      ]
    ],
    [
      "00c3a7a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3a7b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbdd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md#insn-00bbdd30) · [`00bbdd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md#insn-00bbdd3c) · [`00bbdd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md#insn-00bbdd5c)

~~~diff
- 00bbdd30 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
- 00bbdd30 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bbdd30 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bbdd30 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bbdd30 bytes 41010036
- 00bbdd3c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00bbdd3c bytes e0000054
- 00bbdd5c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00bbdd5c bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec743663f139c7924ae738a33fb61fc"></a>

### [`00bbf1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md) → [`00c3bc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md) FUN_00c3bc3c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 2件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf2e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf2f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbf25c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3bcc8"
      ]
    ]
  ],
  "added": [
    [
      "00c3bca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3bcc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbf25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md#insn-00bbf25c) · [`00bbf2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md#insn-00bbf2e0) · [`00bbf2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md#insn-00bbf2e8)

~~~diff
- 00bbf25c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bbf25c bytes 20010054
- 00bbf2e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:48:8"]]
- 00bbf2e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbf2e0 bytes 682600f9
- 00bbf2e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:248:8"]]
- 00bbf2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bbf2e8 bytes 892601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8e283387879d6d20550f2c5bce41a56"></a>

### [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) → [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) FUN_00c3bde4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc5b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md) · 呼出先 19件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bbf1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf1f4.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md)
- 新版 呼出元 7件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c42598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md) · 呼出先 19件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c3bc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bc3c.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3cc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 56.83% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `return_value_candidate` 1件, `store_condition` 3件, `store_value` 3件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf3f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf698"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbf3f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3bf6c"
      ]
    ],
    [
      "unmatched:00bbf4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c484"
      ]
    ],
    [
      "unmatched:00bbf4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c31c"
      ]
    ]
  ],
  "added": [
    [
      "00c3be3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3bf6c"
      ]
    ],
    [
      "00c3bf04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c484"
      ]
    ],
    [
      "00c3bf2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c31c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbf3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md#insn-00bbf3f0) · [`00bbf3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md#insn-00bbf3f4) · [`00bbf42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md#insn-00bbf42c)
- 新版 [`00c3be74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md#insn-00c3be74)

~~~diff
- 00bbf3f0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bbf3f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbf3f0 bytes 680200f9
- 00bbf3f4 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00bbf3f4 bytes 80090054
- 00bbf42c ["INT_ADD", "register:40f0:8", ["const:bbf42c:8", "const:4:8"]]
- 00bbf42c ["CALL", null, ["callee:00c3e02c:8"]]
+ 00c3be74 ["INT_ADD", "register:40f0:8", ["const:c3be74:8", "const:4:8"]]
+ 00c3be74 ["CALL", null, ["callee:00c3e02c:8"]]
- 00bbf42c bytes 6e080094
+ 00c3be74 bytes 6e080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cce155f19abafd4c83c491489cfee39"></a>

### [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) → [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) FUN_00c3c518

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 13件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md)
- 新版 呼出元 4件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 13件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.66% / 新版 83.66%

CFGの説明率　旧版 55.68% / 新版 61.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfcdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfcdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbfb78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c6dc"
      ]
    ],
    [
      "unmatched:00bbfcc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbfce8"
      ]
    ],
    [
      "unmatched:00bbfcd0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ]
  ],
  "added": [
    [
      "00c3c5c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c6dc"
      ]
    ],
    [
      "00c3c710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c730"
      ]
    ],
    [
      "00c3c718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md#insn-00bbfb78) · [`00bbfcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md#insn-00bbfcc8) · [`00bbfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md#insn-00bbfcd0)

~~~diff
- 00bbfb78 ["CBRANCH", null, ["local:b38:8", "register:101:1"]]
- 00bbfb78 bytes e0080054
- 00bbfcc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbfcc8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbfcc8 ["CBRANCH", null, ["local:b44:8", "tmp:1:1"]]
- 00bbfcc8 bytes 08010054
- 00bbfcd0 ["INT_ADD", "register:40f0:8", ["const:bbfcd0:8", "const:4:8"]]
- 00bbfcd0 ["CALL", null, ["callee:00c59c20:8"]]
- 00bbfcd0 bytes 40750094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f693dbfc2a67a8edea667f33d9d1a0"></a>

### [`00bbfdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md) → [`00c3c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md) FUN_00c3c840

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 4件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 35.29% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfe08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfe08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3c850"
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
      "unmatched:00bbfe08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbfe18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c8ec"
      ]
    ],
    [
      "unmatched:00bbfe38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c8a0"
      ]
    ]
  ],
  "added": [
    [
      "00c3c850",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c3c860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c8ec"
      ]
    ],
    [
      "00c3c880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3c8a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfe08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md#insn-00bbfe08) · [`00bbfe18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md#insn-00bbfe18) · [`00bbfe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md#insn-00bbfe38)

~~~diff
- 00bbfe08 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbfe08 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbfe08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbfe08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbfe08 bytes f44f03a9
- 00bbfe18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbfe18 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bbfe18 bytes 61040054
- 00bbfe38 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00bbfe38 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f69acc7bcecb73d69f8689fbd647fb"></a>

### [`00bbfed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md) → [`00c3c918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c918.md) FUN_00c3c918

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfed8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbfed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbfed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbfedc",
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
      "00c3c91c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3c920",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3c924",
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

- 旧版 [`00bbfed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md#insn-00bbfed4) · [`00bbfed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md#insn-00bbfed8) · [`00bbfedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfed0.md#insn-00bbfedc)

~~~diff
- 00bbfed4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbfed4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbfed4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbfed4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbfed4 bytes fd7bbda9
- 00bbfed8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbfed8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bbfed8 bytes f50b00f9
- 00bbfedc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbfedc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbfedc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbfedc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbfedc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908d1159f474109e0995d46a9e4a848c"></a>

### [`00bc00cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc00cc.md) → [`00c3cb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cb14.md) FUN_00c3cb14

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 70.49% / 新版 70.49%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc00dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc00dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc00e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc00dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc00e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc00e4",
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
      "00c3cb24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3cb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3cb2c",
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

- 旧版 [`00bc00dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc00cc.md#insn-00bc00dc) · [`00bc00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc00cc.md#insn-00bc00e0) · [`00bc00e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc00cc.md#insn-00bc00e4)

~~~diff
- 00bc00dc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bc00dc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bc00dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bc00dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc00dc bytes f85f03a9
- 00bc00e0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc00e0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc00e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bc00e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc00e0 bytes f65704a9
- 00bc00e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc00e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc00e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bc00e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc00e4 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2369b410b8bf108efa1f640dfc26591"></a>

### [`00bc01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md) → [`00c3cc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cc08.md) FUN_00c3cc08

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 2件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 71.43% / 新版 64.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc020c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc02b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3cd6c"
      ]
    ]
  ],
  "added": [
    [
      "00c3cd00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3cd6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc020c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md#insn-00bc020c) · [`00bc0214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md#insn-00bc0214) · [`00bc0248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc01c0.md#insn-00bc0248)

~~~diff
- 00bc020c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2a0:8"]]
- 00bc020c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc020c bytes c85201f9
- 00bc0214 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc0214 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc0214 bytes 690a00f9
- 00bc0248 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2a8:8"]]
- 00bc0248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc0248 bytes c85601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ae6a5d169dc8db8fd5d380d30f57e85"></a>

### [`00bc03a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc03a0.md) → [`00c3cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cde8.md) FUN_00c3cde8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc03fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0418"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0404",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc0428",
      "DATA",
      [
        "storage",
        "002aa381",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3ce4c",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ce70",
      "DATA",
      [
        "storage",
        "002bb0fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc03fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc03a0.md#insn-00bc03fc) · [`00bc0404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc03a0.md#insn-00bc0404) · [`00bc0418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc03a0.md#insn-00bc0418)

~~~diff
- 00bc03fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc03fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc03fc bytes a90600f9
- 00bc0404 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0404 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc0404 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc0404 bytes 080c01f8
- 00bc0418 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bc0418 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc0418 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc0418 bytes 08200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d89f9f8d981b7e7699546ecd33a8439"></a>

### [`00bc0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0450.md) → [`00c3ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3ce98.md) FUN_00c3ce98

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0454",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc0458",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc045c",
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
      "00c3ce9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3cea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3cea4",
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

- 旧版 [`00bc0454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0450.md#insn-00bc0454) · [`00bc0458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0450.md#insn-00bc0458) · [`00bc045c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0450.md#insn-00bc045c)

~~~diff
- 00bc0454 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc0454 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc0454 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc0454 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc0454 bytes fd7bbda9
- 00bc0458 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc0458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc0458 bytes f50b00f9
- 00bc045c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc045c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc045c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc045c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc045c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13bb35a908dded016af3d41ff2443281"></a>

### [`00bc0500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0500.md) → [`00c3cf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md) FUN_00c3cf48

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3cfac",
      "incomplete_value": false,
      "site": "00c3cfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0564",
      "incomplete_value": false,
      "site": "00bc0564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "site": "00bc0578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0588"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3cfac",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc0588",
      "DATA",
      [
        "storage",
        "0029085c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3cfac",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3cfd0",
      "DATA",
      [
        "storage",
        "0029fd9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0500.md#insn-00bc0578) · [`00bc0588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0500.md#insn-00bc0588)
- 新版 [`00c3cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cf48.md#insn-00c3cfc0)

~~~diff
- 00bc0578 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bc0578 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc0578 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc0578 bytes 08200039
- 00bc0588 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0588 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00bc0588 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 00bc0588 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc0588 bytes 083001a9
+ 00c3cfc0 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00c3cfc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
+ 00c3cfc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c3cfc0 bytes 08200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376123d8940c71e64b55ecf5c48cd3c4"></a>

### [`00bc05b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc05b0.md) → [`00c3cff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md) FUN_00c3cff8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d05c",
      "incomplete_value": false,
      "site": "00c3d05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0614",
      "incomplete_value": false,
      "site": "00bc0614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00c3d080",
      "incomplete_value": false,
      "site": "00c3d080",
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
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0638",
      "incomplete_value": false,
      "site": "00bc0638",
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
            "const:187:8"
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
      "00c3d05c",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d080",
      "DATA",
      [
        "storage",
        "002a2187",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d05c",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d080",
      "DATA",
      [
        "storage",
        "002b2848",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc05e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc05b0.md#insn-00bc05e4) · [`00bc0604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc05b0.md#insn-00bc0604) · [`00bc0608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc05b0.md#insn-00bc0608)
- 新版 [`00c3d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d02c) · [`00c3d04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d04c) · [`00c3d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3cff8.md#insn-00c3d050)

~~~diff
- 00bc05e4 ["INT_ADD", "register:40f0:8", ["const:bc05e4:8", "const:4:8"]]
- 00bc05e4 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3d02c ["INT_ADD", "register:40f0:8", ["const:c3d02c:8", "const:4:8"]]
+ 00c3d02c ["CALL", null, ["callee:00c59c20:8"]]
- 00bc05e4 bytes fb720094
+ 00c3d02c bytes fd720094
- 00bc0604 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00c3d04c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc0604 bytes a80200f0
+ 00c3d04c bytes c80200d0
- 00bc0608 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 00bc0608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d050 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 00c3d050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0608 bytes 08a11e91
+ 00c3d050 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3564b4e9d1fc8675179510151f1bceac"></a>

### [`00bc0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0660.md) → [`00c3d0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d0a8.md) FUN_00c3d0a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0664",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc0668",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc066c",
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
      "00c3d0ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3d0b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3d0b4",
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

- 旧版 [`00bc0664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0660.md#insn-00bc0664) · [`00bc0668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0660.md#insn-00bc0668) · [`00bc066c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0660.md#insn-00bc066c)

~~~diff
- 00bc0664 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc0664 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc0664 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc0664 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc0664 bytes fd7bbda9
- 00bc0668 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc0668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc0668 bytes f50b00f9
- 00bc066c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc066c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc066c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc066c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc066c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19655ab9de2a4a1607591699628cd30e"></a>

### [`00bc0710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0710.md) → [`00c3d158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d158.md) FUN_00c3d158

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 85.48% / 新版 86.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0878"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c3d2c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bc0878"
      ],
      [
        "FALL_THROUGH",
        "00c3d2c0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c3d2c0",
      "incomplete_value": true,
      "site": "00c3d2c8",
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
                "const:0:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0878",
      "incomplete_value": true,
      "site": "00bc0880",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
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
      "unmatched:00bc0878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3d2cc"
      ]
    ]
  ],
  "added": [
    [
      "00c3d2c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3d2cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0710.md#insn-00bc0878) · [`00bc08b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0710.md#insn-00bc08b8)
- 新版 [`00c3d2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d158.md#insn-00c3d2c0) · [`00c3d300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d158.md#insn-00c3d300)

~~~diff
- 00bc0878 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc0878 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 00bc0878 bytes 61000054
+ 00c3d2c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c3d2c0 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
+ 00c3d2c0 bytes 61000054
- 00bc08b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc08b8 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 00c3d300 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c3d300 ["CBRANCH", null, ["local:b33:8", "tmp:0:1"]]
- 00bc08b8 bytes 21ffff54
+ 00c3d300 bytes 21ffff54
~~~


<a id="compare-a79cb966c786dacb15216cf6d1eb5d00"></a>

### [`00bc08c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc08c0.md) → [`00c3d308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d308.md) FUN_00c3d308

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc091c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0924",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc0948",
      "DATA",
      [
        "storage",
        "002a919e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d36c",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d390",
      "DATA",
      [
        "storage",
        "002b9e35",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc091c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc08c0.md#insn-00bc091c) · [`00bc0924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc08c0.md#insn-00bc0924) · [`00bc0948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc08c0.md#insn-00bc0948)

~~~diff
- 00bc091c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc091c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc091c bytes a90600f9
- 00bc0924 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0924 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc0924 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc0924 bytes 080c01f8
- 00bc0948 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0948 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00bc0948 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 00bc0948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc0948 bytes 083001a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf90c07d3446c9570e10a79b2da5447c"></a>

### [`00bc0970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0970.md) → [`00c3d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md) FUN_00c3d3b8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d420",
      "incomplete_value": false,
      "site": "00c3d420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc09d8",
      "incomplete_value": false,
      "site": "00bc09d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "00c3d420",
      "DATA",
      [
        "storage",
        "00c17828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3d420",
      "DATA",
      [
        "storage",
        "00c971d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc09a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0970.md#insn-00bc09a8) · [`00bc09c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0970.md#insn-00bc09c8) · [`00bc09cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0970.md#insn-00bc09cc)
- 新版 [`00c3d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d3f0) · [`00c3d410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d410) · [`00c3d414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d3b8.md#insn-00c3d414)

~~~diff
- 00bc09a8 ["INT_ADD", "register:40f0:8", ["const:bc09a8:8", "const:4:8"]]
- 00bc09a8 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3d3f0 ["INT_ADD", "register:40f0:8", ["const:c3d3f0:8", "const:4:8"]]
+ 00c3d3f0 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc09a8 bytes 0a720094
+ 00c3d3f0 bytes 0c720094
- 00bc09c8 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00c3d410 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc09c8 bytes a80200f0
+ 00c3d410 bytes c80200d0
- 00bc09cc ["COPY", "tmp:0:8", ["const:828:8"]]
- 00bc09cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc09cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc09cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d414 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 00c3d414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc09cc bytes 08a12091
+ 00c3d414 bytes 08410791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96cf4497f72a8ec328638ff966ae000"></a>

### [`00bc0a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0a18.md) → [`00c3d460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md) FUN_00c3d460

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d4c4",
      "incomplete_value": false,
      "site": "00c3d4c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0a7c",
      "incomplete_value": false,
      "site": "00bc0a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00c3d4e8",
      "incomplete_value": false,
      "site": "00c3d4e8",
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
            "const:8a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0aa0",
      "incomplete_value": false,
      "site": "00bc0aa0",
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
            "const:2fe:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0a40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0a40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3d4ac"
      ]
    ],
    [
      "00c3d4c4",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d4e8",
      "DATA",
      [
        "storage",
        "002a02fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d488",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3d4ac"
      ]
    ],
    [
      "00c3d4c4",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d4e8",
      "DATA",
      [
        "storage",
        "002b08a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0a18.md#insn-00bc0a40) · [`00bc0a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0a18.md#insn-00bc0a34)
- 新版 [`00c3d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d460.md#insn-00c3d488)

~~~diff
- 00bc0a40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc0a40 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc0a40 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bc0a40 bytes 28010054
+ 00c3d488 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c3d488 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c3d488 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c3d488 bytes 28010054
- 00bc0a34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc0a34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc0a34 bytes a80640f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5930f6f823b3e1f3c17ad277a69a0508"></a>

### [`00bc0b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0b78.md) → [`00c3d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d5c0.md) FUN_00c3d5c0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 74.42% / 新版 74.42%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0bf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc0bdc",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc0c00",
      "DATA",
      [
        "storage",
        "00298b10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d624",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d648",
      "DATA",
      [
        "storage",
        "002a88ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0b78.md#insn-00bc0bd4) · [`00bc0bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0b78.md#insn-00bc0bdc) · [`00bc0bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0b78.md#insn-00bc0bf8)

~~~diff
- 00bc0bd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc0bd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc0bd4 bytes a90600f9
- 00bc0bdc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc0bdc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc0bdc ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc0bdc bytes 080c01f8
- 00bc0bf8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc0bf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc0bf8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc0bf8 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a795db2129d9498bcf4b93699985f18"></a>

### [`00bc0c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0c24.md) → [`00c3d66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md) FUN_00c3d66c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d6d0",
      "incomplete_value": false,
      "site": "00c3d6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0c88",
      "incomplete_value": false,
      "site": "00bc0c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00c3d6f4",
      "incomplete_value": false,
      "site": "00c3d6f4",
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
            "const:f66:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0cac",
      "incomplete_value": false,
      "site": "00bc0cac",
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
            "const:9bd:8"
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
      "00c3d6d0",
      "DATA",
      [
        "storage",
        "00c177a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d6f4",
      "DATA",
      [
        "storage",
        "002b09bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3d6d0",
      "DATA",
      [
        "storage",
        "00c97150",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d6f4",
      "DATA",
      [
        "storage",
        "002c1f66",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0c24.md#insn-00bc0c58) · [`00bc0c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0c24.md#insn-00bc0c78) · [`00bc0c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0c24.md#insn-00bc0c7c)
- 新版 [`00c3d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6a0) · [`00c3d6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6c0) · [`00c3d6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d66c.md#insn-00c3d6c4)

~~~diff
- 00bc0c58 ["INT_ADD", "register:40f0:8", ["const:bc0c58:8", "const:4:8"]]
- 00bc0c58 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3d6a0 ["INT_ADD", "register:40f0:8", ["const:c3d6a0:8", "const:4:8"]]
+ 00c3d6a0 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc0c58 bytes 5e710094
+ 00c3d6a0 bytes 60710094
- 00bc0c78 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00c3d6c0 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc0c78 bytes a80200f0
+ 00c3d6c0 bytes c80200d0
- 00bc0c7c ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 00bc0c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3d6c4 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 00c3d6c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d6c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3d6c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0c7c bytes 08a11e91
+ 00c3d6c4 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77abffd4198de0d7c35a988272bc8a87"></a>

### [`00bc0cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md) → [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) FUN_00c3d71c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) · 呼出先 6件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 2件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) · 呼出先 6件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 99.11% / 新版 99.11%

CFGの説明率　旧版 86.49% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d778",
      "DATA",
      [
        "storage",
        "00c17908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3d778",
      "DATA",
      [
        "storage",
        "00c972b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md#insn-00bc0cfc) · [`00bc0d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md#insn-00bc0d08) · [`00bc0d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md#insn-00bc0d0c)
- 新版 [`00c3d744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md#insn-00c3d744) · [`00c3d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md#insn-00c3d750) · [`00c3d754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md#insn-00c3d754)

~~~diff
- 00bc0cfc ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
+ 00c3d744 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00bc0cfc bytes 000b0054
+ 00c3d744 bytes 000b0054
- 00bc0d08 ["COPY", "register:40c0:8", ["const:c17000:8"]]
+ 00c3d750 ["COPY", "register:40c0:8", ["const:c97000:8"]]
- 00bc0d08 bytes b80200f0
+ 00c3d750 bytes d80200d0
- 00bc0d0c ["COPY", "tmp:0:8", ["const:908:8"]]
- 00bc0d0c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00bc0d0c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00bc0d0c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00c3d754 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00c3d754 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00c3d754 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00c3d754 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00bc0d0c bytes 18232491
+ 00c3d754 bytes 18c30a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08fd6868bc62b8c88a329402d19642d7"></a>

### [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) → [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) FUN_00c3db88

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 7件 [`00bc0cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc0/00bc0cd4.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bc561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc561c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 7件 [`00c3d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3d71c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c42064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42064.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 90.00% / 新版 93.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3dca8",
      "incomplete_value": false,
      "site": "00c3dca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1260",
      "incomplete_value": false,
      "site": "00bc1260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c3dca8",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dcb4",
      "DATA",
      [
        "storage",
        "0029f311",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3dca8",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dcb4",
      "DATA",
      [
        "storage",
        "002af724",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc115c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md#insn-00bc115c) · [`00bc116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md#insn-00bc116c) · [`00bc11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md#insn-00bc11a4)
- 新版 [`00c3dba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dba4) · [`00c3dbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dbb4) · [`00c3dbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md#insn-00c3dbec)

~~~diff
- 00bc115c ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00c3dba4 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bc115c bytes 40090054
+ 00c3dba4 bytes 40090054
- 00bc116c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bc116c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00c3dbb4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c3dbb4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bc116c bytes c3080054
+ 00c3dbb4 bytes c3080054
- 00bc11a4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00c3dbec ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00bc11a4 bytes e0000054
+ 00c3dbec bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1217dd367f8e9a3df8bdad116eb8554f"></a>

### [`00bc136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md) → [`00c3ddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3ddb4.md) FUN_00c3ddb4

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc13c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc13d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc13ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc13d0",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3de18",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc13c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md#insn-00bc13c8) · [`00bc13d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md#insn-00bc13d0) · [`00bc13ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc136c.md#insn-00bc13ec)

~~~diff
- 00bc13c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc13c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc13c8 bytes a90600f9
- 00bc13d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc13d0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc13d0 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc13d0 bytes 080c01f8
- 00bc13ec ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bc13ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:9:8"]]
- 00bc13ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00bc13ec bytes 08900078
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47da337813ff851b8feacc53f1fbc5ae"></a>

### [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) → [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) FUN_00c3e02c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 4件 [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 4件 [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.70% / 新版 83.70%

CFGの説明率　旧版 60.71% / 新版 60.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc16c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc16cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc16d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc16cc",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc16f4",
      "DATA",
      [
        "storage",
        "002a80a2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3e114",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e13c",
      "DATA",
      [
        "storage",
        "002b8d44",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc168c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md#insn-00bc168c) · [`00bc16c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md#insn-00bc16c4) · [`00bc16cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md#insn-00bc16cc)
- 新版 [`00c3e0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md#insn-00c3e0d4)

~~~diff
- 00bc168c ["INT_ADD", "register:40f0:8", ["const:bc168c:8", "const:4:8"]]
- 00bc168c ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3e0d4 ["INT_ADD", "register:40f0:8", ["const:c3e0d4:8", "const:4:8"]]
+ 00c3e0d4 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc168c bytes d16e0094
+ 00c3e0d4 bytes d36e0094
- 00bc16c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8:8"]]
- 00bc16c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc16c4 bytes 880600f9
- 00bc16cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bc16cc ["INT_ADD", "register:4098:8", ["register:4098:8", "const:10:8"]]
- 00bc16cc ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00bc16cc bytes 690e01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ecf0884861478008d9ddffc1fa5c74"></a>

### [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) → [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) FUN_00c3e19c

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) · 呼出先 8件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) · 呼出先 8件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.07% / 新版 80.07%

CFGの説明率　旧版 55.12% / 新版 52.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1764",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1768",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc176c",
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
      "00c3e1ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c3e1b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3e1b4",
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

- 旧版 [`00bc1764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md#insn-00bc1764) · [`00bc1768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md#insn-00bc1768) · [`00bc176c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md#insn-00bc176c)

~~~diff
- 00bc1764 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bc1764 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bc1764 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bc1764 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1764 bytes fa6703a9
- 00bc1768 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bc1768 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bc1768 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bc1768 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1768 bytes f85f04a9
- 00bc176c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc176c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc176c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bc176c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc176c bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b98e3b701c24a65e1c12a5114c7021f"></a>

### [`00bc1c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md) → [`00c3e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md) FUN_00c3e66c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e6d4",
      "incomplete_value": false,
      "site": "00c3e6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c8c",
      "incomplete_value": false,
      "site": "00bc1c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00c3e6d4",
      "DATA",
      [
        "storage",
        "00c19798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e6d4",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md#insn-00bc1c5c) · [`00bc1c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md#insn-00bc1c7c) · [`00bc1c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md#insn-00bc1c80)
- 新版 [`00c3e6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e6a4) · [`00c3e6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e6c4) · [`00c3e6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md#insn-00c3e6c8)

~~~diff
- 00bc1c5c ["INT_ADD", "register:40f0:8", ["const:bc1c5c:8", "const:4:8"]]
- 00bc1c5c ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3e6a4 ["INT_ADD", "register:40f0:8", ["const:c3e6a4:8", "const:4:8"]]
+ 00c3e6a4 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc1c5c bytes 5d6d0094
+ 00c3e6a4 bytes 5f6d0094
- 00bc1c7c ["COPY", "register:4040:8", ["const:c19000:8"]]
+ 00c3e6c4 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00bc1c7c bytes c8020090
+ 00c3e6c4 bytes c80200f0
- 00bc1c80 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e6c8 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00c3e6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1c80 bytes 08611e91
+ 00c3e6c8 bytes 08010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28faf93aebd4e76adb103e61e992fc2"></a>

### [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) → [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) FUN_00c3e714

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 7件 [`00bc2b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md) [`00bc2bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 4件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 7件 [`00c3f548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md) [`00c3f620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.55% / 新版 87.55%

CFGの説明率　旧版 80.22% / 新版 81.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1cdc",
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
      "00c3e71c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c3e720",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3e724",
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

- 旧版 [`00bc1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md#insn-00bc1cd4) · [`00bc1cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md#insn-00bc1cd8) · [`00bc1cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md#insn-00bc1cdc)

~~~diff
- 00bc1cd4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1cd4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1cd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1cd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1cd4 bytes fd7b01a9
- 00bc1cd8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bc1cd8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bc1cd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc1cd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1cd8 bytes f85f02a9
- 00bc1cdc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc1cdc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc1cdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bc1cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1cdc bytes f65703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e14d487c4a7171672d97bca6d147d58b"></a>

### [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) → [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) FUN_00c3ead8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 3件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 3件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 3件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 79.17% / 新版 79.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ebb4",
      "incomplete_value": false,
      "site": "00c3ebb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc216c",
      "incomplete_value": false,
      "site": "00bc216c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "definition_site": "00c3ebd4",
      "incomplete_value": false,
      "site": "00c3ebd4",
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
            "const:54c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc218c",
      "incomplete_value": false,
      "site": "00bc218c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:1c7:8"
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
      "00c3ebb4",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ebd4",
      "DATA",
      [
        "storage",
        "0029e1c7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3ebb4",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ebd4",
      "DATA",
      [
        "storage",
        "002ae54c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc20a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md#insn-00bc20a0) · [`00bc20d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md#insn-00bc20d4) · [`00bc20f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md#insn-00bc20f0)
- 新版 [`00c3eb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md#insn-00c3eb1c) · [`00c3eb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md#insn-00c3eb38)

~~~diff
- 00bc20a0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00bc20a0 bytes fd030091
- 00bc20d4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00c3eb1c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00bc20d4 bytes 80000054
+ 00c3eb1c bytes 80000054
- 00bc20f0 ["INT_ADD", "register:40f0:8", ["const:bc20f0:8", "const:4:8"]]
- 00bc20f0 ["CALL", null, ["callee:00c3f954:8"]]
+ 00c3eb38 ["INT_ADD", "register:40f0:8", ["const:c3eb38:8", "const:4:8"]]
+ 00c3eb38 ["CALL", null, ["callee:00c3f954:8"]]
- 00bc20f0 bytes 87030094
+ 00c3eb38 bytes 87030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de9987db93edc0fa381c00a904f4c781"></a>

### [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) → [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) FUN_00c3ec0c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bc15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc15e4.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) · 呼出先 6件 [`00bcf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 3件 [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3e02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e02c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) · 呼出先 6件 [`00c4be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4be00.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.98% / 新版 87.98%

CFGの説明率　旧版 77.38% / 新版 73.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc23d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc23d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc23e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc21e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3eccc"
      ]
    ],
    [
      "00c3edac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3ed18"
      ]
    ],
    [
      "unmatched:00bc2364",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3edb4"
      ]
    ]
  ],
  "added": [
    [
      "00c3ec2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3eccc"
      ]
    ],
    [
      "00c3ecf4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3ed18"
      ]
    ],
    [
      "00c3edac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3edb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc21e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md#insn-00bc21e4) · [`00bc23d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md#insn-00bc23d0) · [`00bc23d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md#insn-00bc23d4)

~~~diff
- 00bc21e4 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00bc21e4 bytes 00050054
- 00bc23d0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc23d0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:8:8"]]
- 00bc23d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc23d0 bytes 89220039
- 00bc23d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c:8"]]
- 00bc23d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:4"]]
- 00bc23d4 bytes 930e00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f27faffc19a22b05eefcb8fc02e2523"></a>

### [`00bc2a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2a60.md) → [`00c3f4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md) FUN_00c3f4a8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f50c",
      "incomplete_value": false,
      "site": "00c3f50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ac4",
      "incomplete_value": false,
      "site": "00bc2ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c3f50c",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f50c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2a60.md#insn-00bc2a94) · [`00bc2ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2a60.md#insn-00bc2ab4) · [`00bc2ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2a60.md#insn-00bc2ab8)
- 新版 [`00c3f4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f4dc) · [`00c3f4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f4fc) · [`00c3f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f4a8.md#insn-00c3f500)

~~~diff
- 00bc2a94 ["INT_ADD", "register:40f0:8", ["const:bc2a94:8", "const:4:8"]]
- 00bc2a94 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3f4dc ["INT_ADD", "register:40f0:8", ["const:c3f4dc:8", "const:4:8"]]
+ 00c3f4dc ["CALL", null, ["callee:00c59c20:8"]]
- 00bc2a94 bytes cf690094
+ 00c3f4dc bytes d1690094
- 00bc2ab4 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00c3f4fc ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc2ab4 bytes a80200b0
+ 00c3f4fc bytes c8020090
- 00bc2ab8 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bc2ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f500 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00c3f500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2ab8 bytes 08612291
+ 00c3f500 bytes 08010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-412f134f8b26865aeb53f36f8984407f"></a>

### [`00bc2b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md) → [`00c3f548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md) FUN_00c3f548

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) · 呼出先 4件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) · 呼出先 4件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 78.57% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md#insn-00bc2b48) · [`00bc2b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md#insn-00bc2b5c) · [`00bc2b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md#insn-00bc2b64)
- 新版 [`00c3f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f590) · [`00c3f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f5a4) · [`00c3f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f548.md#insn-00c3f5ac)

~~~diff
- 00bc2b48 ["INT_ADD", "register:40f0:8", ["const:bc2b48:8", "const:4:8"]]
- 00bc2b48 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c3f590 ["INT_ADD", "register:40f0:8", ["const:c3f590:8", "const:4:8"]]
+ 00c3f590 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc2b48 bytes c2690094
+ 00c3f590 bytes c4690094
- 00bc2b5c ["INT_ADD", "register:40f0:8", ["const:bc2b5c:8", "const:4:8"]]
- 00bc2b5c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c3f5a4 ["INT_ADD", "register:40f0:8", ["const:c3f5a4:8", "const:4:8"]]
+ 00c3f5a4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc2b5c bytes d96d0094
+ 00c3f5a4 bytes e76d0094
- 00bc2b64 ["INT_ADD", "register:40f0:8", ["const:bc2b64:8", "const:4:8"]]
- 00bc2b64 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c3f5ac ["INT_ADD", "register:40f0:8", ["const:c3f5ac:8", "const:4:8"]]
+ 00c3f5ac ["CALL", null, ["callee:00c59c20:8"]]
- 00bc2b64 bytes 9b690094
+ 00c3f5ac bytes 9d690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-697a4a77ae725c09d0f5cd7016f98a0a"></a>

### [`00bc2bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md) → [`00c3f620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f620.md) FUN_00c3f620

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_value, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_value` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f68c",
      "incomplete_value": false,
      "site": "00c3f68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c44",
      "incomplete_value": false,
      "site": "00bc2c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "site": "00bc2c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2c64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3f68c",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f68c",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md#insn-00bc2c5c) · [`00bc2c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md#insn-00bc2c64) · [`00bc2c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2bd8.md#insn-00bc2c68)

~~~diff
- 00bc2c5c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bc2c5c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:8:8"]]
- 00bc2c5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2c5c bytes 8a220039
- 00bc2c64 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2c64 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bc2c64 ["INT_ADD", "tmp:2:8", ["register:40a0:8", "const:10:8"]]
- 00bc2c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2c64 bytes 932201a9
- 00bc2c68 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc2c68 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:9:8"]]
- 00bc2c68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00bc2c68 bytes 89920078
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa682e824c7898c93152a84b3a7ac9ed"></a>

### [`00bc2d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d08.md) → [`00c3f750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md) FUN_00c3f750

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d08.md#insn-00bc2d24) · [`00bc2d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d08.md#insn-00bc2d40) · [`00bc2d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2d08.md#insn-00bc2d54)
- 新版 [`00c3f76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md#insn-00c3f76c) · [`00c3f788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md#insn-00c3f788) · [`00c3f79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f750.md#insn-00c3f79c)

~~~diff
- 00bc2d24 ["BRANCH", null, ["local:b7:8"]]
+ 00c3f76c ["BRANCH", null, ["local:b6:8"]]
- 00bc2d24 bytes 13000014
+ 00c3f76c bytes 13000014
- 00bc2d40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc2d40 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00c3f788 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c3f788 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc2d40 bytes 21010054
+ 00c3f788 bytes 21010054
- 00bc2d54 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2d54 ["INT_ADD", "register:40f0:8", ["const:bc2d54:8", "const:4:8"]]
- 00bc2d54 ["CALLIND", null, ["register:0:8"]]
+ 00c3f79c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3f79c ["INT_ADD", "register:40f0:8", ["const:c3f79c:8", "const:4:8"]]
+ 00c3f79c ["CALLIND", null, ["register:0:8"]]
- 00bc2d54 bytes 20013fd6
+ 00c3f79c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a235e6c192ea0184d027f2363a8ecdfb"></a>

### [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) → [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) FUN_00c3f954

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) · 呼出先 42件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bbfdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfdf8.md)
- 新版 呼出元 14件 [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) · 呼出先 42件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c840.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 51.75% / 新版 51.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 5件, `store_condition` 6件, `store_value` 1件, `unresolved_branch_alignment` 37件, `unresolved_call_alignment` 20件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc325c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2f54",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2f58",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2f5c",
      "DATA",
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
      "00c3f99c",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c3f9a0",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c3f9a4",
      "DATA",
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

- 旧版 [`00bc3250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md#insn-00bc3250) · [`00bc325c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md#insn-00bc325c) · [`00bc3264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md#insn-00bc3264)

~~~diff
- 00bc3250 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bc3250 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc3250 bytes c90600f9
- 00bc325c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc325c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc325c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc325c bytes 080c01f8
- 00bc3264 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc3264 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc3264 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc3264 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4bfad34daae5f3f70716e1de1b1d675"></a>

### [`00bc429c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc429c.md) → [`00c40ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40ce4.md) FUN_00c40ce4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 77.08% / 新版 77.08%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc430c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4318"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc430c",
      "DATA",
      [
        "storage",
        "00c17ea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c40d54",
      "DATA",
      [
        "storage",
        "00c97850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc429c.md#insn-00bc4304) · [`00bc430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc429c.md#insn-00bc430c) · [`00bc4318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc429c.md#insn-00bc4318)

~~~diff
- 00bc4304 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00bc4304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc4304 bytes e90600f9
- 00bc430c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc430c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc430c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc430c bytes 080c01f8
- 00bc4318 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00bc4318 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc4318 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc4318 bytes 0b200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc70b692019d413dd000e9c8f7533040"></a>

### [`00bc435c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc435c.md) → [`00c40da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md) FUN_00c40da4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 85.11% / 新版 85.11%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40e14",
      "incomplete_value": false,
      "site": "00c40e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc43cc",
      "incomplete_value": false,
      "site": "00bc43cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4390"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c40dd8"
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
      "unmatched:00bc4390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c40dfc"
      ]
    ],
    [
      "00c40e14",
      "DATA",
      [
        "storage",
        "00c17f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c40dd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c40dfc"
      ]
    ],
    [
      "00c40e14",
      "DATA",
      [
        "storage",
        "00c978c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc435c.md#insn-00bc4390) · [`00bc4370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc435c.md#insn-00bc4370)
- 新版 [`00c40dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40da4.md#insn-00c40dd8)

~~~diff
- 00bc4390 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc4390 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc4390 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00bc4390 bytes 28010054
+ 00c40dd8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c40dd8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c40dd8 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c40dd8 bytes 28010054
- 00bc4370 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00bc4370 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f054dbc178c48a57001ba858a146e589"></a>

### [`00bc4418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4418.md) → [`00c40e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md) FUN_00c40e60

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40ed4",
      "incomplete_value": false,
      "site": "00c40ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc448c",
      "incomplete_value": false,
      "site": "00bc448c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "00c40ed4",
      "DATA",
      [
        "storage",
        "00c17f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c40ed4",
      "DATA",
      [
        "storage",
        "00c97930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4418.md#insn-00bc4450) · [`00bc445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4418.md#insn-00bc445c) · [`00bc4460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4418.md#insn-00bc4460)
- 新版 [`00c40e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40e98) · [`00c40ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40ea4) · [`00c40ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40e60.md#insn-00c40ea8)

~~~diff
- 00bc4450 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc4450 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc4450 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00c40e98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c40e98 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c40e98 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00bc4450 bytes 28010054
+ 00c40e98 bytes 28010054
- 00bc445c ["INT_ADD", "register:40f0:8", ["const:bc445c:8", "const:4:8"]]
- 00bc445c ["CALL", null, ["callee:00c59c20:8"]]
+ 00c40ea4 ["INT_ADD", "register:40f0:8", ["const:c40ea4:8", "const:4:8"]]
+ 00c40ea4 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc445c bytes 5d630094
+ 00c40ea4 bytes 5f630094
- 00bc4460 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bc4460 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00c40ea8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c40ea8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc4460 bytes 000400b4
+ 00c40ea8 bytes 000400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef37126ef7ec26ff23230a205ca40ae"></a>

### [`00bc44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc44e4.md) → [`00c40f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md) FUN_00c40f2c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40fac",
      "incomplete_value": false,
      "site": "00c40fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4564",
      "incomplete_value": false,
      "site": "00bc4564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "00c40fac",
      "DATA",
      [
        "storage",
        "00c17ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c40fac",
      "DATA",
      [
        "storage",
        "00c979a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc44e4.md#insn-00bc4534) · [`00bc4554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc44e4.md#insn-00bc4554) · [`00bc4558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc44e4.md#insn-00bc4558)
- 新版 [`00c40f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c40f7c) · [`00c40f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c40f9c) · [`00c40fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c40/00c40f2c.md#insn-00c40fa0)

~~~diff
- 00bc4534 ["INT_ADD", "register:40f0:8", ["const:bc4534:8", "const:4:8"]]
- 00bc4534 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c40f7c ["INT_ADD", "register:40f0:8", ["const:c40f7c:8", "const:4:8"]]
+ 00c40f7c ["CALL", null, ["callee:00c59c20:8"]]
- 00bc4534 bytes 27630094
+ 00c40f7c bytes 29630094
- 00bc4554 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00c40f9c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc4554 bytes 880200f0
+ 00c40f9c bytes a80200f0
- 00bc4558 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00bc4558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c40fa0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00c40fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c40fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c40fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc4558 bytes 08e13f91
+ 00c40fa0 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53bb4dc0374df7f82c43d3047012185"></a>

### [`00bc45d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc45d0.md) → [`00c41018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md) FUN_00c41018

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41088",
      "incomplete_value": false,
      "site": "00c41088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4640",
      "incomplete_value": false,
      "site": "00bc4640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4604"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4104c"
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
      "unmatched:00bc4604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41070"
      ]
    ],
    [
      "00c41088",
      "DATA",
      [
        "storage",
        "00c180d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4104c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41070"
      ]
    ],
    [
      "00c41088",
      "DATA",
      [
        "storage",
        "00c97a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc45d0.md#insn-00bc4604) · [`00bc45f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc45d0.md#insn-00bc45f8)
- 新版 [`00c4104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41018.md#insn-00c4104c)

~~~diff
- 00bc4604 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc4604 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc4604 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00bc4604 bytes 28010054
+ 00c4104c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c4104c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c4104c ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c4104c bytes 28010054
- 00bc45f8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00bc45f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc45f8 bytes e80640f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa98e48357126447b9e1f4724a81111a"></a>

### [`00bc4690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4690.md) → [`00c410d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c410d8.md) FUN_00c410d8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc46f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc470c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc46c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41130"
      ]
    ],
    [
      "unmatched:00bc4700",
      "DATA",
      [
        "storage",
        "00c18148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4110c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41130"
      ]
    ],
    [
      "00c41148",
      "DATA",
      [
        "storage",
        "00c97af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc46c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4690.md#insn-00bc46c4) · [`00bc46f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4690.md#insn-00bc46f8) · [`00bc4700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4690.md#insn-00bc4700)

~~~diff
- 00bc46c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc46c4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc46c4 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bc46c4 bytes 28010054
- 00bc46f8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00bc46f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc46f8 bytes e90600f9
- 00bc4700 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc4700 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc4700 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc4700 bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aad7210fc74ab331dfe8ed10705de2a"></a>

### [`00bc4818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4818.md) → [`00c41260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41260.md) FUN_00c41260

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 78.00% / 新版 78.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc488c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4898"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc488c",
      "DATA",
      [
        "storage",
        "00c18228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c412d4",
      "DATA",
      [
        "storage",
        "00c97bd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4818.md#insn-00bc4884) · [`00bc488c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4818.md#insn-00bc488c) · [`00bc4898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc4818.md#insn-00bc4898)

~~~diff
- 00bc4884 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:8:8"]]
- 00bc4884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc4884 bytes 090700f9
- 00bc488c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc488c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc488c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc488c bytes 080c01f8
- 00bc4898 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc4898 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc4898 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc4898 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-921ea6c9ab51386dc1c6f108ffc7fba6"></a>

### [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) → [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) FUN_00c41328

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 12件 [`00bbd2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd2a8.md) [`00bbd308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbd308.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc93c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md) [`00bc94bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md)
- 新版 呼出元 2件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 12件 [`00c39cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39cf0.md) [`00c39d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c39/00c39d50.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md) [`00c45f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.28% / 新版 66.28%

CFGの説明率　旧版 41.30% / 新版 46.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc48f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc48f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc48f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c41388",
      "DATA",
      [
        "storage",
        "002fcc64",
        "switchD_00bc4948::switchdataD_002fcc64",
        "ushort"
      ]
    ],
    [
      "00c41390",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00bc494c"
      ]
    ]
  ],
  "added": [
    [
      "00c41338",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c41388",
      "DATA",
      [
        "storage",
        "00312a9c",
        "switchD_00c41390::switchdataD_00312a9c",
        "ushort"
      ]
    ],
    [
      "00c41390",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00c41394"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc48f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md#insn-00bc48f0) · [`00bc4958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md#insn-00bc4958) · [`00bc4b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md#insn-00bc4b74)

~~~diff
- 00bc48f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc48f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc48f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bc48f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc48f0 bytes f44f04a9
- 00bc4958 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc4958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc4958 bytes e00b00f9
- 00bc4b74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bc4b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc4b74 bytes e00700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97c61885880a5227016e8b80a9cd4f18"></a>

### [`00bc5260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md) → [`00c41ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md) FUN_00c41ca8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 3件 [`00bcc6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 3件 [`00c49134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 65.27% / 新版 65.27%

CFGの説明率　旧版 42.11% / 新版 46.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 13件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc53f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c41db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc5378"
      ]
    ],
    [
      "unmatched:00bc537c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42040"
      ]
    ],
    [
      "unmatched:00bc5388",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc5394"
      ]
    ]
  ],
  "added": [
    [
      "00c41db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41dc0"
      ]
    ],
    [
      "00c41dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42040"
      ]
    ],
    [
      "00c41dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c41ddc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md#insn-00bc5374) · [`00bc537c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md#insn-00bc537c) · [`00bc5388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md#insn-00bc5388)

~~~diff
- 00bc5374 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bc5374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc5374 bytes 080000f9
- 00bc537c ["CBRANCH", null, ["local:b73:8", "register:101:1"]]
- 00bc537c bytes e0130054
- 00bc5388 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc5388 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00bc5388 bytes 61000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ae77570b1848313b58aa11e8f0db43"></a>

### [`00bc5a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5a90.md) → [`00c424d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c424d8.md) FUN_00c424d8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5af0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5b04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc5af8",
      "DATA",
      [
        "storage",
        "00c18298",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bc5b24",
      "DATA",
      [
        "storage",
        "002a72db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c42540",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4256c",
      "DATA",
      [
        "storage",
        "002b7e4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5a90.md#insn-00bc5af0) · [`00bc5af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5a90.md#insn-00bc5af8) · [`00bc5b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5a90.md#insn-00bc5b04)

~~~diff
- 00bc5af0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bc5af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc5af0 bytes c90600f9
- 00bc5af8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc5af8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc5af8 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc5af8 bytes 080c01f8
- 00bc5b04 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bc5b04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bc5b04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc5b04 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9dcca83fa4cdec2b8071c02b7a732c"></a>

### [`00bc5b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md) → [`00c42598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42598.md) FUN_00c42598

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 9件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 9件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.92% / 新版 77.92%

CFGの説明率　旧版 45.08% / 新版 47.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5b6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc5b68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc5b6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc5c2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c426f4"
      ]
    ]
  ],
  "added": [
    [
      "00c425b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c425b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c42674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c426f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md#insn-00bc5b68) · [`00bc5b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md#insn-00bc5b6c) · [`00bc5c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5b50.md#insn-00bc5c10)

~~~diff
- 00bc5b68 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc5b68 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc5b68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bc5b68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc5b68 bytes f65706a9
- 00bc5b6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc5b6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc5b6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bc5b6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc5b6c bytes f44f07a9
- 00bc5c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00bc5c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc5c10 bytes 680e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c2a06d6a52eb98bed3a6ac9d71c95f"></a>

### [`00bc6020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md) → [`00c42a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42a68.md) FUN_00c42a68

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 8件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 8件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.87% / 新版 78.87%

CFGの説明率　旧版 19.32% / 新版 15.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6108"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc613c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6048",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bbde5c"
      ]
    ],
    [
      "unmatched:00bc606c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ad0"
      ]
    ],
    [
      "00c42c24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42b20"
      ]
    ]
  ],
  "added": [
    [
      "00c42a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c3a8a4"
      ]
    ],
    [
      "00c42ab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ad0"
      ]
    ],
    [
      "00c42b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42b20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc606c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md#insn-00bc606c) · [`00bc60d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md#insn-00bc60d0) · [`00bc6108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md#insn-00bc6108)

~~~diff
- 00bc606c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00bc606c bytes e0000054
- 00bc60d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc60d0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bc60d0 bytes 21ffff54
- 00bc6108 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc6108 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bc6108 bytes ea0b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30125339c077f786955dbf5a8f5e59c"></a>

### [`00bc6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6568.md) → [`00c42fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c42/00c42fb0.md) FUN_00c42fb0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 12.50% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc65c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc65cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc65d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ffc"
      ]
    ],
    [
      "unmatched:00bc65cc",
      "DATA",
      [
        "storage",
        "00c18fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42fd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c42ffc"
      ]
    ],
    [
      "00c43014",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6568.md#insn-00bc6590) · [`00bc65c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6568.md#insn-00bc65c4) · [`00bc65cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6568.md#insn-00bc65cc)

~~~diff
- 00bc6590 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc6590 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc6590 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bc6590 bytes 28010054
- 00bc65c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bc65c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc65c4 bytes a90600f9
- 00bc65cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc65cc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc65cc ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc65cc bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ce6a542172b4835304e322978d64891"></a>

### [`00bc66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md) → [`00c430f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c430f8.md) FUN_00c430f8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.44% / 新版 67.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc66b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc66b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc66b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc66b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc66b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc66bc",
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
      "00c430fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c43100",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c43104",
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

- 旧版 [`00bc66b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc66b4) · [`00bc66b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc66b8) · [`00bc66bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc66b0.md#insn-00bc66bc)

~~~diff
- 00bc66b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc66b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc66b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc66b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc66b4 bytes fd7bbda9
- 00bc66b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc66b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc66b8 bytes f50b00f9
- 00bc66bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc66bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc66bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc66bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc66bc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15aacc0d090eff00296ea79b5e0eb86"></a>

### [`00bc675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md) → [`00c431a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md) FUN_00c431a4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43208",
      "incomplete_value": true,
      "site": "00c43208",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc67c0",
      "incomplete_value": true,
      "site": "00bc67c0",
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
            "const:28:8"
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
      "00c43208",
      "DATA",
      [
        "storage",
        "00c19028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43208",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc6790) · [`00bc67b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc67b0) · [`00bc67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc675c.md#insn-00bc67b4)
- 新版 [`00c431d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c431d8) · [`00c431f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c431f8) · [`00c431fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c431a4.md#insn-00c431fc)

~~~diff
- 00bc6790 ["INT_ADD", "register:40f0:8", ["const:bc6790:8", "const:4:8"]]
- 00bc6790 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c431d8 ["INT_ADD", "register:40f0:8", ["const:c431d8:8", "const:4:8"]]
+ 00c431d8 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc6790 bytes 905a0094
+ 00c431d8 bytes 925a0094
- 00bc67b0 ["COPY", "register:4040:8", ["const:c19000:8"]]
+ 00c431f8 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00bc67b0 bytes 880200f0
+ 00c431f8 bytes a80200b0
- 00bc67b4 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00bc67b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc67b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc67b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c431fc ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00c431fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c431fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c431fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc67b4 bytes 08a10091
+ 00c431fc bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abb581cb94da0742b026d47153bf93e2"></a>

### [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) → [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) FUN_00c43244

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 7件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bc1c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1c24.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 7件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c3e66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e66c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.03% / 新版 76.03%

CFGの説明率　旧版 41.45% / 新版 41.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc68c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc68d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc68dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4328c"
      ]
    ],
    [
      "unmatched:00bc683c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c432a8"
      ]
    ],
    [
      "unmatched:00bc6890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43300"
      ]
    ]
  ],
  "added": [
    [
      "00c4327c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4328c"
      ]
    ],
    [
      "00c43284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c432a8"
      ]
    ],
    [
      "00c432d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43300"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc68c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc68c8) · [`00bc68d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc68d0) · [`00bc68dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md#insn-00bc68dc)

~~~diff
- 00bc68c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8:8"]]
- 00bc68c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc68c8 bytes 890600f9
- 00bc68d0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bc68d0 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:10:8"]]
- 00bc68d0 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:0:8"]]
- 00bc68d0 bytes 0a0d01f8
- 00bc68dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00bc68dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc68dc bytes 000900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2412e19665d22fbf231ca83aa9ad9014"></a>

### [`00bc6e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md) → [`00c438b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c438b8.md) FUN_00c438b8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.63% / 新版 68.63%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc6ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc6ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43914"
      ]
    ],
    [
      "unmatched:00bc6ee4",
      "DATA",
      [
        "storage",
        "00c17dc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c438f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c43914"
      ]
    ],
    [
      "00c4392c",
      "DATA",
      [
        "storage",
        "00c97770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6ea8) · [`00bc6edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6edc) · [`00bc6ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6e70.md#insn-00bc6ee4)

~~~diff
- 00bc6ea8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc6ea8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc6ea8 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bc6ea8 bytes 28010054
- 00bc6edc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:8:8"]]
- 00bc6edc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc6edc bytes 090700f9
- 00bc6ee4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bc6ee4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bc6ee4 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bc6ee4 bytes 080c01f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d7f5f32ddb794e31fa469e876d6638a"></a>

### [`00bc7c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md) → [`00c44688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44688.md) FUN_00c44688

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 35.47% / 新版 35.47%

CFGの説明率　旧版 1.52% / 新版 2.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7cf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc7c9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c446fc"
      ]
    ],
    [
      "unmatched:00bc7cdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc7d08"
      ]
    ],
    [
      "unmatched:00bc7cf4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c446e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c446fc"
      ]
    ],
    [
      "00c44724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44750"
      ]
    ],
    [
      "00c4473c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md#insn-00bc7cd4) · [`00bc7cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md#insn-00bc7cf0) · [`00bc7cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7c40.md#insn-00bc7cf8)

~~~diff
- 00bc7cd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00bc7cd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 00bc7cd4 bytes 6b2200b9
- 00bc7cf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc7cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc7cf0 bytes 610a00f9
- 00bc7cf8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc7cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc7cf8 bytes 600200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008884bd29967ec7dfb020a23c82acc1"></a>

### [`00bc7f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md) → [`00c449bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md) FUN_00c449bc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.01% / 新版 57.01%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 6件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc7fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc806c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc80cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc7fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44a1c"
      ]
    ],
    [
      "unmatched:00bc8058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44ac8"
      ]
    ],
    [
      "unmatched:00bc8070",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c449f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44a1c"
      ]
    ],
    [
      "00c44aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44ac8"
      ]
    ],
    [
      "00c44ab8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md#insn-00bc7fe4) · [`00bc806c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md#insn-00bc806c) · [`00bc80cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md#insn-00bc80cc)

~~~diff
- 00bc7fe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bc7fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc7fe4 bytes 680600f9
- 00bc806c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc806c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc806c bytes 610a00f9
- 00bc80cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bc80cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc80cc bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a999ec38d4e6c81a66548c996b5c451"></a>

### [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) → [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) FUN_00c44d1c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00bc7f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc7/00bc7f74.md) [`00bc86dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc86dc.md) [`00bc8808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md) [`00bcbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md) [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 15件 [`00c449bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c449bc.md) [`00c45124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45124.md) [`00c45250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md) [`00c48648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48648.md) [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.29% / 新版 79.29%

CFGの説明率　旧版 4.84% / 新版 7.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc83f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c44e40"
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
      "unmatched:00bc83c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44f08"
      ]
    ],
    [
      "unmatched:00bc83fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44e74"
      ]
    ],
    [
      "unmatched:00bc8458",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44eb8"
      ]
    ]
  ],
  "added": [
    [
      "00c44e0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44f08"
      ]
    ],
    [
      "00c44e44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44e74"
      ]
    ],
    [
      "00c44ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44eb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc83b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md#insn-00bc83b4) · [`00bc83c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md#insn-00bc83c4) · [`00bc83d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md#insn-00bc83d8)

~~~diff
- 00bc83b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc83b4 ["INT_ADD", "register:40f0:8", ["const:bc83b4:8", "const:4:8"]]
- 00bc83b4 ["CALLIND", null, ["register:0:8"]]
- 00bc83b4 bytes 00013fd6
- 00bc83c4 ["CBRANCH", null, ["local:b45:8", "register:101:1"]]
- 00bc83c4 bytes e0070054
- 00bc83d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc83d8 ["INT_ADD", "register:40f0:8", ["const:bc83d8:8", "const:4:8"]]
- 00bc83d8 ["CALLIND", null, ["register:0:8"]]
- 00bc83d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7438e0c5d3f6fd42594a79f7a3cbe1b"></a>

### [`00bc8504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8504.md) → [`00c44f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44f4c.md) FUN_00c44f4c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.79% / 新版 63.79%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc850c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc8508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc850c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc8538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44fa8"
      ]
    ]
  ],
  "added": [
    [
      "00c44f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c44f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c44f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c44fa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc8508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8504.md#insn-00bc8508) · [`00bc850c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8504.md#insn-00bc850c) · [`00bc8538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8504.md#insn-00bc8538)

~~~diff
- 00bc8508 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc8508 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc8508 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc8508 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc8508 bytes fd7bbea9
- 00bc850c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc850c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc850c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc850c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc850c bytes f44f01a9
- 00bc8538 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bc8538 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bc8538 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00bc8538 bytes 49010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

