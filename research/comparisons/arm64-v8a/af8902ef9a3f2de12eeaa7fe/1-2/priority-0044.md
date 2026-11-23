# v15.7.4 → v16.0.0 · 最優先の変更候補 (44)

[一覧の目次](README.md)

<a id="compare-b0643c6a4b5fb72fc2884bd8a6c5f3c7"></a>

### [`008a4be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4be0.md) → [`008d8a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a78.md) FUN_008d8a78

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8a84",
      "incomplete_value": false,
      "site": "008d8a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4bec",
      "incomplete_value": false,
      "site": "008a4bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "008d8a84",
      "DATA",
      [
        "storage",
        "00c06750",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8a84",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4be0.md#insn-008a4be4) · [`008a4be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4be0.md#insn-008a4be8)
- 新版 [`008d8a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a78.md#insn-008d8a7c) · [`008d8a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a78.md#insn-008d8a80)

~~~diff
- 008a4be4 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008d8a7c ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a4be4 bytes 091b00d0
+ 008d8a7c bytes 691d0090
- 008a4be8 ["COPY", "tmp:0:8", ["const:750:8"]]
- 008a4be8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a4be8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a4be8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8a80 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 008d8a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a4be8 bytes 29411d91
+ 008d8a80 bytes 29a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d207a34e13b4e00802ffa1ba0219d224"></a>

### [`008a4bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4bfc.md) → [`008d8a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md) FUN_008d8a94

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0057476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057476c.md) [`00883c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c74.md) [`00883c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c7c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) [`008b6e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e14.md) [`008b6e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e1c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.61% / 新版 81.61%

CFGの説明率　旧版 46.43% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4cec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "008d8aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:008a4ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d8ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d8aec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008d8b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4bfc.md#insn-008a4c38) · [`008a4c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4bfc.md#insn-008a4c54) · [`008a4c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4bfc.md#insn-008a4c98)
- 新版 [`008d8ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8ad0) · [`008d8aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8aec) · [`008d8b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8a94.md#insn-008d8b30)

~~~diff
- 008a4c38 ["INT_ADD", "register:40f0:8", ["const:8a4c38:8", "const:4:8"]]
- 008a4c38 ["CALL", null, ["ram:457e1c:8"]]
+ 008d8ad0 ["INT_ADD", "register:40f0:8", ["const:8d8ad0:8", "const:4:8"]]
+ 008d8ad0 ["CALL", null, ["ram:47acb4:8"]]
- 008a4c38 bytes 79ccee97
+ 008d8ad0 bytes 7988ee97
- 008a4c54 ["INT_ADD", "register:40f0:8", ["const:8a4c54:8", "const:4:8"]]
- 008a4c54 ["CALL", null, ["ram:457e1c:8"]]
+ 008d8aec ["INT_ADD", "register:40f0:8", ["const:8d8aec:8", "const:4:8"]]
+ 008d8aec ["CALL", null, ["ram:47acb4:8"]]
- 008a4c54 bytes 72ccee97
+ 008d8aec bytes 7288ee97
- 008a4c98 ["INT_ADD", "register:40f0:8", ["const:8a4c98:8", "const:4:8"]]
- 008a4c98 ["CALL", null, ["callee:008b7984:8"]]
+ 008d8b30 ["INT_ADD", "register:40f0:8", ["const:8d8b30:8", "const:4:8"]]
+ 008d8b30 ["CALL", null, ["callee:008b7984:8"]]
- 008a4c98 bytes d37eff97
+ 008d8b30 bytes 957bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7712361d65fc95a4fd2c509dc512a49"></a>

### [`008a4e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e10.md) → [`008d8ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8ca8.md) FUN_008d8ca8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d8cac",
      "incomplete_value": false,
      "site": "008d8cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4e14",
      "incomplete_value": false,
      "site": "008a4e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008d8cb0",
      "DATA",
      [
        "storage",
        "00c067c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8cb0",
      "DATA",
      [
        "storage",
        "00c84598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e10.md#insn-008a4e10) · [`008a4e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e10.md#insn-008a4e14)
- 新版 [`008d8ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8ca8.md#insn-008d8ca8) · [`008d8cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8ca8.md#insn-008d8cac)

~~~diff
- 008a4e10 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d8ca8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a4e10 bytes 081b00d0
+ 008d8ca8 bytes 681d0090
- 008a4e14 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 008a4e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a4e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a4e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8cac ["COPY", "tmp:0:8", ["const:598:8"]]
+ 008d8cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a4e14 bytes 08011f91
+ 008d8cac bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e761fdf87781c84a40e053213905c599"></a>

### [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) → [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) FUN_008d8cd0

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449c34.md) [`0052dd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd50.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`00550be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550be8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.89% / 新版 72.89%

CFGの説明率　旧版 12.90% / 新版 16.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4e94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4e98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a4e68",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008a4e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a4e74",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008d8d00",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "008d8d04",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008d8d0c",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md#insn-008a4e6c) · [`008a4e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md#insn-008a4e7c) · [`008a4e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md#insn-008a4e94)

~~~diff
- 008a4e6c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008a4e6c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008a4e6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008a4e6c bytes a8031ff8
- 008a4e7c ["INT_ADD", "register:40f0:8", ["const:8a4e7c:8", "const:4:8"]]
- 008a4e7c ["CALL", null, ["callee:00550be8:8"]]
- 008a4e7c bytes b523f297
- 008a4e94 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008a4e94 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:40:8"]]
- 008a4e94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008a4e94 bytes e8030139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e73ffd17a02be70ec3535b0e1a7137"></a>

### [`008a53d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a53d8.md) → [`008d9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md) FUN_008d9270

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9290",
      "incomplete_value": false,
      "site": "008d9294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a53f8",
      "incomplete_value": false,
      "site": "008a53fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "008d9294",
      "DATA",
      [
        "storage",
        "00c06830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9294",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a53ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a53d8.md#insn-008a53ec) · [`008a53f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a53d8.md#insn-008a53f4) · [`008a53f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a53d8.md#insn-008a53f8)
- 新版 [`008d9284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d9284) · [`008d928c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d928c) · [`008d9290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d9290)

~~~diff
- 008a53ec ["INT_ADD", "register:40f0:8", ["const:8a53ec:8", "const:4:8"]]
- 008a53ec ["CALL", null, ["callee:00c57a90:8"]]
+ 008d9284 ["INT_ADD", "register:40f0:8", ["const:8d9284:8", "const:4:8"]]
+ 008d9284 ["CALL", null, ["callee:00c57a90:8"]]
- 008a53ec bytes 15d70c94
+ 008d9284 bytes 03fa0d94
- 008a53f4 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d928c ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a53f4 bytes 081b00b0
+ 008d928c bytes 481d00f0
- 008a53f8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 008a53f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9290 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 008d9290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 bytes 08c12091
+ 008d9290 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a2a1e8bf9662d9f6561f92b29d7295"></a>

### [`008a5410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5410.md) → [`008d92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92a8.md) FUN_008d92a8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d92ac",
      "incomplete_value": false,
      "site": "008d92b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5414",
      "incomplete_value": false,
      "site": "008a5418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "008d92b0",
      "DATA",
      [
        "storage",
        "00c06830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d92b0",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5410.md#insn-008a5410) · [`008a5414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5410.md#insn-008a5414)
- 新版 [`008d92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92a8.md#insn-008d92a8) · [`008d92ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92a8.md#insn-008d92ac)

~~~diff
- 008a5410 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d92a8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a5410 bytes 081b00b0
+ 008d92a8 bytes 481d00f0
- 008a5414 ["COPY", "tmp:0:8", ["const:830:8"]]
- 008a5414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d92ac ["COPY", "tmp:0:8", ["const:608:8"]]
+ 008d92ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d92ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d92ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5414 bytes 08c12091
+ 008d92ac bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e83450f1485ebe4ff0e2b651d12e0b"></a>

### [`008a54e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a54e4.md) → [`008d937c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d937c.md) FUN_008d937c

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9388",
      "incomplete_value": false,
      "site": "008d9388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a54f0",
      "incomplete_value": false,
      "site": "008a54f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "008d9388",
      "DATA",
      [
        "storage",
        "00c068d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9388",
      "DATA",
      [
        "storage",
        "00c846a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a54e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a54e4.md#insn-008a54e8) · [`008a54ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a54e4.md#insn-008a54ec)
- 新版 [`008d9380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d937c.md#insn-008d9380) · [`008d9384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d937c.md#insn-008d9384)

~~~diff
- 008a54e8 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008d9380 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a54e8 bytes 091b00b0
+ 008d9380 bytes 491d00f0
- 008a54ec ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008a54ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a54ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a54ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d9384 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 008d9384 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9384 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9384 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a54ec bytes 29412391
+ 008d9384 bytes 29a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13bdb9c8d0279d1dbc644eacd020b368"></a>

### [`008a5500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5500.md) → [`008d9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9398.md) FUN_008d9398

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0088482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/0088482c.md) [`008a56d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a56d0.md) [`008a56d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a56d4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md) [`008d9568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9568.md) [`008d956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d956c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.12% / 新版 69.12%

CFGの説明率　旧版 42.86% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5508"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a5504",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a5508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a550c",
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
      "008d939c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d93a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d93a4",
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

- 旧版 [`008a5504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5500.md#insn-008a5504) · [`008a5508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5500.md#insn-008a5508) · [`008a550c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5500.md#insn-008a550c)

~~~diff
- 008a5504 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008a5504 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008a5504 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008a5504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a5504 bytes fd7b04a9
- 008a5508 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 008a5508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008a5508 bytes f52b00f9
- 008a550c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008a550c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008a550c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008a550c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a550c bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f5e68a90d599e329fa3fbe28c133b0"></a>

### [`008a5688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5688.md) → [`008d9520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md) FUN_008d9520

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008d9544",
      "incomplete_value": false,
      "site": "008d9544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a56ac",
      "incomplete_value": false,
      "site": "008a56ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008d9544",
      "DATA",
      [
        "storage",
        "00c06940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9544",
      "DATA",
      [
        "storage",
        "00c84718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a569c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5688.md#insn-008a569c) · [`008a56a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5688.md#insn-008a56a4) · [`008a56a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5688.md#insn-008a56a8)
- 新版 [`008d9534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md#insn-008d9534) · [`008d953c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md#insn-008d953c) · [`008d9540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md#insn-008d9540)

~~~diff
- 008a569c ["INT_ADD", "register:40f0:8", ["const:8a569c:8", "const:4:8"]]
- 008a569c ["CALL", null, ["callee:00c57a90:8"]]
+ 008d9534 ["INT_ADD", "register:40f0:8", ["const:8d9534:8", "const:4:8"]]
+ 008d9534 ["CALL", null, ["callee:00c57a90:8"]]
- 008a569c bytes 69d60c94
+ 008d9534 bytes 57f90d94
- 008a56a4 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d953c ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a56a4 bytes 081b00b0
+ 008d953c bytes 481d00f0
- 008a56a8 ["COPY", "tmp:0:8", ["const:940:8"]]
- 008a56a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9540 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 008d9540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 bytes 08012591
+ 008d9540 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a8aa634093d45f530833e8e987413a"></a>

### [`008a577c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a577c.md) → [`008d9614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md) FUN_008d9614

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "008d9620",
      "incomplete_value": false,
      "site": "008d9624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5788",
      "incomplete_value": false,
      "site": "008a578c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008d9624",
      "DATA",
      [
        "storage",
        "00c069d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9624",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a577c.md#insn-008a5784) · [`008a5788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a577c.md#insn-008a5788)
- 新版 [`008d961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md#insn-008d961c) · [`008d9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9614.md#insn-008d9620)

~~~diff
- 008a5784 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008d961c ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a5784 bytes 091b00b0
+ 008d961c bytes 491d00f0
- 008a5788 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 008a5788 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a5788 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a5788 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d9620 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 008d9620 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9620 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9620 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a5788 bytes 29412791
+ 008d9620 bytes 29a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de8d09cf668ab29cf42010a56b0cb79"></a>

### [`008a57e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a57e0.md) → [`008d9678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9678.md) FUN_008d9678

採用 · 移動量 `+0x33e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4204.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 62.50% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5818"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a5818",
      "DATA",
      [
        "storage",
        "00c069d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d96b0",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a57e0.md#insn-008a5814) · [`008a5818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a57e0.md#insn-008a5818) · [`008a5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a57e0.md#insn-008a5820)

~~~diff
- 008a5814 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008a5814 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 008a5814 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:20:8"]]
- 008a5814 ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 008a5814 bytes bf0e02f8
- 008a5818 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008a5818 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008a5818 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008a5818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a5818 bytes 082400a9
- 008a5820 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008a5820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008a5820 bytes 0a0800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03352a40820d9df06c00acfe1f094042"></a>

### [`008a58d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a58d8.md) → [`008d9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9770.md) FUN_008d9770

採用 · 移動量 `+0x33e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4204.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.24% / 新版 67.24%

CFGの説明率　旧版 36.36% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a58d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a58d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a58dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a58d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a58dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a58e0",
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
      "008d9770",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d9774",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d9778",
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

- 旧版 [`008a58d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a58d8.md#insn-008a58d8) · [`008a58dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a58d8.md#insn-008a58dc) · [`008a58e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a58d8.md#insn-008a58e0)

~~~diff
- 008a58d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008a58d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008a58d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008a58d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008a58d8 bytes fd7bbca9
- 008a58dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008a58dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008a58dc bytes f70b00f9
- 008a58e0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008a58e0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008a58e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008a58e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a58e0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69779b873e861226d4de6750906136eb"></a>

### [`008a5a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a0c.md) → [`008d98a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d98a4.md) FUN_008d98a4

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md) [`0089eb04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089e/0089eb04.md) [`008a395c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a3/008a395c.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008d299c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d299c.md) [`008d77f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d77f4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 25.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d98d4",
      "incomplete_value": true,
      "site": "008d98d8",
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
            "const:2078:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5a3c",
      "incomplete_value": true,
      "site": "008a5a40",
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
            "const:1f90:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008a5a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a0c.md#insn-008a5a40) · [`008a5a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a0c.md#insn-008a5a14) · [`008a5a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a0c.md#insn-008a5a2c)
- 新版 [`008d98d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d98a4.md#insn-008d98d8) · [`008d98ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d98a4.md#insn-008d98ac)

~~~diff
- 008a5a40 ["INT_ADD", "register:40f0:8", ["const:8a5a40:8", "const:4:8"]]
- 008a5a40 ["CALL", null, ["callee:008d77f4:8"]]
+ 008d98d8 ["INT_ADD", "register:40f0:8", ["const:8d98d8:8", "const:4:8"]]
+ 008d98d8 ["CALL", null, ["callee:008d77f4:8"]]
- 008a5a40 bytes c7f7ff97
+ 008d98d8 bytes c7f7ff97
- 008a5a14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008a5a14 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008d98ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d98ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008a5a14 bytes 41020054
+ 008d98ac bytes 41020054
- 008a5a2c ["COPY", "register:4040:8", ["const:1f90:8"]]
- 008a5a2c bytes 08f28352
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76e95f36971065fb56f36afdb6d343ed"></a>

### [`008a5a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a8c.md) → [`008d9924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md) FUN_008d9924

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9938",
      "incomplete_value": false,
      "site": "008d993c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5aa0",
      "incomplete_value": false,
      "site": "008a5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008d993c",
      "DATA",
      [
        "storage",
        "00c06a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d993c",
      "DATA",
      [
        "storage",
        "00c84828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a8c.md#insn-008a5a98) · [`008a5a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a8c.md#insn-008a5a9c) · [`008a5aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5a8c.md#insn-008a5aa0)
- 新版 [`008d9930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md#insn-008d9930) · [`008d9934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md#insn-008d9934) · [`008d9938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9924.md#insn-008d9938)

~~~diff
- 008a5a98 ["INT_ADD", "register:40f0:8", ["const:8a5a98:8", "const:4:8"]]
- 008a5a98 ["CALL", null, ["callee:00c57a90:8"]]
+ 008d9930 ["INT_ADD", "register:40f0:8", ["const:8d9930:8", "const:4:8"]]
+ 008d9930 ["CALL", null, ["callee:00c57a90:8"]]
- 008a5a98 bytes 6ad50c94
+ 008d9930 bytes 58f80d94
- 008a5a9c ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d9934 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a5a9c bytes 081b00b0
+ 008d9934 bytes 481d00f0
- 008a5aa0 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008a5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9938 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 008d9938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 bytes 08412991
+ 008d9938 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de34213ff637fa28190febacb1ed541c"></a>

### [`008a5ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5ab0.md) → [`008d9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9948.md) FUN_008d9948

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d994c",
      "incomplete_value": false,
      "site": "008d9950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5ab4",
      "incomplete_value": false,
      "site": "008a5ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008d9950",
      "DATA",
      [
        "storage",
        "00c06a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9950",
      "DATA",
      [
        "storage",
        "00c84828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5ab0.md#insn-008a5ab0) · [`008a5ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5ab0.md#insn-008a5ab4)
- 新版 [`008d9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9948.md#insn-008d9948) · [`008d994c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9948.md#insn-008d994c)

~~~diff
- 008a5ab0 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d9948 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a5ab0 bytes 081b00b0
+ 008d9948 bytes 481d00f0
- 008a5ab4 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008a5ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d994c ["COPY", "tmp:0:8", ["const:828:8"]]
+ 008d994c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d994c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d994c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 bytes 08412991
+ 008d994c bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae56cf040de3284b50bfcbd8bca8890f"></a>

### [`008a5b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5b30.md) → [`008d99c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99c8.md) FUN_008d99c8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d99cc",
      "incomplete_value": false,
      "site": "008d99d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5b34",
      "incomplete_value": false,
      "site": "008a5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "008d99d0",
      "DATA",
      [
        "storage",
        "00c06ad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d99d0",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5b30.md#insn-008a5b30) · [`008a5b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5b30.md#insn-008a5b34)
- 新版 [`008d99c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99c8.md#insn-008d99c8) · [`008d99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d99c8.md#insn-008d99cc)

~~~diff
- 008a5b30 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d99c8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a5b30 bytes 081b00b0
+ 008d99c8 bytes 481d00f0
- 008a5b34 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 008a5b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d99cc ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 008d99cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d99cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d99cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 bytes 08412b91
+ 008d99cc bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63179b426a328cdd8e028e80ad4fe912"></a>

### [`008a5bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bb0.md) → [`008d9a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a48.md) FUN_008d9a48

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008d9a4c",
      "incomplete_value": false,
      "site": "008d9a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5bb4",
      "incomplete_value": false,
      "site": "008a5bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "008d9a50",
      "DATA",
      [
        "storage",
        "00c06b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9a50",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bb0.md#insn-008a5bb0) · [`008a5bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bb0.md#insn-008a5bb4)
- 新版 [`008d9a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a48.md#insn-008d9a48) · [`008d9a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a48.md#insn-008d9a4c)

~~~diff
- 008a5bb0 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008d9a48 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a5bb0 bytes 081b00b0
+ 008d9a48 bytes 481d00f0
- 008a5bb4 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 008a5bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d9a4c ["COPY", "tmp:0:8", ["const:928:8"]]
+ 008d9a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d9a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 bytes 08412d91
+ 008d9a4c bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f780a071a6a589362a668c5be0f933db"></a>

### [`008a6330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6330.md) → [`008da1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md) FUN_008da1c8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da1dc",
      "incomplete_value": false,
      "site": "008da1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6344",
      "incomplete_value": false,
      "site": "008a6348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "008da1e0",
      "DATA",
      [
        "storage",
        "00c06bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da1e0",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a633c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6330.md#insn-008a633c) · [`008a6340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6330.md#insn-008a6340) · [`008a6344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6330.md#insn-008a6344)
- 新版 [`008da1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md#insn-008da1d4) · [`008da1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md#insn-008da1d8) · [`008da1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da1c8.md#insn-008da1dc)

~~~diff
- 008a633c ["INT_ADD", "register:40f0:8", ["const:8a633c:8", "const:4:8"]]
- 008a633c ["CALL", null, ["callee:00c57a90:8"]]
+ 008da1d4 ["INT_ADD", "register:40f0:8", ["const:8da1d4:8", "const:4:8"]]
+ 008da1d4 ["CALL", null, ["callee:00c57a90:8"]]
- 008a633c bytes 41d30c94
+ 008da1d4 bytes 2ff60d94
- 008a6340 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008da1d8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a6340 bytes 081b0090
+ 008da1d8 bytes 481d00d0
- 008a6344 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 008a6344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da1dc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 008da1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6344 bytes 08012f91
+ 008da1dc bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4b452de8b351f08e257d94acd2c358"></a>

### [`008a63b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a63b0.md) → [`008da248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md) FUN_008da248

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da25c",
      "incomplete_value": false,
      "site": "008da260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a63c4",
      "incomplete_value": false,
      "site": "008a63c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "008da260",
      "DATA",
      [
        "storage",
        "00c06c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da260",
      "DATA",
      [
        "storage",
        "00c84a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a63bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a63b0.md#insn-008a63bc) · [`008a63c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a63b0.md#insn-008a63c0) · [`008a63c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a63b0.md#insn-008a63c4)
- 新版 [`008da254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md#insn-008da254) · [`008da258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md#insn-008da258) · [`008da25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da248.md#insn-008da25c)

~~~diff
- 008a63bc ["INT_ADD", "register:40f0:8", ["const:8a63bc:8", "const:4:8"]]
- 008a63bc ["CALL", null, ["callee:00c57a90:8"]]
+ 008da254 ["INT_ADD", "register:40f0:8", ["const:8da254:8", "const:4:8"]]
+ 008da254 ["CALL", null, ["callee:00c57a90:8"]]
- 008a63bc bytes 21d30c94
+ 008da254 bytes 0ff60d94
- 008a63c0 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008da258 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a63c0 bytes 081b0090
+ 008da258 bytes 481d00d0
- 008a63c4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 008a63c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da25c ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 008da25c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da25c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da25c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 bytes 08013191
+ 008da25c bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad4a0620757c3d3d4d375c6ee8cbbcd4"></a>

### [`008a6430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6430.md) → [`008da2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md) FUN_008da2c8

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008da2dc",
      "incomplete_value": false,
      "site": "008da2e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6444",
      "incomplete_value": false,
      "site": "008a6448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "008da2e0",
      "DATA",
      [
        "storage",
        "00c06cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da2e0",
      "DATA",
      [
        "storage",
        "00c84a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a643c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6430.md#insn-008a643c) · [`008a6440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6430.md#insn-008a6440) · [`008a6444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6430.md#insn-008a6444)
- 新版 [`008da2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md#insn-008da2d4) · [`008da2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md#insn-008da2d8) · [`008da2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da2c8.md#insn-008da2dc)

~~~diff
- 008a643c ["INT_ADD", "register:40f0:8", ["const:8a643c:8", "const:4:8"]]
- 008a643c ["CALL", null, ["callee:00c57a90:8"]]
+ 008da2d4 ["INT_ADD", "register:40f0:8", ["const:8da2d4:8", "const:4:8"]]
+ 008da2d4 ["CALL", null, ["callee:00c57a90:8"]]
- 008a643c bytes 01d30c94
+ 008da2d4 bytes eff50d94
- 008a6440 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008da2d8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a6440 bytes 081b0090
+ 008da2d8 bytes 481d00d0
- 008a6444 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 008a6444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008da2dc ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 008da2dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008da2dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008da2dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6444 bytes 08013391
+ 008da2dc bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-effe5813d02ef3d4e5025b8bf330c173"></a>

### [`008a65cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a65cc.md) → [`008da464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md) FUN_008da464

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da48c",
      "incomplete_value": false,
      "site": "008da490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a65f4",
      "incomplete_value": false,
      "site": "008a65f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "008da490",
      "DATA",
      [
        "storage",
        "00c06dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da490",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a65e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a65cc.md#insn-008a65e0) · [`008a65f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a65cc.md#insn-008a65f0) · [`008a65f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a65cc.md#insn-008a65f4)
- 新版 [`008da478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da478) · [`008da488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da488) · [`008da48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da464.md#insn-008da48c)

~~~diff
- 008a65e0 ["INT_ADD", "register:40f0:8", ["const:8a65e0:8", "const:4:8"]]
- 008a65e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008da478 ["INT_ADD", "register:40f0:8", ["const:8da478:8", "const:4:8"]]
+ 008da478 ["CALL", null, ["callee:00c57a90:8"]]
- 008a65e0 bytes 98d20c94
+ 008da478 bytes 86f50d94
- 008a65f0 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008da488 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a65f0 bytes 091b0090
+ 008da488 bytes 491d00d0
- 008a65f4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 008a65f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008da48c ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 008da48c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008da48c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008da48c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 bytes 29413791
+ 008da48c bytes 29a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49cf32c66bfd3a0f6ad74679b4a1b928"></a>

### [`008a6664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6664.md) → [`008da4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md) FUN_008da4fc

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008da51c",
      "incomplete_value": false,
      "site": "008da520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6684",
      "incomplete_value": false,
      "site": "008a6688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "008da520",
      "DATA",
      [
        "storage",
        "00c06dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da520",
      "DATA",
      [
        "storage",
        "00c84ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6664.md#insn-008a6680) · [`008a6684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6664.md#insn-008a6684) · [`008a66a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6664.md#insn-008a66a8)
- 新版 [`008da518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da518) · [`008da51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da51c) · [`008da540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da4fc.md#insn-008da540)

~~~diff
- 008a6680 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008da518 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a6680 bytes 091b0090
+ 008da518 bytes 491d00d0
- 008a6684 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 008a6684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a6684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a6684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008da51c ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 008da51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008da51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008da51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a6684 bytes 29413791
+ 008da51c bytes 29a12e91
- 008a66a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a66a8 ["INT_ADD", "register:40f0:8", ["const:8a66a8:8", "const:4:8"]]
- 008a66a8 ["CALLIND", null, ["register:0:8"]]
+ 008da540 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da540 ["INT_ADD", "register:40f0:8", ["const:8da540:8", "const:4:8"]]
+ 008da540 ["CALLIND", null, ["register:0:8"]]
- 008a66a8 bytes 00013fd6
+ 008da540 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2c983dd8f607f3aca1d5f0316eab9a"></a>

### [`008a6770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6770.md) → [`008da608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md) FUN_008da608

採用 · 移動量 `+0x33e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00833b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833b3c.md) [`008a20d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a20d4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) [`008d5f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008da6d0",
      "incomplete_value": true,
      "site": "008da6d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:629:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6838",
      "incomplete_value": true,
      "site": "008a6838",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:121:8"
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
      "008da6b8",
      "READ",
      [
        "storage",
        "00291121",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008da6b8",
      "READ",
      [
        "storage",
        "002a0629",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6770.md#insn-008a67b4) · [`008a67d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6770.md#insn-008a67d4) · [`008a67e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6770.md#insn-008a67e0)
- 新版 [`008da64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da64c) · [`008da66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da66c) · [`008da678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008da608.md#insn-008da678)

~~~diff
- 008a67b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a67b4 ["INT_ADD", "register:40f0:8", ["const:8a67b4:8", "const:4:8"]]
- 008a67b4 ["CALLIND", null, ["register:0:8"]]
+ 008da64c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008da64c ["INT_ADD", "register:40f0:8", ["const:8da64c:8", "const:4:8"]]
+ 008da64c ["CALLIND", null, ["register:0:8"]]
- 008a67b4 bytes 00013fd6
+ 008da64c bytes 00013fd6
- 008a67d4 ["INT_ADD", "register:40f0:8", ["const:8a67d4:8", "const:4:8"]]
- 008a67d4 ["CALL", null, ["callee:00c538b0:8"]]
+ 008da66c ["INT_ADD", "register:40f0:8", ["const:8da66c:8", "const:4:8"]]
+ 008da66c ["CALL", null, ["callee:00c538b0:8"]]
- 008a67d4 bytes a3c10c94
+ 008da66c bytes 91e40d94
- 008a67e0 ["INT_ADD", "register:40f0:8", ["const:8a67e0:8", "const:4:8"]]
- 008a67e0 ["CALL", null, ["callee:00596eec:8"]]
+ 008da678 ["INT_ADD", "register:40f0:8", ["const:8da678:8", "const:4:8"]]
+ 008da678 ["CALL", null, ["callee:00596eec:8"]]
- 008a67e0 bytes 1d36f397
+ 008da678 bytes 1df2f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2b6fa46d829faa3de48bdbf88f6e5b"></a>

### [`008a6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c3c.md) → [`008daad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md) FUN_008daad4

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008daae0",
      "incomplete_value": false,
      "site": "008daaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6c48",
      "incomplete_value": false,
      "site": "008a6c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "008daaec",
      "DATA",
      [
        "storage",
        "00c06e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008daaec",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c3c.md#insn-008a6c44) · [`008a6c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c3c.md#insn-008a6c48)
- 新版 [`008daadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md#insn-008daadc) · [`008daae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008daad4.md#insn-008daae0)

~~~diff
- 008a6c44 ["COPY", "register:4050:8", ["const:c06000:8"]]
+ 008daadc ["COPY", "register:4050:8", ["const:c84000:8"]]
- 008a6c44 bytes 0a1b0090
+ 008daadc bytes 4a1d00d0
- 008a6c48 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008a6c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008daae0 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008daae0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008daae0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008daae0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 bytes 4a413991
+ 008daae0 bytes 4aa13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43752d7b84670ebbd9c75f3ecabcadb8"></a>

### [`008a6c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c80.md) → [`008dab18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md) FUN_008dab18

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "008dab30",
      "incomplete_value": false,
      "site": "008dab3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6c98",
      "incomplete_value": false,
      "site": "008a6ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "008dab3c",
      "DATA",
      [
        "storage",
        "00c06e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dab3c",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c80.md#insn-008a6c94) · [`008a6c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c80.md#insn-008a6c98) · [`008a6cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6c80.md#insn-008a6cc8)
- 新版 [`008dab2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab2c) · [`008dab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab30) · [`008dab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab18.md#insn-008dab60)

~~~diff
- 008a6c94 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008dab2c ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008a6c94 bytes 081b0090
+ 008dab2c bytes 481d00d0
- 008a6c98 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008a6c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008dab30 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008dab30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008dab30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008dab30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 bytes 08413991
+ 008dab30 bytes 08a13091
- 008a6cc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a6cc8 ["INT_ADD", "register:40f0:8", ["const:8a6cc8:8", "const:4:8"]]
- 008a6cc8 ["CALLIND", null, ["register:0:8"]]
+ 008dab60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dab60 ["INT_ADD", "register:40f0:8", ["const:8dab60:8", "const:4:8"]]
+ 008dab60 ["CALLIND", null, ["register:0:8"]]
- 008a6cc8 bytes 00013fd6
+ 008dab60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b7ce57fdb943146126ecee868f1025"></a>

### [`008a6cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6cdc.md) → [`008dab74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md) FUN_008dab74

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008dab9c",
      "incomplete_value": false,
      "site": "008daba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6d04",
      "incomplete_value": false,
      "site": "008a6d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "008daba0",
      "DATA",
      [
        "storage",
        "00c06e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008daba0",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6cdc.md#insn-008a6cf0) · [`008a6d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6cdc.md#insn-008a6d00) · [`008a6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6cdc.md#insn-008a6d04)
- 新版 [`008dab88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab88) · [`008dab98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab98) · [`008dab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dab74.md#insn-008dab9c)

~~~diff
- 008a6cf0 ["INT_ADD", "register:40f0:8", ["const:8a6cf0:8", "const:4:8"]]
- 008a6cf0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008dab88 ["INT_ADD", "register:40f0:8", ["const:8dab88:8", "const:4:8"]]
+ 008dab88 ["CALL", null, ["callee:00c57a90:8"]]
- 008a6cf0 bytes d4d00c94
+ 008dab88 bytes c2f30d94
- 008a6d00 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008dab98 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008a6d00 bytes 091b0090
+ 008dab98 bytes 491d00d0
- 008a6d04 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008a6d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008dab9c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008dab9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008dab9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008dab9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 bytes 29413991
+ 008dab9c bytes 29a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5351396da5074c4e53bb32321b75a085"></a>

### [`008a6d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6d6c.md) → [`008dac04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md) FUN_008dac04

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008dac20",
      "incomplete_value": false,
      "site": "008dac24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6d88",
      "incomplete_value": false,
      "site": "008a6d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "008dac24",
      "DATA",
      [
        "storage",
        "00c06e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008dac24",
      "DATA",
      [
        "storage",
        "00c84c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6d6c.md#insn-008a6d84) · [`008a6d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6d6c.md#insn-008a6d88) · [`008a6db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6d6c.md#insn-008a6db0)
- 新版 [`008dac1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac1c) · [`008dac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac20) · [`008dac48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dac04.md#insn-008dac48)

~~~diff
- 008a6d84 ["COPY", "register:4050:8", ["const:c06000:8"]]
+ 008dac1c ["COPY", "register:4050:8", ["const:c84000:8"]]
- 008a6d84 bytes 0a1b0090
+ 008dac1c bytes 4a1d00d0
- 008a6d88 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 008a6d88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008dac20 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008dac20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008dac20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008dac20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 bytes 4a413991
+ 008dac20 bytes 4aa13091
- 008a6db0 ["COPY", "register:0:8", ["register:4048:8"]]
- 008a6db0 ["INT_ADD", "register:40f0:8", ["const:8a6db0:8", "const:4:8"]]
- 008a6db0 ["CALLIND", null, ["register:0:8"]]
+ 008dac48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008dac48 ["INT_ADD", "register:40f0:8", ["const:8dac48:8", "const:4:8"]]
+ 008dac48 ["CALLIND", null, ["register:0:8"]]
- 008a6db0 bytes 20013fd6
+ 008dac48 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a02244c70347de368f75fdd5b3b5f82"></a>

### [`008a6e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e74.md) → [`008dad0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md) FUN_008dad0c

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00833b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833b3c.md) [`008a20d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a20d4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00596eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596eec.md) [`00865ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865ab4.md) [`008d5f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d5f6c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.18% / 新版 91.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008dae64",
      "incomplete_value": true,
      "site": "008dae80",
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
    "old": null,
    "ordinal": 9,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008a6fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e74.md#insn-008a6fe8) · [`008a6eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e74.md#insn-008a6eb8) · [`008a6ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a6/008a6e74.md#insn-008a6ed0)
- 新版 [`008dae80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md#insn-008dae80) · [`008dad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md#insn-008dad50) · [`008dad68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dad0c.md#insn-008dad68)

~~~diff
- 008a6fe8 ["INT_ADD", "register:40f0:8", ["const:8a6fe8:8", "const:4:8"]]
- 008a6fe8 ["CALL", null, ["callee:00865ab4:8"]]
+ 008dae80 ["INT_ADD", "register:40f0:8", ["const:8dae80:8", "const:4:8"]]
+ 008dae80 ["CALL", null, ["callee:00865ab4:8"]]
- 008a6fe8 bytes d532fe97
+ 008dae80 bytes 0d2bfe97
- 008a6eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008a6eb8 ["INT_ADD", "register:40f0:8", ["const:8a6eb8:8", "const:4:8"]]
- 008a6eb8 ["CALLIND", null, ["register:0:8"]]
+ 008dad50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008dad50 ["INT_ADD", "register:40f0:8", ["const:8dad50:8", "const:4:8"]]
+ 008dad50 ["CALLIND", null, ["register:0:8"]]
- 008a6eb8 bytes 00013fd6
+ 008dad50 bytes 00013fd6
- 008a6ed0 ["COPY", "register:0:8", ["register:4048:8"]]
- 008a6ed0 ["INT_ADD", "register:40f0:8", ["const:8a6ed0:8", "const:4:8"]]
- 008a6ed0 ["CALLIND", null, ["register:0:8"]]
+ 008dad68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 008dad68 ["INT_ADD", "register:40f0:8", ["const:8dad68:8", "const:4:8"]]
+ 008dad68 ["CALLIND", null, ["register:0:8"]]
- 008a6ed0 bytes 20013fd6
+ 008dad68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c36700b5764fd1c340fc36c73092c38"></a>

### [`008a7144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a7144.md) → [`008dafdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008da/008dafdc.md) _INIT_172

採用 · 移動量 `+0x33e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 54.80% / 新版 54.80%

CFGの説明率　旧版 64.86% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a7174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a7188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a718c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a7174",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a7180",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008a7188",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008db00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008db018",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "008db020",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a7144.md#insn-008a7174) · [`008a7188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a7144.md#insn-008a7188) · [`008a718c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a7144.md#insn-008a718c)

~~~diff
- 008a7174 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008a7174 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008a7174 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008a7174 bytes a9831ff8
- 008a7188 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 008a7188 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 008a7188 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008a7188 bytes ea130278
- 008a718c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008a718c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 008a718c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-667c0009535b6c7493c020a30d9bcd31"></a>

### [`008a75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a75e8.md) → [`008db480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md) FUN_008db480

採用 · 移動量 `+0x33e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008a74d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a74d4.md) [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) · 呼出先 4件 [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`008db36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db36c.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 4件 [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.63% / 新版 79.63%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a7604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008db49c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a765c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a7604",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a765c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008db520"
      ]
    ],
    [
      "unmatched:008a7668",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ],
  "added": [
    [
      "008db49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008db4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008db520"
      ]
    ],
    [
      "008db500",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a7604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a75e8.md#insn-008a7604) · [`008a7630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a75e8.md#insn-008a7630) · [`008a7648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a75e8.md#insn-008a7648)
- 新版 [`008db4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db480.md#insn-008db4e0)

~~~diff
- 008a7604 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008a7604 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008a7604 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008a7604 bytes a8831ff8
- 008a7630 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a7630 ["RETURN", null, ["register:0:8"]]
- 008a7630 bytes c0035fd6
- 008a7648 ["INT_ADD", "register:40f0:8", ["const:8a7648:8", "const:4:8"]]
- 008a7648 ["CALL", null, ["callee:006662e0:8"]]
+ 008db4e0 ["INT_ADD", "register:40f0:8", ["const:8db4e0:8", "const:4:8"]]
+ 008db4e0 ["CALL", null, ["callee:006662e0:8"]]
- 008a7648 bytes 7062f697
+ 008db4e0 bytes 802bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae295d1f662333123a287aa1b405447a"></a>

### [`008a76c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a76c0.md) → [`008db558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008db558.md) FUN_008db558

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md) [`0063e518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e518.md) [`0063f964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f964.md) [`0063f9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f9a0.md)
- 新版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`006647f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006647f0.md) [`00665c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c3c.md) [`00665c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665c78.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.60% / 新版 54.60%

CFGの説明率　旧版 8.43% / 新版 5.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 34件, `call_target` 1件, `store_condition` 5件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a76e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a76f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a76f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a76e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a76f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a7700",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063f964"
      ]
    ]
  ],
  "added": [
    [
      "008db580",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "008db588",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008db598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00665c3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a76e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a76c0.md#insn-008a76e8) · [`008a76f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a76c0.md#insn-008a76f0) · [`008a76f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a76c0.md#insn-008a76f4)

~~~diff
- 008a76e8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 008a76e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a76e8 bytes e80300f9
- 008a76f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008a76f0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008a76f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008a76f0 bytes a8031ff8
- 008a76f4 ["COPY", "tmp:0:4", ["register:4008:4"]]
- 008a76f4 ["COPY", "tmp:1:4", ["register:4010:4"]]
- 008a76f4 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 008a76f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:4"]]
- 008a76f4 bytes 01080229
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acd0c2475536543e7896c1d590cdd644"></a>

### [`008a8630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md) → [`008dc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md) FUN_008dc4c8

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008a99d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a99d0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`008dd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md) · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.67% / 新版 71.67%

CFGの説明率　旧版 31.82% / 新版 16.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a8648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a8648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008dc4e0"
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
      "unmatched:008a8648",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a865c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008a8664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008dc524"
      ]
    ]
  ],
  "added": [
    [
      "008dc4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008dc4f4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008dc4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008dc524"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a8648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md#insn-008a8648) · [`008a8664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md#insn-008a8664) · [`008a8680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md#insn-008a8680)
- 新版 [`008dc518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md#insn-008dc518)

~~~diff
- 008a8648 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008a8648 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008a8648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008a8648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a8648 bytes f44f06a9
- 008a8664 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008a8664 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008a8664 bytes 480100b4
- 008a8680 ["INT_ADD", "register:40f0:8", ["const:8a8680:8", "const:4:8"]]
- 008a8680 ["CALL", null, ["callee:00c58210:8"]]
+ 008dc518 ["INT_ADD", "register:40f0:8", ["const:8dc518:8", "const:4:8"]]
+ 008dc518 ["CALL", null, ["callee:00c58210:8"]]
- 008a8680 bytes 50cc0c94
+ 008dc518 bytes 3eef0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f788c36d84b1b7cf05036a18f6a43d09"></a>

### [`008a8ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8ffc.md) → [`008dce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dce94.md) FUN_008dce94

採用 · 移動量 `+0x33e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) · 呼出先 3件 [`008ab3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ab/008ab3d8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda00.md)
- 新版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 3件 [`008df27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008df/008df27c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.09% / 新版 72.09%

CFGの説明率　旧版 81.82% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a8ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a8ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a9000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a8ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a9000",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a9004",
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
      "008dce94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008dce98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008dce9c",
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

- 旧版 [`008a8ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8ffc.md#insn-008a8ffc) · [`008a9000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8ffc.md#insn-008a9000) · [`008a9004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8ffc.md#insn-008a9004)

~~~diff
- 008a8ffc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008a8ffc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008a8ffc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008a8ffc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008a8ffc bytes fd7bbca9
- 008a9000 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008a9000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008a9000 bytes f70b00f9
- 008a9004 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008a9004 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008a9004 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008a9004 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a9004 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71dd85806ed1ff1b5f29aa8feb332cf1"></a>

### [`008a99d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a99d0.md) → [`008dd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md) FUN_008dd868

採用 · 移動量 `+0x33e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008aaa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008aa/008aaa18.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008a8630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8630.md)
- 新版 呼出元 1件 [`008de8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008de/008de8bc.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008dc4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc4c8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.81% / 新版 71.81%

CFGの説明率　旧版 11.86% / 新版 18.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a99d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a99d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a99d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a99d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a99d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008a99d8",
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
      "008dd868",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008dd86c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008dd870",
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

- 旧版 [`008a99d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a99d0.md#insn-008a99d0) · [`008a99d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a99d0.md#insn-008a99d4) · [`008a99d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a99d0.md#insn-008a99d8)

~~~diff
- 008a99d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 008a99d0 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5120:8"]]
- 008a99d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 008a99d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008a99d0 bytes e923bb6d
- 008a99d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008a99d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008a99d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008a99d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a99d4 bytes fd7b01a9
- 008a99d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 008a99d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 008a99d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008a99d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008a99d8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465fb2f44f818e82ba6bd5478a25de3a"></a>

### [`008ac754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac754.md) → [`008e05f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e05f8.md) FUN_008e05f8

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008a90c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a90c0.md) [`008ac5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md) · 呼出先 2件 [`006acf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ac/006acf9c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 2件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) · 呼出先 2件 [`006d5e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d5/006d5e64.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.75% / 新版 91.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ac754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ac754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ac758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ac754",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ac758",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ac75c",
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
      "008e05f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008e05fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008e0600",
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

- 旧版 [`008ac754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac754.md#insn-008ac754) · [`008ac758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac754.md#insn-008ac758) · [`008ac75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac754.md#insn-008ac75c)

~~~diff
- 008ac754 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ac754 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ac754 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008ac754 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008ac754 bytes fd7bbca9
- 008ac758 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008ac758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008ac758 bytes f70b00f9
- 008ac75c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008ac75c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008ac75c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008ac75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ac75c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4edb90babe43ea57d84707d722cdb55e"></a>

### [`008aca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008aca00.md) → [`008e08a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e08a4.md) FUN_008e08a4

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ac5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`008e0458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0458.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 88.24% / 新版 93.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 5件

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008aca18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008aca1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008aca30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008aca3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e08f4"
      ]
    ]
  ],
  "added": [
    [
      "008e08e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e08f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008aca18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008aca00.md#insn-008aca18) · [`008aca1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008aca00.md#insn-008aca1c) · [`008aca30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008aca00.md#insn-008aca30)

~~~diff
- 008aca18 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 008aca18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008aca18 bytes 081000f9
- 008aca1c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008aca1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008aca1c bytes 0004803d
- 008aca30 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008aca30 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:30:8"]]
- 008aca30 ["STORE", null, ["const:1b1:8", "register:4048:8", "tmp:0:8"]]
- 008aca30 bytes 2a0d03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd36337df1605265f945d38eacd5c62"></a>

### [`008acbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md) → [`008e0a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e0/008e0a94.md) FUN_008e0a94

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a9c80.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md)
- 新版 呼出元 1件 [`008ddb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddb18.md) · 呼出先 13件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`00758190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/00758190.md) [`0086369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00863/0086369c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 31.99% / 新版 31.99%

CFGの説明率　旧版 8.85% / 新版 9.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 6件, `unresolved_branch_alignment` 61件, `unresolved_call_alignment` 64件, `unresolved_store_alignment` 100件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008acc34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008acc3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008acc50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008acc34",
      "DATA",
      [
        "storage",
        "00c06ee8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008acc40",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:008acc44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e1460"
      ]
    ]
  ],
  "added": [
    [
      "008e0ad8",
      "DATA",
      [
        "storage",
        "00c84cc0",
        null,
        "pointer"
      ]
    ],
    [
      "008e0ae4",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e0ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e1460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008acc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md#insn-008acc34) · [`008acc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md#insn-008acc3c) · [`008acc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md#insn-008acc50)

~~~diff
- 008acc34 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 008acc34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008acc34 bytes 680200f9
- 008acc3c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008acc3c ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:2f0:8"]]
- 008acc3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008acc3c bytes 68c20b39
- 008acc50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008acc50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008acc50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 008acc50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008acc50 bytes ffaf0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8758c122bd4b6ecff04a47e65c9a55da"></a>

### [`008ad8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad8d4.md) → [`008e1778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md) FUN_008e1778

採用 · 移動量 `+0x33ea4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e1790",
      "incomplete_value": false,
      "site": "008e1794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad8ec",
      "incomplete_value": false,
      "site": "008ad8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e17cc",
      "incomplete_value": false,
      "site": "008e17d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad928",
      "incomplete_value": false,
      "site": "008ad92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "008e1794",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "008e17d0",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008e1794",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "008e17d0",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad8d4.md#insn-008ad8e8) · [`008ad8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad8d4.md#insn-008ad8ec) · [`008ad900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad8d4.md#insn-008ad900)
- 新版 [`008e178c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e178c) · [`008e1790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e1790) · [`008e17a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1778.md#insn-008e17a4)

~~~diff
- 008ad8e8 ["COPY", "register:4040:8", ["const:bfa000:8"]]
+ 008e178c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 008ad8e8 bytes 681a00b0
+ 008e178c bytes a81c00d0
- 008ad8ec ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008ad8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e1790 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 008e1790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec bytes 08213891
+ 008e1790 bytes 08c13c91
- 008ad900 ["INT_ADD", "register:40f0:8", ["const:8ad900:8", "const:4:8"]]
- 008ad900 ["CALL", null, ["callee:00c538e0:8"]]
+ 008e17a4 ["INT_ADD", "register:40f0:8", ["const:8e17a4:8", "const:4:8"]]
+ 008e17a4 ["CALL", null, ["callee:00c538e0:8"]]
- 008ad900 bytes 64a50c94
+ 008e17a4 bytes 4fc80d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ff8eef4da5a86cc9088293d0533e72"></a>

### [`008ad974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad974.md) → [`008e1818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md) _INIT_173

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

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
      "definition_site": "008e1854",
      "incomplete_value": true,
      "site": "008e1870",
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
    "old": {
      "definition_site": "008ad9b0",
      "incomplete_value": true,
      "site": "008ad9cc",
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
                "const:377:8"
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
      "definition_site": "008e1878",
      "incomplete_value": true,
      "site": "008e1894",
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
    "old": {
      "definition_site": "008ad9d4",
      "incomplete_value": true,
      "site": "008ad9f0",
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
                "const:38a:8"
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
      "definition_site": "008e1898",
      "incomplete_value": true,
      "site": "008e18b4",
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
    "old": {
      "definition_site": "008ad9f4",
      "incomplete_value": true,
      "site": "008ada10",
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
                "const:2a8000:8"
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
      "008e1854",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008e1878",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008e1898",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e1854",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "008e1878",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "008e1898",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008adad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad974.md#insn-008adad4) · [`008adba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad974.md#insn-008adba8) · [`008ad99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad974.md#insn-008ad99c)
- 新版 [`008e1978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e1978) · [`008e1a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e1a4c) · [`008e1840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1818.md#insn-008e1840)

~~~diff
- 008adad4 ["INT_ADD", "register:40f0:8", ["const:8adad4:8", "const:4:8"]]
- 008adad4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 008e1978 ["INT_ADD", "register:40f0:8", ["const:8e1978:8", "const:4:8"]]
+ 008e1978 ["CALL", null, ["callee:0043b7b8:8"]]
- 008adad4 bytes 79aced97
+ 008e1978 bytes 9067ed97
- 008adba8 ["INT_ADD", "register:40f0:8", ["const:8adba8:8", "const:4:8"]]
- 008adba8 ["CALL", null, ["callee:00c57a30:8"]]
+ 008e1a4c ["INT_ADD", "register:40f0:8", ["const:8e1a4c:8", "const:4:8"]]
+ 008e1a4c ["CALL", null, ["callee:00c57a30:8"]]
- 008adba8 bytes 0eb50c94
+ 008e1a4c bytes f9d70d94
- 008ad99c ["COPY", "register:4098:8", ["const:109e000:8"]]
+ 008e1840 ["COPY", "register:4098:8", ["const:1123000:8"]]
- 008ad99c bytes 933f00b0
+ 008e1840 bytes 134200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e91bba907e6d01baa1e1a0629c52c8"></a>

### [`008add04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008add04.md) → [`008e1ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md) FUN_008e1ba8

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.55% / 新版 88.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e1bf4",
      "incomplete_value": false,
      "site": "008e1bfc",
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
    "old": {
      "definition_site": "008add50",
      "incomplete_value": false,
      "site": "008add58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "008e1c20",
      "incomplete_value": true,
      "site": "008e1c30",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:226:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008add7c",
      "incomplete_value": true,
      "site": "008add8c",
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
                "const:b35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e1c34",
      "incomplete_value": true,
      "site": "008e1c34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008add90",
      "incomplete_value": true,
      "site": "008add90",
      "value": [
        "LOAD",
        "8",
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
      "008e1bfc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008e1c20",
      "READ",
      [
        "storage",
        "002a3b35",
        null,
        "string"
      ]
    ],
    [
      "008e1c24",
      "READ",
      [
        "storage",
        "002a3b44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e1bfc",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "008e1c20",
      "READ",
      [
        "storage",
        "002b4226",
        null,
        "string"
      ]
    ],
    [
      "008e1c24",
      "READ",
      [
        "storage",
        "002b4235",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008add3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008add04.md#insn-008add3c) · [`008add4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008add04.md#insn-008add4c) · [`008add50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008add04.md#insn-008add50)
- 新版 [`008e1be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1be0) · [`008e1bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1bf0) · [`008e1bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e1/008e1ba8.md#insn-008e1bf4)

~~~diff
- 008add3c ["INT_ADD", "register:40f0:8", ["const:8add3c:8", "const:4:8"]]
- 008add3c ["CALL", null, ["callee:00487de0:8"]]
+ 008e1be0 ["INT_ADD", "register:40f0:8", ["const:8e1be0:8", "const:4:8"]]
+ 008e1be0 ["CALL", null, ["callee:00487de0:8"]]
- 008add3c bytes 83dcee97
+ 008e1be0 bytes 8098ee97
- 008add4c ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 008e1bf0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 008add4c bytes c81900d0
+ 008e1bf0 bytes 081c00f0
- 008add50 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 008add50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e1bf4 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 008e1bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008add50 bytes 08e13591
+ 008e1bf4 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55e209b40ec21b88fe68545924b3191"></a>

### [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) → [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) FUN_008e2720

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e2764",
      "incomplete_value": false,
      "site": "008e276c",
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
    "old": {
      "definition_site": "008ae8c0",
      "incomplete_value": false,
      "site": "008ae8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "008e2784",
      "incomplete_value": true,
      "site": "008e2790",
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
                "const:777:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ae8e0",
      "incomplete_value": true,
      "site": "008ae8ec",
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
                "const:b1b:8"
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
      "definition_site": "008e28b0",
      "incomplete_value": true,
      "site": "008e28b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008aea0c",
      "incomplete_value": true,
      "site": "008aea0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b3d:8"
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
      "008e276c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2784",
      "READ",
      [
        "storage",
        "002a7b1b",
        null,
        "string"
      ]
    ],
    [
      "008e28a0",
      "READ",
      [
        "storage",
        "0029bb3d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e276c",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2784",
      "READ",
      [
        "storage",
        "002b8777",
        null,
        "string"
      ]
    ],
    [
      "008e28a0",
      "READ",
      [
        "storage",
        "002abbed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ae8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md#insn-008ae8b4) · [`008ae8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md#insn-008ae8bc) · [`008ae8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md#insn-008ae8c0)
- 新版 [`008e2758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2758) · [`008e2760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2760) · [`008e2764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md#insn-008e2764)

~~~diff
- 008ae8b4 ["INT_ADD", "register:40f0:8", ["const:8ae8b4:8", "const:4:8"]]
- 008ae8b4 ["CALL", null, ["callee:00487de0:8"]]
+ 008e2758 ["INT_ADD", "register:40f0:8", ["const:8e2758:8", "const:4:8"]]
+ 008e2758 ["CALL", null, ["callee:00487de0:8"]]
- 008ae8b4 bytes a5d9ee97
+ 008e2758 bytes a295ee97
- 008ae8bc ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 008e2760 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 008ae8bc bytes c81900b0
+ 008e2760 bytes 081c00d0
- 008ae8c0 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 008ae8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e2764 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 008e2764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 bytes 08e13591
+ 008e2764 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d699a40e439d01ef819f7645faed792"></a>

### [`008af36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md) → [`008e3210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e3/008e3210.md) FUN_008e3210

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d4c.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) · 呼出先 22件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6eec.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.27% / 新版 83.27%

CFGの説明率　旧版 75.73% / 新版 74.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `call_target` 2件, `store_value` 4件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008af4cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008af4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008af4f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e3254",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008e3260",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3268",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e3254",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008e3260",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e3268",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008af4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md#insn-008af4cc) · [`008af4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md#insn-008af4e8) · [`008af4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md#insn-008af4ec)

~~~diff
- 008af4cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008af4cc ["COPY", "tmp:1:8", ["register:4000:8"]]
- 008af4cc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 008af4cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008af4cc bytes 080405f8
- 008af4e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008af4e8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008af4e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008af4e8 bytes ff0f00f9
- 008af4ec ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 008af4ec ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008af4ec bytes b60200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9dec78e1f4d3945b106af8d18b5d9ae"></a>

### [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) → [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) FUN_008e4804

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b5c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5c4c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`008e9af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9af0.md) · 呼出先 26件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.64% / 新版 93.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 2件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e498c",
      "incomplete_value": true,
      "site": "008e49a0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:ad4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b0ae8",
      "incomplete_value": true,
      "site": "008b0afc",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:74f:8"
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
      "definition_site": "008e49a4",
      "incomplete_value": true,
      "site": "008e49a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b0b00",
      "incomplete_value": true,
      "site": "008b0b00",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008e4df0",
      "incomplete_value": false,
      "site": "008e4df0",
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
                "const:b00:8"
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
      "definition_site": "008b0f4c",
      "incomplete_value": false,
      "site": "008b0f4c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
    "ordinal": 53,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e4978",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008e498c",
      "READ",
      [
        "storage",
        "0029e74f",
        null,
        "string"
      ]
    ],
    [
      "008e4990",
      "READ",
      [
        "storage",
        "0029e75c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e4978",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e498c",
      "READ",
      [
        "storage",
        "002aead4",
        null,
        "string"
      ]
    ],
    [
      "008e4990",
      "READ",
      [
        "storage",
        "002aeae1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md#insn-008b0a4c) · [`008b0b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md#insn-008b0b08) · [`008b0b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md#insn-008b0b48)
- 新版 [`008e48f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e48f0) · [`008e49ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e49ac) · [`008e49ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md#insn-008e49ec)

~~~diff
- 008b0a4c ["INT_ADD", "register:40f0:8", ["const:8b0a4c:8", "const:4:8"]]
- 008b0a4c ["CALL", null, ["callee:00b3baf8:8"]]
+ 008e48f0 ["INT_ADD", "register:40f0:8", ["const:8e48f0:8", "const:4:8"]]
+ 008e48f0 ["CALL", null, ["callee:00b3baf8:8"]]
- 008b0a4c bytes b5ad0894
+ 008e48f0 bytes 825c0994
- 008b0b08 ["INT_ADD", "register:40f0:8", ["const:8b0b08:8", "const:4:8"]]
- 008b0b08 ["CALL", null, ["ram:6f3104:8"]]
+ 008e49ac ["INT_ADD", "register:40f0:8", ["const:8e49ac:8", "const:4:8"]]
+ 008e49ac ["CALL", null, ["ram:71d16c:8"]]
- 008b0b08 bytes 7f09f997
+ 008e49ac bytes f0e1f897
- 008b0b48 ["INT_ADD", "register:40f0:8", ["const:8b0b48:8", "const:4:8"]]
- 008b0b48 ["CALL", null, ["callee:0047e5cc:8"]]
+ 008e49ec ["INT_ADD", "register:40f0:8", ["const:8e49ec:8", "const:4:8"]]
+ 008e49ec ["CALL", null, ["callee:0047e5cc:8"]]
- 008b0b48 bytes fbaaee97
+ 008e49ec bytes f866ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a62e3981ab8418ae0e6a0da4a8b0a4"></a>

### [`008b11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md) → [`008e5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md) FUN_008e5048

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b627c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006b5748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5748.md)
- 新版 呼出元 1件 [`008ea120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea120.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006df504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006df504.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.97% / 新版 83.97%

CFGの説明率　旧版 74.40% / 新版 73.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `store_value` 4件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e50b8",
      "incomplete_value": true,
      "site": "008e50c8",
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
                "const:2f9000:8"
              ],
              [
                "leaf",
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1214",
      "incomplete_value": true,
      "site": "008b1224",
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
                "const:2e6000:8"
              ],
              [
                "leaf",
                "const:7f4:8"
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
      "definition_site": "008e50b8",
      "incomplete_value": true,
      "site": "008e50c8",
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
      "definition_site": "008b1214",
      "incomplete_value": true,
      "site": "008b1224",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b1434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e50b8",
      "READ",
      [
        "storage",
        "002e67f4",
        null,
        null
      ]
    ],
    [
      "008e50b8",
      "READ",
      [
        "storage",
        "002e6804",
        null,
        null
      ]
    ],
    [
      "unmatched:008b1418",
      "READ",
      [
        "storage",
        "002a7b2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e50b8",
      "READ",
      [
        "storage",
        "002f9a50",
        null,
        null
      ]
    ],
    [
      "008e50b8",
      "READ",
      [
        "storage",
        "002f9a60",
        null,
        null
      ]
    ],
    [
      "008e52bc",
      "READ",
      [
        "storage",
        "002b8788",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b1434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md#insn-008b1434) · [`008b1470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md#insn-008b1470) · [`008b1474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md#insn-008b1474)

~~~diff
- 008b1434 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 008b1434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008b1434 bytes 2003803d
- 008b1470 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 008b1470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008b1470 bytes e83300f9
- 008b1474 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 008b1474 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008b1474 bytes e017803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d486de84a1e5cf5440619ed839f67eae"></a>

### [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) → [`008e5de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5de0.md) FUN_008e5de0

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c620.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`006b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2968.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 66.67% / 新版 63.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e5e8c",
      "incomplete_value": true,
      "site": "008e5e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e24:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1fe8",
      "incomplete_value": true,
      "site": "008b1fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:1ec:8"
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
      "definition_site": "008e5e90",
      "incomplete_value": true,
      "site": "008e5e90",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1fec",
      "incomplete_value": true,
      "site": "008b1fec",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e5eb4",
      "incomplete_value": true,
      "site": "008e5ec8",
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
                "const:102:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2010",
      "incomplete_value": true,
      "site": "008b2024",
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
                "const:ce4:8"
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
      "008e5e68",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008e5e7c",
      "READ",
      [
        "storage",
        "002981ec",
        null,
        "string"
      ]
    ],
    [
      "008e5e80",
      "READ",
      [
        "storage",
        "002981f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e5e68",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "008e5e7c",
      "READ",
      [
        "storage",
        "002a7e24",
        null,
        "string"
      ]
    ],
    [
      "008e5e80",
      "READ",
      [
        "storage",
        "002a7e2a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b20f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md#insn-008b20f4) · [`008b20fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md#insn-008b20fc) · [`008b2100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md#insn-008b2100)

~~~diff
- 008b20f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 008b20f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b20f4 bytes 68fa02b9
- 008b20fc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008b20fc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:69:8"]]
- 008b20fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008b20fc bytes e8930678
- 008b2100 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:59:8"]]
- 008b2100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008b2100 bytes e093853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-554e77b5ef21ee70b1124704c4d4f2a2"></a>

### [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) → [`008e6510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md) FUN_008e6510

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c7d4.md) · 呼出先 42件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0042bab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md)
- 新版 呼出元 1件 [`006b2b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2b1c.md) · 呼出先 42件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0044e948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044e948.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 79.94% / 新版 79.94%

CFGの説明率　旧版 73.81% / 新版 74.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 11件, `store_value` 10件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e6608",
      "incomplete_value": true,
      "site": "008e6608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "008b2764",
      "incomplete_value": true,
      "site": "008b2764",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
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
      "definition_site": "008e66ac",
      "incomplete_value": true,
      "site": "008e66ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2808",
      "incomplete_value": true,
      "site": "008b2808",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e66c4",
      "incomplete_value": false,
      "site": "008e66c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2820",
      "incomplete_value": false,
      "site": "008b2820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "008e6588",
      "DATA",
      [
        "storage",
        "00397054",
        "fde_00397054",
        "dword"
      ]
    ],
    [
      "008e6590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b2864"
      ]
    ],
    [
      "008e65a0",
      "DATA",
      [
        "storage",
        "0039705c",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008e6588",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "008e6590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e6708"
      ]
    ],
    [
      "008e65a0",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b26bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md#insn-008b26bc) · [`008b2738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md#insn-008b2738) · [`008b27d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md#insn-008b27d4)
- 新版 [`008e6560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e6560) · [`008e65dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e65dc) · [`008e6678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e6/008e6510.md#insn-008e6678)

~~~diff
- 008b26bc ["INT_ADD", "register:40f0:8", ["const:8b26bc:8", "const:4:8"]]
- 008b26bc ["CALL", null, ["callee:0046ee18:8"]]
+ 008e6560 ["INT_ADD", "register:40f0:8", ["const:8e6560:8", "const:4:8"]]
+ 008e6560 ["CALL", null, ["callee:0046ee18:8"]]
- 008b26bc bytes 3166ee97
+ 008e6560 bytes 2e22ee97
- 008b2738 ["INT_ADD", "register:40f0:8", ["const:8b2738:8", "const:4:8"]]
- 008b2738 ["CALL", null, ["ram:469e20:8"]]
+ 008e65dc ["INT_ADD", "register:40f0:8", ["const:8e65dc:8", "const:4:8"]]
+ 008e65dc ["CALL", null, ["ram:48ccb8:8"]]
- 008b2738 bytes baddee97
+ 008e65dc bytes b799ee97
- 008b27d4 ["INT_ADD", "register:40f0:8", ["const:8b27d4:8", "const:4:8"]]
- 008b27d4 ["CALL", null, ["callee:008bb4e8:8"]]
+ 008e6678 ["INT_ADD", "register:40f0:8", ["const:8e6678:8", "const:4:8"]]
+ 008e6678 ["CALL", null, ["callee:008bb4e8:8"]]
- 008b27d4 bytes a156ff97
+ 008e6678 bytes 9c53ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79bde523a96e84f5550ca16cc7aeda7"></a>

### [`008b3390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md) → [`008e7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md) FUN_008e7234

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)
- 新版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 15件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 76.30% / 新版 76.30%

CFGの説明率　旧版 47.37% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e7278",
      "incomplete_value": true,
      "site": "008e7278",
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
      "definition_site": "008b33d4",
      "incomplete_value": true,
      "site": "008b33d4",
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
      "site": "008b3710"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b37b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e7274",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008e7280",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e7288",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e7274",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008e7280",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e7288",
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b33ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md#insn-008b33ec) · [`008b351c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md#insn-008b351c) · [`008b3588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md#insn-008b3588)
- 新版 [`008e7290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md#insn-008e7290) · [`008e73c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e7234.md#insn-008e73c0)

~~~diff
- 008b33ec ["INT_ADD", "register:40f0:8", ["const:8b33ec:8", "const:4:8"]]
- 008b33ec ["CALL", null, ["callee:00c58210:8"]]
+ 008e7290 ["INT_ADD", "register:40f0:8", ["const:8e7290:8", "const:4:8"]]
+ 008e7290 ["CALL", null, ["callee:00c58210:8"]]
- 008b33ec bytes f5a00c94
+ 008e7290 bytes e0c30d94
- 008b351c ["INT_ADD", "register:40f0:8", ["const:8b351c:8", "const:4:8"]]
- 008b351c ["CALL", null, ["callee:00470074:8"]]
+ 008e73c0 ["INT_ADD", "register:40f0:8", ["const:8e73c0:8", "const:4:8"]]
+ 008e73c0 ["CALL", null, ["callee:00470074:8"]]
- 008b351c bytes 3067ee97
+ 008e73c0 bytes 2d23ee97
- 008b3588 ["INT_ADD", "register:40f0:8", ["const:8b3588:8", "const:4:8"]]
- 008b3588 ["CALL", null, ["callee:008514b8:8"]]
- 008b3588 bytes feaffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2d733269241d7a7e94fead49062385"></a>

### [`008b3a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3a28.md) → [`008e78cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e7/008e78cc.md) FUN_008e78cc

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md)
- 新版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.62% / 新版 71.62%

CFGの説明率　旧版 37.16% / 新版 34.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 5件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b3abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b3d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b3df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e7914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b402c"
      ]
    ],
    [
      "008e7924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b402c"
      ]
    ],
    [
      "008e7938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b402c"
      ]
    ]
  ],
  "added": [
    [
      "008e7914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7ed0"
      ]
    ],
    [
      "008e7924",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7ed0"
      ]
    ],
    [
      "008e7938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e7ed0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b3abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3a28.md#insn-008b3abc) · [`008b3ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3a28.md#insn-008b3ac0) · [`008b3af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3a28.md#insn-008b3af4)

~~~diff
- 008b3abc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2e0:8"]]
- 008b3abc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008b3abc bytes 747201f9
- 008b3ac0 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 008b3ac0 bytes c2000054
- 008b3af4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008b3af4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008b3af4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008b3af4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008b3af4 bytes 2831889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f61a18150605e9b0b8fffdca386b60c7"></a>

### [`008b4224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md) → [`008e80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md) FUN_008e80c8

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008af0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md) [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) [`008b4610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008e2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2f58.md) [`008e4804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e4804.md) [`008e84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e80d8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b4234",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e80d4",
      "incomplete_value": false,
      "site": "008e80d8",
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
      "definition_site": "008b4230",
      "incomplete_value": false,
      "site": "008b4234",
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
      "008e80d4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e80d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e80d4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e80d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b4234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md#insn-008b4234) · [`008b422c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md#insn-008b422c) · [`008b4230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md#insn-008b4230)
- 新版 [`008e80d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md#insn-008e80d8) · [`008e80d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md#insn-008e80d0) · [`008e80d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e80c8.md#insn-008e80d4)

~~~diff
- 008b4234 ["INT_ADD", "register:40f0:8", ["const:8b4234:8", "const:4:8"]]
- 008b4234 ["CALL", null, ["ram:418c38:8"]]
+ 008e80d8 ["INT_ADD", "register:40f0:8", ["const:8e80d8:8", "const:4:8"]]
+ 008e80d8 ["CALL", null, ["ram:43b738:8"]]
- 008b4234 bytes 8192ed97
+ 008e80d8 bytes 984ded97
- 008b422c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e80d0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b422c bytes 80cffff0
+ 008e80d0 bytes 60cefff0
- 008b4230 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b4230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e80d4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e80d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e80d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e80d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4230 bytes 00740e91
+ 008e80d4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b58454387e1bcd880e76d2ba9e90f8"></a>

### [`008b450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md) → [`008e83b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md) FUN_008e83b0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008b4328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md) [`008b4e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008e81cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e81cc.md) [`008e8ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ca4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e83c0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b451c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e83bc",
      "incomplete_value": false,
      "site": "008e83c0",
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
      "definition_site": "008b4518",
      "incomplete_value": false,
      "site": "008b451c",
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
      "008e83bc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e83c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e83bc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e83c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b451c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md#insn-008b451c) · [`008b4514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md#insn-008b4514) · [`008b4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md#insn-008b4518)
- 新版 [`008e83c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md#insn-008e83c0) · [`008e83b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md#insn-008e83b8) · [`008e83bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e83b0.md#insn-008e83bc)

~~~diff
- 008b451c ["INT_ADD", "register:40f0:8", ["const:8b451c:8", "const:4:8"]]
- 008b451c ["CALL", null, ["ram:418c38:8"]]
+ 008e83c0 ["INT_ADD", "register:40f0:8", ["const:8e83c0:8", "const:4:8"]]
+ 008e83c0 ["CALL", null, ["ram:43b738:8"]]
- 008b451c bytes c791ed97
+ 008e83c0 bytes de4ced97
- 008b4514 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e83b8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b4514 bytes 80cffff0
+ 008e83b8 bytes 60cefff0
- 008b4518 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b4518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e83bc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e83bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e83bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e83bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4518 bytes 00740e91
+ 008e83bc bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44da7463cb74bba9aef85e0fe7b7fc28"></a>

### [`008b45fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md) → [`008e84a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md) FUN_008e84a0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) [`008b4c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) [`008e8b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8b1c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e84b0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b460c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e84ac",
      "incomplete_value": false,
      "site": "008e84b0",
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
      "definition_site": "008b4608",
      "incomplete_value": false,
      "site": "008b460c",
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
      "008e84ac",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e84b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e84ac",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e84b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b460c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md#insn-008b460c) · [`008b4604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md#insn-008b4604) · [`008b4608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md#insn-008b4608)
- 新版 [`008e84b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md#insn-008e84b0) · [`008e84a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md#insn-008e84a8) · [`008e84ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e84a0.md#insn-008e84ac)

~~~diff
- 008b460c ["INT_ADD", "register:40f0:8", ["const:8b460c:8", "const:4:8"]]
- 008b460c ["CALL", null, ["ram:418c38:8"]]
+ 008e84b0 ["INT_ADD", "register:40f0:8", ["const:8e84b0:8", "const:4:8"]]
+ 008e84b0 ["CALL", null, ["ram:43b738:8"]]
- 008b460c bytes 8b91ed97
+ 008e84b0 bytes a24ced97
- 008b4604 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e84a8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b4604 bytes 80cffff0
+ 008e84a8 bytes 60cefff0
- 008b4608 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e84ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e84ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e84ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e84ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4608 bytes 00740e91
+ 008e84ac bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be5f5d086bc900f3f8e19edc638b16fb"></a>

### [`008b47cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47cc.md) → [`008e8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md) FUN_008e8670

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) [`008e43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e43f4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e8680",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b47dc",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e867c",
      "incomplete_value": false,
      "site": "008e8680",
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
      "definition_site": "008b47d8",
      "incomplete_value": false,
      "site": "008b47dc",
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
      "008e867c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e8680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e867c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e8680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b47dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47cc.md#insn-008b47dc) · [`008b47d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47cc.md#insn-008b47d4) · [`008b47d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47cc.md#insn-008b47d8)
- 新版 [`008e8680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md#insn-008e8680) · [`008e8678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md#insn-008e8678) · [`008e867c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8670.md#insn-008e867c)

~~~diff
- 008b47dc ["INT_ADD", "register:40f0:8", ["const:8b47dc:8", "const:4:8"]]
- 008b47dc ["CALL", null, ["ram:418c38:8"]]
+ 008e8680 ["INT_ADD", "register:40f0:8", ["const:8e8680:8", "const:4:8"]]
+ 008e8680 ["CALL", null, ["ram:43b738:8"]]
- 008b47dc bytes 1791ed97
+ 008e8680 bytes 2e4ced97
- 008b47d4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e8678 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b47d4 bytes 80cffff0
+ 008e8678 bytes 60cefff0
- 008b47d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b47d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e867c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e867c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e867c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e867c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 bytes 00740e91
+ 008e867c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234e56a6124fd0b14ba4c6b580316e01"></a>

### [`008b49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md) → [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) FUN_008e8868

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008b47e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md) [`008b4f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md) [`008b6558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008e8684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8684.md) [`008e8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md) [`008ea3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea3fc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e8878",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b49d4",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e8874",
      "incomplete_value": false,
      "site": "008e8878",
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
      "definition_site": "008b49d0",
      "incomplete_value": false,
      "site": "008b49d4",
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
      "008e8874",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e8878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e8874",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e8878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b49d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md#insn-008b49d4) · [`008b49cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md#insn-008b49cc) · [`008b49d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md#insn-008b49d0)
- 新版 [`008e8878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md#insn-008e8878) · [`008e8870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md#insn-008e8870) · [`008e8874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md#insn-008e8874)

~~~diff
- 008b49d4 ["INT_ADD", "register:40f0:8", ["const:8b49d4:8", "const:4:8"]]
- 008b49d4 ["CALL", null, ["ram:418c38:8"]]
+ 008e8878 ["INT_ADD", "register:40f0:8", ["const:8e8878:8", "const:4:8"]]
+ 008e8878 ["CALL", null, ["ram:43b738:8"]]
- 008b49d4 bytes 9990ed97
+ 008e8878 bytes b04bed97
- 008b49cc ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e8870 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b49cc bytes 80cffff0
+ 008e8870 bytes 60cefff0
- 008b49d0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b49d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8874 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e8874 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8874 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8874 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 bytes 00740e91
+ 008e8874 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c65806d56a7a9264d278c3fe10b4efaa"></a>

### [`008b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md) → [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) FUN_008e8ab4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008b4a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md) [`008b50f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b50f8.md) [`008b635c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008e88d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e88d0.md) [`008e8f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md) [`008ea200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea200.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008e8ac4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b4c20",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e8ac0",
      "incomplete_value": false,
      "site": "008e8ac4",
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
      "definition_site": "008b4c1c",
      "incomplete_value": false,
      "site": "008b4c20",
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
      "008e8ac0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008e8ac4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008e8ac0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008e8ac4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b4c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md#insn-008b4c20) · [`008b4c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md#insn-008b4c18) · [`008b4c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md#insn-008b4c1c)
- 新版 [`008e8ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md#insn-008e8ac4) · [`008e8abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md#insn-008e8abc) · [`008e8ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md#insn-008e8ac0)

~~~diff
- 008b4c20 ["INT_ADD", "register:40f0:8", ["const:8b4c20:8", "const:4:8"]]
- 008b4c20 ["CALL", null, ["ram:418c38:8"]]
+ 008e8ac4 ["INT_ADD", "register:40f0:8", ["const:8e8ac4:8", "const:4:8"]]
+ 008e8ac4 ["CALL", null, ["ram:43b738:8"]]
- 008b4c20 bytes 0690ed97
+ 008e8ac4 bytes 1d4bed97
- 008b4c18 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008e8abc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008b4c18 bytes 80cffff0
+ 008e8abc bytes 60cefff0
- 008b4c1c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008b4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e8ac0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008e8ac0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8ac0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e8ac0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c bytes 00740e91
+ 008e8ac0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-226d696ee629710dc6752057fd4b8e58"></a>

### [`008b50f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b50f8.md) → [`008e8f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md) FUN_008e8f9c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`008b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8ab4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 79.17% / 新版 73.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b51dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008e9080"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "008b521c",
      "incomplete_value": true,
      "site": "008b5230",
      "value": [
        "live",
        "register:40a8:8"
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
      "unmatched:008b51dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9054"
      ]
    ]
  ],
  "added": [
    [
      "008e9080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b51dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b50f8.md#insn-008b51dc) · [`008b5124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b50f8.md#insn-008b5124)
- 新版 [`008e9080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md#insn-008e9080) · [`008e8fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8f9c.md#insn-008e8fc8)

~~~diff
- 008b51dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008b51dc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008b51dc bytes a1feff54
+ 008e9080 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008e9080 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008e9080 bytes a1feff54
- 008b5124 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008b5124 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 008e8fc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 008e8fc8 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 008b5124 bytes 8a0800b5
+ 008e8fc8 bytes 8a0800b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e3a259cceb5721dae9117db298b7e9"></a>

### [`008b52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b52e0.md) → [`008e9184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md) FUN_008e9184

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008e9190",
      "incomplete_value": false,
      "site": "008e9190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b52ec",
      "incomplete_value": false,
      "site": "008b52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "008e9190",
      "DATA",
      [
        "storage",
        "00c06f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9190",
      "DATA",
      [
        "storage",
        "00c84ce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b52e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b52e0.md#insn-008b52e4) · [`008b52e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b52e0.md#insn-008b52e8)
- 新版 [`008e9188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md#insn-008e9188) · [`008e918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9184.md#insn-008e918c)

~~~diff
- 008b52e4 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008e9188 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008b52e4 bytes 891a00b0
+ 008e9188 bytes c91c00f0
- 008b52e8 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 008b52e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e918c ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 008e918c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e918c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e918c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 bytes 29213c91
+ 008e918c bytes 29813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35db9835097263f4e37495d0c1dbfdfa"></a>

### [`008b5460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5460.md) → [`008e9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md) FUN_008e9304

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008e9310",
      "incomplete_value": false,
      "site": "008e9310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b546c",
      "incomplete_value": false,
      "site": "008b546c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "008e9310",
      "DATA",
      [
        "storage",
        "00c06f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9310",
      "DATA",
      [
        "storage",
        "00c84d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5460.md#insn-008b5464) · [`008b5468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5460.md#insn-008b5468)
- 新版 [`008e9308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md#insn-008e9308) · [`008e930c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9304.md#insn-008e930c)

~~~diff
- 008b5464 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008e9308 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008b5464 bytes 891a00b0
+ 008e9308 bytes c91c00f0
- 008b5468 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 008b5468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e930c ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 008e930c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e930c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e930c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5468 bytes 29213e91
+ 008e930c bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-040c1068356c8bc65d3e0507bdd2c532"></a>

### [`008b5a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5a6c.md) → [`008e9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md) FUN_008e9910

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008e9930",
      "incomplete_value": false,
      "site": "008e9934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5a8c",
      "incomplete_value": false,
      "site": "008b5a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "008e9934",
      "DATA",
      [
        "storage",
        "00c07078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9934",
      "DATA",
      [
        "storage",
        "00c84e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5a6c.md#insn-008b5a80) · [`008b5a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5a6c.md#insn-008b5a88) · [`008b5a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5a6c.md#insn-008b5a8c)
- 新版 [`008e9924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e9924) · [`008e992c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e992c) · [`008e9930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9910.md#insn-008e9930)

~~~diff
- 008b5a80 ["INT_ADD", "register:40f0:8", ["const:8b5a80:8", "const:4:8"]]
- 008b5a80 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e9924 ["INT_ADD", "register:40f0:8", ["const:8e9924:8", "const:4:8"]]
+ 008e9924 ["CALL", null, ["callee:00c57a90:8"]]
- 008b5a80 bytes 70950c94
+ 008e9924 bytes 5bb80d94
- 008b5a88 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008e992c ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008b5a88 bytes 881a00d0
+ 008e992c bytes c81c00f0
- 008b5a8c ["COPY", "tmp:0:8", ["const:78:8"]]
- 008b5a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9930 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 008e9930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c bytes 08e10191
+ 008e9930 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a8c9b6c72c0428c96a92600d9047fd"></a>

### [`008b5ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5ac4.md) → [`008e9968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md) FUN_008e9968

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "008e9990",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b5aec",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008e9990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008e9990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5ac4.md#insn-008b5aec) · [`008b5ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5ac4.md#insn-008b5ae8)
- 新版 [`008e9990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md#insn-008e9990) · [`008e998c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9968.md#insn-008e998c)

~~~diff
- 008b5aec ["INT_ADD", "register:40f0:8", ["const:8b5aec:8", "const:4:8"]]
- 008b5aec ["CALL", null, ["ram:457e1c:8"]]
+ 008e9990 ["INT_ADD", "register:40f0:8", ["const:8e9990:8", "const:4:8"]]
+ 008e9990 ["CALL", null, ["ram:47acb4:8"]]
- 008b5aec bytes cc88ee97
+ 008e9990 bytes c944ee97
- 008b5ae8 ["INT_ADD", "register:40f0:8", ["const:8b5ae8:8", "const:4:8"]]
- 008b5ae8 ["CALL", null, ["callee:008b9134:8"]]
+ 008e998c ["INT_ADD", "register:40f0:8", ["const:8e998c:8", "const:4:8"]]
+ 008e998c ["CALL", null, ["callee:008b9134:8"]]
- 008b5ae8 bytes 2641ff97
+ 008e998c bytes ea3dff97
~~~


<a id="compare-fb52e4e8e3e42b9f3ca1dad3cc385470"></a>

### [`008b5b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5b88.md) → [`008e9a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md) FUN_008e9a2c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "008e9a54",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b5bb0",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008e9a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008e9a54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5b88.md#insn-008b5bb0) · [`008b5bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5b88.md#insn-008b5bac)
- 新版 [`008e9a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md#insn-008e9a54) · [`008e9a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a2c.md#insn-008e9a50)

~~~diff
- 008b5bb0 ["INT_ADD", "register:40f0:8", ["const:8b5bb0:8", "const:4:8"]]
- 008b5bb0 ["CALL", null, ["ram:457e1c:8"]]
+ 008e9a54 ["INT_ADD", "register:40f0:8", ["const:8e9a54:8", "const:4:8"]]
+ 008e9a54 ["CALL", null, ["ram:47acb4:8"]]
- 008b5bb0 bytes 9b88ee97
+ 008e9a54 bytes 9844ee97
- 008b5bac ["INT_ADD", "register:40f0:8", ["const:8b5bac:8", "const:4:8"]]
- 008b5bac ["CALL", null, ["callee:008b9134:8"]]
+ 008e9a50 ["INT_ADD", "register:40f0:8", ["const:8e9a50:8", "const:4:8"]]
+ 008e9a50 ["CALL", null, ["callee:008b9134:8"]]
- 008b5bac bytes f540ff97
+ 008e9a50 bytes b93dff97
~~~


<a id="compare-cdf6be09152e79df9b7a7f25c54411dc"></a>

### [`008b5bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5bf4.md) → [`008e9a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md) FUN_008e9a98

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008e9ab8",
      "incomplete_value": false,
      "site": "008e9abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5c14",
      "incomplete_value": false,
      "site": "008b5c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "008e9abc",
      "DATA",
      [
        "storage",
        "00c07178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9abc",
      "DATA",
      [
        "storage",
        "00c84f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5bf4.md#insn-008b5c08) · [`008b5c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5bf4.md#insn-008b5c10) · [`008b5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5bf4.md#insn-008b5c14)
- 新版 [`008e9aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9aac) · [`008e9ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9ab4) · [`008e9ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9a98.md#insn-008e9ab8)

~~~diff
- 008b5c08 ["INT_ADD", "register:40f0:8", ["const:8b5c08:8", "const:4:8"]]
- 008b5c08 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e9aac ["INT_ADD", "register:40f0:8", ["const:8e9aac:8", "const:4:8"]]
+ 008e9aac ["CALL", null, ["callee:00c57a90:8"]]
- 008b5c08 bytes 0e950c94
+ 008e9aac bytes f9b70d94
- 008b5c10 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008e9ab4 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008b5c10 bytes 881a00d0
+ 008e9ab4 bytes c81c00f0
- 008b5c14 ["COPY", "tmp:0:8", ["const:178:8"]]
- 008b5c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9ab8 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 008e9ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 bytes 08e10591
+ 008e9ab8 bytes 08413d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9527f0c1a63127a8415c16719dd08268"></a>

### [`008b5d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d18.md) → [`008e9bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md) FUN_008e9bbc

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008e9be0",
      "incomplete_value": false,
      "site": "008e9be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d3c",
      "incomplete_value": false,
      "site": "008b5d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "008e9be0",
      "DATA",
      [
        "storage",
        "00c07208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9be0",
      "DATA",
      [
        "storage",
        "00c84fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d18.md#insn-008b5d2c) · [`008b5d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d18.md#insn-008b5d34) · [`008b5d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d18.md#insn-008b5d38)
- 新版 [`008e9bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bd0) · [`008e9bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bd8) · [`008e9bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bbc.md#insn-008e9bdc)

~~~diff
- 008b5d2c ["INT_ADD", "register:40f0:8", ["const:8b5d2c:8", "const:4:8"]]
- 008b5d2c ["CALL", null, ["callee:00c57a90:8"]]
+ 008e9bd0 ["INT_ADD", "register:40f0:8", ["const:8e9bd0:8", "const:4:8"]]
+ 008e9bd0 ["CALL", null, ["callee:00c57a90:8"]]
- 008b5d2c bytes c5940c94
+ 008e9bd0 bytes b0b70d94
- 008b5d34 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008e9bd8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008b5d34 bytes 881a00d0
+ 008e9bd8 bytes c81c00f0
- 008b5d38 ["COPY", "tmp:0:8", ["const:208:8"]]
- 008b5d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9bdc ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 008e9bdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9bdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9bdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 bytes 08210891
+ 008e9bdc bytes 08813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99c91dc335e295475f4f60a5eabd8d20"></a>

### [`008b5d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d4c.md) → [`008e9bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md) FUN_008e9bf0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008e9bfc",
      "incomplete_value": false,
      "site": "008e9bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d58",
      "incomplete_value": false,
      "site": "008b5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "008e9bfc",
      "DATA",
      [
        "storage",
        "00c07208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9bfc",
      "DATA",
      [
        "storage",
        "00c84fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d4c.md#insn-008b5d50) · [`008b5d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d4c.md#insn-008b5d54)
- 新版 [`008e9bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md#insn-008e9bf4) · [`008e9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9bf0.md#insn-008e9bf8)

~~~diff
- 008b5d50 ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008e9bf4 ["COPY", "register:4048:8", ["const:c84000:8"]]
- 008b5d50 bytes 891a00d0
+ 008e9bf4 bytes c91c00f0
- 008b5d54 ["COPY", "tmp:0:8", ["const:208:8"]]
- 008b5d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008e9bf8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 008e9bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008e9bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 bytes 29210891
+ 008e9bf8 bytes 29813f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff23a3ca00c9cd38940120db3aab30c0"></a>

### [`008b60b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60b4.md) → [`008e9f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md) FUN_008e9f58

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008e9f7c",
      "incomplete_value": false,
      "site": "008e9f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b60d8",
      "incomplete_value": false,
      "site": "008b60d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "008e9f7c",
      "DATA",
      [
        "storage",
        "00c07278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e9f7c",
      "DATA",
      [
        "storage",
        "00c85050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b60c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60b4.md#insn-008b60c8) · [`008b60d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60b4.md#insn-008b60d0) · [`008b60d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60b4.md#insn-008b60d4)
- 新版 [`008e9f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md#insn-008e9f6c) · [`008e9f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md#insn-008e9f74) · [`008e9f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9f58.md#insn-008e9f78)

~~~diff
- 008b60c8 ["INT_ADD", "register:40f0:8", ["const:8b60c8:8", "const:4:8"]]
- 008b60c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 008e9f6c ["INT_ADD", "register:40f0:8", ["const:8e9f6c:8", "const:4:8"]]
+ 008e9f6c ["CALL", null, ["callee:00c57a90:8"]]
- 008b60c8 bytes de930c94
+ 008e9f6c bytes c9b60d94
- 008b60d0 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008e9f74 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b60d0 bytes 881a00b0
+ 008e9f74 bytes e81c0090
- 008b60d4 ["COPY", "tmp:0:8", ["const:278:8"]]
- 008b60d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e9f78 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 008e9f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e9f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 bytes 08e10991
+ 008e9f78 bytes 08410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-686c7220546f7d78dd5f86e46a0c5fbe"></a>

### [`008b6104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6104.md) → [`008e9fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md) FUN_008e9fa8

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "008e9fd0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b612c",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008e9fd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008e9fd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b612c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6104.md#insn-008b612c) · [`008b6128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6104.md#insn-008b6128)
- 新版 [`008e9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md#insn-008e9fd0) · [`008e9fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9fa8.md#insn-008e9fcc)

~~~diff
- 008b612c ["INT_ADD", "register:40f0:8", ["const:8b612c:8", "const:4:8"]]
- 008b612c ["CALL", null, ["ram:457e1c:8"]]
+ 008e9fd0 ["INT_ADD", "register:40f0:8", ["const:8e9fd0:8", "const:4:8"]]
+ 008e9fd0 ["CALL", null, ["ram:47acb4:8"]]
- 008b612c bytes 3c87ee97
+ 008e9fd0 bytes 3943ee97
- 008b6128 ["INT_ADD", "register:40f0:8", ["const:8b6128:8", "const:4:8"]]
- 008b6128 ["CALL", null, ["callee:008b9134:8"]]
+ 008e9fcc ["INT_ADD", "register:40f0:8", ["const:8e9fcc:8", "const:4:8"]]
+ 008e9fcc ["CALL", null, ["callee:008b9134:8"]]
- 008b6128 bytes 963fff97
+ 008e9fcc bytes 5a3cff97
~~~


<a id="compare-fe151f7c22f4959c28ff86d3d3059a17"></a>

### [`008b6170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6170.md) → [`008ea014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md) FUN_008ea014

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea038",
      "incomplete_value": false,
      "site": "008ea038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6194",
      "incomplete_value": false,
      "site": "008b6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "008ea038",
      "DATA",
      [
        "storage",
        "00c072f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea038",
      "DATA",
      [
        "storage",
        "00c850d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6170.md#insn-008b6184) · [`008b618c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6170.md#insn-008b618c) · [`008b6190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6170.md#insn-008b6190)
- 新版 [`008ea028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md#insn-008ea028) · [`008ea030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md#insn-008ea030) · [`008ea034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea014.md#insn-008ea034)

~~~diff
- 008b6184 ["INT_ADD", "register:40f0:8", ["const:8b6184:8", "const:4:8"]]
- 008b6184 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea028 ["INT_ADD", "register:40f0:8", ["const:8ea028:8", "const:4:8"]]
+ 008ea028 ["CALL", null, ["callee:00c57a90:8"]]
- 008b6184 bytes af930c94
+ 008ea028 bytes 9ab60d94
- 008b618c ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea030 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b618c bytes 881a00b0
+ 008ea030 bytes c81c00f0
- 008b6190 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 008b6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea034 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 008ea034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6190 bytes 08e10b91
+ 008ea034 bytes 08410391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25810276dc7f83040e077fa5c7686897"></a>

### [`008b61c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b61c0.md) → [`008ea064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md) FUN_008ea064

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "008ea08c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b61e8",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008ea08c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008ea08c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b61e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b61c0.md#insn-008b61e8) · [`008b61e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b61c0.md#insn-008b61e4)
- 新版 [`008ea08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md#insn-008ea08c) · [`008ea088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea064.md#insn-008ea088)

~~~diff
- 008b61e8 ["INT_ADD", "register:40f0:8", ["const:8b61e8:8", "const:4:8"]]
- 008b61e8 ["CALL", null, ["ram:457e1c:8"]]
+ 008ea08c ["INT_ADD", "register:40f0:8", ["const:8ea08c:8", "const:4:8"]]
+ 008ea08c ["CALL", null, ["ram:47acb4:8"]]
- 008b61e8 bytes 0d87ee97
+ 008ea08c bytes 0a43ee97
- 008b61e4 ["INT_ADD", "register:40f0:8", ["const:8b61e4:8", "const:4:8"]]
- 008b61e4 ["CALL", null, ["callee:008b9134:8"]]
+ 008ea088 ["INT_ADD", "register:40f0:8", ["const:8ea088:8", "const:4:8"]]
+ 008ea088 ["CALL", null, ["callee:008b9134:8"]]
- 008b61e4 bytes 673fff97
+ 008ea088 bytes 2b3cff97
~~~


<a id="compare-041235ec555887c74121c8ca0dcaa92d"></a>

### [`008b622c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b622c.md) → [`008ea0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md) FUN_008ea0d0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea0f4",
      "incomplete_value": false,
      "site": "008ea0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6250",
      "incomplete_value": false,
      "site": "008b6250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "008ea0f4",
      "DATA",
      [
        "storage",
        "00c07378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea0f4",
      "DATA",
      [
        "storage",
        "00c85150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b622c.md#insn-008b6240) · [`008b6248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b622c.md#insn-008b6248) · [`008b624c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b622c.md#insn-008b624c)
- 新版 [`008ea0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md#insn-008ea0e4) · [`008ea0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md#insn-008ea0ec) · [`008ea0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea0d0.md#insn-008ea0f0)

~~~diff
- 008b6240 ["INT_ADD", "register:40f0:8", ["const:8b6240:8", "const:4:8"]]
- 008b6240 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea0e4 ["INT_ADD", "register:40f0:8", ["const:8ea0e4:8", "const:4:8"]]
+ 008ea0e4 ["CALL", null, ["callee:00c57a90:8"]]
- 008b6240 bytes 80930c94
+ 008ea0e4 bytes 6bb60d94
- 008b6248 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea0ec ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b6248 bytes 881a00b0
+ 008ea0ec bytes c81c00f0
- 008b624c ["COPY", "tmp:0:8", ["const:378:8"]]
- 008b624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea0f0 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 008ea0f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea0f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea0f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b624c bytes 08e10d91
+ 008ea0f0 bytes 08410591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2226e7ec18dd1a3328a4394e5434bc"></a>

### [`008b6750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6750.md) → [`008ea5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md) FUN_008ea5f4

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea618",
      "incomplete_value": false,
      "site": "008ea618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6774",
      "incomplete_value": false,
      "site": "008b6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "008ea618",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea618",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6750.md#insn-008b6764) · [`008b676c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6750.md#insn-008b676c) · [`008b6770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6750.md#insn-008b6770)
- 新版 [`008ea608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md#insn-008ea608) · [`008ea610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md#insn-008ea610) · [`008ea614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea5f4.md#insn-008ea614)

~~~diff
- 008b6764 ["INT_ADD", "register:40f0:8", ["const:8b6764:8", "const:4:8"]]
- 008b6764 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea608 ["INT_ADD", "register:40f0:8", ["const:8ea608:8", "const:4:8"]]
+ 008ea608 ["CALL", null, ["callee:00c57a90:8"]]
- 008b6764 bytes 37920c94
+ 008ea608 bytes 22b50d94
- 008b676c ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea610 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b676c bytes 881a00b0
+ 008ea610 bytes c81c00f0
- 008b6770 ["COPY", "tmp:0:8", ["const:408:8"]]
- 008b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea614 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 008ea614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6770 bytes 08211091
+ 008ea614 bytes 08810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-519de05461ce45e49f873d4a294a9d4a"></a>

### [`008b6784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6784.md) → [`008ea628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea628.md) FUN_008ea628

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ea634",
      "incomplete_value": false,
      "site": "008ea634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6790",
      "incomplete_value": false,
      "site": "008b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "008ea634",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea634",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6784.md#insn-008b6788) · [`008b678c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6784.md#insn-008b678c)
- 新版 [`008ea62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea628.md#insn-008ea62c) · [`008ea630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea628.md#insn-008ea630)

~~~diff
- 008b6788 ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008ea62c ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008b6788 bytes 891a00b0
+ 008ea62c bytes c91c00f0
- 008b678c ["COPY", "tmp:0:8", ["const:408:8"]]
- 008b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea630 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 008ea630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b678c bytes 29211091
+ 008ea630 bytes 29810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0692875515ff681015e140420eb3d0ab"></a>

### [`008b67a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b67a0.md) → [`008ea644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md) FUN_008ea644

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "008ea668",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b67c4",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008ea668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008ea668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b67c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b67a0.md#insn-008b67c4) · [`008b67c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b67a0.md#insn-008b67c0)
- 新版 [`008ea668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md#insn-008ea668) · [`008ea664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea644.md#insn-008ea664)

~~~diff
- 008b67c4 ["INT_ADD", "register:40f0:8", ["const:8b67c4:8", "const:4:8"]]
- 008b67c4 ["CALL", null, ["ram:457e1c:8"]]
+ 008ea668 ["INT_ADD", "register:40f0:8", ["const:8ea668:8", "const:4:8"]]
+ 008ea668 ["CALL", null, ["ram:47acb4:8"]]
- 008b67c4 bytes 9685ee97
+ 008ea668 bytes 9341ee97
- 008b67c0 ["INT_ADD", "register:40f0:8", ["const:8b67c0:8", "const:4:8"]]
- 008b67c0 ["CALL", null, ["callee:008b9134:8"]]
+ 008ea664 ["INT_ADD", "register:40f0:8", ["const:8ea664:8", "const:4:8"]]
+ 008ea664 ["CALL", null, ["callee:008b9134:8"]]
- 008b67c0 bytes f03dff97
+ 008ea664 bytes b43aff97
~~~


<a id="compare-928f8bfde702636a9df87d0c050c44d0"></a>

### [`008b6814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6814.md) → [`008ea6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md) FUN_008ea6b8

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea6dc",
      "incomplete_value": false,
      "site": "008ea6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6838",
      "incomplete_value": false,
      "site": "008b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "008ea6dc",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea6dc",
      "DATA",
      [
        "storage",
        "00c85260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6814.md#insn-008b6828) · [`008b6830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6814.md#insn-008b6830) · [`008b6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6814.md#insn-008b6834)
- 新版 [`008ea6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md#insn-008ea6cc) · [`008ea6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md#insn-008ea6d4) · [`008ea6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6b8.md#insn-008ea6d8)

~~~diff
- 008b6828 ["INT_ADD", "register:40f0:8", ["const:8b6828:8", "const:4:8"]]
- 008b6828 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea6cc ["INT_ADD", "register:40f0:8", ["const:8ea6cc:8", "const:4:8"]]
+ 008ea6cc ["CALL", null, ["callee:00c57a90:8"]]
- 008b6828 bytes 06920c94
+ 008ea6cc bytes f1b40d94
- 008b6830 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea6d4 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b6830 bytes 881a00b0
+ 008ea6d4 bytes c81c00f0
- 008b6834 ["COPY", "tmp:0:8", ["const:488:8"]]
- 008b6834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea6d8 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 008ea6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6834 bytes 08211291
+ 008ea6d8 bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d40a3fd36c31f11ebdc46242edbb0bb"></a>

### [`008b6848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6848.md) → [`008ea6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6ec.md) FUN_008ea6ec

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ea6f8",
      "incomplete_value": false,
      "site": "008ea6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6854",
      "incomplete_value": false,
      "site": "008b6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "008ea6f8",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea6f8",
      "DATA",
      [
        "storage",
        "00c85260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b684c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6848.md#insn-008b684c) · [`008b6850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6848.md#insn-008b6850)
- 新版 [`008ea6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6ec.md#insn-008ea6f0) · [`008ea6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea6ec.md#insn-008ea6f4)

~~~diff
- 008b684c ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008ea6f0 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008b684c bytes 891a00b0
+ 008ea6f0 bytes c91c00f0
- 008b6850 ["COPY", "tmp:0:8", ["const:488:8"]]
- 008b6850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea6f4 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 008ea6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6850 bytes 29211291
+ 008ea6f4 bytes 29810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ff20ce6aed2411e506ba3c68f3874d6"></a>

### [`008b6864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6864.md) → [`008ea708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md) FUN_008ea708

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "008ea72c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b6888",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008ea72c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008ea72c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6864.md#insn-008b6888) · [`008b6884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6864.md#insn-008b6884)
- 新版 [`008ea72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md#insn-008ea72c) · [`008ea728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea708.md#insn-008ea728)

~~~diff
- 008b6888 ["INT_ADD", "register:40f0:8", ["const:8b6888:8", "const:4:8"]]
- 008b6888 ["CALL", null, ["ram:457e1c:8"]]
+ 008ea72c ["INT_ADD", "register:40f0:8", ["const:8ea72c:8", "const:4:8"]]
+ 008ea72c ["CALL", null, ["ram:47acb4:8"]]
- 008b6888 bytes 6585ee97
+ 008ea72c bytes 6241ee97
- 008b6884 ["INT_ADD", "register:40f0:8", ["const:8b6884:8", "const:4:8"]]
- 008b6884 ["CALL", null, ["callee:008b9134:8"]]
+ 008ea728 ["INT_ADD", "register:40f0:8", ["const:8ea728:8", "const:4:8"]]
+ 008ea728 ["CALL", null, ["callee:008b9134:8"]]
- 008b6884 bytes bf3dff97
+ 008ea728 bytes 833aff97
~~~


<a id="compare-b4b382cc08adedc6519f64824509ed4a"></a>

### [`008b6908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6908.md) → [`008ea7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md) FUN_008ea7ac

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea7d0",
      "incomplete_value": false,
      "site": "008ea7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b692c",
      "incomplete_value": false,
      "site": "008b692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "008ea7d0",
      "DATA",
      [
        "storage",
        "00c07508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea7d0",
      "DATA",
      [
        "storage",
        "00c852e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b691c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6908.md#insn-008b691c) · [`008b6924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6908.md#insn-008b6924) · [`008b6928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6908.md#insn-008b6928)
- 新版 [`008ea7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md#insn-008ea7c0) · [`008ea7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md#insn-008ea7c8) · [`008ea7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7ac.md#insn-008ea7cc)

~~~diff
- 008b691c ["INT_ADD", "register:40f0:8", ["const:8b691c:8", "const:4:8"]]
- 008b691c ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea7c0 ["INT_ADD", "register:40f0:8", ["const:8ea7c0:8", "const:4:8"]]
+ 008ea7c0 ["CALL", null, ["callee:00c57a90:8"]]
- 008b691c bytes c9910c94
+ 008ea7c0 bytes b4b40d94
- 008b6924 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea7c8 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b6924 bytes 881a00b0
+ 008ea7c8 bytes c81c00f0
- 008b6928 ["COPY", "tmp:0:8", ["const:508:8"]]
- 008b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea7cc ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 008ea7cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea7cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea7cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6928 bytes 08211491
+ 008ea7cc bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2411275e4ef3a92dfaf400fd58a14d75"></a>

### [`008b693c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b693c.md) → [`008ea7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7e0.md) FUN_008ea7e0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ea7ec",
      "incomplete_value": false,
      "site": "008ea7ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6948",
      "incomplete_value": false,
      "site": "008b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "008ea7ec",
      "DATA",
      [
        "storage",
        "00c07508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea7ec",
      "DATA",
      [
        "storage",
        "00c852e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b693c.md#insn-008b6940) · [`008b6944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b693c.md#insn-008b6944)
- 新版 [`008ea7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7e0.md#insn-008ea7e4) · [`008ea7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7e0.md#insn-008ea7e8)

~~~diff
- 008b6940 ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008ea7e4 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008b6940 bytes 891a00b0
+ 008ea7e4 bytes c91c00f0
- 008b6944 ["COPY", "tmp:0:8", ["const:508:8"]]
- 008b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea7e8 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 008ea7e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea7e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea7e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6944 bytes 29211491
+ 008ea7e8 bytes 29810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d2899c43a7f746d4e1339b03bd4dc0"></a>

### [`008b6958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6958.md) → [`008ea7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md) FUN_008ea7fc

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "008ea818",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b6974",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008ea818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008ea818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6958.md#insn-008b6974) · [`008b6970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6958.md#insn-008b6970)
- 新版 [`008ea818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md#insn-008ea818) · [`008ea814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea7fc.md#insn-008ea814)

~~~diff
- 008b6974 ["INT_ADD", "register:40f0:8", ["const:8b6974:8", "const:4:8"]]
- 008b6974 ["CALL", null, ["ram:457e1c:8"]]
+ 008ea818 ["INT_ADD", "register:40f0:8", ["const:8ea818:8", "const:4:8"]]
+ 008ea818 ["CALL", null, ["ram:47acb4:8"]]
- 008b6974 bytes 2a85ee97
+ 008ea818 bytes 2741ee97
- 008b6970 ["INT_ADD", "register:40f0:8", ["const:8b6970:8", "const:4:8"]]
- 008b6970 ["CALL", null, ["callee:008b9134:8"]]
+ 008ea814 ["INT_ADD", "register:40f0:8", ["const:8ea814:8", "const:4:8"]]
+ 008ea814 ["CALL", null, ["callee:008b9134:8"]]
- 008b6970 bytes 843dff97
+ 008ea814 bytes 483aff97
~~~


<a id="compare-f4a877417bb7a49189c25405ef284948"></a>

### [`008b69b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69b8.md) → [`008ea85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md) FUN_008ea85c

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ea880",
      "incomplete_value": false,
      "site": "008ea880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69dc",
      "incomplete_value": false,
      "site": "008b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "008ea880",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea880",
      "DATA",
      [
        "storage",
        "00c85360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69b8.md#insn-008b69cc) · [`008b69d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69b8.md#insn-008b69d4) · [`008b69d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69b8.md#insn-008b69d8)
- 新版 [`008ea870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md#insn-008ea870) · [`008ea878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md#insn-008ea878) · [`008ea87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea85c.md#insn-008ea87c)

~~~diff
- 008b69cc ["INT_ADD", "register:40f0:8", ["const:8b69cc:8", "const:4:8"]]
- 008b69cc ["CALL", null, ["callee:00c57a90:8"]]
+ 008ea870 ["INT_ADD", "register:40f0:8", ["const:8ea870:8", "const:4:8"]]
+ 008ea870 ["CALL", null, ["callee:00c57a90:8"]]
- 008b69cc bytes 9d910c94
+ 008ea870 bytes 88b40d94
- 008b69d4 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ea878 ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b69d4 bytes 881a00b0
+ 008ea878 bytes c81c00f0
- 008b69d8 ["COPY", "tmp:0:8", ["const:588:8"]]
- 008b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea87c ["COPY", "tmp:0:8", ["const:360:8"]]
+ 008ea87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 bytes 08211691
+ 008ea87c bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8484a0fa30c745e20d5c24a0824fd1e"></a>

### [`008b69ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69ec.md) → [`008ea890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea890.md) FUN_008ea890

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ea89c",
      "incomplete_value": false,
      "site": "008ea89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69f8",
      "incomplete_value": false,
      "site": "008b69f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "008ea89c",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea89c",
      "DATA",
      [
        "storage",
        "00c85360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69ec.md#insn-008b69f0) · [`008b69f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69ec.md#insn-008b69f4)
- 新版 [`008ea894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea890.md#insn-008ea894) · [`008ea898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea890.md#insn-008ea898)

~~~diff
- 008b69f0 ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008ea894 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008b69f0 bytes 891a00b0
+ 008ea894 bytes c91c00f0
- 008b69f4 ["COPY", "tmp:0:8", ["const:588:8"]]
- 008b69f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea898 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 008ea898 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea898 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea898 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 bytes 29211691
+ 008ea898 bytes 29810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e24fd2bda56800c9315e8090dd7888"></a>

### [`008b6a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6a08.md) → [`008ea8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md) FUN_008ea8ac

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.69% / 新版 94.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ea994",
      "incomplete_value": true,
      "site": "008ea9ac",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:5f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6af0",
      "incomplete_value": true,
      "site": "008b6b08",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:93d:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008eaa84",
      "incomplete_value": false,
      "site": "008eaa84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6be0",
      "incomplete_value": false,
      "site": "008b6be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea8f0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b6a4c",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "008ea8f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "008ea974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "008ea994",
      "READ",
      [
        "storage",
        "002a893d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ea8f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008ea974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "008ea994",
      "READ",
      [
        "storage",
        "002b95f8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6a08.md#insn-008b6a4c) · [`008b6ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6a08.md#insn-008b6ad0) · [`008b6b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6a08.md#insn-008b6b24)
- 新版 [`008ea8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea8f0) · [`008ea974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea974) · [`008ea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ea8ac.md#insn-008ea9c8)

~~~diff
- 008b6a4c ["INT_ADD", "register:40f0:8", ["const:8b6a4c:8", "const:4:8"]]
- 008b6a4c ["CALL", null, ["ram:457e1c:8"]]
+ 008ea8f0 ["INT_ADD", "register:40f0:8", ["const:8ea8f0:8", "const:4:8"]]
+ 008ea8f0 ["CALL", null, ["ram:47acb4:8"]]
- 008b6a4c bytes f484ee97
+ 008ea8f0 bytes f140ee97
- 008b6ad0 ["INT_ADD", "register:40f0:8", ["const:8b6ad0:8", "const:4:8"]]
- 008b6ad0 ["CALL", null, ["ram:457e1c:8"]]
+ 008ea974 ["INT_ADD", "register:40f0:8", ["const:8ea974:8", "const:4:8"]]
+ 008ea974 ["CALL", null, ["ram:47acb4:8"]]
- 008b6ad0 bytes d384ee97
+ 008ea974 bytes d040ee97
- 008b6b24 ["INT_ADD", "register:40f0:8", ["const:8b6b24:8", "const:4:8"]]
- 008b6b24 ["CALL", null, ["ram:6f4c58:8"]]
+ 008ea9c8 ["INT_ADD", "register:40f0:8", ["const:8ea9c8:8", "const:4:8"]]
+ 008ea9c8 ["CALL", null, ["ram:71ecc0:8"]]
- 008b6b24 bytes 4df8f897
+ 008ea9c8 bytes bed0f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7d8968b98b257c0430c714b205a0b4"></a>

### [`008b6e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6e8c.md) → [`008ead30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md) FUN_008ead30

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "008ead54",
      "incomplete_value": false,
      "site": "008ead54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6eb0",
      "incomplete_value": false,
      "site": "008b6eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "008ead54",
      "DATA",
      [
        "storage",
        "00c075f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ead54",
      "DATA",
      [
        "storage",
        "00c853d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6e8c.md#insn-008b6ea0) · [`008b6ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6e8c.md#insn-008b6ea8) · [`008b6eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6e8c.md#insn-008b6eac)
- 新版 [`008ead44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md#insn-008ead44) · [`008ead4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md#insn-008ead4c) · [`008ead50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead30.md#insn-008ead50)

~~~diff
- 008b6ea0 ["INT_ADD", "register:40f0:8", ["const:8b6ea0:8", "const:4:8"]]
- 008b6ea0 ["CALL", null, ["callee:00c57a90:8"]]
+ 008ead44 ["INT_ADD", "register:40f0:8", ["const:8ead44:8", "const:4:8"]]
+ 008ead44 ["CALL", null, ["callee:00c57a90:8"]]
- 008b6ea0 bytes 68900c94
+ 008ead44 bytes 53b30d94
- 008b6ea8 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ead4c ["COPY", "register:4040:8", ["const:c85000:8"]]
- 008b6ea8 bytes 881a00b0
+ 008ead4c bytes c81c00f0
- 008b6eac ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008b6eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ead50 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 008ead50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ead50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ead50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6eac bytes 08e11791
+ 008ead50 bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bb7ecf042a64fcc897f9e755cdcb1d2"></a>

### [`008b6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6ec0.md) → [`008ead64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead64.md) FUN_008ead64

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ead70",
      "incomplete_value": false,
      "site": "008ead70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6ecc",
      "incomplete_value": false,
      "site": "008b6ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "008ead70",
      "DATA",
      [
        "storage",
        "00c075f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ead70",
      "DATA",
      [
        "storage",
        "00c853d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6ec0.md#insn-008b6ec4) · [`008b6ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6ec0.md#insn-008b6ec8)
- 新版 [`008ead68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead64.md#insn-008ead68) · [`008ead6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead64.md#insn-008ead6c)

~~~diff
- 008b6ec4 ["COPY", "register:4048:8", ["const:c07000:8"]]
+ 008ead68 ["COPY", "register:4048:8", ["const:c85000:8"]]
- 008b6ec4 bytes 891a00b0
+ 008ead68 bytes c91c00f0
- 008b6ec8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 008b6ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ead6c ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 008ead6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ead6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ead6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 bytes 29e11791
+ 008ead6c bytes 29410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f150eafc9b069dba203781a4b0c849"></a>

### [`008b6edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6edc.md) → [`008ead80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead80.md) FUN_008ead80

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ead88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6ef8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b6ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eadb0"
      ]
    ],
    [
      "unmatched:008b6ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "008ead88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eadb0"
      ]
    ],
    [
      "008ead9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6edc.md#insn-008b6ee4) · [`008b6ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6edc.md#insn-008b6ef8)
- 新版 [`008ead88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008ead80.md#insn-008ead88)

~~~diff
- 008b6ee4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008b6ee4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008b6ee4 bytes 41010054
- 008b6ef8 ["INT_ADD", "register:40f0:8", ["const:8b6ef8:8", "const:4:8"]]
- 008b6ef8 ["CALL", null, ["ram:457e1c:8"]]
- 008b6ef8 bytes c983ee97
+ 008ead88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008ead88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008ead88 bytes 41010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f67bacd9c6c12df4582af25b20670c0"></a>

### [`008b6f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f3c.md) → [`008eade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md) FUN_008eade0

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b6f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b6f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b6f60",
      "DATA",
      [
        "storage",
        "00c07688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eade0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008eade4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008eae04",
      "DATA",
      [
        "storage",
        "00c85460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f3c.md#insn-008b6f3c) · [`008b6f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f3c.md#insn-008b6f40) · [`008b6f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f3c.md#insn-008b6f50)
- 新版 [`008eadf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eade0.md#insn-008eadf4)

~~~diff
- 008b6f3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008b6f3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008b6f3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008b6f3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008b6f3c bytes fd7bbea9
- 008b6f40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008b6f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008b6f40 bytes f30b00f9
- 008b6f50 ["INT_ADD", "register:40f0:8", ["const:8b6f50:8", "const:4:8"]]
- 008b6f50 ["CALL", null, ["callee:00c57a90:8"]]
+ 008eadf4 ["INT_ADD", "register:40f0:8", ["const:8eadf4:8", "const:4:8"]]
+ 008eadf4 ["CALL", null, ["callee:00c57a90:8"]]
- 008b6f50 bytes 3c900c94
+ 008eadf4 bytes 27b30d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e04e83c1b009ca86c426fd9259ac6471"></a>

### [`008b6f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f8c.md) → [`008eae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md) FUN_008eae30

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008eae68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008eae70",
      "incomplete_value": false,
      "site": "008eae84",
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
    "old": {
      "definition_site": "008b6fcc",
      "incomplete_value": false,
      "site": "008b6fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "unmatched:008b6fc0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008b6fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eaea0"
      ]
    ],
    [
      "unmatched:008b6fcc",
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
      "008eae64",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008eae68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eaea0"
      ]
    ],
    [
      "008eae70",
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

- 旧版 [`008b6fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f8c.md#insn-008b6fc4) · [`008b6fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f8c.md#insn-008b6fe0) · [`008b7050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f8c.md#insn-008b7050)
- 新版 [`008eae84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md#insn-008eae84) · [`008eaef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md#insn-008eaef4)

~~~diff
- 008b6fc4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008b6fc4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008b6fc4 bytes c80100b4
- 008b6fe0 ["INT_ADD", "register:40f0:8", ["const:8b6fe0:8", "const:4:8"]]
- 008b6fe0 ["CALL", null, ["callee:00c58210:8"]]
+ 008eae84 ["INT_ADD", "register:40f0:8", ["const:8eae84:8", "const:4:8"]]
+ 008eae84 ["CALL", null, ["callee:00c58210:8"]]
- 008b6fe0 bytes f8910c94
+ 008eae84 bytes e3b40d94
- 008b7050 ["INT_ADD", "register:40f0:8", ["const:8b7050:8", "const:4:8"]]
- 008b7050 ["CALL", null, ["callee:00a82908:8"]]
+ 008eaef4 ["INT_ADD", "register:40f0:8", ["const:8eaef4:8", "const:4:8"]]
+ 008eaef4 ["CALL", null, ["callee:00a82908:8"]]
- 008b7050 bytes 8ab60594
+ 008eaef4 bytes 855e0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f96cda870fe472b96d863b97bacc7db"></a>

### [`008b70b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b70b8.md) → [`008eaf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eaf5c.md) _INIT_174

採用 · 移動量 `+0x33ea4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.53% / 新版 78.53%

CFGの説明率　旧版 41.03% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b70e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b711c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b70e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b70f4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008b7110",
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
      "008eaf8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008eaf98",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "008eafb4",
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

- 旧版 [`008b70e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b70b8.md#insn-008b70e8) · [`008b7110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b70b8.md#insn-008b7110) · [`008b711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b70b8.md#insn-008b711c)

~~~diff
- 008b70e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008b70e8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008b70e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008b70e8 bytes a9831ff8
- 008b7110 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008b7110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008b7110 bytes e013813c
- 008b711c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008b711c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 008b711c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008b711c bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75bbebb26933e60e8cd199f915e02896"></a>

### [`008b7448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md) → [`008eb2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md) FUN_008eb2ec

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ae96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae96c.md) · 呼出先 2件 [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) [`008b7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7948.md)
- 新版 呼出元 1件 [`006d8728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8728.md) · 呼出先 2件 [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) [`008eb7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 81.25% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b74a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eb370",
      "incomplete_value": true,
      "site": "008eb370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:214:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b74cc",
      "incomplete_value": true,
      "site": "008b74cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:72c:8"
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
    "new": {
      "site": "008eb348"
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
      "008eb328",
      "READ",
      [
        "storage",
        "00c24728",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:008b74a4",
      "WRITE",
      [
        "storage",
        "00c24728",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:008b74a8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb374"
      ]
    ]
  ],
  "added": [
    [
      "008eb328",
      "READ",
      [
        "storage",
        "00ca4210",
        null,
        "undefined4"
      ]
    ],
    [
      "008eb348",
      "WRITE",
      [
        "storage",
        "00ca4210",
        null,
        "undefined4"
      ]
    ],
    [
      "008eb34c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008eb374"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b74a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md#insn-008b74a4) · [`008b74c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md#insn-008b74c4) · [`008b74cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md#insn-008b74cc)
- 新版 [`008eb368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md#insn-008eb368) · [`008eb370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md#insn-008eb370)

~~~diff
- 008b74a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
- 008b74a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74a4 bytes 682a07b9
- 008b74c4 ["INT_ADD", "register:40f0:8", ["const:8b74c4:8", "const:4:8"]]
- 008b74c4 ["CALL", null, ["ram:8b7948:8"]]
+ 008eb368 ["INT_ADD", "register:40f0:8", ["const:8eb368:8", "const:4:8"]]
+ 008eb368 ["CALL", null, ["ram:8eb7ec:8"]]
- 008b74c4 bytes 21010094
+ 008eb368 bytes 21010094
- 008b74cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:72c:8"]]
- 008b74cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008eb370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:214:8"]]
+ 008eb370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74cc bytes 682e07b9
+ 008eb370 bytes 681602b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f9dcfecf8d713dca9834871913223c5"></a>

### [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) → [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) FUN_008eb380

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008b7448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md) [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`008be334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md)
- 新版 呼出元 4件 [`008eb2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md) [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 13件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`008f21dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.20% / 新版 91.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008eb5bc",
      "incomplete_value": true,
      "site": "008eb5c8",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:4b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7718",
      "incomplete_value": true,
      "site": "008b7724",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:f18:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eb734",
      "incomplete_value": false,
      "site": "008eb734",
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
                "const:b00:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7890",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eb738",
      "incomplete_value": false,
      "site": "008eb738",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7894",
      "incomplete_value": false,
      "site": "008b7894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008eb42c",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ],
    [
      "008eb46c",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ],
    [
      "008eb5a8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008eb42c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008eb46c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "008eb5a8",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b776c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md#insn-008b776c) · [`008b7868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md#insn-008b7868) · [`008b78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md#insn-008b78a8)
- 新版 [`008eb610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb610) · [`008eb70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb70c) · [`008eb74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md#insn-008eb74c)

~~~diff
- 008b776c ["INT_ADD", "register:40f0:8", ["const:8b776c:8", "const:4:8"]]
- 008b776c ["CALL", null, ["callee:006337a4:8"]]
+ 008eb610 ["INT_ADD", "register:40f0:8", ["const:8eb610:8", "const:4:8"]]
+ 008eb610 ["CALL", null, ["callee:006337a4:8"]]
- 008b776c bytes 5059f597
+ 008eb610 bytes 6520f597
- 008b7868 ["INT_ADD", "register:40f0:8", ["const:8b7868:8", "const:4:8"]]
- 008b7868 ["CALL", null, ["callee:00c57a50:8"]]
+ 008eb70c ["INT_ADD", "register:40f0:8", ["const:8eb70c:8", "const:4:8"]]
+ 008eb70c ["CALL", null, ["callee:00c57a50:8"]]
- 008b7868 bytes e68d0c94
+ 008eb70c bytes d1b00d94
- 008b78a8 ["INT_ADD", "register:40f0:8", ["const:8b78a8:8", "const:4:8"]]
- 008b78a8 ["CALL", null, ["callee:00c57a30:8"]]
+ 008eb74c ["INT_ADD", "register:40f0:8", ["const:8eb74c:8", "const:4:8"]]
+ 008eb74c ["CALL", null, ["callee:00c57a30:8"]]
- 008b78a8 bytes ce8d0c94
+ 008eb74c bytes b9b00d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bde2c6f6702f1283540e46c1e72aaf9"></a>

### [`008b7b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md) → [`008eb9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md) FUN_008eb9dc

採用 · 移動量 `+0x33ea4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 14件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 81.40% / 新版 74.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7bc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b7b94",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008b7b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b7bb0",
      "READ",
      [
        "storage",
        "00295046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008eba38",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "008eba38",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "008eba54",
      "READ",
      [
        "storage",
        "002a4962",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md#insn-008b7b94) · [`008b7bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md#insn-008b7bbc) · [`008b7bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md#insn-008b7bc0)

~~~diff
- 008b7b94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008b7b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008b7b94 bytes e91700f9
- 008b7bbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008b7bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008b7bbc bytes e01300f9
- 008b7bc0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 008b7bc0 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 008b7bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 008b7bc0 bytes 09400079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b89ca0bc28682fcd638c111e8385d5"></a>

### [`008b7e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7e34.md) → [`008ebcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md) FUN_008ebcd8

採用 · 移動量 `+0x33ea4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd560.md) [`007d0e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0e6c.md) [`008c497c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md)
- 新版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`00804034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804034.md) [`008f8850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 86.96% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ebd08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ebd4c",
      "value": [
        "leaf",
        "ram:804034:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008b7ea8",
      "value": [
        "leaf",
        "ram:7d0e6c:8"
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
      "unmatched:008b7e64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebdec"
      ]
    ],
    [
      "008ebd4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007d0e6c"
      ]
    ]
  ],
  "added": [
    [
      "008ebd08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ebdec"
      ]
    ],
    [
      "008ebd4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804034"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7e34.md#insn-008b7e64) · [`008b7ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7e34.md#insn-008b7ea8)
- 新版 [`008ebd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md#insn-008ebd4c) · [`008ebd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md#insn-008ebd08)

~~~diff
- 008b7e64 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 008b7e64 bytes 20070054
- 008b7ea8 ["INT_ADD", "register:40f0:8", ["const:8b7ea8:8", "const:4:8"]]
- 008b7ea8 ["CALL", null, ["ram:7d0e6c:8"]]
+ 008ebd4c ["INT_ADD", "register:40f0:8", ["const:8ebd4c:8", "const:4:8"]]
+ 008ebd4c ["CALL", null, ["ram:804034:8"]]
- 008b7ea8 bytes f163fc97
+ 008ebd4c bytes ba60fc97
+ 008ebd08 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 008ebd08 bytes 20070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-112979173370ee279786db3c9ceb665f"></a>

### [`008b8e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8e1c.md) → [`008eccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md) FUN_008eccc4

採用 · 移動量 `+0x33ea8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.71% / 新版 82.71%

CFGの説明率　旧版 60.49% / 新版 61.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b8fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b8ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b9004"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b8fd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ece94"
      ]
    ],
    [
      "unmatched:008b8ff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ecec8"
      ]
    ],
    [
      "unmatched:008b9000",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ],
  "added": [
    [
      "008ece78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ece94"
      ]
    ],
    [
      "008ece9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ecec8"
      ]
    ],
    [
      "008ecea8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b8e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8e1c.md#insn-008b8e98) · [`008b8f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8e1c.md#insn-008b8f0c) · [`008b8f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8e1c.md#insn-008b8f14)
- 新版 [`008ecdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008eccc4.md#insn-008ecdbc)

~~~diff
- 008b8e98 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b8e98 ["INT_ADD", "register:40f0:8", ["const:8b8e98:8", "const:4:8"]]
- 008b8e98 ["CALLIND", null, ["register:0:8"]]
- 008b8e98 bytes 00013fd6
- 008b8f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 008b8f0c ["INT_ADD", "register:40f0:8", ["const:8b8f0c:8", "const:4:8"]]
- 008b8f0c ["CALLIND", null, ["register:0:8"]]
- 008b8f0c bytes 00013fd6
- 008b8f14 ["INT_ADD", "register:40f0:8", ["const:8b8f14:8", "const:4:8"]]
- 008b8f14 ["CALL", null, ["callee:00c57a80:8"]]
+ 008ecdbc ["INT_ADD", "register:40f0:8", ["const:8ecdbc:8", "const:4:8"]]
+ 008ecdbc ["CALL", null, ["callee:00c57a80:8"]]
- 008b8f14 bytes 47880c94
+ 008ecdbc bytes 31ab0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-919c840962e49c9005fe31f6fbc3b02f"></a>

### [`008bb8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md) → [`008ef76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md) FUN_008ef76c

採用 · 移動量 `+0x33ea8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0069ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab88.md) [`0069bb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069bb8c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 1件 [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`006c0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0eec.md) [`006c1ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c1/006c1ef0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008ef78c",
      "incomplete_value": true,
      "site": "008ef78c",
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
      "definition_site": "008bb8e4",
      "incomplete_value": true,
      "site": "008bb8e4",
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
      "definition_site": "008ef794",
      "incomplete_value": false,
      "site": "008ef7a8",
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
    "old": {
      "definition_site": "008bb8ec",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "008ef79c",
      "incomplete_value": false,
      "site": "008ef7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bb8f4",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ef788",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008ef794",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ef79c",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008ef788",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008ef794",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ef79c",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md#insn-008bb900) · [`008bb928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md#insn-008bb928) · [`008bb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md#insn-008bb930)
- 新版 [`008ef7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md#insn-008ef7a8) · [`008ef7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md#insn-008ef7d0)

~~~diff
- 008bb900 ["INT_ADD", "register:40f0:8", ["const:8bb900:8", "const:4:8"]]
- 008bb900 ["CALL", null, ["callee:00c58210:8"]]
+ 008ef7a8 ["INT_ADD", "register:40f0:8", ["const:8ef7a8:8", "const:4:8"]]
+ 008ef7a8 ["CALL", null, ["callee:00c58210:8"]]
- 008bb900 bytes b07f0c94
+ 008ef7a8 bytes 9aa20d94
- 008bb928 ["INT_ADD", "register:40f0:8", ["const:8bb928:8", "const:4:8"]]
- 008bb928 ["CALL", null, ["ram:449aec:8"]]
+ 008ef7d0 ["INT_ADD", "register:40f0:8", ["const:8ef7d0:8", "const:4:8"]]
+ 008ef7d0 ["CALL", null, ["ram:46c984:8"]]
- 008bb928 bytes 7138ee97
+ 008ef7d0 bytes 6df4ed97
- 008bb930 ["INT_ADD", "register:40f0:8", ["const:8bb930:8", "const:4:8"]]
- 008bb930 ["CALL", null, ["callee:008514b8:8"]]
- 008bb930 bytes 148ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2727f7fc890c5710188515fe8a83a214"></a>

### [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) → [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) FUN_008ef858

採用 · 移動量 `+0x33ea8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c26e0.md) · 呼出先 41件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md)
- 新版 呼出元 1件 [`008f65a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65a4.md) · 呼出先 41件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.70% / 新版 82.70%

CFGの説明率　旧版 57.05% / 新版 51.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `call_target` 14件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 19件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008efb58",
      "incomplete_value": true,
      "site": "008efb5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bbcb0",
      "incomplete_value": true,
      "site": "008bbcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bbd28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bbd6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008bbb14",
      "READ",
      [
        "storage",
        "00c1b730",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008bbb20",
      "DATA",
      [
        "storage",
        "00c240c4",
        null,
        null
      ]
    ],
    [
      "008efac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aa3f64"
      ]
    ]
  ],
  "added": [
    [
      "008ef9bc",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "008ef9c8",
      "DATA",
      [
        "storage",
        "00ca3bac",
        null,
        null
      ]
    ],
    [
      "008efac8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b0376c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bbcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md#insn-008bbcec) · [`008bbcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md#insn-008bbcf4) · [`008bbd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md#insn-008bbd28)

~~~diff
- 008bbcec ["COPY", "tmp:0:4", ["const:0:4"]]
- 008bbcec ["INT_EQUAL", "tmp:1:1", ["register:4040:4", "const:0:4"]]
- 008bbcec ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 008bbcec ["INT_SDIV", "tmp:0:4", ["register:40a0:4", "register:4040:4"]]
- 008bbcec bytes 890ec81a
- 008bbcf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 008bbcf4 ["CBRANCH", null, ["local:b185:8", "tmp:0:1"]]
- 008bbcf4 bytes e8570035
- 008bbd28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:29:8"]]
- 008bbd28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008bbd28 bytes e093823c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f83c63277c14870d210b3adc0000cd"></a>

### [`008bc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md) → [`008f0838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f0/008f0838.md) FUN_008f0838

採用 · 移動量 `+0x33ea8` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c3/008c3e08.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · 呼出先 41件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.53% / 新版 70.53%

CFGの説明率　旧版 22.57% / 新版 24.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 73件, `call_target` 10件, `store_condition` 1件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 67件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bce4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bce54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bce58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f0878",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0884",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f088c",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f0878",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0884",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f088c",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bce4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md#insn-008bce4c) · [`008bce54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md#insn-008bce54) · [`008bce58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md#insn-008bce58)

~~~diff
- 008bce4c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008bce4c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:48:8"]]
- 008bce4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008bce4c bytes e8230139
- 008bce54 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008bce54 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008bce54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:58:8"]]
- 008bce54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008bce54 bytes ff630139
- 008bce58 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008bce58 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:49:8"]]
- 008bce58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008bce58 bytes ea9304f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6896c64dae958116d0f840f3702e18"></a>

### [`008be334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md) → [`008f21dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f21dc.md) FUN_008f21dc

採用 · 移動量 `+0x33ea8` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008c4a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4a54.md)
- 新版 呼出元 1件 [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) · 呼出先 12件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`006662e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/006662e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008f8928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8928.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.14% / 新版 56.14%

CFGの説明率　旧版 8.93% / 新版 8.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008be350"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008be3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008be46c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008be350",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008be3a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f227c"
      ]
    ],
    [
      "unmatched:008be3b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ],
  "added": [
    [
      "008f21f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008f2250",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f227c"
      ]
    ],
    [
      "008f225c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c538e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008be350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md#insn-008be350) · [`008be3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md#insn-008be3a4) · [`008be3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md#insn-008be3a8)

~~~diff
- 008be350 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008be350 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008be350 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008be350 bytes a8831ff8
- 008be3a4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 008be3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008be3a4 bytes 6002803d
- 008be3a8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 008be3a8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008be3a8 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d0a80c03c223aab8165b2a3ca76783"></a>

### [`008c1290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1290.md) → [`008f5150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5150.md) FUN_008f5150

採用 · 移動量 `+0x33ec0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) · 呼出先 3件 [`008c5d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c5/008c5d98.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda00.md)
- 新版 呼出元 1件 [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) · 呼出先 3件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 58.33% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f5184",
      "incomplete_value": true,
      "site": "008f518c",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2:8"
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
      "definition_site": "008f5188",
      "incomplete_value": true,
      "site": "008f518c",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008f51c8",
      "value": [
        "leaf",
        "ram:8f9c6c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008c1308",
      "value": [
        "leaf",
        "ram:8c5d98:8"
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
      "008f5180",
      "READ",
      [
        "storage",
        "00c1b728",
        null,
        "pointer"
      ]
    ],
    [
      "008f5188",
      "PARAM",
      [
        "storage",
        "002fa62d",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "008f51c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008c5d98"
      ]
    ]
  ],
  "added": [
    [
      "008f5180",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "008f5188",
      "PARAM",
      [
        "storage",
        "00310461",
        "_ZSt7nothrow",
        "undefined1"
      ]
    ],
    [
      "008f51c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008f9c6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c12cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1290.md#insn-008c12cc) · [`008c1308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1290.md#insn-008c1308) · [`008c12b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1290.md#insn-008c12b4)
- 新版 [`008f518c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5150.md#insn-008f518c) · [`008f51c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5150.md#insn-008f51c8) · [`008f5174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5150.md#insn-008f5174)

~~~diff
- 008c12cc ["INT_ADD", "register:40f0:8", ["const:8c12cc:8", "const:4:8"]]
- 008c12cc ["CALL", null, ["callee:00c5a450:8"]]
+ 008f518c ["INT_ADD", "register:40f0:8", ["const:8f518c:8", "const:4:8"]]
+ 008f518c ["CALL", null, ["callee:00c5a450:8"]]
- 008c12cc bytes cd710c94
+ 008f518c bytes b1940d94
- 008c1308 ["INT_ADD", "register:40f0:8", ["const:8c1308:8", "const:4:8"]]
- 008c1308 ["CALL", null, ["ram:8c5d98:8"]]
+ 008f51c8 ["INT_ADD", "register:40f0:8", ["const:8f51c8:8", "const:4:8"]]
+ 008f51c8 ["CALL", null, ["ram:8f9c6c:8"]]
- 008c1308 bytes a4120094
+ 008f51c8 bytes a9120094
- 008c12b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008c12b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008f5174 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008f5174 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008c12b4 bytes 8b010054
+ 008f5174 bytes 8b010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e05c64416d76cc6ea44e41e0ebae1b7"></a>

### [`008c1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1a20.md) → [`008f58e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f58e4.md) FUN_008f58e4

採用 · 移動量 `+0x33ec4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) · 呼出先 4件 [`006ae0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae0f8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) · 呼出先 4件 [`006d7eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7eb4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 56.52% / 新版 68.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c1ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008f5974"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f596c",
      "incomplete_value": false,
      "site": "008f5970",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
      ]
    },
    "old": null,
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
      "unmatched:008c1ab0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f5990"
      ]
    ],
    [
      "unmatched:008c1ac0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008f5974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f5990"
      ]
    ],
    [
      "008f5984",
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

- 旧版 [`008c1aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1a20.md#insn-008c1aac) · [`008c1ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1a20.md#insn-008c1ab0) · [`008c1ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1a20.md#insn-008c1ac0)
- 新版 [`008f5970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f58e4.md#insn-008f5970)

~~~diff
- 008c1aac ["INT_ADD", "register:40f0:8", ["const:8c1aac:8", "const:4:8"]]
- 008c1aac ["CALL", null, ["callee:00c538e0:8"]]
+ 008f5970 ["INT_ADD", "register:40f0:8", ["const:8f5970:8", "const:4:8"]]
+ 008f5970 ["CALL", null, ["callee:00c538e0:8"]]
- 008c1aac bytes f9540c94
+ 008f5970 bytes dc770d94
- 008c1ab0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008c1ab0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 008c1ab0 bytes e00000b5
- 008c1ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008c1ac0 ["INT_ADD", "register:40f0:8", ["const:8c1ac0:8", "const:4:8"]]
- 008c1ac0 ["CALLIND", null, ["register:0:8"]]
- 008c1ac0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79bb1bc39fd8db233de594fd9635865c"></a>

### [`008c2284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2284.md) → [`008f6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md) FUN_008f6148

採用 · 移動量 `+0x33ec4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c3/008c3e08.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`008f7cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f7/008f7cdc.md) · 呼出先 14件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.85% / 新版 75.85%

CFGの説明率　旧版 44.64% / 新版 47.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c2358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c23f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c2484"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f617c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008c22c4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:008c22cc",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f617c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008f6188",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f6190",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c22bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2284.md#insn-008c22bc) · [`008c22d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2284.md#insn-008c22d8) · [`008c2358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2284.md#insn-008c2358)
- 新版 [`008f6180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md#insn-008f6180) · [`008f619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md#insn-008f619c)

~~~diff
- 008c22bc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008c22bc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008f6180 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008f6180 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008c22bc bytes 480100b4
+ 008f6180 bytes 480100b4
- 008c22d8 ["INT_ADD", "register:40f0:8", ["const:8c22d8:8", "const:4:8"]]
- 008c22d8 ["CALL", null, ["callee:00c58210:8"]]
+ 008f619c ["INT_ADD", "register:40f0:8", ["const:8f619c:8", "const:4:8"]]
+ 008f619c ["CALL", null, ["callee:00c58210:8"]]
- 008c22d8 bytes 3a650c94
+ 008f619c bytes 1d880d94
- 008c2358 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008c2358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 008c2358 bytes fa0b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a57bb9f9f0db32b31b8f0608a84d8db"></a>

### [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) → [`008f64f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md) FUN_008f64f8

採用 · 移動量 `+0x33ec4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 7件 [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`0069de18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de18.md) [`006a86c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a86c4.md) [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) [`008bb8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md)
- 新版 呼出元 1件 [`008f65c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f65c8.md) · 呼出先 7件 [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`006c417c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c417c.md) [`006d1808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1808.md) [`008ed01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ed/008ed01c.md) [`008ef76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef76c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 83.72% / 新版 83.72%

CFGの説明率　旧版 62.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `call_target` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f6510",
      "incomplete_value": true,
      "site": "008f6510",
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
      "definition_site": "008c264c",
      "incomplete_value": true,
      "site": "008c264c",
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
      "definition_site": "008f6518",
      "incomplete_value": false,
      "site": "008f652c",
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
    "old": {
      "definition_site": "008c2654",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "008f6520",
      "incomplete_value": false,
      "site": "008f652c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c265c",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f650c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008f6518",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f6520",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f650c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "008f6518",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f6520",
      "PARAM",
      [
        "storage",
        "00c854d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md#insn-008c2668) · [`008c2684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md#insn-008c2684) · [`008c26b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md#insn-008c26b0)
- 新版 [`008f652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md#insn-008f652c) · [`008f6548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f64f8.md#insn-008f6548)

~~~diff
- 008c2668 ["INT_ADD", "register:40f0:8", ["const:8c2668:8", "const:4:8"]]
- 008c2668 ["CALL", null, ["callee:00c58210:8"]]
+ 008f652c ["INT_ADD", "register:40f0:8", ["const:8f652c:8", "const:4:8"]]
+ 008f652c ["CALL", null, ["callee:00c58210:8"]]
- 008c2668 bytes 56640c94
+ 008f652c bytes 39870d94
- 008c2684 ["INT_ADD", "register:40f0:8", ["const:8c2684:8", "const:4:8"]]
- 008c2684 ["CALL", null, ["ram:8c1354:8"]]
+ 008f6548 ["INT_ADD", "register:40f0:8", ["const:8f6548:8", "const:4:8"]]
+ 008f6548 ["CALL", null, ["ram:8f5214:8"]]
- 008c2684 bytes 34fbff97
+ 008f6548 bytes 33fbff97
- 008c26b0 ["INT_ADD", "register:40f0:8", ["const:8c26b0:8", "const:4:8"]]
- 008c26b0 ["CALL", null, ["ram:8b9174:8"]]
- 008c26b0 bytes b1daff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f62e13f01dae90f74c679b45ece5ca9"></a>

### [`008c497c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md) → [`008f8850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md) FUN_008f8850

採用 · 移動量 `+0x33ed4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008b7b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md) [`008b7e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7e34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008eb9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb9dc.md) [`008ebcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008ebcd8.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "008f8860",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008c498c",
      "value": [
        "leaf",
        "ram:418c38:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f885c",
      "incomplete_value": false,
      "site": "008f8860",
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
      "definition_site": "008c4988",
      "incomplete_value": false,
      "site": "008c498c",
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
      "008f885c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "008f8860",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "008f885c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "008f8860",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c498c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md#insn-008c498c) · [`008c4984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md#insn-008c4984) · [`008c4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md#insn-008c4988)
- 新版 [`008f8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md#insn-008f8860) · [`008f8858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md#insn-008f8858) · [`008f885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f8/008f8850.md#insn-008f885c)

~~~diff
- 008c498c ["INT_ADD", "register:40f0:8", ["const:8c498c:8", "const:4:8"]]
- 008c498c ["CALL", null, ["ram:418c38:8"]]
+ 008f8860 ["INT_ADD", "register:40f0:8", ["const:8f8860:8", "const:4:8"]]
+ 008f8860 ["CALL", null, ["ram:43b738:8"]]
- 008c498c bytes ab50ed97
+ 008f8860 bytes b60bed97
- 008c4984 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 008f8858 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 008c4984 bytes 00cffff0
+ 008f8858 bytes e0cdfff0
- 008c4988 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 008c4988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008f885c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 008f885c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008f885c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008f885c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008c4988 bytes 00740e91
+ 008f885c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

